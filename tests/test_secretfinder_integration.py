import contextlib
import io
import logging
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from framework.config import Config
from framework.printer import print_secretfinder_results
from modules.secretfinder import SecretFinderScanner, _is_secret_essential, _mask_value, _normalize_target
from secretfinder_runner import (
    SecretFinderResult,
    get_project_root,
    get_secretfinder_paths,
    is_secretfinder_installed,
    run_secretfinder,
)


class TestSecretFinderIntegration(unittest.TestCase):
    """Unit test suite for SecretFinder built-in module integration."""

    def setUp(self):
        self.logger = logging.getLogger("TestSecretFinderLogger")
        self.config = Config(
            target="example.com",
            output_dir=Path("tests_temp_secretfinder"),
            secretfinder_timeout=30,
            secretfinder_output_format="cli",
        )

    def test_paths_and_root(self):
        root = get_project_root()
        self.assertTrue(root.exists())

        script_path, venv_python = get_secretfinder_paths(root)
        possible_script_paths = {
            root / "SecretFinder" / "SecretFinder.py",
            root / "tools" / "SecretFinder" / "SecretFinder.py",
        }
        possible_venv_paths = {
            root / "SecretFinder" / "venv" / "bin" / "python",
            root / "tools" / "SecretFinder" / "venv" / "bin" / "python",
        }

        self.assertIn(script_path, possible_script_paths)
        self.assertIn(venv_python, possible_venv_paths)

    def test_result_tuple_unpacking(self):
        res = SecretFinderResult(stdout="hello", stderr="", exit_code=0)
        stdout, stderr, code = res
        self.assertEqual(stdout, "hello")
        self.assertEqual(stderr, "")
        self.assertEqual(code, 0)
        self.assertEqual(res.returncode, 0)

    @patch("secretfinder_runner.subprocess.run")
    def test_run_secretfinder_wrapper(self, mock_subproc):
        mock_proc = MagicMock()
        mock_proc.stdout = "[ + ] URL: https://example.com/app.js\ngoogle_api\t->\tAIzaSy123456"
        mock_proc.stderr = ""
        mock_proc.returncode = 0
        mock_subproc.returncode = 0
        mock_subproc.return_value = mock_proc

        with patch("pathlib.Path.is_file", return_value=True):
            res = run_secretfinder("https://example.com/app.js", extract_mode=False)
            self.assertEqual(res.exit_code, 0)
            self.assertIn("google_api", res.stdout)

    def test_secretfinder_scanner_parse_output(self):
        scanner = SecretFinderScanner(self.config, self.logger, katana_data={})
        raw_output = (
            "[ + ] URL: https://example.com/main.js\n"
            "google_api\t->\tAIzaSyTestingKey123456789\n"
            "aws_access_key\t->\tAKIAIOSFODNN7EXAMPLE\n"
            "example\t->\tplaceholder-token\n"
        )
        findings = scanner.parse_output(raw_output, "https://example.com/main.js")
        self.assertGreaterEqual(len(findings), 2)
        self.assertEqual(findings[0]["secret_type"], "Google API Key")
        self.assertEqual(findings[0]["severity"], "critical")
        self.assertEqual(findings[1]["severity"], "critical")

    def test_essential_secret_filter_filters_low_value_findings(self):
        scanner = SecretFinderScanner(self.config, self.logger, katana_data={})
        findings = [
            {
                "url": "https://example.com/main.js",
                "secret_type": "Other Secret",
                "severity": "low",
                "raw_value": "example-placeholder-token",
                "meaningful": True,
            },
            {
                "url": "https://example.com/main.js",
                "secret_type": "Google API Key",
                "severity": "critical",
                "raw_value": "AIzaSyTestingKey123456789",
                "meaningful": True,
            },
            {
                "url": "https://example.com/main.js",
                "secret_type": "API Key",
                "severity": "medium",
                "raw_value": "api_key = '1234567890abcdef'",
                "meaningful": True,
            },
        ]
        filtered = [f for f in findings if _is_secret_essential(f)]
        self.assertEqual(len(filtered), 2)
        self.assertTrue(any(f["secret_type"] == "Google API Key" for f in filtered))
        self.assertTrue(any(f["secret_type"] == "API Key" for f in filtered))

    def test_mask_value_hides_sensitive_content(self):
        self.assertEqual(_mask_value("AIzaSyTestingKey123456789"), "AIza...6789")
        self.assertEqual(_mask_value("short"), "short")

    def test_normalize_target_adds_https_for_bare_domains(self):
        self.assertEqual(_normalize_target("example.com"), "https://example.com")
        self.assertEqual(_normalize_target("https://example.com"), "https://example.com")
        self.assertEqual(_normalize_target("example.com/app.js"), "https://example.com/app.js")

    def test_print_secretfinder_results_shows_no_sensitive_secrets_message(self):
        data = {
            "status": "success",
            "js_files_total": 2,
            "js_files_scanned": 2,
            "js_files_failed": 0,
            "secrets_found": 0,
            "findings": [],
            "severity_counts": {},
        }
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            print_secretfinder_results(data)
        output = buffer.getvalue()
        self.assertIn("No sensitive secrets detected", output)

    @patch("modules.secretfinder.prompt_install_secretfinder", return_value=False)
    @patch("modules.secretfinder.is_secretfinder_installed", return_value=False)
    def test_scanner_graceful_skip_when_missing(self, mock_installed, mock_prompt):
        scanner = SecretFinderScanner(self.config, self.logger, katana_data={})
        res = scanner.run()
        self.assertEqual(res["status"], "skipped")
        self.assertIn("reason", res)


if __name__ == "__main__":
    unittest.main()
