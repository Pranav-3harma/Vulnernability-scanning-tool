import logging
from typing import Any

from framework.config import Config
from framework.printer import print_final_summary
from framework.reporter import ReportEngine
from framework.tool_registry import build_tool_instance, get_full_scan_plan, get_tool_printer


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
        Executes complete multi-phase assessment lifecycle or a single selected tool.
        """
        self.logger.info(f"=== Starting Assessment Pipeline on Target: {self.config.target} ===")
        recon_results: dict[str, Any] = {}
        scan_results: dict[str, Any] = {}

        plan = list(get_full_scan_plan())
        if getattr(self.config, "enable_naabu", True):
            from framework.tool_registry import get_available_tools
            registry = {t.key: t for t in get_available_tools()}
            if "naabu" in registry and "naabu" not in [t.key for t in plan]:
                try:
                    idx = [t.key for t in plan].index("httpx")
                except ValueError:
                    idx = 1
                plan.insert(idx + 1, registry["naabu"])

        for tool_spec in plan:
            self.logger.info(f"--> Running module: {tool_spec.name}")
            tool = build_tool_instance(tool_spec.key, self.config, self.logger, recon_results.get("katana"))
            if tool_spec.key in {"secretfinder", "linkfinder"}:
                self._run_tool(tool_spec.key, tool, recon_results)
            else:
                self._run_tool(tool_spec.key, tool, recon_results if tool_spec.key in {"subfinder", "httpx", "nmap", "whatweb", "katana"} else scan_results)

            printer = get_tool_printer(tool_spec.key)
            if printer is not None:
                if tool_spec.key in {"subfinder", "httpx", "naabu", "nmap", "whatweb", "katana", "linkfinder", "secretfinder"}:
                    printer(recon_results.get(tool_spec.key, {}))
                else:
                    printer(scan_results.get(tool_spec.key, {}))

        self.logger.info("--> Generating Consolidated Reports...")
        report_paths = {
            "json": str((self.config.get_target_output_dir() / "report.json").resolve()),
            "markdown": str((self.config.get_target_output_dir() / "summary.md").resolve()),
            "html": str((self.config.get_target_output_dir() / "report.html").resolve()),
        }

        try:
            json_path = self.reporter.generate_json_report(recon_results, scan_results)
            report_paths["json"] = str(json_path.resolve())
        except Exception as err:
            self.logger.error(f"Failed to generate JSON report: {err}")

        try:
            md_path = self.reporter.generate_markdown_summary(recon_results, scan_results)
            report_paths["markdown"] = str(md_path.resolve())
        except Exception as err:
            self.logger.error(f"Failed to generate Markdown summary: {err}")

        try:
            html_path = self.reporter.generate_html_report(recon_results, scan_results)
            report_paths["html"] = str(html_path.resolve())
        except Exception as err:
            self.logger.error(f"Failed to generate HTML report: {err}")

        self.logger.info("=== Assessment Pipeline Execution Finished ===")
        print_final_summary(self.config.target, recon_results, scan_results, report_paths)

        return {
            "reconnaissance": recon_results,
            "vulnerabilities": scan_results,
            "reports": report_paths,
        }

    def run_single_tool(self, tool_key: str) -> dict[str, Any]:
        """Runs one tool module and prints its output using the shared printer."""
        self.logger.info(f"--> Running selected module: {tool_key}")
        results: dict[str, Any] = {}
        tool = build_tool_instance(tool_key, self.config, self.logger, {})
        self._run_tool(tool_key, tool, results)

        printer = get_tool_printer(tool_key)
        if printer is not None:
            printer(results.get(tool_key, {}))

        return results
