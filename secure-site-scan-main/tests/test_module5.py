import json
import logging
import shutil
import unittest
from pathlib import Path

from framework.config import Config
from framework.reporter import ReportEngine


class TestModule5Reporter(unittest.TestCase):
    """Unit test suite for Module 5 ReportEngine."""

    def setUp(self):
        self.logger = logging.getLogger("TestReporterLogger")
        self.config = Config(target="example.com", output_dir=Path("tests_temp_reports"))
        self.reporter = ReportEngine(self.config, self.logger)

    def test_json_and_markdown_report_generation(self):
        recon_data = {
            "subfinder": {"subdomains": ["sub1.example.com"]},
            "httpx": {"services": [{"url": "https://example.com", "status_code": 200}]},
            "nmap": {"hosts": [{"ip": "93.184.216.34", "state": "up", "open_ports": [{"port": 80, "protocol": "tcp", "state": "open", "service": "http", "product": "Nginx", "version": "1.18"}]}]},
            "katana": {"endpoints": ["https://example.com/login"]}
        }
        scan_data = {
            "nuclei": {"vulnerabilities": [{"name": "Test Vulnerability", "severity": "high", "matched_at": "https://example.com", "template_id": "test-id"}]},
            "testssl": {"findings": []}
        }

        json_file = self.reporter.generate_json_report(recon_data, scan_data)
        md_file = self.reporter.generate_markdown_summary(recon_data, scan_data)

        self.assertTrue(json_file.exists())
        self.assertTrue(md_file.exists())

        # Verify JSON report structure
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(data["metadata"]["target"], "example.com")
            self.assertIn("reconnaissance", data)
            self.assertIn("vulnerabilities", data)

        # Cleanup
        if self.config.output_dir.exists():
            shutil.rmtree(self.config.output_dir)


if __name__ == "__main__":
    unittest.main()
