# Security Assessment Report: https://www.nasa.gov/
**Generated Date:** 2026-07-25 02:51:03

---

## Executive Summary
- **Target:** `https://www.nasa.gov/`
- **Subdomains Discovered:** 1
- **Live Web Endpoints (HTTPX):** 1
- **Crawled Endpoints (Katana):** 41899
- **Nuclei Findings Count:** 1
- **TLS/SSL Security Alerts:** 0

---

## 1. Discovered Ports & Services (Nmap)

### Host: `192.0.66.108` (State: up)
| Port | Protocol | State | Service | Product / Version |
|---|---|---|---|---|
| 80 | tcp | open | http | nginx  |
| 443 | tcp | open | http | nginx  |

---

## 2. Vulnerability Assessment Findings (Nuclei)
| Severity | Vulnerability Name | Matched Location | Template ID |
|---|---|---|---|
| **INFO** | WAF Detection | `https://www.nasa.gov/` | `waf-detect` |

---

## 3. TLS/SSL Security Audit Details (testssl)
No TLS/SSL audit findings recorded.