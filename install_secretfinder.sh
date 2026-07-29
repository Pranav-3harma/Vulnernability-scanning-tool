#!/usr/bin/env bash
# ==============================================================================
# install_secretfinder.sh
# Installer script for SecretFinder built-in tool module.
#
# Clones SecretFinder into tools/SecretFinder/ and sets up an isolated
# Python virtual environment in tools/SecretFinder/venv/.
# Complies with PEP 668 on Kali Linux by avoiding system Python package installs.
# ==============================================================================

set -e

# Color definitions
RED="\033[91m"
GREEN="\033[92m"
YELLOW="\033[93m"
CYAN="\033[96m"
BOLD="\033[1m"
RESET="\033[0m"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLS_DIR="$SCRIPT_DIR/tools"
SECRETFINDER_DIR="$TOOLS_DIR/SecretFinder"
VENV_DIR="$SECRETFINDER_DIR/venv"
REPO_URL="https://github.com/m4ll0k/SecretFinder.git"

echo -e "${BOLD}${CYAN}[+] Installing / Updating SecretFinder Module...${RESET}"

# Step 1: Ensure tools directory exists
mkdir -p "$TOOLS_DIR"

# Step 2: Clone or verify SecretFinder repository
if [ -d "$SECRETFINDER_DIR" ] && [ -f "$SECRETFINDER_DIR/SecretFinder.py" ]; then
    echo -e "${GREEN}[✓] SecretFinder repository detected at: ${SECRETFINDER_DIR}${RESET}"
else
    echo -e "${YELLOW}[!] SecretFinder repository not found. Cloning from ${REPO_URL}...${RESET}"
    if command -v git &> /dev/null; then
        git clone "$REPO_URL" "$SECRETFINDER_DIR"
        echo -e "${GREEN}[✓] SecretFinder repository cloned successfully.${RESET}"
    else
        echo -e "${RED}[✗] Error: 'git' is not installed or not in PATH.${RESET}"
        exit 1
    fi
fi

# Step 3: Check and create virtual environment if missing
if [ -d "$VENV_DIR" ] && [ -f "$VENV_DIR/bin/python" ]; then
    echo -e "${GREEN}[✓] SecretFinder virtual environment detected at: ${VENV_DIR}${RESET}"
else
    echo -e "${YELLOW}[!] Virtual environment missing. Creating venv at: ${VENV_DIR}...${RESET}"
    python3 -m venv "$VENV_DIR"
    echo -e "${GREEN}[✓] Virtual environment created successfully.${RESET}"
fi

# Step 4: Install/update dependencies inside the virtual environment
if [ -f "$SECRETFINDER_DIR/requirements.txt" ]; then
    echo -e "${CYAN}[*] Installing dependencies into virtual environment...${RESET}"
    "$VENV_DIR/bin/pip" install --upgrade pip setuptools wheel --quiet || true
    "$VENV_DIR/bin/pip" install -r "$SECRETFINDER_DIR/requirements.txt" --quiet
    echo -e "${GREEN}[✓] SecretFinder dependencies installed successfully.${RESET}"
else
    echo -e "${YELLOW}[!] Warning: requirements.txt not found in ${SECRETFINDER_DIR}${RESET}"
fi

echo -e "${BOLD}${GREEN}[✓] SecretFinder setup completed successfully!${RESET}"
echo -e "${CYAN}    Path: ${SECRETFINDER_DIR}/SecretFinder.py${RESET}"
echo -e "${CYAN}    Venv Python: ${VENV_DIR}/bin/python${RESET}"
exit 0
