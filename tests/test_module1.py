import unittest
from pathlib import Path
from framework.config import Config
from framework.ui import validate_target


class TestModule1Core(unittest.TestCase):
    """
    Independent Unit Test Suite for Module 1 Core Infrastructure.
    """

    def test_target_validation_domain(self):
        valid, target = validate_target("example.com")
        self.assertTrue(valid)
        self.assertEqual(target, "example.com")

    def test_target_validation_subdomain(self):
        valid, target = validate_target("sub.domain.example.co.uk")
        self.assertTrue(valid)

    def test_target_validation_ip(self):
        valid, target = validate_target("192.168.1.1")
        self.assertTrue(valid)
        self.assertEqual(target, "192.168.1.1")

    def test_target_validation_url(self):
        valid, target = validate_target("https://example.com/login")
        self.assertTrue(valid)

    def test_target_validation_invalid(self):
        valid, target = validate_target("invalid..domain!!")
        self.assertFalse(valid)
        self.assertEqual(target, "")

    def test_config_target_directory_creation(self):
        cfg = Config(target="example.com", output_dir=Path("tests_temp_reports"))
        target_dir = cfg.get_target_output_dir()
        self.assertTrue(target_dir.exists())
        self.assertEqual(target_dir.name, "example.com")

        # Cleanup test folder
        if target_dir.exists():
            target_dir.rmdir()
        if cfg.output_dir.exists():
            cfg.output_dir.rmdir()


if __name__ == "__main__":
    unittest.main()
