"""
modules/linkfinder.py

LinkFinder integration to discover hidden endpoints by scanning JavaScript files.

Responsibilities:
- Accept a list of JavaScript URLs (from Katana/wayback/other crawlers).
- Run LinkFinder for each unique JS URL, collect endpoints, dedupe and classify.
- Persist endpoints to <target_output>/endpoints_output.json.
- Return structured list of endpoints: {"endpoint": "/api/login", "type": "API", "source": "...js"}

Execution strategy:
- Uses subprocess via modules.executor.execute_command with timeout and capture.
- Logs per-file errors and continues scanning remaining files.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from modules.base import BaseScanner
from modules.executor import execute_command
from modules.recon import _extract_hostname


def _classify_endpoint(path: str) -> str:
    p = path.lower()
    if "graphql" in p or "gql" in p:
        return "GraphQL"
    if "/api/" in p or p.startswith("api/"):
        return "API"
    if "admin" in p or "/admin" in p:
        return "Admin"
    if "upload" in p or "fileupload" in p:
        return "Upload"
    if "auth" in p or "login" in p or "signin" in p:
        return "Auth"
    if "swagger" in p or "docs" in p:
        return "Swagger"
    if "debug" in p or "dump" in p:
        return "Debug"
    # fallback
    return "Other"


class LinkFinderScanner(BaseScanner):
    """Runs LinkFinder against JS files to extract endpoints."""

    @property
    def name(self) -> str:
        return "LinkFinder Hidden Endpoint Discovery"

    @property
    def tool_binary(self) -> str:
        return "linkfinder"

    def __init__(self, config, logger, js_urls: list[str] | None = None):
        super().__init__(config, logger)
        self.js_urls = js_urls or []

    def is_available(self) -> bool:
        candidates = ["linkfinder", "python3"]
        repo_venv = Path(__file__).resolve().parents[1] / ".venv_linkfinder" / "bin" / "python"
        if repo_venv.exists():
            candidates.append(str(repo_venv))

        for candidate in candidates:
            if candidate == "linkfinder":
                try:
                    import shutil
                    if shutil.which("linkfinder"):
                        return True
                except Exception:
                    pass
            elif candidate == "python3":
                try:
                    import subprocess
                    proc = subprocess.run(["python3", "-c", "import linkfinder"], capture_output=True, text=True, check=False)
                    if proc.returncode == 0:
                        return True
                except Exception:
                    pass
            else:
                try:
                    import subprocess
                    proc = subprocess.run([candidate, "-c", "import linkfinder"], capture_output=True, text=True, check=False)
                    if proc.returncode == 0:
                        return True
                except Exception:
                    pass
        return False

    def _get_linkfinder_command(self, js_url: str) -> list[str]:
        repo_venv = Path(__file__).resolve().parents[1] / ".venv_linkfinder" / "bin" / "python"
        if repo_venv.exists():
            return [str(repo_venv), "-m", "linkfinder", "-i", js_url, "-o", "cli"]
        if os.system("linkfinder --help >/dev/null 2>&1") == 0:
            return ["linkfinder", "-i", js_url, "-o", "cli"]
        return ["python3", "-m", "linkfinder", "-i", js_url, "-o", "cli"]

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {"status": "skipped", "reason": "linkfinder not installed or unavailable", "endpoints": []}

        if not self.js_urls:
            hostname = _extract_hostname(self.target)
            target_url = self.target if self.target.startswith(("http://", "https://")) else f"https://{hostname}"
            self.js_urls = [target_url]

        self.logger.info(f"Running LinkFinder on {len(self.js_urls)} JavaScript candidate(s)")

        unique_js = []
        seen = set()
        for u in self.js_urls:
            if u in seen:
                continue
            seen.add(u)
            unique_js.append(u)

        endpoints = []
        for js in unique_js:
            try:
                cmd = self._get_linkfinder_command(js)
                result = execute_command(cmd, timeout=getattr(self.config, "linkfinder_timeout", 30), logger=self.logger)
                raw = result.stdout or result.stderr or ""
                if not raw.strip() and js.startswith("http"):
                    try:
                        domain_cmd = [str(Path(__file__).resolve().parents[1] / ".venv_linkfinder" / "bin" / "python"), "-m", "linkfinder", "-d", "-i", js, "-o", "cli"]
                        domain_result = execute_command(domain_cmd, timeout=getattr(self.config, "linkfinder_timeout", 30), logger=self.logger)
                        raw = domain_result.stdout or domain_result.stderr or raw
                    except Exception:
                        pass

                # LinkFinder in CLI mode prints discovered endpoints line-by-line
                for line in raw.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    # Normalize to path portion if full URL
                    try:
                        parsed = urlparse(line)
                        path = parsed.path or line
                    except Exception:
                        path = line

                    etype = _classify_endpoint(path)
                    endpoints.append({"endpoint": path, "type": etype, "source": js})

            except Exception as exc:
                self.logger.error(f"LinkFinder failed on {js}: {exc}")
                continue

        # Deduplicate by endpoint
        seen_e = set()
        deduped = []
        for e in endpoints:
            key = (e.get("endpoint"), e.get("type"))
            if key not in seen_e:
                seen_e.add(key)
                deduped.append(e)

        out_file = self.output_dir / "endpoints_output.json"
        try:
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(deduped, f, indent=2)
        except Exception:
            self.logger.warning("Failed to write LinkFinder output file")

        return {"status": "success" if deduped else "failed", "count": len(deduped), "endpoints": deduped, "output_file": str(out_file)}

    def parse_output(self, raw_output: str) -> Any:
        try:
            return json.loads(raw_output)
        except Exception:
            return []
