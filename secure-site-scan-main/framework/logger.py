import logging
import sys
from pathlib import Path


def setup_logger(name: str = "VulnerabilityAssessmentFramework", log_file: Path | None = None, level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance with console and optional file handling.
    
    Args:
        name: Name of the logger instance.
        log_file: Optional Path object specifying file path to write log output.
        level: Logging verbosity level (default: logging.INFO).
    
    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicating handlers if re-initialized
    if logger.handlers:
        return logger

    # Console Handler Formatter
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

    # Console Handler (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # Optional File Handler
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d]: %(message)s"
        )
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

    return logger
