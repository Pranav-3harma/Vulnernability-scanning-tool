"""
framework/printer.py

ANSI-colored CLI result printer.
Displays detailed scan results in the terminal after each tool finishes,
with red-highlighted vulnerability severity warnings.
"""

from typing import Any

# ─── ANSI Color Codes ────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
RED     = "\033[91m"
YELLOW  = "\033[93m"
ORANGE  = "\033[38;5;214m"
BLUE    = "\033[94m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
MAGENTA = "\033[95m"
GREY    = "\033[90m"
WHITE   = "\033[97m"

# ─── Severity Color Map ───────────────────────────────────────────────────────
SEVERITY_COLOR = {
    "critical": RED,
    "high":     RED,
    "warn":     ORANGE,
    "medium":   YELLOW,
    "low":      BLUE,
    "info":     GREY,
    "ok":       GREEN,
}


def _color_severity(severity: str) -> str:
    """Returns ANSI colored severity label."""
    sev_lower = severity.lower()
    color = SEVERITY_COLOR.get(sev_lower, GREY)
    return f"{BOLD}{color}{severity.upper()}{RESET}"


def _section(title: str, icon: str = "◈") -> None:
    """Prints a formatted section header."""
    print(f"\n{BOLD}{CYAN}{'─' * 70}{RESET}")
    print(f"{BOLD}{WHITE}  {icon}  {title}{RESET}")
    print(f"{BOLD}{CYAN}{'─' * 70}{RESET}")


def _ok(msg: str) -> None:
    print(f"  {GREEN}[+]{RESET} {msg}")


def _warn(msg: str) -> None:
    print(f"  {YELLOW}[!]{RESET} {msg}")


def _info(msg: str) -> None:
    print(f"  {GREY}[*]{RESET} {msg}")


def _vuln(msg: str) -> None:
    """Prints a red-highlighted vulnerability line."""
    print(f"  {BOLD}{RED}[VULN]{RESET} {msg}")


def _row(label: str, value: str, label_w: int = 22) -> None:
    """Prints a labeled key-value row."""
    print(f"  {GREY}{label:<{label_w}}{RESET}: {WHITE}{value}{RESET}")


# ─── Subfinder ───────────────────────────────────────────────────────────────

def print_subfinder_results(data: dict[str, Any]) -> None:
    """Prints Subfinder subdomain discovery results."""
    _section("SUBFINDER — Subdomain Discovery", "🌍")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'tool not installed')}")
        return

    subdomains = data.get("subdomains", [])
    _row("Status", status)
    _row("Duration", f"{data.get('duration', 0):.2f}s")
    _row("Total Found", f"{BOLD}{GREEN}{len(subdomains)}{RESET} subdomains")

    if subdomains:
        print()
        for i, sub in enumerate(subdomains, 1):
            print(f"    {GREY}{i:>4}.{RESET}  {CYAN}{sub}{RESET}")
    else:
        _warn("No subdomains discovered.")


# ─── HTTPX (curl-based) ───────────────────────────────────────────────────────

def print_httpx_results(data: dict[str, Any]) -> None:
    """Prints HTTP service probing results."""
    _section("HTTP PROBER — Service Discovery", "📡")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'tool not installed')}")
        return

    services = data.get("services", [])
    _row("Status", status)
    _row("Services Found", f"{BOLD}{GREEN}{len(services)}{RESET}")

    if not services:
        _warn("No HTTP services responded.")
        return

    for s in services:
        code = s.get("status_code", 0)
        if 200 <= code < 300:
            code_color = GREEN
        elif 300 <= code < 400:
            code_color = YELLOW
        else:
            code_color = RED

        print(f"\n  {BOLD}{'─' * 66}{RESET}")
        _row("URL", f"{CYAN}{s.get('url', '')}{RESET}")
        _row("Status Code", f"{BOLD}{code_color}{code}{RESET}")
        if s.get("title"):
            _row("Page Title", s["title"])
        if s.get("server"):
            _row("Server", f"{MAGENTA}{s['server']}{RESET}")
        if s.get("x_powered_by"):
            _row("X-Powered-By", f"{MAGENTA}{s['x_powered_by']}{RESET}")
        if s.get("content_type"):
            _row("Content-Type", s["content_type"])
        _row("Content Size", f"{s.get('content_length', 0):,} bytes")
        if s.get("hsts"):
            _ok(f"HSTS Enabled: {s['hsts']}")
        else:
            _warn("HSTS header NOT present")
        if s.get("x_frame_options"):
            _ok(f"X-Frame-Options: {s['x_frame_options']}")
        if s.get("x_content_type_options"):
            _ok(f"X-Content-Type-Options: {s['x_content_type_options']}")
        if s.get("redirect_location"):
            _info(f"Redirects to: {s['redirect_location']}")


# ─── Nmap ──────────────────────────────────────────────────────────────────────

def print_nmap_results(data: dict[str, Any]) -> None:
    """Prints Nmap port scan results with NSE script output."""
    _section("NMAP — Port & Service Discovery", "🔌")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'tool not installed')}")
        return

    hosts = data.get("hosts", [])
    _row("Status", status)
    _row("Duration", f"{data.get('duration', 0):.2f}s")
    _row("Hosts Found", f"{BOLD}{len(hosts)}{RESET}")
    if data.get("summary"):
        _info(data["summary"])

    if not hosts:
        _warn("No hosts discovered or all ports closed.")
        return

    for host in hosts:
        ip = host.get("ip", "?")
        hostname = host.get("hostname", "")
        state = host.get("state", "?")
        os_info = host.get("os", {}) or {}
        os_name = os_info.get("name", "")
        os_acc = os_info.get("accuracy", "")
        ports = host.get("open_ports", [])
        hostnames = host.get("hostnames", [])
        reverse_dns = host.get("reverse_dns", [])
        latency_ms = host.get("latency_ms")
        uptime_seconds = host.get("uptime_seconds")
        traceroute = host.get("traceroute", [])
        host_scripts = host.get("host_scripts", {})

        state_color = GREEN if state == "up" else RED
        print(f"\n  {BOLD}Host:{RESET} {CYAN}{ip}{RESET}", end="")
        if hostname:
            print(f"  ({CYAN}{hostname}{RESET})", end="")
        print(f"  State: {BOLD}{state_color}{state.upper()}{RESET}  "
              f"Open Ports: {BOLD}{GREEN}{len(ports)}{RESET}")

        if hostnames:
            _info(f"Resolved Hostnames: {', '.join(hostnames)}")
        if reverse_dns:
            _info(f"Reverse DNS: {', '.join(reverse_dns)}")
        if latency_ms is not None:
            _info(f"Latency: {latency_ms} ms")
        if uptime_seconds is not None:
            _info(f"Uptime: {uptime_seconds}s")
        if os_name:
            _info(f"OS Detection: {MAGENTA}{os_name}{RESET} (Accuracy: {os_acc or 'unknown'}%)")

        if host_scripts:
            _info("Host-level NSE script outputs:")
            for script_id, output in host_scripts.items():
                if not str(output).strip():
                    continue
                snippet = str(output).strip().replace("\n", " ")[:120]
                if len(str(output).strip()) > 120:
                    snippet += "…"
                print(f"    {GREY}[host script: {script_id}]{RESET} {DIM}{snippet}{RESET}")

        if not ports:
            _warn("No open ports found.")
            continue

        print(f"\n    {BOLD}{GREY}{'PORT':<6} {'PROTO':<6} {'SERVICE':<15} {'PRODUCT':<18} {'VERSION':<16} {'FINGERPRINT':<18} {'SCRIPTS'}{RESET}")
        print(f"    {GREY}{'─' * 120}{RESET}")

        for p in ports:
            port_state = p.get("state", "")
            pcolor = GREEN if port_state == "open" else YELLOW if port_state in {"filtered", "closed"} else GREY
            fingerprint = p.get("service_fingerprint", "")
            script_labels = ", ".join((p.get("scripts") or {}).keys()) if p.get("scripts") else ""
            print(
                f"    {BOLD}{pcolor}{str(p.get('port', '')):<6}{RESET}"
                f"{p.get('protocol', ''):<6}"
                f"{CYAN}{p.get('service', ''):<15}{RESET}"
                f"{MAGENTA}{p.get('product', ''):<18}{RESET}"
                f"{WHITE}{p.get('version', ''):<16}{RESET}"
                f"{GREY}{fingerprint:<18}{RESET}"
                f"{YELLOW}{script_labels}{RESET}"
            )

            service_details = p.get("service_details", {}) or {}
            if service_details:
                banner = service_details.get("banner", "")
                http_title = service_details.get("http_title", "")
                http_server = service_details.get("http_server_header", "")
                http_methods = service_details.get("http_methods", "")
                ssl_info = service_details.get("ssl_tls_info", "")
                robots = service_details.get("robots", "")
                if banner:
                    _info(f"      Banner: {banner}")
                if http_title:
                    _info(f"      HTTP Title: {http_title}")
                if http_server:
                    _info(f"      HTTP Server Header: {http_server}")
                if http_methods:
                    _info(f"      HTTP Methods: {http_methods}")
                if ssl_info:
                    _info(f"      SSL/TLS Info: {ssl_info}")
                if robots:
                    _info(f"      Robots.txt: {robots}")

            for script_id, script_out in (p.get("scripts") or {}).items():
                if str(script_out).strip():
                    preview = str(script_out).strip().replace("\n", " ")
                    if len(preview) > 150:
                        preview = preview[:150] + "…"
                    print(f"            {GREY}[{script_id}]{RESET} {DIM}{preview}{RESET}")

        if traceroute:
            _info("Traceroute path:")
            for hop in traceroute:
                _info(f"TTL {hop.get('ttl')} → {hop.get('ipaddr')} {hop.get('host', '')} | RTT: {hop.get('rtt')}")

    analysis = data.get("analysis", {}) or {}
    if analysis:
        _section("Nmap Analysis Summary", "🧠")
        risk_score = analysis.get("risk_score", {})
        _row("Risk Level", risk_score.get("level", "N/A"))
        _row("Risk Score", f"{risk_score.get('score', 0)}/{risk_score.get('scale_max', 'N/A')}")
        ai_summary = analysis.get("ai_summary", "")
        if ai_summary:
            print(f"\n  {WHITE}Summary:{RESET} {ai_summary}")

        findings = analysis.get("findings", [])
        if findings:
            print(f"\n  {BOLD}Top Findings:{RESET}")
            for finding in findings[:5]:
                severity = _color_severity(finding.get("severity", "informational"))
                print(f"    - {severity} {finding.get('name')} — {finding.get('explanation')}")
                print(f"      Recommendation: {finding.get('recommendation')}")


# ─── WhatWeb ──────────────────────────────────────────────────────────────────

def print_whatweb_results(data: dict[str, Any]) -> None:
    """Prints WhatWeb technology fingerprinting results."""
    _section("WHATWEB — Technology Fingerprinting", "🧩")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'tool not installed')}")
        return

    tech_stack = data.get("tech_stack", [])
    _row("Status", status)
    _row("Duration", f"{data.get('duration', 0):.2f}s")

    if not tech_stack:
        _warn("No technology fingerprints detected.")
        return

    for item in tech_stack:
        print(f"\n  {BOLD}Target:{RESET} {CYAN}{item.get('target', '')}{RESET}  "
              f"HTTP Status: {GREEN}{item.get('status', 0)}{RESET}")
        techs = item.get("technologies", [])
        if techs:
            print(f"  {BOLD}Detected Technologies ({len(techs)}):{RESET}")
            for t in techs:
                name = t.get("name", "") if isinstance(t, dict) else str(t)
                version = t.get("version", "") if isinstance(t, dict) else ""
                detail = t.get("detail", "") if isinstance(t, dict) else ""
                parts = [f"{MAGENTA}{name}{RESET}"]
                if version:
                    parts.append(f"v{YELLOW}{version}{RESET}")
                if detail:
                    parts.append(f"{DIM}({detail}){RESET}")
                _ok("  ".join(parts))


def print_naabu_results(data: dict[str, Any]) -> None:
    """Prints Naabu port discovery results."""
    _section("PORT DISCOVERY — Naabu Results", "🔎")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'tool not installed')}")
        return

    ports = data.get("ports", [])
    _row("Status", status)
    _row("Ports Found", f"{BOLD}{GREEN}{len(ports)}{RESET}")
    if not ports:
        _warn("No open ports discovered by Naabu.")
        return

    for i, p in enumerate(ports, 1):
        print(f"  {GREY}{i:>3}.{RESET} {CYAN}{p.get('ip')}{RESET}:{BOLD}{GREEN}{p.get('port')}{RESET}")


def print_linkfinder_results(data: dict[str, Any]) -> None:
    """Prints LinkFinder hidden endpoint discovery results."""
    _section("HIDDEN ENDPOINT DISCOVERY — LinkFinder", "🔗")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'tool not installed')}")
        return

    endpoints = data.get("endpoints", [])
    _row("Status", status)
    _row("Endpoints Found", f"{BOLD}{GREEN}{len(endpoints)}{RESET}")
    if not endpoints:
        _warn("No endpoints discovered by LinkFinder.")
        return

    for e in endpoints[:200]:
        etype = e.get("type", "Other")
        ep = e.get("endpoint", "")
        src = e.get("source", "")
        print(f"  {GREY}- {RESET}{CYAN}{ep}{RESET}  {MAGENTA}[{etype}]{RESET}  {DIM}{src}{RESET}")


# ─── Katana ───────────────────────────────────────────────────────────────────

def print_katana_results(data: dict[str, Any]) -> None:
    """Prints Katana web crawling results."""
    _section("KATANA — Web Crawl & Endpoint Discovery", "🕷️")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'tool not installed')}")
        return

    endpoints = data.get("endpoints", [])
    _row("Status", status)
    _row("Duration", f"{data.get('duration', 0):.2f}s")
    _row("Endpoints Found", f"{BOLD}{GREEN}{len(endpoints)}{RESET}")

    if endpoints:
        print()
        for i, ep in enumerate(endpoints, 1):
            print(f"    {GREY}{i:>4}.{RESET}  {CYAN}{ep}{RESET}")
    else:
        _warn("No endpoints crawled.")


# ─── SecretFinder ────────────────────────────────────────────────────────────

def print_secretfinder_results(data: dict[str, Any]) -> None:
    """Prints SecretFinder JavaScript secret scanning results with severity coloring."""
    _section("SECRETFINDER — JavaScript Secret Analysis", "🔑")
    status = data.get("status", "unknown")

    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'SecretFinder not available')}")
        return

    js_total   = data.get("js_files_total", 0)
    js_scanned = data.get("js_files_scanned", 0)
    js_failed  = data.get("js_files_failed", 0)
    files_with_findings = data.get("files_with_findings", 0)
    secrets    = data.get("secrets_found", 0)
    findings   = data.get("findings", [])
    sev_counts = data.get("severity_counts", {})

    _row("Status",             status)
    _row("JS Files Total",     str(js_total))
    _row("JS Files Scanned",   f"{BOLD}{GREEN}{js_scanned}{RESET}")
    _row("JS Files Failed",    f"{BOLD}{(RED if js_failed else GREY)}{js_failed}{RESET}")
    _row("Files With Findings", f"{BOLD}{(RED if files_with_findings else GREEN)}{files_with_findings}{RESET}")
    _row("Meaningful Findings", f"{BOLD}{(RED if secrets else GREEN)}{secrets}{RESET}")

    if sev_counts:
        print()
        _row("Critical",       f"{BOLD}{RED}{sev_counts.get('critical', 0)}{RESET}")
        _row("High",           f"{BOLD}{ORANGE}{sev_counts.get('high', 0)}{RESET}")
        _row("Medium",         f"{BOLD}{YELLOW}{sev_counts.get('medium', 0)}{RESET}")
        _row("Low",            f"{BOLD}{BLUE}{sev_counts.get('low', 0)}{RESET}")

    if not findings:
        print()
        _ok("No sensitive secrets detected")
        return

    print(f"\n  {BOLD}{RED}  ⚠  {secrets} meaningful secret finding(s) detected:{RESET}")
    print(f"\n    {BOLD}{GREY}{'SEV':<8} {'TYPE':<28} {'LINE':<6} {'SOURCE URL'}{RESET}")
    print(f"    {GREY}{'─' * 90}{RESET}")

    for f in findings:
        sev = f.get("severity", "low")
        stype = f.get("secret_type", "Other Secret")
        url = f.get("url", "")
        line_number = f.get("line_number")
        value = f.get("value", "")
        sev_label = _color_severity(sev)

        short_url = url if len(url) <= 70 else "…" + url[-69:]
        line_text = str(line_number) if line_number is not None else "-"

        print(
            f"    {sev_label:<8}  "
            f"{CYAN}{stype:<28}{RESET}  "
            f"{GREY}{line_text:<6}{RESET}  "
            f"{DIM}{short_url}{RESET}"
        )
        if value:
            print(f"    {GREY}{'':>10}↳ {WHITE}{value}{RESET}")

    if data.get("output_file"):
        print()
        _info(f"Secrets saved to: {data['output_file']}")


# ─── TestSSL ──────────────────────────────────────────────────────────────────

def print_testssl_results(data: dict[str, Any]) -> None:
    """
    Prints TestSSL comprehensive TLS/SSL audit results.
    Renders full native testssl.sh colored terminal output.
    """
    _section("TESTSSL — Comprehensive TLS/SSL Security Audit", "🔒")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'testssl not installed')}")
        _info("Install with: sudo apt install testssl.sh")
        return

    raw_stdout = data.get("raw_stdout", "")
    if raw_stdout and raw_stdout.strip():
        print(raw_stdout)
        return

    findings = data.get("findings", [])
    summary = data.get("summary", {})
    _row("Status", status)
    _row("Duration", f"{data.get('duration', 0):.2f}s")
    _row("Total Findings", f"{BOLD}{len(findings)}{RESET}")

    grade = summary.get("grade", "")
    if grade:
        grade_color = GREEN if grade.startswith(("A")) else (YELLOW if grade.startswith("B") else RED)
        _row("Overall Grade", f"{BOLD}{grade_color}{grade}{RESET}")

    # Print summary warnings first
    warnings = summary.get("warnings", [])
    if warnings:
        print(f"\n  {BOLD}{RED}  ⚠  {len(warnings)} Security Alerts:{RESET}")
        for w in warnings:
            cve_str = ""
            if w.get("cve"):
                cve_str = f"  CVE: {BOLD}{RED}{', '.join(w['cve'])}{RESET}"
            _vuln(
                f"{_color_severity(w['severity'])} | {CYAN}{w['id']}{RESET} | "
                f"{WHITE}{w['finding']}{RESET}{cve_str}"
            )

    if not findings:
        _ok("No issues found. TLS/SSL configuration appears secure.")
        return

    # Group all findings by category
    from collections import defaultdict
    by_category: dict[str, list] = defaultdict(list)
    for f in findings:
        by_category[f.get("category", "General")].append(f)

    # Print categories in a logical order
    category_order = [
        "Protocol Support", "Cipher Suite", "Weak Cipher",
        "Perfect Forward Secrecy", "Certificate", "Certificate Transparency",
        "HTTP Security Header", "Session Management", "Configuration",
        "Vulnerability", "DNS / Certificate", "Server Configuration",
        "Overall Assessment", "General"
    ]

    for cat in category_order:
        cat_findings = by_category.get(cat, [])
        if not cat_findings:
            continue

        print(f"\n  {BOLD}{YELLOW}  [{cat}]{RESET}")
        for f in cat_findings:
            sev = f.get("severity", "INFO")
            fid = f.get("id", "")
            text = f.get("finding", "")
            cve_list = f.get("cve", [])

            if sev in ("HIGH", "CRITICAL"):
                _vuln(f"{_color_severity(sev)} | {CYAN}{fid}{RESET} → {BOLD}{RED}{text}{RESET}")
                if cve_list:
                    for cve in cve_list:
                        print(f"             {BOLD}{RED}CVE: {cve}{RESET}")
            elif sev in ("MEDIUM", "WARN"):
                _warn(f"{_color_severity(sev)} | {CYAN}{fid}{RESET} → {YELLOW}{text}{RESET}")
            elif sev == "LOW":
                _info(f"{_color_severity(sev)} | {CYAN}{fid}{RESET} → {text}")
            else:
                # INFO / OK - print full detail without truncation
                print(f"    {GREY}{fid:<35}{RESET}  {WHITE}{text}{RESET}")


# ─── Nuclei ───────────────────────────────────────────────────────────────────

def print_nuclei_results(data: dict[str, Any]) -> None:
    """Prints Nuclei vulnerability findings with red severity highlighting."""
    _section("NUCLEI — Vulnerability Scanner", "🔴")
    status = data.get("status", "unknown")
    if status == "skipped":
        _warn(f"Skipped: {data.get('reason', 'tool not installed')}")
        return

    vulns = data.get("vulnerabilities", [])
    _row("Status", status)
    _row("Duration", f"{data.get('duration', 0):.2f}s")
    _row("Findings", f"{BOLD}{RED if vulns else GREEN}{len(vulns)}{RESET}")

    if not vulns:
        _ok("No vulnerabilities found by Nuclei.")
        return

    for v in vulns:
        sev = v.get("severity", "info")
        cve_list = v.get("cve_id", [])
        desc = v.get("description", "")
        tags = v.get("tags", [])
        refs = v.get("reference", [])

        print(f"\n  {BOLD}{'─' * 66}{RESET}")
        print(f"  {BOLD}{WHITE}{v.get('name', '')}{RESET}  {_color_severity(sev)}")
        _row("Template ID", f"{CYAN}{v.get('template_id', '')}{RESET}")
        _row("Type", f"{MAGENTA}{v.get('type', '')}{RESET}")
        _row("Matched At", f"{YELLOW}{v.get('matched_at', '')}{RESET}")
        if cve_list:
            _vuln(f"CVE(s): {BOLD}{RED}{', '.join(cve_list)}{RESET}")
        if desc:
            _row("Description", f"{DIM}{desc[:120]}{RESET}")
        if tags:
            _info(f"Tags: {', '.join(tags)}")
        if refs:
            _info(f"References: {refs[0]}")


# ─── Final Summary ────────────────────────────────────────────────────────────

def print_final_summary(target: str, recon: dict, scan: dict, report_paths: dict) -> None:
    """Prints a structured CLI summary with a per-tool breakdown and overall highlights."""
    subdomains = recon.get("subfinder", {}).get("subdomains", [])
    services = recon.get("httpx", {}).get("services", [])
    nmap_hosts = recon.get("nmap", {}).get("hosts", [])
    whatweb_tech = recon.get("whatweb", {}).get("tech_stack", [])
    katana_endpoints = recon.get("katana", {}).get("endpoints", [])
    naabu_ports = recon.get("naabu", {}).get("ports", [])
    linkfinder_endpoints = recon.get("linkfinder", {}).get("endpoints", [])

    sf_data = recon.get("secretfinder", {})
    sf_secrets = sf_data.get("secrets_found", 0)
    sf_js_scanned = sf_data.get("js_files_scanned", 0)
    sf_files_with_finding = sf_data.get("files_with_findings", 0)
    sf_sev = sf_data.get("severity_counts", {})
    sf_critical_high = sf_sev.get("critical", 0) + sf_sev.get("high", 0)

    testssl_findings = scan.get("testssl", {}).get("findings", [])
    testssl_warnings = scan.get("testssl", {}).get("summary", {}).get("warnings", [])
    nuclei_vulns = scan.get("nuclei", {}).get("vulnerabilities", [])

    nuclei_critical = sum(
        1 for v in nuclei_vulns
        if v.get("severity", "").lower() in ("critical", "high")
    )
    tls_high = sum(
        1 for f in testssl_findings
        if f.get("severity", "").upper() in ("HIGH", "CRITICAL")
    )
    all_ports = sum(len(h.get("open_ports", [])) for h in nmap_hosts)
    tech_count = sum(len(i.get("technologies", [])) for i in whatweb_tech)

    def _tool_status_label(status: str) -> tuple[str, str]:
        status = (status or "unknown").lower()
        if status in {"success", "ok", "completed"}:
            return GREEN, "[OK]"
        if status in {"skipped", "disabled"}:
            return YELLOW, "[SKIP]"
        if status in {"error", "failed"}:
            return RED, "[ERR]"
        return GREY, "[INFO]"

    print(f"\n{BOLD}{CYAN}{'═' * 74}{RESET}")
    print(f"{BOLD}{WHITE}  📊 COMPREHENSIVE ASSESSMENT EXECUTIVE SUMMARY — {target}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * 74}{RESET}")

    print(f"\n  {BOLD}{WHITE}TOOL-BY-TOOL SUMMARY:{RESET}")
    tool_specs = [
        ("Subfinder", recon.get("subfinder", {}), f"{len(subdomains)} subdomains"),
        ("HTTPX", recon.get("httpx", {}), f"{len(services)} services"),
        ("Naabu", recon.get("naabu", {}), f"{len(naabu_ports)} open ports"),
        ("Nmap", recon.get("nmap", {}), f"{len(nmap_hosts)} hosts / {all_ports} open ports"),
        ("WhatWeb", recon.get("whatweb", {}), f"{tech_count} technologies"),
        ("Katana", recon.get("katana", {}), f"{len(katana_endpoints)} endpoints"),
        ("LinkFinder", recon.get("linkfinder", {}), f"{len(linkfinder_endpoints)} endpoints"),
        ("SecretFinder", recon.get("secretfinder", {}), f"{sf_js_scanned} JS files / {sf_secrets} findings"),
        ("TestSSL", scan.get("testssl", {}), f"{len(testssl_findings)} findings / {len(testssl_warnings)} alerts"),
        ("Nuclei", scan.get("nuclei", {}), f"{len(nuclei_vulns)} vulnerabilities"),
    ]

    for name, data, detail in tool_specs:
        color, status_symbol = _tool_status_label(data.get("status", "unknown"))
        reason = data.get("reason", "")
        print(f"  {color}{status_symbol}{RESET} {BOLD}{name:<14}{RESET}: {WHITE}{detail}{RESET}")
        if reason:
            print(f"      {GREY}{reason}{RESET}")

    print(f"\n  {BOLD}{WHITE}RECONNAISSANCE & ENUMERATION:{RESET}")
    print(f"  {GREY}{'Subdomains Discovered':<24}{RESET}: {GREEN}{BOLD}{len(subdomains)}{RESET}")
    print(f"  {GREY}{'HTTP Services Probed':<24}{RESET}: {GREEN}{BOLD}{len(services)}{RESET}")
    print(f"  {GREY}{'Open Ports Discovered':<24}{RESET}: {GREEN}{BOLD}{all_ports}{RESET}")
    print(f"  {GREY}{'Tech Stack Components':<24}{RESET}: {GREEN}{BOLD}{tech_count}{RESET}")
    print(f"  {GREY}{'Crawled Endpoints':<24}{RESET}: {GREEN}{BOLD}{len(katana_endpoints)}{RESET}")

    print(f"\n  {BOLD}{WHITE}SECRET & SENSITIVE DATA ANALYSIS:{RESET}")
    print(f"  {GREY}{'JavaScript Files Scanned':<24}{RESET}: {GREEN}{BOLD}{sf_js_scanned}{RESET}")
    print(f"  {GREY}{'Files With Findings':<24}{RESET}: {(RED + BOLD) if sf_files_with_finding else (GREEN + BOLD)}{sf_files_with_finding}{RESET}")
    print(f"  {GREY}{'Meaningful Findings':<24}{RESET}: {(RED + BOLD) if sf_secrets else (GREEN + BOLD)}{sf_secrets}{RESET}")
    if sf_secrets > 0:
        print(f"    {GREY}├── Critical Severity Secrets{RESET}    : {BOLD}{RED}{sf_sev.get('critical', 0)}{RESET}")
        print(f"    {GREY}├── High Severity Secrets{RESET}        : {BOLD}{ORANGE}{sf_sev.get('high', 0)}{RESET}")
        print(f"    {GREY}├── Medium Severity Secrets{RESET}      : {BOLD}{YELLOW}{sf_sev.get('medium', 0)}{RESET}")
        print(f"    {GREY}└── Low / Informational Secrets{RESET}  : {GREY}{sf_sev.get('low', 0) + sf_sev.get('informational', 0)}{RESET}")

    print(f"\n  {BOLD}{WHITE}VULNERABILITY ASSESSMENT:{RESET}")
    print(f"  {GREY}{'TLS/SSL Security Alerts':<24}{RESET}: {(RED + BOLD) if testssl_warnings else (GREEN + BOLD)}{len(testssl_warnings)}{RESET}")
    print(f"  {GREY}{'TLS/SSL High/Critical Alerts':<24}{RESET}: {(RED + BOLD) if tls_high else (GREEN + BOLD)}{tls_high}{RESET}")
    print(f"  {GREY}{'Nuclei Vulnerabilities Found':<24}{RESET}: {(RED + BOLD) if nuclei_vulns else (GREEN + BOLD)}{len(nuclei_vulns)}{RESET}")

    total_critical = nuclei_critical + tls_high + sf_critical_high
    if total_critical > 0:
        print(f"\n  {BOLD}{RED}⚠  CRITICAL ACTION REQUIRED: {total_critical} High/Critical security issue(s) identified!{RESET}")

    testssl_grade = scan.get("testssl", {}).get("summary", {}).get("grade", "")
    if testssl_grade:
        gcolor = GREEN if testssl_grade.startswith("A") else (YELLOW if testssl_grade.startswith("B") else RED)
        print(f"  {GREY}{'Overall TLS Configuration Grade':<24}{RESET}: {BOLD}{gcolor}{testssl_grade}{RESET}")

    print(f"\n  {BOLD}{CYAN}{'─' * 74}{RESET}")
    print(f"  {GREEN}[+]{RESET} Consolidated JSON Report : {CYAN}{report_paths.get('json', '')}{RESET}")
    print(f"  {GREEN}[+]{RESET} Executive Markdown       : {CYAN}{report_paths.get('markdown', '')}{RESET}")
    print(f"  {GREEN}[+]{RESET} Interactive HTML Report  : {CYAN}{report_paths.get('html', '')}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * 74}{RESET}\n")
