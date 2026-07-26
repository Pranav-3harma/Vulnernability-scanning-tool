import ipaddress
import re
from urllib.parse import urlparse

# ANSI Color Codes
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"
WHITE = "\033[97m"
CYAN = "\033[96m"

BANNER_TEXT = r"""
  ____  _______   _____ _     _       _____   ______   _____ 
 |  _ \| ____\ \ / /_ _| |   | |     |  ___|  \ \ / / | ____|
 | | | |  _|  \ V / | || |   | |     | |___    \ V /  |  _|  
 | |_| | |___  | |  | || |___| |___  |  ___|    | |   | |___ 
 |____/|_____| |_| |___|_____|_____| |_|        |_|   |_____|
"""


def display_banner() -> None:
    """
    Prints the DEVIL'S EYE ASCII logo banner in RED text to the console.
    """
    print(f"{BOLD}{RED}{BANNER_TEXT}{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 66}{RESET}")
    print(f"{BOLD}{WHITE}    DEVIL'S EYE — Vulnerability Assessment Framework v1.0.0{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 66}{RESET}")
    print()


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
