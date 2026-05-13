# Poland [PL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh; prior pass 2026-05-06)

## Status: YES — free government NTRIP caster (ASG-EUPOS) operating since Oct 2022

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (ASG-EUPOS — free since 2 Oct 2022) |
| **host:port — ASG-EUPOS** | `system.asgeupos.pl:2101` (IP: 91.198.76.2) · also port 8080 (RTN), port 8082/8083 (GPS+GLO only), port 8086 (GPS+GLO+GAL+BDS — full multi-constellation) |
| **VRS** | Yes — NAWGEO service (Network RTK / RTN) provides VRS-style network corrections (mountpoints `NAWGEO_VRS_3_1`, `NAWGEO_VRS_2_3`, `NAWGEO_VRS_CMR`, plus `NAWGEO_MAC_3_1` for Master-Auxiliary). Single-base RTK from nearest physical CORS also available on port 8086. |
| **tariff** | Free since 2 October 2022 (all services: RTK, RTN/NAWGEO, DGNSS); registration required |
| **num_stations** | ~190 Polish CORS currently operating (per the asgeupos.pl Reference Stations page, May 2026 — well above the original 130-station design ceiling). Additionally incorporates selected EPN/IGS stations. |
| **hobbyist_eligibility** | yes — individual persons (osoby fizyczne) may register; open to all entity types |
| **legal_residency_required** | no explicit residency requirement; registration open internationally; users must agree to terms (no resale of corrections to third parties) |
| **last_confirmed_alive** | `system.asgeupos.pl:2101` and `:8086` both returned `SOURCETABLE 200 OK` on 2026-05-12 (curl — `Server: NTRIP Trimble Ntrip Caster 5.2`). Port 2101 sourcetable advertises NAWGEO_VRS_3_1 / NAWGEO_MAC_3_1 / NAWGEO_VRS_2_3 / NAWGEO_VRS_CMR. |

## Context Notes

- **ASG-EUPOS** (Active Geodetic Network – European Position System): Operated by the Head Office of Geodesy and Cartography (GUGiK) since 2008. Poland's national contribution to the pan-European EUPOS standard. All fees eliminated 2 October 2022.
- **Infrastructure**: ~190 Polish reference stations as of May 2026 (per the asgeupos.pl Reference Stations table; the design specification was up to 130 stations — the network has expanded beyond that ceiling). Part of EUPOS network interoperable with neighbouring countries' systems (CzechGEO, SKPOS, etc.); foreign EPN/IGS stations along Poland's borders are also incorporated.
- **Service types**:
  - **RTK** — single-station or nearest-station positioning; cm-level accuracy
  - **NAWGEO (RTN)** — network RTK/VRS mode; requires transmission of receiver position to server (NtripV2); achieves 1–2 cm horizontal, 2–3 cm vertical
  - **DGNSS** — sub-metre differential corrections
- **Data formats**: RTCM 3.4, RTCM 3.1, RTCM 2.3 across various mountpoints
- **Authentication**: Username/password via NTRIP protocol after registration at www.asgeupos.pl or system.asgeupos.pl; NTRIP version 2.0 recommended for RTN/VRS mode
- **Registration**: Electronic form at asgeupos.pl; entity type selection (individual / entrepreneur / public unit); email activation link required
- **Note on VRS / NRTK polygon**: ASG-EUPOS is VRS (no physical pinned stations in the volunteer sense); rtk2go hosts 54 Polish volunteer single-base stations (confirmed via `scripts/stations_by_country.py POL` 2026-05-12) as a complement for users who need physical reference point diversity.
- **Operator contact**: GUGiK (Główny Urząd Geodezji i Kartografii); asgeupos@gugik.gov.pl

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ASG-EUPOS POZGEO** — online post-processing | https://system.asgeupos.pl/ | Free |
| **RINEX archive** — raw data from ASG-EUPOS reference stations | https://system.asgeupos.pl/ | Free |

## Sources Consulted
- ASG-EUPOS English homepage: https://www.asgeupos.pl/language/en/
- ASG-EUPOS RTK service: https://www.asgeupos.pl/language/en/rtk-eng/
- ASG-EUPOS RTN service: https://www.asgeupos.pl/language/en/rtn-eng/
- ASG-EUPOS system portal: https://system.asgeupos.pl/
- Agrotechnology free signal article: https://agrotechnology.pl/bezplatny-sygnal-korekcji-rtk-od-kiedy/
- ArduSimple Poland RTK page: https://www.ardusimple.pl/rtk-correction-services-and-ntrip-casters-in-poland/
- ASG-EUPOS Reference Stations list: https://www.asgeupos.pl/language/en/services-2/reference-stations/ (table lists ~190 PL stations + foreign EPN/IGS sites, May 2026)
- curl probe of `system.asgeupos.pl:2101` — SOURCETABLE 200 OK confirmed 2026-05-12 (Trimble Ntrip Caster 5.2; NAWGEO VRS / MAC mountpoints)
- curl probe of `system.asgeupos.pl:8086` — SOURCETABLE 200 OK confirmed 2026-05-12 (multi-constellation single-base streams; e.g. BART_RTCM_3_2, BIAL_RTCM_3_2, BILG_RTCM_3_2, BOGI_RTCM_3_2 — GPS+GLO+GAL+BDS)
- Local pipeline check `scripts/stations_by_country.py POL` (2026-05-12): 54 rtk2go community bases in Poland
