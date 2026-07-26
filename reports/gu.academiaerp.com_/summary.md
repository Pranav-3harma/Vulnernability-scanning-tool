# Security Assessment Report: https://gu.academiaerp.com/
**Generated Date:** 2026-07-25 02:24:00

---

## Executive Summary
- **Target:** `https://gu.academiaerp.com/`
- **Subdomains Discovered:** 0
- **Live Web Endpoints (HTTPX):** 1
- **Crawled Endpoints (Katana):** 443
- **Nuclei Findings Count:** 11
- **TLS/SSL Security Alerts:** 0

---

## 1. Discovered Ports & Services (Nmap)

### Host: `104.26.14.209` (State: up)
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
| **INFO** | WAF Detection | `https://gu.academiaerp.com/` | `waf-detect` |
| **INFO** | TLS Version - Detect | `gu.academiaerp.com:443` | `tls-version` |
| **INFO** | Missing Subresource Integrity | `https://gu.academiaerp.com/` | `missing-sri` |
| **INFO** | HTTP Missing Security Headers | `https://gu.academiaerp.com/` | `http-missing-security-headers` |
| **INFO** | HTTP Missing Security Headers | `https://gu.academiaerp.com/` | `http-missing-security-headers` |
| **INFO** | HTTP Missing Security Headers | `https://gu.academiaerp.com/` | `http-missing-security-headers` |
| **INFO** | HTTP Missing Security Headers | `https://gu.academiaerp.com/` | `http-missing-security-headers` |
| **INFO** | HTTP Missing Security Headers | `https://gu.academiaerp.com/` | `http-missing-security-headers` |
| **INFO** | HTTP Missing Security Headers | `https://gu.academiaerp.com/` | `http-missing-security-headers` |
| **INFO** | Weak HTTP Strict-Transport-Security - Detect | `https://gu.academiaerp.com/` | `weak-hsts-detect` |
| **INFO** | Wappalyzer Technology Detection | `https://gu.academiaerp.com/` | `tech-detect` |