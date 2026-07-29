import logging
import unittest
from pathlib import Path
from framework.config import Config
from modules.recon import (
    HttpxScanner,
    KatanaScanner,
    NmapScanner,
    SubfinderScanner,
    WhatWebScanner,
)


class TestModule3ReconParsers(unittest.TestCase):
    """Unit test suite for Module 3 Reconnaissance output parsers."""

    def setUp(self):
        self.logger = logging.getLogger("TestReconLogger")
        self.config = Config(target="example.com", output_dir=Path("tests_temp"))

    def test_subfinder_parse_output(self):
        scanner = SubfinderScanner(self.config, self.logger)
        raw_output = "sub1.example.com\nsub2.example.com\nsub1.example.com\n"
        subdomains = scanner.parse_output(raw_output)
        self.assertEqual(subdomains, ["sub1.example.com", "sub2.example.com"])

    def test_httpx_parse_output(self):
        scanner = HttpxScanner(self.config, self.logger)
        raw_output = '[{"url":"https://example.com","status_code":200,"title":"Example","server":"nginx","content_length":100}]'
        services = scanner.parse_output(raw_output)
        self.assertEqual(len(services), 1)
        self.assertEqual(services[0]["url"], "https://example.com")
        self.assertEqual(services[0]["status_code"], 200)

    def test_nmap_parse_output(self):
        scanner = NmapScanner(self.config, self.logger)
        xml_data = """<?xml version="1.0"?>
        <nmaprun>
          <host>
            <status state="up"/>
            <address addr="93.184.216.34"/>
            <ports>
              <port protocol="tcp" portid="80">
                <state state="open"/>
                <service name="http" product="Apache" version="2.4.41"/>
              </port>
            </ports>
          </host>
        </nmaprun>"""
        parsed = scanner.parse_output(xml_data)
        hosts = parsed.get("hosts", [])
        self.assertEqual(len(hosts), 1)
        self.assertEqual(hosts[0]["ip"], "93.184.216.34")
        self.assertEqual(hosts[0]["open_ports"][0]["port"], 80)
        self.assertEqual(hosts[0]["open_ports"][0]["service"], "http")

    def test_nmap_analysis_summary(self):
        scanner = NmapScanner(self.config, self.logger)
        host_payload = {
            "ip": "93.184.216.34",
            "all_ports": [
                {
                    "port": 21,
                    "protocol": "tcp",
                    "state": "open",
                    "service": "ftp",
                    "service_details": {
                        "raw_scripts": {"ftp-anon": "Anonymous login allowed"},
                        "ssl_tls_info": "",
                        "http_methods": "",
                        "robots": "",
                        "http_title": "",
                        "banner": "",
                    },
                }
            ],
        }
        analysis = scanner._analyze_findings([host_payload], {})
        self.assertEqual(analysis["risk_score"]["level"], "High")
        self.assertTrue(any(f["id"] == "anonymous-ftp" for f in analysis["findings"]))

    def test_whatweb_parse_output(self):
        scanner = WhatWebScanner(self.config, self.logger)
        raw_output = '{"target":"http://example.com","http_status":200,"plugins":{"Apache":{},"HTML5":{}}}'
        tech = scanner.parse_output(raw_output)
        self.assertEqual(len(tech), 1)
        self.assertIn("Apache", tech[0]["tech_names"])

    def test_katana_parse_output(self):
        scanner = KatanaScanner(self.config, self.logger)
        raw_output = 'http://example.com/api/v1\nhttp://example.com/login\n'
        endpoints = scanner.parse_output(raw_output)
        self.assertIn("http://example.com/api/v1", endpoints)
        self.assertIn("http://example.com/login", endpoints)


if __name__ == "__main__":
    unittest.main()
