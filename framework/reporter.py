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
        """
        summary_file = self.output_dir / "summary.md"
        
        lines = [
            f"# Security Assessment Report: {self.config.target}",
            f"**Generated Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "\n---\n",
            "## Executive Summary",
            f"- **Target:** `{self.config.target}`",
            f"- **Subdomains Discovered:** {len(recon_data.get('subfinder', {}).get('subdomains', []))}",
            f"- **Live Web Endpoints (HTTPX):** {len(recon_data.get('httpx', {}).get('services', []))}",
            f"- **Crawled Endpoints (Katana):** {len(recon_data.get('katana', {}).get('endpoints', []))}",
            f"- **Nuclei Findings Count:** {len(scan_data.get('nuclei', {}).get('vulnerabilities', []))}",
            f"- **TLS/SSL Security Alerts:** {len(scan_data.get('testssl', {}).get('findings', []))}",
            "\n---\n",
            "## 1. Discovered Ports & Services (Nmap)",
        ]

        nmap_hosts = recon_data.get("nmap", {}).get("hosts", [])
        if not nmap_hosts:
            lines.append("No open ports reported or scan skipped.")
        else:
            for host in nmap_hosts:
                lines.append(f"\n### Host: `{host.get('ip')}` (State: {host.get('state')})")
                lines.append("| Port | Protocol | State | Service | Product / Version |")
                lines.append("|---|---|---|---|---|")
                for p in host.get("open_ports", []):
                    lines.append(
                        f"| {p.get('port')} | {p.get('protocol')} | {p.get('state')} | "
                        f"{p.get('service')} | {p.get('product')} {p.get('version')} |"
                    )

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
