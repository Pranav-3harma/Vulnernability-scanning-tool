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
        os_name = host.get("os", "")
        os_acc = host.get("os_accuracy", "")
        ports = host.get("open_ports", [])

        state_color = GREEN if state == "up" else RED
        print(f"\n  {BOLD}Host:{RESET} {CYAN}{ip}{RESET}", end="")
        if hostname:
            print(f"  ({CYAN}{hostname}{RESET})", end="")
        print(f"  State: {BOLD}{state_color}{state.upper()}{RESET}  "
              f"Open Ports: {BOLD}{GREEN}{len(ports)}{RESET}")
        if os_name:
            _info(f"OS Detection: {MAGENTA}{os_name}{RESET} (Accuracy: {os_acc}%)")

        if not ports:
            _warn("No open ports found.")
            continue

        print(f"\n    {BOLD}{GREY}{'PORT':<8} {'PROTO':<6} {'SERVICE':<15} {'PRODUCT':<20} {'VERSION'}{RESET}")
        print(f"    {GREY}{'─' * 80}{RESET}")

        for p in ports:
            pcolor = GREEN if p.get("state") == "open" else GREY
            extra = f" {p.get('extra_info', '')}" if p.get("extra_info") else ""
            tunnel = f" [{p.get('tunnel')}]" if p.get("tunnel") else ""
            print(
                f"    {BOLD}{pcolor}{str(p.get('port', '')):<8}{RESET}"
                f"{p.get('protocol', ''):<6}"
                f"{CYAN}{p.get('service', ''):<15}{RESET}"
                f"{MAGENTA}{p.get('product', ''):<20}{RESET}"
                f"{WHITE}{p.get('version', '')}{extra}{tunnel}{RESET}"
            )
            # Print NSE script results
            scripts = p.get("scripts", {})
            for script_id, script_out in scripts.items():
                if script_out.strip():
                    # Truncate long outputs to first 150 chars
                    preview = script_out.strip().replace("\n", " ")[:150]
                    print(f"            {GREY}[{script_id}]{RESET} {DIM}{preview}{RESET}")


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
    """Prints final colored CLI summary with counts and report locations."""
    nuclei_vulns = scan.get("nuclei", {}).get("vulnerabilities", [])
    testssl_findings = scan.get("testssl", {}).get("findings", [])
    testssl_warnings = scan.get("testssl", {}).get("summary", {}).get("warnings", [])
    critical_count = sum(
        1 for v in nuclei_vulns
        if v.get("severity", "").lower() in ("critical", "high")
    )
    tls_high = sum(
        1 for f in testssl_findings
        if f.get("severity", "").upper() in ("HIGH", "CRITICAL")
    )
    all_ports = sum(
        len(h.get("open_ports", []))
        for h in recon.get("nmap", {}).get("hosts", [])
    )

    print(f"\n{BOLD}{CYAN}{'═' * 70}{RESET}")
    print(f"{BOLD}{WHITE}  ASSESSMENT COMPLETE — {target}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * 70}{RESET}")
    print(f"  {GREY}{'Subdomains Discovered':<30}{RESET}: {GREEN}{BOLD}{len(recon.get('subfinder', {}).get('subdomains', []))}{RESET}")
    print(f"  {GREY}{'HTTP Services Probed':<30}{RESET}: {GREEN}{BOLD}{len(recon.get('httpx', {}).get('services', []))}{RESET}")
    print(f"  {GREY}{'Open Ports (Nmap)':<30}{RESET}: {GREEN}{BOLD}{all_ports}{RESET}")
    print(f"  {GREY}{'Technologies (WhatWeb)':<30}{RESET}: {GREEN}{BOLD}{sum(len(i.get('technologies', [])) for i in recon.get('whatweb', {}).get('tech_stack', []))}{RESET}")
    print(f"  {GREY}{'Crawled Endpoints (Katana)':<30}{RESET}: {GREEN}{BOLD}{len(recon.get('katana', {}).get('endpoints', []))}{RESET}")
    print(f"  {GREY}{'TLS/SSL Findings':<30}{RESET}: {(RED + BOLD) if testssl_warnings else (GREEN + BOLD)}{len(testssl_warnings)}{RESET}")
    print(f"  {GREY}{'TLS/SSL High/Critical':<30}{RESET}: {(RED + BOLD) if tls_high else (GREEN + BOLD)}{tls_high}{RESET}")
    print(f"  {GREY}{'Nuclei Vulnerabilities':<30}{RESET}: {(RED + BOLD) if nuclei_vulns else (GREEN + BOLD)}{len(nuclei_vulns)}{RESET}")

    if critical_count > 0 or tls_high > 0:
        total_crit = critical_count + tls_high
        print(f"\n  {BOLD}{RED}⚠  {total_crit} CRITICAL/HIGH findings require immediate attention!{RESET}")

    testssl_grade = scan.get("testssl", {}).get("summary", {}).get("grade", "")
    if testssl_grade:
        gcolor = GREEN if testssl_grade.startswith("A") else (YELLOW if testssl_grade.startswith("B") else RED)
        print(f"  {GREY}{'TLS Overall Grade':<30}{RESET}: {BOLD}{gcolor}{testssl_grade}{RESET}")

    print(f"\n  {BOLD}{'─' * 66}{RESET}")
    print(f"  {GREEN}[+]{RESET} JSON Report   : {CYAN}{report_paths.get('json', '')}{RESET}")
    print(f"  {GREEN}[+]{RESET} Markdown       : {CYAN}{report_paths.get('markdown', '')}{RESET}")
    print(f"  {GREEN}[+]{RESET} HTML Report    : {CYAN}{report_paths.get('html', '')}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * 70}{RESET}\n")
