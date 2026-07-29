# Security Assessment Report: netflix.com
**Generated Date:** 2026-07-29 01:52:17

---

## Executive Summary
- **Target:** `netflix.com`
- **Subdomains Discovered:** 3767
- **Live Web Endpoints (HTTPX):** 2
- **Crawled Endpoints (Katana):** 4479
- **Secrets Found in JS Files:** 1898
- **Nuclei Findings Count:** 0
- **TLS/SSL Security Alerts:** 0

---

## 1. Discovered Ports & Services (Nmap)

### Host: `54.246.79.9` (State: up)
| Port | Protocol | State | Service | Product / Version |
|---|---|---|---|---|
| 80 | tcp | open | tcpwrapped |   |
| 443 | tcp | open | tcpwrapped |   |

---

## 2. Vulnerability Assessment Findings (Nuclei)
No vulnerabilities identified by Nuclei.

---

## 3. TLS/SSL Security Audit Details (testssl)
No TLS/SSL audit findings recorded.

---

## 4. JavaScript Secret Analysis (SecretFinder)

### Scan Statistics

| Metric | Value |
|---|---|
| Status | `success` |
| Total JavaScript Files | 392 |
| Files Successfully Scanned | 392 |
| Files Failed / Timed Out | 0 |
| **Secrets Found** | **1898** |
| Critical | 388 |
| High | 1311 |
| Medium | 180 |
| Low | 19 |
| Informational | 0 |

### Findings

| Severity | Secret Type | Source JavaScript URL | Matched Value (truncated) | Confidence |
|---|---|---|---|---|
| **HIGH** | API Token / Key | `http://about.netflix.com/_next/static/chunks/245-2d5be4a0b4ebda6e.js` | `api object` | medium |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **LOW** | Google Captcha Key | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `6LesC-sgAAAAABvX8wXBEQtqn8RedE2rNYRd3I-f` | medium |
| **HIGH** | Basic Auth Credentials | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `BasicHtmlNodes:` | high |
| **HIGH** | Basic Auth Credentials | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `BasicHtmlNodesFor:` | high |
| **HIGH** | Basic Auth Credentials | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `basicOptionalMinutes:/` | high |
| **HIGH** | Basic Auth Credentials | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `basicOptionalSeconds:/` | high |
| **HIGH** | Basic Auth Credentials | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `basicOptionalMinutes` | high |
| **HIGH** | Basic Auth Credentials | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `basicOptionalSeconds` | high |
| **HIGH** | API Token / Key | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `API compatible` | medium |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `ac_April_Mei_Jun_Julai_Ogos_Septem` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `ac_Apr_Mei_Jun_Jul_Ogs_Sep_Okt_Nov` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `achi_Aprili_Mei_Juni_Julai_Agosti_` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `ac_Apr_Mei_Jun_Jul_Ago_Sep_Okt_Nov` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acy-of-inclusion-article-title-lin` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionArticleTitleLinkWrap` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `achea_Febrerachea_Marsachea_Abrila` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `achea_Junachea_Julaiachea_Agostach` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `achea_Otubrachea_Novembrachea_Deze` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-option--selec` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation--years-` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-dropdown--scr` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-read-view--do` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-read-view--se` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-dropdown-cont` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-option--sele` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-read-view--d` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-read-view--s` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-dropdown-con` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-year-option-` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-year-dropdow` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-year-read-vi` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__day--keyboard-sele` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__day--in-selecting-` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__day--selecting-ran` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__day--outside-month` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__week-number--click` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__week-number--selec` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__week-number--keybo` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__week--keyboard-sel` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--disabl` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--select` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--keyboa` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--in-sel` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--in-ran` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--range-` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--disa` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--sele` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--keyb` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--in-s` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--in-r` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--rang` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month--selecting-r` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__time-list-item--se` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__time-list-item--di` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__time-list-item--in` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__time-container--wi` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__header--time--only` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--selecte` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--disable` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--keyboar` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--range-s` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--range-e` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--in-rang` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--in-sele` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--selecti` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year--selecting-ra` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__input-time-contain` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker-time__input-contain` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation--previo` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation-icon--p` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation--next--` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation-icon--n` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__current-month--has` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__header--has-time-s` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__header__dropdown--` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__children-container` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker-ignore-onclickoutsi` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__close-icon--disabl` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__view-calendar-icon` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acy-of-inclusion-news-articles-car` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionNewsArticlesCarousel` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionArticlesGridItemCont` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionArticlesGridItemWrap` | high |
| **HIGH** | Twilio Account SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionArticlesGridImageWra` | high |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_mei_jun_jul_aug_sep_okt_nov_de` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_mei_juni_juli_augustus_septe` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Aprel_May_Iyun_Iyul_Avgust_Sentabr` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_May_Iyun_Iyul_Avg_Sen_Okt_Noy_` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_May_June_July_August_Septemb` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_Mei_Junie_Julie_Augustus_Sep` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Aug_Sep_Okt_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_Mei_Jun_Julai_Ogos_September` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Ogs_Sep_Okt_Nov_Di` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `aprel_may_iyun_iyul_avqust_sentyab` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_may_iyn_iyl_avq_sen_okt_noy_de` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_Mai_Juni_Juli_August_Septemb` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Aprili_Mei_Juni_Julai_Agosti_Septe` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Ago_Sep_Okt_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apili_Jumatatu_Jumanne_Jumatano_Al` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `aprill_mai_juuni_juuli_august_sept` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_mai_juuni_juuli_aug_sept_okt_n` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `aprile_maggio_giugno_luglio_agosto` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_mag_giu_lug_ago_set_ott_nov_di` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_mai_juni_juli_august_septemb` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maj_juni_juli_augusti_septem` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_maj_jun_jul_aug_sep_okt_nov_de` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maj_juni_juli_august_septemb` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apirila_maiatza_ekaina_uztaila_abu` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_Mei_Juni_Juli_Agustus_Septem` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Agt_Sep_Okt_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maj_junij_julij_avgust_septe` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maj_jun_jul_avgust_septembar` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Ags_Sep_Okt_Nop_De` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_mai_jun_jul_aug_sep_okt_nov_de` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maaie_juny_july_augustus_sep` | medium |
| **MEDIUM** | Twilio App SID | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `aprilie_mai_iunie_iulie_august_sep` | medium |
| **CRITICAL** | Heroku API Key | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `00000000-0000-0000-0000-000000000000` | high |
| **CRITICAL** | Heroku API Key | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `ffffffff-ffff-ffff-ffff-ffffffffffff` | high |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Password:eV.default,isTaxID:em.default,isDate:z.de…` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Password:eV.default,isTaxID:em.default,isDate:z.de…` | medium |
| **LOW** | Other Secret | `http://about.netflix.com/_next/static/chunks/pages/index-629a31e313a279d4.js` | `('Connection aborted.', ConnectionResetError(104, …` | low |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password="",s.host=null,s.port=null,s.path=[],s.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,c=…` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `Password:function(){return` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `Password:function(t){var` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=n.getPassword(),e.host=n.getHost(),e.host…` | medium |
| **HIGH** | Hardcoded Credentials | `http://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password",Ag("getPassword","setPassword")),so(Pg,"…` | medium |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/framework-1ce91eb6f9ecda85.js` | `password"===e.type)\|\|"textarea"===n\|\|"true"===e.co…` | medium |
| **LOW** | Google Captcha Key | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `6LesC-sgAAAAABvX8wXBEQtqn8RedE2rNYRd3I-f` | medium |
| **HIGH** | Basic Auth Credentials | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `BasicHtmlNodes:` | high |
| **HIGH** | Basic Auth Credentials | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `BasicHtmlNodesFor:` | high |
| **HIGH** | Basic Auth Credentials | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `basicOptionalMinutes:/` | high |
| **HIGH** | Basic Auth Credentials | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `basicOptionalSeconds:/` | high |
| **HIGH** | Basic Auth Credentials | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `basicOptionalMinutes` | high |
| **HIGH** | Basic Auth Credentials | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `basicOptionalSeconds` | high |
| **HIGH** | API Token / Key | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `API compatible` | medium |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `ac_April_Mei_Jun_Julai_Ogos_Septem` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `ac_Apr_Mei_Jun_Jul_Ogs_Sep_Okt_Nov` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `achi_Aprili_Mei_Juni_Julai_Agosti_` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `ac_Apr_Mei_Jun_Jul_Ago_Sep_Okt_Nov` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acy-of-inclusion-article-title-lin` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionArticleTitleLinkWrap` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `achea_Febrerachea_Marsachea_Abrila` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `achea_Junachea_Julaiachea_Agostach` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `achea_Otubrachea_Novembrachea_Deze` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-option--selec` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation--years-` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-dropdown--scr` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-read-view--do` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-read-view--se` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-dropdown-cont` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-option--sele` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-read-view--d` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-read-view--s` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-dropdown-con` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-year-option-` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-year-dropdow` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-year-read-vi` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__day--keyboard-sele` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__day--in-selecting-` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__day--selecting-ran` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__day--outside-month` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__week-number--click` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__week-number--selec` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__week-number--keybo` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__week--keyboard-sel` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--disabl` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--select` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--keyboa` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--in-sel` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--in-ran` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month-text--range-` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--disa` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--sele` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--keyb` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--in-s` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--in-r` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__quarter-text--rang` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__month--selecting-r` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__time-list-item--se` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__time-list-item--di` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__time-list-item--in` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__time-container--wi` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__header--time--only` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--selecte` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--disable` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--keyboar` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--range-s` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--range-e` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--in-rang` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--in-sele` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year-text--selecti` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__year--selecting-ra` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__input-time-contain` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker-time__input-contain` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation--previo` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation-icon--p` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation--next--` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__navigation-icon--n` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__current-month--has` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__header--has-time-s` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__header__dropdown--` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__children-container` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker-ignore-onclickoutsi` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__close-icon--disabl` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `act-datepicker__view-calendar-icon` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acy-of-inclusion-news-articles-car` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionNewsArticlesCarousel` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionArticlesGridItemCont` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionArticlesGridItemWrap` | high |
| **HIGH** | Twilio Account SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `acyOfInclusionArticlesGridImageWra` | high |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_mei_jun_jul_aug_sep_okt_nov_de` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_mei_juni_juli_augustus_septe` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Aprel_May_Iyun_Iyul_Avgust_Sentabr` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_May_Iyun_Iyul_Avg_Sen_Okt_Noy_` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_May_June_July_August_Septemb` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_Mei_Junie_Julie_Augustus_Sep` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Aug_Sep_Okt_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_Mei_Jun_Julai_Ogos_September` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Ogs_Sep_Okt_Nov_Di` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `aprel_may_iyun_iyul_avqust_sentyab` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_may_iyn_iyl_avq_sen_okt_noy_de` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_Mai_Juni_Juli_August_Septemb` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Aprili_Mei_Juni_Julai_Agosti_Septe` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Ago_Sep_Okt_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apili_Jumatatu_Jumanne_Jumatano_Al` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `aprill_mai_juuni_juuli_august_sept` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_mai_juuni_juuli_aug_sept_okt_n` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `aprile_maggio_giugno_luglio_agosto` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_mag_giu_lug_ago_set_ott_nov_di` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_mai_juni_juli_august_septemb` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maj_juni_juli_augusti_septem` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_maj_jun_jul_aug_sep_okt_nov_de` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maj_juni_juli_august_septemb` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apirila_maiatza_ekaina_uztaila_abu` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `April_Mei_Juni_Juli_Agustus_Septem` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Agt_Sep_Okt_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maj_junij_julij_avgust_septe` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maj_jun_jul_avgust_septembar` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Apr_Mei_Jun_Jul_Ags_Sep_Okt_Nop_De` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `apr_mai_jun_jul_aug_sep_okt_nov_de` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `april_maaie_juny_july_augustus_sep` | medium |
| **MEDIUM** | Twilio App SID | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `aprilie_mai_iunie_iulie_august_sep` | medium |
| **CRITICAL** | Heroku API Key | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `00000000-0000-0000-0000-000000000000` | high |
| **CRITICAL** | Heroku API Key | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `ffffffff-ffff-ffff-ffff-ffffffffffff` | high |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Password:eV.default,isTaxID:em.default,isDate:z.de…` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/pages/_app-7718d23e00d2f0d1.js` | `Password:eV.default,isTaxID:em.default,isDate:z.de…` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password="",s.host=null,s.port=null,s.path=[],s.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,c=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `Password:function(){return` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `Password:function(t){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=n.getPassword(),e.host=n.getHost(),e.host…` | medium |
| **HIGH** | Hardcoded Credentials | `https://about.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password",Ag("getPassword","setPassword")),so(Pg,"…` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `6l51krOo8gn3NUdIe0AAAAUCAESEAAAAAAEkm5NA` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `6Ly9jcmwuYXBwbGUuY29tL2tleXNlcnZpY2VzLmN` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `apiEndpoint` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ApiErrorSyncSymbol` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `API request` | medium |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ac1Nya3hjMndPRHZpWWNCMmJoWDdQOTNHQ` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcwA9ACIAaAB0AHQAcAA6AC8ALwBzAGMAa` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC4AbQBpAGMAcgBvAHMAbwBmAHQALgBjAG` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC8AMgAwADAANwAvADAAMwAvAFAAbABhAH` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACIAIAB2AGUAcgBzAGkAbwBuAD0AIgA0AC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACIAPgA8AEQAQQBUAEEAPgA8AFAAUgBPAF` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACIAIABWAEEATABVAEUAPQAiAEEAQQBBAE` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACIAPgA8AC8ASwBJAEQAPgA8AC8ASwBJAE` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcAA6AC8ALwBjAGEAcABwAHIAcwB2AHIAM` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC8AcwBpAGwAdgBlAHIAbABpAGcAaAB0AD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcwBtAGEAbgBhAGcAZQByAC4AYQBzAG0Ae` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC8ATABBAF8AVQBSAEwAPgA8AEwAVQBJAF` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcgBzAHYAcgAwADYALwBzAGkAbAB2AGUAc` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACBtZGhkAAAAAAAAAAAAAAAAAABdwAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACXm1pbmYAAAAUdm1oZAAAAAEAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACRkaW5mAAAAHGRyZWYAAAAAAAAAAQAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACB0ZW5jAAAAAAAAAQgAAAAABJJuTQAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC5YXZjMQAAAAAAAAABAAAAAAAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcgBzAGkAbwBuAD0AIgA0AC4AMgAuADAAL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACIAIAB4AG0AbABuAHMAPQAiAGgAdAB0AH` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC8AcwBjAGgAZQBtAGEAcwAuAG0AaQBjAH` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC4AYwBvAG0ALwBEAFIATQAvADIAMAAwAD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcgAiAD4ADQAKACAAIAA8AEQAQQBUAEEAP` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAIAA8AEQARQBDAFIAWQBQAFQATwBSAF` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC8ARABFAEMAUgBZAFAAVABPAFIAUwBFAF` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgA8AC8AVwBSAE0ASABFAEEARABFAFIAP` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACBtZGhkAAAAAAAAAAAAAAAAAAB1MAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AClnN0c2QAAAAAAAAAAgAAAWtlbmN2AAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC0ABIAAAASAAAAAAAAAABAAAAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACXQBLwqIAAQAHRAHBcvY8kAAAABBwYXNw` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AChzY2hpAAAAIHRlbmMAAAAAAAABCAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACB0cmV4AAAAAAAAAAEAAAABAAAD6QAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAdgBlAHIAcwBpAG8AbgA9ACIANAAuAD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC4AMAAiACAAeABtAGwAbgBzAD0AIgBoAH` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcwBvAGYAdAAuAGMAbwBtAC8ARABSAE0AL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC8AMAAzAC8AUABsAGEAeQBSAGUAYQBkAH` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgAgACAAPABEAEEAVABBAD4ADQAKACAAI` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAPABEAEUAQwBSAFkAUABUAE8AUgBTAE` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgAgACAAPAAvAEQAQQBUAEEAPgANAAoAP` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACZW1pbmYAAAAUdm1oZAAAAAEAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcllbmN2AAAAAAAAAAEAAAAAAAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACRGAAVtaAABwSAAAAAQc3R0cwAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAADa3RyYWsAAABcdGtoZAAAAAHk19Zf` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACRlZHRzAAAAHGVsc3QAAAAAAAAAAQAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AChG1pbmYAAAAUdm1oZAAAAAEAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACHABIAAAASAAAAAAAAAABAAAAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACBkdmNDAQAKDQAAAAAAAAAAAAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAIAAoAAAABQc2luZgAAAAxmcm1hZHZo` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACamQAHyWAAAdpQAAAAzGR2aGUAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgAAAABRidHJ0AACamQAHyWAAAdpQAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC4AMAAuADAAIgAgAHgAbQBsAG4AcwA9AC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcAA6AC8ALwBzAGMAaABlAG0AYQBzAC4Ab` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcgBvAHMAbwBmAHQALgBjAG8AbQAvAEQAU` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgAgACAAIAAgADwARABFAEMAUgBZAFAAV` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `aCBHUEFDIDIuMy1ERVYtcmV2NzMyNC1nYm` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcZWxzdAAAAAAAAAABAAAAAAAAAAAAAQAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACVoZGxyAAAAAAAAAABzb3VuAAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `Ac291bgAAAAFIbWluZgAAABBzbWhkAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACWbXA0YQAAAAAAAAABAAAAAAAAAAAAAgA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACEIAIGQAYCAAABMAK5JYATgAgAASfSwAG` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAAAAQABAAAAOG12ZXgAAAAQbWVoZAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAAABwAAAEgAAAAAAAAACE5ldGZsaXgA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAAAJAAAQBAU73up7T8eJYVK4UHuKYgM` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAAAAAQAAAAwAAAAHAAABmAAAAAAAAACA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAUGxheVJlYWR5IFNMMCBNZXRlcmluZyB` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAMS4wLjAuMQAAAAAAAAAAAAAAAAAAAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcgZnR5BwBpBzBvA2gBYBABgA4CBkBzBtg` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACBCBtFvB2gDYBdsbXZoBkgA4BgAAJC7CA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgGABeWdHJhBrgBYBBcB0BrgOYDgIIKgL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACABgAYBdMdHJhgC4CAgB0gC4CACAAA6gC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAUgG4AB1BugFYFAIgAYBBsgAQAcYCG1k` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACPAdHdDcgCQFAPgHIRgbgBgdIBDjgFgMA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC7CAgtgFgCIBC2gPgBCOgK4BgEoFAHCNg` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAeA2gCYBDegVwADxgSoADdguoAgAAEgd` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAbgioSABgagBDWC0gjQogdARgk4NgAAC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAGgDYDgioOhCwCCtgjQphHokBghiAJgA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcbbbfPhUQBgEYEiFQCADBrgP4BhFICgEg` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACABhWwGgrgEgAAQADhkwBhWQChkYFgIYM` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACA7jcoFC4hFQWiJgBj4oDj7wEBfgQ4LhW` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AChxwFghAMgEACAdjYgFDcgQQWgcABhxYD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACCtBtFvB2gDYBdsbXZoBkgA4BgAAJBdDA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgGABefdHJhBrgBYBBcB0BrgOYDADgLoZ` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgaQMgkwAAQgwQJAqBlgGQABzgBACADAc` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACdidWR0gZICBagG4AgA4DgAACAhgrwKgy` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACABgAYBdkdHJhgC4CAcB0gC4CACAAAqgC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAwgGYAB1BugAwAACgE4CAHgAYBCEgAYB` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcsN4FAqsN4LsNYUB4sNYEACsNYGDMgCwE` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgGABfhdHJhBrgBYBBcB0BrgOYDAHgLoZ` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgZQMgjwAAQgvQJB0BlgGQABzgBACADgL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcSS2aBACAEAGALBcCIACAJACAIAJAIAAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACCGAIBCgHAAgQoABggGAAcFFUKegSwAeu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAhg0AKg6gBhHQAFwgp4CgAAHBIBpBsgP` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACCpB0hZQAgPgChbIAgHgDgKQDBGgFwAg4` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACUBtFvBmgA4BcQbWZoBkgA4BgAACABgAY` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcB0gC4CACAAAqgC4FgAYBAIgBIEgGYBgD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACBIgGYAB1BugAwAACAFgBYBAMgAYBCcgJ` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcSS2aBACAEAGALBcCIACAJACAIAJgQIAc` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACCGAIBCAAAggVgABggGAAcFFUKeBsAACu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcP8ARWDLAEAAA5BAB7AkAAAbCVDAAMCbD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACjCpZpgACEdVMAFtDKDgAjgVIACDDwgvQ` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACQCngVQHBwhEwCALAiCaalgACRgqoOA0g` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACKDZBgklYABNklYCcCQIejDUAQgFAAgAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACYgACTCmhoAAdhIEPYD2ACAVhLIIALAlg` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AClCkojoAocwCDQgNQABooZICBObSgACUD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgrwTAEgrwDBEgfAAAggrwAgnoAgrwYgC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACCfhx5wABDzhx5XDggAYBAOgDgDCPhtZS` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACuhtYMAACegzgChtYXDggaQBhtYyAhgKo` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcxQ4EFBMAAAKAThWgBAPCkgHAAB3hXABc` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACBAgDYDBZABBBgA4Dgd4ACBgA4DAYgB4F` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AccAwDEAEAIAACADQAKCWCxAIBdA9D8DAD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACCfgiAAckgUSQAJAkBBAECECIADgXYAfd` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgtYZAEgtYDBEgf4AAggtYAgowAgtYcgD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgEYAgzAKADANBDgzAJAugzAACEAgAGgE` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcUIIQCgzoWAEgzoDBDCwg4QCgEgAgzoKA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AC4g2wCB8AOA2g6IKgzwFg6IAgJwAcGPQT` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACpCDhF4JAphF4ACDCAhFYAhF4De0WsyEA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACDNBtFvB2gDYBdsbXZoBkgA4BgAAJBdDA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgAQBchdHJhBrgBYBBcB0BrgOYDgIIKgL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcF3AB4ChBMCwgJQAcFaOvjDLgT4CAQBwh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACguQBBnDggAYEgEYAgW4AgvADgAAGgB4B` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgqYAhdhRDjhdg9CjhdgEABBXhdgMABBH` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACgPgCCQgfAEgI4AH9H6gBAAAPADCggIoB` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AChboAgEIBhcQBgAQAddmLAkChgDgBBtBC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACXBAASDwABAuCAAlDhCigOIBcHRAHBByD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACggHgBcAIPWAAKD8CAgAoDCQgDICANgDI` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AczjsxSCKBCD8BJgDQBgEAAADA8gFIDBXD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAOgZIAfgDjjCARC8CVgBoBBTgOYAgEQI` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACACgPgCCQgfAEgI4AH9H6gBAAAPhQoDhb` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAggGoBAACQgAgCgAQBddmLAkgDYBBtBC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACXBAASDwABAuCAAlDhgVYCdEAcFyD2A8g` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACggPoCcg9YAKD8CAgAoDCQgDICANgDIAA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ACAQgMoBdw6rGEAnB4gMwPANgIgGh1YAgE` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AcceptableVMAFRebufferScalingFacto` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `aceRateSelectorAlgorithmNonPipelin` | high |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgA8AEQAQQBUAEEAPgA8AFAAUgBPAFQAR` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APQAiAEEARQBTAEMAVABSACIAIABWAEEAT` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APQAiAEEAQQBBAEEAQQBNAFkARQB4AEkAR` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APQA9ACIAPgA8AC8ASwBJAEQAPgA8AC8AS` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgA8AEwAQQBfAFUAUgBMAD4AaAB0AHQAc` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgA8AEwAVQBJAF8AVQBSAEwAPgBoAHQAd` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APABEAEUAQwBSAFkAUABUAE8AUgBTAEUAV` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgBPAE4ARABFAE0AQQBOAEQAPAAvAEQAR` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `apTitlesForResolutionVMAFStreamFil` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APpAAAAAAABAAAAAAGJcHNzaAAAAACaBPB` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APQAiAGgAdAB0AHAAOgAvAC8AcwBjAGgAZ` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgANAAoAIAAgACAAIAA8AEQARQBDAFIAW` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APpAAB1MPoq978AS6AJeACXQBLwqIAAQAH` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APABEAEEAVABBAD4ADQAKACAAIAAgACAAP` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APAAvAEQAQQBUAEEAPgANAAoAPAAvAFcAU` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APpAABAAAAAAK6bWRpYQAAACBtZGhkAAAA` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APAAAAACBkdmNDAQAKDQAAAAAAAAAAAAAA` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APQAiADQALgAyAC4AMAAuADAAIgAgAHgAb` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgANAAoAIAAgADwALwBEAEEAVABBAD4AD` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ApMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ap7Znzn7preIvmS93xWjm75I6UBVQGo6pn` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgBgCAUBignwAB0gAwAADgpYBDugB4CDA` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgHIRgbgBgdIBDjgFgMAGC1CtgNgADQgO` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APC6CRAFCAAyAaAoACCfgiAAckgUSQAJAk` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ApAYAyC9AdBNAmDtAABiBhBEChBiA0CxC7` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `Ap8AKAkgJwKfYsUrPgJoCgDIAAOgJoBhAg` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AphF4ACDCAhFYAhF4De0WsyEAUBXA2B4AS` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `ApBnkJ4hf8AAIOAAAAACgGeYXRCvwAAtoA` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APADCggIoBcYQAEMABgFIAgEAChboAgEIB` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APhQoDhboFhLIFAAAThSYAghIABuBjBshO` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `APgEwBAzgA4BhRYAhk4EDShk4JCNhe4JgC` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `AppendHeadersWhenClearAndEncrypted` | medium |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAABAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAABAAAAAAYAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAH0gABAAAAAAKzbWRpYQAAACBtZGhkAAAAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAACRkaW5mAAAAHGRyZWYAAAAAAAAAAQAAAAx1…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAAAAYAA2ABIAAAASAAAAAAAAAABAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAA4PAAAAC5YXZjMQAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAUYnRydAAAV0MABDEQAADg8AAAABBzdHRzAAAAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAABAAAAABQAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAH0gABAAAAAAN3bWRpYQAAACBtZGhkAAAAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAACRkaW5mAAAAHGRyZWYAAAAAAAAAAQAAAAx1…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAAABQAC0ABIAAAASAAAAAAAAAABAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAPpAAB1MPoq978AS6AJeACXQBLwqIAAQAHRAHBcvY8kAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAATY29scm5jbHgAAQABAAEAAAAAUHNpbmYAAAAMZnJtYWh2…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAChzY2hpAAAAIHRlbmMAAAAAAAABCAAAAAAEkm5NAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAATY29scm5jbHgAAQABAAEAAAAAFGJ0cnQAAH0dAA6tQAAH…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAABAAAD6QAAAAAAAQAAAAABiXBzc2gAAAAAmgTweZhAQoar…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAABAAAAAAmAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAPpAABAAAAAAK6bWRpYQAAACBtZGhkAAAAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAACRkaW5mAAAAHGRyZWYAAAAAAAAAAQAAAAx1…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAAAAmABVgBIAAAASAAAAAAAAAABAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAA3aGRscgAAAAAAAAAAdmlkZQAAAAAAAAAAAAAAAD9AR…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAACRkaW5mAAAAHGRyZWYAAAAAAAAAAQAAAAx1…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAAAAAAAAAAAAAAAAAAA8ACHABIAAAASAAAAAAAAAABAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAABAAAAE2NvbHJuY2x4AAIAAgACgAAAABRidHJ0AACamQAH…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAEAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAQAAAAAA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAAMdXJsIAAAAAEAAAEMc3RibAAAAKZzdHNkAAAAAAAAAAEA…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `eAAAAAABAAUAAAAMAAAAAAABAAYAAABcAAAAAQABAgAAAAAAgl…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAAACAAAABwAAAEgAAAAAAAAACE5ldGZsaXgAAAAAH1BsYXlS…` | high |
| **CRITICAL** | Square Access Token | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EAAA5BAB7AkAAAbCVDAAMCbD2CiA8gNIBcPAMBAgTYAeC8AFgD…` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `9A04F079-9840-4286-AB92-E65BE0885F95` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `29701FE4-3CC7-4A34-8C5B-AE90C7439A47` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `EDEF8BA9-79D6-4ACE-A3C8-27DCD51D21ED` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `4E657466-6C69-7850-6966-665374726D21` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `4E657466-6C69-7848-6165-6465722E7632` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `A2394F52-5A9B-4F14-A244-6C427C648DF4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `4E657466-6C69-7846-7261-6D6552617465` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `8974DBCE-7BE7-4C51-84F9-7148F9882554` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `10000000-1000-4000-8000-100000000000` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `6674654e-696c-5078-6966-665374726d21` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `6674654e-696c-4878-6165-6465722e7632` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `6674654e-696c-5078-6966-66496e646578` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `6674654e-696c-4d78-6f6f-6653697a6573` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `6674654e-696c-5378-6565-6b506f696e74` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `cedb7489-e77b-514c-84f9-7148f9882554` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `524f39a2-9b5a-144f-a244-6c427c648df4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `6674654e-696c-4678-7261-6d6552617465` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `password"):` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `password:C}},{}).then(function(){})}function` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `Pwd:F(J,"historyTimeOfDayGranularity",` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `password=Y.password\|\|""):V&&(ea.useNetflixUserAuth…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `PWD1zjew2PjoGEwJYlKbSbHVcUNygplaGmPkUCBThDh7p/5Lx5…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `password=n;return` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `password",q.password);return` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `password==m.password:!1};return` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `password");return` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `PASSWORD"),mrd:new` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/player/html/ffe/cadmium-playercore-6.0060.258.911.js` | `pwd=function(l,m){return` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `6lFhp8ueK-yEX8RZy8dDrm3umniOWOC1g7_6Zqxe` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `6l47DEFUBt_kVBgqk5U2KPXDkBPRvpfC_IfDq3xm` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `6LmQXAMPK6bqCb-kjkt_7bt3Y--ZQ09B3WphZcmg` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `6l1bhVZC_i8Pc__V9jkAF_TNEeGyFm0yBIw4LW-F` | medium |
| **HIGH** | Basic Auth Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `basic-selector` | high |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiErrorCloud` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiEndCloud` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiEndKids` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiErrorKids` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiEndMobile` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiErrorMobile` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiEndController` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiErrorController` | medium |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AccordionSpaceBetweenHeadlinePanel` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `acyDataAnyIndividualAssentDocument` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `acyAndDataSettingsSharedResponseFr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `accountOrCpfInSystemDeferredCancel` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACTION_ADDON_SETUP_NO_PROFILE_TRAN` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACTION_CREATE_ACCOUNT_PROFILE_TRAN` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACTION_ADDON_SETUP_LOGIN_CREDENTIA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACTION_ADD_ON_CLAIM_REGISTRATION_A` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AccordionSpaceBetweenHeadlineIconT` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `acmtxvYeUx-PlJjeGBGhMlxWp7OUdj0Btc` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `aCBr2JEHfTJK011YH68g00wymeT60puFw0` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Acm6QHeUWv7ScDvnr9a-IkVKMlmzKegmoo` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACYO9mWzCyHtB3l3x5Frk30s3yyTathzM9` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AcD4N1RQAEK3Zf_5cprTV4caZvILjLu9Fp` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACWXApiNnH4XAPwC_hgvLaxqL-ArajlvI-` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACuym_G7RjVOeaMDIF-HEans5mYFiqbzJs` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AcU1QC7qr71VNCQ3a0OWlyfRi661n_9i7R` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `acGPXhqYvTS3pLoN2OaRmnXS8rOUZYqEwN` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AC32JPFGdpEn9OE99Z3tfEDcY9p1sxTOsz` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AchxkB_5wK80bgwuVFpjc6a0_txXdrZds_` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACQCAYAAADnRuK4AAAAAXNSR0IArs4c6QA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACXCCwABHjxQFMaafgeAvRGtDxuiw2q1Go` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Ac7FQ6GB2yjWeV2fJsBGZRCjS06meBpCHv` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `acZMZ0nftSAXEIwAT1wWcBIKqchly2T3Nr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACwkql8qBcLneq1ep2pVLp1Gq1zfPz8x29` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ACBW67al9AZAABAONO682Go0OQGo2m1sRO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemBorderFocusedOutline` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemForegroundDescriptio` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemForegroundMessageErr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemBorderRadiusFocusedO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemBorderWidthFocusedOu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemSpaceBetweenTextSmal` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemSpaceBetweenValidati` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemSpaceHorizontalMediu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemSpaceHorizontalSmall` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemSpaceValidationIconV` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceDuotoneBott` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceDuotoneLeft` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceDuotoneRigh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceDuotoneSwap` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceDuotoneTopL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceDuotoneTopR` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceMonotoneBot` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceMonotoneLef` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceMonotoneRig` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceMonotoneSwa` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceMonotoneTop` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceNeutralBott` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceNeutralLeft` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceNeutralRigh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceNeutralTopL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ackgroundTextureSurfaceNeutralTopR` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemTextDescriptionMediu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ActionListItemTextDescriptionSmall` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Achievement_AchievementLockedError` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Achievement_UnknownAchievementErro` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Achievement_ArchivedAchievementErr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `acy_PlayerToBeBlockedNotFoundError` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `acterAppIconWithTrailerEntityTreat` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AccessibilityEmptySectionTreatment` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Acvq-FaCNg-n4JbHA_0Rfuwq0c_YlUz1kn` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AcljwhfBi0JNlAJX1y0scEhX1dpuTfGnLD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AcWJc52qhzDr11uHhwV67876anVnzfhCFn` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AcmWkmWiOl-IZby7vT-hpmH4lVXyZHe6yA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `aC4a78HmYJR2mxL1FocW2KeBIS2mlilOgh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `activeConcurrentSessionCountByType` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `activeConcurrentContextCountByType` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `accountNavigationConsolidationEnab` | high |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `apperPropsGrowthAccountFragmentDoc` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `APDPuS_gXyPzToHtCtL2naytGMEfooqszy` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Aplws5Mz2ZyquQhssTwvtX0mf10eVMJMSI` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApDfJhmDDgZajAVeVYfmtChdX1Bv1WjqWV` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ap_oxLuhm1LiV7ip-ocMqRFiwXYp58PH8j` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApiNnH4XAPwC_hgvLaxqL-ArajlvI-bqdp` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `aPngZQIgjp_fhxHeTd7SjLtSocEaNaEpgV` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `aPn4HPN4QwilpNnz9kDpfzCO9bIfgz0wJ9` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ApYt0MOA2qMXHVQdFbEF3WPSLqPpe4EG2a` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `aPY_sDjavu82TriL1rYeC7rvJSEum65Sl0` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `APy4XJDiHR6gNYhv2ifUY7OBZ5JhTGCPhR` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Ap2A5TmWYprONTdddnkgzsrgMLG79LHgKD` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `APTqTNUi4wwPdDdafVHavQhbzMba9Xp9q1` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `APwiVemKgG5cEPVYhA0VvZOdZx193POh8r` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Ap1arbVerVazvRFejhmGMEEG58hbKCoAu3` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `AppIconCrossContentEntityTreatment` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `aptionedStandardBoxshotEntityTreat` | medium |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `cc17bcbc-6211-49b8-8a84-576f0916707a` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `8d985f07-2117-4add-980c-b83895549d1c` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `11403da1-d6fd-4cd7-9ad7-892554b70047` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `a5e82016-e05b-4704-b294-276399a300ec` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `d43e296a-cada-4621-95ad-1cebb05dac53` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ad34d96b-44ec-4934-87f0-71a4656f3314` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `968dc303-dede-46b1-8561-712f7510b2bc` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `bdb05997-238a-4d88-9390-0860b5de1979` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `573bcc5d-b976-4302-8b57-c3f99479532d` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `55685474-d9f8-4b55-abb0-2a15776942f6` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `c6a61b41-db7d-4e62-8daf-bf95567649d4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `c32a2088-2d0a-4171-ba16-e7d6b29368eb` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `5e197520-4947-40d0-aad8-2e3c3d8f5126` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `9f961899-4cc0-4f3b-af57-11c10f17fe7b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `babf907e-fb1f-4064-985c-f0b4b3d1040b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `f490f470-b47c-4788-98e0-b13dac06f611` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `d1528f2f-ed01-4dc1-b870-ee91bb2c3850` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `aba9d655-78c6-4ac1-9972-7d20807ae0db` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `979e5a0f-d529-451a-bcca-b40d020bff49` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `ada67a22-b4f8-491a-a03c-2a6a4c4bba7d` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `3ba26cf5-ac12-41b6-a46f-71636e95c7b0` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `7914a465-77c8-4f83-a1f7-74143e7ab44c` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `8e8c3ad1-e864-4903-976f-ed39769164b8` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `7a59e969-591c-40dc-829c-05ab9addf3b0` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `75fa2481-4150-4b58-be85-7b9fc12a18c2` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `abc705bf-9058-4359-a481-2c4361031cfe` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `8509c4ac-8d9a-4d76-830f-0ac50334ceef` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `f887aee9-99d4-4dd0-9a3f-1165a881d115` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `40fdbbd2-af28-4962-bb30-e0025648e2de` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `b22dfce1-c3fb-44e7-843d-2ee408bbc434` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `079b2271-196b-4edd-b65c-e9439b22e305` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `8c2a5567-3772-4c87-b366-217feab3fc60` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `b4a5ebd3-5bba-4598-9c93-fb38f396ff3a` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `2187feea-8ac0-4675-8bda-b0f6adf1b0b4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `9dbc81f5-2724-4e4d-979e-1d333e580ce1` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `d3f262c0-b1bc-4c24-ac10-d162637b4f07` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `fd8fc53e-3cb9-49eb-ba9d-5fe71a883bb4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `d7814c36-d08b-4656-b491-26e5c8564cde` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `511a758b-100a-4742-8c87-e0f07ef44b91` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `e3746bf7-d066-40e0-a00f-9f9eec5d01f7` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `08436c22-508e-4c94-b43e-885054b5654a` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `974eaa5b-8a26-4c15-810b-500c257f27a2` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `af50e276-c340-4aef-96cd-8bf18ce97480` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `972b874e-5dae-48cc-a101-6c357403ee2b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `c0134b54-33a2-4965-b0c3-ea6b5a631450` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `dfc43a9a-2ef3-45d2-b27d-214e52fc10ce` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `93ad8739-c910-4ce1-a34b-630752e10a17` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `f6716e37-8e38-4a8a-88b0-4c2ed89e2234` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `1e3117f3-64f2-4006-9bda-38b9de1c8dea` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `e9be6db8-50e7-40da-8b6a-946c692c9760` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password":return(0,p.jsx)(s.default,l({type:"passw…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:(0,o.createRoute)({path:"/password"}),ver…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD=n.ACTION_ENTER_PASSWORD=n.ACTION_EDIT_PAY…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD="createPasswordAction",n.ACTION_ENTER_PAS…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password"}),s=(0,a.default)("",{bundleOverride:"si…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password"}),P=(0,d.default)("",{bundleOverride:"si…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:{displayIndex:0,type:"password",name:"pas…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password"]),H="WithContext",W="Context",z="learnMo…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password"===window.location.pathname?window.locati…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:(0,a.default)("",{bundleOverride:"signup/…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password",name:"password",required:!0,fieldType:"S…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:{autoComplete:"new-password",displayIndex…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:{autoComplete:"new-password",displayIndex…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:f.label_your_password)},type:"password",n…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD=n.INPUT_KIND_NAME=n.INPUT_KIND_LAST_NAME=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD="password",n.INPUT_KIND_GIFT_CODE="giftCa…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:(0,a.default)("",{bundleOverride:"signup/…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD:b.ACTION_SEND_LINK}))),h.MONEYBALL_FLOWS.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD=n.ACTION_CREATE_ACCOUNT_PROFILE_TRANSFER=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD="forgotPasswordAction",n.ACTION_RESEND_VE…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:(0,a.default)("",{bundleOverride:"signup/…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:{autoComplete:"new-password",displayIndex…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password";return` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:(0,a.default)("",{bundleOverride:"account…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:(0,a.default)("",{bundleOverride:"signup/…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:{displayIndex:1,type:"password",name:"pas…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password"},forgotPasswordLink:{fieldPath:"messages…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password"===r.type)\|\|"textarea"===n\|\|"true"===r.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password:null,hostname:null,urn:null,port:null,pat…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password=i[0]?u.decode(i.join(":")):null,r=o.subst…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password=_("password"),s.hostname=_("hostname"),s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password","hostname","port"];if(this._parts.urn)th…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password::-webkit-textfield-decoration-container")…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD:"changePassword",PASSWORD_ONLY:"passwordO…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `Password:"editMemberPassword",editPayment:"editPay…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD":return"current-password";case"NEW_PASSWO…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `PASSWORD":return"password";case"TELEPHONE":return"…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password"===P?L.replace(/./g,""):L).split("").reve…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password":"text","-").concat(i)),description:null=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password",onFocus:A,validation:I,title:null!=(a=nu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password",width:"full",localDesign:dI})),b&&(0,tB.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/clcs/login/client.fa3ac2b0442bf8f95d07.js` | `password",value:r},n===Math.min(et,B)&&{"data-curr…` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `6lFhp8ueK-yEX8RZy8dDrm3umniOWOC1g7_6Zqxe` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `6LmQXAMPK6bqCb-kjkt_7bt3Y--ZQ09B3WphZcmg` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `6lsGnX1PPwuWrDlLN1WpwYh6hno8EYvz-5LtBEMY` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `6lDtc4r7gtvj0dSLcSa-MLi7-qbB7tQ5z7j6dxDJ` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `6L-OVu4X1UNqFl8DURdvPWsTlNK6vqJ8WQ0Ztacc` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `6L2QjRy1BZbkuTNPM7F3CvwMBWpJmS7--8nnoTKe` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `6l1bhVZC_i8Pc__V9jkAF_TNEeGyFm0yBIw4LW-F` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `APIEndpoint` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiErrorCloud` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiEndCloud` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiEndKids` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiErrorKids` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiEndMobile` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiErrorMobile` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiEndController` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiErrorController` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `API already` | medium |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `acyDataAnyIndividualAssentDocument` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `acyAndDataSettingsSharedResponseFr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `accountOrCpfInSystemDeferredCancel` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACTION_CREATE_ACCOUNT_PROFILE_TRAN` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACTION_ADD_ON_CLAIM_REGISTRATION_A` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACTION_ADDON_SETUP_NO_PROFILE_TRAN` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACTION_ADDON_SETUP_LOGIN_CREDENTIA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AccordionSpaceBetweenHeadlinePanel` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `acmtxvYeUx-PlJjeGBGhMlxWp7OUdj0Btc` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `aCBr2JEHfTJK011YH68g00wymeT60puFw0` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Acx-GqqC3JCLMCKSs7slxgWHTdDTGT_dU6` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACowo4AbM30Hcr5sab8i9X3gx-f8Nv2fjy` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `aCrYSbuttRtA5OJoQQ-_fsmeJNay16_swM` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `aCDJdql1filYyjnMStSgF5vx6rXe0-0VNn` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Ac8xQkjIJFTE6GscTCIh-hpggY-BzGGEVC` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACsCUOEYBu-2BXJ3xXj6382UvRgbzQWAAu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `accEHHOGWJkEHufWMkxPu6TzXMiv6-m-4h` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Ac8NW3XJufF0OumYKpfdFgZiWm1yHurz3Q` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ac1c07PtNij9BJMJs0hSQ_Ja4qGXSvG6NK` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AcVs6DgRunDQRi-F-CEblXGIiAPBHsROTD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACL4v9wL28aglagE6Zau5laei623iobFXQ` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `acqXygH31d5ldFt5yVz99BFTZwdBLjximO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AcUaII67eD1UkauYtFcgLzUING0HQkCNMG` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AcD4N1RQAEK3Zf_5cprTV4caZvILjLu9Fp` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACWXApiNnH4XAPwC_hgvLaxqL-ArajlvI-` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AcU1QC7qr71VNCQ3a0OWlyfRi661n_9i7R` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `acGPXhqYvTS3pLoN2OaRmnXS8rOUZYqEwN` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AC32JPFGdpEn9OE99Z3tfEDcY9p1sxTOsz` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AchxkB_5wK80bgwuVFpjc6a0_txXdrZds_` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACQCAYAAADnRuK4AAAAAXNSR0IArs4c6QA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACXCCwABHjxQFMaafgeAvRGtDxuiw2q1Go` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Ac7FQ6GB2yjWeV2fJsBGZRCjS06meBpCHv` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `acZMZ0nftSAXEIwAT1wWcBIKqchly2T3Nr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACwkql8qBcLneq1ep2pVLp1Gq1zfPz8x29` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ACBW67al9AZAABAONO682Go0OQGo2m1sRO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemBorderFocusedOutline` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemForegroundDescriptio` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemForegroundMessageErr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AccordionSpaceBetweenHeadlineIconT` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemBorderRadiusFocusedO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemBorderWidthFocusedOu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemSpaceBetweenTextSmal` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemSpaceBetweenValidati` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemSpaceHorizontalMediu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemSpaceHorizontalSmall` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemSpaceValidationIconV` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceDuotoneBott` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceDuotoneLeft` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceDuotoneRigh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceDuotoneSwap` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceDuotoneTopL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceDuotoneTopR` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceMonotoneBot` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceMonotoneLef` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceMonotoneRig` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceMonotoneSwa` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceMonotoneTop` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceNeutralBott` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceNeutralLeft` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceNeutralRigh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceNeutralTopL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ackgroundTextureSurfaceNeutralTopR` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemTextDescriptionMediu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ActionListItemTextDescriptionSmall` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `activeConcurrentSessionCountByType` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `activeConcurrentContextCountByType` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Achievement_AchievementLockedError` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Achievement_UnknownAchievementErro` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Achievement_ArchivedAchievementErr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `acy_PlayerToBeBlockedNotFoundError` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `acterAppIconWithTrailerEntityTreat` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AccessibilityEmptySectionTreatment` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `accountNavigationConsolidationEnab` | high |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `apperPropsGrowthAccountFragmentDoc` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AppCanHandlePageVideoContainerEvid` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AProblemDialog--completion-contain` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AProblemDialog--message-fieldset-v` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AProblemDialog--checkbox-label-def` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AProblemDialog--checkbox-container` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AProblemDialog--details-question-o` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AProblemDialog--confirmation-title` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AProblemDialog--confirmation-subte` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Aplws5Mz2ZyquQhssTwvtX0mf10eVMJMSI` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApDfJhmDDgZajAVeVYfmtChdX1Bv1WjqWV` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ap_oxLuhm1LiV7ip-ocMqRFiwXYp58PH8j` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `apNHaaZYLvB3KWuMtW3-AMV6mXMEIrSMj8` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AP1a447ZPmRE6n-jt7d4b_rip24zLQAq9g` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `apgBoKDnKlTPsWIs6qgy6EYCu8ih6sbmsY` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApCcPDJ2r_5r5Uhun5TPOiFjBYnB3d2WWh` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `APBHsROTDRcgi5iKZo5GAYIWPKhJ3Sf8iT` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `apDaT5PEkG2-4mL5sz-wBcNbt1RJmG0uGZ` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `apOx6SBHnPuo729aKY4o0NkM6bxVrR6TWM` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `APBvsh8XqMDmnvk2bkq7CToKoMRPCkS6oG` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApiNnH4XAPwC_hgvLaxqL-ArajlvI-bqdp` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `aPn4HPN4QwilpNnz9kDpfzCO9bIfgz0wJ9` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ApYt0MOA2qMXHVQdFbEF3WPSLqPpe4EG2a` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `aPY_sDjavu82TriL1rYeC7rvJSEum65Sl0` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `APy4XJDiHR6gNYhv2ifUY7OBZ5JhTGCPhR` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Ap2A5TmWYprONTdddnkgzsrgMLG79LHgKD` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `APTqTNUi4wwPdDdafVHavQhbzMba9Xp9q1` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `APwiVemKgG5cEPVYhA0VvZOdZx193POh8r` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Ap1arbVerVazvRFejhmGMEEG58hbKCoAu3` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `AppIconCrossContentEntityTreatment` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `aptionedStandardBoxshotEntityTreat` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `aP65zQypYPP7EDXn4ETOcwZqZqruxOnel0` | medium |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `8d985f07-2117-4add-980c-b83895549d1c` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `11403da1-d6fd-4cd7-9ad7-892554b70047` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `a5e82016-e05b-4704-b294-276399a300ec` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `d43e296a-cada-4621-95ad-1cebb05dac53` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ad34d96b-44ec-4934-87f0-71a4656f3314` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `968dc303-dede-46b1-8561-712f7510b2bc` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `9d86f317-bdd0-45ed-b7f9-539a2dadfda6` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `4a01a48c-ce94-42fc-9e27-8e152e5c2735` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `7445680b-ff11-4b44-ac1e-4ea45ca1269e` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `b4aae418-d151-485c-b10f-2d22cb895781` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `a82c00a2-978b-407a-8b3b-135323ad24d9` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `bdb05997-238a-4d88-9390-0860b5de1979` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `573bcc5d-b976-4302-8b57-c3f99479532d` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `55685474-d9f8-4b55-abb0-2a15776942f6` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `c6a61b41-db7d-4e62-8daf-bf95567649d4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `c32a2088-2d0a-4171-ba16-e7d6b29368eb` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `5e197520-4947-40d0-aad8-2e3c3d8f5126` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `9f961899-4cc0-4f3b-af57-11c10f17fe7b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `babf907e-fb1f-4064-985c-f0b4b3d1040b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `f490f470-b47c-4788-98e0-b13dac06f611` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `d1528f2f-ed01-4dc1-b870-ee91bb2c3850` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `aba9d655-78c6-4ac1-9972-7d20807ae0db` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `979e5a0f-d529-451a-bcca-b40d020bff49` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `ada67a22-b4f8-491a-a03c-2a6a4c4bba7d` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `3ba26cf5-ac12-41b6-a46f-71636e95c7b0` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `7914a465-77c8-4f83-a1f7-74143e7ab44c` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `8e8c3ad1-e864-4903-976f-ed39769164b8` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `7a59e969-591c-40dc-829c-05ab9addf3b0` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `75fa2481-4150-4b58-be85-7b9fc12a18c2` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `abc705bf-9058-4359-a481-2c4361031cfe` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `8509c4ac-8d9a-4d76-830f-0ac50334ceef` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `f887aee9-99d4-4dd0-9a3f-1165a881d115` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `0aec9bc3-54ba-448e-86e3-acaf9bcb5443` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `3d90ba47-efa5-433a-aa3a-4762261ef9b1` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `b368627b-a1a2-4ca0-affc-dcbb79912bfa` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `721a691f-480a-4d3a-a303-1db6836a40d7` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `0e872f21-7ba3-408d-aa5e-e226d0e5aafa` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `9d59c3d8-7dc2-4edf-98ea-25fd1d007788` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `a5e09e1a-789b-469d-acd6-00eb341e98d5` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `536f85e0-03b3-45de-a27a-5983f562750b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `217277fd-12a1-4816-a5b2-b9d7b9afd4ea` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `4c02d217-f945-42f5-b37c-207df5d1384f` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `a4cb6adb-fa6d-4f8d-bbfb-d86ccfebebdf` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `28635a91-01d2-4bf5-9dee-3f7b989d36c5` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `01d14612-7911-4a70-a3ce-9f1561f857fe` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `4c249a85-1554-4f5b-a535-d1c3c331298c` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `67ff079f-1c4c-404d-96c4-73c0fe8930cd` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `b22dfce1-c3fb-44e7-843d-2ee408bbc434` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `079b2271-196b-4edd-b65c-e9439b22e305` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `8c2a5567-3772-4c87-b366-217feab3fc60` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `b4a5ebd3-5bba-4598-9c93-fb38f396ff3a` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `2187feea-8ac0-4675-8bda-b0f6adf1b0b4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `9dbc81f5-2724-4e4d-979e-1d333e580ce1` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `d3f262c0-b1bc-4c24-ac10-d162637b4f07` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `fd8fc53e-3cb9-49eb-ba9d-5fe71a883bb4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `d7814c36-d08b-4656-b491-26e5c8564cde` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `511a758b-100a-4742-8c87-e0f07ef44b91` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `e3746bf7-d066-40e0-a00f-9f9eec5d01f7` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `08436c22-508e-4c94-b43e-885054b5654a` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `974eaa5b-8a26-4c15-810b-500c257f27a2` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `af50e276-c340-4aef-96cd-8bf18ce97480` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `972b874e-5dae-48cc-a101-6c357403ee2b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `c0134b54-33a2-4965-b0c3-ea6b5a631450` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `dfc43a9a-2ef3-45d2-b27d-214e52fc10ce` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `93ad8739-c910-4ce1-a34b-630752e10a17` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `f6716e37-8e38-4a8a-88b0-4c2ed89e2234` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `1e3117f3-64f2-4006-9bda-38b9de1c8dea` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `e9be6db8-50e7-40da-8b6a-946c692c9760` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password:(0,i.createRoute)({path:"/password"}),ver…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `PASSWORD=t.INPUT_KIND_NAME=t.INPUT_KIND_LAST_NAME=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `PASSWORD="password",t.INPUT_KIND_GIFT_CODE="giftCa…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `PASSWORD=t.ACTION_CREATE_ACCOUNT_PROFILE_TRANSFER=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `PASSWORD="forgotPasswordAction",t.ACTION_RESEND_VE…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password:!0,number:!0,date:!0,month:!0,week:!0,tim…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password:null,hostname:null,urn:null,port:null,pat…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password=n[0]?o.decode(n.join(":")):null,e=i.subst…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password=S("password"),l.hostname=S("hostname"),l.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password","hostname","port"];if(this._parts.urn)th…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `password::-webkit-textfield-decoration-container")…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `PASSWORD:"changePassword",PASSWORD_ONLY:"passwordO…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmContent/nmTitle/nmTitleComposedClient.ae1503b528ea1ef45b3f.js` | `Password:"editMemberPassword",editPayment:"editPay…` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `6lFhp8ueK-yEX8RZy8dDrm3umniOWOC1g7_6Zqxe` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `6l1bhVZC_i8Pc__V9jkAF_TNEeGyFm0yBIw4LW-F` | medium |
| **HIGH** | Basic Auth Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `basicLayout:` | high |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApiErrorCloud` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApiEndCloud` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApiEndKids` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApiErrorKids` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApiEndMobile` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApiErrorMobile` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApiEndController` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApiErrorController` | medium |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `acyDataAnyIndividualAssentDocument` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `acyAndDataSettingsSharedResponseFr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `accountOrCpfInSystemDeferredCancel` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `AccordionSpaceBetweenHeadlineIconT` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `AccordionSpaceBetweenHeadlinePanel` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `acmtxvYeUx-PlJjeGBGhMlxWp7OUdj0Btc` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `aCBr2JEHfTJK011YH68g00wymeT60puFw0` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `AcU1QC7qr71VNCQ3a0OWlyfRi661n_9i7R` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `acGPXhqYvTS3pLoN2OaRmnXS8rOUZYqEwN` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `AC32JPFGdpEn9OE99Z3tfEDcY9p1sxTOsz` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `AchxkB_5wK80bgwuVFpjc6a0_txXdrZds_` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ACQCAYAAADnRuK4AAAAAXNSR0IArs4c6QA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ACXCCwABHjxQFMaafgeAvRGtDxuiw2q1Go` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `Ac7FQ6GB2yjWeV2fJsBGZRCjS06meBpCHv` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `acZMZ0nftSAXEIwAT1wWcBIKqchly2T3Nr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ACwkql8qBcLneq1ep2pVLp1Gq1zfPz8x29` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ACBW67al9AZAABAONO682Go0OQGo2m1sRO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemBorderFocusedOutline` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemForegroundDescriptio` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemForegroundMessageErr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemBorderRadiusFocusedO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemBorderWidthFocusedOu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemSpaceBetweenTextSmal` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemSpaceBetweenValidati` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemSpaceHorizontalMediu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemSpaceHorizontalSmall` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemSpaceValidationIconV` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceDuotoneBott` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceDuotoneLeft` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceDuotoneRigh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceDuotoneSwap` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceDuotoneTopL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceDuotoneTopR` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceMonotoneBot` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceMonotoneLef` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceMonotoneRig` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceMonotoneSwa` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceMonotoneTop` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceNeutralBott` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceNeutralLeft` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceNeutralRigh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceNeutralTopL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ackgroundTextureSurfaceNeutralTopR` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemTextDescriptionMediu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ActionListItemTextDescriptionSmall` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `activeConcurrentSessionCountByType` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `activeConcurrentContextCountByType` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `Achievement_AchievementLockedError` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `Achievement_UnknownAchievementErro` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `Achievement_ArchivedAchievementErr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `acy_PlayerToBeBlockedNotFoundError` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `acterAppIconWithTrailerEntityTreat` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `AccessibilityEmptySectionTreatment` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `accountNavigationConsolidationEnab` | high |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `apperPropsGrowthAccountFragmentDoc` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `AppCanHandlePageVideoContainerEvid` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `APDPuS_gXyPzToHtCtL2naytGMEfooqszy` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `Aplws5Mz2ZyquQhssTwvtX0mf10eVMJMSI` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApDfJhmDDgZajAVeVYfmtChdX1Bv1WjqWV` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `aPn4HPN4QwilpNnz9kDpfzCO9bIfgz0wJ9` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ApYt0MOA2qMXHVQdFbEF3WPSLqPpe4EG2a` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `aPY_sDjavu82TriL1rYeC7rvJSEum65Sl0` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `APy4XJDiHR6gNYhv2ifUY7OBZ5JhTGCPhR` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `Ap2A5TmWYprONTdddnkgzsrgMLG79LHgKD` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `APTqTNUi4wwPdDdafVHavQhbzMba9Xp9q1` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `APwiVemKgG5cEPVYhA0VvZOdZx193POh8r` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `Ap1arbVerVazvRFejhmGMEEG58hbKCoAu3` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `AppIconCrossContentEntityTreatment` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `aptionedStandardBoxshotEntityTreat` | medium |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `8d985f07-2117-4add-980c-b83895549d1c` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `11403da1-d6fd-4cd7-9ad7-892554b70047` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `a5e82016-e05b-4704-b294-276399a300ec` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `d43e296a-cada-4621-95ad-1cebb05dac53` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ad34d96b-44ec-4934-87f0-71a4656f3314` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `968dc303-dede-46b1-8561-712f7510b2bc` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `9f9e3f46-ae32-468e-850d-64719466ab16` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `0a7af6bd-e473-430f-b2f2-4ada1c9e6dfb` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `3f50f3b3-fff8-48c0-bbd3-5fa2cb04b3c1` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `bdb05997-238a-4d88-9390-0860b5de1979` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `573bcc5d-b976-4302-8b57-c3f99479532d` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `55685474-d9f8-4b55-abb0-2a15776942f6` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `c6a61b41-db7d-4e62-8daf-bf95567649d4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `c32a2088-2d0a-4171-ba16-e7d6b29368eb` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `5e197520-4947-40d0-aad8-2e3c3d8f5126` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `9f961899-4cc0-4f3b-af57-11c10f17fe7b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `babf907e-fb1f-4064-985c-f0b4b3d1040b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `f490f470-b47c-4788-98e0-b13dac06f611` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `d1528f2f-ed01-4dc1-b870-ee91bb2c3850` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `aba9d655-78c6-4ac1-9972-7d20807ae0db` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `979e5a0f-d529-451a-bcca-b40d020bff49` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `ada67a22-b4f8-491a-a03c-2a6a4c4bba7d` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `3ba26cf5-ac12-41b6-a46f-71636e95c7b0` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `7914a465-77c8-4f83-a1f7-74143e7ab44c` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `8e8c3ad1-e864-4903-976f-ed39769164b8` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `7a59e969-591c-40dc-829c-05ab9addf3b0` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `75fa2481-4150-4b58-be85-7b9fc12a18c2` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `abc705bf-9058-4359-a481-2c4361031cfe` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `8509c4ac-8d9a-4d76-830f-0ac50334ceef` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `f887aee9-99d4-4dd0-9a3f-1165a881d115` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `0aec9bc3-54ba-448e-86e3-acaf9bcb5443` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `3d90ba47-efa5-433a-aa3a-4762261ef9b1` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `b368627b-a1a2-4ca0-affc-dcbb79912bfa` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `721a691f-480a-4d3a-a303-1db6836a40d7` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `0e872f21-7ba3-408d-aa5e-e226d0e5aafa` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `9d59c3d8-7dc2-4edf-98ea-25fd1d007788` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `a5e09e1a-789b-469d-acd6-00eb341e98d5` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `536f85e0-03b3-45de-a27a-5983f562750b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `217277fd-12a1-4816-a5b2-b9d7b9afd4ea` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `4c02d217-f945-42f5-b37c-207df5d1384f` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `a4cb6adb-fa6d-4f8d-bbfb-d86ccfebebdf` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `28635a91-01d2-4bf5-9dee-3f7b989d36c5` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `01d14612-7911-4a70-a3ce-9f1561f857fe` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `4c249a85-1554-4f5b-a535-d1c3c331298c` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `67ff079f-1c4c-404d-96c4-73c0fe8930cd` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `b22dfce1-c3fb-44e7-843d-2ee408bbc434` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `079b2271-196b-4edd-b65c-e9439b22e305` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `8c2a5567-3772-4c87-b366-217feab3fc60` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `b4a5ebd3-5bba-4598-9c93-fb38f396ff3a` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `2187feea-8ac0-4675-8bda-b0f6adf1b0b4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `9dbc81f5-2724-4e4d-979e-1d333e580ce1` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `d3f262c0-b1bc-4c24-ac10-d162637b4f07` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `fd8fc53e-3cb9-49eb-ba9d-5fe71a883bb4` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `d7814c36-d08b-4656-b491-26e5c8564cde` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `511a758b-100a-4742-8c87-e0f07ef44b91` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `e3746bf7-d066-40e0-a00f-9f9eec5d01f7` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `08436c22-508e-4c94-b43e-885054b5654a` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `974eaa5b-8a26-4c15-810b-500c257f27a2` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `af50e276-c340-4aef-96cd-8bf18ce97480` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `972b874e-5dae-48cc-a101-6c357403ee2b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `c0134b54-33a2-4965-b0c3-ea6b5a631450` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `dfc43a9a-2ef3-45d2-b27d-214e52fc10ce` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `93ad8739-c910-4ce1-a34b-630752e10a17` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `f6716e37-8e38-4a8a-88b0-4c2ed89e2234` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `1e3117f3-64f2-4006-9bda-38b9de1c8dea` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `e9be6db8-50e7-40da-8b6a-946c692c9760` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password:(0,i.createRoute)({path:"/password"}),ver…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password:{displayIndex:1,type:"password",name:"pas…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `PASSWORD=t.INPUT_KIND_NAME=t.INPUT_KIND_LAST_NAME=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `PASSWORD="password",t.INPUT_KIND_GIFT_CODE="giftCa…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password:null,hostname:null,urn:null,port:null,pat…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password=n[0]?o.decode(n.join(":")):null,e=i.subst…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password=S("password"),l.hostname=S("hostname"),l.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password","hostname","port"];if(this._parts.urn)th…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `password::-webkit-textfield-decoration-container")…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `PASSWORD:"changePassword",PASSWORD_ONLY:"passwordO…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/landingPages/nmhp/nmhpFrameworkClient.fb984a62c6866e8f5146.js` | `Password:"editMemberPassword",editPayment:"editPay…` | medium |
| **LOW** | Google Captcha Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `6l1bhVZC_i8Pc__V9jkAF_TNEeGyFm0yBIw4LW-F` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `API error` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `api_version` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApiErrorCloud` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApiEndCloud` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApiEndKids` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApiErrorKids` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApiEndMobile` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApiErrorMobile` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApiEndController` | medium |
| **HIGH** | API Token / Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApiErrorController` | medium |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundItemEntityFieldsFragmentD` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `Acm6QHeUWv7ScDvnr9a-IkVKMlmzKegmoo` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ACYO9mWzCyHtB3l3x5Frk30s3yyTathzM9` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `AcWJc52qhzDr11uHhwV67876anVnzfhCFn` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `AcmWkmWiOl-IZby7vT-hpmH4lVXyZHe6yA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `AcU1QC7qr71VNCQ3a0OWlyfRi661n_9i7R` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `acGPXhqYvTS3pLoN2OaRmnXS8rOUZYqEwN` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `AC32JPFGdpEn9OE99Z3tfEDcY9p1sxTOsz` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `AchxkB_5wK80bgwuVFpjc6a0_txXdrZds_` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ACQCAYAAADnRuK4AAAAAXNSR0IArs4c6QA` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ACXCCwABHjxQFMaafgeAvRGtDxuiw2q1Go` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `Ac7FQ6GB2yjWeV2fJsBGZRCjS06meBpCHv` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `acZMZ0nftSAXEIwAT1wWcBIKqchly2T3Nr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ACwkql8qBcLneq1ep2pVLp1Gq1zfPz8x29` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ACBW67al9AZAABAONO682Go0OQGo2m1sRO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemBorderFocusedOutline` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemForegroundDescriptio` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemForegroundMessageErr` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `AccordionSpaceBetweenHeadlineIconT` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `AccordionSpaceBetweenHeadlinePanel` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemBorderRadiusFocusedO` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemBorderWidthFocusedOu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemSpaceBetweenTextSmal` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemSpaceBetweenValidati` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemSpaceHorizontalMediu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemSpaceHorizontalSmall` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemSpaceValidationIconV` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceDuotoneBott` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceDuotoneLeft` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceDuotoneRigh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceDuotoneSwap` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceDuotoneTopL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceDuotoneTopR` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceMonotoneBot` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceMonotoneLef` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceMonotoneRig` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceMonotoneSwa` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceMonotoneTop` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceNeutralBott` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceNeutralLeft` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceNeutralRigh` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceNeutralTopL` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ackgroundTextureSurfaceNeutralTopR` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemTextDescriptionMediu` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ActionListItemTextDescriptionSmall` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `activeConcurrentSessionCountByType` | high |
| **HIGH** | Twilio Account SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `activeConcurrentContextCountByType` | high |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `aPn4HPN4QwilpNnz9kDpfzCO9bIfgz0wJ9` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ApYt0MOA2qMXHVQdFbEF3WPSLqPpe4EG2a` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `aPY_sDjavu82TriL1rYeC7rvJSEum65Sl0` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `APy4XJDiHR6gNYhv2ifUY7OBZ5JhTGCPhR` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `Ap2A5TmWYprONTdddnkgzsrgMLG79LHgKD` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `APTqTNUi4wwPdDdafVHavQhbzMba9Xp9q1` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `APwiVemKgG5cEPVYhA0VvZOdZx193POh8r` | medium |
| **MEDIUM** | Twilio App SID | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `Ap1arbVerVazvRFejhmGMEEG58hbKCoAu3` | medium |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `047c9e7a-c32d-4078-904a-884298e58227` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `2f58ae16-df79-431a-9ac7-f197c9e69877` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `10f2cb92-8fb7-442a-8ccb-fac13356cc90` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `c39b0cfd-2e12-4114-b94e-7c27ac29b7e5` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `a3e1627c-9e43-4e46-9e82-11c2e69758e2` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `2547a476-e0da-4beb-a8e6-2b7260edd9d5` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `3adb29c3-74da-49d4-86b3-1e604e0f1f21` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `c25956c7-81f3-4494-9e55-b7242cafba40` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `17a5712e-7a8d-4390-84ae-d7eeb9f325c0` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `2a4a5a77-5997-43ff-b643-1745c456b696` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `ffe50a99-3bc2-4175-a697-fdd31da9e124` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `79841625-26bb-4899-80ee-63b2e1c36b23` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `592260c9-ef04-4ae6-bec7-ae2d47498f9b` | high |
| **CRITICAL** | Heroku API Key | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `87b6a5c0-0104-4e96-a291-092c11350111` | high |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `PwdrR"}),r.SITE_NAV_SHOWS=(0,o.default)("",{bundle…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `password:!0,number:!0,date:!0,month:!0,week:!0,tim…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `password"===n.type)\|\|"textarea"===r\|\|"true"===n.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `password:null,hostname:null,urn:null,port:null,pat…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `password=i[0]?u.decode(i.join(":")):null,n=a.subst…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `password=_("password"),s.hostname=_("hostname"),s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `password","hostname","port"];if(this._parts.urn)th…` | medium |
| **HIGH** | Hardcoded Credentials | `https://assets.nflxext.com/web/ffe/wp/ui/pulseClient.56d3fd2ec39173fe11bd.js` | `password::-webkit-textfield-decoration-container")…` | medium |
| **HIGH** | Basic Auth Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `BasicHtmlNodes:` | high |
| **HIGH** | Basic Auth Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `BasicHtmlNodesFor:` | high |
| **HIGH** | Basic Auth Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `BasicHtmlNodes` | high |
| **HIGH** | Basic Auth Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `BasicHtmlNodesFor` | high |
| **HIGH** | Basic Auth Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `basicOptionalMinutes:/` | high |
| **HIGH** | Basic Auth Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `basicOptionalSeconds:/` | high |
| **HIGH** | Basic Auth Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `basicOptionalMinutes` | high |
| **HIGH** | Basic Auth Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `basicOptionalSeconds` | high |
| **HIGH** | API Token / Key | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `API compatible` | medium |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `ace-allownode-allowedtypes-and-dis` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `acter-after-doctype-system-identif` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `aceBetweenDoctypePublicAndSystemId` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `ace-between-doctype-public-and-sys` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `acter-reference-outside-unicode-ra` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-option--selec` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__navigation--years-` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-dropdown--scr` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-read-view--do` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-read-view--se` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-dropdown-cont` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-option--sele` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-read-view--d` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-read-view--s` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-dropdown-con` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-year-option-` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-year-dropdow` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-year-read-vi` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__day--keyboard-sele` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__day--in-selecting-` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__day--selecting-ran` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__day--outside-month` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__week-number--click` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__week-number--selec` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__week-number--keybo` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__week--keyboard-sel` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-text--disabl` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-text--select` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-text--keyboa` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-text--in-sel` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-text--in-ran` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month-text--range-` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__quarter-text--disa` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__quarter-text--sele` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__quarter-text--keyb` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__quarter-text--in-s` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__quarter-text--in-r` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__quarter-text--rang` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__month--selecting-r` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__time-list-item--se` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__time-list-item--di` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__time-list-item--in` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__time-container--wi` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__header--time--only` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-text--selecte` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-text--disable` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-text--keyboar` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-text--range-s` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-text--range-e` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-text--in-rang` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-text--in-sele` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year-text--selecti` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__year--selecting-ra` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__input-time-contain` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker-time__input-contain` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__navigation--previo` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__navigation-icon--p` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__navigation--next--` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__navigation-icon--n` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__current-month--has` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__header--has-time-s` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__header__dropdown--` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__children-container` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker-ignore-onclickoutsi` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__close-icon--disabl` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `act-datepicker__view-calendar-icon` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `ACXBIWXMAAAsSAAALEgHS3X78AAAGvklEQ` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `AcRr7XZNBuzk16jgVskXRlUYozmeSfGJD9` | high |
| **HIGH** | Twilio Account SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `ACXBIWXMAAAsSAAALEgHS3X78AAAGpklEQ` | high |
| **MEDIUM** | Twilio App SID | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `APIl6rP07XmRCMJ2t6yAcRr7XZNBuzk16j` | medium |
| **HIGH** | Hardcoded Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://brand.netflix.com/assets/index-Da7LePZz.js` | `password")\|\|t==="textarea"\|\|e.contentEditable==="t…` | medium |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `act-autowhatever__items-container-` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `act-autowhatever__item--highlighte` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `act-autowhatever__section-containe` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `act-autosuggest__suggestions-conta` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `act-autosuggest__suggestion--first` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `act-autosuggest__suggestion--highl` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `act-autosuggest__section-container` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://help.nflxext.com/helpcenter/common_235de676caebb637148f.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemTextDescriptionSmall` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemTextDescriptionMediu` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemForegroundDescriptio` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemSpaceHorizontalSmall` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemSpaceHorizontalMediu` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemSpaceBetweenTextSmal` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemForegroundMessageErr` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemSpaceValidationIconV` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemSpaceBetweenValidati` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `aceBetweenContentDismissHorizontal` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ACQCAYAAADnRuK4AAAAAXNSR0IArs4c6QA` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ACXCCwABHjxQFMaafgeAvRGtDxuiw2q1Go` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `Ac7FQ6GB2yjWeV2fJsBGZRCjS06meBpCHv` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `acZMZ0nftSAXEIwAT1wWcBIKqchly2T3Nr` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ACwkql8qBcLneq1ep2pVLp1Gq1zfPz8x29` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ACBW67al9AZAABAONO682Go0OQGo2m1sRO` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemBorderFocusedOutline` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `AccordionSpaceBetweenHeadlineIconT` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `AccordionSpaceBetweenHeadlinePanel` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemBorderRadiusFocusedO` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ActionListItemBorderWidthFocusedOu` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceDuotoneBott` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceDuotoneLeft` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceDuotoneRigh` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceDuotoneSwap` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceDuotoneTopL` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceDuotoneTopR` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceMonotoneBot` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceMonotoneLef` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceMonotoneRig` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceMonotoneSwa` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceMonotoneTop` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceNeutralBott` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceNeutralLeft` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceNeutralRigh` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceNeutralTopL` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `ackgroundTextureSurfaceNeutralTopR` | high |
| **HIGH** | Twilio Account SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `act-async-component-lifecycle-hook` | high |
| **MEDIUM** | Twilio App SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `Ap2A5TmWYprONTdddnkgzsrgMLG79LHgKD` | medium |
| **MEDIUM** | Twilio App SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `APTqTNUi4wwPdDdafVHavQhbzMba9Xp9q1` | medium |
| **MEDIUM** | Twilio App SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `APwiVemKgG5cEPVYhA0VvZOdZx193POh8r` | medium |
| **MEDIUM** | Twilio App SID | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `Ap1arbVerVazvRFejhmGMEEG58hbKCoAu3` | medium |
| **HIGH** | Hardcoded Credentials | `https://help.nflxext.com/helpcenter/contact-us_5d586c820500c9465ec2.js` | `password::-webkit-textfield-decoration-container")…` | medium |
| **MEDIUM** | Twilio App SID | `https://jobs.netflix.com/%5C.js` | `APORE_20240903_NETFLIX_JobsitesSG_` | medium |
| **CRITICAL** | Heroku API Key | `https://jobs.netflix.com/%5C.js` | `22ee2df4-2249-4280-8b58-e53ceefcac95` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/03k0_nub65s~w.js` | `ACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJl` | high |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `password="",s.host=null,s.port=null,s.path=[],s.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `password=r.password,s.host=r.host,s.port=r.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `password=r.password,s.host=r.host,s.port=r.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `password=r.password,s.host=r.host,s.port=r.port,c=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `Password:function(){return` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `Password:function(t){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `password=n.getPassword(),e.host=n.getHost(),e.host…` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/03~yq9q893hmn.js` | `password",Ag("getPassword","setPassword")),so(Pg,"…` | medium |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/0886e-te5tcp0.js` | `actSourcePageFromFlightRouterState` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/0886e-te5tcp0.js` | `ActionDidRevalidateStaticAndDynami` | high |
| **HIGH** | Basic Auth Credentials | `https://jobs.netflix.com/_next/static/chunks/089n_43zxbqbw.js` | `BasicMaterial=` | high |
| **HIGH** | Basic Auth Credentials | `https://jobs.netflix.com/_next/static/chunks/089n_43zxbqbw.js` | `BasicMaterial` | high |
| **HIGH** | Basic Auth Credentials | `https://jobs.netflix.com/_next/static/chunks/089n_43zxbqbw.js` | `BasicMaterial:` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/089n_43zxbqbw.js` | `AcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAA` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/089n_43zxbqbw.js` | `ACAAIABoAAAAAXaXBtYQAAAAAAAAABAAEE` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/089n_43zxbqbw.js` | `ackgroundProvider-module-scss-modu` | high |
| **CRITICAL** | Square Access Token | `https://jobs.netflix.com/_next/static/chunks/089n_43zxbqbw.js` | `EAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAAABcAAAAoaWlu…` | high |
| **CRITICAL** | Square Access Token | `https://jobs.netflix.com/_next/static/chunks/089n_43zxbqbw.js` | `EAAAABAAAAEHBpeGkAAAAAAwgICAAAAAxhdjFDgQAMAAAAABNj…` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/09wr_2vdc3yom.js` | `ACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJl` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/09wr_2vdc3yom.js` | `ACuyE5IAAAAVUlEQVR42j2MSwqAMBBDZ68` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/0d3shmwh5_nmn.js` | `ActionDidRevalidateStaticAndDynami` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/0o32pymt6.p2t.js` | `ACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJl` | high |
| **HIGH** | API Token / Key | `https://jobs.netflix.com/_next/static/chunks/0pqt~8bl3ukh4.js` | `API Usage` | medium |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/0wu_aayw0psgm.js` | `ACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJl` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/0z9kjhg1i3f6b.js` | `ACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJl` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/0ztf5tn0vgp-_.js` | `actSourcePageFromFlightRouterState` | high |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/0ztf5tn0vgp-_.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://jobs.netflix.com/_next/static/chunks/0ztf5tn0vgp-_.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/12ofn_zmdhlba.js` | `ace-allownode-allowedtypes-and-dis` | high |
| **HIGH** | Twilio Account SID | `https://jobs.netflix.com/_next/static/chunks/13ujtabdaqifl.js` | `ACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJl` | high |
| **MEDIUM** | Twilio App SID | `https://jobs.netflix.com/edge.fullstory.com/s/edge.fullstory.com/s/fs.js` | `APORE_20240903_NETFLIX_JobsitesSG_` | medium |
| **CRITICAL** | Heroku API Key | `https://jobs.netflix.com/edge.fullstory.com/s/edge.fullstory.com/s/fs.js` | `22ee2df4-2249-4280-8b58-e53ceefcac95` | high |
| **MEDIUM** | Twilio App SID | `https://jobs.netflix.com/edge.fullstory.com/s/fs.js` | `APORE_20240903_NETFLIX_JobsitesSG_` | medium |
| **CRITICAL** | Heroku API Key | `https://jobs.netflix.com/edge.fullstory.com/s/fs.js` | `22ee2df4-2249-4280-8b58-e53ceefcac95` | high |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/chunks/Moment.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/Moment.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/chunks/Moment.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/Moment.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/chunks/Moment.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/Moment.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/chunks/Moment.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/Moment.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/chunks/Moment.js?countryCode=IN&amp;*=_next%2Fstatic%2Fchunks%2FMoment.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/Moment.js?countryCode=IN&amp;*=_next%2Fstatic%2Fchunks%2FMoment.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/chunks/Moment.js?countryCode=IN&amp;*=_next%2Fstatic%2Fchunks%2FMoment.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/Moment.js?countryCode=IN&amp;*=_next%2Fstatic%2Fchunks%2FMoment.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/chunks/_next/static/chunks/Moment.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/_next/static/chunks/Moment.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/chunks/_next/static/chunks/Moment.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/_next/static/chunks/Moment.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **MEDIUM** | Twilio App SID | `https://media.netflix.com/_next/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_De` | medium |
| **MEDIUM** | Twilio App SID | `https://media.netflix.com/_next/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `April_May_June_July_August_Septemb` | medium |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/framework-df468cf7b33363bb.js` | `actInternalMemoizedUnmaskedChildCo` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/framework-df468cf7b33363bb.js` | `actInternalMemoizedMaskedChildCont` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/framework-df468cf7b33363bb.js` | `actInternalMemoizedMergedChildCont` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/framework-df468cf7b33363bb.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/framework-df468cf7b33363bb.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `password="",this.host=null,this.port=null,this.pat…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `password=r.password,this.host=r.host,this.port=r.p…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `password=r.password,this.host=r.host,this.port=r.p…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `password=r.password,this.host=r.host,this.port=r.p…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `password=r.password,this.host=r.host,this.port=r.p…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `Password:function(){return` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `Password:function(t){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `password=n.getPassword(),e.host=n.getHost(),e.host…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/main-40f843b55ed5a9b6.js` | `password",tW("getPassword","setPassword")),l(tH,"h…` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `BasicHtmlNodes:` | high |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `BasicHtmlNodesFor:` | high |
| **HIGH** | API Token / Key | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `API compatible` | medium |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `ackgroundColorContextualBannerNeut` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `ackgroundColorContextualBannerRegu` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `ackgroundColorContextualBannerSucc` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `ackgroundColorContextualBannerWarn` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `ackgroundColorContextualBannerErro` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/pages/_app-ece13c027e963805.js` | `password:!0,number:!0,date:!0,month:!0,week:!0,tim…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `password:"https://help.netflix.com/".concat(e,"/no…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password="",s.host=null,s.port=null,s.path=[],s.qu…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,s.…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=r.password,s.host=r.host,s.port=r.port,c=…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `Password:function(){return` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `Password:function(t){var` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password="";for(var` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password=n.getPassword(),e.host=n.getHost(),e.host…` | medium |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/chunks/polyfills-42372ed130431b0a.js` | `password",Ag("getPassword","setPassword")),so(Pg,"…` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F113-54612556567c5907.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F113-54612556567c5907.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F113-54612556567c5907.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F113-54612556567c5907.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F213-4d9c1f3b3a745f44.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F213-4d9c1f3b3a745f44.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F213-4d9c1f3b3a745f44.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F213-4d9c1f3b3a745f44.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F219-6795a6f2a7c65c5b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F219-6795a6f2a7c65c5b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F219-6795a6f2a7c65c5b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F219-6795a6f2a7c65c5b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F236-5e4de06559285774.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F236-5e4de06559285774.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F236-5e4de06559285774.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F236-5e4de06559285774.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F269-946a8ad6bf925b38.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F269-946a8ad6bf925b38.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F269-946a8ad6bf925b38.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F269-946a8ad6bf925b38.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F280-6ddb053189490c83.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F280-6ddb053189490c83.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F280-6ddb053189490c83.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F280-6ddb053189490c83.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F300-71e1b115ad6976d6.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F300-71e1b115ad6976d6.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F300-71e1b115ad6976d6.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F300-71e1b115ad6976d6.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F345-0615c307ac44e39d.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F345-0615c307ac44e39d.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F345-0615c307ac44e39d.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F345-0615c307ac44e39d.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F449-456bcecb76a9419b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F449-456bcecb76a9419b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F449-456bcecb76a9419b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F449-456bcecb76a9419b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F459-9f50698b862da313.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F459-9f50698b862da313.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F459-9f50698b862da313.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F459-9f50698b862da313.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F516-d77b45ff297cfb30.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F516-d77b45ff297cfb30.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F516-d77b45ff297cfb30.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F516-d77b45ff297cfb30.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F550-56c05694e52c7af8.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F550-56c05694e52c7af8.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F550-56c05694e52c7af8.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F550-56c05694e52c7af8.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F602-0c7177fafa81d782.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F602-0c7177fafa81d782.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F602-0c7177fafa81d782.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F602-0c7177fafa81d782.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F658-45a47801bd911c69.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F658-45a47801bd911c69.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F658-45a47801bd911c69.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F658-45a47801bd911c69.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F738-5f2a3c7ebaa46a6c.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F738-5f2a3c7ebaa46a6c.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F738-5f2a3c7ebaa46a6c.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F738-5f2a3c7ebaa46a6c.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F814-7dbc831267b56e4a.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F814-7dbc831267b56e4a.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F814-7dbc831267b56e4a.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F814-7dbc831267b56e4a.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F842-afce79e906c1e379.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F842-afce79e906c1e379.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F842-afce79e906c1e379.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F842-afce79e906c1e379.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F93865858-1a9f2e9cbfb492fc.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F93865858-1a9f2e9cbfb492fc.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F93865858-1a9f2e9cbfb492fc.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F93865858-1a9f2e9cbfb492fc.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F955-e1dce3e356870753.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F955-e1dce3e356870753.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F955-e1dce3e356870753.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2F955-e1dce3e356870753.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/113-54612556567c5907.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/213-4d9c1f3b3a745f44.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/219-6795a6f2a7c65c5b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/236-5e4de06559285774.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/269-946a8ad6bf925b38.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/280-6ddb053189490c83.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/300-71e1b115ad6976d6.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/345-0615c307ac44e39d.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/449-456bcecb76a9419b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/459-9f50698b862da313.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/516-d77b45ff297cfb30.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/550-56c05694e52c7af8.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/602-0c7177fafa81d782.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/658-45a47801bd911c69.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/738-5f2a3c7ebaa46a6c.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/814-7dbc831267b56e4a.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/842-afce79e906c1e379.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/93865858-1a9f2e9cbfb492fc.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/955-e1dce3e356870753.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fa29ae703-cd43c5a1bde5c24c.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fa29ae703-cd43c5a1bde5c24c.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fa29ae703-cd43c5a1bde5c24c.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/a29ae703-cd43c5a1bde5c24c.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fa29ae703-cd43c5a1bde5c24c.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fb7dac8a5-43f31d4c50c33dce.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fb7dac8a5-43f31d4c50c33dce.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fb7dac8a5-43f31d4c50c33dce.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/b7dac8a5-43f31d4c50c33dce.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fb7dac8a5-43f31d4c50c33dce.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fe999873e-2ce9cfc212871b2e.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fe999873e-2ce9cfc212871b2e.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fe999873e-2ce9cfc212871b2e.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/e999873e-2ce9cfc212871b2e.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fe999873e-2ce9cfc212871b2e.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2F_error-70b1f584e630e8dc.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2F_error-70b1f584e630e8dc.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2F_error-70b1f584e630e8dc.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2F_error-70b1f584e630e8dc.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_error-70b1f584e630e8dc.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Faccount-bfc755b404055607.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Faccount-bfc755b404055607.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Faccount-bfc755b404055607.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/account-bfc755b404055607.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Faccount-bfc755b404055607.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fapply-b8b8724000a8352e.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fapply-b8b8724000a8352e.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fapply-b8b8724000a8352e.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/apply-b8b8724000a8352e.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fapply-b8b8724000a8352e.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fcontact-us-9fe19f63d9c28706.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fcontact-us-9fe19f63d9c28706.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fcontact-us-9fe19f63d9c28706.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/contact-us-9fe19f63d9c28706.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fcontact-us-9fe19f63d9c28706.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Findex-b865a6e0b265e98b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Findex-b865a6e0b265e98b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Findex-b865a6e0b265e98b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/index-b865a6e0b265e98b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Findex-b865a6e0b265e98b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fmy-screeners-a8677ca00216cdf3.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fmy-screeners-a8677ca00216cdf3.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fmy-screeners-a8677ca00216cdf3.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/my-screeners-a8677ca00216cdf3.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fmy-screeners-a8677ca00216cdf3.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsearch-8a96c39cf6d2415b.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsearch-8a96c39cf6d2415b.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsearch-8a96c39cf6d2415b.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/search-8a96c39cf6d2415b.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsearch-8a96c39cf6d2415b.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsetup-screeners-676428adc99f0169.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsetup-screeners-676428adc99f0169.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsetup-screeners-676428adc99f0169.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/setup-screeners-676428adc99f0169.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsetup-screeners-676428adc99f0169.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsite-unavailable-e41748134bf5eff3.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsite-unavailable-e41748134bf5eff3.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsite-unavailable-e41748134bf5eff3.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/site-unavailable-e41748134bf5eff3.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fsite-unavailable-e41748134bf5eff3.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js?countryCode=IN&amp` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js?countryCode=IN&amp` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js?countryCode=IN&amp` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js?countryCode=IN&amp` | `password","request_reason_screener_issue":"I'm` | medium |
| **HIGH** | Basic Auth Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fwelcome-6cb9ea8120dcb2c0.js` | `basic_info` | high |
| **HIGH** | Twilio Account SID | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fwelcome-6cb9ea8120dcb2c0.js` | `acfef05-6890-4fba-8f1f-44cc313ee12` | high |
| **CRITICAL** | Heroku API Key | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fwelcome-6cb9ea8120dcb2c0.js` | `3acfef05-6890-4fba-8f1f-44cc313ee12d` | high |
| **HIGH** | Hardcoded Credentials | `https://media.netflix.com/_next/static/dis2BKdPCyVz8yD02CffD/static/chunks/pages/welcome-6cb9ea8120dcb2c0.js?countryCode=IN&amp;*=_next%2Fstatic%2Fdis2BKdPCyVz8yD02CffD%2Fstatic%2Fchunks%2Fpages%2Fwelcome-6cb9ea8120dcb2c0.js` | `password","request_reason_screener_issue":"I'm` | medium |
| **CRITICAL** | Google API Key | `https://www.google-analytics.com/analytics.js` | `AIzaSyA65lEHUEizIsNtlbNo-l2K18dT680nsaM` | high |