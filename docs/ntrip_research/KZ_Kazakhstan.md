# Kazakhstan [KZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06; expanded with national-operator + four commercial providers 2026-05-12

## Status: PARTIAL — national operator KGS runs an 86-station reference network with RTK + RINEX services, but no public NTRIP endpoint is published; access is contract-based via 4+ confirmed commercial resellers / private CORS operators

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | **Yes (contract-based, not open-access)** — national operator JSC NC "Қазақстан Ғарыш Сапары" (Kazakhstan Gharysh Sapary / KGS) provides RTK corrections from 86 reference stations; commercial entities (GeoComm, EFT, Geokurs/Trimble RTX, RTKNet, qgeo.kz) act as access/integration channels. No advertised free-tier or self-serve NTRIP endpoint. |
| **landing_url — NCGPI / KazGeoDesy** | `https://qazgeodesy.kz/` (HU/RU; EN at `/en/`) — official operator landing for RGP "National Centre of Geodesy and Spatial Information" (NCGPI) under the Committee of Geodesy and Cartography. Describes the RTK correcting-information service. Replaces previous `rtk.qgeo.kz` (degraded to near-empty header 2026-05-12) as the canonical landing. KGS corporate site `https://gharysh.kz/` covers the wider national space mandate. |
| **access_url — NCGPI / KazGeoDesy** | Skip — no public self-serve registration page exists; the historical tariff page at `rtk.qgeo.kz/tarifs` is no longer reachable, and access is sales-contact-only via NCGPI reception (+7 7172 27-27-75) or a reseller. The landing_url adequately surfaces this. |
| **host:port — KGS national** | Not publicly disclosed. Connection requires GNSS receiver + GPRS/4G modem + service contract via KGS or a reseller. The "Корректирующая Информация" page at `https://rtk.qgeo.kz/` is the most prominent public entry surface but contains only a logo and a link to instructions; sandbox observed the page as a near-empty header (2026-05-12). |
| **host:port — GeoComm** | Not published on the public site (geocomm.kz/bazovye-stanczii/). Access via direct contact: Anatoly +7 (771) 180-78-99 / saa@geocomm.kz · Karaganda, Moskovskaya 16/1. |
| **host:port — EFT** | Not published on eft.kz/base. Contact: +7 (727) 310 00 81 · info@eft.kz · Almaty. Free RINEX after registration; "continuous RTK corrections coverage across Kazakhstan" using EFT RS1 receivers (GPS+GLONASS+BeiDou+Galileo). |
| **host:port — Geokurs / Trimble RTX** | PPP / SSR via satellite (Trimble CenterPoint RTX) — **out of scope per project rule (PPP not RTK-NTRIP)** but documented for completeness. Distributor: bs.geokurs.kz; +7 727 229 00 00. 30-day free trial promo code `FREE30`. Annual subscription, KZT pricing on request. |
| **host:port — RTKNet (Geo Master A)** | Not published on southinstrument.kz/rtknet. ТОО "Гео Мастер А", Almaty. Sales-only page; no endpoint, mountpoint, or KZT pricing on public web. |
| **tariff** | **Unknown — all commercial** (KGS state network, GeoComm, EFT, RTKNet). All providers gate price disclosure behind a sales contact. Geokurs RTX (PPP, out of scope) advertises a 30-day free trial via code `FREE30`. |
| **hobbyist_eligibility** | Unclear — all four providers are oriented to surveyors / engineering firms; no individual / hobbyist tier was advertised. Nothing in the public material explicitly excludes individual buyers, but a Kazakh-language contract negotiation and bank-transfer payment workflow is the practical barrier. |
| **legal_residency_required** | Effectively yes — KZT bank transfer + Kazakh-language contract are the typical onboarding workflow. No formal residency bar published. |
| **last_confirmed_alive** | geocomm.kz/bazovye-stanczii/ HTTPS 200 (2026-05-12); eft.kz/base HTTPS 200 (2026-05-12); bs.geokurs.kz/rtx HTTPS 200 (2026-05-12); rtk.qgeo.kz HTTPS 200 (near-empty page; 2026-05-12); gharysh.kz HTTPS 200 (2026-05-12). No live sourcetable connection from sandbox. |

## Most Recent Project Announcement

**National RTK infrastructure — JSC NC "Қазақстан Ғарыш Сапары" (KGS / Kazakhstan Gharysh Sapary)** is the national operator of the high-precision satellite navigation system of the Republic of Kazakhstan. Per the company's own public-facing summary (cited by geocomm.kz and reproduced by 2gis.kz business directory and gharysh.kz): KGS owns **60 navigation stations** receiving GPS/GLONASS satellite signals with real-time corrections at metre- and centimetre-level accuracy. Under a separate state investment programme **86 reference stations** were installed; users can obtain RINEX for post-processing and RTK corrections through this network. Headquarters: Astana, Turan Avenue 89. No public NTRIP host:port has been disclosed; access is via service contract.

**Government decree:** Decree of the Government of the Republic of Kazakhstan RK №721 (31 May 2012) authorised the National Space Agency to provide RTK corrections; KGS is the operational descendant of that mandate.

**Commercial CORS / NTRIP layer:**
- **GeoComm LLP** (geocomm.kz; Karaganda HQ) — operates / advertises a private CORS network; price on contact. 24/7 service marketing.
- **EFT** (eft.kz/base; Almaty) — "modern infrastructure project" providing continuous RTK across Kazakhstan; EFT RS1 receivers; free RINEX post-registration.
- **Geokurs / Trimble RTX** (bs.geokurs.kz; Almaty) — satellite-delivered PPP-RTK; out of scope for this project but the most accessible centimetre-class option for foreigners (no in-country contract needed if buying RTX subscription directly from Trimble).
- **RTKNet (Гео Мастер А)** (southinstrument.kz/rtknet; Almaty) — equipment-distributor-operated network; no public endpoint.

## Context Notes

- **No free / open public NTRIP**: ArduSimple's Kazakhstan page (re-checked 2026-05-12) still states the country has no national RTK network — this is wrong if "national" includes contract-gated state RTK; correct in spirit if it means "open / free national tier". RTK2GO, IGS, and EarthScope are the suggested fallbacks.
- **KGS station count discrepancy**: KGS publishes both "60 navigation stations" and "86 reference stations" figures; these likely refer to the original 2012-era deployment vs. the expanded state-investment build-out. The 86-station figure is the one currently used in RINEX/RTK marketing.
- **Coverage**: 86 stations across 2.72 million km² yields ~180 km mean spacing — adequate for network-RTK in the populated north (Astana–Pavlodar–Karaganda) and southeast (Almaty), thinner in the western steppe and Caspian region. No public coverage map.
- **Free-tier alternatives**: RTK2GO has **1 base station in Kazakhstan** (`GerAndry` at 53.09 N / 77.44 E, near Pavlodar — confirmed in stations.json 2026-05-12). Coverage is point-only; rover must be within ~30–40 km. Galileo HAS provides ~40 cm globally with no contract. GEODNET / Onocoy: no Kazakhstan coverage confirmed.
- **PPP fallback for foreigners**: Trimble RTX via Geokurs / direct Trimble subscription is the most realistic centimetre-class option for non-resident hobbyists.
- **Searches in Kazakh/Russian**: queries on "Казахстан ГНСС НТРИП сеть", "Қазақстан Ғарыш Сапары RTK", "геодезия Казахстан реальное время" surfaced KGS + GeoComm + EFT + Geokurs + RTKNet + qgeo as the prominent providers, none with self-serve pricing.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — IGS stations in Kazakhstan (e.g., ARTI, ARTU, KIT3) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |
| **BKG NTRIP** — IGS real-time streams including Central Asian stations | https://igs.bkg.bund.de/ntrip/ | Free (account required) |

## Sources Consulted
- ArduSimple — RTK correction services and NTRIP Casters in Kazakhstan (re-checked 2026-05-12)
- **geocomm.kz/bazovye-stanczii/** — GeoComm base stations page; KGS 60-station + 86-station figures, contacts (HTTPS 200 2026-05-12)
- **eft.kz/base** — EFT base-station network landing page (HTTPS 200 2026-05-12)
- **bs.geokurs.kz/rtx** — Geokurs / Trimble CenterPoint RTX Kazakhstan landing (HTTPS 200 2026-05-12)
- **rtk.qgeo.kz** — "Корректирующая Информация" page (near-empty header; HTTPS 200 2026-05-12)
- **gharysh.kz** — JSC NC "Қазақстан Ғарыш Сапары" corporate page (HTTPS 200 2026-05-12)
- southinstrument.kz/rtknet — RTKNet reference page; operator ТОО "Гео Мастер А" (Almaty)
- 2gis.kz — KGS HQ address (Astana, Turan Avenue 89)
- GitHub mvarga1989 GNSS CORS RTK networks list
- Russian-language survey forums and trade press (gis2000.ru, vestnik-glonass.ru)
- RTK2go monitor / stations.json — **1 KZ rtk2go station confirmed: `GerAndry` 53.09 N / 77.44 E** (2026-05-12)
- NTRIP-list.com — no Kazakhstan entry confirmed
