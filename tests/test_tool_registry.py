import logging
import unittest

from framework.config import Config
from framework.tool_registry import build_tool_instance, get_available_tools, get_full_scan_plan, get_tool_menu_entries


class TestToolRegistry(unittest.TestCase):
    def test_full_scan_plan_contains_only_implemented_tools(self):
        plan = get_full_scan_plan()
        self.assertTrue(plan)
        self.assertIn("naabu", [tool.key for tool in plan])
        self.assertEqual([tool.key for tool in plan], ["subfinder", "httpx", "naabu", "nmap", "whatweb", "katana", "linkfinder", "secretfinder", "testssl", "nuclei"])

    def test_config_enables_naabu_by_default(self):
        self.assertTrue(Config().enable_naabu)

    def test_custom_menu_includes_implemented_and_unimplemented_tools(self):
        menu = get_tool_menu_entries()
        self.assertTrue(menu)
        self.assertIn("subfinder", [item["key"] for item in menu])
        self.assertIn("linkfinder", [item["key"] for item in menu])

    def test_available_tools_expose_registry_metadata(self):
        tools = get_available_tools()
        self.assertTrue(any(tool.key == "subfinder" and tool.enabled for tool in tools))
        self.assertTrue(any(tool.key == "linkfinder" and tool.enabled for tool in tools))

    def test_linkfinder_extracts_js_urls_from_katana_results(self):
        config = Config(target="example.com")
        logger = logging.getLogger("linkfinder-test")
        tool = build_tool_instance("linkfinder", config, logger, {"endpoints": ["https://example.com/app.js", "https://example.com/login"]})
        self.assertIn("https://example.com/app.js", tool.js_urls)


if __name__ == "__main__":
    unittest.main()
