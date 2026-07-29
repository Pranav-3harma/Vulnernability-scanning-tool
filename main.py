#!/usr/bin/env python3
"""
Modular Vulnerability Assessment Framework
Main CLI Entrypoint
"""

import sys
from pathlib import Path

from framework.config import Config
from framework.logger import setup_logger
from framework.runner import ScanOrchestrator
from framework.ui import display_banner, prompt_custom_tool, prompt_follow_up_action, prompt_scan_mode, prompt_target


def run_session(target: str) -> None:
    """Runs a full scan or a custom single-tool workflow for a given target."""
    config = Config(target=target)
    # Allow enabling Naabu at runtime via environment variable `ENABLE_NAABU` (true/1)
    import os
    ena = os.getenv("ENABLE_NAABU", "").lower()
    if ena in ("1", "true", "yes", "on"):
        config.enable_naabu = True
        # optional timeout override via NAABU_TIMEOUT
        try:
            tout = int(os.getenv("NAABU_TIMEOUT", "60"))
            config.naabu_timeout = tout
        except Exception:
            pass
    target_dir = config.get_target_output_dir()
    log_file = target_dir / "scan.log"
    logger = setup_logger(log_file=log_file)

    logger.info("Initializing Modular Vulnerability Assessment Session...")
    logger.info(f"Target Acquired: {config.target}")
    logger.info(f"Output Directory Configured: {target_dir.resolve()}")

    orchestrator = ScanOrchestrator(config, logger)
    mode = prompt_scan_mode()

    if mode == "full":
        orchestrator.execute_scan_pipeline()
    else:
        tool_key = prompt_custom_tool()
        if tool_key is None:
            return
        orchestrator.run_single_tool(tool_key)


def main() -> None:
    """
    Primary CLI execution entry point.
    Displays banner, initializes logging, prompts user for target, and executes scan pipeline.
    """
    display_banner()

    while True:
        target = prompt_target()
        run_session(target)
        action = prompt_follow_up_action()
        if action == "2":
            continue
        if action == "3":
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"[!] Critical execution error: {err}", file=sys.stderr)
        sys.exit(1)
