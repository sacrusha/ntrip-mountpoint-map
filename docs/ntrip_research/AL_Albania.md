# Albania [AL] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-15)
**status:** YES — ALBCORS (state, ASIG) + SATNET LIVE (commercial, Land&Co). Both casters confirmed live by direct sourcetable fetch 2026-05-21. No volunteer ALB bases in any free network.

## Caster 1 — ALBCORS (state, ASIG)

| field | value |
|---|---|
| landing_url | https://krgjsh.asig.gov.al/?page_id=1210&lang=en (operator NET record advertises this URL) |
| access_url | https://asig.gov.al/en/application-form/ (ALBCORS application PDF + Geoportal registration form, contact `info.albcors@asig.gov.al`) |
| operator | ASIG — Autoriteti Shtetëror për Informacionin Gjeohapësinor / KRGJSH control centre |
| host:port | `albcors.asig.gov.al:2101` — live `SOURCETABLE 200 OK` from `NTRIP GNSMART_Caster 2.0/1.0`, 11 STR rows + 1 NET + 1 CAS, 2034 bytes, 2026-05-21. Hostname confirmed as operator-canonical: the NET record in the live sourcetable lists `https://krgjsh.asig.gov.al/?page_id=1210&lang=en` as both the `info_url` and `misc_url` fields, identifying ASIG as the caster operator. The hostname `albcors.asig.gov.al` resolves to this caster; it is not advertised on the ASIG website pages accessible via WebFetch but is implied by the subdomain pattern and confirmed by the live NET record. |
| num_stations | 27 physical CORS (21 ground-mounted concrete pillars + 6 roof-mounted stations inherited from the predecessor ALBPOS system) — confirmed verbatim 2026-05-21 from the page_id=1210 page. |
| vrs | yes — sourcetable advertises VRS (`CMR_plus`, `VRS_RTCM_2.3`, `VRS-MSM-GG`), FKP (`FKP01`), MAC (`MAC01`), Nearest Station (`NSTA-GG`, `NSTAT`), single-base PRS streams (`PRS01`, `PRS-LEGACY`, `PRS-MSM`) and a DGPS stream (out of scope). GPS+GLO on most; `NSTAT` and `PRS-MSM` add GAL+BDS. |
| tariff | Not published on operator pages — date observed 2026-05-21, sources https://krgjsh.asig.gov.al/?page_id=1210&lang=en and https://asig.gov.al/en/application-form/ (neither lists fees). Application-gated; specific fees not publicly disclosed. Currency unknown (ALL or EUR likely but not confirmed). VAT status not stated. NET record tariff field = `B` (fee=basic) per NTRIP convention. |
| hobbyist_eligibility | ? — eligibility criteria not published. The application PDF (`ASIG_Formulari-i-aplikimit-ALBCORS-04.03.2021.pdf`) is the gating document but contents not extractable from sandbox. Professional/cadastral context strongly implied; no language excluding hobbyists found. |
| legal_residency_required | ? — not stated publicly |
| last_confirmed_alive | 2026-05-21 — `albcors.asig.gov.al:2101` `SOURCETABLE 200 OK` from `NTRIP GNSMART_Caster 2.0`, 11 STR rows + NET + CAS records, 2034 bytes |

`datum_epoch` omitted: national frame is **ETRS89-ALB (KRGJSH 2010)**, CM 20°E, GRS80 (EPSG:6870) per Council of Ministers Decision 669 (2013-08-07). EUREF 2023 Gothenburg KRGJSH country report cites ETRF2000 epoch 2014.177, but no operator URL pins broadcast epoch of the caster output and EPSG treats the underlying datum as an ensemble.

### ALBCORS sourcetable (2026-05-21)

| Mount | Format | Method | Systems |
|---|---|---|---|
| `CMR_plus` | CMR+ | VRS | GPS+GLO |
| `VRS_RTCM_2.3` | RTCM 2.3 | VRS | GPS+GLO |
| `VRS-MSM-GG` | RTCM 3.2 | VRS | GPS+GLO |
| `MAC01` | RTCM 3.1 | MAC | GPS+GLO |
| `FKP01` | RTCM 3.1 | FKP | GPS+GLO |
| `NSTA-GG` | RTCM 3.2 | Nearest | GPS+GLO |
| `NSTAT` | RTCM 3.2 | Nearest | GPS+GLO+GAL+BDS |
| `PRS01` | RTCM 3.0 | PRS (single base) | GPS+GLO |
| `PRS-LEGACY` | RTCM 3.0 | PRS | GPS+GLO |
| `PRS-MSM` | RTCM 3.2 | PRS | GPS+GLO+GAL+BDS |
| `DGPS_ALBCORS` | RTCM 2.1 | DGPS | GPS+GLO (out of scope) |

## Caster 2 — SATNET LIVE ALBANIA (commercial)

| field | value |
|---|---|
| landing_url | https://landcoal.com/ (Land&Co — Topcon distributor for Albania, Tirana) |
| access_url | https://landcoal.com/satnet_live_rtk_cors_network (service page; registration via on-page form or the "SATNET live" mobile app) |
| operator | Land&Co (Topcon distributor, Tirana) |
| host:port | `77.242.24.183:2101` — live `SOURCETABLE 200 OK` from `EagleGnss-basic/200923`, 6 STR rows, 764 bytes, 2026-05-21. Caster IP printed on the Land&Co service page. |
| num_stations | Not disclosed. Sourcetable advertises 6 mountpoints all sharing station identifier `NRS0.221011` and 0.00/0.00 coordinates — consistent with a single-base or anonymised setup, not a multi-station network. The service page does not state a station count. Land&Co service page (WebFetch 2026-05-21) states coverage in "central Albania and parts of Kosovo and Macedonia." No per-tier source URL exists for the ongoing subscription rate. |
| vrs | no — no VRS/Nearest/FKP/MAC mountpoints in sourcetable; only fixed-format physical-style streams. Service page does not claim VRS. |
| tariff | 3 free days for all new registrants; 1 year free with purchase of Land&Co GPS hardware. Ongoing subscription rate not published on the site — contact Land&Co. No per-tier pricing source available. VAT status not stated. Observed 2026-05-21. |
| hobbyist_eligibility | ? — site language ("ofrohet posaqërisht për përdoruesit nga kompania" / "specifically for users of the company") implies Land&Co-customer-first; mobile-app self-registration suggests broader access is technically possible. No explicit exclusion of hobbyists found. |
| legal_residency_required | ? — not stated |
| last_confirmed_alive | 2026-05-21 — `77.242.24.183:2101` SOURCETABLE 200 OK, EagleGnss-basic/200923, 6 STR rows: `RTCM23`, `RTD`, `CMR`, `RTCM30`, `RTCM32-MSM`, `landco`. All stamped station `NRS0.221011`, lat=lon=0.00. |

`datum_epoch` omitted: not declared by operator.

## Geodetic context

- Albania's national frame is **ETRS89-ALB (KRGJSH 2010)**, CM 20°E, GRS80 (EPSG:6870, https://epsg.io/6870).
- First realisation: 2007-2008 GNSS campaign linking the legacy Albanian datum to ETRS89. EUREF 2023 Gothenburg KRGJSH country report (http://www.euref.eu/sites/default/files/symposia/2023Gothenburg/04-01-Albania.pdf) gives **ETRF2000 @ epoch 2014.177**. No ASIG-operator declaration pins the broadcast epoch of ALBCORS or SATNET streams to a specific ETRFyy realisation — EPSG treats the underlying datum as an ensemble, so the operator-declaration rule is not satisfied and `datum_epoch` is omitted on both casters.
- Legal basis: Decision of the Council of Ministers no. 669, 2013-08-07.

## Volunteer / community coverage

- rtk2go: zero AL mountpoints (`py scripts/stations_by_country.py ALB` returns "No stations" 2026-05-21).
- Centipede-RTK: zero AL bases.
- EarthScope: zero (out of geography).
- Nearest cross-border alternative checked via `stations_by_radius.py`: the only volunteer station within 200 km of the Albanian coast is `B506Fields` (rtk2go, Puglia, Italy) at ~127 km from south-Albanian shore (40.41°N, 18.00°E) — too far across the Adriatic for usable single-base RTK. Inland borders (XK, MK, ME, GR) have no rtk2go / Centipede / EarthScope stations within 200 km of Albanian territory.

## Sandbox reachability notes

- `https://krgjsh.asig.gov.al/?page_id=1218&lang=en` still returns HTTP 404 via WebFetch 2026-05-21 (same on 2026-05-15 and 2026-05-17); accessible in normal browsers — UA/redirect filter on the WordPress site.
- `https://krgjsh.asig.gov.al/?page_id=1210&lang=en` returns 200 to WebFetch: confirms 27 CORS, ETRS89 realisation.
- `https://asig.gov.al/en/application-form/` returns 200 but only links the ALBCORS application PDF (`https://asig.gov.al/wp-content/uploads/2023/10/ASIG_FormALBCORS.pdf`); PDF text not extractable from sandbox.
- **Naming note**: ArduSimple's Albania page refers to the state caster as **"ALBPOS"** (legacy name); operator-published name is **ALBCORS** (per `krgjsh.asig.gov.al/?page_id=1210`). ALBCORS inherited 6 of ALBPOS's rooftop stations and replaced the rest with concrete-pillar CORS.

## Sources

- ASIG GNSS Network page (KRGJSH, page_id=1210): https://krgjsh.asig.gov.al/?page_id=1210&lang=en (WebFetch 2026-05-21 — 27 stations confirmed)
- ASIG application-form landing page: https://asig.gov.al/en/application-form/
- ALBCORS application PDF (binary, not parseable): https://krgjsh.asig.gov.al/wp-content/uploads/2021/03/ASIG_Formulari-i-aplikimit-ALBCORS-04.03.2021.pdf
- Land&Co SATNET LIVE service page (caster IP advertised): https://landcoal.com/satnet_live_rtk_cors_network
- EPSG:6870 ETRS89-ALB KRGJSH 2010: https://epsg.io/6870
- EUREF 2023 Gothenburg — Albania country report: http://www.euref.eu/sites/default/files/symposia/2023Gothenburg/04-01-Albania.pdf
- ASIG laws and bylaws (CoM Decision 669/2013): https://asig.gov.al/en/laws-and-bylaws/
- Live caster sourcetables (raw-socket fetches, 2026-05-21):
  - `albcors.asig.gov.al:2101` — SOURCETABLE 200 OK, 11 STR rows + NET + CAS, 2034 bytes
  - `77.242.24.183:2101` — SOURCETABLE 200 OK, EagleGnss-basic, 6 STR rows, 764 bytes
- ArduSimple AL (uses "ALBPOS" legacy name): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-albania/
