"""
secretfinder_runner.py

Python wrapper for executing SecretFinder using its dedicated virtual environment.
Prefers a local SecretFinder/ copy in the project root and falls back to tools/SecretFinder/ if needed.
Ensures PEP 668 compliance and self-contained execution.
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import NamedTuple, Optional, Tuple


class SecretFinderResult(tuple):
    """Backward-compatible result container for SecretFinder executions."""

    def __new__(cls, stdout: str, stderr: str, exit_code: int, command: Tuple[str, ...] = (), python_bin: str = "", script_path: str = "") -> "SecretFinderResult":
        return super().__new__(cls, (stdout, stderr, exit_code))

    def __init__(self, stdout: str, stderr: str, exit_code: int, command: Tuple[str, ...] = (), python_bin: str = "", script_path: str = "") -> None:
        self.command = command
        self.python_bin = python_bin
        self.script_path = script_path

    @property
    def returncode(self) -> int:
        return self.exit_code

    @property
    def stdout(self) -> str:
        return self[0]

    @property
    def stderr(self) -> str:
        return self[1]

    @property
    def exit_code(self) -> int:
        return self[2]


def get_project_root() -> Path:
    """
    Locates the project root directory containing the local SecretFinder folder.
    """
    current_file = Path(__file__).resolve()
    candidate = current_file.parent

    for parent in [candidate, *candidate.parents]:
        if (parent / "SecretFinder" / "SecretFinder.py").exists() or \
           (parent / "tools" / "SecretFinder" / "SecretFinder.py").exists():
            return parent

    return candidate


def get_secretfinder_paths(project_root: Optional[Path] = None) -> Tuple[Path, Path]:
    """
    Returns (script_path, venv_python_path) for SecretFinder.
    """
    if project_root is None:
        project_root = get_project_root()

    local_script = project_root / "SecretFinder" / "SecretFinder.py"
    local_venv_python = project_root / "SecretFinder" / "venv" / "bin" / "python"
    tools_script = project_root / "tools" / "SecretFinder" / "SecretFinder.py"
    tools_venv_python = project_root / "tools" / "SecretFinder" / "venv" / "bin" / "python"

    if local_script.exists() or local_venv_python.exists():
        return local_script, local_venv_python

    return tools_script, tools_venv_python


def is_secretfinder_installed(project_root: Optional[Path] = None) -> bool:
    """
    Checks whether SecretFinder script and its virtual environment Python exist.
    """
    script_path, venv_python = get_secretfinder_paths(project_root)
    return script_path.is_file() and venv_python.is_file()


def run_secretfinder(
    target_url: str,
    extract_mode: bool = False,
    output_format: str = "cli",
    timeout: int = 60,
    project_root: Optional[Path] = None,
    custom_python: Optional[str] = None,
    script_path: Optional[str] = None,
    regex_filter: Optional[str] = None,
    debug: bool = False,
) -> SecretFinderResult:
    """
    Executes SecretFinder against a target URL using the venv Python binary.

    Args:
        target_url: URL of the JS file or web page to scan.
        extract_mode: If True, passes '-e' to extract JS from HTML page.
        output_format: Output format ('cli', 'json', 'html'). Default: 'cli'.
        timeout: Execution timeout in seconds. Default: 60s.
        project_root: Optional explicit project root path.
        custom_python: Optional override path to python executable.
        script_path: Optional override path to SecretFinder.py script.

    Returns:
        SecretFinderResult(stdout, stderr, exit_code)
    """
    def_script, def_python = get_secretfinder_paths(project_root)
    python_bin = Path(custom_python) if custom_python else def_python
    sf_script = Path(script_path) if script_path else def_script

    if not python_bin.is_file():
        return SecretFinderResult(
            stdout="",
            stderr=f"Error: SecretFinder venv Python not found at {python_bin}",
            exit_code=127,
        )

    if not sf_script.is_file():
        return SecretFinderResult(
            stdout="",
            stderr=f"Error: SecretFinder script not found at {sf_script}",
            exit_code=127,
        )

    cmd = [
        str(python_bin),
        str(sf_script),
        "-i", target_url,
        "-o", output_format,
    ]

    if extract_mode:
        cmd.append("-e")

    if regex_filter:
        cmd.extend(["-r", regex_filter])

    if debug:
        print(f"[SecretFinder][debug] Executed command: {' '.join(cmd)}")
        print(f"[SecretFinder][debug] Python interpreter: {python_bin}")
        print(f"[SecretFinder][debug] Target URL: {target_url}")

    try:
        proc = subprocess.run(
            cmd,
            shell=False,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        if debug:
            print(f"[SecretFinder][debug] Exit code: {proc.returncode}")
            if proc.stdout:
                print(f"[SecretFinder][debug] STDOUT:\n{proc.stdout}")
            if proc.stderr:
                print(f"[SecretFinder][debug] STDERR:\n{proc.stderr}")
        return SecretFinderResult(
            stdout=proc.stdout,
            stderr=proc.stderr,
            exit_code=proc.returncode,
            command=tuple(cmd),
            python_bin=str(python_bin),
            script_path=str(sf_script),
        )
    except subprocess.TimeoutExpired as exc:
        message = f"SecretFinder execution timed out after {timeout} seconds for {target_url}"
        if debug:
            print(f"[SecretFinder][debug] ERROR: {message}")
        return SecretFinderResult(
            stdout="",
            stderr=message,
            exit_code=124,
            command=tuple(cmd),
            python_bin=str(python_bin),
            script_path=str(sf_script),
        )
    except Exception as exc:
        message = f"Error running SecretFinder: {exc}"
        if debug:
            print(f"[SecretFinder][debug] ERROR: {message}")
        return SecretFinderResult(
            stdout="",
            stderr=message,
            exit_code=1,
            command=tuple(cmd),
            python_bin=str(python_bin),
            script_path=str(sf_script),
        )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 secretfinder_runner.py <target_url>")
        sys.exit(1)
    res = run_secretfinder(sys.argv[1])
    print(f"Exit Code: {res.exit_code}")
    print("--- STDOUT ---")
    print(res.stdout)
    print("--- STDERR ---")
    print(res.stderr)
