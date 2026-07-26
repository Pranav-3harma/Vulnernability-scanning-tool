import logging
import shutil
import unittest
from pathlib import Path
from framework.config import Config
from modules.base import BaseScanner
from modules.executor import ExecutionResult, check_tool_installed, execute_command


class DummyScanner(BaseScanner):
    """Concrete implementation of BaseScanner for unit testing."""
    @property
    def name(self) -> str:
        return "Dummy Test Scanner"

    @property
    def tool_binary(self) -> str:
        return "echo"

    def run(self) -> dict:
        return {"status": "success"}

    def parse_output(self, raw_output: str) -> dict:
        return {"raw": raw_output.strip()}


class TestModule2Executor(unittest.TestCase):
    """Unit tests for subprocess executor and base scanner interface."""

    def setUp(self):
        self.logger = logging.getLogger("TestLogger")

    def test_check_tool_installed_valid(self):
        # 'echo' and 'python3' should always be installed on standard system
        self.assertTrue(check_tool_installed("echo"))
        self.assertTrue(check_tool_installed("python3"))

    def test_check_tool_installed_invalid(self):
        self.assertFalse(check_tool_installed("non_existent_tool_binary_xyz_123"))

    def test_execute_command_success(self):
        result = execute_command(["echo", "Hello World"], timeout=5, logger=self.logger)
        self.assertTrue(result.success)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Hello World", result.stdout)
        self.assertFalse(result.timed_out)

    def test_execute_command_timeout(self):
        # Run python script that sleeps longer than timeout
        result = execute_command(
            ["python3", "-c", "import time; time.sleep(3)"],
            timeout=1,
            logger=self.logger
        )
        self.assertFalse(result.success)
        self.assertTrue(result.timed_out)
        self.assertEqual(result.returncode, -1)

    def test_base_scanner_subclass(self):
        cfg = Config(target="example.com", output_dir=Path("tests_temp"))
        scanner = DummyScanner(cfg, self.logger)

        self.assertEqual(scanner.name, "Dummy Test Scanner")
        self.assertTrue(scanner.is_available())
        self.assertEqual(scanner.run(), {"status": "success"})
        self.assertEqual(scanner.parse_output("hello"), {"raw": "hello"})

        # Clean up directory recursively
        if cfg.output_dir.exists():
            shutil.rmtree(cfg.output_dir)


if __name__ == "__main__":
    unittest.main()
