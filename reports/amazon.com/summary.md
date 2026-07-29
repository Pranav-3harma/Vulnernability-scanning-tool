# Security Assessment Report: amazon.com
**Generated Date:** 2026-07-29 15:31:03

---

## Executive Summary
- **Target:** `amazon.com`
- **Subdomains Discovered:** 0
- **Live Web Endpoints (HTTPX):** 2
- **Crawled Endpoints (Katana):** 3
- **Secrets Found in JS Files:** 0
- **Nuclei Findings Count:** 1
- **TLS/SSL Security Alerts:** 0

---

## 1. Discovered Ports & Services (Nmap)
- **Nmap Risk Level:** Informational (0/50)
- **Nmap Analysis Summary:** Nmap scanned 0 host(s) and found 0 open port(s). Next steps: validate these findings with authenticated application testing and TLS hardening checks.
- **Top Recommendations:** Continue with deeper application-layer and authenticated scanning.
No open ports reported or scan skipped.

---

## 2. Vulnerability Assessment Findings (Nuclei)
| Severity | Vulnerability Name | Matched Location | Template ID |
|---|---|---|---|
| **INFO** | Microsoft Azure Domain Tenant ID - Detect | `https://login.microsoftonline.com:443/amazon.com/v2.0/.well-known/openid-configuration` | `azure-domain-tenant` |

---

## 3. TLS/SSL Security Audit Details (testssl)
No TLS/SSL audit findings recorded.

---

## 4. JavaScript Secret Analysis (SecretFinder)

---

## 5. Port Discovery (Naabu)
No ports discovered by Naabu or scan skipped.

---

## 6. Hidden Endpoint Discovery (LinkFinder)
- Total endpoints discovered: 2
  - `text/javascript` (Other)  — source: https://amazon.com
  - `/1c5c1ecf7303/d6a7a58005ec/04c5ab18cd2d/challenge.js` (Other)  — source: https://amazon.com

### Scan Statistics

| Metric | Value |
|---|---|
| Status | `success` |
| Total JavaScript Files | 1 |
| Files Successfully Scanned | 1 |
| Files Failed / Timed Out | 0 |
| **Secrets Found** | **0** |
| Critical | 0 |
| High | 0 |
| Medium | 0 |
| Low | 0 |
| Informational | 0 |

✅ No secrets discovered in JavaScript files.