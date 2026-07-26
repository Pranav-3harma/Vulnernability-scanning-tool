# Security Assessment Report: www.hackerone.com
**Generated Date:** 2026-07-25 05:04:56

---

## Executive Summary
- **Target:** `www.hackerone.com`
- **Subdomains Discovered:** 0
- **Live Web Endpoints (HTTPX):** 2
- **Crawled Endpoints (Katana):** 5905
- **Nuclei Findings Count:** 6
- **TLS/SSL Security Alerts:** 0

---

## 1. Discovered Ports & Services (Nmap)

### Host: `104.18.36.214` (State: up)
| Port | Protocol | State | Service | Product / Version |
|---|---|---|---|---|
| 80 | tcp | open | tcpwrapped |   |
| 443 | tcp | open | tcpwrapped |   |
| 8080 | tcp | open | tcpwrapped |   |
| 8443 | tcp | open | tcpwrapped |   |

---

## 2. Vulnerability Assessment Findings (Nuclei)
| Severity | Vulnerability Name | Matched Location | Template ID |
|---|---|---|---|
| **INFO** | WAF Detection | `https://www.hackerone.com` | `waf-detect` |
| **INFO** | TLS Version - Detect | `www.hackerone.com:443` | `tls-version` |
| **INFO** | TLS Version - Detect | `www.hackerone.com:443` | `tls-version` |
| **INFO** | Wappalyzer Technology Detection | `https://www.hackerone.com` | `tech-detect` |
| **INFO** | README.md file disclosure | `https://www.hackerone.com/README.md` | `readme-md` |
| **INFO** | HTTP Missing Security Headers | `https://www.hackerone.com` | `http-missing-security-headers` |

---

## 3. TLS/SSL Security Audit Details (testssl)
No TLS/SSL audit findings recorded.