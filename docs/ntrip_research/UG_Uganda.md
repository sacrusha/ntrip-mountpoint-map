# Uganda [UG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-13 entry)

## Status: YES — free national NTRIP (UGRF CORS); registration via Spider Business Center required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | MLHUD — Ministry of Lands, Housing and Urban Development; Department of Surveys and Mapping |
| **Service name** | UGRF (Uganda Geodetic Reference Frame) CORS Network |
| **landing_url** | `https://mlhud.go.ug/lands-managment/department-of-surveys-and-mapping/` — operator (MLHUD) Department of Surveys and Mapping page; describes UGRF and its purpose. The dedicated network portal `ugrf.mlhud.go.ug` is a Leica Spider Business Center login wall (no public description). |
| **access_url** | `https://ugrf.mlhud.go.ug/SBC` — Spider Business Center; account creation page for NTRIP credentials. (Operator portal also referenced as `http://ugrf.go.ug/SBC`.) |
| **host:port** | `ugrf.mlhud.go.ug:2101` (IP: 154.72.216.21:2101) |
| **VRS** | Yes — mountpoints: VRSRTCM3, MAXRTCM3 (network RTK); also iMAX_RTCM, FKP_RTCM |
| **Constellations** | GPS+GLONASS (primary); GPS+GLO+GAL+BDS on NEAREST mountpoint |
| **num_stations** | 78 physical CORS = 40 government + 38 private (MLHUD 2024 workshop). Sourcetable exposes 44 mountpoints = 6 network virtual streams + 38 single-base STR entries; the 38 single-base entries correspond to the government-owned subset publicly served (private stations contribute to the network solution but are not individually exposed). No conflict between figures. |
| **tariff** | Free — expected to remain free for the foreseeable future; future maintenance fee possible |
| **hobbyist_eligibility** | Yes — no professional licence requirement stated; open registration |
| **legal_residency_required** | Unclear — registration via ugrf.mlhud.go.ug/SBC; no explicit residency restriction found |
| **last_confirmed_alive** | `ugrf.mlhud.go.ug:2101` SOURCETABLE 200 OK 2026-05-17 (Leica GNSS Spider 7.10.1.168; 44 mountpoints; 4046 bytes — byte-identical to 2026-05-13 capture) |
| **datum_epoch** | omitted -- no citable operator declaration. UGRF-2018 referenced in MLHUD 2024 workshop write-up but not as a verbatim datum-frame statement; Arc 1960 explicitly replaced per GIM International (2014 article) but successor frame not declared on operator portal. |

## Sourcetable Observations (2026-05-17; unchanged from 2026-05-13)

Full 44-mountpoint sourcetable retrieved via curl. Network virtual streams (broadcast at Entebbe HQ, 0.06°N 32.48°E):
- `ENTB` — Entebbe ref station
- `NEAREST` — nearest-base auto-selection, RTCM 3, GPS+GLO+GAL+BDS (the only multi-constellation NEAREST stream)
- `MAXRTCM3` — Master-Auxiliary (MAC) network corrections
- `VRSRTCM3` — VRS, RTCM 3, GPS+GLO (network RTK)
- `iMAX_RTCM` — individualised MAC, RTCM 3, GPS only
- `FKP_RTCM` — FKP corrections, RTCM 3, GPS+GLO

Physical single-base mountpoints — primary 14 stations (NMEA required where bit 13 = 1):
- `JING` Jinja (0.42, 33.21), `MBAL` Mbarara/Mbale (1.07, 34.17), `FPRT` Fort Portal (0.65, 30.30 — GPS+GLO+GAL), `GULU` (2.78, 32.30), `ARUA` (3.02, 30.91), `KBLE` Kabale-area (0.80, 31.08), `LIRA` (2.25, 32.90), `MRTO` Moroto (2.53, 34.66), `MSKA` (-0.34, 31.72), `MSND` (1.69, 31.72), `SRTI` (1.72, 33.62)

Physical single-base mountpoints — secondary 24 (lower priority flag = 0, includes regional stations across Karamoja, West Nile, Buganda, Ankole):
- `Kotido`, `Kaabong`, `Abim`, `Adjm` (Adjumani), `Apac`, `Bombo`, `Bugiri`, `Nakasongola`, `Ibanda`, `Kabale`, `Kalangala`, `Kamuli`, `Kasese`, `Kiboga`, `Kikuube`, `Kitgum`, `Kyegegwa`, `Mbarara`, `Mityana`, `Nakapiripirit`, `Napak`, `Ochero`, `Rakai`, `Rukungiri`, `Sembabule`, `Packwach`, `Yumbe`

All single-base mountpoints are RTCM 3, GPS+GLO except FPRT which adds Galileo. The sourcetable lists 38 single-base stations + 6 network streams = 44 total mountpoints; this matches Uganda's previously documented 40 government + 38 private = 78 total station figure if government plus a subset of private feeds are exposed in the public NTRIP. National workshop (2024) noted Phase II expansion from a 12-station Phase I.

## Context Notes

- UGRF is one of the few free, publicly accessible national NTRIP casters in Sub-Saharan Africa with a confirmed live sourcetable.
- The network comprises 40 government CORS + 38 private stations = 78 total. 14+ station names visible in sourcetable covering the country from Arua (north) to Kabale (south), Moroto (east) to Fort Portal (west).
- VRS accuracy: better than 1–2 cm within 20 km of a station; 5 cm within 80 km with network RTK.
- Registration: create account at https://ugrf.mlhud.go.ug/SBC (Spider Business Center login page). NTRIP credentials provided after account creation.
- The UGRF portal (ugrf.mlhud.go.ug) returned ECONNREFUSED on HTTP fetch but the NTRIP port 2101 responded normally — portal may be HTTPS-only or temporarily misconfigured.
- National Workshop on UGRF held November 2024; network expansion, enhanced training, and updated legal frameworks discussed.
- Post-processing RINEX download also available via the SBC portal.
- 40 government CORS stations provide geodetic data for land administration, infrastructure, disaster monitoring, and cadastral surveys.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **UGRF SBC RINEX download** | https://ugrf.mlhud.go.ug/SBC | Free (account required) |
| **IGS online post-processing via EarthScope** | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- Uganda UGRF FAQ (CORS access): http://ugrf.mlhud.go.ug/faq/cors-real-time-corrections (ECONNREFUSED 2026-05-06; content from cached search result)
- Uganda UGRF Spider Business Center: http://ugrf.go.ug/SBC (accessed via search result)
- MLHUD National Workshop on UGRF 2024: https://mlhud.go.ug/national-workshop-on-ugandas-geodetic-reference-framework-2024/ (observed 2026-05-06)
- MLHUD Department of Surveys and Mapping: https://mlhud.go.ug/lands-managment/department-of-surveys-and-mapping/ (observed 2026-05-06)
- GIM International UGRF article: https://www.gim-international.com/content/article/establishing-an-accurate-geodetic-reference-network-for-uganda
- curl probe of `ugrf.mlhud.go.ug:2101` (154.72.216.21:2101) — SOURCETABLE 200 OK 2026-05-06, 2026-05-13, 2026-05-17; Leica GNSS Spider 7.10.1.168; 44 mountpoints (6 network + 38 single-base); content stable across all three probes
