import logging
import unittest
from pathlib import Path
from framework.config import Config
from modules.scanners import NucleiScanner, TestSslScanner


class TestModule4Scanners(unittest.TestCase):
    """Unit test suite for Module 4 Security Scanners output parsers."""

    def setUp(self):
        self.logger = logging.getLogger("TestScannersLogger")
        self.config = Config(target="example.com", output_dir=Path("tests_temp"))

    def test_testssl_parse_output(self):
        scanner = TestSslScanner(self.config, self.logger)
        raw_output = '''[
            {"id": "heartbleed", "severity": "HIGH", "finding": "Vulnerable to Heartbleed", "cve": "CVE-2014-0160"},
            {"id": "cert", "severity": "INFO", "finding": "Cert expires in 90 days"}
        ]'''
        parsed = scanner.parse_output(raw_output)
        findings = parsed["findings"]
        self.assertEqual(len(findings), 2)
        self.assertEqual(findings[0]["id"], "heartbleed")
        self.assertEqual(findings[0]["severity"], "HIGH")

    def test_nuclei_parse_output(self):
        scanner = NucleiScanner(self.config, self.logger)
        raw_output = '{"template-id":"cve-2021-44228","info":{"name":"Log4j RCE","severity":"critical","description":"Apache Log4j RCE","classification":{"cve-id":["CVE-2021-44228"]}},"matched-at":"https://example.com/login","type":"http"}\n'
        vulns = scanner.parse_output(raw_output)
        self.assertEqual(len(vulns), 1)
        self.assertEqual(vulns[0]["template_id"], "cve-2021-44228")
        self.assertEqual(vulns[0]["severity"], "critical")
        self.assertEqual(vulns[0]["name"], "Log4j RCE")


if __name__ == "__main__":
    unittest.main()
