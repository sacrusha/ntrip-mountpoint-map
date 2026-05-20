# Lesotho [LS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; still no LS caster; TrigNet ZA remains nearest practical fallback)

## Status: NO — no public NTRIP RTK caster operating within Lesotho

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | None found |
| **tariff** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster identified 2026-05-12 |
| **Nearest practical fallback** | TrigNet (ZA) — `trignet.co.za:2101`, free; see below |

## Most Recent Project Announcement

No national CORS programme or NTRIP project announcement found for Lesotho as of 2026-05-12. The Department of Lands, Surveys and Physical Planning (DLSPP), under the Ministry of Local Government, Chieftainship, Home Affairs and Police, is the national geodetic authority, but no public documentation of a CORS installation or real-time GNSS service has been located.

## Context Notes

- **National authority:** Department of Lands, Surveys and Physical Planning (DLSPP) — no website with public geodetic data service found.
- **AFREF / SAFREF:** Lesotho is within the SAFREF (Southern Africa Geodetic Reference Frame) geographic scope alongside Botswana, Malawi, Namibia, South Africa, Swaziland, Zambia, and Zimbabwe. No Lesotho IGS or AFREF core station has been identified in AFREF station lists or HartRAO archives; the nearest AFREF-contributing CORS are in South Africa.
- **No entries on rtk2go, Centipede or EarthScope:** Zero LS mountpoints observed in any of the project's three pipelines as of 2026-05-12.
- **Nearest pipeline stations from Maseru (29.6°S, 28.3°E)** — `py scripts/stations_by_radius.py -29.6 28.3 500` (2026-05-12): rtk2go `LouwNPP` (ZAF, −27.34/30.90, 357 km) and `mabuda_farm` (SWZ, −26.47/31.94, 499 km); Centipede `PIER` (ZAF, −32.43/25.74, 398 km). All baselines are too long for sub-decimetre RTK; PIER/LouwNPP are only useful for sub-metre work or as a courtesy DGNSS source. No South African TrigNet mountpoint is closer to Maseru than ~210 km (Bloemfontein BLMF) per published station list.
- **No entry on ntrip-list.com:** Lesotho is absent from the Africa listing on ntrip-list.com.
- **No commercial NTRIP providers found** covering Lesotho (GEODNET, ONOCOY, PointOne, HxGN SmartNet — none list Lesotho coverage).
- **Geographic enclave consideration:** Lesotho is entirely surrounded by South Africa. TrigNet (`trignet.co.za:2101`, free, web registration at trignet.co.za) has stations ringing the border — Bloemfontein (~210 km from Maseru), Bethlehem, and stations along the eastern Highlands corridor. Baseline distances of 100–200 km are typically too long for centimetre RTK; single-base RTK degrades sharply beyond ~50–60 km. Practical RTK coverage from TrigNet exists only in the narrow Maseru-border strip and possibly the north-eastern lowlands where TrigNet station spacing is tighter. TrigNet is not a Lesotho service; cross-border use is incidental and not guaranteed. → rtk_inventory.md: `trignet`
- **Practical hobbyist guidance:** Deploy a local GNSS base station (e.g., Emlid Reach RS2+, u-blox ZED-F9P) for single-base RTK; use Galileo HAS / PPP for sub-metre post-processing work without a base.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **TrigNet RINEX download** — nearest South African CORS (Bloemfontein, Bethlehem); usable for post-processing within Lesotho if baseline is acceptable | http://www.trignet.co.za/ | Free (NGI policy, R 0.00) |
| **EarthScope / IGS RINEX archive** — no Lesotho station; nearest qualifying station is in South Africa | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

## Negative Findings

- AFREF station map: no LS station identified
- HartRAO GNSS archive: no Lesotho station in 28-station African network
- IGS network: no station with country code LS
- rtk2go monitor: zero LS mountpoints
- Centipede: zero LS nodes
- ntrip-list.com/africa: no Lesotho entry
- GEODNET, ONOCOY, PointOne, Trimble RTX, Galileo HAS: coverage maps do not specifically address Lesotho (HAS provides global sub-decimetre PPP but not network RTK)

## Sources Consulted
- AFREF background documentation: https://un-spider.org/space-application/space-application-matrix/african-geodetic-reference-frame-afref
- AFREF station map (ResearchGate): https://www.researchgate.net/figure/GNSS-stations-which-could-be-available-for-AFREF-purposes_fig1_256294236
- HartRAO GNSS data: https://geodesy.hartrao.ac.za/site/en/data-and-products/gnss.html
- TrigNet (NGI): https://ngi.dalrrd.gov.za/index.php/what-we-do/geodetic-and-control-survey-services/37-trignet-continuously-operating-gnss-network
- ntrip-list.com Africa: https://ntrip-list.com/africa/
- East View Geospatial — Lesotho country data: https://geospatial.com/resources/country-data/lesotho/
- rtk2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Local pipeline check (2026-05-12): `py scripts/stations_by_radius.py -29.6 28.3 500` → 2 rtk2go + 1 Centipede pin within 500 km (all in ZAF/SWZ, not LS); `py scripts/stations_by_country.py` → no LSO entries in any pipeline source
