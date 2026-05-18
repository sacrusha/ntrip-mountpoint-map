# Mauritius [MU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (MAJOR REVISION: prior "no public NTRIP caster" framing corrected — Mauritius has a live IGS station VACS00MUS0 (Vacoas) republished on BKG IGS-IP and AUSCORS, plus an additional MIRAI mountpoint QMUP00MUS, both single-base real-time. The Survey Division still operates no Mauritius-branded caster.)

## Status: NO Mauritius-operated public NTRIP caster, BUT the IGS station VACS (Vacoas) is republished live on the BKG IGS-IP global caster and mirrored on AUSCORS; an additional QMUP mountpoint exists on the Japanese MIRAI caster. Combined, free single-base real-time RTK is available within ~30 km of either Vacoas (central Mauritius) or QMUP (-20.50, 57.45).

| Field | Value |
|---|---|
| **Mauritius-operated public NTRIP caster** | No — no Survey-Division host:port found in any directory, sourcetable, or academic reference |
| **Foreign-operated NTRIP streams covering MU** | Yes — `VACS00MUS0` (-20.30, 57.50, Vacoas IGS site) on `www.igs-ip.net:2101` (BKG IGS-IP) AND mirrored on `ntrip.data.gnss.ga.gov.au:2101` (AUSCORS rebroadcast); plus `QMUP00MUS` (-20.50, 57.45) on the MIRAI caster (Japanese GEONET successor; access via MIRAI registration — 2 forms + 365 d inactivity expiry) |
| **landing_url — BKG IGS-IP** | https://igs.bkg.bund.de/ntrip/ (BKG NTRIP service description) |
| **access_url — BKG IGS-IP** | https://igs.bkg.bund.de/ntrip/register (BKG NTRIP account registration) |
| **landing_url — AUSCORS** | https://gnss.ga.gov.au/stream (Geoscience Australia AUSCORS landing) |
| **access_url — AUSCORS** | https://gnss.ga.gov.au/registration (GA self-service registration, CC BY 4.0) |
| **landing_url — MIRAI** | https://www.mirai-gnss.com/ (operator description page for the Japanese MIRAI / GEONET-successor caster) |
| **access_url — MIRAI** | Skip — operator publishes no canonical self-service signup URL; per primer ingested-globals notes, MIRAI access is a 2-form manual workflow with 365-day inactivity expiry |
| **num_stations** | 2 physical CORS visible to MU users: VACS00MUS0 (Vacoas; same site exposed on IGS-IP and AUSCORS — count once) + QMUP00MUS (MIRAI). Snapshot 2026-05-17 via `py scripts/stations_by_country.py MUS`. |
| **datum_epoch** | omitted — IGS-IP / AUSCORS / MIRAI rebroadcast carries no Mauritius-operator-side datum declaration; the Survey Division publishes no NTRIP caster and no citable real-time-stream datum/epoch statement. Per primer, do NOT infer ITRF/IGS from caster identity. |
| **Operator (national, no caster)** | Survey Division, Ministry of Housing and Land Use Planning, Ebène (`housing.govmu.org`) |
| **host:port — IGS-IP** | `www.igs-ip.net:2101` (mountpoint `VACS00MUS0`) |
| **host:port — AUSCORS mirror** | `ntrip.data.gnss.ga.gov.au:2101` (mountpoint `VACS00MUS0`) |
| **host:port — MIRAI** | MIRAI caster (Japan; mountpoint `QMUP00MUS`) |
| **tariff (IGS-IP / AUSCORS)** | Free; BKG NTRIP account `igs.bkg.bund.de/ntrip/register` (IGS-IP) or GA self-service registration `gnss.ga.gov.au/registration` (AUSCORS, CC BY 4.0) |
| **tariff (MIRAI)** | Free; MIRAI registration (slow — 2 forms; 365-day inactivity expiry per ingested-globals notes) |
| **hobbyist_eligibility** | Yes (IGS-IP / AUSCORS) — no surveyor licence required. MIRAI: yes for non-commercial in practice |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-17 — VACS00MUS0 present in local data/igs_ip.sourcetable + data/auscors.sourcetable; QMUP00MUS in data/mirai.sourcetable. Radius probe `py scripts/stations_by_radius.py -20.2 57.5 1500` returns VACS00MUS0 at 11.1 km and QMUP00MUS at 33.9 km from Port Louis |

## Operator

**Survey Division**
Ministry of Housing and Land Use Planning
7th Floor, Emmanuel Anquetil Building, Port Louis / Ebène, Mauritius
Website: https://housing.govmu.org/Pages/Dept%20and%20Org/Divisions/Survey/Survey.aspx

## Context

- **National geodetic authority:** The Survey Division is responsible for land survey, cadastral implementation, and cartography for Mauritius (main island + Rodrigues, Agaléga, etc.). No Mauritius-operated NTRIP caster has been found despite the 2016 RCMRD feasibility workshop.
- **2016 RCMRD feasibility workshop:** May 2016 workshop hosted at the Ministry in Ebène, facilitated by RCMRD (Nairobi), examined establishing a national CORS network. ~40 participants. No follow-up operational caster from the Survey Division has been confirmed since.
- **IGS station VACS (Vacoas):** **CORRECTED** — VACS00MUS0 (-20.30, 57.50) is an IGS site on Mauritius proper (Vacoas, central main island). It is republished live as an NTRIP stream on BKG IGS-IP and AUSCORS as of 2026-05-17. Prior framing ("no IGS CORS in Mauritius proper") was incorrect.
- **MIRAI QMUP00MUS:** A second mountpoint at (-20.50, 57.45) exists on the MIRAI caster (Japan; GEONET successor). MIRAI rebroadcasts select international stations; QMUP is the Mauritius entry.
- **Territory size:** Main island ~2,040 km² — VACS in Vacoas covers the bulk of the inhabited interior within ~30 km single-base RTK range; coastal extremities and Rodrigues remain out of range.
- **GIS platform:** Mauritius has an operational GIS portal (`gis.govmu.org`); no Survey-Division-operated GNSS correction service listed there.
- **RCMRD / AFREF:** No Mauritius-operated streaming NTRIP endpoint found in RCMRD or AFREF documentation; VACS rebroadcast is via IGS/BKG, not via a Mauritian operator.

## Negative Findings

- RTK2GO / Centipede: Zero MU mountpoints in any public sourcetable (verified 2026-05-17 via `py scripts/stations_by_radius.py -20.2 57.5 1500`; nearest Centipede stations are on Réunion ~222 km east)
- NTRIP-list.com Africa/Indian Ocean: Mauritius not listed
- ArduSimple country directory: Mauritius not listed with any NTRIP service
- mvarga1989 GNSS CORS list (GitHub): No Mauritius NTRIP endpoint
- No public caster address found in any indexed source as of 2026-05-12

## Most Recent Project Reference

**May 2016 RCMRD CORS feasibility workshop** — the last confirmed public event related to a Mauritius-operated CORS. No subsequent Survey-Division launch announcement, tender, or operational caster has been found. The IGS site at Vacoas predates the workshop and is operated under IGS / international agreements, not by the Survey Division.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS / EarthScope** — VACS (Vacoas, Mauritius proper) + REUN (Réunion) RINEX archives | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |
| **IGS station page VACS00MUS** | https://network.igs.org/VACS00MUS | Free (metadata) |

## Sources Consulted
- Survey Division, Ministry of Housing and Lands (Mauritius): https://housing.govmu.org/Pages/Dept%20and%20Org/Divisions/Survey/Survey.aspx
- Mauritius GIS portal: https://gis.govmu.org/SitePages/Index.aspx
- RCMRD — Regional Centre for Mapping of Resources for Development: https://www.rcmrd.org/
- IGS network page VACS00MUS: https://network.igs.org/VACS00MUS
- BKG NTRIP registration: https://igs.bkg.bund.de/ntrip/register
- Geoscience Australia AUSCORS registration: https://gnss.ga.gov.au/registration
- RTK2GO monitor (monitor.use-snip.com) — no MU mountpoints visible
- NTRIP-list.com/africa — Mauritius not listed as a national network
- ArduSimple RTK correction services directory — Mauritius not listed
- Local data: `py scripts/stations_by_country.py MUS` — VACS00MUS0 (auscors + igs_ip) + QMUP00MUS (mirai) = 3 MPs across 3 sources (2026-05-17 snapshot)
