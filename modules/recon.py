"""
modules/recon.py

Reconnaissance & enumeration tool wrappers.
Covers: Subfinder, HttpProber (curl-based), Nmap, WhatWeb, Katana.
"""

import json
import re
import shutil
import subprocess
import time
import xml.etree.ElementTree as ET
from typing import Any
from urllib.parse import urlparse

from modules.base import BaseScanner
from modules.executor import execute_command


# ─── Helper ───────────────────────────────────────────────────────────────────

def _normalize_url(target: str) -> str:
    """
    Ensures the target has an http/https scheme for tools that require a URL.
    """
    if not target.startswith("http://") and not target.startswith("https://"):
        return f"https://{target}"
    return target


def _extract_hostname(target: str) -> str:
    """
    Extracts bare hostname/IP from a URL or plain domain/IP string.
    """
    if target.startswith("http://") or target.startswith("https://"):
        return urlparse(target).hostname or target
    return target.split(":")[0]


# ─── Subfinder ────────────────────────────────────────────────────────────────

class SubfinderScanner(BaseScanner):
    """
    Subfinder wrapper — passive subdomain discovery.
    Uses: subfinder -d <domain> -o <file>
    """

    @property
    def name(self) -> str:
        return "Subfinder Subdomain Discovery"

    @property
    def tool_binary(self) -> str:
        return "subfinder"

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {"status": "skipped", "reason": "subfinder not installed", "subdomains": []}

        # subfinder requires a bare domain — strip any protocol/path
        hostname = _extract_hostname(self.target)
        self.logger.info(f"Running [{self.name}] on: {hostname}")
        out_file = self.output_dir / "subfinder_output.txt"

        cmd = [
            self.tool_binary,
            "-d", hostname,
            "-o", str(out_file),
            "-silent",
            "-all",         # Use all passive sources
        ]
        result = execute_command(cmd, timeout=self.config.timeout, logger=self.logger)

        # Read from output file first, fall back to stdout
        raw = out_file.read_text(encoding="utf-8") if out_file.exists() else result.stdout
        subdomains = self.parse_output(raw)

        return {
            "status": "success" if (result.success or subdomains) else "failed",
            "duration": result.duration,
            "subdomains": subdomains,
            "count": len(subdomains),
            "target_hostname": hostname,
            "output_file": str(out_file)
        }

    def parse_output(self, raw_output: str) -> list[str]:
        """Deduplicates and sorts discovered subdomain lines."""
        subdomains = set()
        for line in raw_output.splitlines():
            cleaned = line.strip().lower()
            if cleaned and "." in cleaned:
                subdomains.add(cleaned)
        return sorted(list(subdomains))


# ─── HTTP Prober (curl-based replacement for ProjectDiscovery httpx) ──────────

class HttpxScanner(BaseScanner):
    """
    HTTP service prober using curl.
    Probes target URL(s) for status codes, headers, server fingerprint, and title.
    Supports both bare domains (probes http + https) and explicit URLs.
    """

    @property
    def name(self) -> str:
        return "HTTP Service Prober"

    @property
    def tool_binary(self) -> str:
        return "curl"

    def _probe_url(self, url: str) -> dict[str, Any] | None:
        """
        Probes a single URL using curl and returns structured response data.
        """
        cmd = [
            "curl",
            "-sSL",                     # Silent, follow redirects
            "--max-time", "15",
            "--connect-timeout", "8",
            "-w", "\n---CURL-META---\nHTTP_CODE:%{http_code}\nFINAL_URL:%{url_effective}\nCONTENT_TYPE:%{content_type}\nSIZE:%{size_download}\nTIME:%{time_total}",
            "-D", "-",                   # Dump response headers to stdout
            "--insecure",
            url
        ]
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=20, check=False
            )
            raw = proc.stdout
        except Exception:
            return None

        if "---CURL-META---" not in raw:
            return None

        body_and_headers, meta_block = raw.split("---CURL-META---", 1)
        meta = {}
        for line in meta_block.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()

        http_code = int(meta.get("HTTP_CODE", "0") or "0")
        if http_code == 0:
            return None

        # Parse response headers (first block before blank line is headers)
        headers: dict[str, str] = {}
        header_section = ""
        # curl -D - dumps ALL redirect headers; we want the last set
        header_blocks = body_and_headers.split("\r\n\r\n")
        if header_blocks:
            header_section = header_blocks[-2] if len(header_blocks) > 1 else header_blocks[0]
        for hline in header_section.splitlines():
            if ": " in hline:
                hk, hv = hline.split(": ", 1)
                headers[hk.strip().lower()] = hv.strip()

        # Extract page title from last body block
        body = header_blocks[-1] if header_blocks else ""
        title = ""
        import re
        title_match = re.search(r"<title[^>]*>([^<]{1,200})</title>", body, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = " ".join(title_match.group(1).strip().split())

        return {
            "url": meta.get("FINAL_URL", url),
            "probed_url": url,
            "status_code": http_code,
            "title": title,
            "server": headers.get("server", ""),
            "x_powered_by": headers.get("x-powered-by", ""),
            "content_type": meta.get("CONTENT_TYPE", ""),
            "content_length": int(meta.get("SIZE", "0") or "0"),
            "hsts": headers.get("strict-transport-security", ""),
            "x_frame_options": headers.get("x-frame-options", ""),
            "x_content_type_options": headers.get("x-content-type-options", ""),
            "redirect_location": headers.get("location", ""),
            "technologies": [v for k, v in headers.items() if k in ("server", "x-powered-by") and v],
        }

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {"status": "skipped", "reason": "curl not installed", "services": []}

        self.logger.info(f"Running [{self.name}] on target: {self.target}")
        services = []
        hostname = _extract_hostname(self.target)

        # Build list of URLs to probe
        urls_to_probe: list[str] = []
        if self.target.startswith("http://") or self.target.startswith("https://"):
            urls_to_probe.append(self.target)
        else:
            urls_to_probe.extend([f"https://{hostname}", f"http://{hostname}"])

        for url in urls_to_probe:
            result = self._probe_url(url)
            if result:
                services.append(result)

        # Save to file
        out_file = self.output_dir / "httpx_output.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(services, f, indent=2)

        return {
            "status": "success" if services else "failed",
            "duration": 0,
            "services": services,
            "count": len(services),
            "output_file": str(out_file)
        }

    def parse_output(self, raw_output: str) -> list[dict[str, Any]]:
        """Parses saved JSON output file."""
        try:
            return json.loads(raw_output)
        except json.JSONDecodeError:
            return []


# ─── Nmap ──────────────────────────────────────────────────────────────────────

class NmapScanner(BaseScanner):
    """
    Nmap wrapper — full port scan with service/version + OS detection.
    Uses full Nmap XML output to build a detailed host and service dashboard.
    """

    @property
    def name(self) -> str:
        return "Nmap Port & Service Scanner"

    @property
    def tool_binary(self) -> str:
        return "nmap"

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {"status": "skipped", "reason": "nmap not installed", "hosts": []}

        hostname = _extract_hostname(self.target)
        self.logger.info(f"Running [{self.name}] on: {hostname}")
        out_file = self.output_dir / "nmap_output.xml"

        cmd = [
            self.tool_binary,
            "-Pn",
            "-sV",
            "-sC",
            "-O",
            "-A",
            "--top-ports", str(getattr(self.config, "nmap_scan_top_ports", 1000)),
            "-T4",
        ]

        if getattr(self.config, "nmap_enable_traceroute", True):
            cmd.append("--traceroute")

        if getattr(self.config, "nmap_enable_version_intensity", True):
            cmd.append("--version-all")
        else:
            cmd.extend(["--version-intensity", "5"])

        if getattr(self.config, "nmap_enable_udp", False):
            cmd.append("-sU")

        if getattr(self.config, "nmap_enable_vuln_scripts", True):
            cmd.extend(["--script", "vuln"])

        cmd.extend(["-oX", str(out_file), hostname])
        result = execute_command(
            cmd,
            timeout=self.config.timeout,
            logger=self.logger,
            show_progress=True,
        )

        xml_content = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
        if not xml_content and result.stdout:
            xml_content = result.stdout

        parsed = self.parse_output(xml_content)
        analysis = self._analyze_findings(parsed.get("hosts", []), parsed.get("scan_info", {}))

        return {
            "status": "success" if (result.success or parsed.get("hosts")) else "failed",
            "duration": result.duration,
            "hostname": hostname,
            "target": self.target,
            "hosts": parsed.get("hosts", []),
            "summary": parsed.get("summary", ""),
            "scan_info": parsed.get("scan_info", {}),
            "analysis": analysis,
            "raw_xml": xml_content,
            "output_file": str(out_file),
        }

    def parse_output(self, raw_output: str) -> dict[str, Any]:
        """Parses Nmap XML output into structured host/port dictionaries."""
        if not raw_output or not raw_output.strip():
            return {"hosts": [], "summary": "", "scan_info": {}}

        hosts: list[dict[str, Any]] = []
        summary = ""
        scan_info: dict[str, Any] = {}

        try:
            root = ET.fromstring(raw_output)

            scan_info = {
                "scanner": root.attrib.get("scanner", ""),
                "args": root.attrib.get("args", ""),
                "startstr": root.attrib.get("startstr", ""),
                "version": root.attrib.get("version", ""),
                "xmloutputversion": root.attrib.get("xmloutputversion", ""),
            }

            scaninfo_node = root.find("scaninfo")
            if scaninfo_node is not None:
                scan_info["scan_type"] = scaninfo_node.attrib.get("type", "")
                scan_info["protocol"] = scaninfo_node.attrib.get("protocol", "")
                scan_info["services"] = scaninfo_node.attrib.get("services", "")
                scan_info["num_services"] = scaninfo_node.attrib.get("numservices", "")

            run_stats = root.find("runstats/finished")
            if run_stats is not None:
                summary = run_stats.attrib.get("summary", "")
                scan_info.update({
                    "summary": summary,
                    "elapsed": run_stats.attrib.get("elapsed", ""),
                    "timestr": run_stats.attrib.get("timestr", ""),
                    "hosts": run_stats.attrib.get("hosts", ""),
                    "exit": run_stats.attrib.get("exit", ""),
                    "reason": run_stats.attrib.get("reason", ""),
                })

            for host_node in root.findall("host"):
                addresses = [
                    {
                        "addr": addr.attrib.get("addr", ""),
                        "addrtype": addr.attrib.get("addrtype", ""),
                        "vendor": addr.attrib.get("vendor", ""),
                    }
                    for addr in host_node.findall("address")
                ]

                hostnames = [
                    hostname.attrib.get("name", "")
                    for hostname in host_node.findall("hostnames/hostname")
                ]
                reverse_dns = [
                    hostname.attrib.get("name", "")
                    for hostname in host_node.findall("hostnames/hostname")
                    if hostname.attrib.get("type", "") == "PTR"
                ]

                status_node = host_node.find("status")
                state = status_node.attrib.get("state", "unknown") if status_node is not None else "unknown"

                latency_ms = None
                times_node = host_node.find("times")
                if times_node is not None:
                    srtt = times_node.attrib.get("srtt") or times_node.attrib.get("rtt")
                    if srtt and srtt.isdigit():
                        latency_ms = round(int(srtt) / 1000.0, 2)

                uptime_node = host_node.find("uptime")
                uptime_seconds = None
                uptime_lastboot = ""
                if uptime_node is not None:
                    uptime_seconds = int(uptime_node.attrib.get("seconds", "0") or "0")
                    uptime_lastboot = uptime_node.attrib.get("lastboot", "")

                os_node = host_node.find("os")
                os_match_name = ""
                os_accuracy = ""
                os_classes: list[dict[str, Any]] = []
                if os_node is not None:
                    os_match = os_node.find("osmatch")
                    if os_match is not None:
                        os_match_name = os_match.attrib.get("name", "")
                        os_accuracy = os_match.attrib.get("accuracy", "")

                    for os_class in os_node.findall("osclass"):
                        os_classes.append({
                            "vendor": os_class.attrib.get("vendor", ""),
                            "osfamily": os_class.attrib.get("osfamily", ""),
                            "osgen": os_class.attrib.get("osgen", ""),
                            "type": os_class.attrib.get("type", ""),
                            "accuracy": os_class.attrib.get("accuracy", ""),
                            "cpe": os_class.attrib.get("cpe", ""),
                        })

                host_scripts: dict[str, str] = {}
                for script_node in host_node.findall("hostscript/script"):
                    sid = script_node.attrib.get("id", "")
                    if sid:
                        host_scripts[sid] = script_node.attrib.get("output", "")

                traceroute: list[dict[str, Any]] = []
                for hop_node in host_node.findall("trace/hop"):
                    traceroute.append({
                        "ttl": hop_node.attrib.get("ttl", ""),
                        "rtt": hop_node.attrib.get("rtt", ""),
                        "ipaddr": hop_node.attrib.get("ipaddr", ""),
                        "host": hop_node.attrib.get("host", ""),
                    })

                ports: list[dict[str, Any]] = []
                for port_node in host_node.findall("ports/port"):
                    port_state_node = port_node.find("state")
                    port_state = port_state_node.attrib.get("state", "") if port_state_node is not None else ""
                    port_reason = port_state_node.attrib.get("reason", "") if port_state_node is not None else ""

                    service_node = port_node.find("service")
                    service_name = ""
                    product = ""
                    version = ""
                    extra_info = ""
                    tunnel = ""
                    method = ""
                    confidence = ""
                    service_fp = ""
                    if service_node is not None:
                        service_name = service_node.attrib.get("name", "")
                        product = service_node.attrib.get("product", "")
                        version = service_node.attrib.get("version", "")
                        extra_info = service_node.attrib.get("extrainfo", "")
                        tunnel = service_node.attrib.get("tunnel", "")
                        method = service_node.attrib.get("method", "")
                        confidence = service_node.attrib.get("conf", "")
                        service_fp = service_node.attrib.get("servicefp", "")

                    scripts: dict[str, str] = {}
                    service_details: dict[str, Any] = {
                        "banner": "",
                        "service_fingerprint": service_fp,
                        "protocol": service_name,
                        "ssl_tls_info": "",
                        "http_title": "",
                        "http_server_header": "",
                        "redirects": "",
                        "robots": "",
                        "http_methods": "",
                        "allowed_methods": [],
                        "raw_scripts": {},
                    }

                    for script_node in port_node.findall("script"):
                        sid = script_node.attrib.get("id", "")
                        sout = script_node.attrib.get("output", "")
                        scripts[sid] = sout
                        service_details["raw_scripts"][sid] = sout

                        if sid == "http-title":
                            service_details["http_title"] = sout
                        elif sid == "http-server-header":
                            service_details["http_server_header"] = sout
                        elif sid == "http-methods":
                            service_details["http_methods"] = sout
                            methods = re.findall(r"[A-Z]{3,}", sout)
                            service_details["allowed_methods"] = sorted(set(methods))
                        elif sid == "robots.txt":
                            service_details["robots"] = sout
                        elif sid == "ssl-cert":
                            service_details["ssl_tls_info"] = sout
                        elif sid == "http-trace":
                            service_details["redirects"] = sout
                        elif sid == "ftp-anon" and "anonymous" in sout.lower():
                            service_details["banner"] = sout

                    banner_parts = [product, version, extra_info]
                    service_details["banner"] = service_details["banner"] or " ".join([p for p in banner_parts if p]).strip()

                    ports.append({
                        "port": int(port_node.attrib.get("portid", "0") or "0"),
                        "protocol": port_node.attrib.get("protocol", ""),
                        "state": port_state,
                        "service": service_name,
                        "product": product,
                        "version": version,
                        "extra_info": extra_info,
                        "tunnel": tunnel,
                        "reason": port_reason,
                        "confidence": confidence,
                        "method": method,
                        "service_fingerprint": service_fp,
                        "service_details": service_details,
                        "scripts": scripts,
                    })

                hosts.append({
                    "ip": next((addr["addr"] for addr in addresses if addr["addrtype"] == "ipv4"), addresses[0]["addr"] if addresses else ""),
                    "addresses": addresses,
                    "hostnames": hostnames,
                    "hostname": hostnames[0] if hostnames else "",
                    "reverse_dns": reverse_dns,
                    "state": state,
                    "latency_ms": latency_ms,
                    "uptime_seconds": uptime_seconds,
                    "uptime_lastboot": uptime_lastboot,
                    "os": {
                        "name": os_match_name,
                        "accuracy": os_accuracy,
                        "classes": os_classes,
                    },
                    "host_scripts": host_scripts,
                    "traceroute": traceroute,
                    "all_ports": ports,
                    "open_ports": [p for p in ports if p.get("state") == "open"],
                    "closed_ports": [p for p in ports if p.get("state") == "closed"],
                    "filtered_ports": [p for p in ports if p.get("state") == "filtered"],
                })

        except ET.ParseError as err:
            self.logger.error(f"Failed to parse Nmap XML: {err}")

        return {"hosts": hosts, "summary": summary, "scan_info": scan_info}

    def _analyze_findings(self, hosts: list[dict[str, Any]], scan_info: dict[str, Any]) -> dict[str, Any]:
        findings: list[dict[str, Any]] = []
        recommendations: list[str] = []
        tech_inventory: set[str] = set()
        open_ports: set[str] = set()

        def add_finding(finding_id: str, name: str, severity: str, explanation: str, evidence: str, recommendation: str) -> None:
            findings.append({
                "id": finding_id,
                "name": name,
                "severity": severity,
                "explanation": explanation,
                "evidence": evidence,
                "recommendation": recommendation,
            })
            if recommendation not in recommendations:
                recommendations.append(recommendation)

        for host in hosts:
            for p in host.get("all_ports", []):
                service = (p.get("service") or "").lower()
                port_key = f"{p.get('port')}/{p.get('protocol')}"
                if service:
                    tech_inventory.add(service)
                if p.get("state") == "open":
                    open_ports.add(port_key)

                details = p.get("service_details", {}) or {}
                raw_scripts = details.get("raw_scripts", {})
                ssl_info = (details.get("ssl_tls_info") or "").lower()
                http_methods = details.get("http_methods") or ""
                robots = details.get("robots") or ""
                http_title = (details.get("http_title") or "").lower()
                banner = (details.get("banner") or "").lower()

                if service == "ftp":
                    anon_output = raw_scripts.get("ftp-anon", "")
                    if anon_output and "anonymous" in anon_output.lower():
                        add_finding(
                            "anonymous-ftp",
                            "Anonymous FTP Login Allowed",
                            "high",
                            "FTP anonymous access is enabled, which permits unauthenticated file listing or download.",
                            anon_output,
                            "Disable anonymous FTP access or restrict it to trusted accounts."
                        )

                if service == "smb" or p.get("port") in {139, 445}:
                    smb_security = raw_scripts.get("smb-security-mode", "")
                    if smb_security and "signing disabled" in smb_security.lower():
                        add_finding(
                            "smb-signing-disabled",
                            "SMB Signing Disabled",
                            "high",
                            "SMB signing is disabled, increasing the risk of tampered SMB sessions.",
                            smb_security,
                            "Require SMB signing and enforce channel integrity."
                        )

                if ssl_info and any(token in ssl_info for token in ["self-signed", "expired", "weak", "obsolete", "sha1"]):
                    add_finding(
                        "weak-ssl-tls",
                        "Weak SSL/TLS Configuration",
                        "medium",
                        "The service exposes SSL/TLS metadata that suggests weak or obsolete configuration.",
                        ssl_info,
                        "Review certificate validity and disable weak TLS ciphers."
                    )

                if "trace" in http_methods.lower() or "put" in http_methods.upper() or "delete" in http_methods.upper() or "connect" in http_methods.upper():
                    add_finding(
                        "unsafe-http-methods",
                        "Unsafe HTTP Methods Exposed",
                        "low",
                        "The HTTP service supports methods that may increase attack surface.",
                        http_methods,
                        "Allow only safe HTTP methods and disable TRACE/PUT/DELETE/CONNECT if not required."
                    )

                if robots and "disallow" not in robots.lower():
                    add_finding(
                        "robots-public",
                        "Public robots.txt",
                        "informational",
                        "A robots.txt file is accessible and may reveal hidden or sensitive paths.",
                        robots,
                        "Review robots.txt content to avoid exposing sensitive URLs."
                    )

                if any(tag in http_title for tag in ["admin", "login", "administrator"]):
                    add_finding(
                        "admin-page-detected",
                        "Administrative Interface Detected",
                        "medium",
                        "The web title suggests an admin portal or login interface is exposed.",
                        details.get("http_title", ""),
                        "Restrict access to administrative endpoints with authentication and IP allowlisting."
                    )

        if not findings:
            findings.append({
                "id": "no-nmap-findings",
                "name": "No significant Nmap-level findings detected",
                "severity": "informational",
                "explanation": "Parsed Nmap output did not reveal obvious protocol or service misconfigurations.",
                "evidence": "",
                "recommendation": "Continue with deeper application-layer and authenticated scanning.",
            })
            recommendations.append("Continue with deeper application-layer and authenticated scanning.")

        severity_map = {
            "critical": 10,
            "high": 7,
            "medium": 4,
            "low": 2,
            "informational": 0,
        }
        risk_score = sum(severity_map.get(item["severity"], 0) for item in findings)
        risk_level = "Informational"
        if any(item["severity"] == "critical" for item in findings):
            risk_level = "Critical"
        elif any(item["severity"] == "high" for item in findings):
            risk_level = "High"
        elif any(item["severity"] == "medium" for item in findings):
            risk_level = "Medium"
        elif any(item["severity"] == "low" for item in findings):
            risk_level = "Low"

        ai_summary_parts: list[str] = []
        ai_summary_parts.append(f"Nmap scanned {len(hosts)} host(s) and found {len(open_ports)} open port(s).")
        if tech_inventory:
            ai_summary_parts.append(f"Detected service fingerprints include: {', '.join(sorted(tech_inventory))}.")
        if findings and findings[0]["id"] != "no-nmap-findings":
            ai_summary_parts.append("Key items include service misconfigurations, weak TLS indicators, and exposed admin or anonymous services.")
        ai_summary_parts.append("Next steps: validate these findings with authenticated application testing and TLS hardening checks.")

        return {
            "findings": findings,
            "risk_score": {
                "level": risk_level,
                "score": risk_score,
                "scale_max": 50,
            },
            "recommendations": recommendations,
            "ai_summary": " ".join(ai_summary_parts),
        }


# ─── WhatWeb ──────────────────────────────────────────────────────────────────

class WhatWebScanner(BaseScanner):
    """
    WhatWeb wrapper — web technology stack fingerprinting.
    Uses: whatweb --log-json=<file> --aggression 3 <url>
    """

    @property
    def name(self) -> str:
        return "WhatWeb Tech Stack Fingerprinter"

    @property
    def tool_binary(self) -> str:
        return "whatweb"

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {"status": "skipped", "reason": "whatweb not installed", "tech_stack": []}

        url = _normalize_url(self.target)
        self.logger.info(f"Running [{self.name}] on: {url}")
        out_file = self.output_dir / "whatweb_output.json"

        cmd = [
            self.tool_binary,
            "--log-json", str(out_file),  # space-separated, not =
            "--aggression", "3",           # Level 3: send additional HTTP requests
            "--no-errors",
            url
        ]
        result = execute_command(cmd, timeout=self.config.timeout, logger=self.logger)

        raw = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
        if not raw.strip():
            raw = result.stdout
        tech_stack = self.parse_output(raw)

        return {
            "status": "success" if (result.success or tech_stack) else "failed",
            "duration": result.duration,
            "tech_stack": tech_stack,
            "output_file": str(out_file)
        }

    def parse_output(self, raw_output: str) -> list[dict[str, Any]]:
        """
        WhatWeb JSON output is one JSON object per line.
        Each line represents a scanned URL with detected plugins.
        """
        results = []
        if not raw_output.strip():
            return results

        for line in raw_output.strip().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
                # WhatWeb produces either a list-of-one or a single object per line
                if isinstance(item, list):
                    item = item[0] if item else {}

                target_url = item.get("target", "")
                http_status = item.get("http_status", 0)
                plugins = item.get("plugins", {})

                # Build rich technology list with version info
                technologies = []
                for plugin_name, plugin_data in plugins.items():
                    entry = {"name": plugin_name}
                    if isinstance(plugin_data, dict):
                        version_list = plugin_data.get("version", [])
                        if version_list:
                            entry["version"] = version_list[0] if version_list else ""
                        string_list = plugin_data.get("string", [])
                        if string_list:
                            entry["detail"] = string_list[0] if string_list else ""
                    technologies.append(entry)

                results.append({
                    "target": target_url,
                    "status": http_status,
                    "technologies": technologies,
                    "tech_names": [t["name"] for t in technologies]
                })
            except (json.JSONDecodeError, IndexError):
                continue

        return results


# ─── Katana ───────────────────────────────────────────────────────────────────

class KatanaScanner(BaseScanner):
    """
    Katana wrapper — web crawling and endpoint discovery.
    Uses: katana -u <url> -jc -d 3 -silent
    """

    @property
    def name(self) -> str:
        return "Katana Web Crawler"

    @property
    def tool_binary(self) -> str:
        return "katana"

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {"status": "skipped", "reason": "katana not installed", "endpoints": []}

        url = _normalize_url(self.target)
        self.logger.info(f"Running [{self.name}] on: {url}")
        out_file = self.output_dir / "katana_output.txt"

        cmd = [
            self.tool_binary,
            "-u", url,
            "-jc",          # JavaScript crawling
            "-d", "3",      # Crawl depth
            "-silent",
            "-o", str(out_file),
        ]
        result = execute_command(cmd, timeout=self.config.timeout, logger=self.logger)
        raw = out_file.read_text(encoding="utf-8") if out_file.exists() else result.stdout
        endpoints = self.parse_output(raw)

        return {
            "status": "success" if (result.success or endpoints) else "failed",
            "duration": result.duration,
            "endpoints": endpoints,
            "count": len(endpoints),
            "output_file": str(out_file)
        }

    def parse_output(self, raw_output: str) -> list[str]:
        """Parses katana plain-text URL lines into a sorted deduplicated list."""
        endpoints = set()
        for line in raw_output.splitlines():
            cleaned = line.strip()
            if cleaned and cleaned.startswith("http"):
                endpoints.add(cleaned)
        return sorted(list(endpoints))
