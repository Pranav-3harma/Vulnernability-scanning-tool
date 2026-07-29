from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ToolSpec:
    key: str
    name: str
    enabled: bool = True
    description: str = ""


_TOOL_REGISTRY: tuple[ToolSpec, ...] = (
    ToolSpec("subfinder", "Subfinder", enabled=True, description="Subdomain discovery"),
    ToolSpec("httpx", "HTTPX", enabled=True, description="HTTP service probing"),
    ToolSpec("nmap", "Nmap", enabled=True, description="Port and service enumeration"),
    ToolSpec("whatweb", "WhatWeb", enabled=True, description="Technology fingerprinting"),
    ToolSpec("katana", "Katana", enabled=True, description="Web crawling and endpoint discovery"),
    ToolSpec("secretfinder", "SecretFinder", enabled=True, description="JavaScript secret scanning"),
    ToolSpec("testssl", "TestSSL", enabled=True, description="TLS/SSL assessment"),
    ToolSpec("nuclei", "Nuclei", enabled=True, description="Vulnerability scanning"),
    ToolSpec("linkfinder", "LinkFinder", enabled=True, description="JS endpoint extraction"),
    ToolSpec("naabu", "Naabu", enabled=True, description="Fast port scanning"),
    ToolSpec("waybackurls", "WaybackURLs", enabled=False, description="Historical URL discovery"),
)

_FULL_SCAN_ORDER = (
    "subfinder",
    "httpx",
    "naabu",
    "nmap",
    "whatweb",
    "katana",
    "linkfinder",
    "secretfinder",
    "testssl",
    "nuclei",
)


def get_available_tools() -> tuple[ToolSpec, ...]:
    return _TOOL_REGISTRY


def get_full_scan_plan() -> tuple[ToolSpec, ...]:
    registry = {tool.key: tool for tool in _TOOL_REGISTRY}
    return tuple(
        registry[key]
        for key in _FULL_SCAN_ORDER
        if key in registry and registry[key].enabled
    )


def get_tool_menu_entries() -> list[dict[str, Any]]:
    return [
        {"key": tool.key, "name": tool.name, "enabled": tool.enabled, "description": tool.description}
        for tool in _TOOL_REGISTRY
    ]


def build_tool_instance(tool_key: str, config: Any, logger: Any, katana_results: dict[str, Any] | None = None) -> Any:
    """Constructs the appropriate scanner instance for a registry tool key."""
    from modules.recon import HttpxScanner, KatanaScanner, NmapScanner, SubfinderScanner, WhatWebScanner
    from modules.scanners import NucleiScanner, TestSslScanner
    from modules.secretfinder import SecretFinderScanner
    from modules.naabu import NaabuScanner
    from modules.linkfinder import LinkFinderScanner

    if tool_key == "subfinder":
        return SubfinderScanner(config, logger)
    if tool_key == "httpx":
        return HttpxScanner(config, logger)
    if tool_key == "nmap":
        return NmapScanner(config, logger)
    if tool_key == "whatweb":
        return WhatWebScanner(config, logger)
    if tool_key == "katana":
        return KatanaScanner(config, logger)
    if tool_key == "secretfinder":
        return SecretFinderScanner(config, logger, katana_data=katana_results or {})
    if tool_key == "naabu":
        return NaabuScanner(config, logger)
    if tool_key == "linkfinder":
        js_urls: list[str] = []
        try:
            if katana_results and isinstance(katana_results, dict):
                raw_candidates = []
                raw_candidates.extend(katana_results.get("js_files", []) or [])
                raw_candidates.extend(katana_results.get("endpoints", []) or [])
                for candidate in raw_candidates:
                    if not isinstance(candidate, str):
                        continue
                    c = candidate.strip()
                    if not c:
                        continue
                    if c.endswith(".js") or ".js?" in c.lower() or ".mjs" in c.lower() or ".cjs" in c.lower() or "/js/" in c.lower():
                        js_urls.append(c)
        except Exception:
            js_urls = []
        return LinkFinderScanner(config, logger, js_urls=js_urls)
    if tool_key == "testssl":
        return TestSslScanner(config, logger)
    if tool_key == "nuclei":
        return NucleiScanner(config, logger)

    raise ValueError(f"Unsupported tool key: {tool_key}")


def get_tool_printer(tool_key: str):
    """Returns the CLI printer associated with a tool key."""
    from framework.printer import (
        print_httpx_results,
        print_katana_results,
        print_nmap_results,
        print_nuclei_results,
        print_secretfinder_results,
        print_subfinder_results,
        print_testssl_results,
        print_whatweb_results,
        print_naabu_results,
        print_linkfinder_results,
    )

    printer_map = {
        "subfinder": print_subfinder_results,
        "httpx": print_httpx_results,
        "nmap": print_nmap_results,
        "whatweb": print_whatweb_results,
        "katana": print_katana_results,
        "secretfinder": print_secretfinder_results,
        "testssl": print_testssl_results,
        "nuclei": print_nuclei_results,
        "naabu": print_naabu_results,
        "linkfinder": print_linkfinder_results,
    }
    return printer_map.get(tool_key)
