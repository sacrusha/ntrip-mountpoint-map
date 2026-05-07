# Ukraine [UA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07 (refresh of 2026-05-06 entry)

## Status: YES — multiple commercial NTRIP casters operational; war conditions affect eastern infrastructure; no free government tier; no Centipede / no rtk2go presence worth using

There is no free national government RTK caster in Ukraine. The pre-war "UA-EUPOS" framework (Ukraine's planned contribution to the pan-European EUPOS standard, alongside Poland's ASG-EUPOS and Slovakia's SKPOS) was never consolidated into a unified public service; in practice the ecosystem is dominated by competing commercial operators. Coverage in Kharkiv, Zaporizhzhia, Donetsk, Kherson, Crimea, and Luhansk oblasts is degraded or absent due to occupation, infrastructure damage, jamming and active spoofing.

**Three operational commercial casters as of 2026-05-07** (curl-confirmed alive where externally reachable):

- **System.NET** (`gnss.org.ua:2101`) — Leica GNSS Spider; 200+ stations; the largest network — **alive ✓**
- **Kyivstar mAgri.RTK** (`rtk.kyivstar.ua:2101`) — Trimble Pivot Platform; ~97 stations — **alive ✓**
- **RTK HUB** (TNT-TPI; `rtkhub.com`, endpoint disclosed post-registration) — Topcon — **alive (catalog reachable 2026-05-07)**
- **ZAKPOS** (Закарпатгеодезцентр; western Ukraine) — externally unreachable from the test sandbox 2026-05-07; portal still online via web

Defunct: **NGCNET** — domain `www.ngcnet.com.ua` repurposed to a casino site; service treated as defunct as of 2026-05-07.

---

## Service A: System.NET / gnss.org.ua (PAID — largest UA network)

| Field | Value |
|---|---|
| **Operator** | Системи Солюшнс (Systems Solutions LLC); Swiss-Ukrainian joint venture; Leica Geosystems GNSS Spider platform |
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
| **last_confirmed_alive** | `gnss.org.ua:2101` SOURCETABLE 200 OK on 2026-05-07 (curl probe) |

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
| **tariff — GEO 30 (monthly)** | **UAH 5,550/30 days** |
| **tariff — GEO 7 (weekly)** | **UAH 1,800/7 days** |
| **tariff — GEO 1 (daily)** | **UAH 450/day** |
| **tariff — Try&Buy** | **UAH 2** for 7-day trial |
| **tariff — mAgri.RTK 365 StarLink** | Annual subscription bundling Starlink connectivity for low-coverage areas (premium tier, sold via gpsgeometer; price not transparently listed 2026-05-07) |
| **VAT** | Ukrainian VAT 20% — Kyivstar pricing typically TTC for retail products; verify at checkout |
| **hobbyist_eligibility** | **Yes** for any Kyivstar contract subscriber; service is intended for B2B/agriculture but does not require a professional licence |
| **legal_residency_required** | **Unclear → effectively yes** — service expected to require a Kyivstar mobile contract (Ukrainian carrier); foreign customers without a UA mobile number will struggle to subscribe; wartime payment restrictions further complicate non-UA enrolment |
| **last_confirmed_alive** | `rtk.kyivstar.ua:2101` SOURCETABLE 200 OK on 2026-05-07 (curl probe) |

---

## Service C: RTK HUB / TNT-TPI Network (PAID — cheapest national pricing; Topcon)

| Field | Value |
|---|---|
| **Operator** | TNT-TPI (Topcon distributor in Ukraine); brand `RTKHUB` |
| **host:port** | Not publicly published — disclosed post-registration; portal at https://rtkhub.com (also https://tnt-tpi.com/brand/rtkhub) |
| **Modes offered** | Network RTK (VRS), Nearest RTK, Station RTK, DGPS RTK; ~1–2 cm accuracy claim |
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
| **last_confirmed_alive** | https://rtkhub.com / https://tnt-tpi.com catalog reachable 2026-05-07; NTRIP endpoint not externally probable without credentials |

**Position:** RTK HUB is currently the **cheapest national RTK subscription in Ukraine** (UAH 10,500/yr ≈ USD 250 — roughly 60% the price of System.NET geodesy and Kyivstar GEO 365), with the most flexible short-term packages (24-hour day passes from UAH 210 ≈ USD 5). Trade-off: smaller station footprint than System.NET; endpoint not visible until after subscription.

---

## Service D: ZAKPOS (Закарпатгеодезцентр — paid; Zakarpattia / nationwide)

| Field | Value |
|---|---|
| **Operator** | ДП "Закарпатський науково-дослідний та проектний інститут землеустрою — Закарпатгеодезцентр" (state enterprise; Zakarpattia, far western Ukraine; HQ Mukachevo / Uzhhorod) |
| **host:port** | `zakpos.zakgeo.com.ua:2102` (IP `185.68.16.164:2102`) — primary; older country-survey reference `195.16.76.194:2102` |
| **Lineage** | Original UA-EUPOS-branded member; oldest of the Ukrainian commercial RTK networks |
| **Coverage** | Originally Zakarpattia-anchored, expanded to nationwide with VRS zones |
| **Service modes** | RTK, VRS (zone-based), DGNSS |
| **tariff (wartime, 2025 reduced)** | **UAH 15,000/yr** (~USD 360) — reduced wartime tariff; service paused under martial law from Feb 2022, resumed April 2025 (per country-survey aggregation; date_added 2026-04-30) |
| **VAT** | Ukrainian VAT 20% (TTC retail listing convention) |
| **hobbyist_eligibility** | **Yes** — open subscription |
| **legal_residency_required** | **Unclear → likely yes** — Ukrainian state enterprise, UAH-only |
| **last_confirmed_alive** | Web portal at http://zakpos.zakgeo.com.ua/ reachable 2026-05-07 (Joomla CMS, redirect-loop on some article URLs); NTRIP `:2102` and `:2101` did not return SOURCETABLE from the test sandbox on 2026-05-07 (timeout — could be IP allow-listing, intermittent uptime, or wartime air-raid pause). Report this as **alive (web) / unconfirmed (NTRIP)** |

**Operational note:** ZAKPOS pauses during air-raid alerts. Even outside alerts the public NTRIP port has been intermittently unreachable from outside Ukraine. Confirm with the operator before purchasing.

---

## Defunct / Unconfirmed

- **NGCNET** (NGC Ltd) — pre-war Ukrainian RTK service. Domain `www.ngcnet.com.ua` now redirects to a casino site; treated as **defunct** as of 2026-05-07. No replacement endpoint located.
- **GeoTerrace** (Інститут геодезії, Lviv Polytechnic National University; https://geoterrace.lpnu.ua/) — operates the Lviv Polytechnic Permanent GNSS Stations network, but the public-facing services are **post-processing only** (RINEX downloads, coordinate transformation tools). No real-time public NTRIP RTK caster. Not an option for hobbyist real-time work.
- **State Permanent GNSS Network (СКНЗУ, Держгеокадастр)** — operates reference stations for geodetic control and post-processing; **no public NTRIP caster**.

---

## No free government NTRIP

There is no free national RTK service in Ukraine (a notable contrast with Poland's ASG-EUPOS, free since 2022-10-02). The State Geodetic Survey infrastructure (Держгеокадастр / СКНЗУ) is for post-processing and internal geodetic control only; no free public NTRIP stream.

## No volunteer footprint

- **Centipede:** **0 UA-coded mountpoints** on `crtk.net:2101` sourcetable (1,224 STR entries probed 2026-05-07; zero match `;UKR;`).
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
| System.NET | `gnss.org.ua:2101` | No | Yes | UAH 19,000 (geodesy) / 19,200 (agro) | Yes | 2026-05-07 ✓ |
| Kyivstar mAgri.RTK | `rtk.kyivstar.ua:2101` | No | Yes | UAH 17,700 (GEO 365) | Yes (Kyivstar contract) | 2026-05-07 ✓ |
| RTK HUB | (post-registration) | No | Yes | UAH 10,500 | Yes | 2026-05-07 (portal) |
| ZAKPOS | `zakpos.zakgeo.com.ua:2102` | No | Yes | UAH 15,000 (wartime reduced) | Yes | 2026-05-07 (web only; NTRIP timed out) |
| NGCNET | n/a | — | — | — | — | Defunct (domain repurposed) |

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
- curl probe of `gnss.org.ua:2101` — SOURCETABLE 200 OK 2026-05-07 (4 mountpoints; Leica GNSS Spider 7.11.1.109)
- curl probe of `rtk.kyivstar.ua:2101` — SOURCETABLE 200 OK 2026-05-07 (25+ mountpoints; Trimble Ntrip Caster 5.2)
- curl probe of `crtk.net:2101` — 0 UA-coded mountpoints (1,224 STR entries; confirms zero Centipede UA presence)
- curl probe of `zakpos.zakgeo.com.ua:2102` and `:2101` — timeout from sandbox 2026-05-07 (NTRIP port not externally responsive); web portal reachable
- curl probe of `rtkhub.com:2101` — no response (endpoint expected post-registration; not a public NTRIP port)
