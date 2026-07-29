# Security Assessment Report: https://www.nvidia.com/en-in/
**Generated Date:** 2026-07-28 12:15:14

---

## Executive Summary
- **Target:** `https://www.nvidia.com/en-in/`
- **Subdomains Discovered:** 0
- **Live Web Endpoints (HTTPX):** 1
- **Crawled Endpoints (Katana):** 16016
- **Secrets Found in JS Files:** 1127
- **Nuclei Findings Count:** 2
- **TLS/SSL Security Alerts:** 0

---

## 1. Discovered Ports & Services (Nmap)

### Host: `117.239.141.98` (State: up)
| Port | Protocol | State | Service | Product / Version |
|---|---|---|---|---|
| 80 | tcp | open | http | AkamaiGHost  |
| 443 | tcp | open | http | AkamaiGHost  |

---

## 2. Vulnerability Assessment Findings (Nuclei)
| Severity | Vulnerability Name | Matched Location | Template ID |
|---|---|---|---|
| **INFO** | Cookies without HttpOnly attribute - Detect | `www.nvidia.com` | `cookies-without-httponly` |
| **INFO** | WAF Detection | `https://www.nvidia.com/en-in/` | `waf-detect` |

---

## 3. TLS/SSL Security Audit Details (testssl)
No TLS/SSL audit findings recorded.

---

## 4. JavaScript Secret Analysis (SecretFinder)

### Scan Statistics

| Metric | Value |
|---|---|
| Status | `success` |
| Total JavaScript Files | 582 |
| Files Successfully Scanned | 580 |
| Files Failed / Timed Out | 2 |
| **Secrets Found** | **1127** |
| Critical | 122 |
| High | 910 |
| Medium | 72 |
| Low | 20 |
| Informational | 3 |

### Findings

| Severity | Secret Type | Source JavaScript URL | Matched Value (truncated) | Confidence |
|---|---|---|---|---|
| **HIGH** | Hardcoded Credentials | `https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js` | `password:!0,image:!0})b.pseudos[e]=de(e);for(e` | medium |
| **LOW** | Google Captcha Key | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `6lC6Zog7JqSqZmYlosl2K6pwNA84zRnQW6SaALYZ` | medium |
| **LOW** | Google Captcha Key | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `6lWMnyaYirx1rFUQZFBkb2zJUtoXeJCeg0WnLtHe` | medium |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `ACYAAAC3AAABHQZg6OcWhlYWQAAA3QAAAA` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `ACM744AAGxvY2EAAA4wAAAASAAAAEhF6kq` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `ACY7BUgAeJxjYGS7wTiBgZWBgaWQ5RkDA8` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `acqZmQzRq0ypDXS2TPLT02YIkQETnOE445` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `AcICGAJYArQC4AMwA7AD3gQwBJYE3AUkBW` | high |
| **MEDIUM** | Twilio App SID | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `APgAAAFZRiV3hY21hcAAAAYQAAADaAAADP` | medium |
| **MEDIUM** | Twilio App SID | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `apfbORfKsDTuZ0OBgx4cfdjCf5tbWNITnL` | medium |
| **CRITICAL** | Square Access Token | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `EAAA4wAAAASAAAAEhF6kqubWF4cAAADngAAAAfAAAAIAE0AIFu…` | high |
| **HIGH** | Hardcoded Credentials | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://api-prod.nvidia.com/search/nvidia-gallery-widget.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **LOW** | Google Captcha Key | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `6lC6Zog7JqSqZmYlosl2K6pwNA84zRnQW6SaALYZ` | medium |
| **LOW** | Google Captcha Key | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `6lWMnyaYirx1rFUQZFBkb2zJUtoXeJCeg0WnLtHe` | medium |
| **HIGH** | Basic Auth Credentials | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `Basic=function` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `ACYAAAC3AAABHQZg6OcWhlYWQAAA3QAAAA` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `ACM744AAGxvY2EAAA4wAAAASAAAAEhF6kq` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `ACY7BUgAeJxjYGS7wTiBgZWBgaWQ5RkDA8` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `acqZmQzRq0ypDXS2TPLT02YIkQETnOE445` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `AcICGAJYArQC4AMwA7AD3gQwBJYE3AUkBW` | high |
| **MEDIUM** | Twilio App SID | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `APgAAAFZRiV3hY21hcAAAAYQAAADaAAADP` | medium |
| **MEDIUM** | Twilio App SID | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `apfbORfKsDTuZ0OBgx4cfdjCf5tbWNITnL` | medium |
| **MEDIUM** | Twilio App SID | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `April_May_June_July_August_Septemb` | medium |
| **CRITICAL** | Square Access Token | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `EAAA4wAAAASAAAAEhF6kqubWF4cAAADngAAAAfAAAAIAE0AIFu…` | high |
| **CRITICAL** | Heroku API Key | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `edef8ba9-79d6-4ace-a3c8-27dcd51d21ed` | high |
| **CRITICAL** | Heroku API Key | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `1077efec-c0b2-4d02-ace3-3c1e52e2fb4b` | high |
| **CRITICAL** | Heroku API Key | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `9a04f079-9840-4286-ab92-e65be0885f95` | high |
| **CRITICAL** | Heroku API Key | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `f239e769-efa3-4850-9c16-a903c6932efb` | high |
| **HIGH** | Hardcoded Credentials | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://api-prod.nvidia.com/search/nvidia-search-library.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **LOW** | Google Captcha Key | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `6lC6Zog7JqSqZmYlosl2K6pwNA84zRnQW6SaALYZ` | medium |
| **LOW** | Google Captcha Key | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `6lWMnyaYirx1rFUQZFBkb2zJUtoXeJCeg0WnLtHe` | medium |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `ACYAAAC3AAABHQZg6OcWhlYWQAAA3QAAAA` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `ACM744AAGxvY2EAAA4wAAAASAAAAEhF6kq` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `ACY7BUgAeJxjYGS7wTiBgZWBgaWQ5RkDA8` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `acqZmQzRq0ypDXS2TPLT02YIkQETnOE445` | high |
| **HIGH** | Twilio Account SID | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `AcICGAJYArQC4AMwA7AD3gQwBJYE3AUkBW` | high |
| **MEDIUM** | Twilio App SID | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `APgAAAFZRiV3hY21hcAAAAYQAAADaAAADP` | medium |
| **MEDIUM** | Twilio App SID | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `apfbORfKsDTuZ0OBgx4cfdjCf5tbWNITnL` | medium |
| **MEDIUM** | Twilio App SID | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `April_May_June_July_August_Septemb` | medium |
| **CRITICAL** | Square Access Token | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `EAAA4wAAAASAAAAEhF6kqubWF4cAAADngAAAAfAAAAIAE0AIFu…` | high |
| **HIGH** | Hardcoded Credentials | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://api-prod.nvidia.com/search/nvidia-search-page-widget.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://app-sj14.marketo.com/js/forms2/js/forms2.min.js` | `password:!0,image:!0})A.pseudos[z]=h(z);for(z` | medium |
| **HIGH** | Hardcoded Credentials | `https://app-sj14.marketo.com/js/forms2/js/forms2.min.js?ver=5.6.2` | `password:!0,image:!0})A.pseudos[z]=h(z);for(z` | medium |
| **LOW** | Google Captcha Key | `https://app.nvidia.com/search/nvidia-search-library.js` | `6lC6Zog7JqSqZmYlosl2K6pwNA84zRnQW6SaALYZ` | medium |
| **LOW** | Google Captcha Key | `https://app.nvidia.com/search/nvidia-search-library.js` | `6lWMnyaYirx1rFUQZFBkb2zJUtoXeJCeg0WnLtHe` | medium |
| **HIGH** | Basic Auth Credentials | `https://app.nvidia.com/search/nvidia-search-library.js` | `Basic=function` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-library.js` | `ACYAAAC3AAABHQZg6OcWhlYWQAAA3QAAAA` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-library.js` | `ACM744AAGxvY2EAAA4wAAAASAAAAEhF6kq` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-library.js` | `ACY7BUgAeJxjYGS7wTiBgZWBgaWQ5RkDA8` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-library.js` | `acqZmQzRq0ypDXS2TPLT02YIkQETnOE445` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-library.js` | `AcICGAJYArQC4AMwA7AD3gQwBJYE3AUkBW` | high |
| **MEDIUM** | Twilio App SID | `https://app.nvidia.com/search/nvidia-search-library.js` | `APgAAAFZRiV3hY21hcAAAAYQAAADaAAADP` | medium |
| **MEDIUM** | Twilio App SID | `https://app.nvidia.com/search/nvidia-search-library.js` | `apfbORfKsDTuZ0OBgx4cfdjCf5tbWNITnL` | medium |
| **MEDIUM** | Twilio App SID | `https://app.nvidia.com/search/nvidia-search-library.js` | `April_May_June_July_August_Septemb` | medium |
| **CRITICAL** | Square Access Token | `https://app.nvidia.com/search/nvidia-search-library.js` | `EAAA4wAAAASAAAAEhF6kqubWF4cAAADngAAAAfAAAAIAE0AIFu…` | high |
| **CRITICAL** | Heroku API Key | `https://app.nvidia.com/search/nvidia-search-library.js` | `edef8ba9-79d6-4ace-a3c8-27dcd51d21ed` | high |
| **CRITICAL** | Heroku API Key | `https://app.nvidia.com/search/nvidia-search-library.js` | `1077efec-c0b2-4d02-ace3-3c1e52e2fb4b` | high |
| **CRITICAL** | Heroku API Key | `https://app.nvidia.com/search/nvidia-search-library.js` | `9a04f079-9840-4286-ab92-e65be0885f95` | high |
| **CRITICAL** | Heroku API Key | `https://app.nvidia.com/search/nvidia-search-library.js` | `f239e769-efa3-4850-9c16-a903c6932efb` | high |
| **HIGH** | Hardcoded Credentials | `https://app.nvidia.com/search/nvidia-search-library.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://app.nvidia.com/search/nvidia-search-library.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **LOW** | Google Captcha Key | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `6lC6Zog7JqSqZmYlosl2K6pwNA84zRnQW6SaALYZ` | medium |
| **LOW** | Google Captcha Key | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `6lWMnyaYirx1rFUQZFBkb2zJUtoXeJCeg0WnLtHe` | medium |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `ACYAAAC3AAABHQZg6OcWhlYWQAAA3QAAAA` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `ACM744AAGxvY2EAAA4wAAAASAAAAEhF6kq` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `ACY7BUgAeJxjYGS7wTiBgZWBgaWQ5RkDA8` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `acqZmQzRq0ypDXS2TPLT02YIkQETnOE445` | high |
| **HIGH** | Twilio Account SID | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `AcICGAJYArQC4AMwA7AD3gQwBJYE3AUkBW` | high |
| **MEDIUM** | Twilio App SID | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `APgAAAFZRiV3hY21hcAAAAYQAAADaAAADP` | medium |
| **MEDIUM** | Twilio App SID | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `apfbORfKsDTuZ0OBgx4cfdjCf5tbWNITnL` | medium |
| **MEDIUM** | Twilio App SID | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `April_May_June_July_August_Septemb` | medium |
| **CRITICAL** | Square Access Token | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `EAAA4wAAAASAAAAEhF6kqubWF4cAAADngAAAAfAAAAIAE0AIFu…` | high |
| **HIGH** | Hardcoded Credentials | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://app.nvidia.com/search/nvidia-search-page-widget.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | API Token / Key | `https://assets.adobedtm.com/5d4962a43b79/76a76b0bb8ea/launch-7d434965ec64.min.js` | `API requests` | medium |
| **HIGH** | API Token / Key | `https://assets.adobedtm.com/5d4962a43b79/76a76b0bb8ea/launch-7d434965ec64.min.js` | `API processing` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.adobedtm.com/5d4962a43b79/76a76b0bb8ea/launch-7d434965ec64.min.js` | `AppMeasurement_Module_AudienceMana` | medium |
| **CRITICAL** | Heroku API Key | `https://assets.adobedtm.com/5d4962a43b79/76a76b0bb8ea/launch-7d434965ec64.min.js` | `29cd6713-5c26-bc5c-8484-7bf8a902b8f9` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.adobedtm.com/5d4962a43b79/76a76b0bb8ea/launch-7d434965ec64.min.js` | `password","host","port","relative","path","directo…` | medium |
| **HIGH** | API Token / Key | `https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js` | `API requests` | medium |
| **HIGH** | API Token / Key | `https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js` | `API processing` | medium |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js` | `accelerating-retail-operations-ai-` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js` | `ac0272ff4f1faa698d8bdec18650-sourc` | high |
| **MEDIUM** | Twilio App SID | `https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js` | `AppMeasurement_Module_AudienceMana` | medium |
| **CRITICAL** | Heroku API Key | `https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js` | `29cd6713-5c26-bc5c-8484-7bf8a902b8f9` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.adobedtm.com/5d4962a43b79/814eb6e9b4e1/launch-4bc07f1e0b0b.min.js` | `password","host","port","relative","path","directo…` | medium |
| **HIGH** | API Token / Key | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `API requests` | medium |
| **HIGH** | API Token / Key | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `API processing` | medium |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `achines-embedded-systems-jetson-or` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `accelerate-ai-training-and-inferen` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `ac8693020412bbfe54294f3ddb28b-sour` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `ac6b3a969f49eca4e9a7fcaf25cfd9-sou` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `ac23e5cdb41848608e58e9eaa6c5b4c7-s` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `accelerated-drug-discovery-webinar` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `accelerating-covid-19-research-web` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `ac27fee7ed1d42e3862f2355546d79c5-s` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `acca5b648d1a39294e7bfd51425-source` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `acing-trailer-screenshots-announce` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `achine-learning-artificial-intelli` | high |
| **MEDIUM** | Twilio App SID | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `AppMeasurement_Module_AudienceMana` | medium |
| **CRITICAL** | Heroku API Key | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `cb4959c9-de84-4957-bbce-7381ebf32126` | high |
| **CRITICAL** | Heroku API Key | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `98a7ac3d-0736-43b0-9dbb-e8126fb10a5a` | high |
| **CRITICAL** | Heroku API Key | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `29cd6713-5c26-bc5c-8484-7bf8a902b8f9` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.adobedtm.com/5d4962a43b79/96fada676f0e/launch-95431b44ee81.min.js` | `password","host","port","relative","path","directo…` | medium |
| **HIGH** | API Token / Key | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `API requests` | medium |
| **HIGH** | API Token / Key | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `API processing` | medium |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `ac9d48489ebaecd48c3cfec9-libraryCo` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `accelerate-video-analytics-deepstr` | high |
| **HIGH** | Twilio Account SID | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `actical-technique-to-customize-llm` | high |
| **MEDIUM** | Twilio App SID | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `AppMeasurement_Module_AudienceMana` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `applications-with-new-beta-release` | medium |
| **CRITICAL** | Heroku API Key | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `29cd6713-5c26-bc5c-8484-7bf8a902b8f9` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.adobedtm.com/5d4962a43b79/c1061d2c5e7b/launch-191c2462b890.min.js` | `password","host","port","relative","path","directo…` | medium |
| **HIGH** | API Token / Key | `https://blogs.nvidia.com/%5C/www.nvidia.com%5C/content%5C/dam%5C/en-zz%5C/Solutions%5C/librarian%5C/bundle-search-prod-pub-v3.1.js` | `APIEndpoint` | medium |
| **CRITICAL** | Heroku API Key | `https://blogs.nvidia.com/%5C/www.nvidia.com%5C/content%5C/dam%5C/en-zz%5C/Solutions%5C/librarian%5C/bundle-search-prod-pub-v3.1.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | Basic Auth Credentials | `https://blogs.nvidia.com/wp-content/plugins/revslider/public/js/sr7.js` | `Basic:function` | high |
| **HIGH** | Basic Auth Credentials | `https://blogs.nvidia.com/wp-content/plugins/revslider/public/js/sr7.js` | `BasicMetas=` | high |
| **HIGH** | Basic Auth Credentials | `https://blogs.nvidia.com/wp-content/plugins/revslider/public/js/sr7.js` | `BasicMetas` | high |
| **HIGH** | Basic Auth Credentials | `https://blogs.nvidia.com/wp-content/plugins/revslider/public/js/sr7.js?ver=6.7.57` | `Basic:function` | high |
| **HIGH** | Basic Auth Credentials | `https://blogs.nvidia.com/wp-content/plugins/revslider/public/js/sr7.js?ver=6.7.57` | `BasicMetas=` | high |
| **HIGH** | Basic Auth Credentials | `https://blogs.nvidia.com/wp-content/plugins/revslider/public/js/sr7.js?ver=6.7.57` | `BasicMetas` | high |
| **HIGH** | Hardcoded Credentials | `https://blogs.nvidia.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1` | `password:!0,image:!0})b.pseudos[e]=B(e);for(e` | medium |
| **HIGH** | Hardcoded Credentials | `https://catalog.ngc.nvidia.com/assets/client-BQGawC2F.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://catalog.ngc.nvidia.com/assets/client-BQGawC2F.js` | `password`)\|\|t===`textarea`\|\|e.contentEditable===`t…` | medium |
| **CRITICAL** | Heroku API Key | `https://catalog.ngc.nvidia.com/assets/esm-dzPUXh8L.js` | `10000000-1000-4000-8000-100000000000` | high |
| **HIGH** | Hardcoded Credentials | `https://catalog.ngc.nvidia.com/assets/esm-dzPUXh8L.js` | `password`:return!1}if(t&&!t.some(function(e){retur…` | medium |
| **HIGH** | Hardcoded Credentials | `https://catalog.ngc.nvidia.com/assets/esm-dzPUXh8L.js` | `password`,`hidden`];function` | medium |
| **HIGH** | API Token / Key | `https://catalog.ngc.nvidia.com/assets/esm-nMUgGhZg.js` | `api\|secret` | medium |
| **HIGH** | Twilio Account SID | `https://catalog.ngc.nvidia.com/assets/esm-nMUgGhZg.js` | `ACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw` | high |
| **HIGH** | Twilio Account SID | `https://catalog.ngc.nvidia.com/assets/esm-nMUgGhZg.js` | `action_to_next_paint_target_select` | high |
| **CRITICAL** | Heroku API Key | `https://catalog.ngc.nvidia.com/assets/esm-nMUgGhZg.js` | `10000000-1000-4000-8000-100000000000` | high |
| **CRITICAL** | Heroku API Key | `https://catalog.ngc.nvidia.com/assets/esm-nMUgGhZg.js` | `00000000-aaaa-0000-aaaa-000000000000` | high |
| **HIGH** | Hardcoded Credentials | `https://catalog.ngc.nvidia.com/assets/esm-nMUgGhZg.js` | `password`&&t===`value`}function` | medium |
| **HIGH** | Hardcoded Credentials | `https://catalog.ngc.nvidia.com/assets/esm-nMUgGhZg.js` | `password`\|\|t.type===`email`\|\|t.type===`tel`\|\|t.typ…` | medium |
| **HIGH** | Hardcoded Credentials | `https://catalog.ngc.nvidia.com/assets/esm-nMUgGhZg.js` | `password`)))return` | medium |
| **HIGH** | API Token / Key | `https://catalog.ngc.nvidia.com/assets/root-OeWpZy7f.js` | `API calls` | medium |
| **HIGH** | API Token / Key | `https://catalog.ngc.nvidia.com/at.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://catalog.ngc.nvidia.com/at.js` | `API reference` | medium |
| **HIGH** | API Token / Key | `https://catalog.ngc.nvidia.com/at.js` | `API access` | medium |
| **CRITICAL** | Heroku API Key | `https://catalog.ngc.nvidia.com/at.js` | `4c857e4f-5ffa-45fa-b75e-af773c22f0ad` | high |
| **CRITICAL** | Heroku API Key | `https://catalog.ngc.nvidia.com/at.js` | `6f1bcf42-55d0-45d1-b4b6-f08c68a50bbe` | high |
| **CRITICAL** | Heroku API Key | `https://catalog.ngc.nvidia.com/at.js` | `e91ca707-db64-49d6-9761-4781590a9685` | high |
| **CRITICAL** | Heroku API Key | `https://catalog.ngc.nvidia.com/at.js` | `7ba64fc5-7c44-4864-a5e6-7bde05126935` | high |
| **LOW** | Google Captcha Key | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `6LSzdwUdC0iPB609Hg9398NuGIVnduL3bUcHBEdP` | medium |
| **LOW** | Google Captcha Key | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `6l35GZCI6RN13lG6gG3YjmwGXw6xHrGx71uxHK6Z` | medium |
| **HIGH** | Basic Auth Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `BasicStyling:Gn` | high |
| **HIGH** | Basic Auth Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `BasicStyling` | high |
| **HIGH** | Twilio Account SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `ACWCAYAAAA8AXHiAAAACXBIWXMAAAsTAAA` | high |
| **HIGH** | Twilio Account SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `aC2fXODbwPZ9PN7OGzvjYd4js4aADiNpuJ` | high |
| **HIGH** | Twilio Account SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `ACpg9vuoiLg6MqTIXpcV6tUaNEMYUVbKu2` | high |
| **HIGH** | Twilio Account SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `acqFh225xsoMUdN3hOeTnE4sLYhxD45XmX` | high |
| **HIGH** | Twilio Account SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `acRaOLnLJz07cew7rZ7kyeBZdVALBfmXx2` | high |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `April_May_June_July_August_Septemb` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `aPj89y9lahwxesKKC0T4XiVSwOTNJLyiDL` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `APVdQw2v6jnApOyGYTOAI98AiIdbPxx4LF` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `ApCsGMJp2OGBuDBiIVA29DvejwekgrBQkC` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `ApLYCIxHwnxVyjPgga8GXg8oEDuS3dM8xN` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `APyb621FjOTb3DbpCehs2whhLbPaDx2pSa` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `APK0DjO8AK1vJxSagU4150eKwFpRvLlYA2` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `APsZno2LypXKA27MVHVliKLshKwRPxbuKS` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `appzMPK4CzZXADmwJi6Z8BdrsYpAGNcx3g` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `ApwsSnv9tjBLEVFNfXshqjrNxpK0V9Bfsd` | medium |
| **MEDIUM** | Twilio App SID | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `Ap8LcJrVc1nK1GjVmnwCSNXynuz8Y9M295` | medium |
| **CRITICAL** | Heroku API Key | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `00000000-0000-0000-0000-000000000000` | high |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password=""),t.stripHash&&(o.hash=""),o.pathname&&…` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password="",s.host=null,s.port=null,s.path=[],s.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password=n.password,s.host=n.host,s.port=n.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password=n.password,s.host=n.host,s.port=n.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password=n.password,s.host=n.host,s.port=n.port,u=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `Password:function(){return` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `Password:function(e){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password=o.getPassword(),t.host=o.getHost(),t.host…` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password",Be("getPassword","setPassword")),p(Ne,"h…` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://cdn-app.pathfactory.com/production/jukebox/current/jukebox.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | API Token / Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `APIException` | medium |
| **HIGH** | API Token / Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `API_ERROR` | medium |
| **HIGH** | API Token / Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `API_RESPONSE_MISMATCH` | medium |
| **HIGH** | API Token / Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `API_UNAVAILABLE` | medium |
| **HIGH** | API Token / Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `API support` | medium |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `AccessControlModifyRequestHostRege` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `ACAGlzb21pc28ybXA0MQAAAAhmcmVlAAAC` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `AcAAAAsJtb292AAAAbG12aGQAAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `ACRlZHRzAAAAHGVsc3QAAAAAAAAAAQAAAC` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `Ac291bgAAAAAAAAAAAAAAAFNvdW5kSGFuZ` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `ACEhAGgICAAQIAAAAYc3R0cwAAAAAAAAAB` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `Acc3RzYwAAAAAAAAABAAAAAQAAAAIAAAAB` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `ACWpdG9vAAAAHWRhdGEAAAABAAAAAExhdm` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `ACY_APPLE_MEDIA_KEYS_NOT_SUPPORTED` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `ACyAgCdASoCAAIALmk0mk0iIiIiIgBoSyg` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `AcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAA` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `ACAAAAEHBpeGkAAAAAAwgICAAAAAxhdjFD` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `ACAAIAAYAAAAAXaXBtYQAAAAAAAAABAAEE` | high |
| **HIGH** | Twilio Account SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `aCapabilitiesEncryptionSchemePolyf` | high |
| **MEDIUM** | Twilio App SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `aptionsOrSubtitlesFromCharacterist` | medium |
| **MEDIUM** | Twilio App SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `APoAAAALwABAAABAAAAAAAAAAAAAAAAAQA` | medium |
| **MEDIUM** | Twilio App SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `apabilitiesEncryptionSchemePolyfil` | medium |
| **MEDIUM** | Twilio App SID | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `appendNewFailedLiveEventToLocalSto` | medium |
| **CRITICAL** | Square Access Token | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `EAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `EAAAAAAQAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAEAA…` | high |
| **CRITICAL** | Square Access Token | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `EAAAAAAWRtZGlhAAAAIG1kaGQAAAAAAAAAAAAAAAAAAKxEAAAI…` | high |
| **CRITICAL** | Square Access Token | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `EAAAAMdXJsIAAAAAEAAADTc3RibAAAAGdzdHNkAAAAAAAAAAEA…` | high |
| **CRITICAL** | Square Access Token | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `EAAAAsAAAAYnVkdGEAAABabWV0YQAAAAAAAAAhaGRscgAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `EAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAAAB0AAAAoaWlu…` | high |
| **CRITICAL** | Heroku API Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `edef8ba9-79d6-4ace-a3c8-27dcd51d21ed` | high |
| **CRITICAL** | Heroku API Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `1077efec-c0b2-4d02-ace3-3c1e52e2fb4b` | high |
| **CRITICAL** | Heroku API Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `e2719d58-a985-b3c9-781a-b030af78d30e` | high |
| **CRITICAL** | Heroku API Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `9a04f079-9840-4286-ab92-e65be0885f95` | high |
| **CRITICAL** | Heroku API Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `79f0049a-4098-8642-ab92-e65be0885f95` | high |
| **CRITICAL** | Heroku API Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `94ce86fb-07ff-4f43-adb8-93d2fa968ca2` | high |
| **CRITICAL** | Heroku API Key | `https://cdnapisec.kaltura.com/p/2935771/embedPlaykitJs/uiconf_id/47494613.js` | `3d5e6d35-9b9a-41e8-b843-dd3c6e72c42c` | high |
| **HIGH** | Hardcoded Credentials | `https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.3/jquery.min.js` | `password:!0,image:!0})b.pseudos[e]=de(e);for(e` | medium |
| **HIGH** | Hardcoded Credentials | `https://code.jquery.com/jquery-2.2.4.min.js` | `password:!0,image:!0})d.pseudos[b]=la(b);for(b` | medium |
| **HIGH** | Hardcoded Credentials | `https://code.jquery.com/jquery-3.2.1.min.js` | `password:!0,image:!0})d.pseudos[b]=ma(b);for(b` | medium |
| **CRITICAL** | Heroku API Key | `https://code.jquery.com/jquery-latest.min.js` | `D27CDB6E-AE6D-11cf-96B8-444553540000` | high |
| **HIGH** | Hardcoded Credentials | `https://code.jquery.com/jquery-latest.min.js` | `password:!0,image:!0})d.pseudos[b]=lb(b);for(b` | medium |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac8bcbddcdadaeb636363969696bdbdbdd` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac8226ad8127ad8128ae8029af7f2ab07f` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac16d4cc26c4ec36b50c46a52c56954c56` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac8645cc8635ec96260ca6063cb5f65cb5` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac76feae77feb078feb27afeb47bfeb67c` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `acfcecaefceeb0fcf0b2fcf2b4fcf4b6fc` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `acb4149cc4248ce4347cf4446d04545d24` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac11fcae12fcb014fcb216fcb418fbb61a` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac026fac228fac42afac62df9c72ff9c93` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac2694ad2793ae2892b02991b12a90b22b` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `aca457acb4679cc4778cc4977cd4a76ce4` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v4.min.js` | `ac33fdae32fdaf31fdb130fdb22ffdb42f` | high |
| **HIGH** | Hardcoded Credentials | `https://d3js.org/d3.v4.min.js` | `password:function(t){return` | medium |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `accbd5e8f4cae4e6f5c9fff2aef1e2cccc` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `acb2abd2d8daebfee0b6fdb863e08214b3` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `acb2abd2d8daebf7f7f7fee0b6fdb863e0` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac994c7df65b0e7298ace1256980043670` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac8226ad8127ad8128ae8029af7f2ab07f` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac16d4cc26c4ec36b50c46a52c56954c56` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac8645cc8635ec96260ca6063cb5f65cb5` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac76feae77feb078feb27afeb47bfeb67c` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `acfcecaefceeb0fcf0b2fcf2b4fcf4b6fc` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `acb4149cc4248ce4347cf4446d04545d24` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac11fcae12fcb014fcb216fcb418fbb61a` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac026fac228fac42afac62df9c72ff9c93` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac2694ad2793ae2892b02991b12a90b22b` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `aca457acb4679cc4778cc4977cd4a76ce4` | high |
| **HIGH** | Twilio Account SID | `https://d3js.org/d3.v7.min.js` | `ac33fdae32fdaf31fdb130fdb22ffdb42f` | high |
| **HIGH** | API Token / Key | `https://d3mey6isb8np59.cloudfront.net/nvidia/main.js` | `api_error` | medium |
| **HIGH** | API Token / Key | `https://d3mey6isb8np59.cloudfront.net/nvidia/main.js` | `api_latency` | medium |
| **HIGH** | API Token / Key | `https://d3mey6isb8np59.cloudfront.net/nvidia/main.js` | `API latency` | medium |
| **HIGH** | API Token / Key | `https://d3mey6isb8np59.cloudfront.net/nvidia/main.js` | `API failed` | medium |
| **HIGH** | API Token / Key | `https://d3mey6isb8np59.cloudfront.net/nvidia/main.js` | `API request` | medium |
| **HIGH** | Twilio Account SID | `https://d3mey6isb8np59.cloudfront.net/nvidia/main.js` | `acy-notice-link-hover-underline-co` | high |
| **MEDIUM** | Twilio App SID | `https://d3mey6isb8np59.cloudfront.net/nvidia/main.js` | `applyClearHistoryButtonStyleConfig` | medium |
| **HIGH** | Hardcoded Credentials | `https://d3mey6isb8np59.cloudfront.net/nvidia/main.js` | `password":return"password";default:return"text"}}c…` | medium |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__header-element` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__button--filter` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__filter-mobile-` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__button--mobile` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__autocomplete-w` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__autocomplete-t` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__autocomplete-i` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__filter-toggler` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__top-bar-expand` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__filters--visib` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__filters--overl` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__filters-panel-` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__button--primar` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__button--second` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form__filters-no-dat` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-faceted-search/js/faceted-search/build/facetedSearchBundle.js?ver=67484da` | `aceted-search-form-filters-wrapper` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-recommender/js/dist/index.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-recommender/js/dist/index.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-recommender/js/dist/index.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-recommender/js/dist/index.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/nv-recommender/js/dist/index.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/ja-jp/wp-content/plugins/syntaxhighlighter/syntaxhighlighter3/scripts/shBrushBash.js?ver=3.0.9b` | `pwd quota` | medium |
| **HIGH** | Basic Auth Credentials | `https://developer-blogs.nvidia.com/ja-jp/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `BasicClassPrefix` | high |
| **HIGH** | Basic Auth Credentials | `https://developer-blogs.nvidia.com/ja-jp/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `BasicClassPrefix=function` | high |
| **HIGH** | API Token / Key | `https://developer-blogs.nvidia.com/ja-jp/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `ApiKeydownHandler` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/ja-jp/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `password" autofill="no"` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/ja-jp/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `password",autofill:"no"})})}),g.define("drag_drop"…` | medium |
| **HIGH** | API Token / Key | `https://developer-blogs.nvidia.com/ja-jp/wp-content/themes/nvidia/resources/assets/libs/nv-developer-menu/nv-developer-menu.js?ver=1.0.0` | `API Catalog` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/ja-jp/wp-includes/js/jquery/jquery.min.js?ver=3.7.1` | `password:!0,image:!0})b.pseudos[e]=B(e);for(e` | medium |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/wp-content/plugins/nv-recommender/js/dist/index.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/wp-content/plugins/nv-recommender/js/dist/index.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://developer-blogs.nvidia.com/wp-content/plugins/nv-recommender/js/dist/index.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/wp-content/plugins/nv-recommender/js/dist/index.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/wp-content/plugins/nv-recommender/js/dist/index.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **HIGH** | Basic Auth Credentials | `https://developer-blogs.nvidia.com/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `BasicClassPrefix` | high |
| **HIGH** | Basic Auth Credentials | `https://developer-blogs.nvidia.com/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `BasicClassPrefix=function` | high |
| **HIGH** | API Token / Key | `https://developer-blogs.nvidia.com/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `ApiKeydownHandler` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `password" autofill="no"` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/wp-content/themes/nvidia/dist/scripts/main_5b67153c.js` | `password",autofill:"no"})})}),g.define("drag_drop"…` | medium |
| **HIGH** | API Token / Key | `https://developer-blogs.nvidia.com/wp-content/themes/nvidia/resources/assets/libs/nv-developer-menu/nv-developer-menu.js?ver=1.0.0` | `API Catalog` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer-blogs.nvidia.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1` | `password:!0,image:!0})b.pseudos[e]=B(e);for(e` | medium |
| **HIGH** | API Token / Key | `https://developer.download.nvidia.com/scripts/typesense.js` | `APIKEYHEADERNAME` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.download.nvidia.com/scripts/typesense.js` | `password = unescape(encodeURIComponent(config.auth…` | medium |
| **HIGH** | Basic Auth Credentials | `https://developer.nvidia.com/assets/bootstrap/5.1.3/bootstrap.bundle.min-51ad1d8cab4ebd9873a0429f5e67ca717a71fd96daf8025bc04a88848e5b375c.js` | `BasicClassPrefix` | high |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/assets/bootstrap/5.1.3/bootstrap.bundle.min-51ad1d8cab4ebd9873a0429f5e67ca717a71fd96daf8025bc04a88848e5b375c.js` | `ApiKeydownHandler` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/assets/devzone3/new/dist/dz3-new-bundle-5e5224f77427893f6e6e8928b699298c96fb16292431055f18e740803e7ddea8.js` | `ApiKeydownHandler` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/assets/devzone3/new/dist/dz3-new-bundle-5e5224f77427893f6e6e8928b699298c96fb16292431055f18e740803e7ddea8.js` | `password: !0,` | medium |
| **INFORMATIONAL** | Other Secret | `https://developer.nvidia.com/assets/feed-aggregator/feed-aggregator-7f147443abc2d1300a239c29e4ba3ca0d0d2eb0dc66b608765e2b3be50e18e10.js` | `('Connection aborted.', ConnectionResetError(104, …` | low |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac8bcbddcdadaeb636363969696bdbdbdd` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac8226ad8127ad8128ae8029af7f2ab07f` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac16d4cc26c4ec36b50c46a52c56954c56` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac8645cc8635ec96260ca6063cb5f65cb5` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac76feae77feb078feb27afeb47bfeb67c` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `acfcecaefceeb0fcf0b2fcf2b4fcf4b6fc` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `acb4149cc4248ce4347cf4446d04545d24` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac11fcae12fcb014fcb216fcb418fbb61a` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac026fac228fac42afac62df9c72ff9c93` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac2694ad2793ae2892b02991b12a90b22b` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `aca457acb4679cc4778cc4977cd4a76ce4` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac33fdae32fdaf31fdb130fdb22ffdb42f` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/assets/horizontal-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `password:function(t){return` | medium |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac8bcbddcdadaeb636363969696bdbdbdd` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac8226ad8127ad8128ae8029af7f2ab07f` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac16d4cc26c4ec36b50c46a52c56954c56` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac8645cc8635ec96260ca6063cb5f65cb5` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac76feae77feb078feb27afeb47bfeb67c` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `acfcecaefceeb0fcf0b2fcf2b4fcf4b6fc` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `acb4149cc4248ce4347cf4446d04545d24` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac11fcae12fcb014fcb216fcb418fbb61a` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac026fac228fac42afac62df9c72ff9c93` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac2694ad2793ae2892b02991b12a90b22b` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `aca457acb4679cc4778cc4977cd4a76ce4` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `ac33fdae32fdaf31fdb130fdb22ffdb42f` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/assets/legacy-chart/d3.v4.min-41cfecdf7c41476e805de7afacf4aacdd1a4be6947fbecf95217e947ebc2faf5.js` | `password:function(t){return` | medium |
| **HIGH** | Basic Auth Credentials | `https://developer.nvidia.com/assets/momentjs/moment-b955adb4137f92dd932ff2c3179ce60cb5e1daed5fcc4423f95cf17df02b4d68.js` | `basicIsoRegex` | high |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/assets/momentjs/moment-b955adb4137f92dd932ff2c3179ce60cb5e1daed5fcc4423f95cf17df02b4d68.js` | `April_May_June_July_August_Septemb` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/assets/momentjs/moment-b955adb4137f92dd932ff2c3179ce60cb5e1daed5fcc4423f95cf17df02b4d68.js` | `Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_De` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/assets/nv-developer-menu-c88ee4614adbf7a100e9a74ffafb4d2c78601cff8c61752d42de9d8ba1b5d769.js` | `API Catalog` | medium |
| **HIGH** | Basic Auth Credentials | `https://developer.nvidia.com/assets/sf-validation/moment-620a5949fff0ad37198f07464b91d7b7c110ecdb6f94ca90ca7d2e1b471f1da8.js` | `basicIsoRegex` | high |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/assets/sf-validation/moment-620a5949fff0ad37198f07464b91d7b7c110ecdb6f94ca90ca7d2e1b471f1da8.js` | `April_May_June_July_August_Septemb` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/assets/sf-validation/moment-620a5949fff0ad37198f07464b91d7b7c110ecdb6f94ca90ca7d2e1b471f1da8.js` | `Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_De` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/data-science/sage/filter-preselect.js` | `api getTCData` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/data-science/sage/filter-preselect.js` | `api_found` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/data-science/sage/filter-preselect.js` | `api function` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/blog/category/data-science/sage/filter-preselect.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/blog/category/data-science/sage/filter-preselect.js` | `password:!0}};return{ajax:{deny_list:void` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/blog/category/data-science/sage/filter-preselect.js` | `password:!0}:(0,g.R)(7,t)}},session_trace:{enabled…` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/data-science/sage/main.js` | `api getTCData` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/data-science/sage/main.js` | `api_found` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/data-science/sage/main.js` | `api function` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/blog/category/data-science/sage/main.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/blog/category/data-science/sage/main.js` | `password:!0}};return{ajax:{deny_list:void` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/blog/category/data-science/sage/main.js` | `password:!0}:(0,g.R)(7,t)}},session_trace:{enabled…` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/robotics/sage/filter-preselect.js` | `api getTCData` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/robotics/sage/filter-preselect.js` | `api_found` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/robotics/sage/filter-preselect.js` | `api function` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/blog/category/robotics/sage/filter-preselect.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/blog/category/robotics/sage/filter-preselect.js` | `password:!0}};return{ajax:{deny_list:void` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/blog/category/robotics/sage/filter-preselect.js` | `password:!0}:(0,g.R)(7,t)}},session_trace:{enabled…` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/robotics/sage/main.js` | `api getTCData` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/robotics/sage/main.js` | `api_found` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/category/robotics/sage/main.js` | `api function` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/blog/category/robotics/sage/main.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/search-posts/sage/main.js` | `api getTCData` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/search-posts/sage/main.js` | `api_found` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/blog/search-posts/sage/main.js` | `api function` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/blog/search-posts/sage/main.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/blog/search-posts/sage/main.js` | `password:!0}};return{ajax:{deny_list:void` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/blog/search-posts/sage/main.js` | `password:!0}:(0,g.R)(7,t)}},session_trace:{enabled…` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/ja-jp/sage/main.js` | `application-27f4f7c671b317333903a4` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/ja-jp/sage/main.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/ja-jp/sage/main.js` | `9fc963c7-14e6-403d-bdec-ee671550bb7f` | high |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/ja-jp/sage/recommender.js` | `application-27f4f7c671b317333903a4` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/ja-jp/sage/recommender.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/ja-jp/sage/recommender.js` | `9fc963c7-14e6-403d-bdec-ee671550bb7f` | high |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `API Catalog` | medium |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-search-clear-filters--empty` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-filters-results--profile-te` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-search-results--layout-3-co` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-search-results--layout-4-co` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-search-stats-wrapper--cards` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-search-pagination--one-page` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-filters-form__sorting-widge` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-filters-form__sorting-heade` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-filters-form--filters_wrapp` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-filters-form--filters_toggl` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `accordion-item__description-list-r` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-search-card__pretitle--trun` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-search-card--with-image-pad` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `aceted-search-card--clickable-card` | high |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `api-core-configuration-filters-glo` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/packs/js/2104-1205c85fc37800ded6a3.js` | `0c627028-b44c-4ede-8699-ad757af8508d` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2681-d317b4e683473b6fe74d.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2681-d317b4e683473b6fe74d.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/2681-d317b4e683473b6fe74d.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/2681-d317b4e683473b6fe74d.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/2681-d317b4e683473b6fe74d.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/4692-a478c93816dbe985b4fa.js` | `password:!0,image:!0})r.pseudos[t]=de(t);for(t` | medium |
| **HIGH** | Basic Auth Credentials | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `Basics_of_HTTP/MIME_types/Common_types` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `act-async-component-lifecycle-hook` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ackgroundCornerRadiusFromCssVariab` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ackgroundCornerRadiusToCssVariable` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-icon-color-hovere` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-icon-color-with-t` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ace-placeholder-text-margin-bottom` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-left-larg` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-right-lar` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-top-large` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-bottom-la` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-background-color-` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-left-smal` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-right-sma` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-top-small` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-bottom-sm` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-left-medi` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-right-med` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-top-mediu` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-padding-bottom-me` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-text-color-disabl` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-border-color-sele` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-border-width-sele` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-icon-height-small` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ackground-color-conjunction-hovere` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actions-description-text-color-dis` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ace-placeholder-text-description-c` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `action-button-background-color-hov` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-drag-indicator-padding-l` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-drag-indicator-padding-r` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-drag-indicator-padding-t` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-drag-indicator-padding-b` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `aceholder-background-color-hovered` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ackground-corner-radius-drop-spot-` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ace-button-padding-horizontal-cont` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ace-button-contextual-button-margi` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ace-button-contextual-button-icon-` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ace-button-contextual-button-corne` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ace-button-contextual-button-paddi` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `ackground-color-remove-button-hove` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-border-color-high` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `actionbar-button-border-width-high` | high |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `aption-with-actions-text-color-dis` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `apse-button-background-color-hover` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `apter-caption-background-color-hov` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `apter-caption-background-color-foc` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `aption-with-actions-description-te` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `password:"password",range:"range",tel:"tel",text:"…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `password:"Password",range:"Range",tel:"Phone` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `password":"New` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `Password","current-password":"Current` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/486-4ee95e78721864401fdd.js` | `Password",organization:"Organization` | medium |
| **HIGH** | Basic Auth Credentials | `https://developer.nvidia.com/packs/js/6900-06759c19ec8c9a99401a.js` | `basic-components` | high |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/packs/js/6900-06759c19ec8c9a99401a.js` | `f18dab56-2dee-4195-ae3c-3147e7f90360` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/8465-34d1ba762d9cdeef15fb.js` | `password=xt.number=xt.tel=xt.url=xt.search=xt.date…` | medium |
| **HIGH** | API Token / Key | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `ApiKeyAsQueryParam` | medium |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `acetableFieldsWithSpecialCharacter` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `ackAutocompleteSuggestionClickThro` | high |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `apeSpecialCharsWithinTagAttributes` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `00000000-0000-0000-0000-000000000000` | high |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `password===t.password}function` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `password","range","tel","text","time","url","week"…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `password"].indexOf(this.inputType)>-1},t.prototype…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/8726-22e112d2c4254c5e6617.js` | `password"].indexOf(this.inputType)>-1},enumerable:…` | medium |
| **CRITICAL** | AWS Access Key ID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `asiAlbertGraphDistri` | high |
| **HIGH** | Basic Auth Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `BasicRecurrentLayer` | high |
| **HIGH** | Basic Auth Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `basic_slide` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `achievement_show_challenge_notific` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `acebook_request_publish_permission` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `achievement_type_achievement_chall` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `AcceptedForGameRankedByAcceptanceD` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_ADD_REQUISITE_YES_CO` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_CHANGE_REQUISITE_COD` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_CHANGE_REQUISITE_YES` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_DELETE_REQUISITE_COD` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_DELETE_REQUISITE_YES` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_EXECUTE_REQUISITE_CO` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_EXECUTE_REQUISITE_YE` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_NO_ACCESS_REQUISITE_` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_RATIFY_REQUISITE_COD` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_RATIFY_REQUISITE_YES` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_RIGHTS_VIEW_REQUISITE_YES_C` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACTION_TYPE_DISABLE_DELEGATE_ACCES` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACTION_TYPE_ENABLE_DELEGATE_ACCESS` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACTION_TYPE_ENCRYPTION_BY_CERTIFIC` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACTION_TYPE_ENCRYPTION_BY_PASSWORD` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACTION_TYPE_RECOVER_FROM_LOCAL_COP` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACTION_TYPE_WORKFLOW_DESCRIPTION_M` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACKED_DIAGNOSTICS_ACCESSED_WITHOUT` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACCESS_MODE_FOR_BRANCH_TRANSACTION` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACTIVE_SQL_TRANSACTION_FOR_BRANCH_` | high |
| **HIGH** | Twilio Account SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `ACTION_INTEGRITY_CONSTRAINT_VIOLAT` | high |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `APPROVING_SIGNATURE_REQUISITE_CODE` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `APPROPRIATE_ACCESS_MODE_FOR_BRANCH` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `APPROPRIATE_ISOLATION_LEVEL_FOR_BR` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `pwd","readonly","return","shift","test","times","t…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `Pwd","Qed","Quit","Rec","Record","Recursive","Redi…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `pwd quit` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `pwd python` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `password","path","pool","prepare","primary","priva…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `pwd r` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `pwd rand` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `pwd q\\s` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `pwd","read","refchan","regexp","registry","regsub\|…` | medium |
| **HIGH** | Hardcoded Credentials | `https://developer.nvidia.com/packs/js/9878-ace6038de3dd10e07189.js` | `pwd py3do` | medium |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/sage/main.js` | `application-27f4f7c671b317333903a4` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/sage/main.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/sage/main.js` | `9fc963c7-14e6-403d-bdec-ee671550bb7f` | high |
| **MEDIUM** | Twilio App SID | `https://developer.nvidia.com/sage/recommender.js` | `application-27f4f7c671b317333903a4` | medium |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/sage/recommender.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **CRITICAL** | Heroku API Key | `https://developer.nvidia.com/sage/recommender.js` | `9fc963c7-14e6-403d-bdec-ee671550bb7f` | high |
| **HIGH** | Hardcoded Credentials | `https://forums.developer.nvidia.com/highlight-js/forums.developer.nvidia.com/600885de53a0c5dcaf15540b83e94aafa44c5313.js` | `pwd","readonly","return","shift","test","times","t…` | medium |
| **MEDIUM** | AWS S3 Bucket URL | `https://github.com/algolia/autocomplete.js` | `github-cloud.s3.amazonaws.com` | high |
| **HIGH** | Basic Auth Credentials | `https://github.com/algolia/autocomplete.js` | `basic-configuration-options/` | high |
| **HIGH** | API Token / Key | `https://github.com/algolia/autocomplete.js` | `api_agentic_issue_marshal_yaml` | medium |
| **HIGH** | API Token / Key | `https://github.com/algolia/autocomplete.js` | `api_token_for_dotcom_context` | medium |
| **HIGH** | API Token / Key | `https://github.com/algolia/autocomplete.js` | `api_github_rest_style` | medium |
| **HIGH** | API Token / Key | `https://github.com/algolia/autocomplete.js` | `API reference` | medium |
| **HIGH** | Twilio Account SID | `https://github.com/algolia/autocomplete.js` | `aces_prebuild_region_target_update` | high |
| **HIGH** | Twilio Account SID | `https://github.com/algolia/autocomplete.js` | `accelerator_link_open_source_navba` | high |
| **HIGH** | Twilio Account SID | `https://github.com/algolia/autocomplete.js` | `ACSjY4rhSdOwF3qNcqPAa6idsb21aXkeBg` | high |
| **HIGH** | Twilio Account SID | `https://github.com/algolia/autocomplete.js` | `ac8cb5e9e6dfe42da3ca63edd9aeab5102` | high |
| **HIGH** | Twilio Account SID | `https://github.com/algolia/autocomplete.js` | `action-menu-79e78771-734e-4123-9a3` | high |
| **HIGH** | Twilio Account SID | `https://github.com/algolia/autocomplete.js` | `act-directory-row-name-cell-small-` | high |
| **HIGH** | Twilio Account SID | `https://github.com/algolia/autocomplete.js` | `act-directory-row-name-cell-large-` | high |
| **MEDIUM** | Twilio App SID | `https://github.com/algolia/autocomplete.js` | `Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoq` | medium |
| **MEDIUM** | Twilio App SID | `https://github.com/algolia/autocomplete.js` | `app_modernization_link_solutions_n` | medium |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `f8645a64-eb12-de53-929c-d619de01243c` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `6aaa2100-abef-11eb-93c3-9e2977fc734c` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `27ca63e6-109a-40d0-bee0-6ec70480b0e9` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `faa67bf3-e4d7-4d11-a266-23eacbf0659e` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `0d92ca81-33fc-40a3-9e98-69e3150243f6` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `75e3e29a-7bf1-4f3f-8dd5-f93229ffacbe` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `efa07a59-073b-4fe0-9235-5716439d9cab` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `61b2d38b-e67e-4f5a-a02f-68e08b4a7dec` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `23ce5e83-05ea-438f-b8a7-0c7f486626b4` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `6c71aa16-f862-4262-bb08-4430f46948a6` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `79e78771-734e-4123-9a35-50f6850172b4` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `4db636d1-0cdb-4eb6-ade5-cec3c2337efa` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `28347cfa-bf5d-4e8c-a109-265d8539c497` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `808fc855-d463-4725-8723-00625d145195` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `eeb57683-e39e-4882-8e64-9f64d2f06cc1` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `dd898f93-e930-4461-b65a-4264f1bd8715` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `1f282198-6e93-49db-a579-667b63bb8a28` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `ef1552ae-7339-46a6-a74c-736f1693fc86` | high |
| **CRITICAL** | Heroku API Key | `https://github.com/algolia/autocomplete.js` | `515f787c-6cea-45ee-825f-c0271a2eaefe` | high |
| **MEDIUM** | AWS S3 Bucket URL | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-by9tgp8z.digested.js` | `s3-bucket` | high |
| **MEDIUM** | AWS S3 Bucket URL | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-by9tgp8z.digested.js` | `s3-multipart` | high |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-by9tgp8z.digested.js` | `api support` | medium |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-by9tgp8z.digested.js` | `ACKVERYMINDBUSHWOLF_GQZbfghjklqvwy` | high |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-by9tgp8z.digested.js` | `password`&&Ei(e.target)}static{O(this.prototype,`p…` | medium |
| **MEDIUM** | Twilio App SID | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-bz82g8lx.digested.js` | `April_May_June_July_August_Septemb` | medium |
| **MEDIUM** | Twilio App SID | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-bz82g8lx.digested.js` | `Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_De` | medium |
| **HIGH** | Basic Auth Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `basic_topic` | high |
| **HIGH** | Basic Auth Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `basic_group` | high |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `API_KEY_SCOPE_MODES` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `API callback` | medium |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `ace_with_open_eyes_and_hand_over_m` | high |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `password:!0,image:!0})r.pseudos[t]=F(t);for(t` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `password:this.email_password,flair_icon:null,flair…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `password`),{type:`PUT`})}loadSecondFactorCodes(){r…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-c9o9v9mv.digested.js` | `password:e.accountPassword,username:e.accountUsern…` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-kzds8qh6.digested.js` | `API deprecated` | medium |
| **CRITICAL** | Heroku API Key | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-kzds8qh6.digested.js` | `1b32f5c2-7623-43d6-a0ad-9672898920a1` | high |
| **CRITICAL** | Heroku API Key | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-kzds8qh6.digested.js` | `30000000-1000-4000-2000-100000000000` | high |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-pd5tza7q.digested.js` | `api instead` | medium |
| **CRITICAL** | Heroku API Key | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-pd5tza7q.digested.js` | `30000000-1000-4000-2000-100000000000` | high |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-pd5tza7q.digested.js` | `password`,`range`,`search`,`tel`,`text`,`time`,`ur…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-pd5tza7q.digested.js` | `password:`password`};var` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-pd5tza7q.digested.js` | `password`;static{L(this.prototype,`type`,[j],funct…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-pd5tza7q.digested.js` | `password"],[16,"disabled",[30,1,["disabled"]]],[16…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-pd5tza7q.digested.js` | `password:Wc,question:Jc,"radio-group":il,select:dl…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/chunk-pd5tza7q.digested.js` | `Password:this.legacyComponentFor(Wc,e),Composer:th…` | medium |
| **MEDIUM** | AWS S3 Bucket URL | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `s3-multipart` | high |
| **HIGH** | Basic Auth Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `basicUsernameValidation` | high |
| **HIGH** | Basic Auth Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `basicNameValidation` | high |
| **HIGH** | Basic Auth Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `basic-topic-list` | high |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `API_KEY_SCOPE_MODES` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `API_KEY_INVALID` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_public_key` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `API_KEY_AUTHORIZATION_STATES` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `API_KEY_DEVICE_ACTIVATION_STATES` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `API_KEY_DEVICE_POLL_STATUSES` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_approved` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_last_used_at` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_expired_at` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_expires_at` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_expires_never` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_show_permissions` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_key_device_activation` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_key_authorization` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_key_otp` | medium |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `api_key_result` | medium |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `ActionWillDestroyAnyExistingMerged` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `ActionWillClearYourSearchResultsAr` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `access_permission_remove_descripti` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `access_permission_viewer_descripti` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `access_permission_editor_descripti` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `access-control__permission-descrip` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `acking-controls__watched-categorie` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `acking-controls__tracked-categorie` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `acking-controls__watched-first-cat` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `acking-controls__regular-categorie` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `acking-controls__watched-first-pos` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `account-email-validation-more-info` | high |
| **MEDIUM** | Twilio App SID | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `apLoggedInUsersToEveryoneForStorag` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password"],["if"]]`,moduleName:`(unknown` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`,`tel`,`text`,`url`]):e.validity.tooShort…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`).focus());if(r.authenticated){let` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password:n}){this.field=e,this.getValidationVisibl…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`),element:this.field.element})),UH.forEac…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password:t,showValidationOnInit:n=!0}){this.getUse…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password:this.getAccountPassword})))}}get` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`),...e}}function` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password===this.owner.accountUsername?kQ({reason:z…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`,{...GQ,type:`password`}),qQ(`radio-group…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password:()=>null,showValidationOnInit:!1});#O;#k=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password","generation","f"],["if","unless","each",…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`),(await` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password:this.password}})).success?(this.errorMess…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[24,0,"input-large"],[24,"autofocus","a…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password",[30,0,["sendPasswordResetEmail"]]]],null…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`,`email_from_alias`,`smtp_server`,`smtp_p…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password:e.email_password};return` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password:e.email_password}),this.toasts.success({d…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password","password",[28,[32,1],["groups.manage.em…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`)}static{I(this.prototype,`_init`,[Xo(`in…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`,{data:{login:this.emailOrUsername.trim()…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password"]],[30,0,["submitDisabled"]],"forgot_pass…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[M],function(){return!0})}#n=(P(this,`ma…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password=!this.maskPassword}static{I(this.prototyp…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[k])}authenticateSecurityKey(){x$(this.a…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[24,"maxlength","200"],[24,"tabindex","…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[12],[1,"\\n` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],null]],[1,"\\n` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password","@togglePasswordMask"],[[30,0,["maskPass…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password"]]],null],[12],[1,"\\n` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password","@loginPasswordChanged","@secondFactorMe…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password:this.login?.loginPassword,email:this.newE…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[24,1,"new-account-password"],[16,0,[28…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password","@togglePasswordMask","@parentController…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[M])}#e=(P(this,`accountPassword`),void` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password:()=>this.accountPassword});successMessage…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`)}static{I(this.prototype,`togglePassword…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password:this.accountPassword,user_custom_fields:e…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password"],[[30,1,["loginName"]],[30,1,["usePasswo…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password","@loginPasswordChanged","@secondFactorMe…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[M],function(){return``})}#f=(P(this,`lo…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[k])}securityKeyCredentialChanged(e){thi…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`),this.flashType=`error`;return}try{this.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password:this.loginPassword,second_factor_token:th…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`,this.loginPassword);let` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[24,1,"new-account-password"],[16,4,[52…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password","@togglePasswordMask"],[[30,1,["maskPass…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"]],null],[1,"\\n"]],[]]]],[]]],[1,"` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password=!0;passwordValidationHelper=new` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`)}static{I(this.prototype,`togglePassword…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password:this.accountPassword,second_factor_token:…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password:null,errorMessage:e})})}static{I(this.pro…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`)}model(e){if(Po.get(`password_reset`))re…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password"]],[[[1,"` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[14,"data-setting-name","user-password"…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password"]]],null]],[24,0,"btn` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"]],[[[1,"` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],null]],[1,"\\n"]],[]],[[[1,"` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password"]]],[[[1,"` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"]]],[[[1,"` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password"]]],null]],[16,"hidden",[30,1,["removePas…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"]],null],[1,"\\n\\n"],[41,[30,1,["canChec…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[E(`model.staged`)])}get` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[E(`model.is_anonymous`)])}get` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[k])}get` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[E(`model.is_anonymous`,`model.no_passwo…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`,!0)}).catch(e=>{this.set(`removePassword…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[k])}toggleShowAllAuthTokens(e){e?.preve…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password",[28,[32,7],null,[["accountName","account…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[12],[1,"\\n"],[41,[30,1,["passwordRequ…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[24,"aria-describedby","password-valida…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password"],[16,0,[28,[32,15],[[30,1,["accountPassw…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password",[30,1,["accountHoneypot"]]]],null],[1,"\…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password",[28,[32,7],null,[["accountName","account…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password","userFields"],[[30,1,["accountName"]],[3…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`,[M])}#i=(P(this,`accountPassword`),void` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password=!0;emailValidationVisible=!1;nameValidati…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password:()=>this.accountPassword,showValidationOn…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password:this.accountPassword,accountUsername:this…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`,this.accountPassword);let{destination_ur…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`]?.length>0&&this.passwordValidationHelpe…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `Password`)}static{I(this.prototype,`togglePassword…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password`,{path:`/password-reset`}),this.route(`fa…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/discourse-e0107frj.digested.js` | `password":sc,"discourse/form-kit/components/fk/con…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-ai_chunk.CIm3Zu-9qx3hf9x.digested.js` | `password"]],[["default"],[[[[1,"\\n` | medium |
| **HIGH** | Basic Auth Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-ai_main.BRqGhl-9qx3hf9x.digested.js` | `basic-topic-list` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-ai_main.BRqGhl-9qx3hf9x.digested.js` | `action-menu__translate-translation` | high |
| **HIGH** | API Token / Key | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-akismet_main.CfkKPX-pctu82q7.digested.js` | `api_error` | medium |
| **HIGH** | Basic Auth Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-assign_main.Calwtq-r88onvk1.digested.js` | `basic-topic-list` | high |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-calendar_main.CKhvh7-o1h6dm7e.digested.js` | `password:e.password\|\|"",userName:e.user_name,userE…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-calendar_main.CKhvh7-o1h6dm7e.digested.js` | `passWord:e.password\|\|"",userName:e.user_name,userE…` | medium |
| **HIGH** | Basic Auth Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-docs_main.CamamM-n1v6c4v7.digested.js` | `basic-topic-list` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-reactions_main.CL9FP0-alxkilxd.digested.js` | `actions_desaturated_reaction_panel` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-reactions_main.CL9FP0-alxkilxd.digested.js` | `actions-user-notification-reaction` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-reactions_main.CL9FP0-alxkilxd.digested.js` | `actions-admin-plugin-configuration` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-reactions_main.CL9FP0-alxkilxd.digested.js` | `actions-user-notifications-route-m` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-solved_main.c0CSSu-7zfz6z2g.digested.js` | `action-menu__solved-accepted-toolt` | high |
| **HIGH** | Twilio Account SID | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/discourse-yearly-review_main.Cyyo7p-e3s18qp9.digested.js` | `acyDashboardYearlyReviewAdminNotic` | high |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `Password",[r])}#s=void` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `Password")` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `Password=!0` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `Password")}static{dt7948.n(this.prototype,"toggleP…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `password:this.accountPassword,timezone:moment.tz.g…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `password"]&&e.errors["user_password.password"].len…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `Password"]]],null]],[16,4,[52,[30,1,["maskPassword…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `password"],[12],[1,[28,[32,5],["invites.password_l…` | medium |
| **HIGH** | Hardcoded Credentials | `https://global.discourse-cdn.com/nvidia/assets/gz/plugins/hosted-site_main.Drta7t-m58rmyap.digested.js` | `Password","@togglePasswordMask"],[[30,1,["maskPass…` | medium |
| **HIGH** | API Token / Key | `https://images.nvidia.com/aem-dam/Solutions/ot-js/ot-custom.js` | `API` | medium |
| **INFORMATIONAL** | Other Secret | `https://images.nvidia.com/aem-dam/Solutions/ot-js/ot-custom.js` | `function` | low |
| **CRITICAL** | Heroku API Key | `https://images.nvidia.com/aem-dam/Solutions/ot-js/ot-custom.js` | `77d885a8-5f36-43b2-96cc-76d21266da74` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password="",e.host=null,e.port=null,e.path=[],e.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password=o.password,e.host=o.host,e.port=o.port,e.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password=o.password,e.host=o.host,e.port=o.port,e.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password=o.password,e.host=o.host,e.port=o.port,s=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password=Ne.call(r),r.host=Pe.call(r),r.hostname=A…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password:Le(Ne,(function(e){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-0.7.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Basic Auth Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `BasicHtmlNodes:` | high |
| **HIGH** | Basic Auth Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `BasicHtmlNodesFor:` | high |
| **HIGH** | API Token / Key | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `API compatible` | medium |
| **HIGH** | API Token / Key | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `APIEndpoint` | medium |
| **HIGH** | API Token / Key | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `api response` | medium |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `ACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `action_to_next_paint_target_select` | high |
| **CRITICAL** | Heroku API Key | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `00000000-aaaa-0000-aaaa-000000000000` | high |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `password"===t.type\|\|"email"===t.type\|\|"tel"===t.ty…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-us/navigation-v3.3.0.js?ver=3.3.0` | `password")))return` | medium |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/resources-component/bundle-resources-spring2023.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/resources-component/bundle-resources-spring2023.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/resources-component/bundle-resources-spring2023.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/resources-component/bundle-resources-spring2023.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/resources-component/bundle-resources-spring2023.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/use-case-component/bundle-v3.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/use-case-component/bundle-v3.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/use-case-component/bundle-v3.js` | `actInternalMemoizedMergedChildCont` | high |
| **MEDIUM** | Twilio App SID | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/use-case-component/bundle-v3.js` | `APTOP-----------------------------` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/use-case-component/bundle-v3.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/aem-dam/en-zz/Solutions/industries/use-case-component/bundle-v3.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer-v2.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer-v2.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer-v2.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer-v2.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer-v2.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://images.nvidia.com/nv-story-tool/commons/react-header-footer.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://info.nvidia.com/js/forms2/js/forms2.min.js?ver=1.1.0.1` | `password:!0,image:!0})A.pseudos[z]=h(z);for(z` | medium |
| **HIGH** | API Token / Key | `https://info.nvidia.com/rs/156-OFN-742/images/businessemailvalidation.js?ver=1.1.0.1` | `apierkorb` | medium |
| **HIGH** | Basic Auth Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `basic_topic_list` | high |
| **HIGH** | Basic Auth Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `basic_auth` | high |
| **HIGH** | Basic Auth Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `basic_plan` | high |
| **HIGH** | Bearer Token | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `bearer_auth` | high |
| **HIGH** | Bearer Token | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `bearer_token` | high |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_approved` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_last_used_at` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_expires_at` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_expired_at` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_expires_never` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_show_permissions` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `API key setting` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_error` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `API Error` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `apier_webhook` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_base_url` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_base_url_blocked` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_access` | medium |
| **HIGH** | API Token / Key | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `api_webhooks` | medium |
| **HIGH** | Twilio Account SID | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `access_permission_editor_descripti` | high |
| **HIGH** | Twilio Account SID | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `access_permission_viewer_descripti` | high |
| **HIGH** | Twilio Account SID | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `access_permission_remove_descripti` | high |
| **HIGH** | Twilio Account SID | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `achment_upload_not_allowed_for_new` | high |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"Password"},"settings":{"title":"Setting…` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"Your` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":{"success":"(email` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"Set` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `Password","choose_new":"Choose` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password","choose":"Choose` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password","verify_identity":"To` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `Password","remove_disabled":"The` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"The` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"Forgot` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":{"title":"Password","too_short":{"one":"…` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password","confirm":"Confirm","incorrect_password"…` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":{"title":"Password` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password","invite":"Enter` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `Password","complete_username":"If` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"Password","show_password":"Show","hide_…` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password","hide_password_title":"Hide` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password","second_factor_title":"Two-Factor` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"Please` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"Reset` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `Password","logging_in":"Signing` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `Password"},"password_reset":{"continue":"Continue` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"Password","field_type_date":"Date","fie…` | medium |
| **HIGH** | Hardcoded Credentials | `https://sea2.discourse-cdn.com/nvidia/extra-locales/5f9ca1a060758bb72975d78bbee71d31937976b6/en/main.js` | `password":"After` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-login.nvidia.com/service/default/assets/index-VDLRcbtD.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-login.nvidia.com/service/default/assets/index-VDLRcbtD.js` | `password`)\|\|t===`textarea`\|\|e.contentEditable===`t…` | medium |
| **HIGH** | Twilio Account SID | `https://www.datadoghq-browser-agent.com/us1/v5/datadog-rum.js` | `ACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw` | high |
| **HIGH** | Twilio Account SID | `https://www.datadoghq-browser-agent.com/us1/v5/datadog-rum.js` | `action_to_next_paint_target_select` | high |
| **CRITICAL** | Heroku API Key | `https://www.datadoghq-browser-agent.com/us1/v5/datadog-rum.js` | `00000000-aaaa-0000-aaaa-000000000000` | high |
| **HIGH** | Hardcoded Credentials | `https://www.datadoghq-browser-agent.com/us1/v5/datadog-rum.js` | `password"===e.type\|\|"email"===e.type\|\|"tel"===e.ty…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.datadoghq-browser-agent.com/us1/v5/datadog-rum.js` | `password")))return` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/assets/nv-academy/v0.0.13/aem/assets/en.js` | `Achievements_downloadLearningTrans` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/assets/nvod/nvod-login.js` | `API called` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/assets/nvod/nvod-login.js` | `password="",t.host=null,t.port=null,t.path=[],t.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/assets/nvod/nvod-login.js` | `password=o.password,t.host=o.host,t.port=o.port,t.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/assets/nvod/nvod-login.js` | `password=o.password,t.host=o.host,t.port=o.port,t.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/assets/nvod/nvod-login.js` | `password=o.password,t.host=o.host,t.port=o.port,f=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/assets/nvod/nvod-login.js` | `password=Lt.call(r),r.host=Pt.call(r),r.hostname=k…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/assets/nvod/nvod-login.js` | `password:Ut(Lt,(function(t){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/assets/nvod/nvod-login.js` | `password="";for(var` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/assets/preferences-portal/bundle.js` | `ackChunk_monorepo_preferences_port` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/DLI/dli.js` | `API Error` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/DLI/dli.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/DLI/dli.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/DLI/dli.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/DLI/dli.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/DLI/dli.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/calendar/bundle-events-core.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/calendar/bundle-events-core.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/calendar/bundle-events-core.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/calendar/bundle-events-core.js` | `aCBmaWxsPSIjMDAwIiBkPSJNMzU3IDM1Lj` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/calendar/bundle-events-core.js` | `aCBmaWxsPSIjZmZmIiBkPSJNMzU3IDM1Lj` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/calendar/bundle-events-core.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/calendar/bundle-events-core.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/webinar.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/webinar.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/webinar.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/webinar.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/webinar.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/case-studies/casestudies_widget.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/case-studies/casestudies_widget.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/case-studies/casestudies_widget.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/case-studies/casestudies_widget.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/case-studies/casestudies_widget.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/case-studies/casestudies_widget.js` | `password:!0,number:!0,date:!0,month:!0,week:!0,tim…` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac8bcbddcdadaeb636363969696bdbdbdd` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac8226ad8127ad8128ae8029af7f2ab07f` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac16d4cc26c4ec36b50c46a52c56954c56` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac8645cc8635ec96260ca6063cb5f65cb5` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac76feae77feb078feb27afeb47bfeb67c` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `acfcecaefceeb0fcf0b2fcf2b4fcf4b6fc` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `acb4149cc4248ce4347cf4446d04545d24` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac11fcae12fcb014fcb216fcb418fbb61a` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac026fac228fac42afac62df9c72ff9c93` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac2694ad2793ae2892b02991b12a90b22b` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `aca457acb4679cc4778cc4977cd4a76ce4` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `ac33fdae32fdaf31fdb130fdb22ffdb42f` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/chart/d3.v4.min.js` | `password:function(t){return` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/bundle-search-prod-pub-v3.1.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/bundle-search-prod-pub-v3.1.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/bundle-search-prod-pub-v3.1.js` | `actInternalMemoizedMergedChildCont` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/bundle-search-prod-pub-v3.1.js` | `ab0dd5a5-e266-4b0a-a482-c706e6bed0fe` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/bundle-search-prod-pub-v3.1.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/bundle-search-prod-pub-v3.1.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/librarian-404-page.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/librarian-404-page.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/librarian-404-page.js` | `actInternalMemoizedMergedChildCont` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/librarian-404-page.js` | `ab0dd5a5-e266-4b0a-a482-c706e6bed0fe` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/librarian-404-page.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/librarian/librarian-404-page.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password="",e.host=null,e.port=null,e.path=[],e.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password=o.password,e.host=o.host,e.port=o.port,e.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password=o.password,e.host=o.host,e.port=o.port,e.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password=o.password,e.host=o.host,e.port=o.port,s=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password=Ne.call(r),r.host=Pe.call(r),r.hostname=A…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password:Le(Ne,(function(e){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/navigation/react/brandfooter.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Basic Auth Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `BasicImage` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password="",e.host=null,e.port=null,e.path=[],e.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password=i.password,e.host=i.host,e.port=i.port,e.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password=i.password,e.host=i.host,e.port=i.port,e.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password=i.password,e.host=i.host,e.port=i.port,s=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password=Pe.call(r),r.host=Ae.call(r),r.hostname=j…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password:ze(Pe,(function(e){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/newsroom/bundle-260403.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **LOW** | Google Captcha Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `6lVU1STUUTRodHTwaGppY1euo6vX0SGii6JBXwQY` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `API returned` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `ACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdT` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `ACxIAAAsSAdLdfvwAAAAHdElNRQfgChgTJ` | high |
| **MEDIUM** | Twilio App SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `APoAAACA6AAAdTAAAOpgAAA6mAAAF3Ccul` | medium |
| **MEDIUM** | Twilio App SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `APqKqqKucL9zD8v383e77xqnO2fBFYfRSb` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/react-brand/bundle.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/support/jquery-1.9.1.min.js` | `D27CDB6E-AE6D-11cf-96B8-444553540000` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/support/jquery-1.9.1.min.js` | `password:!0,image:!0})i.pseudos[n]=lt(n);for(n` | medium |
| **LOW** | Google Captcha Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `6Le5-BQmAAAAAMs1Nbm38roKdHBAXiPEt1cd8xjf` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `actInternalMemoizedMergedChildCont` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `e6a230f9-4ce5-4c30-b414-efcba39b4a6d` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `86058abb-49e8-4b2d-8f4c-d992f7755488` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `fa762272-d953-4c99-878d-abb0a20ba11c` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `ab0dd5a5-e266-4b0a-a482-c706e6bed0fe` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/Solutions/vertexAI/bundle-search-prod-pub.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/use-case/usecasesExplorerCatalogWidget.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/use-case/usecasesExplorerCatalogWidget.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/content/dam/en-zz/use-case/usecasesExplorerCatalogWidget.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/use-case/usecasesExplorerCatalogWidget.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/use-case/usecasesExplorerCatalogWidget.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/dam/en-zz/use-case/usecasesExplorerCatalogWidget.js` | `password:!0,number:!0,date:!0,month:!0,week:!0,tim…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/content/libraries/js/jquery-3.1.1.min.js` | `password:!0,image:!0})d.pseudos[b]=ma(b);for(b` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/de-de/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/de-de/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/de-de/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/en-au/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/en-au/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/en-au/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/en-au/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/en-eu/shield/js-agent.newrelic.com/nr-spa-1167.min.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/en-eu/shield/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/en-eu/shield/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/en-eu/shield/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/en-gb/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/en-gb/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/en-gb/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/en-gb/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/en-sg/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/en-sg/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/en-sg/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/en-sg/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/clientlibs/granite/jquery.min.cee8557e8779d371fe722bbcdd3b3eb7.js` | `D27CDB6E-AE6D-11cf-96B8-444553540000` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/etc.clientlibs/clientlibs/granite/jquery.min.cee8557e8779d371fe722bbcdd3b3eb7.js` | `password:!0,image:!0})B.pseudos[x]=l(x);for(x` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/I18N/en.min.1eef303f686fe0d9ec82c6dfdd24572d.js` | `API returns` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/I18N/en.min.1eef303f686fe0d9ec82c6dfdd24572d.js` | `API checks` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/I18N/en.min.1eef303f686fe0d9ec82c6dfdd24572d.js` | `password:!0,image:!0})b.pseudos[e]=de(e);for(e` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/I18N/zh_TW.min.eb9a2e6e93c9a11902ae492dda412530.js` | `API returns` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/I18N/zh_TW.min.eb9a2e6e93c9a11902ae492dda412530.js` | `API checks` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/I18N/zh_TW.min.eb9a2e6e93c9a11902ae492dda412530.js` | `password:!0,image:!0})b.pseudos[e]=de(e);for(e` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/affix.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/affix.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/affix.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/affix.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/alert.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/alert.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/alert.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/alert.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/button.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/button.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/button.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/button.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/carousel.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/carousel.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/carousel.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/carousel.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/collapse.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/collapse.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/collapse.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/collapse.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/dropdown.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/dropdown.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/dropdown.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/dropdown.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API doesn` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API surface` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API succeeded` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API provides` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API fails` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API until` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API returns` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API whereas` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API throws` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API takes` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API Failed` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API triggers` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API accepts` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API Usage` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API instead` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API would` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API indicates` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API enables` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API hides` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API displays` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API disables` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `api keypress` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API receives` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `API internally` | medium |
| **MEDIUM** | Twilio App SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `apOfObjectsHavingTempPathAndFileNa` | medium |
| **MEDIUM** | Twilio App SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `APSIBLE_COLUMNS_CONTROL_ROW_SELECT` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `Password : {` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/guideRuntime.min.32edfae982d5a7c4b0a2038f377d029d.js` | `Password");` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/modal.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/modal.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/modal.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/modal.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/popover.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/popover.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/popover.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/popover.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/recaptcha/api.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/recaptcha/api.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/recaptcha/api.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/recaptcha/api.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/recaptcha/enterprise.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/recaptcha/enterprise.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/recaptcha/enterprise.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/recaptcha/enterprise.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/scrollspy.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/scrollspy.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/scrollspy.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/scrollspy.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/spinner.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/spinner.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/spinner.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/spinner.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/tab.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/tab.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/tab.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/tab.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/tooltip.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/tooltip.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/tooltip.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/tooltip.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/transition.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/transition.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/transition.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/af/runtime/clientlibs/transition.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/Underscore.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/Underscore.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/Underscore.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/Underscore.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/e4x.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/e4x.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/e4x.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/e4x.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/etc.clientlibs/fd/xfaforms/clientlibs/third-party.min.be251cc80d68e452f51ac2fb0aadf86a.js` | `password:!0,image:!0})b.pseudos[e]=de(e);for(e` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/Node.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/Node.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/Node.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/Node.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **MEDIUM** | AWS S3 Bucket URL | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs-all.min.925e688d70287fd907edab04e0e0dde1.js` | `nvdmo-formsprocessor.s3.amazonaws.com` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs-all.min.925e688d70287fd907edab04e0e0dde1.js` | `ACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs-all.min.925e688d70287fd907edab04e0e0dde1.js` | `ACH5BAAAAAAALAAAAAACAAEAAAICBAoAOw` | high |
| **LOW** | Google Captcha Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN` | medium |
| **LOW** | Google Captcha Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `API_________` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `API___________` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `API error` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `API_INIT_FUNCTIONS` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `API_ON_EVENT` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `api_on_event` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `api event` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `aCfnp2cm5qZmJeWlZSTkpGQj46NjIuKiYi` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `AcGBQQDAgEAACH5BAEAAAAALAAAAAABAAE` | high |
| **MEDIUM** | Twilio App SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base.min.1636c5282c77b207f6ec21834a3d3f73.js` | `APDg0MCwoJCAcGBQQDAgEAACH5BAEAAAAA` | medium |
| **LOW** | Google Captcha Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN` | medium |
| **LOW** | Google Captcha Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `API_________` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `API___________` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `API error` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `API_INIT_FUNCTIONS` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `API_ON_EVENT` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `api_on_event` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `api event` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `aCfnp2cm5qZmJeWlZSTkpGQj46NjIuKiYi` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `AcGBQQDAgEAACH5BAEAAAAALAAAAAABAAE` | high |
| **MEDIUM** | Twilio App SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_base_scripts.min.ddd74b44c8650c2172d3935ccd1b8621.js` | `APDg0MCwoJCAcGBQQDAgEAACH5BAEAAAAA` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_form_container.min.2ba50dc5bb639615258634a4564a9376.js` | `APIKEYHEADERNAME` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_form_container.min.2ba50dc5bb639615258634a4564a9376.js` | `API Failed` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/etc/designs/nvidiaGDC/clientlibs_form_container.min.2ba50dc5bb639615258634a4564a9376.js` | `password = unescape(encodeURIComponent(config.auth…` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/runtime.js` | `API Catalog` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/runtime.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/etc/designs/nvidiaGDC/runtime.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/etc/designs/nvidiaGDC/runtime.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/fi-fi/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/fi-fi/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/fi-fi/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/fr-be/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/fr-be/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/fr-be/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/fr-fr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/fr-fr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/fr-fr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | API Token / Key | `https://www.nvidia.com/ja-jp/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `api` | medium |
| **INFORMATIONAL** | Other Secret | `https://www.nvidia.com/ja-jp/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `return` | low |
| **HIGH** | API Token / Key | `https://www.nvidia.com/ja-jp/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/ja-jp/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/ja-jp/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/nvidia-artifacts/nv-contenthub/cards/content-hub-cards.umd.cjs` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/nvidia-artifacts/nv-contenthub/cards/content-hub-cards.umd.cjs` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/nvidia-artifacts/nv-contenthub/cards/content-hub-cards.umd.cjs` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/nvidia-artifacts/nv-contenthub/cards/content-hub-cards.umd.cjs` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://www.nvidia.com/nvidia-artifacts/nv-contenthub/cards/content-hub-cards.umd.cjs` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/tr-tr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API Katalo` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/tr-tr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `ap snfn` | medium |
| **HIGH** | API Token / Key | `https://www.nvidia.com/tr-tr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `API variable` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/tr-tr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `ac254803_27c7_43e7_95b6_09ac2a70ad` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/tr-tr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/tr-tr/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |
| **LOW** | Google Captcha Key | `https://www.nvidia.com/zh-tw/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN` | medium |
| **LOW** | Google Captcha Key | `https://www.nvidia.com/zh-tw/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtbG5` | medium |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/zh-tw/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `account-icon-anonuser-mobile-label` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/zh-tw/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `aCfnp2cm5qZmJeWlZSTkpGQj46NjIuKiYi` | high |
| **HIGH** | Twilio Account SID | `https://www.nvidia.com/zh-tw/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `AcGBQQDAgEAACH5BAEAAAAALAAAAAABAAE` | high |
| **MEDIUM** | Twilio App SID | `https://www.nvidia.com/zh-tw/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `apper68552976_8f4b_4e10_a276_a7aec` | medium |
| **MEDIUM** | Twilio App SID | `https://www.nvidia.com/zh-tw/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `APDg0MCwoJCAcGBQQDAgEAACH5BAEAAAAA` | medium |
| **CRITICAL** | Heroku API Key | `https://www.nvidia.com/zh-tw/geforce/products/g-sync-monitors/js-agent.newrelic.com/nr-spa-1167.min.js` | `3e2b62ff-7ae7-4ac5-87c8-d5949ecafff5` | high |