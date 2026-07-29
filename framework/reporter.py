import json
from datetime import datetime
from pathlib import Path
from typing import Any

from framework.config import Config

try:
    from jinja2 import Environment, FileSystemLoader
    JINJA_AVAILABLE = True
except ImportError:
    JINJA_AVAILABLE = False


class ReportEngine:
    """
    Structured Report Generation Engine.
    Aggregates reconnaissance and vulnerability scanning findings into JSON, Markdown, and HTML reports.
    """

    def __init__(self, config: Config, logger: Any) -> None:
        self.config = config
        self.logger = logger
        self.output_dir = config.get_target_output_dir()
        self.templates_dir = Path(__file__).parent.parent / "templates"

    def generate_json_report(
        self,
        recon_data: dict[str, Any],
        scan_data: dict[str, Any]
    ) -> Path:
        """
        Aggregates scan findings into a unified, structured JSON report file.
        """
        report_file = self.output_dir / "report.json"
        
        master_report = {
            "metadata": {
                "target": self.config.target,
                "timestamp": datetime.now().isoformat(),
                "scanner_version": "1.0.0"
            },
            "reconnaissance": recon_data,
            "vulnerabilities": scan_data
        }

        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(master_report, f, indent=4)

        self.logger.info(f"Master JSON report generated at: {report_file.resolve()}")
        return report_file

    def generate_markdown_summary(
        self,
        recon_data: dict[str, Any],
        scan_data: dict[str, Any]
    ) -> Path:
        """
        Generates an executive human-readable Markdown summary report.
        Includes sections for Nmap, Nuclei, TestSSL, and SecretFinder results.
        """
        summary_file = self.output_dir / "summary.md"

        sf_data = recon_data.get("secretfinder") or {}
        sf_secrets = sf_data.get("secrets_found", 0)

        lines = [
            f"# Security Assessment Report: {self.config.target}",
            f"**Generated Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "\n---\n",
            "## Executive Summary",
            f"- **Target:** `{self.config.target}`",
            f"- **Subdomains Discovered:** {len((recon_data.get('subfinder') or {}).get('subdomains', []))}",
            f"- **Live Web Endpoints (HTTPX):** {len((recon_data.get('httpx') or {}).get('services', []))}",
            f"- **Crawled Endpoints (Katana):** {len((recon_data.get('katana') or {}).get('endpoints', []))}",
            f"- **Secrets Found in JS Files:** {sf_secrets}",
            f"- **Nuclei Findings Count:** {len((scan_data.get('nuclei') or {}).get('vulnerabilities', []))}",
            f"- **TLS/SSL Security Alerts:** {len((scan_data.get('testssl') or {}).get('findings', []))}",
            "\n---\n",
            "## 1. Discovered Ports & Services (Nmap)",
        ]

        nmap_hosts = (recon_data.get("nmap") or {}).get("hosts", [])
        nmap_analysis = (recon_data.get("nmap") or {}).get("analysis", {})
        if nmap_analysis:
            score = nmap_analysis.get("risk_score", {})
            lines.append(f"- **Nmap Risk Level:** {score.get('level', 'N/A')} ({score.get('score', 0)}/{score.get('scale_max', 'N/A')})")
            if nmap_analysis.get("ai_summary"):
                lines.append(f"- **Nmap Analysis Summary:** {nmap_analysis.get('ai_summary')}")
            if nmap_analysis.get("recommendations"):
                lines.append(f"- **Top Recommendations:** {', '.join(nmap_analysis.get('recommendations', [])[:3])}")

        if not nmap_hosts:
            lines.append("No open ports reported or scan skipped.")
        else:
            for host in nmap_hosts:
                hostnames = ", ".join(host.get("hostnames", [])) if host.get("hostnames") else "—"
                reverse_dns = ", ".join(host.get("reverse_dns", [])) if host.get("reverse_dns") else "—"
                latency = f"{host.get('latency_ms')} ms" if host.get('latency_ms') is not None else "—"
                uptime = f"{host.get('uptime_seconds')}s" if host.get('uptime_seconds') is not None else "—"
                os_name = host.get("os", {}).get("name", "Unknown")
                os_accuracy = host.get("os", {}).get("accuracy", "—")

                lines.append(f"\n### Host: `{host.get('ip')}` (State: {host.get('state')})")
                lines.append(f"- Hostnames: `{hostnames}`")
                lines.append(f"- Reverse DNS: `{reverse_dns}`")
                lines.append(f"- Latency: `{latency}`")
                lines.append(f"- Uptime: `{uptime}`")
                lines.append(f"- OS: `{os_name}` (Accuracy: `{os_accuracy}%`) ")

                if host.get("host_scripts"):
                    script_ids = ", ".join(host.get("host_scripts", {}).keys())
                    lines.append(f"- Host NSE scripts: `{script_ids}`")

                if host.get("traceroute"):
                    lines.append("- Traceroute hops:")
                    for hop in host.get("traceroute", []):
                        lines.append(
                            f"  - TTL `{hop.get('ttl')}` → `{hop.get('ipaddr')}` "
                            f"({hop.get('host') or 'n/a'}) RTT `{hop.get('rtt')}`"
                        )

                open_ports = host.get("open_ports", [])
                if open_ports:
                    lines.append("")
                    lines.append("| Port | Protocol | State | Service | Product / Version | Banner | Scripts |")
                    lines.append("|---|---|---|---|---|---|---|")
                    for p in open_ports:
                        banner = p.get("service_details", {}).get("banner", "") or " ".join([v for v in [p.get("product", ""), p.get("version", ""), p.get("extra_info", "") ] if v]).strip()
                        scripts = ", ".join(p.get("scripts", {}).keys()) if p.get("scripts") else "—"
                        banner = banner.replace("|", "\\|")
                        lines.append(
                            f"| {p.get('port')} | {p.get('protocol')} | {p.get('state')} | "
                            f"{p.get('service')} | {p.get('product')} {p.get('version')} | {banner} | {scripts} |"
                        )
                else:
                    lines.append("No open ports detected on this host.")

        lines.extend([
            "\n---\n",
            "## 2. Vulnerability Assessment Findings (Nuclei)",
        ])

        nuclei_vulns = scan_data.get("nuclei", {}).get("vulnerabilities", [])
        if not nuclei_vulns:
            lines.append("No vulnerabilities identified by Nuclei.")
        else:
            lines.append("| Severity | Vulnerability Name | Matched Location | Template ID |")
            lines.append("|---|---|---|---|")
            for v in nuclei_vulns:
                lines.append(
                    f"| **{v.get('severity', '').upper()}** | {v.get('name')} | `{v.get('matched_at')}` | `{v.get('template_id')}` |"
                )

        lines.extend([
            "\n---\n",
            "## 3. TLS/SSL Security Audit Details (testssl)",
        ])

        testssl_findings = scan_data.get("testssl", {}).get("findings", [])
        if not testssl_findings:
            lines.append("No TLS/SSL audit findings recorded.")
        else:
            lines.append("| Category | Severity | Test ID | Finding Details | CVE |")
            lines.append("|---|---|---|---|---|")
            for f in testssl_findings:
                cve_str = ", ".join(f.get("cve", [])) if f.get("cve") else "—"
                lines.append(
                    f"| {f.get('category', 'General')} | **{f.get('severity', 'INFO')}** | `{f.get('id', '')}` | {f.get('finding', '')} | {cve_str} |"
                )

        # ── Section 4: JavaScript Secret Analysis ────────────────────────────
        lines.extend([
            "\n---\n",
            "## 4. JavaScript Secret Analysis (SecretFinder)",
        ])

        # ── Section 5: Port Discovery (Naabu) ─────────────────────────────
        naabu_data = recon_data.get("naabu", {})
        naabu_ports = naabu_data.get("ports", [])
        lines.extend([
            "\n---\n",
            "## 5. Port Discovery (Naabu)",
        ])
        if not naabu_ports:
            lines.append("No ports discovered by Naabu or scan skipped.")
        else:
            lines.append(f"- Total ports discovered: {len(naabu_ports)}")
            for p in naabu_ports:
                lines.append(f"  - `{p.get('ip')}`:`{p.get('port')}`")

        # ── Section 6: Hidden Endpoint Discovery (LinkFinder) ─────────────
        link_data = recon_data.get("linkfinder", {})
        link_eps = link_data.get("endpoints", [])
        lines.extend([
            "\n---\n",
            "## 6. Hidden Endpoint Discovery (LinkFinder)",
        ])
        if not link_eps:
            lines.append("No hidden endpoints discovered or LinkFinder skipped.")
        else:
            lines.append(f"- Total endpoints discovered: {len(link_eps)}")
            for e in link_eps[:200]:
                lines.append(f"  - `{e.get('endpoint')}` ({e.get('type')})  — source: {e.get('source')}")

        sf_status   = sf_data.get("status", "skipped")
        sf_total    = sf_data.get("js_files_total", 0)
        sf_scanned  = sf_data.get("js_files_scanned", 0)
        sf_failed   = sf_data.get("js_files_failed", 0)
        sf_sev      = sf_data.get("severity_counts", {})
        sf_findings = sf_data.get("findings", [])

        if sf_status == "skipped":
            reason = sf_data.get("reason", "SecretFinder not available")
            lines.append(f"> **Skipped:** {reason}")
        else:
            lines.extend([
                "",
                "### Scan Statistics",
                "",
                "| Metric | Value |",
                "|---|---|",
                f"| Status | `{sf_status}` |",
                f"| Total JavaScript Files | {sf_total} |",
                f"| Files Successfully Scanned | {sf_scanned} |",
                f"| Files Failed / Timed Out | {sf_failed} |",
                f"| **Secrets Found** | **{sf_secrets}** |",
                f"| Critical | {sf_sev.get('critical', 0)} |",
                f"| High | {sf_sev.get('high', 0)} |",
                f"| Medium | {sf_sev.get('medium', 0)} |",
                f"| Low | {sf_sev.get('low', 0)} |",
                f"| Informational | {sf_sev.get('informational', 0)} |",
            ])

            if not sf_findings:
                lines.append("\n✅ No secrets discovered in JavaScript files.")
            else:
                lines.extend([
                    "",
                    "### Findings",
                    "",
                    "| Severity | Secret Type | Source JavaScript URL | Matched Value (truncated) | Confidence |",
                    "|---|---|---|---|---|",
                ])
                for finding in sf_findings:
                    sev   = finding.get("severity", "informational").upper()
                    stype = finding.get("secret_type", "Other Secret")
                    url   = finding.get("url", "")
                    value = finding.get("value", "")
                    conf  = finding.get("confidence", "low")
                    # Truncate value at 50 chars for Markdown table readability
                    trunc = (value[:50] + "…") if len(value) > 50 else value
                    # Escape pipe characters that would break the Markdown table
                    trunc = trunc.replace("|", "\\|")
                    lines.append(f"| **{sev}** | {stype} | `{url}` | `{trunc}` | {conf} |")

        with open(summary_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        self.logger.info(f"Executive Markdown summary generated at: {summary_file.resolve()}")
        return summary_file

    def generate_html_report(
        self,
        recon_data: dict[str, Any],
        scan_data: dict[str, Any]
    ) -> Path:
        """
        Renders Jinja2 HTML report from templates/report_template.html.
        """
        html_file = self.output_dir / "report.html"

        if not JINJA_AVAILABLE:
            self.logger.warning("Jinja2 is not installed. Skipping HTML report rendering.")
            return html_file

        template_path = self.templates_dir / "report_template.html"
        if not template_path.exists():
            self.logger.warning(f"HTML template not found at {template_path}. Skipping HTML generation.")
            return html_file

        env = Environment(loader=FileSystemLoader(self.templates_dir), autoescape=True)
        template = env.get_template("report_template.html")

        html_content = template.render(
            target=self.config.target,
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            recon=recon_data,
            scan=scan_data
        )

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        self.logger.info(f"Professional Jinja2 HTML report generated at: {html_file.resolve()}")
        return html_file
