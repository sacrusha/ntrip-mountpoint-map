# Burkina Faso [BF] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21

## Status

BF-CORS national NTRIP caster (IGB, Trimble Pivot, 13 single-base RTK mountpoints + 1 multi-station VRS) is live and anonymously enumerable. Web `RegisterAccount.aspx` redirects to a maintenance error page and has done so since at least 2026-05-15; new-account self-service is currently broken. No community / volunteer NTRIP coverage in country.

## Caster — BF-CORS (IGB)

| Field | Value |
|---|---|
| **landing_url** | https://www.igb.bf/?page_id=47 (IGB GNSS-CORS page; instructs users to register at `www.bfcors.net`) |
| **access_url** | http://www.bfcors.net/ (Trimble Pivot Web portal home; `RegisterAccount.aspx` redirects to `DefaultErrorPage.aspx` with "service is temporarily not available due to maintenance or technical problems" — observed 2026-05-21) |
| **host:port** | `www.bfcors.net:2101` — confirmed `SOURCETABLE 200 OK` 2026-05-21 (`Server: NTRIP Trimble Ntrip Caster 4.1`, Content-Length 2754); probe requires `curl --http0.9` |
| **num_stations** | 13 physical CORS (DORI, DIAP, FADA, BF01, BOBO, DEDG, GAOA, MANG, OHGY, DPGO, IGB0, KBRI, TGDA), matching IGB's reported 9-station 2011 deployment (Gampela, Manga, Fada, Diapaga, Dori, Ouahigouya, Dédougou, Bobo-Dioulasso, Gaoua) plus the 2018 4-station capital densification (Ouagadougou/IGB, Koubri, Dapélogo, Tanguen-Dassouri). Sourcetable also exposes `MultiStation_RTCM31` (BFA, solution=1 → network solution, not a physical station), `BurkinaDGNSSMulti` (BFA, format field blank, carrier=2, solution=1 — identifier names DGNSS but the sourcetable row itself is not the carrier=0 row our pipeline rule targets), and 1 `VRSRTCM32` row tagged country=DEU with blank format — likely an unconfigured Trimble Pivot template entry, not an actual German passthrough. |
| **vrs** | yes — `MultiStation_RTCM31` BFA, RTCM 3.1, solution=1 |
| **tariff** | not published; no public tariff page pre-login |
| **hobbyist_eligibility** | ? — IGB's stated audience is "géomètres, cadastreurs, cartographes"; no explicit hobbyist tier; registration approval gates access |
| **legal_residency_required** | ? — not stated |
| **last_confirmed_alive** | 2026-05-22 — sourcetable returned `SOURCETABLE 200 OK` with 13 BFA single-base + 1 BFA `MultiStation_RTCM31` + 1 BFA `BurkinaDGNSSMulti` + 1 DEU-tagged `VRSRTCM32` template row; `http://www.bfcors.net/` returns HTTP 200 (Microsoft-IIS/8.0); `RegisterAccount.aspx` still redirects to `DefaultErrorPage.aspx` |
| **datum_epoch** | omitted — no citable operator declaration. IGB references a "système de référence national" without specifying datum or epoch in any public document |

Sourcetable mountpoint rows publish `lat=0/lon=0` (Trimble Pivot default obfuscation) — the published station-city correspondence comes from IGB, not the sourcetable.

**Pipeline note**: every BFA single-base row carries `nmea=1, solution=0`. Per `data/rtk_map.json` BF-CORS has no `endpoints[]` configured (tier `weird`, RINEX/contact-only), so the pipeline does not parse this caster. If BF-CORS is ever wired into endpoints[], an `nmea_filter=False` override would be required to retain the 13 single-base stations — the `nmea=1` flag is misset by the Trimble Pivot template, not a real VRS GGA requirement.

## Context

- IGB tutelle: Ministry of Infrastructure; technical management of the network since September 2012.
- 2010 procurement: MCA-BF (Millennium Challenge Account Burkina Faso) signed a 48-month contract with Trimble Europe BV for the original 9-station deployment, ~700 MFCFA.
- 2018: 4-station capital densification funded from state budget.
- Academic confirmation of historical operation: BF01 (Ouagadougou) raw GNSS data 2013–2021 used in a 2024 ionospheric VTEC publication.
- Security/political context: 2022 military coup; Burkina Faso, Mali and Niger withdrew from ECOWAS and formed the Alliance of Sahel States (January 2025); jihadist insurgency affects a large share of national territory. Operational continuity of remote stations is plausibly degraded; the persistent `RegisterAccount.aspx` maintenance error is consistent with reduced operator capacity.

## Volunteer / Free Coverage

None inside the country. `scripts/stations_by_country.py BFA` returns no stations; `scripts/stations_by_radius.py 12.37 -1.52 200` returns nothing within 200 km of Ouagadougou. No rtk2go, no Centipede, no GEODNET/ONOCOY/Emlid bases in BF. EarthScope NOTA scope is Americas-only. Nearest cross-border CORS infrastructure of any kind (RECI in Côte d'Ivoire, IGN Bénin, IGN Niger, IGN Mali) is well beyond single-base RTK range and equally non-public.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| IGB BF-CORS RINEX archive (13 stations; contact IGB; portal section gated) | https://www.igb.bf/?page_id=47 | not published |
| SONEL station OUAG (Ouagadougou, AMMA → IGS contribution since 2011) | https://www.sonel.org/spip.php?page=gps&idStation=2561 | free |
| IGS / CDDIS data archive (if/when BF stations federate) | https://cddis.nasa.gov/Techniques/GNSS/IGS_Summary.html | free non-commercial |

## Probes (2026-05-21)

| Endpoint | Result |
|---|---|
| `http://www.bfcors.net/` | HTTP 200, Microsoft-IIS/8.0 |
| `http://www.bfcors.net/RegisterAccount.aspx` | HTTP 200 after redirect to `DefaultErrorPage.aspx?aspxerrorpath=/RegisterAccount.aspx` ("service is temporarily not available") |
| `http://www.bfcors.net:2101/` (with `--http0.9`) | `SOURCETABLE 200 OK`, `Server: NTRIP Trimble Ntrip Caster 4.1`, 16 STR rows (13 BFA single-base RTCM31 + 1 BFA `MultiStation_RTCM31` + 1 BFA `BurkinaDGNSSMulti` + 1 DEU-tagged `VRSRTCM32` template row). All single-base rows: `carrier=2; nmea=1; solution=0`. All single-base coords reported `lat=0/lon=0`. |

## Sources

- IGB GNSS-CORS page — https://www.igb.bf/?page_id=47
- IGB home page — https://www.igb.bf/
- BF-CORS Trimble Pivot Web — http://www.bfcors.net/
- BF-CORS NTRIP caster — `http://www.bfcors.net:2101/` (probed 2026-05-21)
- IGB contact email observed on igb.bf: infogeo.bf@gmail.com
- 2024 ionospheric VTEC paper on BF01 — https://www.researchgate.net/publication/379545036
- SONEL OUAG — https://www.sonel.org/spip.php?page=gps&idStation=2561
- Local: `py scripts/stations_by_country.py BFA` → no stations; `py scripts/stations_by_radius.py 12.37 -1.52 200` → no stations
