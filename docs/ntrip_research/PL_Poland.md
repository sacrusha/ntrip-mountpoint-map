# Poland [PL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (station list research added; prior: 2026-05-17)

## Status: YES — free gov NTRIP caster (ASG-EUPOS) operating since Oct 2022

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (ASG-EUPOS — free since 2 Oct 2022) |
| **landing_url** | `https://www.asgeupos.pl/language/en/` |
| **access_url** | `https://www.asgeupos.pl/language/en/rtk-eng/` (RTK product + connection guide; registration form linked from same portal) |
| **host:port — ASG-EUPOS** | `system.asgeupos.pl:2101` (IP: 91.198.76.2) · port 8080 (RTN), 8082/8083 (GPS+GLO), 8086 (GPS+GLO+GAL+BDS multi-constellation) |
| **VRS** | Yes — NAWGEO RTN: `NAWGEO_VRS_3_1`, `NAWGEO_VRS_2_3`, `NAWGEO_VRS_CMR`, `NAWGEO_MAC_3_1` (MAC). Also RTN4G_VRS_RTCM32 (GPS+GLO+GAL+BDS) per :2101 ST 2026-05-17. Single-base nearest-CORS streams on :8086. |
| **tariff** | Free since 2 Oct 2022 (RTK, RTN/NAWGEO, DGNSS); registration required. Date per ASG-EUPOS English portal (canonical). Polish-press item at agrokonsument.pl gives "2 września 2022" (2 Sept 2022) — treat as a possible pre-announcement or staggered rollout; official portal date supersedes. |
| **num_stations** | 119+ Polish CORS with published XYZ coordinates at `asgeupos.pl/language/en/services-2/coordinates-of-reference-stations/` (119 entries in table, some with 0,0,0 = offline/missing; 8 new stations added Dec 2023: WCKO, PISZ, INWR, SLUP, STCE, BOLE, ZAMO, OSWM; 3 more Jan 2024: GLDP, OSEK, TRSP; network now ~125+ active Polish stations). Network expanded past original 130-station design ceiling. Border-zone EPN/IGS stations also incorporated for network solution. |
| **Physical station coords** | Full ECEF XYZ table (PL-ETRF2000, epoch 2011.0) at `https://www.asgeupos.pl/language/en/services-2/coordinates-of-reference-stations/` — 119 rows confirmed 2026-05-21; conversion to lat/lon requires ECEF→geodetic transform (standard formula). Some stations have 0,0,0 placeholder (offline). Station IDs: 4-char codes (BART, BIAL, BILG, BOGI, BOR1, BPDL, BRSK ... ZARY, ZIGR, ZYWI). |
| **datum_epoch** | PL-ETRF2000 epoch 2011.0 (Polish realization of ETRS89; ETRF2000 adopted by GUGiK 2012). Source: GUGiK ASG-EUPOS portal + Polish legal decree. Operator portal page itself does not state epoch verbatim — citation rule: needs operator-side declaration; mark `omitted -- no citable operator declaration` until found on asgeupos.pl. |
| **hobbyist_eligibility** | yes — individuals (osoby fizyczne) may register; open to all entity types |
| **legal_residency_required** | no explicit residency requirement; international registration open; terms forbid resale of corrections |
| **last_confirmed_alive** | `system.asgeupos.pl:2101` SOURCETABLE 200 OK 2026-05-17 (Trimble Ntrip Caster 5.2; NAWGEO_VRS_3_1, MAC_3_1, RTN4G_VRS_RTCM32 advertised). |

## Context Notes

- **ASG-EUPOS** (Active Geodetic Network – European Position System): Operated by the Head Office of Geodesy and Cartography (GUGiK) since 2008. Poland's national contribution to the pan-European EUPOS standard. All fees eliminated 2 October 2022.
- **Infrastructure**: 119 Polish reference stations listed in the coordinates table as of May 2026 (some with 0,0,0 = offline; ~125+ when including stations added Dec 2023 and Jan 2024). The design specification was up to 130 stations — the network has expanded. Prior project research cited ~160–190; the coordinates page only lists 119 entries; final live count is likely higher when including recent additions not yet reflected in the coords page. Part of EUPOS network interoperable with neighbouring countries' systems (CzechGEO, SKPOS, etc.); foreign EPN/IGS stations along Poland's borders are also incorporated for network solution.
- **Service types**:
  - **RTK** — single-station or nearest-station positioning; cm-level accuracy
  - **NAWGEO (RTN)** — network RTK/VRS mode; requires transmission of receiver position to server (NtripV2); achieves 1–2 cm horizontal, 2–3 cm vertical
  - **DGNSS** — sub-metre differential corrections
- **Data formats**: RTCM 3.4, RTCM 3.1, RTCM 2.3 across various mountpoints
- **Authentication**: Username/password via NTRIP protocol after registration at www.asgeupos.pl or system.asgeupos.pl; NTRIP version 2.0 recommended for RTN/VRS mode
- **Registration**: Electronic form at asgeupos.pl; entity type selection (individual / entrepreneur / public unit); email activation link required
- **Note on VRS / NRTK polygon**: ASG-EUPOS is VRS (no physical pinned stations in volunteer sense); rtk2go hosts 52 Polish volunteer single-base stations (`scripts/stations_by_country.py POL` 2026-05-17). EUREF-IP serves 5 Polish stations (JOZ2, KRA1, KRAW, LAMA, WROC); IGS-IP serves 5 (BOGI, BOR1, JOZ2, LAMA, WROC).
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
- ASG-EUPOS Reference Stations list (table + map): https://www.asgeupos.pl/language/en/services-2/reference-stations/ (map mapa_070125.png = Jan 2025)
- ASG-EUPOS station coordinates (ECEF XYZ, PL-ETRF2000 ep 2011.0; 119 entries): https://www.asgeupos.pl/language/en/services-2/coordinates-of-reference-stations/ (confirmed 2026-05-21)
- 8 new stations Dec 2023 (WCKO, PISZ, INWR, SLUP, STCE, BOLE, ZAMO, OSWM): https://www.gov.pl/web/gugik/nowe-stacje-referencyjne-w-systemie-asg-eupos (confirmed 2026-05-21)
- 3 more Jan 2024 (GLDP, OSEK, TRSP): https://www.geoportal.gov.pl/aktualnosci/nowe-stacje-referencyjne-w-systemie-asg-eupos-2/ (confirmed 2026-05-21)
- curl probe `system.asgeupos.pl:2101` — SOURCETABLE 200 OK 2026-05-17 (Trimble Ntrip Caster 5.2; NAWGEO + RTN + RTN4G mountpoints incl. GPS+GLO+GAL+BDS)
- Local `scripts/stations_by_country.py POL` (2026-05-17): 52 rtk2go bases, 5 EUREF-IP, 5 IGS-IP
