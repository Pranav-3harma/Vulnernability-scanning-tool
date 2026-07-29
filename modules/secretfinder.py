"""
modules/secretfinder.py

SecretFinder integration module — JavaScript secret / credential scanner.

Scans JavaScript files discovered by Katana (or extracted directly from target pages)
for hardcoded secrets, API keys, tokens, credentials, and sensitive data using SecretFinder.

Pipeline position: Katana → SecretFinder → TestSSL
"""

import json
import logging
import re
import time
from pathlib import Path
from typing import Any

from framework.config import Config
from framework.ui import prompt_install_secretfinder
from modules.base import BaseScanner
from secretfinder_runner import (
    get_secretfinder_paths,
    is_secretfinder_installed,
    run_secretfinder,
)

# ensure outputs directory exists for other modules
try:
    Path(__file__).parent.parent.joinpath("reports").mkdir(parents=True, exist_ok=True)
except Exception:
    pass


# ─── Installation Path ────────────────────────────────────────────────────────

_script_path, _venv_python = get_secretfinder_paths()
SECRETFINDER_SCRIPT: Path = _script_path
SECRETFINDER_VENV_PYTHON: Path = _venv_python

# Per-JS-file subprocess timeout in seconds
JS_SCAN_TIMEOUT: int = 60



# ─── SecretFinder Native Key Mapping ──────────────────────────────────────────
# SecretFinder outputs lines in the format: <rule_name>\t->\t<matched_value>
# This catalog maps SecretFinder's native rule names directly to structured metadata.

SECRETFINDER_NATIVE_MAP: dict[str, tuple[str, str, str]] = {
    # rule_name : (secret_type, severity, confidence)
    "google_api": ("Google API Key", "critical", "high"),
    "firebase": ("Firebase Key", "high", "high"),
    "google_captcha": ("Google Captcha Key", "low", "medium"),
    "google_oauth": ("Google OAuth Token", "critical", "high"),
    "amazon_aws_access_key_id": ("AWS Access Key ID", "critical", "high"),
    "amazon_mws_auth_toke": ("Amazon MWS Auth Token", "critical", "high"),
    "amazon_aws_url": ("AWS S3 Bucket URL", "medium", "high"),
    "amazon_aws_url2": ("AWS S3 Bucket URL", "medium", "high"),
    "facebook_access_token": ("Facebook Access Token", "critical", "high"),
    "authorization_basic": ("Basic Auth Credentials", "high", "high"),
    "authorization_bearer": ("Bearer Token", "high", "high"),
    "authorization_api": ("API Token / Key", "high", "medium"),
    "mailgun_api_key": ("Mailgun API Key", "critical", "high"),
    "twilio_api_key": ("Twilio API Key", "critical", "high"),
    "twilio_account_sid": ("Twilio Account SID", "high", "high"),
    "twilio_app_sid": ("Twilio App SID", "medium", "medium"),
    "paypal_braintree_access_token": ("PayPal Braintree Token", "critical", "high"),
    "square_oauth_secret": ("Square OAuth Secret", "critical", "high"),
    "square_access_token": ("Square Access Token", "critical", "high"),
    "stripe_standard_api": ("Stripe Standard API Key", "critical", "high"),
    "stripe_restricted_api": ("Stripe Restricted API Key", "high", "high"),
    "github_access_token": ("GitHub Access Token", "critical", "high"),
    "rsa_private_key": ("Private RSA Key", "critical", "high"),
    "ssh_dsa_private_key": ("Private DSA Key", "critical", "high"),
    "ssh_dc_private_key": ("Private EC Key", "critical", "high"),
    "pgp_private_block": ("Private PGP Key", "critical", "high"),
    "json_web_token": ("JWT Token", "high", "high"),
    "slack_token": ("Slack Token", "high", "high"),
    "SSH_privKey": ("SSH Private Key", "critical", "high"),
    "Heroku API KEY": ("Heroku API Key", "critical", "high"),
    "possible_Creds": ("Hardcoded Credentials", "high", "medium"),
}


# ─── Fallback Secret Catalog ──────────────────────────────────────────────────
# Used if SecretFinder output line does not match native rule keys.

SECRET_CATALOG: list[tuple[str, str, str, str]] = [
    # ── Cloud & Infrastructure ─────────────────────────────────────────────
    ("AWS Access Key", "critical", "high", r"AKIA[0-9A-Z]{16}"),
    ("AWS Secret Key", "critical", "high", r"(?i)aws.{0,20}secret.{0,20}['\"][0-9a-zA-Z/+]{40}['\"]"),
    ("AWS MFA Secret", "high", "medium", r"(?i)aws.{0,20}mfa"),
    ("Google API Key", "critical", "high", r"AIzaSy[0-9A-Za-z\-_]{20,}"),
    ("Google OAuth Token", "critical", "high", r"ya29\.[0-9A-Za-z\-_]{10,}"),
    ("Google Cloud Key", "high", "high", r"(?i)google.{0,30}key.{0,20}['\"][A-Za-z0-9_\-]{30,}['\"]"),
    ("Firebase Key", "high", "high", r"AAAA[A-Za-z0-9_\-]{7}:[A-Za-z0-9_\-]{140}"),
    # ── Source Control ─────────────────────────────────────────────────────
    ("GitHub Token", "critical", "high", r"ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{59,82}"),
    ("GitHub OAuth Token", "critical", "high", r"gho_[A-Za-z0-9]{36}"),
    ("GitHub App Token", "critical", "high", r"ghs_[A-Za-z0-9]{36}|ghu_[A-Za-z0-9]{36}"),
    ("GitLab Token", "critical", "high", r"glpat-[A-Za-z0-9\-_]{20}"),
    # ── Authentication ─────────────────────────────────────────────────────
    ("JWT Token", "high", "high", r"eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]+"),
    ("Bearer Token", "high", "medium", r"(?i)bearer\s+[A-Za-z0-9\-_\.]{20,}"),
    ("OAuth Access Token", "high", "medium", r"(?i)access[_\-]?token.{0,20}['\"][A-Za-z0-9\-_\.]{20,}['\"]"),
    # ── Payment ────────────────────────────────────────────────────────────
    ("Stripe Live Key", "critical", "high", r"sk_live_[0-9a-zA-Z]{24}"),
    ("Stripe Test Key", "medium", "high", r"sk_test_[0-9a-zA-Z]{24}"),
    ("Stripe Publishable Key", "low", "high", r"pk_live_[0-9a-zA-Z]{24}"),
    # ── Communication & Messaging ──────────────────────────────────────────
    ("Slack Token", "high", "high", r"xox[baprs]-[0-9A-Za-z\-]{10,}"),
    ("Slack Webhook", "high", "high", r"https://hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[A-Za-z0-9]+"),
    ("Twilio Account SID", "high", "high", r"AC[a-zA-Z0-9]{32}"),
    ("Twilio Auth Token", "critical", "high", r"(?i)twilio.{0,20}auth.{0,20}['\"][a-zA-Z0-9]{32}['\"]"),
    ("SendGrid API Key", "critical", "high", r"SG\.[0-9A-Za-z\-_]{16,}\.[0-9A-Za-z\-_]{16,}"),
    ("Mailgun API Key", "critical", "high", r"key-[0-9a-zA-Z]{32}"),
    # ── Cryptographic Keys ─────────────────────────────────────────────────
    ("Private RSA Key", "critical", "high", r"-----BEGIN RSA PRIVATE KEY-----"),
    ("Private EC Key", "critical", "high", r"-----BEGIN EC PRIVATE KEY-----"),
    ("Private Key (Generic)", "critical", "high", r"-----BEGIN PRIVATE KEY-----"),
    ("SSH Private Key", "critical", "high", r"-----BEGIN OPENSSH PRIVATE KEY-----"),
    ("PGP Private Key", "critical", "high", r"-----BEGIN PGP PRIVATE KEY BLOCK-----"),
    # ── Database Credentials ───────────────────────────────────────────────
    ("MongoDB Connection URL", "critical", "high", r"mongodb(\+srv)?://[^:]+:[^@]+@[^\s]+"),
    ("PostgreSQL URL", "critical", "high", r"postgres(ql)?://[^:]+:[^@]+@[^\s]+"),
    ("MySQL URL", "critical", "high", r"mysql://[^:]+:[^@]+@[^\s]+"),
    ("Redis URL", "high", "high", r"redis://[^:]*:[^@]+@[^\s]+"),
    ("Database Password", "high", "medium", r"(?i)(db|database)[_\-]?pass(word)?\s*[=:]\s*['\"][^'\"]{6,}['\"]"),
    ("Database Username", "medium", "medium", r"(?i)(db|database)[_\-]?user(name)?\s*[=:]\s*['\"][^'\"]{3,}['\"]"),
    # ── Hardcoded Credentials ──────────────────────────────────────────────
    ("Hardcoded Password", "high", "medium", r"(?i)(password|passwd|pwd)\s*[=:]\s*['\"][^'\"]{6,}['\"]"),
    ("Hardcoded Username", "medium", "medium", r"(?i)(username|user)\s*[=:]\s*['\"][^'\"]{3,}['\"]"),
    ("Hardcoded Secret", "high", "medium", r"(?i)(secret|secret_key)\s*[=:]\s*['\"][^'\"]{8,}['\"]"),
    # ── API Keys (generic) ────────────────────────────────────────────────
    ("API Key", "high", "medium", r"(?i)api[_\-]?key\s*[=:]\s*['\"][A-Za-z0-9\-_\.]{16,}['\"]"),
    ("API Token", "high", "medium", r"(?i)api[_\-]?token\s*[=:]\s*['\"][A-Za-z0-9\-_\.]{16,}['\"]"),
    ("Access Token", "high", "medium", r"(?i)access[_\-]?token\s*[=:]\s*['\"][A-Za-z0-9\-_\.]{16,}['\"]"),
    # ── Webhook URLs ──────────────────────────────────────────────────────
    ("Webhook URL", "medium", "medium", r"https?://[^\s\"']+/webhook[^\s\"']*"),
    # ── Internal Endpoints & IPs ──────────────────────────────────────────
    ("Internal API Endpoint", "medium", "medium", r"(?i)(internal|private|admin)[_\-]?(api|endpoint|url)\s*[=:]\s*['\"][^'\"]+['\"]"),
    ("Internal IP Address", "medium", "high", r"(?:^|[^.\d])(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})(?:[^.\d]|$)"),
    ("Sensitive URL", "low", "low", r"(?i)(admin|login|dashboard|internal|private)/[^\s\"']*"),
]


# ─── Helper Functions ─────────────────────────────────────────────────────────

def _normalize_target(target: str) -> str:
    """Normalizes bare domains and paths into a valid HTTP/HTTPS URL for SecretFinder."""
    value = (target or "").strip()
    if not value:
        return value

    if value.startswith(("http://", "https://")):
        return value

    if "://" in value:
        return value

    if value.startswith("/"):
        return f"https://{value.lstrip('/')}"

    if "/" in value or "." in value or ":" in value:
        return f"https://{value}"

    return f"https://{value}"


def _extract_js_urls(endpoints: list[str], fallback_target: str = "") -> list[str]:
    """Collects JavaScript URLs from crawled endpoints and optional fallback target input."""
    _excluded_extensions = {
        ".css", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
        ".woff", ".woff2", ".ttf", ".eot", ".otf", ".mp4", ".mp3",
        ".webp", ".pdf", ".zip", ".tar", ".gz",
    }

    js_urls: set[str] = set()
    candidates: list[str] = []
    for endpoint in endpoints or []:
        endpoint = endpoint.strip()
        if endpoint:
            candidates.append(endpoint)
    if fallback_target:
        candidates.append(fallback_target)

    for raw_url in candidates:
        url = raw_url.strip()
        if not url.startswith("http"):
            continue

        url_lower = url.lower()
        path_part = url_lower.split("?")[0].split("#")[0]
        ext = Path(path_part).suffix

        if ext in (".js", ".jsx", ".mjs", ".cjs"):
            js_urls.add(url)
        elif ext in _excluded_extensions:
            continue
        elif ".js?" in url_lower or ".js#" in url_lower or "/js/" in url_lower or path_part.endswith(".js"):
            js_urls.add(url)
        elif url_lower.endswith("/") and fallback_target and url in {fallback_target}:
            js_urls.add(url)

    return sorted(js_urls)


def _classify_secret(line: str) -> tuple[str, str, str]:
    """Applies the fallback regex catalog to classify a line when the native map misses it."""
    for secret_type, severity, confidence, pattern in SECRET_CATALOG:
        try:
            if re.search(pattern, line, re.IGNORECASE):
                return secret_type, severity, confidence
        except re.error:
            continue
    return "Other Secret", "informational", "low"


def _truncate_value(value: str, max_len: int = 240) -> str:
    """
    Truncates a discovered secret value while preserving enough context to see the match.
    """
    value = value.strip()
    if len(value) > max_len:
        return value[:max_len] + "…"
    return value


def _normalize_severity(severity: str) -> str:
    """Normalizes severity labels to a compact, display-friendly set."""
    sev = (severity or "informational").strip().lower()
    mapping = {
        "critical": "critical",
        "high": "high",
        "medium": "medium",
        "low": "low",
        "informational": "low",
        "info": "low",
        "warn": "medium",
    }
    return mapping.get(sev, "low")


def _mask_value(value: str, keep_head: int = 4, keep_tail: int = 4) -> str:
    """Masks a sensitive value while preserving a small visible prefix/suffix."""
    value = (value or "").strip()
    if not value:
        return ""
    if len(value) <= keep_head + keep_tail:
        return value
    return f"{value[:keep_head]}...{value[-keep_tail:]}"


def _looks_meaningful(value: str, secret_type: str) -> bool:
    """Keeps obvious token and key matches visible while rejecting only clear placeholders."""
    if not value:
        return False

    text = value.strip().lower()
    if len(text) < 4:
        return False

    blocked_terms = [
        "example", "placeholder", "dummy", "changeme", "your_", "your-",
        "mysecret", "mytoken", "mykey", "localhost", "sample", "fake",
        "false", "none", "null", "undefined"
    ]
    if any(re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", text) for term in blocked_terms):
        return False

    if secret_type == "Other Secret":
        if len(text) < 8:
            return False
        if not any(ch.isdigit() for ch in value) and not any(c in value for c in "._-/"):
            return False

    return True


def _dedup_findings(findings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Removes duplicates while preserving the first evidence and source URL for each match."""
    seen: set[tuple[str, str, str]] = set()
    unique: list[dict[str, Any]] = []
    for finding in findings:
        raw_value = finding.get("raw_value") or finding.get("value", "")
        key = (finding.get("url", ""), finding.get("secret_type", ""), raw_value)
        if key not in seen:
            seen.add(key)
            unique.append(finding)
    return unique

ESSENTIAL_SECRET_KEYWORDS = (
    "key",
    "token",
    "secret",
    "password",
    "bearer",
    "oauth",
    "jwt",
    "auth",
    "api",
    "access",
    "aws",
    "google",
    "firebase",
    "github",
    "gitlab",
    "stripe",
    "sendgrid",
    "mailgun",
    "slack",
    "twilio",
    "mongo",
    "postgres",
    "mysql",
    "redis",
    "ssh",
    "rsa",
    "pgp",
)


def _is_secret_essential(finding: dict[str, Any]) -> bool:
    """Filters out low-value SecretFinder output and only keeps essential credentials/tokens."""
    severity = (finding.get("severity", "low") or "low").strip().lower()
    secret_type = (finding.get("secret_type") or "").lower()
    raw_value = (finding.get("raw_value") or "").lower()
    raw_line = (finding.get("raw_line") or "").lower()

    if secret_type != "other secret":
        return True

    if not finding.get("meaningful", False):
        return False

    return any(
        keyword in raw_value or keyword in raw_line
        for keyword in ESSENTIAL_SECRET_KEYWORDS
    )

# ─── Scanner Class ────────────────────────────────────────────────────────────

class SecretFinderScanner(BaseScanner):
    """
    SecretFinder wrapper — JavaScript secret / hardcoded credential scanner.

    Executes SecretFinder.py against discovered JavaScript URLs or extracts JS files directly,
    parses output, classifies findings into structured severities, deduplicates results,
    and saves to outputs/secrets.json.
    """

    def __init__(
        self,
        config: Config,
        logger: logging.Logger,
        katana_data: dict[str, Any],
    ) -> None:
        super().__init__(config, logger)
        self.katana_data = katana_data or {}
        script_path, venv_python = get_secretfinder_paths()
        self.script_path = script_path
        self.venv_python = venv_python
        self.debug = getattr(config, "secretfinder_debug", False) or getattr(config, "verbose", False)

    @property
    def name(self) -> str:
        return "SecretFinder JavaScript Secret Scanner"

    @property
    def tool_binary(self) -> str:
        return str(self.venv_python)

    def is_available(self) -> bool:
        """
        Verifies SecretFinder script and its virtual environment Python exist on disk.
        If missing, interactively prompts user to run install_secretfinder.sh.
        """
        if is_secretfinder_installed():
            return True

        # SecretFinder script or venv missing — prompt user to install
        installed = prompt_install_secretfinder()
        if installed and is_secretfinder_installed():
            return True

        self.logger.warning(
            f"[{self.name}] SecretFinder script or venv missing.\n"
            f"  ➤  Script: {self.script_path}\n"
            f"  ➤  Venv Python: {self.venv_python}\n"
            f"  ➤  Run './install_secretfinder.sh' to set up SecretFinder automatically.\n"
            f"  ➤  Skipping JavaScript secret analysis — remaining scan will continue."
        )
        return False

    def run(self) -> dict[str, Any]:
        """Runs SecretFinder against all discovered JavaScript sources and writes structured JSON."""
        self.logger.info(f"[{self.name}] ─── Starting SecretFinder JavaScript Analysis ───")

        if not self.is_available():
            return {
                "status": "skipped",
                "reason": f"SecretFinder script or virtual environment not found at {self.script_path}",
                "js_files_total": 0,
                "js_files_scanned": 0,
                "js_files_failed": 0,
                "secrets_found": 0,
                "findings": [],
                "severity_counts": {},
                "output_file": "",
                "errors": [f"SecretFinder script or virtual environment not found at {self.script_path}"],
            }

        # Step 1: Collect JavaScript files from crawler output or the target page itself.
        endpoints: list[str] = self.katana_data.get("endpoints", []) if isinstance(self.katana_data, dict) else []
        normalized_target = _normalize_target(self.target)
        js_urls = _extract_js_urls(endpoints, fallback_target=normalized_target)

        # Step 2: If no explicit JS files were found, let the official tool inspect the target URL itself.
        scan_target_directly = False
        if not js_urls and normalized_target:
            self.logger.info(
                f"[{self.name}] No explicit JS endpoints were found. Falling back to target URL: {normalized_target}"
            )
            js_urls = [normalized_target]
            scan_target_directly = True

        self.logger.info(
            f"[{self.name}] Discovered {len(js_urls)} JavaScript source(s) for SecretFinder analysis."
        )
        if self.debug:
            self.logger.info(f"[{self.name}] JS targets: {js_urls}")

        # Step 3: Run SecretFinder for each discovered JavaScript source and collect results.
        all_findings: list[dict[str, Any]] = []
        scanned_count = 0
        failed_count = 0
        errors: list[str] = []

        for js_url in js_urls:
            self.logger.info(f"[{self.name}] Scanning JS target: {js_url}")
            file_findings, success, error_msg = self._scan_single_js(
                js_url,
                extract_mode=scan_target_directly,
            )
            if success:
                scanned_count += 1
            else:
                failed_count += 1
                if error_msg:
                    errors.append(error_msg)

            all_findings.extend(file_findings)
            if file_findings:
                self.logger.info(f"[{self.name}] {len(file_findings)} finding(s) discovered in {js_url}")

        # Step 4: Deduplicate and filter to meaningful findings.
        unique_findings = _dedup_findings([finding for finding in all_findings if finding.get("meaningful", True)])
        unique_findings = [finding for finding in unique_findings if _is_secret_essential(finding)]

        # Step 5: Build severity summary and write structured JSON.
        severity_counts: dict[str, int] = {"critical": 0, "high": 0, "medium": 0, "low": 0, "informational": 0}
        for finding in unique_findings:
            sev = finding.get("severity", "informational").lower()
            severity_counts[sev] = severity_counts.get(sev, 0) + 1

        output_file = self.output_dir / "secrets.json"
        self._write_secrets_json(unique_findings, output_file)

        self.logger.info(
            f"[{self.name}] Scan complete — JS targets: {len(js_urls)} total / {scanned_count} scanned / {failed_count} failed | "
            f"Unique findings: {len(unique_findings)}"
        )
        if errors:
            self.logger.warning(f"[{self.name}] Encountered {len(errors)} execution error(s): {'; '.join(errors)}")

        files_with_findings = len({finding.get("url") for finding in unique_findings if finding.get("url")})

        return {
            "status": "success",
            "js_files_total": len(js_urls),
            "js_files_scanned": scanned_count,
            "js_files_failed": failed_count,
            "files_with_findings": files_with_findings,
            "secrets_found": len(unique_findings),
            "findings": unique_findings,
            "severity_counts": severity_counts,
            "output_file": str(output_file.resolve()),
            "errors": errors,
        }

    def _scan_single_js(
        self, js_url: str, extract_mode: bool = False
    ) -> tuple[list[dict[str, Any]], bool, str]:
        """Executes SecretFinder for one target and returns parsed findings plus an error message if needed."""
        timeout = getattr(self.config, "secretfinder_timeout", JS_SCAN_TIMEOUT)
        output_fmt = getattr(self.config, "secretfinder_output_format", "cli")
        regex_filter = getattr(self.config, "secretfinder_regex_filter", None)

        start = time.time()
        res = run_secretfinder(
            target_url=js_url,
            extract_mode=extract_mode,
            output_format=output_fmt,
            timeout=timeout,
            custom_python=str(self.venv_python),
            script_path=str(self.script_path),
            regex_filter=regex_filter,
            debug=self.debug,
        )
        duration = round(time.time() - start, 2)

        if res.exit_code != 0:
            error_msg = res.stderr.strip() or f"SecretFinder exited with code {res.exit_code}"
            self.logger.warning(
                f"[{self.name}] SecretFinder failed for {js_url} (exit {res.exit_code}, duration {duration}s): {error_msg}"
            )
            if self.debug and res.stdout:
                self.logger.debug(f"[{self.name}] SecretFinder stdout for {js_url}: {res.stdout}")
            if self.debug and res.stderr:
                self.logger.debug(f"[{self.name}] SecretFinder stderr for {js_url}: {res.stderr}")
            return [], False, error_msg

        findings = self.parse_output(res.stdout, js_url)
        self.logger.debug(
            f"[{self.name}] Scanned {js_url} in {duration}s — exit code {res.exit_code}, {len(findings)} finding(s)"
        )
        return findings, True, ""


    def parse_output(self, raw_output: str, source_url: str = "") -> list[dict[str, Any]]:
        """Parses SecretFinder CLI output into structured findings while preserving evidence and source URL."""
        findings: list[dict[str, Any]] = []

        if not raw_output or not raw_output.strip():
            return findings

        current_url = source_url
        for line in raw_output.splitlines():
            line = line.strip()
            if not line:
                continue

            url_match = re.match(r"^\[\s*[\+\-\*!]\s*\]\s*URL:\s*(.+)$", line, re.IGNORECASE)
            if url_match:
                current_url = url_match.group(1).strip()
                continue

            if line.startswith("---") or line.startswith("==="):
                continue

            rule_name = ""
            matched_val = line
            line_number: int | None = None

            if "->" in line:
                parts = line.split("->", 1)
                rule_name = parts[0].strip()
                matched_val = parts[1].strip()

            if "line" in line.lower():
                line_no_match = re.search(r"(?i)\bline\s*[:#=]\s*(\d+)", line)
                if line_no_match:
                    line_number = int(line_no_match.group(1))

            if rule_name and rule_name in SECRETFINDER_NATIVE_MAP:
                secret_type, severity, confidence = SECRETFINDER_NATIVE_MAP[rule_name]
            else:
                secret_type, severity, confidence = _classify_secret(matched_val or line)

            normalized_severity = _normalize_severity(severity)
            matched_text = matched_val or line
            masked_value = _mask_value(matched_text)
            meaningful = _looks_meaningful(matched_text, secret_type)

            finding = {
                "url": current_url,
                "secret_type": secret_type,
                "severity": normalized_severity,
                "severity_raw": severity,
                "value": _truncate_value(matched_text, max_len=240),
                "masked_value": _truncate_value(masked_value, max_len=240),
                "raw_value": matched_text,
                "line_number": line_number,
                "raw_line": line,
                "confidence": confidence,
                "meaningful": meaningful or bool(rule_name),
            }
            findings.append(finding)

        return findings

    def _write_secrets_json(
        self,
        findings: list[dict[str, Any]],
        output_file: Path,
    ) -> None:
        """
        Persists deduplicated findings to secrets.json.
        """
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(findings, f, indent=4, ensure_ascii=False)
            self.logger.info(f"[{self.name}] Secrets JSON saved to: {output_file.resolve()}")
        except OSError as exc:
            self.logger.error(f"[{self.name}] Failed to write secrets.json: {exc}")
