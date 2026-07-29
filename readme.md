# TRINITY

## Automated Reconnaissance & Vulnerability Assessment Framework for Kali Linux

```{=html}
<p align="center">
```
A modular framework that automates reconnaissance, enumeration,
technology fingerprinting and vulnerability assessment by orchestrating
industry-standard open-source security tools.
```{=html}
</p>
```
> **Disclaimer**
>
> TRINITY is intended **only** for authorized security assessments,
> penetration testing engagements, lab environments, and bug bounty
> programs where testing is explicitly permitted.

------------------------------------------------------------------------

# Table of Contents

1.  Overview
2.  Features
3.  Architecture
4.  Reconnaissance Workflow
5.  Scan Profiles
6.  Integrated Tools
7.  Installation
8.  Usage
9.  Project Structure
10. Reports
11. Roadmap
12. License

------------------------------------------------------------------------

# Overview

TRINITY is a terminal-based automation framework developed for Kali
Linux. Instead of manually running multiple reconnaissance tools one by
one, TRINITY executes them in a structured workflow, parses their
results, presents readable output, and generates professional reports.

It is designed to reduce repetitive tasks while allowing users to choose
between complete automated scans and individual tool execution.

------------------------------------------------------------------------

# Core Features

-   Interactive CLI
-   Modular architecture
-   Multiple scan profiles
-   Automated reconnaissance workflow
-   AI-assisted result analysis
-   Colorized terminal dashboard
-   Structured HTML / JSON / Markdown reports
-   Logging
-   Expandable module system

------------------------------------------------------------------------

# Architecture

``` text
                    +----------------+
                    |     USER       |
                    +-------+--------+
                            |
                            v
                 +----------------------+
                 |    TRINITY CLI       |
                 +----------+-----------+
                            |
        +-------------------+-------------------+
        |                   |                   |
        v                   v                   v
 Recon Modules       Scan Engine         Report Engine
        |                   |                   |
        +---------+---------+-------------------+
                  |
                  v
          External Security Tools
                  |
  +---------------------------------------------+
  | Nmap | Naabu | HTTPX | WhatWeb | Katana     |
  | Subfinder | LinkFinder | SecretFinder       |
  | Nuclei | Other Modules                      |
  +---------------------------------------------+
                  |
                  v
        Parsed & Structured Results
                  |
                  v
      HTML • Markdown • JSON • Terminal
```

------------------------------------------------------------------------

# Reconnaissance Workflow

``` text
                    Target
                       |
                       v
              Target Validation
                       |
                       v
           Subdomain Enumeration
                       |
                       v
                HTTP Probing
                       |
                       v
               Port Discovery
                       |
                       v
             Service Enumeration
                       |
                       v
         Technology Fingerprinting
                       |
                       v
              Website Crawling
                       |
                       v
       JavaScript Endpoint Discovery
                       |
                       v
          Secret & API Key Detection
                       |
                       v
          Vulnerability Scanning
                       |
                       v
             AI Result Analysis
                       |
                       v
            Report Generation
```

------------------------------------------------------------------------

# Scan Profiles

## Fast

-   Host validation
-   Top ports
-   Basic service detection

## Standard

-   Fast profile
-   OS detection
-   Default NSE scripts

## Deep

-   Standard profile
-   Extended service detection
-   Traceroute
-   Additional NSE scripts

## Full

-   Complete TCP scan
-   Advanced fingerprinting
-   Comprehensive analysis
-   Full reporting

## Custom

Run only selected modules.

------------------------------------------------------------------------

# Integrated Tools

  Tool           Purpose
  -------------- ---------------------------------------
  Nmap           Service detection, OS detection, NSE
  Naabu          Fast TCP port discovery
  Subfinder      Subdomain enumeration
  HTTPX          HTTP probing
  WhatWeb        Technology fingerprinting
  Katana         Web crawling
  LinkFinder     JavaScript endpoint discovery
  SecretFinder   Secret detection
  Nuclei         Template-based vulnerability scanning

------------------------------------------------------------------------

# Internal Execution Flow

``` text
User
 |
 +--> Select Scan Mode
 |
 +--> Validate Target
 |
 +--> Launch Required Modules
 |      |
 |      +--> Recon
 |      +--> Enumeration
 |      +--> Port Scan
 |      +--> Fingerprinting
 |      +--> Crawling
 |      +--> Vulnerability Scan
 |
 +--> Parse Tool Output
 |
 +--> Correlate Findings
 |
 +--> AI Summary
 |
 +--> Export Reports
```

------------------------------------------------------------------------

# Installation

``` bash
git clone https://github.com/<your-username>/TRINITY.git
cd TRINITY
pip install -r requirements.txt
```

Install the required external tools before running TRINITY.

------------------------------------------------------------------------

# Usage

``` bash
python3 main.py
```

or

``` bash
TRINITY
```

------------------------------------------------------------------------

# Suggested Project Structure

``` text
TRINITY/
│
├── assets/
├── config/
├── logs/
├── modules/
│   ├── recon/
│   ├── scanners/
│   ├── crawlers/
│   ├── reporting/
│   └── utils/
├── output/
├── reports/
├── requirements.txt
├── README.md
└── main.py
```

------------------------------------------------------------------------

# Reporting

Generated reports may include:

-   Executive summary
-   Open ports
-   Service information
-   Technologies detected
-   JavaScript findings
-   Vulnerability findings
-   AI analysis
-   Recommendations

Formats:

-   HTML
-   Markdown
-   JSON
-   Terminal

------------------------------------------------------------------------

# Future Enhancements

-   Plugin marketplace
-   Docker support
-   Parallel execution
-   Burp Suite integration
-   CVSS scoring
-   Asset inventory
-   REST API
-   Automatic updates
-   Interactive dashboard

------------------------------------------------------------------------

# License

MIT License

------------------------------------------------------------------------

# Author

**Pranav Sharma**

Cybersecurity • Penetration Testing • Linux • Python

------------------------------------------------------------------------

# Acknowledgements

-   Kali Linux
-   ProjectDiscovery
-   Nmap
-   OWASP
-   WhatWeb
-   LinkFinder
-   SecretFinder
-   Open-source security community
