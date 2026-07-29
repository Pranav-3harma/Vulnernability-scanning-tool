"""
modules/naabu.py

Naabu integration for fast port discovery.

Responsibilities:
- Execute `naabu` against a host discovered by HTTPX.
- Prefer JSON output and persist to <target_output>/naabu_output.json.
- Return a list of simple {"ip","port"} mappings for downstream use.

Implementation notes:
- Uses `modules.executor.execute_command` for safe subprocess execution.
- Gracefully skips if `naabu` is not available and never raises.
"""

import json
import logging
from pathlib import Path
from typing import Any

from modules.base import BaseScanner
from modules.executor import execute_command
from modules.recon import _extract_hostname


class NaabuScanner(BaseScanner):
    """Wrapper for Naabu fast port scanner."""

    @property
    def name(self) -> str:
        return "Naabu Fast Port Scanner"

    @property
    def tool_binary(self) -> str:
        return "naabu"

    def run(self) -> dict[str, Any]:
        if not self.is_available():
            return {"status": "skipped", "reason": "naabu not installed", "ports": []}

        hostname = _extract_hostname(self.target)
        self.logger.info(f"Starting Naabu on: {hostname}")
        outputs_dir = self.output_dir / "outputs"
        try:
            outputs_dir.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        out_file = outputs_dir / "naabu.json"

        cmd = [
            self.tool_binary,
            "-host", hostname,
            "-j",
            "-silent",
            "-top-ports", "1000",
            "-o", str(out_file),
        ]

        result = execute_command(cmd, timeout=getattr(self.config, "naabu_timeout", 120), logger=self.logger)

        raw = ""
        if out_file.exists():
            try:
                raw = out_file.read_text(encoding="utf-8")
            except Exception:
                raw = result.stdout or ""
        else:
            raw = result.stdout or ""

        ports = self.parse_output(raw)

        self.logger.info(f"Naabu discovered {len(ports)} open port(s)")

        return {
            "status": "success" if (result.success or ports) else "failed",
            "duration": result.duration,
            "ports": ports,
            "count": len(ports),
            "output_file": str(out_file),
        }

    def parse_output(self, raw_output: str) -> list[dict[str, Any]]:
        """Parses Naabu JSON output. Naabu can emit one JSON object per line or a JSON array.

        Returns a list of simplified dicts: {"ip": "...", "port": 80}
        """
        results: list[dict[str, Any]] = []
        if not raw_output:
            return results

        # Try line-delimited JSON first
        for line in raw_output.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                # try whole payload once if a line is not valid JSON
                try:
                    obj = json.loads(raw_output)
                    if isinstance(obj, list):
                        for item in obj:
                            ip = item.get("ip") or item.get("host") or item.get("address")
                            port = item.get("port") or item.get("port_number")
                            if ip and port:
                                results.append({"ip": ip, "port": int(port)})
                        return results
                except json.JSONDecodeError:
                    continue
                break

            # Naabu JSON lines often include "ip" and "ports" or just "ip" and "port"
            ip = obj.get("ip") or obj.get("host") or obj.get("address")
            port = obj.get("port") or obj.get("port_number") or obj.get("ports")
            if isinstance(port, list):
                for p in port:
                    try:
                        pnum = int(p.get("port")) if isinstance(p, dict) else int(p)
                        results.append({"ip": ip, "port": pnum})
                    except Exception:
                        continue
            else:
                try:
                    if ip and port:
                        results.append({"ip": ip, "port": int(port)})
                except Exception:
                    continue

        # Deduplicate
        seen = set()
        deduped = []
        for r in results:
            key = (r.get("ip"), r.get("port"))
            if key not in seen:
                seen.add(key)
                deduped.append(r)

        return deduped
