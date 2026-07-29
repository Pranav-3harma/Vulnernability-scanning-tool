import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    """
    Centralized framework configuration setting.
    """
    target: str = ""
    output_dir: Path = Path("reports")
    timeout: int = 300  # Default timeout per tool execution in seconds
    verbose: bool = False
    secretfinder_timeout: int = 60
    secretfinder_output_format: str = "cli"
    secretfinder_scan_depth: int = 1
    secretfinder_regex_filter: str | None = None
    secretfinder_debug: bool = False
    # Optional Naabu integration toggle
    enable_naabu: bool = True
    naabu_timeout: int = 60
    # Nmap scan configuration
    nmap_enable_udp: bool = False
    nmap_enable_vuln_scripts: bool = True
    nmap_enable_traceroute: bool = True
    nmap_enable_version_intensity: bool = True
    nmap_scan_top_ports: int = 1000

    def get_target_output_dir(self) -> Path:
        """
        Returns target-specific folder under reports/ output path.
        Creates directory if it does not exist.
        """
        clean_target_name = (
            self.target.replace("http://", "")
            .replace("https://", "")
            .replace("/", "_")
            .strip()
        )
        target_dir = self.output_dir / clean_target_name
        target_dir.mkdir(parents=True, exist_ok=True)
        return target_dir
