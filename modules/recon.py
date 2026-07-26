"""
modules/recon.py

Reconnaissance & enumeration tool wrappers.
Covers: Subfinder, HttpProber (curl-based), Nmap, WhatWeb, Katana.
"""

import json
import shutil
import subprocess
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
    Uses: nmap -sV -sC --top-ports 1000 -T4 -oX <file> <host>
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
            "-sV",              # Service/version detection
            "-sC",              # Default scripts (banner grab, http-title, ssl-cert, etc.)
            "--top-ports", "1000",
            "-T4",              # Aggressive timing (faster)
            "--open",           # Only show open ports
            "-oX", str(out_file),
            hostname
        ]
        result = execute_command(cmd, timeout=self.config.timeout, logger=self.logger)

        xml_content = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
        if not xml_content and result.stdout:
            xml_content = result.stdout

        parsed = self.parse_output(xml_content)

        return {
            "status": "success" if (result.success or parsed.get("hosts")) else "failed",
            "duration": result.duration,
            "hosts": parsed.get("hosts", []),
            "summary": parsed.get("summary", ""),
            "output_file": str(out_file)
        }

    def parse_output(self, raw_output: str) -> dict[str, Any]:
        """Parses Nmap XML output into structured host/port dictionaries."""
        if not raw_output or not raw_output.strip():
            return {"hosts": [], "summary": ""}

        hosts = []
        summary = ""
        try:
            root = ET.fromstring(raw_output)

            # Extract run summary
            run_stats = root.find("runstats/finished")
            if run_stats is not None:
                summary = run_stats.attrib.get("summary", "")

            for host_node in root.findall("host"):
                # IP address
                addr_node = host_node.find("address[@addrtype='ipv4']")
                if addr_node is None:
                    addr_node = host_node.find("address")
                ip_addr = addr_node.attrib.get("addr", "") if addr_node is not None else ""

                # Hostname (DNS name)
                hostname_node = host_node.find("hostnames/hostname")
                dns_name = hostname_node.attrib.get("name", "") if hostname_node is not None else ""

                # Host state
                status_node = host_node.find("status")
                state = status_node.attrib.get("state", "unknown") if status_node is not None else "unknown"

                # OS Detection
                os_match = host_node.find("os/osmatch")
                os_name = os_match.attrib.get("name", "") if os_match is not None else ""
                os_acc = os_match.attrib.get("accuracy", "") if os_match is not None else ""

                ports = []
                ports_node = host_node.find("ports")
                if ports_node is not None:
                    for port_node in ports_node.findall("port"):
                        port_id = int(port_node.attrib.get("portid", 0))
                        protocol = port_node.attrib.get("protocol", "tcp")

                        port_state_node = port_node.find("state")
                        port_state = port_state_node.attrib.get("state", "") if port_state_node is not None else ""

                        if port_state != "open":
                            continue

                        service_node = port_node.find("service")
                        service_name = ""
                        product = ""
                        version = ""
                        extra_info = ""
                        tunnel = ""
                        if service_node is not None:
                            service_name = service_node.attrib.get("name", "")
                            product = service_node.attrib.get("product", "")
                            version = service_node.attrib.get("version", "")
                            extra_info = service_node.attrib.get("extrainfo", "")
                            tunnel = service_node.attrib.get("tunnel", "")

                        # NSE script output (e.g. http-title, ssl-cert)
                        scripts: dict[str, str] = {}
                        for script_node in port_node.findall("script"):
                            sid = script_node.attrib.get("id", "")
                            sout = script_node.attrib.get("output", "")
                            scripts[sid] = sout

                        ports.append({
                            "port": port_id,
                            "protocol": protocol,
                            "state": port_state,
                            "service": service_name,
                            "product": product,
                            "version": version,
                            "extra_info": extra_info,
                            "tunnel": tunnel,
                            "scripts": scripts
                        })

                hosts.append({
                    "ip": ip_addr,
                    "hostname": dns_name,
                    "state": state,
                    "os": os_name,
                    "os_accuracy": os_acc,
                    "open_ports": ports
                })

        except ET.ParseError as err:
            self.logger.error(f"Failed to parse Nmap XML: {err}")

        return {"hosts": hosts, "summary": summary}


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
