import logging
import shutil
import subprocess
import time
from dataclasses import dataclass, field


@dataclass
class ExecutionResult:
    """
    Data structure representing the outcome of a subprocess execution.
    """
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    duration: float
    timed_out: bool = False
    success: bool = False


def check_tool_installed(binary_name: str) -> bool:
    """
    Checks if a security tool binary is installed and executable in system PATH.
    
    Args:
        binary_name: Executable command name (e.g., 'nmap', 'subfinder').
        
    Returns:
        bool: True if installed and accessible, False otherwise.
    """
    return shutil.which(binary_name) is not None


def execute_command(
    command: list[str],
    timeout: int = 300,
    logger: logging.Logger | None = None
) -> ExecutionResult:
    """
    Safely executes CLI commands using subprocess.run without shell=True.
    Enforces execution timeout and captures stdout/stderr.
    
    Args:
        command: List of command line arguments (e.g. ['nmap', '-F', 'example.com']).
        timeout: Maximum execution duration in seconds.
        logger: Logger instance to output execution context.
        
    Returns:
        ExecutionResult: Structured metrics and output from execution.
    """
    cmd_str = " ".join(command)
    if logger:
        logger.debug(f"Executing: {cmd_str}")

    start_time = time.time()
    try:
        process = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False
        )
        duration = round(time.time() - start_time, 2)
        success = (process.returncode == 0)

        return ExecutionResult(
            command=command,
            returncode=process.returncode,
            stdout=process.stdout,
            stderr=process.stderr,
            duration=duration,
            timed_out=False,
            success=success
        )

    except subprocess.TimeoutExpired as exc:
        duration = round(time.time() - start_time, 2)
        if logger:
            logger.error(f"Command timed out after {timeout} seconds: {cmd_str}")
        
        stdout_str = exc.stdout.decode('utf-8', errors='ignore') if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr_str = exc.stderr.decode('utf-8', errors='ignore') if isinstance(exc.stderr, bytes) else (exc.stderr or "")

        return ExecutionResult(
            command=command,
            returncode=-1,
            stdout=stdout_str,
            stderr=stderr_str,
            duration=duration,
            timed_out=True,
            success=False
        )

    except Exception as exc:
        duration = round(time.time() - start_time, 2)
        if logger:
            logger.error(f"Failed to execute command '{cmd_str}': {exc}")

        return ExecutionResult(
            command=command,
            returncode=-1,
            stdout="",
            stderr=str(exc),
            duration=duration,
            timed_out=False,
            success=False
        )
