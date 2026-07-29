import sys
from pathlib import Path

# Ensure root directory is in sys.path
_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from secretfinder_runner import (
    SecretFinderResult,
    get_project_root,
    get_secretfinder_paths,
    is_secretfinder_installed,
    run_secretfinder,
)

__all__ = [
    "SecretFinderResult",
    "get_project_root",
    "get_secretfinder_paths",
    "is_secretfinder_installed",
    "run_secretfinder",
]
