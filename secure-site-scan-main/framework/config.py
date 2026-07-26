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
