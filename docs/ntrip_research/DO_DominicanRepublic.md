# Dominican Republic [DO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (revision; original 2026-05-06)

## Status: YES — multiple active public NTRIP casters

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (FUNDCORSRD curl-confirmed live 2026-05-17; IGN REGNA-RD government; CODIA CORS-MET licensed-only; TopNETlive commercial) |
| **landing_url — FUNDCORSRD** | https://fundcorsrd.com/ |
| **access_url — FUNDCORSRD** | https://fundcorsrd.com/ (contact form / fundcorsrd@gmail.com -- no self-service signup page; access via credential request) |
| **landing_url — IGN REGNA-RD** | https://ntrip.ign.gob.do/ |
| **access_url — IGN REGNA-RD** | https://ntrip.ign.gob.do/ (registration portal) |
| **landing_url — CODIA CORS-MET** | https://www.codia.org.do/ (no public service-specific page located) |
| **access_url — CODIA CORS-MET** | null -- restricted to licensed CODIA members; no public signup |
| **landing_url — TopNETlive** | https://www.topnetlive.com/ |
| **access_url — TopNETlive** | https://www.topnetlive.com/ (commercial signup via Topcon dealer) |
| **host:port -- FUNDCORSRD** | `190.166.228.161:2103` -- sourcetable retrieved live 2026-05-17 (73 STR rows + 1 NEAR routing alias = 39 physical stations across paired RTCM 3.0 + RTCM 3.2/3.3 streams; multi-GNSS GPS+GLO+GAL+BDS; SNIP [wPRO] R3.19.00 of:Dec 19 2025). |
| **host:port -- IGN REGNA-RD** | `ntrip.ign.gob.do` (registration portal reachable; NTRIP port 2101 sandbox-timeout -- Cloudflare WAF/IP filter) |
| **host:port -- CODIA CORS-MET** | not published (CODIA-licensed members only) |
| **host:port -- TopNETlive** | `rtk.topnetlive.com:2101` (Topcon commercial; DR coverage listed on corsstations.com) |
| **num_stations -- FUNDCORSRD** | 39 unique physical stations (live sourcetable 2026-05-17 -- BARA, FCAC, FCBN, FCBO, FCCT, FCCZ, FCDA, FCDN, FCEP, FCHT, FCHY, FCJA, FCLM, FCLR, FCLT, FCMF, FCMI, FCMO, FCNA, FCNB, FCNV, FCOC, FCPS, FCPT, FCRS, FCSF, FCSJ, FCSM, FCUP, FCVP, FCVV, HGUY, LVEG, PEVA, SAMN, SJUM, SPED, SROD, STGO; most stations expose paired RTCM 3.0 + RTCM 3.2/3.3 streams). Growth trajectory: ComNav build-out 2023 -> 32 stations (GPS World 2023-10-09); May 2025 office inauguration -> 30 CORS + 4 from Jurisdicción Inmobiliaria = 34 (inmobiliario.do 2025-05-21); 2026-05-17 live sourcetable -> 39 unique stations. The three figures correspond to consecutive milestones rather than conflicting counts. |
| **num_stations -- IGN REGNA-RD** | 2 original (Moca, Puerto Plata); November 2025 expansion announced (post-expansion station count not enumerated in public sources as of 2026-05-17) |
| **vrs** | FUNDCORSRD: no (single-station mountpoints only — each station offers an RTCM 3.0 stream and an RTCM 3.2/3.3 MSM stream, plus one `NEAR` routing alias); IGN REGNA-RD: ? |
| **tariff** | FUNDCORSRD: not published — credentials via fundcorsrd.com / fundcorsrd@gmail.com. IGN REGNA-RD: appears free. CODIA: gated. TopNETlive: paid commercial. |
| **hobbyist_eligibility** | FUNDCORSRD: unclear — non-profit founded by surveyors but states it serves "society in general" (838+ users as of May 2025 office inauguration); IGN: unclear; CODIA: no (licensed CODIA members only); TopNETlive: yes (open commercial) |
| **legal_residency_required** | unclear |
| **registration** | FUNDCORSRD: contact form at fundcorsrd.com / email fundcorsrd@gmail.com. IGN REGNA-RD: https://ntrip.ign.gob.do/ |
| **last_confirmed_alive** | FUNDCORSRD: **2026-05-17** (sourcetable retrieved live; 73 STR + 1 NEAR; SNIP build of 2025-12-19). IGN REGNA-RD portal: 2026-05-06 reachable (NTRIP port behind WAF/IP filter). |
| **datum_epoch** | omitted -- no citable operator declaration. fundcorsrd.com homepage and the IGN REGNA-RD portal do not publish the geodetic frame/epoch; SIRGAS context suggests SIRGAS2000/ITRF, but per [datum-epoch] rule SIRGAS bulletin / regional context is not citable for the operator. |

## Most Recent Project Announcement

**IGN REGNA-RD expansion** — November 2025. The Instituto Geográfico Nacional expanded the REGNA-RD CORS network beyond the original 2 stations (Moca, Puerto Plata). Registration portal at ntrip.ign.gob.do remained reachable; the actual NTRIP port appears to sit behind a Cloudflare WAF that blocks raw TCP connections to 2101 from outside Cloudflare-allowed paths.

## Context Notes

- **FUNDCORSRD** (Fundación CORS-RD): Non-profit caster founded 2016-01-16 by surveyors. Sourcetable was retrieved live on **2026-05-17** from `190.166.228.161:2103` and lists **73 STR + 1 `NEAR` routing alias = 39 unique physical stations**, most stations exposing paired RTCM 3.0 (legacy GPS+GLO) and RTCM 3.2/3.3 MSM (multi-GNSS GPS+GLO+GAL+BDS, frequently MSM7 1077/1087/1097/1127) streams. Coverage extends nationwide (BARA La Romana, FCAC Azua, FCBN Bani, FCBO Bonao, STGO Santiago, and many others). Caster software: SNIP [wPRO] R3.19.00 (build of 2025-12-19). The caster is closed: credentials are issued via direct request through fundcorsrd.com or fundcorsrd@gmail.com. Self-described as serving "society in general"; the May 2025 office inauguration article cites 30 CORS + 4 from Jurisdicción Inmobiliaria (= 34 then) and 838+ users. Underlying hardware: ComNav SinoGNSS M300 Pro receivers + AT600 choke-ring antennas (per GPS World 2023-10-09 build coverage; FUNDCORSRD partner). Pricing not surfaced publicly. Strategic agreement with IGN confirmed in 2025 press coverage to contribute to the Dominican Republic's Satellite Geodetic System.
- **IGN REGNA-RD** (Instituto Geográfico Nacional): Government service. Hostname `ntrip.ign.gob.do` and registration portal confirmed reachable on 2026-05-06; raw NTRIP port (2101) timed out, consistent with Cloudflare proxying. The service appears to be free for registered users. Originally 2 stations (Moca, Puerto Plata); November 2025 expansion announced (size/locations not yet enumerated in public sources).
- **CODIA CORS-MET**: Restricted to licensed members of CODIA (Colegio Dominicano de Ingenieros, Arquitectos y Agrimensores) — not accessible to non-licensed individuals or hobbyists.
- **TopNETlive (Topcon)**: Paid commercial global subscription network; `rtk.topnetlive.com:2101`; DR coverage listed on corsstations.com. Open enrolment via Topcon dealers; pricing not on public Topcon page.
- **No free unrestricted public caster** confirmed; FUNDCORSRD and IGN REGNA-RD both gate access via registration.

## Volunteer / Global Coverage (ingested-globals check 2026-05-17)

- **rtk2go (DOM-coded, 1 node per `py scripts/stations_by_country.py DOM`):**
  - `geofis_mbase` Santo Domingo (18.46, -69.92) -- `nmea=1`, indicating NRTK or routing alias rather than simple volunteer single-base. Likely an institutional re-feed (UASD / geophysics dept context implied by name); treat as supplementary, not a hobbyist tower.
- **earthscope (NOTA) DOM-coded, 10 stations:** BARA, CN05, CN06, CN07, CN27, LVEG, RDMA, RDSD, SPED, SROD -- accessible via NULA-style non-commercial registration (see [licensing]).
- **igs_ip:** 1 station `RDSD00DOM0` (18.46, -69.91).
- **Centipede:** no DOM-coded nodes observed in project sourcetable.
- **GEODNET:** no Dominican Republic stations visible on public GEODNET coverage map as of 2026-05-17.
- **onocoy:** no Dominican Republic stations visible on public onocoy coverage map as of 2026-05-17.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGN REGNA-RD** — RINEX from REGNA-RD CORS stations | https://ign.gob.do/ | Likely free with account |
| **FUNDCORSRD** — RINEX archive accompanies live caster | https://fundcorsrd.com/ | Account required |
| **EarthScope / SIRGAS-CON** — DR stations in SIRGAS tier | https://www.earthscope.org/data/gnss-data/ | Free noncommercial; USD 1,000/seat/yr commercial |

## Sources Consulted
- FUNDCORSRD sourcetable (`190.166.228.161:2103`) — live curl probe 2026-05-17 (73 STR + 1 NEAR; 39 physical stations)
- FUNDCORSRD homepage: https://fundcorsrd.com/
- Inmobiliario.do — "Office opens to strengthen technological services for surveyors" (2025-05-21; 30 CORS + 4 from Jurisdicción Inmobiliaria; 838+ users; IGN strategic agreement): https://inmobiliario.do/en/office-opens-to-strengthen-technological-services-for-surveyors/
- GPS World — "ComNav Technology and Dominican Republic Forge Advanced CORS Network" (2023-10-09; ComNav SinoGNSS, M300 Pro + AT600, 32 stations build): https://www.gpsworld.com/comnav-technology-and-dominican-republic-forge-advanced-cors-network/
- ArduSimple Dominican Republic page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-dominican-rep/
- IGN Dominican Republic (ign.gob.do)
- ntrip.ign.gob.do registration portal
- CODIA-CORS-MET program references via CODIA
- TopNETlive coverage listing on corsstations.com
- NTRIP-list.com Caribbean/North America
- GEODNET, ONOCOY coverage maps
- SIRGAS-CON station list (regional context only; not citable for FUNDCORSRD datum declaration)
