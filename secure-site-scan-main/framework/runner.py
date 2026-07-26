import logging
from typing import Any

from framework.config import Config
from framework.printer import (
    print_final_summary,
    print_httpx_results,
    print_katana_results,
    print_nmap_results,
    print_nuclei_results,
    print_subfinder_results,
    print_testssl_results,
    print_whatweb_results,
)
from framework.reporter import ReportEngine
from modules.recon import (
    HttpxScanner,
    KatanaScanner,
    NmapScanner,
    SubfinderScanner,
    WhatWebScanner,
)
from modules.scanners import NucleiScanner, TestSslScanner


class ScanOrchestrator:
    """
    Orchestrates execution workflow of reconnaissance and vulnerability assessment tool modules.
    Prints detailed colored CLI output after each tool run.
    """

    def __init__(self, config: Config, logger: logging.Logger) -> None:
        self.config = config
        self.logger = logger
        self.reporter = ReportEngine(config, logger)

    def _run_tool(self, key: str, tool: Any, results: dict) -> None:
        """
        Runs a single tool module, stores results, and catches exceptions safely.
        """
        try:
            results[key] = tool.run()
        except Exception as err:
            self.logger.error(f"Error running tool '{tool.name}': {err}")
            results[key] = {"status": "error", "reason": str(err)}

    def execute_scan_pipeline(self) -> dict[str, Any]:
        """
        Executes complete multi-phase assessment lifecycle:
        1. Reconnaissance Phase (Subfinder, HTTPX, Nmap, WhatWeb, Katana)
        2. Vulnerability Scanning Phase (TestSSL, Nuclei)
        3. Report Generation Phase (JSON, Markdown, HTML)
        """
        self.logger.info(f"=== Starting Assessment Pipeline on Target: {self.config.target} ===")

        # ─── Phase 1: Reconnaissance & Enumeration ─────────────────────────────
        self.logger.info("--> [Phase 1/2] Launching Reconnaissance & Service Enumeration Tools...")
        recon_results: dict[str, Any] = {}

        # Subfinder
        subfinder = SubfinderScanner(self.config, self.logger)
        self._run_tool("subfinder", subfinder, recon_results)
        print_subfinder_results(recon_results["subfinder"])

        # HTTPX
        httpx = HttpxScanner(self.config, self.logger)
        self._run_tool("httpx", httpx, recon_results)
        print_httpx_results(recon_results["httpx"])

        # Nmap
        nmap = NmapScanner(self.config, self.logger)
        self._run_tool("nmap", nmap, recon_results)
        print_nmap_results(recon_results["nmap"])

        # WhatWeb
        whatweb = WhatWebScanner(self.config, self.logger)
        self._run_tool("whatweb", whatweb, recon_results)
        print_whatweb_results(recon_results["whatweb"])

        # Katana
        katana = KatanaScanner(self.config, self.logger)
        self._run_tool("katana", katana, recon_results)
        print_katana_results(recon_results["katana"])

        # ─── Phase 2: Vulnerability Assessment ─────────────────────────────────
        self.logger.info("--> [Phase 2/2] Launching Vulnerability Scanners...")
        scan_results: dict[str, Any] = {}

        # TestSSL
        testssl = TestSslScanner(self.config, self.logger)
        self._run_tool("testssl", testssl, scan_results)
        print_testssl_results(scan_results["testssl"])

        # Nuclei
        nuclei = NucleiScanner(self.config, self.logger)
        self._run_tool("nuclei", nuclei, scan_results)
        print_nuclei_results(scan_results["nuclei"])

        # ─── Phase 3: Report Generation ────────────────────────────────────────
        self.logger.info("--> [Phase 3/3] Generating Consolidated Reports...")
        json_path  = self.reporter.generate_json_report(recon_results, scan_results)
        md_path    = self.reporter.generate_markdown_summary(recon_results, scan_results)
        html_path  = self.reporter.generate_html_report(recon_results, scan_results)

        report_paths = {
            "json":     str(json_path.resolve()),
            "markdown": str(md_path.resolve()),
            "html":     str(html_path.resolve()),
        }

        self.logger.info("=== Assessment Pipeline Execution Finished Successfully ===")
        print_final_summary(self.config.target, recon_results, scan_results, report_paths)

        return {
            "reconnaissance": recon_results,
            "vulnerabilities": scan_results,
            "reports": report_paths
        }
