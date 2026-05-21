# Ukraine [UA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior 2026-05-17, 2026-05-13)

## Status: YES — multiple commercial NTRIP casters operational; war conditions affect eastern infrastructure; no free government tier; no Centipede / no rtk2go presence worth using

There is no free national government RTK caster in Ukraine. The pre-war "UA-EUPOS" framework (Ukraine's planned contribution to the pan-European EUPOS standard, alongside Poland's ASG-EUPOS and Slovakia's SKPOS) was never consolidated into a unified public service; in practice the ecosystem is dominated by competing commercial operators. Coverage in Kharkiv, Zaporizhzhia, Donetsk, Kherson, Crimea, and Luhansk oblasts is degraded or absent due to occupation, infrastructure damage, jamming and active spoofing.

**Operational commercial casters as of 2026-05-21** (curl-confirmed alive where externally reachable):

- **System.NET** (`gnss.org.ua:2101`) — Leica GNSS Spider 7.11.1.109; 120+ stations (operator/reseller) to 200+ (country-survey aggregate); the largest network — alive (SOURCETABLE 200 OK 2026-05-21; 4 public MPs, 366 bytes — unchanged)
- **Kyivstar mAgri.RTK** (`rtk.kyivstar.ua:2101`) — Trimble Pivot Caster 5.2; ~97 stations; sourcetable includes MSK_xx per-oblast Soviet-legacy frames + UCS2000_4z..7z + CS63_1..6 + ITRF2020 — alive (SOURCETABLE 200 OK 2026-05-21; 18,072 bytes; +130 bytes vs 2026-05-17 — minor mountpoint/comment change, mountpoint set effectively unchanged)
- **RTK HUB** (TNT-TPI; `rtkhub.com`, endpoint disclosed post-registration) — Topcon — alive (catalog reachable 2026-05-21; tariffs unchanged)
- **ZAKPOS** (Закарпатгеодезцентр; western Ukraine) — externally unreachable from sandbox 2026-05-21; web portal still online
- **gnss-rtk.com** — separate Dnipro-based operator, claims 275 stations; not externally probable as NTRIP from sandbox; portal home page reachable 2026-05-21 with unchanged 275 / 410-user counters

Defunct: **NGCNET** (former `www.ngcnet.com.ua`) — domain repurposed to a casino site; service treated as defunct.
Reseller-only / not an independent caster: **NGC (ngc.com.ua)** — Kharkiv/Kyiv distributor that now resells SystemNET / System.NET; no separate NGCNET caster.

---

## Service A: System.NET / gnss.org.ua (PAID — largest UA network)

| Field | Value |
|---|---|
| **Operator** | Системи Солюшнс (Systems Solutions LLC); Swiss-Ukrainian joint venture; Leica Geosystems GNSS Spider platform |
| **landing_url** | `https://gnss.org.ua` — operator-owned network portal (Leica Spider Business Center; root page is a login wall with limited description but is the canonical network face — station map at `/User/SiteMap/SiteMapPublic` is openly browsable). Alternative operator corporate site: `https://systemnet.com.ua` (Kyiv office address; thin landing). |
| **access_url** | `https://gpsgeometer.com/en/products/gnss-rtk-network-subscription-plan-for-geodesy-1-year` — authorised reseller product page (EN) with full tariff, registration path. More descriptive than the Leica login portal for a target user. Not operator-owned but most-official EN signup channel. |
| **host:port** | `gnss.org.ua:2101` (IP `91.239.233.25`) |
| **Sourcetable confirmed** | 2026-05-07: SOURCETABLE 200 OK; Server `GNSS Spider 7.11.1.109/1.0`; Content-Length 366 bytes (small public sourcetable; production mountpoints behind authentication) |
| **Mountpoints (public sourcetable)** | `autom`, `nearest`, `imax`, `vrs` (vrs is GPS+GLO+GAL+BDS) |
| **VRS** | Yes — `vrs` mountpoint (Leica VRS) plus i-Max (`imax`) |
| **Stations** | 120+ (per gpsgeometer reseller) to 200+ (per country-survey aggregate) reference stations across Ukraine; station map at https://gnss.org.ua/User/SiteMap/SiteMapPublic |
| **tariff (geodesy, 1 yr)** | **UAH 19,000** (~USD 460 at 41.5 UAH/USD); discounted from list ~UAH 19,900. VAT inclusive (Ukrainian retail listings are TTC). Date observed: 2026-05-07. Source: https://gpsgeometer.com/en/products/gnss-rtk-network-subscription-plan-for-geodesy-1-year |
| **tariff (agro, 1 yr)** | **UAH 19,200** (agriculture variant, geared to tractor RTK; same network, separate SKU). Source: https://gpsgeometer.com/en/products/agro-rtk-gnss-network-subscription-plan-1-year |
| **tariff (other terms)** | Geodesy: 1-month, 3-month, 6-month options at proportional rates; reseller (gpsgeometer / shop.gpsgeometer.com) is a listed channel. |
| **VAT** | Ukrainian standard VAT 20%; reseller list prices are inclusive (retail "ціна з ПДВ"). |
| **hobbyist_eligibility** | **Yes** — purchase via online shop without licence; account registration on gnss.org.ua portal required to receive credentials |
| **legal_residency_required** | **Unclear** — Ukrainian-incorporated reseller; foreign card payment not explicitly supported; expect friction for non-UA buyers under wartime banking restrictions |
| **last_confirmed_alive** | `gnss.org.ua:2101` SOURCETABLE 200 OK 2026-05-21 (4 mountpoints; Leica GNSS Spider 7.11.1.109; 366 bytes; byte-identical to 2026-05-13) |
| **datum_epoch** | omitted -- no citable operator declaration on gnss.org.ua landing/login (production frame likely USC-2000 / SK-63 / ITRF but not declared in public-facing pages) |

---

## Service B: Kyivstar mAgri.RTK (PAID — telecom-distributed, Trimble Pivot)

| Field | Value |
|---|---|
| **Operator** | Kyivstar (Ukraine's largest mobile operator; majority Veon-owned), in partnership with Trimble |
| **host:port** | `rtk.kyivstar.ua:2101` (IP `81.23.16.137`) |
| **Sourcetable confirmed** | 2026-05-07: SOURCETABLE 200 OK; Server `NTRIP Trimble Ntrip Caster 5.2`; Content-Length 17,942 bytes; 25+ mountpoints |
| **Mountpoints** | `VRS` (RTCM3Net, GPS+GLO+GAL+BDS+QZS), `VRS_old` (RTCM 3.1, GPS+GLO), `Nearest_MSM5`, `Nearest_MSM7`, `Nearest` (RTCM 3.4 MSM4), `UCS2000_5z`, `UCS2000_6z` (Ukrainian state coordinate system 2000), and a `MSK_xx` family for the regional Soviet-legacy MSK coordinate systems by oblast (`MSK_05`, `_07`, `_12`, `_14`, `_18`, `_21`, `_23`, `_26`, `_35`, `_46`, `_48`, `_51`, `_53`, `_56`, `_59`, `_61`, `_80`). The MSK mountpoints output corrections in the per-oblast Soviet reference frames — convenient for legacy cadastral work. |
| **VRS** | Yes — `VRS` (RTCM3 MSM, full GNSS) and `Nearest_MSM5/7` |
| **Stations** | 97 RTK base stations (Trimble equipment); 24/7 NOC monitoring; xFill Premium for short-term signal continuity during outages |
| **tariff — GEO 365 (annual)** | **UAH 17,700/yr** (~USD 425 at 41.5 UAH/USD) |
| **tariff — GEO 730 (2 yr)** | **UAH 31,968** (kyivstar.ua/business 2026-05-13) |
| **tariff — GEO 90 (quarterly)** | **UAH 10,200/90 days** (kyivstar.ua/business 2026-05-13) |
| **tariff — GEO 30 (monthly)** | **UAH 5,550/30 days** |
| **tariff — GEO 7 (weekly)** | **UAH 1,800/7 days** |
| **tariff — GEO 1 (daily)** | **UAH 450/day** |
| **tariff — Try&Buy** | **UAH 2** for 7-day trial |
| **tariff — mAgri.RTK 365 StarLink** | Annual subscription bundling Starlink connectivity for low-coverage areas (premium tier, sold via gpsgeometer; price not transparently listed 2026-05-07) |
| **VAT** | Ukrainian VAT 20% — Kyivstar pricing typically TTC for retail products; verify at checkout |
| **hobbyist_eligibility** | **Yes** for any Kyivstar contract subscriber; service is intended for B2B/agriculture but does not require a professional licence |
| **legal_residency_required** | **Unclear → effectively yes** — service expected to require a Kyivstar mobile contract (Ukrainian carrier); foreign customers without a UA mobile number will struggle to subscribe; wartime payment restrictions further complicate non-UA enrolment |
| **last_confirmed_alive** | `rtk.kyivstar.ua:2101` SOURCETABLE 200 OK 2026-05-21 (Trimble Pivot Caster 5.2; 18,072 bytes — +130 bytes vs 2026-05-17; mountpoint set effectively unchanged) |
| **datum_epoch** | omitted -- no citable operator declaration. The Kyivstar product page (https://kyivstar.ua/business/products/geodesiya) lists *output* coordinate systems available to the rover ("УСК-2000(МСК) СК-63, UTM, WGS84, Балтійська система висот 1977р.") but this is a transform-on-output menu, not an operator declaration of the network's underlying realisation/epoch. The `ITRF2020` mountpoint name implies an ITRF2020 stream but the specific epoch is not declared. |

---

## Service C: RTK HUB / TNT-TPI Network (PAID — cheapest national pricing; Topcon)

| Field | Value |
|---|---|
| **Operator** | TNT-TPI (Topcon distributor in Ukraine); brand `RTKHUB` |
| **landing_url** | `https://rtkhub.com/` — operator-owned brand landing; describes the network (RTK 1–2 cm accuracy, coverage, service modes). Not a bare login. Alternative: `https://tnt-tpi.com/brand/rtkhub` (distributor-side mirror). |
| **access_url** | `https://tnt-tpi.com/catalog/pidpiski-na-poslugi-rtk` — RTK subscription catalog with tariffs (1/7/30/90/180/365 days) and per-package terms. More useful than landing for someone deciding to register. |
| **host:port** | Not publicly published — disclosed post-registration; portal at https://rtkhub.com (also https://tnt-tpi.com/brand/rtkhub) |
| **Modes offered** | Network RTK (VRS), Nearest RTK, Station RTK; ~1–2 cm accuracy claim. (Operator catalog also lists a "DGPS RTK" tier — out of project scope per primer [scope] carrier=0 rule; mentioned for completeness only.) |
| **Stations** | Multiple base stations across Ukraine; coverage continuing to expand (recent additions in KMST/ORIH/VASL areas, per RTK HUB news Dec 2024–2025) |
| **tariff — 365 days** | **UAH 10,500/yr** (sale price; was UAH 15,000; UAH 4,500 discount applied) |
| **tariff — 180 days** | **UAH 6,300** (sale; was UAH 9,000) |
| **tariff — 90 days** | **UAH 4,650** |
| **tariff — 30 days** | **UAH 1,800** |
| **tariff — 7 days** | **UAH 600** |
| **tariff — 24 hours** | **UAH 210** |
| **tariff — Minute packages** | Pre-paid minute packs available for ad-hoc usage; see https://tnt-tpi.com/catalog/paketi-hvilin-poslugi-rtk |
| **VAT** | Ukrainian VAT 20% — listings are with VAT (retail "ціна з ПДВ"). Date observed: 2026-05-07. Source: https://tnt-tpi.com/catalog/pidpiski-na-poslugi-rtk |
| **hobbyist_eligibility** | **Yes** — sold via web shop; no licence requirement |
| **legal_residency_required** | **Unclear → likely yes** — UA shop, UAH-only retail; foreign buyers face friction |
| **last_confirmed_alive** | https://rtkhub.com + https://tnt-tpi.com catalog reachable 2026-05-21 (24h ₴210 → 365d ₴10,500 sale prices unchanged); rtkhub.com:2101 not a public NTRIP port (endpoint expected post-registration) |
| **datum_epoch** | omitted -- no operator declaration on rtkhub.com / tnt-tpi.com (RTCM3 / CMR formats stated; coordinate frame not stated) |

**Position:** RTK HUB is currently the **cheapest national RTK subscription in Ukraine** (UAH 10,500/yr ≈ USD 250 — roughly 60% the price of System.NET geodesy and Kyivstar GEO 365), with the most flexible short-term packages (24-hour day passes from UAH 210 ≈ USD 5). Trade-off: smaller station footprint than System.NET; endpoint not visible until after subscription.

---

## Service D: ZAKPOS (Закарпатгеодезцентр — paid; Zakarpattia / nationwide)

| Field | Value |
|---|---|
| **Operator** | ДП "Закарпатський науково-дослідний та проектний інститут землеустрою — Закарпатгеодезцентр" (state enterprise; Zakarpattia, far western Ukraine; HQ Mukachevo / Uzhhorod) |
| **host:port** | `zakpos.zakgeo.com.ua:2102` (IP `185.68.16.164:2102`) — primary RTCM 3.1/3.2; also documented (per rtk_inventory.md 2026-05-13, citing zakpos.zakgeo.com.ua): `:2131` (multi-constellation GPS+GLO+GAL+BDS), `:2100` (agri/drone), `:2999` (RTCM 3.1, Baltic 1977 vertical), `:3000` (RTCM 3.4, GPS+GLO+GAL+BDS+QZSS), `:3130` (individual bases, Baltic 1977), `:3131` (RTCM 3.4, EVRS); older reference `195.16.76.194:2102`. None of these ports responded from the sandbox (2026-05-13 to -21). |
| **access_url** | https://ua-pos.net — Leica Spider Business Center account portal for ZAKPOS; confirmed live 2026-05-21 (login + registration navigation, Ukrainian/English/German). zakpos.zakgeo.com.ua is the operator info site. |
| **Lineage** | Original UA-EUPOS-branded member; oldest of the Ukrainian commercial RTK networks |
| **Coverage** | Originally Zakarpattia-anchored, expanded to nationwide with VRS zones |
| **num_stations** | ? — operator portal exposed only via web shell; no public station count statement found. Country-survey aggregate references nationwide VRS zone deployment but does not quote a precise CORS count. |
| **Service modes** | RTK, VRS (zone-based). (Operator description also lists a DGNSS tier — out of project scope per primer [scope] carrier=0 rule; mentioned for completeness only.) |
| **tariff (wartime, 2025 reduced)** | **UAH 15,000/yr** (~USD 360) — reduced wartime tariff; service paused under martial law from Feb 2022, resumed April 2025 (per country-survey aggregation; date_added 2026-04-30) |
| **VAT** | Ukrainian VAT 20% (TTC retail listing convention) |
| **hobbyist_eligibility** | **Yes** — open subscription |
| **legal_residency_required** | **Unclear → likely yes** — Ukrainian state enterprise, UAH-only |
| **last_confirmed_alive** | NTRIP `:2102` did not return SOURCETABLE from sandbox on 2026-05-13, 2026-05-17, or 2026-05-21 (sustained timeout — IP allow-listing, intermittent uptime, or wartime air-raid pause likely). ua-pos.net account portal reachable 2026-05-21. Web portal at zakpos.zakgeo.com.ua reachable 2026-05-07; not re-checked since. Report **alive (web/portal) / unconfirmed (NTRIP from outside UA)** |

**Operational note:** ZAKPOS pauses during air-raid alerts. Even outside alerts the public NTRIP port has been intermittently unreachable from outside Ukraine. Account registration and management is at https://ua-pos.net (Leica Spider Business Center). Confirm service status with the operator before purchasing.

---

## Service E: gnss-rtk.com (Dnipro-based; claims largest UA station footprint)

| Field | Value |
|---|---|
| **Operator** | Operator at Slobozhanskyi Ave. 20, Dnipro; corporate name not disclosed on the home page; email info@geometer.com.ua; phone +380 50 842 6165 |
| **landing_url** | https://gnss-rtk.com — operator-owned homepage (not a bare login; describes service, station count, contact) |
| **access_url** | https://gnss-rtk.com — no self-serve registration flow found; contact via form at gnss-rtk.com or info@geometer.com.ua to initiate subscription |
| **host:port** | Not publicly published — distributed post-subscription |
| **num_stations** | 275 claimed by operator home page (2026-05-21, excluding occupied territories). Unverified — figure conflicts with competitor claims; treat as operator-self-reported. |
| **Stations claimed** | 275 base stations covering Ukraine (excluding occupied territories), 99% uptime, 410 active users (per gnss-rtk.com home page 2026-05-21). Independent verification not available. |
| **Service modes** | Geodetic (geodesy) and agricultural (agro) RTK corrections; unlimited access; single station + network solutions (Automax, I-Max, VRS); daily / weekly / monthly / quarterly / half-yearly / yearly subscription terms |
| **tariff — geodesy** | **UAH 350/day · UAH 1,350/week · UAH 3,000/month · UAH 7,700/3 months · UAH 10,500/6 months · UAH 19,000/year** (unlimited RTK; single-base + VRS/iMax/Automax). Source: https://gnss-rtk.com/geodetic-pricing.html, observed 2026-05-21 |
| **tariff — agro** | **UAH 4,400/month · UAH 9,600/3 months · UAH 15,500/6 months · UAH 19,200/year** (unlimited RTK). Source: https://gnss-rtk.com/agriculture-rtk-pricing.html, observed 2026-05-21 |
| **VAT** | Ukrainian VAT 20% — retail listings are TTC |
| **hobbyist_eligibility** | **Yes** — subscription available via contact; no licence requirement |
| **legal_residency_required** | **Unclear → likely yes** — UAH retail, UA-incorporated |
| **last_confirmed_alive** | https://gnss-rtk.com home page reachable 2026-05-21 (statistics unchanged: 275 stations / 410 users / "99%" uptime); tariff pages accessible without login 2026-05-21; NTRIP endpoint not externally probable without credentials |

**Note:** This is a separate operator from System.NET, Kyivstar, and RTK HUB; counts of "Ukrainian RTK networks" should treat it as a fourth commercial player. The 275-station figure (if accurate) would put it above System.NET's 200+ claim. Tariff pages are publicly accessible without login at gnss-rtk.com/geodetic-pricing.html and gnss-rtk.com/agriculture-rtk-pricing.html. No self-serve account registration form was found; subscription initiation requires contacting the operator (contact form on homepage, or info@geometer.com.ua).

---

## Defunct / Unconfirmed

- **NGCNET** (NGC Ltd) — pre-war Ukrainian RTK service. Domain `www.ngcnet.com.ua` now redirects to a casino site; treated as **defunct** as of 2026-05-07. The NGC Kharkiv company (`ngc.com.ua`, phones +38 057 728-22-50, +38 067 715-27-37) appears to have repositioned as a **reseller of System.NET** (sells SystemNET RTK subscriptions, RINEX, and equipment rental from offices in Kharkiv and Kyiv) — it is no longer an independent caster operator.
- **GeoTerrace** (Інститут геодезії, Lviv Polytechnic National University; https://geoterrace.lpnu.ua/) — operates the Lviv Polytechnic Permanent GNSS Stations network, but the public-facing services are **post-processing only** (RINEX downloads, coordinate transformation tools). No real-time public NTRIP RTK caster. Not an option for hobbyist real-time work.
- **State Permanent GNSS Network (СКНЗУ, Держгеокадастр)** — operates reference stations for geodetic control and post-processing; **no public NTRIP caster**.

---

## No free government NTRIP

There is no free national RTK service in Ukraine (a notable contrast with Poland's ASG-EUPOS, free since 2022-10-02). The State Geodetic Survey infrastructure (Держгеокадастр / СКНЗУ) is for post-processing and internal geodetic control only; no free public NTRIP stream.

## No volunteer footprint

- **Centipede:** **0 UA-coded mountpoints** on `crtk.net:2101` sourcetable (1,224 STR entries probed 2026-05-07; zero match `;UKR;`; re-check via `py scripts/stations_by_country.py UKR` source filter `centipede`).
- **rtk2go:** ~3 UA bases in stations.json (status uncertain; not a usable substitute for a national network).

The country survey instruction to skip rtk2go/Centipede applies fully here — neither is a meaningful option in Ukraine, and a self-hosted base station is often the only reliable answer in active-conflict regions.

---

## War-condition context

- Russia's full-scale invasion (since 2022-02-24) damaged or made inaccessible CORS infrastructure in Kharkiv, Zaporizhzhia, Donetsk, Kherson, and Luhansk oblasts; portions of Crimea were already inaccessible from 2014.
- All UA networks pause or reduce capacity during air-raid alerts.
- Front-line and rear-area GPS jamming and spoofing further degrade signal quality independent of caster availability — RTK fix may be impossible even when corrections are received.
- Western Ukraine (Lviv, Uzhhorod, Ivano-Frankivsk) and Kyivstar's nationwide coverage with xFill Premium are the most reliable in practice.
- UAH/USD reference: ~41–42 UAH/USD as of May 2026 (wartime rates volatile).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **System.NET RINEX** | https://gnss.org.ua | Via account; pricing unclear |
| **GeoTerrace (Lviv Polytechnic) RINEX** | https://geoterrace.lpnu.ua/ | Free (registration required) |
| **IGS/EPN stations in Ukraine** (limited) | https://www.epncb.oma.be/ | Free |

---

## Summary Table

| Service | host:port | Free? | VRS? | Annual price | Hobbyist | Last alive |
|---|---|---|---|---|---|---|
| System.NET | `gnss.org.ua:2101` | No | Yes | UAH 19,000 (geodesy) / 19,200 (agro) | Yes | 2026-05-21 ✓ |
| Kyivstar mAgri.RTK | `rtk.kyivstar.ua:2101` | No | Yes | UAH 17,700 (GEO 365) | Yes (Kyivstar contract) | 2026-05-21 ✓ |
| RTK HUB | (post-registration) | No | Yes | UAH 10,500 | Yes | 2026-05-21 (portal) |
| ZAKPOS | `zakpos.zakgeo.com.ua:2102` | No | Yes | UAH 15,000 (wartime reduced) | Yes | 2026-05-07 (web only; NTRIP timed out 2026-05-13 / -17 / -21) |
| gnss-rtk.com | (post-registration) | No | Yes | UAH 19,000/yr geodesy; 19,200/yr agro | Yes | 2026-05-21 (web + tariff pages) |
| NGCNET | n/a | — | — | — | — | Defunct (domain repurposed) |
| NGC (ngc.com.ua) | reseller only | n/a | n/a | resells System.NET | Yes via SystemNET | 2026-05-13 (reseller portal) |

---

## Sources Consulted
- System.NET / gnss.org.ua portal: https://gnss.org.ua (sourcetable confirmed 2026-05-07)
- System.NET station map: https://gnss.org.ua/User/SiteMap/SiteMapPublic
- System.NET reseller — geodesy 1-year: https://gpsgeometer.com/en/products/gnss-rtk-network-subscription-plan-for-geodesy-1-year
- System.NET reseller — agro 1-year: https://gpsgeometer.com/en/products/agro-rtk-gnss-network-subscription-plan-1-year
- Kyivstar mAgri.RTK product page: https://kyivstar.ua/business/products/geodesiya
- Kyivstar mAgri.RTK pricing (gpsgeometer / Starlink variant): https://gpsgeometer.com/en/products/magri.rtk-365-by-kyivstar-high-precision-signal-for-gnss-rtk-equipment-starlink
- Trimble × Kyivstar partnership: https://www.terradaily.com/reports/Trimble_and_Kyivstar_to_provide_GNSS_correction_services_in_Ukraine_999.html
- RTK HUB portal: https://rtkhub.com / https://tnt-tpi.com/brand/rtkhub
- RTK HUB subscriptions catalog: https://tnt-tpi.com/catalog/pidpiski-na-poslugi-rtk
- RTK HUB minute packs: https://tnt-tpi.com/catalog/paketi-hvilin-poslugi-rtk
- RTK HUB tariff change announcement: https://www.rtkhub.com/novyny/zmina-taryfikatsii-na-deiaki-posluhy-merezhi-tnt-tpi-network
- RTK HUB coverage expansion (KMST/ORIH/VASL): https://rtkhub.com/novyny/rozshyrennia-pokryttia-merezhi-kmst-orih-vasl
- ZAKPOS portal: http://zakpos.zakgeo.com.ua/
- Ukraine RTK network stability article: https://www.rtk-navigation.com/en/background-information/chi-pratsyuyut-ukrainski-ta-evropejski-rtk-merezhi-stabilno-po-vsij-teritorii-polya-chi-chasto-buvayut-rozrivi
- ArduSimple Ukraine: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-ukraine/
- GeoTerrace (post-processing only): https://geoterrace.lpnu.ua/
- curl probe of `gnss.org.ua:2101` — SOURCETABLE 200 OK 2026-05-21 (4 mountpoints; Leica GNSS Spider 7.11.1.109; 366 bytes; byte-identical to 2026-05-13)
- curl probe of `rtk.kyivstar.ua:2101` — SOURCETABLE 200 OK 2026-05-21 (Trimble Pivot Caster 5.2; 18,072 bytes; +130 bytes vs 2026-05-17)
- Kyivstar mAgri.RTK output frames (datum citation): https://kyivstar.ua/business/products/geodesiya — "УСК-2000(МСК) СК-63, UTM, WGS84, Балтійська система висот 1977р." (re-confirmed 2026-05-21)
- RTK HUB tariff catalog: https://tnt-tpi.com/catalog/pidpiski-na-poslugi-rtk — 2026-05-21 prices unchanged (24h ₴210, 7d ₴600, 30d ₴1,800, 90d ₴4,650, 180d ₴6,300, 365d ₴10,500)
- Kyivstar tariff page: https://kyivstar.ua/business/products/geodesiya — 2026-05-21 tariffs unchanged (GEO 1 ₴450 ... GEO 730 ₴31,968)
- gnss-rtk.com — home page reachable 2026-05-21; 275 stations / 410 users / 99% uptime claimed; email info@geometer.com.ua; phone +380 50 842 6165
- gnss-rtk.com geodetic tariff page: https://gnss-rtk.com/geodetic-pricing.html — fetched 2026-05-21 (no login required): UAH 350/day, 1350/week, 3000/month, 7700/3mo, 10500/6mo, 19000/year
- gnss-rtk.com agro tariff page: https://gnss-rtk.com/agriculture-rtk-pricing.html — fetched 2026-05-21 (no login required): UAH 4400/month, 9600/3mo, 15500/6mo, 19200/year
- ua-pos.net account portal (ZAKPOS): https://ua-pos.net — confirmed live 2026-05-21; login + registration navigation present
- ZAKPOS service portal: http://zakpos.zakgeo.com.ua — operator info site; last reachable 2026-05-07
