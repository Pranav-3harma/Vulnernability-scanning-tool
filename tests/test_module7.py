import json
import logging
import shutil
import unittest
from pathlib import Path

from framework.config import Config
from framework.reporter import ReportEngine


class TestModule7HtmlReporter(unittest.TestCase):
    """Unit test suite for Module 7 Jinja2 HTML Report Generation."""

    def setUp(self):
        self.logger = logging.getLogger("TestHtmlReporterLogger")
        self.config = Config(target="example.com", output_dir=Path("tests_temp_html_reports"))
        self.reporter = ReportEngine(self.config, self.logger)

    def test_html_report_generation(self):
        recon_data = {
            "subfinder": {"subdomains": ["sub1.example.com"]},
            "httpx": {"services": [{"url": "https://example.com", "status_code": 200, "title": "Test Title", "webserver": "nginx"}]},
            "nmap": {"hosts": [{"ip": "93.184.216.34", "state": "up", "open_ports": [{"port": 80, "protocol": "tcp", "state": "open", "service": "http", "product": "Nginx", "version": "1.18"}]}]},
            "katana": {"endpoints": ["https://example.com/login"]}
        }
        scan_data = {
            "nuclei": {"vulnerabilities": [{"name": "Test Vulnerability", "severity": "critical", "matched_at": "https://example.com", "template_id": "test-id"}]},
            "testssl": {"findings": []}
        }

        html_file = self.reporter.generate_html_report(recon_data, scan_data)
        self.assertTrue(html_file.exists())

        content = html_file.read_text(encoding="utf-8")
        self.assertIn("example.com", content)
        self.assertIn("Vulnerability Assessment Report", content)
        self.assertIn("Test Vulnerability", content)
        self.assertIn("sev-critical", content)

        # Cleanup
        if self.config.output_dir.exists():
            shutil.rmtree(self.config.output_dir)


if __name__ == "__main__":
    unittest.main()
