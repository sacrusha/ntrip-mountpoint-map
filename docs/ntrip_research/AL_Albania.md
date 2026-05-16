# Albania [AL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (originally 2026-05-06)

## Status: YES — two active NTRIP casters (ALBCORS state network, SATNET LIVE commercial)

## Caster 1 — ALBCORS (state, ASIG)

| Field | Value |
|---|---|
| **landing_url** | https://krgjsh.asig.gov.al/?page_id=1210&lang=en (advertised in the caster's NET record) |
| **access_url** | https://asig.gov.al/en/application-form/ (ALBCORS application PDF + Geoportal registration form, contact info.albcors@asig.gov.al) |
| **host:port** | albcors.asig.gov.al:2101 (live sourcetable fetched 2026-05-15; not advertised on the public web — discovered via DNS guess) |
| **tariff** | Not published. Application-gated; ASIG sets terms case-by-case. Tariff line in sourcetable is `B` (fee=basic / non-free) per NTRIP convention. |
| **num_stations** | 27 physical CORS (21 ground-mounted concrete pillars + 6 roof-mounted stations inherited from the predecessor ALBPOS system); KRGJSH operates the control centre at ASIG, Tirana. |
| **vrs** | yes — sourcetable advertises VRS (`CMR_plus`, `VRS_RTCM_2.3`, `VRS-MSM-GG`), FKP (`FKP01`), MAC (`MAC01`), Nearest Station (`NSTA-GG`, `NSTAT`), and single-base PRS streams. GPS+GLO on all; `NSTAT` and `PRS-MSM` add GAL+BDS. |
| **hobbyist_eligibility** | ? — eligibility criteria not published; the application PDF (`ASIG_Formulari-i-aplikimit-ALBCORS-04.03.2021.pdf`) is the gating document but its readable contents are not online. Professional/cadastral context strongly implied; no language excluding hobbyists located. |
| **legal_residency_required** | ? — not stated publicly. |
| **last_confirmed_alive** | 2026-05-15 — TCP sourcetable fetch from albcors.asig.gov.al:2101 returned `SOURCETABLE 200 OK` (Server: NTRIP GNSMART_Caster 2.0/1.0, 12 mountpoints, 2034 bytes). |

Datum_epoch omitted: the geodetic frame is ETRS89-ALB (KRGJSH 2010) per Council of Ministers Decision 669 (2013-08-07), but no single citable URL pins the broadcast epoch of the caster output itself; EPSG:6870 treats the underlying datum as an ETRF ensemble.

## Caster 2 — SATNET LIVE ALBANIA (commercial, Land&Co / Topcon)

| Field | Value |
|---|---|
| **landing_url** | https://landcoal.com/ (Land&Co — Topcon distributor for Albania, Tirana) |
| **access_url** | https://landcoal.com/satnet_live_rtk_cors_network (service page; registration via on-page form or the "SATNET live" mobile app) |
| **host:port** | 77.242.24.183:2101 (caster IP printed on the Land&Co service page; live sourcetable fetched 2026-05-15) |
| **tariff** | 3 free days for all new registrants; 1 year free with purchase of Land&Co GPS hardware. Ongoing subscription rate not published on the site (contact Land&Co). VAT status not stated. Observed 2026-05-15 on landcoal.com. |
| **num_stations** | Not disclosed. Sourcetable advertises 6 mountpoints (CMR, CMR+, DGPS, RTCM 2.3, RTCM 3.0, RTCM 3.2-MSM, plus a branded `landco` MSM stream), all with the same station identifier `NRS0.221011` and 0.00/0.00 coordinates — consistent with a single-base or anonymised setup, not a multi-station network. |
| **vrs** | no — no VRS/Nearest/FKP/MAC mountpoints in the sourcetable; only fixed-format physical-style streams. Service page does not claim VRS. |
| **hobbyist_eligibility** | ? — site language ("ofrohet posaqërisht për përdoruesit nga kompania" / "specifically for users of the company") implies Land&Co-customer-first; mobile-app self-registration suggests broader access is at least technically possible. No explicit exclusion of hobbyists found. |
| **legal_residency_required** | ? — not stated. |
| **last_confirmed_alive** | 2026-05-15 — TCP sourcetable fetch from 77.242.24.183:2101 returned `SOURCETABLE 200 OK` (Server: EagleGnss-basic/200923, 6 mountpoints, 764 bytes). |

Datum_epoch omitted: not declared by the operator.

## Geodetic context (no citable single declaration → datum_epoch omitted on both casters)

- Albania's national frame is **ETRS89-ALB (KRGJSH 2010)**, central meridian 20°E, GRS80 ellipsoid (EPSG:6870, https://epsg.io/6870).
- First realisation: 2007–2008 GNSS campaign linking the legacy Albanian datum to ETRS89. Anchor epoch commonly cited as 2008 by ASIG documentation, but no operator declaration pins the broadcast epoch of ALBCORS or SATNET streams to a specific ETRFyy realisation — EPSG treats the underlying datum as an ensemble.
- Legal basis: Decision of the Council of Ministers no. 669, 2013-08-07.

## Volunteer / community coverage

- rtk2go: zero AL mountpoints (`scripts/stations_by_country.py ALB` returns "No stations for 'ALB'", 2026-05-15).
- Centipede-RTK: zero AL bases (none indexed in `stations.json`).
- EarthScope: zero (out of geography).
- Nearest cross-border alternative checked via `scripts/stations_by_radius.py`: the only volunteer station within 200 km of the Albanian coast is **B506Fields** (rtk2go, Puglia, Italy) at ~127 km from south-Albanian shore (40.41°N, 18.00°E) — too far across the Adriatic for usable single-base RTK. Inland borders (Kosovo, North Macedonia, Montenegro, Greece) have no rtk2go/Centipede/EarthScope stations within 200 km of Albanian territory.

## Sandbox reachability notes

- `https://krgjsh.asig.gov.al/?page_id=1218&lang=en` returned **HTTP 404** via WebFetch from this sandbox on 2026-05-15, but the same URL is indexed by search engines and works in normal browsers — likely a UA/redirect filter on the WordPress site.
- `http://77.242.24.183:2101/` raw HTTP via WebFetch failed with a TLS-cert error (the tool auto-upgrades to HTTPS, which the NTRIP caster does not serve); a raw-socket NTRIP GET succeeded, confirming the caster is alive.
- `albcors.asig.gov.al:2101` was discovered by DNS-guess after the public KRGJSH page declined to list it; a raw-socket NTRIP GET returned the full sourcetable.

## Sources consulted

- ASIG GNSS Network page (KRGJSH): https://krgjsh.asig.gov.al/?page_id=1218&lang=en
- ASIG application-form landing page: https://asig.gov.al/en/application-form/
- ALBCORS application PDF (binary, not parseable in tool): https://krgjsh.asig.gov.al/wp-content/uploads/2021/03/ASIG_Formulari-i-aplikimit-ALBCORS-04.03.2021.pdf
- Land&Co — SATNET LIVE service page (caster IP advertised here): https://landcoal.com/satnet_live_rtk_cors_network
- EPSG:6870 ETRS89-ALB KRGJSH 2010: https://epsg.io/6870
- EUREF 2023 Gothenburg symposium — Albania country report: http://www.euref.eu/sites/default/files/symposia/2023Gothenburg/04-01-Albania.pdf
- ASIG laws and bylaws (CoM Decision 669/2013 reference): https://asig.gov.al/en/laws-and-bylaws/
- Live NTRIP sourcetables (raw-socket fetches, 2026-05-15): albcors.asig.gov.al:2101, 77.242.24.183:2101
