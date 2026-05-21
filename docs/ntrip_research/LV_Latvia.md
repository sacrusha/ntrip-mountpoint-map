# Latvia [LV] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior 2026-05-17, 2026-05-12)

## Status: YES — free government NTRIP caster (LatPos) operating; LKS-92 → LKS-2020 frame transition scheduled for 2026-10-01

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — LatPos, free of charge since 2018 |
| **landing_url** | https://www.lgia.gov.lv/lv/latpos — operator-owned LatPos info page on the LGIA agency site (LV; English page returned HTTP 404 on 2026-05-21). Describes the network, station counts, and access flow. |
| **access_url** | https://latpos.lgia.gov.lv/SBC/Account/Register — Leica Spider Business Center registration form; the LGIA landing instructs users to register there. No richer service-description page documents the signup workflow. |
| **host:port** | `latpos.lgia.gov.lv:5001` (IP 91.216.2.20) |
| **num_stations** | 36 base stations contributing to LatPos VRS — 27 in Latvia + 5 in Estonia + 4 in Lithuania (operator statement, lgia.gov.lv/lv/latpos) |
| **vrs** | Yes — 7 mountpoints exposed by the public sourcetable: `SITE` (nearest single base, GPS+GLO RTCM 3), `NETW-MAX` (master-auxiliary RTCM 3 GPS+GLO), `NETW-iMAX` (iMAX GPS+GLO), `VIRTUAL-RS` (VRS RTCM 3 extended GPS+GLO), `SITE-BeiDOU` (GPS+GLO+BDS), `NETW-iMAX-BeiDOU` (iMAX GPS+GLO+BDS), `VRS-BeiDOU` (VRS GPS+GLO+BDS) |
| **tariff** | Free of charge — government-funded; registration required via SBC portal |
| **hobbyist_eligibility** | Yes — any user may register; no professional surveying licence requirement found |
| **legal_residency_required** | ? — not explicitly required; LGIA does not publish a residency clause, but the registration form is Latvian-language only and no foreign-user policy statement is visible. |
| **last_confirmed_alive** | 2026-05-21 — `curl --http0.9 http://latpos.lgia.gov.lv:5001/` returned `SOURCETABLE 200 OK` (Server `GNSS Spider 7.11.1.109/1.0`, Latvian-language Date header `Ceturtd., 21 maijs 2026 09:46:53 GMT`, Content-Length 768); 7 STR rows confirmed |
| **datum_epoch** | omitted — LGIA's LatPos page states only "base station coordinates are calculated in the currently valid Latvian geodetic coordinate system" (LV, 2026-05-21); no epoch is declared. The 1992.75 anchor for LKS-92 appears in the EPSG registry (EPSG:3059) but EPSG is not an operator declaration; primer citation rule excludes EPSG-derived epochs. The LKS-92 → LKS-2020 frame change (2026-10-01) is LGIA-announced at the agency level (EPSG:10306 replacement CRS, LGIA-supplied) but the LatPos operator page does not declare the epoch for the network output frame. |

## Context Notes

- **LatPos**: Permanent GNSS reference station network operated by the Latvian Geospatial Information Agency (LGIA / Latvijas Ģeotelpiskās informācijas aģentūra). Made free to all registered users in 2018.
- **Infrastructure**: 36 base stations contributing — 27 in Latvia, 5 in Estonia (via LGIA–EuroGeographics cooperation with the Estonian Land Board), 4 in Lithuania (LitPOS cooperation). All operate continuously and distribute corrections via mobile internet. Constellations: GPS, GLONASS, Galileo, BeiDou (BeiDou via the dedicated `*-BeiDOU` mountpoints).
- **Real-time accuracy**: ~2 cm horizontal in real-time; ~5 mm in post-processing.
- **Access**: Registration required via the LatPos SBC (Spider Business Center) portal. Users must accept LatPos terms of use before account activation.
- **Sandbox connectivity**: 2026-05-21 `curl --http0.9 http://latpos.lgia.gov.lv:5001/` returned the sourcetable normally; an earlier 2026-05-17 timeout was a transient sandbox-side effect, not a service outage.
- **Frame transition (2026-10-01)**: LGIA replaces LKS-92 by LKS-2020 (EPSG 10303 geographic / 10306 projected) on 2026-10-01. LGIA has announced this transition at the agency level (lgia.gov.lv/lv/latpos, 2026-05-21); how LatPos RTK output will follow the change has not been declared by the operator in any source consulted. Rover users with stored grid offsets should monitor official LGIA communications before 2026-10-01.
- **Volunteer presence on rtk2go / Centipede**: `py scripts/stations_by_country.py LVA` returns 3 rtk2go pins (`Bracas` 57.07,24.83; `KALSNAVA` 56.73,25.96; `mnt239_1` 56.90,24.19) and 1 Centipede pin (`RIGA` 56.905,24.191). These are unofficial — LatPos is the authoritative service.
- **Operator contact**: LGIA, Rīga; service email `latpos@lgia.gov.lv`; agency portal `https://www.lgia.gov.lv/`

## Post-Processing (RINEX) Fallback

RINEX data available via the LatPos SBC portal after registration at no cost. EUREF/EPN archive carries Latvian stations (RIGA etc.) for global-frame post-processing — https://www.epncb.oma.be/

## Inventory Discrepancy

`rtk_inventory.md` records `landing_url` as `https://www.lgia.gov.lv/en/latpos` (the English-language variant). That URL returns HTTP 404 as of 2026-05-21 (confirmed by direct fetch). The correct live URL is `https://www.lgia.gov.lv/lv/latpos` (Latvian-language; used in this file). The rtk_inventory entry should be updated to the LV URL.

## Sources Consulted
- LatPos LV operator page: https://www.lgia.gov.lv/lv/latpos (observed 2026-05-21; EN variant `/en/latpos` returns HTTP 404)
- LatPos SBC sign-up portal: https://latpos.lgia.gov.lv/SBC/Account/Register
- Alberding caster map (LatPos): https://www.alberding.eu/cgi-bin/map.cgi?caster=latpos.lgia.gov.lv&port=5001&lang=en&gencgi=1
- ArduSimple Latvia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-latvia/
- Inside GNSS — LatPos free-access article: https://insidegnss.com/latvias-latpos-network-consolidates-free-access-and-operational-resilience/
- LKS-92 / Latvia TM (EPSG:3059, LGIA-supplied parameters): https://epsg.io/3059 — EPSG registry notes anchor epoch 1992.75 (not declared by LGIA on the LatPos operator page; not citable per primer); replaced by LKS-2020 from 2026-10-01
- LKS-2020 / Latvia TM (EPSG:10306, LGIA-supplied parameters): https://epsg.io/10306 — effective from 2026-10-01; LGIA-announced frame change but LatPos output epoch not declared
- Live caster probe (2026-05-21): `curl --http0.9 http://latpos.lgia.gov.lv:5001/` → SOURCETABLE 200 OK, 7 STR, Server `GNSS Spider 7.11.1.109/1.0`
- Local pipeline check: `py scripts/stations_by_country.py LVA` returns 1 Centipede + 1 EUREF/IGS + 3 rtk2go LV pins; LatPos itself contributes 0 mappable pins (sourcetable rows carry `0.00, 0.00` placeholders for most VRS streams)
