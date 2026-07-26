"""
modules/scanners.py

Security & vulnerability scanner tool wrappers.
Covers: TestSSL (comprehensive TLS/SSL audit) and Nuclei (template-based vuln scan).
"""

import json
from pathlib import Path
from typing import Any

from modules.base import BaseScanner
from modules.executor import execute_command
from modules.recon import _extract_hostname, _normalize_url


# ─── TLS/SSL Category Mapping ─────────────────────────────────────────────────
# Maps testssl finding ID prefixes/keywords to human-readable categories.
# Used for grouping in the report.
_TLS_CATEGORIES = {
    "protocol": "Protocol Support",
    "cipher": "Cipher Suite",
    "pfs": "Perfect Forward Secrecy",
    "cert": "Certificate",
    "hsts": "HTTP Security Header",
    "hpkp": "HTTP Security Header",
    "heartbleed": "Vulnerability",
    "ccs": "Vulnerability",
    "poodle": "Vulnerability",
    "beast": "Vulnerability",
    "crime": "Vulnerability",
    "breach": "Vulnerability",
    "freak": "Vulnerability",
    "logjam": "Vulnerability",
    "drown": "Vulnerability",
    "robot": "Vulnerability",
    "sweet32": "Vulnerability",
    "lucky13": "Vulnerability",
    "ticketbleed": "Vulnerability",
    "zombie": "Vulnerability",
    "goldendoodle": "Vulnerability",
    "raccoon": "Vulnerability",
    "padding": "Vulnerability",
    "rc4": "Weak Cipher",
    "3des": "Weak Cipher",
    "null": "Weak Cipher",
    "anon": "Weak Cipher",
    "export": "Weak Cipher",
    "session": "Session Management",
    "alpn": "Protocol Support",
    "http2": "Protocol Support",
    "sni": "Protocol Support",
    "caa": "DNS / Certificate",
    "ocsp": "Certificate",
    "ct": "Certificate Transparency",
    "compression": "Configuration",
    "renegotiation": "Configuration",
    "server_defaults": "Server Configuration",
    "overall_grade": "Overall Assessment",
}


def _get_tls_category(finding_id: str) -> str:
    """Returns a human-readable category for a testssl finding ID."""
    fid_lower = finding_id.lower()
    for key, cat in _TLS_CATEGORIES.items():
        if key in fid_lower:
            return cat
    return "General"


# ─── TestSSL Scanner ──────────────────────────────────────────────────────────

class TestSslScanner(BaseScanner):
    """
    TestSSL wrapper for comprehensive TLS/SSL security assessment.
    
    Runs a full testssl check covering:
      - SSL/TLS protocol support (SSLv2, SSLv3, TLS 1.0, 1.1, 1.2, 1.3)
      - Cipher suites (strength, NULL, anonymous, export-grade, RC4, 3DES, DES)
      - Perfect Forward Secrecy & DH parameters
      - Certificate validity, expiry, chain, hostname match, SAN, wildcard
      - OCSP Stapling, Certificate Transparency, HSTS, HPKP
      - Session resumption & session tickets
      - ALPN, HTTP/2, SNI support
      - DNS CAA records
      - Vulnerabilities: Heartbleed, CCS Injection, POODLE, BEAST, CRIME,
        BREACH, FREAK, LOGJAM, DROWN, ROBOT, SWEET32, Lucky13, Ticketbleed,
        Zombie POODLE, GOLDENDOODLE, Raccoon, Padding Oracle
      - Compression, renegotiation
      - Server preference & overall TLS grade
    """

    @property
    def name(self) -> str:
        return "TestSSL Comprehensive TLS/SSL Auditor"

    @property
    def tool_binary(self) -> str:
        # On Kali Linux the binary is named 'testssl' (without .sh)
        return "testssl"

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {
                "status": "skipped",
                "reason": "testssl not installed (install: apt install testssl.sh)",
                "findings": [],
                "summary": {}
            }

        # testssl requires host[:port] — extract clean hostname
        hostname = _extract_hostname(self.target)
        self.logger.info(f"Running [{self.name}] on: {hostname}:443")
        out_file = self.output_dir / "testssl_output.json"

        cmd = [
            self.tool_binary,
            "--color", "2",
            "--overwrite",
            "--jsonfile-pretty", str(out_file),
            f"{hostname}:443"
        ]

        result = execute_command(cmd, timeout=self.config.timeout, logger=self.logger)

        raw = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
        if not raw.strip():
            raw = result.stdout or ""

        parsed = self.parse_output(raw)
        is_success = result.success or (result.returncode in (0, 2, 3, 4, 5, 6, 7)) or bool(parsed["findings"])

        return {
            "status": "success" if is_success else "failed",
            "duration": result.duration,
            "findings": parsed["findings"],
            "summary": parsed["summary"],
            "count": len(parsed["findings"]),
            "raw_stdout": result.stdout,
            "output_file": str(out_file)
        }

    def parse_output(self, raw_output: str) -> dict[str, Any]:
        """
        Parses testssl JSON output.
        
        testssl --jsonfile-pretty produces a JSON with key 'scanResult' containing
        a list of result objects. Each has an 'id', 'severity', 'finding', and 'cve'.
        
        Returns a dict with:
          - findings: all entries (INFO included for completeness)
          - summary: a dict grouping findings by category and extracting the grade
        """
        findings: list[dict[str, Any]] = []
        summary: dict[str, Any] = {
            "grade": "",
            "protocols": {},
            "vulnerabilities": [],
            "warnings": [],
        }

        if not raw_output.strip():
            return {"findings": findings, "summary": summary}

        try:
            data = json.loads(raw_output)
        except json.JSONDecodeError:
            return {"findings": findings, "summary": summary}

        # testssl --jsonfile-pretty wraps results in {"scanResult": [...]}
        scan_results = []
        if isinstance(data, dict):
            scan_results = data.get("scanResult", [])
            if not scan_results and isinstance(data.get("id"), str):
                # Single result object (older testssl versions)
                scan_results = [data]
        elif isinstance(data, list):
            scan_results = data

        for result_block in scan_results:
            # result_block may itself contain nested lists (per-finding)
            items = result_block if isinstance(result_block, list) else [result_block]

            for item in items:
                if not isinstance(item, dict):
                    continue

                finding_id = item.get("id", "").strip()
                severity = item.get("severity", "INFO").strip().upper()
                finding_text = item.get("finding", "").strip()
                cve_raw = item.get("cve", "").strip()
                cwe_raw = item.get("cwe", "").strip()

                if not finding_id or not finding_text:
                    continue

                category = _get_tls_category(finding_id)
                cve_list = [c.strip() for c in cve_raw.split() if c.strip().upper().startswith("CVE")]

                entry = {
                    "id": finding_id,
                    "severity": severity,
                    "category": category,
                    "finding": finding_text,
                    "cve": cve_list,
                    "cwe": cwe_raw,
                }
                findings.append(entry)

                # Build summary sub-structures
                if "overall_grade" in finding_id.lower() or "grade" in finding_id.lower():
                    summary["grade"] = finding_text

                if category == "Protocol Support" and "protocol" in finding_id.lower():
                    summary["protocols"][finding_id] = finding_text

                if category == "Vulnerability" and severity in ("HIGH", "CRITICAL", "MEDIUM", "WARN"):
                    summary["vulnerabilities"].append(finding_id)

                if severity in ("WARN", "MEDIUM", "HIGH", "CRITICAL"):
                    summary["warnings"].append({
                        "id": finding_id,
                        "severity": severity,
                        "finding": finding_text,
                        "cve": cve_list
                    })

        return {"findings": findings, "summary": summary}


# ─── Nuclei Scanner ───────────────────────────────────────────────────────────

class NucleiScanner(BaseScanner):
    """
    Nuclei wrapper — fast template-based vulnerability scanner.
    Uses: nuclei -u <url> -j -o <file> -silent
    """

    @property
    def name(self) -> str:
        return "Nuclei Vulnerability Scanner"

    @property
    def tool_binary(self) -> str:
        return "nuclei"

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {"status": "skipped", "reason": "nuclei not installed", "vulnerabilities": []}

        url = _normalize_url(self.target)
        self.logger.info(f"Running [{self.name}] on: {url}")
        out_file = self.output_dir / "nuclei_output.json"

        cmd = [
            self.tool_binary,
            "-u", url,
            "-j",           # JSON output
            "-o", str(out_file),
            "-silent",
            "-no-color",
        ]
        result = execute_command(cmd, timeout=self.config.timeout, logger=self.logger)
        raw = out_file.read_text(encoding="utf-8") if out_file.exists() else result.stdout
        vulnerabilities = self.parse_output(raw)

        return {
            "status": "success" if result.success else "failed",
            "duration": result.duration,
            "vulnerabilities": vulnerabilities,
            "count": len(vulnerabilities),
            "output_file": str(out_file)
        }

    def parse_output(self, raw_output: str) -> list[dict[str, Any]]:
        """Parses nuclei JSON-line stream output."""
        vulnerabilities = []
        for line in raw_output.splitlines():
            cleaned = line.strip()
            if not cleaned:
                continue
            try:
                data = json.loads(cleaned)
                info = data.get("info", {})
                vulnerabilities.append({
                    "template_id": data.get("template-id", ""),
                    "name": info.get("name", ""),
                    "severity": info.get("severity", "info"),
                    "matched_at": data.get("matched-at", ""),
                    "description": info.get("description", ""),
                    "cve_id": info.get("classification", {}).get("cve-id", []),
                    "type": data.get("type", ""),
                    "tags": info.get("tags", []),
                    "reference": info.get("reference", []),
                })
            except json.JSONDecodeError:
                continue
        return vulnerabilities
