import logging
import shutil
import subprocess
import sys
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
    logger: logging.Logger | None = None,
    show_progress: bool = False
) -> ExecutionResult:
    """
    Safely executes CLI commands using subprocess.run or subprocess.Popen.
    Enforces execution timeout, captures stdout/stderr, and optionally shows progress.
    
    Args:
        command: List of command line arguments (e.g. ['nmap', '-F', 'example.com']).
        timeout: Maximum execution duration in seconds.
        logger: Logger instance to output execution context.
        show_progress: Whether to display a live spinner and elapsed time.
        
    Returns:
        ExecutionResult: Structured metrics and output from execution.
    """
    cmd_str = " ".join(command)
    if logger:
        logger.debug(f"Executing: {cmd_str}")

    start_time = time.time()
    try:
        if not show_progress:
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

        spinner = ["|", "/", "-", "\\"]
        spinner_index = 0
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        while process.poll() is None:
            elapsed = round(time.time() - start_time)
            sys.stdout.write(
                f"\r  [ {spinner[spinner_index % len(spinner)]} ] Running: {command[0]}  Elapsed: {elapsed}s"
            )
            sys.stdout.flush()
            spinner_index += 1
            time.sleep(0.4)

        stdout_str, stderr_str = process.communicate(timeout=max(0, timeout - int(time.time() - start_time)))
        duration = round(time.time() - start_time, 2)
        sys.stdout.write("\r" + " " * 100 + "\r")
        sys.stdout.flush()
        success = (process.returncode == 0)

        return ExecutionResult(
            command=command,
            returncode=process.returncode,
            stdout=stdout_str,
            stderr=stderr_str,
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
