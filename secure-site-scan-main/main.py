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
from framework.ui import display_banner, prompt_target


def main() -> None:
    """
    Primary CLI execution entry point.
    Displays banner, initializes logging, prompts user for target, and executes scan pipeline.
    """
    # Step 1: Render ASCII Branding Banner
    display_banner()

    # Step 2: Prompt user for target input
    target = prompt_target()

    # Step 3: Initialize Configuration Object
    config = Config(target=target)

    # Step 4: Setup Target Output Directory & Logging
    target_dir = config.get_target_output_dir()
    log_file = target_dir / "scan.log"
    logger = setup_logger(log_file=log_file)

    logger.info("Initializing Modular Vulnerability Assessment Session...")
    logger.info(f"Target Acquired: {config.target}")
    logger.info(f"Output Directory Configured: {target_dir.resolve()}")

    # Step 5: Execute Scan Orchestration Pipeline
    orchestrator = ScanOrchestrator(config, logger)
    orchestrator.execute_scan_pipeline()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"[!] Critical execution error: {err}", file=sys.stderr)
        sys.exit(1)
