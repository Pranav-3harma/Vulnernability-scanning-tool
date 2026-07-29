# Security Assessment Report: flipkart.com
**Generated Date:** 2026-07-29 15:13:47

---

## Executive Summary
- **Target:** `flipkart.com`
- **Subdomains Discovered:** 1115
- **Live Web Endpoints (HTTPX):** 2
- **Crawled Endpoints (Katana):** 1
- **Secrets Found in JS Files:** 642
- **Nuclei Findings Count:** 2
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
| **INFO** | Microsoft Azure Domain Tenant ID - Detect | `https://login.microsoftonline.com:443/flipkart.com/v2.0/.well-known/openid-configuration` | `azure-domain-tenant` |
| **INFO** | WAF Detection | `https://flipkart.com` | `waf-detect` |

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
- Total endpoints discovered: 512
  - `https://1.rome.api.flipkart.com` (Other)  — source: https://flipkart.com
  - `https://2.rome.api.flipkart.com` (Other)  — source: https://flipkart.com
  - `https://static-assets-web.flixcart.com` (Other)  — source: https://flipkart.com
  - `https://rukminim2.flixcart.com` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/logo_lite-cbb357.png` (Other)  — source: https://flipkart.com
  - `image/png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/app-icons/app-icon_192x192.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/app-icons/app-icon_256x256.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/app-icons/app-icon_384x384.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/app-icons/app-icon_512x512.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_430x932.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_393x852.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_390x844.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_428x926.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_375x812.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_414x736.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_320x568.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_414x896.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_375x667.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_1024x1366.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_834x1194.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_820x1180.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_810x1080.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_834x1112.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_768x1024.png` (Other)  — source: https://flipkart.com
  - `/apex-static/images/fk-lite-assets/splash-screen/splash-screen_744x1133.png` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/fonts/Inter-Regular.woff2` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/fonts/Inter-SemiBold.woff2` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/fonts/Inter-Bold.woff2` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/234/image/5b013f4848aeb33a.jpg` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.css` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossCommon.css` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.css` (Other)  — source: https://flipkart.com
  - `http://custom.transaction` (Other)  — source: https://flipkart.com
  - `/called` (Other)  — source: https://flipkart.com
  - `API/noticeError/called` (API)  — source: https://flipkart.com
  - `/` (Other)  — source: https://flipkart.com
  - `https://www.flipkart.com` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/DesktopComponents.css` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/52/44/image/d2ecfddf891a3922.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/26/22/image/d2ecfddf891a3922.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/92/36/image/31f7e3af490c225f.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/46/18/image/31f7e3af490c225f.png` (Other)  — source: https://flipkart.com
  - `/flights-travel-uhp-at-store` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/58/44/image/7ab4040af860941d.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/29/22/image/7ab4040af860941d.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/72/36/image/5a9ff48eef96b876.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/36/18/image/5a9ff48eef96b876.png` (Other)  — source: https://flipkart.com
  - `/search` (Other)  — source: https://flipkart.com
  - `/2000/svg` (Other)  — source: https://flipkart.com
  - `/searchsuggestion` (Other)  — source: https://flipkart.com
  - `/account/login` (Auth)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/profile-6bae67.svg` (Other)  — source: https://flipkart.com
  - `/plus` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/fkplus-f1a046.svg` (Other)  — source: https://flipkart.com
  - `/account/orders` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/orders-e444ac.svg` (Other)  — source: https://flipkart.com
  - `/wishlist` (Other)  — source: https://flipkart.com
  - `/sell-online/` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/Store-134a49.svg` (Other)  — source: https://flipkart.com
  - `/account/rewards` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/rewards-a8acd9.svg` (Other)  — source: https://flipkart.com
  - `/the-gift-card-store` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/GiftCardV2-6885f6.svg` (Other)  — source: https://flipkart.com
  - `/communication-preferences/push` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/notificationPreferences-3439a8.svg` (Other)  — source: https://flipkart.com
  - `/helpcentre` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/helpcenter-f09fd8.svg` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/AdvertiseV2-e6b830.svg` (Other)  — source: https://flipkart.com
  - `/mobile-apps` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/downloadApp-7569a8.svg` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/NotificationSetting-caba6c.svg` (Other)  — source: https://flipkart.com
  - `/viewcart` (Other)  — source: https://flipkart.com
  - `/batman-returns/batman-returns/p/images/header_cart_v4-6ac9a8.svg` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/all.svg` (Other)  — source: https://flipkart.com
  - `/ss-26-base-inline-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/fashion.svg` (Other)  — source: https://flipkart.com
  - `/mobile-phones-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/mobiles.svg` (Other)  — source: https://flipkart.com
  - `/new-elec-clp-march-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/electronics.svg` (Other)  — source: https://flipkart.com
  - `/bpc-bau-new-inline-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/beauty.svg` (Other)  — source: https://flipkart.com
  - `/home-kitchen-25-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/home-final.svg` (Other)  — source: https://flipkart.com
  - `/tv-and-appliances-inline-ab-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/tv.svg` (Other)  — source: https://flipkart.com
  - `/toysbc-new26-inline-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/toy.svg` (Other)  — source: https://flipkart.com
  - `/fnhc-2025-new-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/food.svg` (Other)  — source: https://flipkart.com
  - `/aa-2025-new-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/auto-acc.svg` (Other)  — source: https://flipkart.com
  - `/sf-inline-2025-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/sport.svg` (Other)  — source: https://flipkart.com
  - `/india-ka-furniture-studio-inlines-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/furniture.svg` (Other)  — source: https://flipkart.com
  - `/booksmedia-2025-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/books.svg` (Other)  — source: https://flipkart.com
  - `/twowheelers-at-store` (Other)  — source: https://flipkart.com
  - `/apex-static/images/svgs/L1Nav/auto-new.svg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/360/image/6015c703748e7a42.jpg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/220/image/6015c703748e7a42.jpg` (Other)  — source: https://flipkart.com
  - `/mens-footwear/mens-slippers-flip-flops/pr` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/b68b8e773e9bdfea.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/b68b8e773e9bdfea.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/b68b8e773e9bdfea.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/72ce7261255bed4d.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/72ce7261255bed4d.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/72ce7261255bed4d.png` (Other)  — source: https://flipkart.com
  - `/cadlec-defender-5-year-warranty-bldc-motor-remote-1200-mm-ceiling-fan/p/itm06a8bf3115478` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/6a838f36968eb033.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/6a838f36968eb033.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/6a838f36968eb033.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/4c35e731936d1c2f.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/4c35e731936d1c2f.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/4c35e731936d1c2f.png` (Other)  — source: https://flipkart.com
  - `/vivo-t5x-5g-fusion-red-128-gb/p/itm7da8aa253e72b` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/1ae9be3bc0146d16.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/1ae9be3bc0146d16.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/1ae9be3bc0146d16.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/6a9146ee79e84423.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/6a9146ee79e84423.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/6a9146ee79e84423.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/aa023621dfacb4ed.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/aa023621dfacb4ed.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/aa023621dfacb4ed.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/aabb762c8cea7696.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/aabb762c8cea7696.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/aabb762c8cea7696.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/f655d854a7ef812c.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/f655d854a7ef812c.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/f655d854a7ef812c.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/780/image/5e2c4ab813da09b4.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/490/image/5e2c4ab813da09b4.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/480/230/image/5e2c4ab813da09b4.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/4843f5e3e39f1a67.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/4843f5e3e39f1a67.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/4843f5e3e39f1a67.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/8521ddedc16a3a96.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/8521ddedc16a3a96.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/8521ddedc16a3a96.png` (Other)  — source: https://flipkart.com
  - `/health-care/health-supplements/milk-drink-mixes/pr` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/916fecd25300170c.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/916fecd25300170c.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/916fecd25300170c.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/a6f220c3de2f9759.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/a6f220c3de2f9759.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/a6f220c3de2f9759.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/ee27eb03888df008.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/ee27eb03888df008.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/ee27eb03888df008.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/91e6fd038b997be7.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/91e6fd038b997be7.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/91e6fd038b997be7.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/b56dbedee1948cb7.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/b56dbedee1948cb7.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/b56dbedee1948cb7.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/e44ad9c158ee10b8.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/e44ad9c158ee10b8.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/e44ad9c158ee10b8.png` (Other)  — source: https://flipkart.com
  - `/horlicks-diabetes-plus-chocolate-400g-helps-manage-blood-sugar-starts-working-day-1/p/itm0cd7ebe76bc1c` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/17aecee1db4ae0c3.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/17aecee1db4ae0c3.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/17aecee1db4ae0c3.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/350/170/image/8bcb7dddfa6edab4.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/220/110/image/8bcb7dddfa6edab4.png` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/110/50/image/8bcb7dddfa6edab4.png` (Other)  — source: https://flipkart.com
  - `/image/280/374/xif0q/panty/w/m/f/90-5-luxkarismapanty-lux-original-imahhf5tft3s8dqn.jpeg` (Other)  — source: https://flipkart.com
  - `/image/140/187/xif0q/panty/w/m/f/90-5-luxkarismapanty-lux-original-imahhf5tft3s8dqn.jpeg` (Other)  — source: https://flipkart.com
  - `/image/280/374/xif0q/sari/c/c/1/free-rsmps-001-soham-unstitched-original-imahzf7x9eekerkm.jpeg` (Other)  — source: https://flipkart.com
  - `/image/140/187/xif0q/sari/c/c/1/free-rsmps-001-soham-unstitched-original-imahzf7x9eekerkm.jpeg` (Other)  — source: https://flipkart.com
  - `/image/280/374/xif0q/track-suit/4/r/l/m-tk-black-02-abdani-original-imah9b7mvmjqzfsv.jpeg` (Other)  — source: https://flipkart.com
  - `/image/140/187/xif0q/track-suit/4/r/l/m-tk-black-02-abdani-original-imah9b7mvmjqzfsv.jpeg` (Other)  — source: https://flipkart.com
  - `/image/280/374/xif0q/bra/2/a/j/lightly-padded-40-2-regular-no-regular-bf-foam-anamta-original-imahgamxqwy6v3qq.jpeg` (Other)  — source: https://flipkart.com
  - `/image/140/187/xif0q/bra/2/a/j/lightly-padded-40-2-regular-no-regular-bf-foam-anamta-original-imahgamxqwy6v3qq.jpeg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1570/350/image/797026f420ca951c.jpg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/980/220/image/797026f420ca951c.jpg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/470/100/image/797026f420ca951c.jpg` (Other)  — source: https://flipkart.com
  - `/www/1600/530/promos/10/06/2025/0761f406-0baa-4fad-94e9-7fb1b27e8ca7.jpg` (Other)  — source: https://flipkart.com
  - `/www/1000/330/promos/10/06/2025/0761f406-0baa-4fad-94e9-7fb1b27e8ca7.jpg` (Other)  — source: https://flipkart.com
  - `/www/480/160/promos/10/06/2025/0761f406-0baa-4fad-94e9-7fb1b27e8ca7.jpg` (Other)  — source: https://flipkart.com
  - `/offers-list/recommended-for-you` (Other)  — source: https://flipkart.com
  - `/all/~cs-6ef68bc8d283b86730515a8f2c87ff23/pr` (Other)  — source: https://flipkart.com
  - `/image/280/374/xif0q/headphone/t/j/o/-enriched-transparent-original-imahgnf4fegyc7mu.png` (Other)  — source: https://flipkart.com
  - `/image/140/187/xif0q/headphone/t/j/o/-enriched-transparent-original-imahgnf4fegyc7mu.png` (Other)  — source: https://flipkart.com
  - `/all/~cs-21e789349087c946d1b57cb0a6372ff1/pr` (Other)  — source: https://flipkart.com
  - `/image/280/374/xif0q/smartwatch/s/i/u/-original-imah76jt64ffmwg4.jpeg` (Other)  — source: https://flipkart.com
  - `/image/140/187/xif0q/smartwatch/s/i/u/-original-imah76jt64ffmwg4.jpeg` (Other)  — source: https://flipkart.com
  - `/all/~cs-8b496c9470edf46bfa6b26c32f3aa85a/pr` (Other)  — source: https://flipkart.com
  - `/image/280/374/xif0q/mixer-grinder-juicer/q/o/o/-original-imahpjw7hcqyktzz.jpeg` (Other)  — source: https://flipkart.com
  - `/image/140/187/xif0q/mixer-grinder-juicer/q/o/o/-original-imahpjw7hcqyktzz.jpeg` (Other)  — source: https://flipkart.com
  - `/all/~cs-bacfa40f92431ec57291097ce5888532/pr` (Other)  — source: https://flipkart.com
  - `/image/280/374/xif0q/speaker/r/n/n/-original-imahezg4nm5qpjmb.jpeg` (Other)  — source: https://flipkart.com
  - `/image/140/187/xif0q/speaker/r/n/n/-original-imahezg4nm5qpjmb.jpeg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1570/350/image/679f84c79e14f710.jpg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/980/220/image/679f84c79e14f710.jpg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/470/100/image/679f84c79e14f710.jpg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1600/640/image/70fcb68e3d18caa4.jpg` (Other)  — source: https://flipkart.com
  - `/fk-p-flap/1000/400/image/70fcb68e3d18caa4.jpg` (Other)  — source: https://flipkart.com

### Scan Statistics

| Metric | Value |
|---|---|
| Status | `success` |
| Total JavaScript Files | 1 |
| Files Successfully Scanned | 1 |
| Files Failed / Timed Out | 0 |
| **Secrets Found** | **642** |
| Critical | 453 |
| High | 152 |
| Medium | 23 |
| Low | 14 |
| Informational | 0 |

### Findings

| Severity | Secret Type | Source JavaScript URL | Matched Value (truncated) | Confidence |
|---|---|---|---|---|
| **LOW** | Google Captcha Key | `https://flipkart.com/` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgZml` | medium |
| **LOW** | Google Captcha Key | `https://flipkart.com/` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGg` | medium |
| **LOW** | Google Captcha Key | `https://flipkart.com/` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2x` | medium |
| **HIGH** | API Token / Key | `https://flipkart.com/` | `api_from_browser_ab` | medium |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `acerpure-nitro-189-2-cm-75-inch-ql` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `ache-green-original-imahc5d2y2h4fw` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `ack16-mat-8-5-feet-bpa-free-horse-` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `ack-16-small-snowberry-original-im` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `action-athleo-atg-424-comfortable-` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `action-grey-watermarked-original-i` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `ace-wash-combo-50ml-each-2-combo-f` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `acid-oily-skin-sulphate-free-anti-` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `ace-cleanser-lha-zinc-acne-pimples` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `ace-serum-skin-brightening-2-niaci` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `ack-stunners-6-0-white-dial-silver` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `acid-face-serum-1-alpha-arbutin-ni` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `acinamide-dark-spots-blemishes-pig` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `aCBkPSJNMTMuNTQzNiAxMC42MTc5TDIwLj` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `ACE_HEADER_V3_DLS_1_tabbedHeaderWi` | high |
| **HIGH** | Twilio Account SID | `https://flipkart.com/` | `across-funnel-renaming-ads-to-spon` | high |
| **MEDIUM** | Twilio App SID | `https://flipkart.com/` | `apple-jamun-face-wash-combo-50ml-e` | medium |
| **MEDIUM** | Twilio App SID | `https://flipkart.com/` | `apis-pure-honey-squeezy-500g-natur` | medium |
| **MEDIUM** | Twilio App SID | `https://flipkart.com/` | `apple-iphone-16-pro-natural-titani` | medium |
| **MEDIUM** | Twilio App SID | `https://flipkart.com/` | `apple-iphone-17-pro-cosmic-orange-` | medium |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `8620794b-87fa-4e66-9eff-534828a75346` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `40c40a28-0aa2-47e6-91f3-db6ef8afcbfd` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `046495cc-c0f7-46dd-99ef-a63f8833e4c8` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `f7634981-4fd5-4127-9b93-9f57606dccd3` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `39d573db-dd62-430a-8166-0dcc53b6f299` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `6e4fe892-0517-46bc-ac56-f3ee86bf8aa4` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `db1549b7-a409-4bea-aa76-d57e97fd9304` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `c1895632-47f2-45f7-a2af-0f736fd52969` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `b124a16b-e4b6-4d76-a271-81cf6ee830c9` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `e33209f1-50f0-4f08-bc7b-bf0d61c87b84` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `735e2a1e-ab96-41c2-b875-56c25c233a29` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `935ce1e9-ca68-4b8c-9e12-f10298bb86d4` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `ed27f892-1bc6-462f-805b-953f5add4f6a` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `9b08f194-51e5-4e6a-a052-f5f91d75b8a0` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `85837403-84fa-49b6-a23d-9c878b810d45` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `56b829f7-d4ea-40e9-9c35-900560809a09` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `6350965b-ae8b-4b2a-a298-2ce4c7371f0d` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `6c3c5fe2-c236-4fa2-8d97-595e1e01da01` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `9c056ec4-f39c-4740-938d-33e1a6c7c108` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `44d98c6b-16de-4759-a3c4-9d6412ad8bfa` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `4119b37e-1811-4401-8fe5-41646a5e624a` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `1514bd7d-a1d1-46a8-bd7d-028fc27f25fd` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `afa33081-fdc2-4dac-af42-7f99ff316372` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `a8956a0e-08db-468a-a2be-59d69bde697d` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `71af54bd-9160-41ff-81cc-c55e534dedeb` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `770a758a-02a1-4d17-a58a-23629e78369e` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `16d67830-9e3d-4265-ba00-b89872a6b1b6` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `a1362677-d570-4fad-a0c5-4e5aede723b5` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `b75e7523-d45a-42ec-af0e-ecae9339f88f` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `419c1794-2911-4c46-8ab1-65fd60deddff` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `0a29047b-b18f-4481-81ff-9ea09fe57dd9` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `35db7ed6-1808-4fd5-bcde-9a7886ab72d0` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `01603892-4131-4901-92f5-129d1b65958a` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `9f609338-34f1-4828-9693-1af1b39a6f8e` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `8319bd84-cbc7-4ab4-a754-74a190576f8e` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `163411fb-3ef7-4b34-bf1f-4fbad375fa79` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `a9131f44-1c69-4b13-9cc8-785ab64171a9` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `82fcc789-3dcd-4964-81de-7689a71bc7f9` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `2888f310-8fba-4d2f-8a69-f7e12870fa17` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `e54bbba6-b4ba-40ac-b1a7-5ca3e16d23d2` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `cf2979c8-1e4c-4d32-b9b1-62deb00e6c71` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `646e58a1-fbab-451f-b1d1-6d21e7828767` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `a293a8d1-2fd9-4884-846f-91a3b1c7f5a1` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `7394e0d1-bf17-4452-b742-65c764d0af2d` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `14327ea8-fd2b-42b3-bfae-2beaf5eb687d` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `dfd47f5a-f8e6-47e3-868b-819f874ce89c` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `3f04ed13-41e0-43c0-80bd-f962fb721500` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `b32b2533-8b80-11f1-8814-f3090d886c99` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `b329786e-8b80-11f1-ad4f-4f780f60ef97` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `b329786f-8b80-11f1-ad4f-4f780f60ef97` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `e85e11d5-ef53-af25-3ed0-346f8d6295c6` | high |
| **CRITICAL** | Heroku API Key | `https://flipkart.com/` | `8067d1e6-1899-2a63-12f3-e9dee38b91b0` | high |
| **HIGH** | Hardcoded Credentials | `https://flipkart.com/` | `password:!0}};return{allow_bfcache:!0,privacy:{coo…` | medium |
| **HIGH** | Hardcoded Credentials | `https://flipkart.com/` | `password:!0}}},spa:{enabled:!0,harvestTimeSeconds:…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/fkvendor.js` | `password:!0,range:!0,search:!0,tel:!0,text:!0,time…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/fkvendor.js` | `password"===e.type)\|\|"textarea"===t\|\|"true"===e.co…` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossCommon.js` | `API error` | medium |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossCommon.js` | `cb582554-0856-4e83-8354-f9f473f42a5a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossCommon.js` | `6f0764bb-e654-4fcc-8f78-85d6dd23c3a1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossCommon.js` | `1b2aef47-a316-4586-a817-ff6fb4bde745` | high |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossCommon.js` | `password");var` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBzdHJ` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyBmaWx` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCB` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `ApiErrorEvent` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `Api Error` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `apiErrorInfo` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `apiErrorMessage` | medium |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `aCBkPSJNNjEuNjQ3IDUuOTFjLS44NS0xLj` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `aCBkPSJNNDEuNjc1IDEzLjAxYy42ODUuMz` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `aC0xLjU2Yy0uNjE1IDEuNzQ4LTIuMjggMy` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `aCBkPSJNMTcuNTU2IDcuODQ3SDFNNy40NS` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `ackEventWithModifiedNavigationCont` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `aC05LjYyMWMtLjQxMyAwLS43NjUtLjI2Ny` | high |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `APP_NOTIFICATIONS_DELETE_NOTIFICAT` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `appNotificationsUnreadCountSuccess` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `APP_NOTIFICATIONS_UNREAD_COUNT_SUC` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `APP_NOTIFICATIONS_UNREAD_COUNT_ERR` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `APP_NOTIFICATIONS_MARK_AS_READ_SUC` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `APP_NOTIFICATIONS_MARK_AS_READ_ERR` | medium |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `046495cc-c0f7-46dd-99ef-a63f8833e4c8` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `e258152d-055c-4dc5-a358-d0dcc4acd962` | high |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password:e.data.password};i.A.fetch("post",{ajaxCo…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password:n}=e.data,{requestId:r,loginId:o,otp:a}=t…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password:n,otp:a,otpRequestId:r};i.A.fetch("post",…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password:o}=e.data,{requestId:a,loginId:s,otp:c}=r…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `PASSWORD:"AskPassword:Displayed",LOGIN_PAGE_FROM_B…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `Password:Displayed"},l="prop21",c="prop65",u="Logi…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `PASSWORD:"Login2Step:Phone_Existing_EnterPassword"…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `Password",EMAIL_ENTER_PASSWORD_BOTTOMSHEET:"HP_Log…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `Password",PHONE_NEW_ENTER_OTP_BOTTOMSHEET:"HP_Logi…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `PASSWORD:Mobile_FkUser_OTP_Sent",ON_FORGOT_OTP_SEN…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `PASSWORD:Email_FkUser_OTP_Sent",EMAIL_SIGN_IN_SUCC…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password",additionalData:null});const` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password:e.password};l.A.loginViaSmartLock({cred:t…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password",FORGOT_OTP:"/login/forgot/otp",SIGN_UP:"…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password:!0,mediation:"optional"}))).catch((()=>Pr…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password:{id:e.id,password:e.password,name:e.name,…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `Pwd",window.omniture.trackLink(o,"Login` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `PwdSuccess(e,t,n){let` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `PwdClick",window.omniture.trackLink(o,"Login` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `password"in` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `PASSWORD:"password",FEDERATED:"FederatedCredential…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/app.js` | `PASSWORD:"FORGOTPASSWORD",LOGINWITHOTP:"LOGINWITHO…` | medium |
| **CRITICAL** | Google API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `AIzaSyAtKsoYaqKOXMV00f9qLDAgbYYevlxAGsQ` | high |
| **HIGH** | Basic Auth Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `BASIC_DETAIL=` | high |
| **HIGH** | Basic Auth Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `BASIC_DETAIL` | high |
| **HIGH** | Basic Auth Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `BASIC_FORM_DATA_WIDGET=` | high |
| **HIGH** | Basic Auth Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `BASIC_FORM_DATA_WIDGET` | high |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_ACTION` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `apiErrorInfo` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_HANDLER` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_CALLED` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_FAILURE` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_SUCCESS` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_STATUS` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API providers` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_VERSION` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API error` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_TIME_TAKEN` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_DEBOUNCE_MS` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_API_EVENT` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `apiEndPoint` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `apiEndpoint` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `API_NOT_AVAILABLE` | medium |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `AccessLocationActionDispatchOnHPDe` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `accessLocationActionDispatchOnHPDe` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `AccessLocationActionDispatchPostSe` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `accessLocationActionDispatchPostSe` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `AccessLocationPollingBackoffConsta` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `accessLocationPollingBackoffConsta` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ackDiscoveryContentEngagementEvent` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ACE_TABBED_HEADER_PAGE_LOAD_ADD_DA` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ActionWithBottomSheetTrackingConfi` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ActionWithColorSwatchBottomSheetBe` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ackEventWithModifiedNavigationCont` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ac14d0-6e45-49f3-8a70-88d06d3e7bdc` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ACQUISITION_PAYLATER_NON_ADOPTER_W` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ACQUISITION_CBC_NON_ADOPTER_WIDGET` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ACQUISITION_PAYLATER_ADOPTER_WIDGE` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ackPermissionGrantedAndLocationSer` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `actNudgeViewCoordsFromNudgePositio` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ACKGROUNDSUBTLE_OPACITY_AD_AND_SPO` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ACKGROUNDBOLD_BRANDSECONDARY_EMPHA` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ACKGROUNDBOLD_BRANDPRIMARY_EMPHASI` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `actionPageColorOverridesResponsePa` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ACK_MARKETPLACE_TAB_CHANGE_PAGE_VI` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ackTravelCancellationInitPageLoadE` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ackTravelCancellationReviewPageLoa` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ackTravelCancellationResultPageLoa` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ac0e89b-eb93-4d55-9b5a-4efe925a467` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `acdb9b-5848-47e8-bd46-81054aac032e` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ac32fe8-f2d4-47fc-a498-5ee2a696531` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `aCarouselSwipeOnboardingLocalStora` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `aCaptureTooltipOnboardingLocalStor` | high |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `applyUrlDeferredActionsAndNavigate` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `apApplicationStateToComponentProps` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `AppSessionAndTriggerLocationRefres` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `appLaunchCountSinceInAppUpdateShow` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `appableViewContainerLeftAlignedSty` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `appableViewContainerRightAlignedSt` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `appableTravelDatesSectionContainer` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `appableTravelContainerLeftAlignedS` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `appableTravelContainerRightAligned` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `APPLY_CUSTOM_DENOMINATION_FORM_CON` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `aPermissionOnboardingLocalStorageK` | medium |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `aptureTooltipOnboardingLocalStorag` | medium |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f49027c3-2979-4775-b0f9-d5a9bacd8e97` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `603d29f6-40c4-4453-904e-0484099bca90` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `39d5e258-647b-45fc-937c-4613b08ebbf0` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `daee1dbb-6ee1-4f64-8bf7-72f1fa48c68f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2d824eca-d95d-4dd4-bd0d-1cdd02f651ff` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2b122c28-4cef-490b-a251-41e0176c977a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `77b35dc2-9755-470d-b2c3-327cae345ee6` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `fee006c5-57dd-4880-ac23-c11af6410b01` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `778ef6b8-125a-476d-8203-a5f7da499171` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ef6a81a2-ffd7-4c3f-9f80-9a7b24843ac0` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `791ca7d0-172e-4980-ae1e-5bc2f4143b98` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `62f36a1e-caf6-4433-a848-2adb7e164a4d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d775ea02-5588-4cda-95ad-1ae03bb67e17` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6aac14d0-6e45-49f3-8a70-88d06d3e7bdc` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `06c1b347-66e0-4fbd-9bbf-923aff2a0577` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5bbabbf4-4c7e-42cd-93af-421822916848` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `31ce3aa7-f914-4ada-88be-d4fb33dc5db9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e364d9fe-1225-4814-bfee-2c461bf1c442` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7f9d1b18-2200-4ef3-bc9a-a77faa28d7e0` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2a89dca4-875e-43a7-a32e-8ce4ed6c38f1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `64971da7-5103-46da-b81f-4142c6d795ff` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a986d51e-f89f-408e-9999-2f491453e872` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a7e5d7bd-105f-4ff5-9a1a-bcc95db63593` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `97b5ed63-c3e0-4ab6-b1b0-b67b14146c01` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1f65e166-cfd9-4993-8964-d440b4b5f644` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `046495cc-c0f7-46dd-99ef-a63f8833e4c8` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d3abe488-5038-4eb4-b5b1-33e15b3df423` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9beec475-31e4-4788-a0e3-e2b3e10c6e88` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `27f413eb-3ca4-43d9-a919-d0e8538a2d6c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `824717fd-71e0-4f1b-b376-3a6f2e872f23` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `99c7924c-1785-470a-ba63-b415bcc6a0c9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0078d5d6-554b-4721-b796-a2d15bbb172b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `47a85b97-4647-455c-9ac9-63137d1c76ee` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1dbce533-a399-42b0-a24f-74c14c9e3f85` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e6d061eb-f510-41a1-89da-57cec5098707` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ea699eff-41fa-4b36-b5fc-428db8599b6d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `887c5ebb-4ff0-4e81-a93b-ae1ee4c55865` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7613234b-a7a3-47ef-832b-314be97a6603` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e99cecca-1bae-453e-8eca-08fb154d5cf9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7c0ab296-0784-44d3-be1b-7aaa4c36d990` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7020b0cb-158b-4a71-96b1-b9534d04499b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7b036604-c843-4bb5-af27-7c675bf60f67` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8a904dd1-92bb-48cf-84e6-d8794993a194` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `fe371a70-e315-49f9-a63b-1358a8d02787` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5b353419-e40e-4856-88ac-e3c213f996a0` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c78de6b7-ce2e-4279-bc4a-3b75f54d6f15` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `604d7438-166d-4674-b54a-329f9fe014ac` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ab35ec69-c0e2-427f-9b78-59e2aa3208e1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d3747c2f-19f1-4d15-a137-466d1bad6978` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `117c27e3-90db-4819-a0c3-dd753e7ae12c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `915bfb60-9074-41aa-a8cc-928996d11800` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `85659d2c-d09c-409c-bb09-f0a650de6d8e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6f8e76d9-c07f-46db-9de9-e562c4cad456` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `863987ce-e2bd-45d9-ad2a-f3b45883dc93` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5b37f089-afbf-4de4-b4db-b05a21ae5b1d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1948342e-af71-4997-8f1a-028da2ce712d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e98cfe30-91fb-4d75-967d-0d5eee44b952` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a76dff7e-d644-455c-9bb1-76ab974c4c5e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8b2c1cd2-f8e5-4cd0-ba35-66059de1f7d5` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c7954921-8021-417d-8cbc-838315527b53` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `392122cd-1ada-4571-8bf8-3d81352688dd` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `b9b6b480-aa33-412f-8c48-2a9049a16b17` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `bd064927-22ee-4b7b-82db-3bf4c6270184` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ad481e85-188d-45e5-bcb2-e00b732885b8` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e383eca4-a4f2-4dcb-824d-d5b27a35e22b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ca99011a-0436-4c4c-a3e6-3a5d6ef01f75` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9f870a08-4cf9-45bd-ac99-1428d6153ac5` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `b18677f9-63d3-4fb8-ad6b-3e95dd8c0847` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7b8629b4-cb5a-45b8-8ef0-b3a5022212b6` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8ae8f380-ff40-40fd-b23c-983a9ece4790` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `43d68a30-c775-4189-93b8-d7a2b86f5662` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `fa6a64d3-c203-45b3-be24-e69b1fb3922f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c0ebbf76-9996-4048-9e3b-298eab3b0c33` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `399d6027-12af-4bf8-b2ab-35eddfae9243` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7a53e413-7813-41a7-95d3-de4af5ffde6c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4fbc8a72-5b72-4521-b1df-4a5f29650c8c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `87fb8c17-a1d5-4068-86aa-2fb508e1bafa` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `bf0a9db7-c166-48b9-897d-8a73e5922709` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6a537674-af11-4e4c-ac0a-37c7d555d9eb` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `621206fd-10bc-4004-9de4-440e3905fe6d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `93b6ade0-317a-49a4-aece-fcf9818d610d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2c3684ce-966a-43b1-b93b-35d288875e8e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `b05dc6a8-7e45-48ef-8f27-482e3a02bd67` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0049b8f4-06f2-4488-93e1-f64f194b6415` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ebfda897-cecd-4fca-92ce-fcde1bca339d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `fc5b5d39-5697-4dfa-aa06-7b114effba7d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `cd6b5323-f958-4068-aeec-d54ce3b01b1b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9eefe6e3-f92d-43f9-b87c-347f022f5150` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `960920fc-dc9c-4681-a5b1-e2d6d7e67f47` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `bd67745e-d9c6-40af-b186-ef3f357bfa27` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `74b547bf-45f1-4e92-9915-5a44c87db20b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f4571e25-faea-4d25-b6b2-2fa80b0c0fe5` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d62c4972-483d-4f51-ac3c-e67f2ee94943` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9adf36a3-ef2c-4c09-8658-957d3e29bfde` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `14dd6ca3-f75d-4b00-976a-297c1f00f552` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3b3cf5e3-729f-43e5-b70e-d43531259788` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d36d4152-3f96-4e62-91a6-19e83080e87b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1cc22ed9-4d36-48f6-8ecb-aea5b1341708` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3cfb1844-82e2-4d7d-9c08-8dc365d7c48e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3fd8d55c-4390-4c35-90b1-938d61e7378d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d4290384-d847-42d4-bdfa-a11dcd5d708c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `568b6b98-cb63-4da6-aba3-519c454d73a7` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `72671f72-0a77-4e1e-ab36-93306753f8e2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e846cdc3-f803-404d-b0df-5da8c5b4418c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c4d74ffe-54e6-466f-ad73-5f627069cd55` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f626bb3a-30e7-4343-b687-6a7e71e5b50f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2329d0d7-fe1d-4ff4-b0b8-93344eaefcec` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c3e58cb7-8297-44be-9dba-eca6037be585` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0a12f57c-e5fd-46fd-afc2-bb97a90205a7` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a1768b86-5e87-4819-a7f4-bea043a685d8` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e3fae98e-8e69-4417-bbf0-895a91eae76a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `616b7aaf-9054-4490-9cfc-e89d8a36c6b5` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3ac0e89b-eb93-4d55-9b5a-4efe925a467e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a1a693fb-b382-4e1f-a820-71297130bc8e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1685caa0-e286-4f4e-95a8-6a6b77e9183e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7c2e7532-1637-4913-b569-95e54b0571ed` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d60e8bff-fbc8-4bed-b299-bfddaaa75b20` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `beb19156-518d-4110-bceb-9c24585e464c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3030b69a-b977-462b-b62e-eb2de32e96bc` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5295e08b-79e1-4bde-84ab-fade16e0219a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6713dcf1-182c-4217-9c1e-ab8fb70b84f9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0a362275-35a0-40e6-9118-f543cbe80b32` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `11198da1-796b-4cc3-8bee-c4d884b9b85b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9b9d35c7-6f63-4e02-b488-9f63ac52f8df` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5c8070e3-3a7a-4d4e-ab7a-876839f52cd8` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `abb0ce2b-7431-4d85-8d2a-fbb91d2c5778` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3b938f92-a261-4a33-8482-a16fda20789a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0b02bbf4-7ad4-4088-b1b3-d24f3761524b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5ef6a089-a602-4936-b726-c46eb04c482d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6e28357e-2153-4801-a491-3a56d5f907a9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `64d26270-f49b-4963-a9a3-5430e0c15df3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `35f169d5-346c-4db9-9c60-46655d58b6cf` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `30d070ac-329c-49a6-9ad7-beac3e6b7557` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `110e5c35-e5d1-44f4-8491-ba6da3daad87` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `908ec1b6-4b61-4536-bb77-35869356b9b3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6fc27f5c-4ea8-467f-8c32-07285164427a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `be2c2e00-c2df-4c0b-9828-ed134330650f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `96824684-aefa-4e5f-866e-1dff086bc17c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `91ab8379-ae86-4999-a60f-93e8711c1adb` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d76c1147-a22c-4ed7-88bc-9f1b56a9adb2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6f1daa0f-2139-4cde-a459-b711ce825923` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `70838a06-b9f2-40f9-8556-243a5bb348f6` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9cc16c80-3c3c-4b3a-a033-1c4e71194b47` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3e7edc03-086d-47f7-b723-494e301abd50` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9c5c9dec-4763-4e55-ab63-ae637fc522d2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `bfe76d2d-34d7-45ea-b668-bac2b8ab329d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f9541c2b-1139-4ae5-bae2-ddbbeb3efc23` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4b08c079-c396-494b-afdc-628fd321de0d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `08c3e554-ff1f-4adb-a9c0-815a1011feb2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `95708836-9ef3-45f1-af98-5c339a10e995` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d9bf0ac1-3fa1-4c71-a857-780e77a835ce` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4aebbd99-7478-411e-aced-265e7722d18d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7078c7e4-bf1e-4be8-9249-d0ad05425743` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5c6faebf-e9cf-44e9-aa98-df583617e480` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5af97bf6-710b-4428-b3ca-b011fd5e70a5` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2492636a-d2bb-42ae-8207-5b848a265b44` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `62ea89df-f552-4e59-a42e-acb0bbe61e6b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `51c238f7-59a8-42d4-9f78-6fba77ccc0f0` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5fad4706-b644-47e1-a19f-b7fbd5bbfc4b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3610ff95-fe39-4618-b83d-06fb1874eb00` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `497c8b8c-5f37-4a82-b3f7-f185de6194de` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e5d6f177-9700-426b-b663-c240a718a948` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `20def2a2-cc8e-4f84-9ffc-667d0ad6e19c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `65bc6c28-df86-4a04-adb1-5ede0dfcd305` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f860fe7a-5497-4e24-a679-364117902065` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `92198726-fb1c-4c57-8979-66290dc90e8d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6541eb4b-2fe8-4337-9381-8f99ab20e43b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a958dd4a-4edb-4673-a89f-3d1baa3c8bd5` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3d7c0499-e9ac-40c0-8b67-35da1be1f493` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `891191b4-862f-46c8-bbd5-9cc62e8a6cde` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `32676f41-0be8-4c1a-906b-9426b04108d6` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c02dc211-a659-49ab-83c2-3b9b47b40120` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `14ee4679-024a-4748-bb04-0d3a378c09b4` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2995ef5c-179f-4453-b73b-bafd6e641613` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7a25825f-e698-4b43-b7c9-49d3fb0b9d2a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `bb6eb39b-7894-4c1a-9c2e-659a88cd03e1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2c9a6b23-a4c5-4ffc-a082-9bdba501f02c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `87bc97d5-58c3-47c0-b905-f1576530590e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8cc36ff8-d34f-4186-8488-da3e1e35acc2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `059c3a65-e36f-48ba-ac27-3746ad1b32b2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5e9da80a-9dee-4106-9dae-a33eab9a6d6d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f3c01241-2d07-4d5e-9bb4-2063d96cafa3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8b23fe68-dd7e-4fd9-90e9-a4e45e9abacf` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `470a25f0-7273-491f-926c-ff9607b8ed58` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `42d5b418-ccda-4a81-87e4-03fdf88edbad` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `03d44bb6-3be2-401b-8c5f-43c0c58236b0` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2d1b278c-178a-417e-a949-a995cb573d7c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6af1b0a2-4ce0-4438-b860-251aaccd5cde` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8ed853a3-2e5e-471a-a0c1-5008c581df92` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7ec95eec-a1c1-488b-ae51-81985d655805` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `cccd54d6-a425-408c-9080-e51248024177` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `644db540-0052-4b15-939e-66bfed6ca594` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a5fd2136-8a0d-4871-bedc-d8da35e4b52f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9195187c-b0f8-4c27-ad46-a70a76544412` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `97304d9e-bfb6-4ab0-a3c6-21ab9ac868db` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4567af16-1703-42e3-bf1c-72f9b98e2c70` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8e927c0f-533e-4d8a-9810-81fbd1a2b3dc` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `fced91a6-72ed-4c15-9ceb-e7a8f220659a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `cdd09a73-89b1-41ec-954d-7feedee3707f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `07fbc80c-243d-4720-9aad-b19fddef37a1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8be28dcb-b690-4fe8-83f8-0a28bf10c380` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `52f3d19f-e919-40d1-9673-7d0d1b8bff1d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `403d7552-46b4-42e6-99c3-9c7159bacb71` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6f3ca92e-db24-4649-894f-ed121cf50d97` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `75f3e7d6-f6b4-4ee1-b6c2-ae161b0ea942` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6dbc8235-a70e-4655-bb37-fb24d93abc04` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c4511eee-9f31-40fb-939c-a5b618d2329a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `99ed4b21-b364-48ab-a37f-24e72a5162d2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9f35c3c1-8965-4d90-a368-59913d1f1f5b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9c842ddf-7d0e-4985-9d76-39caca76c3db` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5636334d-fc70-4edc-9ea7-116292e75292` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6970f3e0-d948-4bb1-b885-463cd1cb24e4` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `667ff428-3bfa-4555-9428-b2e005452cf3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f9f7000d-4b40-4b19-bfcf-fc0b01682cf1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9ec7b819-a5c1-4e51-b2f2-36bde0ae2ce4` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `30a383c6-f0e9-4567-91bc-e616f1685d05` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5cff7b07-a976-404b-b7e3-4648c5246660` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `23192c90-5209-4817-8e3e-9b47abe40458` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `17aa4313-7136-40e7-864d-35aa54d03abb` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3a392fd0-0a11-4135-b24a-837ae11740ff` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `113ae9f5-a7d4-4e31-aee6-10d4f9f8d9ba` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4c480ac8-c9d9-4684-8f74-65eacdc7369f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `aff11183-41bf-4ef7-8c53-d980673222ef` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f34a3dad-bc36-400d-9447-573895697369` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1adef358-8c22-4705-b19d-9b58ac49d29e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f58fdf1d-52f1-4170-a5cd-957a25fff130` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e6301e2e-2076-4e63-a8e1-b4d68faca09c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9c55320e-7431-4f60-b0de-ba4bd5f2ef4e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `37c34a02-52f3-42b8-aaeb-14df4ef63703` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0a7052ef-8498-45e4-9be3-c03d6c81bc7e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9575116a-3e65-4be1-a133-d85efce2703e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6d745b3d-f01a-41f0-acbd-a63a8826f131` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `527ad7ec-13ba-45e0-a5f4-57bc45bc6c1f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `876726a6-fc67-453e-b1b7-10e9e86dc859` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `84a12d57-8694-49f2-af58-203db6060d2e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `61002255-29bc-4e22-b4e3-a2811dc3923c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d1bb2b72-3810-4133-bf9f-757c2a341293` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `64e3fc9f-0af0-4409-ab37-db238f66ef4e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `75af1b52-79cf-4abc-a4a7-9a433c49c870` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4451abd2-be85-4fde-9db2-1ea769bdac99` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d7d1c8b4-bec6-480d-b02b-02085f5dff6f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `353029b7-66e4-4855-b233-291f01de0077` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2eacdb9b-5848-47e8-bd46-81054aac032e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3c01edb3-4d94-4594-ae1e-deaeb657a3a3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c33854c9-169c-441b-9a2a-c93865837eca` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7d0154eb-4909-4a82-80e1-c05520499b07` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `13df8c24-f721-45db-b74d-60f542298709` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ae34939f-9887-4d2a-8032-763fecf527d5` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `79e5ff63-49c3-41fe-bbfd-2c4a67dd8130` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `57279423-3ac4-46db-bb5c-6588124bfcde` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2bb1eff1-e7e6-4e9d-93a4-c6dffb2f5db9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f9944bc0-8520-48e3-9537-01dd74e0b261` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0e00a8bd-fa8e-4884-8564-714383b8384d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a0591867-fd5a-40f1-85ed-fe216d79690e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4b95e20f-53cf-454f-bb44-45c6f80ddedf` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `bbdd9444-aa25-46fa-baca-4745f9e83a89` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `830d1146-86c7-4882-8b49-9d5f2af8b7fd` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `14a49d37-ccdb-4672-83a6-1922a86c2cf8` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a6b47b88-f401-43da-9589-b9f89448f194` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `074a8362-6881-49d2-a412-12399d391c11` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3ffc21f2-c16e-47af-9623-93d3f8ae9fef` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `b67b563b-455c-46ac-9275-27b30c4b6fdb` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a1e6d0bf-7329-4c2d-bf4a-f16f106f150e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `dece98f9-ee08-428a-929d-280a231b9ddd` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4efd033e-d533-4551-9700-81ab8f47daf9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `b3624095-3423-4ea6-a849-f1217c1f7368` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `afa33081-fdc2-4dac-af42-7f99ff316372` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6a047cc3-001f-45e1-a898-ae1f36134155` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a14891b7-2389-4127-84cc-a544868103cf` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5d3ccb4d-f93b-4774-ba33-3748111a6cef` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `13191ecf-721f-42a5-9c87-b42c6eb4ba84` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `3c1b8b0f-d1c4-42de-abdd-0781ab197d40` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d8e595db-b507-4ae7-b7d9-a54b3fb603f1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8ce9fd5d-c653-43da-8a15-125036026fb1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8ba5db00-a0ab-4b82-a9c8-95a926a23e2f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d2439819-b1eb-4ea6-85d1-fd21e2af54c1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `464b86de-f76c-4692-80cc-64b103f47041` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `fd2c593c-ef9c-41f9-8f47-cae075c23876` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `59653a66-5317-444c-b4f2-eed3f82e5f03` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `cd4f3a0a-fedc-433f-a6ca-ebca93ffaa43` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e2ced37f-7535-41fe-a204-6eaedc579362` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `99b7f71c-86c6-4bc2-bb9c-07688a64d5d1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1a49989f-3941-4f9f-8d2e-7014343d872e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `de885a7e-0d4c-4501-b953-388e0fa41a3d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ce592b18-07e8-4502-aa07-56a4c6bbb74a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e8cde28f-493b-48d8-999a-394e3db33ee4` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `eaf5ecde-1727-4390-a93f-be3fa3c1ab64` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `86187cf1-d993-40ff-84e9-7d2da447249a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `77e89c5c-6baf-4bd5-9d1c-b3ac4a7a3155` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d09eafe7-4f26-4c52-8a99-c405604961fc` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ec23039c-09a1-43d7-8892-012ac76b92c3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `09546f58-b918-475c-974b-26c0ad1128af` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `cb913376-3bd6-45c9-b181-fefcd07a60fb` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c5cc216e-9b6e-4ff6-9d40-9a7bdc4de104` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `980262a9-66b7-4d58-9ee8-7b6701e2bffa` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `befefd1d-3d14-4588-a675-98e586f5a323` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `671835aa-f8cb-420f-b468-55032c55a099` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `fcf7afe9-14d8-4066-892a-fb4750a8ed2d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e074c109-e168-4fdc-8c13-043ee11f5ede` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `64ab2b02-68ab-4902-87b5-51a580e4db3a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0f48ce77-0129-4cbc-8256-a6ef16a9e374` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `344af97c-54e9-4a7b-99f6-b0b23cbfb35b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6d8f3bd8-cea2-4321-a6d7-7a23ce4bfde6` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f6cbb472-5f94-4d61-bd56-6a4dd12039a3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a7e35180-836b-4b06-a4d0-dd4cffeaec35` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `944dc8ff-8394-44f2-bfb3-17c2cf432cdf` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `b0a60d17-dfe7-4613-953a-443cdbfea0f3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9d5fea6e-6f5f-42b2-9a5e-d89a0bdc92f2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ceffb734-f57d-4d77-9111-49030ba01fd3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d640ceaa-6b7a-46ec-b2a6-8510935b21bb` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `5cfbbc96-9e9b-4362-99c0-5134fed729a1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6ead2c54-c163-43d4-9ef3-d84b5ee2d1c2` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `71030cf8-4365-4e49-b0a3-63d164703e1a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d39fa7d7-dc75-4934-9667-4633cddeb584` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1747271c-fa1d-45d0-a258-64183e4ea435` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `17aaf058-5b8a-4d1c-b59d-dbf122be1b60` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `b72f7e87-fd30-4a72-84b3-c7481bdb88f4` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `dd537472-6514-413f-90d6-207b36a058be` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `08e94e7e-cf2a-427f-aba0-152cbe99e039` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `24842722-5d50-4dc0-930e-bc64a45303ef` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `945444fa-8af9-4513-925a-f4aa6912acdd` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `68882214-bab4-4794-85f7-35c12475e513` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `957ea400-b9db-4885-8f93-55896d0607f1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ee4ca1d7-aee9-440b-8d1c-0cd5915d3e14` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `22bc0644-aed7-4378-8c3a-c34fa2ebbb44` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `038b169b-858e-46f7-9d73-16441b1ae1de` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4321a208-596a-4708-bb95-ff6c19bd01fe` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4f314901-3e0b-4824-abba-8e6bf6609dd9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `39e836bd-efeb-4a77-9a8d-04c09a276582` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9d7e93e6-0e34-4840-acbf-8c28afcc996f` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `21ba93d2-8243-45ad-835c-7914a4066224` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `79417140-c610-452d-88ec-9c80ef99c3bb` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2a4ee0ad-1fef-421a-ba9c-d1b7bae10a41` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `38165ef1-3176-4eb5-b85b-a30e37b585dd` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `05048745-9594-48d6-9714-492f657ff7e9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `db04deb2-04f6-4d70-ba14-02f67a594132` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c87ccdd8-1db1-4380-b237-c911c521f569` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c84990ef-45b2-4d9d-b263-92688d9bff6c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f619fbf1-81ea-4319-a059-af0ad6921cb9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `702be889-270b-4671-bfb8-2bd53f91477d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `bf2106c3-5090-4c18-b9e9-1c3b48fa8a40` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ab210749-2edf-4b06-933d-e3d0cf83cefc` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `c290ab0a-8577-4f5d-bd01-dc1ffa578a3d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `64b34d19-8493-46fd-af26-e86bfa8c5f98` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d8a6bab3-7c1d-46a9-8e7a-e4dfff1df588` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ca4d660f-42ac-4ff6-891d-d2d8b855c738` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e4033c16-c938-4e93-9024-6b86c391c440` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `94409b97-cd1d-4841-a66f-d3c8999a72e9` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `0645b289-ecd0-435d-b3e7-e778f573ce12` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `64ae6f12-54d2-40c0-9364-6f14cfd3735d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `15d473cf-371b-4d14-8752-079148b498e3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4ed3180f-8687-47e2-a73e-2c7dcbbebee4` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a72b6403-9a02-41f8-b683-a78d9f54a61e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `83850fa6-44f6-42f8-a28b-8bdb524c103a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `e2f0abe7-aa4d-4812-ab19-861d9be1709e` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `cdf5fab2-eea0-4e06-b797-0a3294f3ce2b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `9f1eafc4-3691-451c-8a15-d4f8cfb54534` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1aecc14a-5b27-48c1-b3fb-9a46081f82c0` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `4173f777-0dea-49db-9a9b-55aee7960909` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `83a71bb5-066f-42fb-812b-3c6485f71149` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `23933ce8-03f3-44a5-8fa3-4fbe71cbd1a1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `434ecfad-45d5-4cb4-be9a-dc2efda0ceb7` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `f75ce7f7-5d19-4897-95d6-6c12b1afb8fd` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `deda450e-42c3-44df-86eb-54028164201b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `6e11fcb9-81a8-4afe-882a-492375048fa6` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8cda3a82-a4b0-4cb2-bf6c-a55582472959` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `d910301d-805c-4c9e-91a4-71eb84aeab39` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `671268ee-df53-4368-9a1d-692df2ff0337` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `1f576ee9-2e62-40b6-9a5c-928c9a590540` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `86fea128-e979-4571-9101-1a0a3e9e02fb` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a9ed6dfa-46a1-4c4f-abb5-ea7304531a39` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `620ddc9e-61dd-40b6-adff-58af67c6c622` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `79ca98ef-fefd-4033-b88b-052a08cc79f4` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8ac32fe8-f2d4-47fc-a498-5ee2a6965313` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a2b676d2-a1a6-48a1-a2c2-33b806945bba` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `ca9c7c7e-f902-4234-99e8-2886dc71496a` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `bce1982a-bbe1-49ef-b893-f6bdcb040eea` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2d67caf9-76d6-42df-82cc-64a2da744e49` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `2c46027a-a3a3-4e15-8078-b3c5eaaa6ac1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `a5aa5028-8ccb-4d1c-ba0c-a2c696b6f42d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `7899b848-a018-4f1d-884d-ecb0b2c11b96` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `8d05cd5c-8f1b-4c26-80af-e3141cbfdaa1` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `afdd3758-9cfb-4860-bf97-691db72cb48c` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `b7ae5803-3539-4589-8b39-0562b9a3d28b` | high |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password",5:"Connection` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password="REDACTED"),this._trace("Client.connect",…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password:a,cleanSession:o,keepAliveInterval:s}=e,l…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password:a,mqttVersion:n,willMessage:i,keepAliveIn…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password:t,willMessage:i,timeout:n=3e4,keepAliveIn…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password:t,willMessage:i,timeout:n,keepAliveInterv…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password"]));if(i){if(!(i` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password:t,willMessage:i\|\|null,timeout:n,keepAlive…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `PASSWORD="PASSWORD",e.NUMBER="NUMBER",e.SECURE_NUM…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `PASSWORD="PASSWORD",e.NUMBER="NUMBER",e.SECURE_NUM…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `PASSWORD="AUTH_INPUT_PASSWORD",e.AUTH_INPUT_OTP="A…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password","email","family-name","gender","given-na…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/MultiWidgetpage.js` | `password="",A.auth&&(h=A.auth.split(":"),A.usernam…` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgZml` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGg` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2x` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Q` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aAo` | medium |
| **HIGH** | Basic Auth Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `BASIC_DETAIL=` | high |
| **HIGH** | Basic Auth Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `BASIC_DETAIL` | high |
| **HIGH** | Basic Auth Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `BASIC_FORM_DATA_WIDGET=` | high |
| **HIGH** | Basic Auth Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `BASIC_FORM_DATA_WIDGET` | high |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `Api Error` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `ApiErrorEvent` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `API_TIMEOUT` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `apiEndpoint` | medium |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `aCBkPSJNNC41IDYuMjVIMjAuNSIgc3Ryb2` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `aCBkPSJNNC41IDE3Ljc1SDIwLjUiIHN0cm` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `aCBkPSJNMTAuNSA0LjVIMTMuNSIgc3Ryb2` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `aCBpZD0iY2xpcDBfMTE1NzBfODc5OTgiPg` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `acFlcCogjGvBYMNTp4GytVvfWKtCI8zBud` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `aCBkPSJNMTMuNTQzNiAxMC42MTc5TDIwLj` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `aCBkPSJNMjkuNjg0IDMwLjgyN0gzMy4wOT` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `aCBkPSJNMTEgMTBDMTEgOC4zNDMxIDEyLj` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `aCBkPSJNMTQgMTFDMTQuNTUyMyAxMSAxNS` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `ackEventWithModifiedNavigationCont` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `ACTA_AddtoCartError_ParentOOS_Chil` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `ACQUISITION_PAYLATER_NON_ADOPTER_W` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `ACQUISITION_CBC_NON_ADOPTER_WIDGET` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `ACQUISITION_PAYLATER_ADOPTER_WIDGE` | high |
| **MEDIUM** | Twilio App SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `ApIj4KPHBhdGggZD0iTTE4IDdWNC45MjMw` | medium |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `4a815cb2-29f5-4c5b-a5af-a9278feb1a1b` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `c1c2c887-ba6f-4346-9bac-fd98e208bb03` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `2ad891cf-64df-4873-a27d-2a352a36c4e3` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `321e89f8-9ffa-47a7-a9d4-731da9bde6c4` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `8299eae5-6d05-44cf-81ab-8de20c42f8ea` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `a9d93c52-874b-436b-80c3-fa162a5ab052` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `0d9cf50d-0234-41ab-a740-fb3367937859` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `14327ea8-fd2b-42b3-bfae-2beaf5eb687d` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `ff7afb2c-d34d-416d-adf1-3127a1057aef` | high |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/CrossPlatformModules.js` | `PASSWORD="AUTH_INPUT_PASSWORD",e.AUTH_INPUT_OTP="A…` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/OVHomePageTS.js` | `API_ACTION` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/OVHomePageTS.js` | `API_FAILED` | medium |
| **HIGH** | API Token / Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/OVHomePageTS.js` | `API_FAILURE` | medium |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/OVHomePageTS.js` | `ackDiscoveryContentEngagementEvent` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/OVHomePageTS.js` | `actSwatchPillColorsToDrawWithColor` | high |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/OVHomePageTS.js` | `ACKGROUNDBOLD_BRANDPRIMARY_EMPHASI` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/OVHomePageTS.js` | `c9db80b9-c9b0-40f2-925e-e94fc956b273` | high |
| **CRITICAL** | Heroku API Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/OVHomePageTS.js` | `cc200d5d-6f40-4ed7-9431-fe0806c18025` | high |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/DesktopComponents.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGg` | medium |
| **LOW** | Google Captcha Key | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/DesktopComponents.js` | `6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2x` | medium |
| **HIGH** | Twilio Account SID | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/DesktopComponents.js` | `aCBkPSJNMTMuNTQzNiAxMC42MTc5TDIwLj` | high |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/DesktopComponents.js` | `pwd:{value:"Login:{@loginId}_Empty_Password",custo…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/DesktopComponents.js` | `Password"},login_success:{value:"Login:{@loginId}_…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/DesktopComponents.js` | `pwd_success:{value:"Login:Forgot_Password_{@loginI…` | medium |
| **HIGH** | Hardcoded Credentials | `https://static-assets-web.flixcart.com/batman-returns/batman-returns/p/81c7ef61138b70808f9540bfce756244/DesktopComponents.js` | `password:{value:"Login:Forgot_Password_{@loginId}_…` | medium |