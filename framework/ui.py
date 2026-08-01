import ipaddress
import re
from urllib.parse import urlparse

from framework.tool_registry import get_tool_menu_entries

# ANSI Color Codes
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"
WHITE = "\033[97m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
DIM = "\033[2m"

BANNER_LOGO = [ 

    
              "████████╗██████╗ ██╗███╗   ██╗██╗████████╗██╗   ██╗",
              "╚══██╔══╝██╔══██╗██║████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝",
              "   ██║   ██████╔╝██║██╔██╗ ██║██║   ██║    ╚████╔╝",
              "   ██║   ██╔══██╗██║██║╚██╗██║██║   ██║     ╚██╔╝",
              "   ██║   ██║  ██║██║██║ ╚████║██║   ██║      ██║",
              "   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝",
]


BOX_TITLE = "T R I N I T Y   v1.0"
BOX_SUBTITLE = "Advanced Automated Reconnaissance Framework"

LEFT_FEATURES = [
    "🌐 Subdomain Enumeration",
    "🕷️  Web Crawling",
    "📜 JavaScript Analysis",
    "📡 Technology Fingerprinting",
    "📄 Wayback URL Collection",
    "🚀 Parallel Multi-thread Scan",
]

RIGHT_FEATURES = [
    "⚡ Port Discovery (Naabu/Nmap)",
    "🔍 Directory & Endpoint Discovery",
    "🔑 Secret & API Key Detection",
    "🛡️ Vulnerability Detection (Nuclei)",
    "📊 Detailed HTML & JSON Reports",
    "🎯 Interactive Scan Profiles",
]

METADATA = [
    ("Framework", "Trinity"),
    ("Platform", "Kali Linux / Debian-based Linux"),
    ("Developer", "Pranav Sharma"),
    ("Purpose", "Authorized Security Reconnaissance Only"),
    ("License", "Educational & Ethical Use Only"),
]


def display_banner() -> None:
    """
    Prints the Trinity ASCII logo banner in bright colors to the console.
    """
    # Print big logo (TRINITY) in red
    print()
    for line in BANNER_LOGO:
        print(f"{BOLD}{RED}{line}{RESET}")
    print()

    # Build boxed info area while computing widths to avoid wrapping
    left_w = max(len(s) for s in LEFT_FEATURES)
    right_w = max(len(s) for s in RIGHT_FEATURES)
    middle_gap = 6
    inner_content = left_w + middle_gap + right_w
    inner_width = inner_content + 4  # account for padding inside box

    top = f"╔{'═' * inner_width}╗"
    mid_sep = f"╠{'═' * inner_width}╣"
    bot = f"╚{'═' * inner_width}╝"

    # Print top border
    print(f"{BOLD}{CYAN}{top}{RESET}")

    # Title centered (TRINITY title in red)
    print(f"{BOLD}{CYAN}║{RESET} {BOLD}{RED}{BOX_TITLE.center(inner_width - 2)}{RESET} {BOLD}{CYAN}║{RESET}")
    print(f"{BOLD}{CYAN}║{RESET} {BOLD}{WHITE}{BOX_SUBTITLE.center(inner_width - 2)}{RESET} {BOLD}{CYAN}║{RESET}")

    # Middle separator
    print(f"{BOLD}{CYAN}{mid_sep}{RESET}")

    # Feature rows (pair left/right)
    for l, r in zip(LEFT_FEATURES, RIGHT_FEATURES):
        left_part = l.ljust(left_w)
        right_part = r.ljust(right_w)
        print(
            f"{BOLD}{CYAN}║{RESET}  {GREEN}{left_part}{RESET}  {BOLD}{CYAN}│{RESET}  {YELLOW}{right_part}{RESET}  {BOLD}{CYAN}║{RESET}"
        )

    # Separator before metadata
    print(f"{BOLD}{CYAN}{mid_sep}{RESET}")

    # Metadata rows
    for key, val in METADATA:
        left = f"{key} : {val}"
        print(f"{BOLD}{CYAN}║{RESET} {WHITE}{left.ljust(inner_width - 2)}{RESET} {BOLD}{CYAN}║{RESET}")

    # Bottom border
    print(f"{BOLD}{CYAN}{bot}{RESET}")

def validate_target(target: str) -> tuple[bool, str]:
    """
    Validates whether input is a valid domain, IP address (v4/v6), or URL.
    
    Args:
        target: The target string entered by user.
        
    Returns:
        tuple[bool, str]: (is_valid, sanitized_target)
    """
    target = target.strip()
    if not target:
        return False, ""

    # Remove protocol prefix if included for IP/domain validation check
    clean_host = target
    if target.startswith("http://") or target.startswith("https://"):
        parsed = urlparse(target)
        clean_host = parsed.netloc.split(":")[0]  # Remove port if present

    # Check if target is a valid IP address
    try:
        ipaddress.ip_address(clean_host)
        return True, target
    except ValueError:
        pass

    # Check if target is a valid Domain name (RFC 1123 matching)
    domain_regex = re.compile(
        r"^(?:[a-zA-Z0-9]"
        r"(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
        r"[a-zA-Z]{2,}$"
    )

    if domain_regex.match(clean_host):
        return True, target

    return False, ""


def prompt_target() -> str:
    """
    Interactively prompts the user to enter a target until a valid domain/IP/URL is provided.
    
    Returns:
        str: Validated target string.
    """
    while True:
        try:
            user_input = input(f"{BOLD}{RED}[?]{RESET} Enter Target Domain, IP address, or URL: ")
            is_valid, sanitized_target = validate_target(user_input)
            if is_valid:
                print(f"{BOLD}{CYAN}[+]{RESET} Target set to: {sanitized_target}\n")
                return sanitized_target
            else:
                print(f"{BOLD}{RED}[-]{RESET} Invalid target format. Please enter a valid Domain name (e.g. example.com), IP, or URL.\n")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOLD}{RED}[-]{RESET} Scan cancelled by user.")
            exit(0)


def prompt_install_secretfinder() -> bool:
    """
    Prompts the user to automatically run install_secretfinder.sh if SecretFinder is missing.

    Returns:
        bool: True if installation was executed and succeeded, False otherwise.
    """
    import subprocess
    import sys
    from pathlib import Path

    project_root = Path(__file__).resolve().parent.parent
    installer = project_root / "install_secretfinder.sh"

    print(f"\n{BOLD}{YELLOW}[!]{RESET} SecretFinder module or Python virtual environment was not found.")

    if not sys.stdin.isatty():
        print(f"{BOLD}{YELLOW}[!]{RESET} Non-interactive terminal detected. "
              f"Please run '{installer.name}' manually to enable SecretFinder.\n")
        return False

    try:
        ans = input(f"{BOLD}{CYAN}[?]{RESET} Would you like to run installer '{installer.name}' now? [Y/n]: ").strip().lower()
        if ans in ("", "y", "yes"):
            print(f"{BOLD}{CYAN}[*]{RESET} Running SecretFinder installer...\n")
            res = subprocess.run(["bash", str(installer)], check=False)
            return res.returncode == 0
        else:
            print(f"{BOLD}{YELLOW}[!]{RESET} SecretFinder installation skipped. Secret analysis will be bypassed.\n")
            return False
    except (KeyboardInterrupt, EOFError):
        print(f"\n{BOLD}{YELLOW}[!]{RESET} SecretFinder installation skipped by user.\n")
        return False


def prompt_scan_mode() -> str:
    """Prompts the user to choose between a full scan and a custom single-tool scan."""
    print(f"\n{BOLD}{WHITE}Select Scan Mode:{RESET}")
    print(f"  {CYAN}[1]{RESET} Full Scan")
    print(f"  {CYAN}[2]{RESET} Custom Scan (Choose Specific Tool)\n")

    while True:
        try:
            choice = input(f"{BOLD}{CYAN}Enter your choice:{RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOLD}{RED}[-]{RESET} Scan cancelled by user.")
            raise SystemExit(0)

        if choice in {"1", "2"}:
            return "full" if choice == "1" else "custom"

        print(f"{BOLD}{YELLOW}[!]{RESET} Please enter 1 or 2.")


def prompt_custom_tool() -> str | None:
    """Prompts the user to select a single tool from the registry."""
    entries = get_tool_menu_entries()
    print(f"\n{BOLD}{WHITE}Available Tools:{RESET}")
    for idx, entry in enumerate(entries, start=1):
        status = "enabled" if entry["enabled"] else "disabled"
        print(f"  {CYAN}[{idx}]{RESET} {entry['name']:<12} {DIM}({status}){RESET} {entry['description']}")
    print(f"  {CYAN}[{len(entries) + 1}]{RESET} Exit\n")

    while True:
        try:
            choice = input(f"{BOLD}{CYAN}Enter your choice:{RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOLD}{RED}[-]{RESET} Scan cancelled by user.")
            raise SystemExit(0)

        if choice.isdigit():
            index = int(choice)
            if index == len(entries) + 1:
                return None
            if 1 <= index <= len(entries):
                selected = entries[index - 1]
                if selected["enabled"]:
                    return selected["key"]
                print(f"{BOLD}{YELLOW}[!]{RESET} That tool is currently disabled.")
                continue
        print(f"{BOLD}{YELLOW}[!]{RESET} Please enter a valid menu number.")


def prompt_follow_up_action() -> str:
    """Asks the user what to do after a custom scan completes."""
    print(f"\n{BOLD}{WHITE}Scan completed.{RESET}")
    print(f"  {CYAN}[1]{RESET} Run another tool on the same target")
    print(f"  {CYAN}[2]{RESET} Start a new target")
    print(f"  {CYAN}[3]{RESET} Exit\n")

    while True:
        try:
            choice = input(f"{BOLD}{CYAN}Enter your choice:{RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOLD}{RED}[-]{RESET} Scan cancelled by user.")
            raise SystemExit(0)

        if choice in {"1", "2", "3"}:
            return choice
        print(f"{BOLD}{YELLOW}[!]{RESET} Please enter 1, 2, or 3.")

