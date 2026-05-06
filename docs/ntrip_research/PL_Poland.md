# Poland [PL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free government NTRIP caster (ASG-EUPOS) operating since Oct 2022

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (ASG-EUPOS — free since 2 Oct 2022) |
| **host:port — ASG-EUPOS** | `system.asgeupos.pl:2101` (IP: 91.198.76.2) · also port 8080 (RTN), port 8082/8083 (GPS+GLO only), port 8086 (GPS+GLO+GAL+BDS) |
| **VRS** | Yes — NAWGEO service (Network RTK / RTN) provides VRS-style network corrections; RTK service also allows nearest-station single-base mode |
| **tariff** | Free since 2 October 2022 (all services: RTK, RTN/NAWGEO, DGNSS); registration required |
| **hobbyist_eligibility** | yes — individual persons (osoby fizyczne) may register; open to all entity types |
| **legal_residency_required** | no explicit residency requirement; registration open internationally; users must agree to terms (no resale of corrections to third parties) |
| **last_confirmed_alive** | `system.asgeupos.pl:2101` and `:8086` both returned `SOURCETABLE 200 OK` on 2026-05-06 (curl verified) |

## Context Notes

- **ASG-EUPOS** (Active Geodetic Network – European Position System): Operated by the Head Office of Geodesy and Cartography (GUGiK) since 2008. Poland's national contribution to the pan-European EUPOS standard. All fees eliminated 2 October 2022.
- **Infrastructure**: ~100 reference stations across Poland. Part of EUPOS network interoperable with neighbouring countries' systems (CzechGEO, SKPOS, ASG-EUPOS etc.).
- **Service types**:
  - **RTK** — single-station or nearest-station positioning; cm-level accuracy
  - **NAWGEO (RTN)** — network RTK/VRS mode; requires transmission of receiver position to server (NtripV2); achieves 1–2 cm horizontal, 2–3 cm vertical
  - **DGNSS** — sub-metre differential corrections
- **Data formats**: RTCM 3.4, RTCM 3.1, RTCM 2.3 across various mountpoints
- **Authentication**: Username/password via NTRIP protocol after registration at www.asgeupos.pl or system.asgeupos.pl; NTRIP version 2.0 recommended for RTN/VRS mode
- **Registration**: Electronic form at asgeupos.pl; entity type selection (individual / entrepreneur / public unit); email activation link required
- **Note on VRS / NRTK polygon**: ASG-EUPOS is VRS (no physical pinned stations in the volunteer sense); rtk2go hosts ~40+ Polish volunteer single-base stations as a complement for users who need physical reference point diversity.
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
- curl probe of `system.asgeupos.pl:2101` — SOURCETABLE 200 OK confirmed 2026-05-06
- curl probe of `system.asgeupos.pl:8086` — SOURCETABLE 200 OK confirmed 2026-05-06
