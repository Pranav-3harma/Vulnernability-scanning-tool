import logging
from abc import ABC, abstractmethod
from typing import Any

from framework.config import Config
from modules.executor import check_tool_installed


class BaseScanner(ABC):
    """
    Abstract Base Class for all security tool integration modules.
    Provides standard lifecycle interfaces for execution and output parsing.
    """

    def __init__(self, config: Config, logger: logging.Logger) -> None:
        """
        Initializes base scanner with target configuration and logger.
        """
        self.config = config
        self.logger = logger
        self.target = config.target
        self.output_dir = config.get_target_output_dir()

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name of the tool module (e.g. 'Nmap Port Scanner')."""
        pass

    @property
    @abstractmethod
    def tool_binary(self) -> str:
        """Command line executable binary name (e.g. 'nmap')."""
        pass

    def is_available(self) -> bool:
        """
        Checks if the required security tool binary exists in system PATH.
        """
        installed = check_tool_installed(self.tool_binary)
        if not installed:
            self.logger.warning(
                f"Tool binary '{self.tool_binary}' for module '{self.name}' was not found in system PATH."
            )
        return installed

    @abstractmethod
    def run(self) -> dict[str, Any]:
        """
        Executes the tool scan sequence and returns structured result data.
        
        Returns:
            dict[str, Any]: Dictionary containing tool execution status and parsed findings.
        """
        pass

    @abstractmethod
    def parse_output(self, raw_output: str) -> Any:
        """
        Parses raw CLI stdout/file output into structured Python data objects.
        
        Args:
            raw_output: Raw output string from execution.
            
        Returns:
            Any: Structured parsed representation (dict, list, etc.)
        """
        pass
