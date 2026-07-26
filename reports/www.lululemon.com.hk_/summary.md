# Security Assessment Report: https://www.lululemon.com.hk/
**Generated Date:** 2026-07-26 03:09:07

---

## Executive Summary
- **Target:** `https://www.lululemon.com.hk/`
- **Subdomains Discovered:** 0
- **Live Web Endpoints (HTTPX):** 1
- **Crawled Endpoints (Katana):** 1
- **Nuclei Findings Count:** 12
- **TLS/SSL Security Alerts:** 0

---

## 1. Discovered Ports & Services (Nmap)
No open ports reported or scan skipped.

---

## 2. Vulnerability Assessment Findings (Nuclei)
| Severity | Vulnerability Name | Matched Location | Template ID |
|---|---|---|---|
| **INFO** | WAF Detection | `https://www.lululemon.com.hk/` | `waf-detect` |
| **INFO** | TLS Version - Detect | `www.lululemon.com.hk:443` | `tls-version` |
| **INFO** | TLS Version - Detect | `www.lululemon.com.hk:443` | `tls-version` |
| **INFO** | Missing Cookie SameSite Strict | `https://www.lululemon.com.hk/` | `missing-cookie-samesite-strict` |
| **INFO** | Wappalyzer Technology Detection | `https://www.lululemon.com.hk/` | `tech-detect` |
| **INFO** | Weak Content Security Policy - Detect | `https://www.lululemon.com.hk/` | `weak-csp-detect` |
| **INFO** | HTTP Missing Security Headers | `https://www.lululemon.com.hk/` | `http-missing-security-headers` |
| **INFO** | HTTP Missing Security Headers | `https://www.lululemon.com.hk/` | `http-missing-security-headers` |
| **INFO** | DNS SaaS Service Detection | `www.lululemon.com.hk` | `dns-saas-service-detection` |
| **INFO** | AAAA Record - IPv6 Detection | `www.lululemon.com.hk` | `aaaa-fingerprint` |
| **INFO** | Detect SSL Certificate Issuer | `www.lululemon.com.hk:443` | `ssl-issuer` |
| **INFO** | SSL DNS Names | `www.lululemon.com.hk:443` | `ssl-dns-names` |

---

## 3. TLS/SSL Security Audit Details (testssl)
No TLS/SSL audit findings recorded.