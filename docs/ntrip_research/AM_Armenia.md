# Armenia [AM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-15, 2026-05-12, 2026-05-06)

## Status: ARMPOS exists on paper (12 physical CORS commissioned 2013) but no public NTRIP host:port has ever been published; EuroGeographics still lists Armenia's national positioning service as "No". One IGS station (ARUC00ARM, Aruch) is broadcast in real time via IGS-IP — single-base, scientific use only.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | None found |
| **Network name** | ARMPOS — Armenian Positioning System (CORS network) |
| **Operator** | Cadastre Committee of the Republic of Armenia (Անշարժ Գույքի Կադաստրի Կոմիտե) — successor to the State Committee for Real Property Cadastre |
| **landing_url** | https://www.cadastre.am/en (operator homepage — no positioning service surfaced) |
| **access_url** | None — no public sign-up page exists; Cadastre Committee hotline +374-60-474205 is the only published contact |
| **host:port** | Not publicly listed |
| **tariff** | Not publicly listed |
| **num_stations** | 12 physical single-base CORS (per 2013 Norwegian-funded buildout; ~50 km spacing across ~30,000 km²) |
| **vrs** | n/a — no public service exists (2013 tender described single-base design; never exposed publicly) |
| **hobbyist_eligibility** | n/a — no public service exists |
| **legal_residency_required** | ? (no open registration form to inspect) |
| **last_confirmed_alive** | 2026-05-17 — cadastre.am operator portal reachable (latest news 2025-11-07, no GNSS mention); no NTRIP endpoint to probe; EuroGeographics member page still lists "Positioning Service: No" for Armenia (re-fetched 2026-05-17) |

(datum_epoch omitted — ARMREF02 is widely referenced in third-party sources but no official Armenian government declaration URL was locatable in 2026-05-15 research.)

## ARMPOS — what is known

- **Commissioning**: Installed by Leica Geosystems under a 2013 tender funded by the Norwegian government (NOK 9.8 million ≈ USD 1.6 million at 2013 rates), supervised by the Norwegian Mapping Authority (Statens kartverk). Sole owner: the Cadastre Committee.
- **Design**: 12 stations, single-base (the 2013 tender describes real-time NTRIP RTK at metre / sub-metre / centimetre tiers and post-processing at cm / sub-cm; no VRS or network-RTK module specified).
- **Constellations**: GPS + GLONASS (original Leica L1+L2 infrastructure; any multi-constellation upgrade is undocumented publicly).
- **Reference frame**: Third-party sources name ARMREF02 as Armenia's national rectangular system. No legal-instrument URL found; figure cited for context only.
- **Coverage area**: Stations distributed across the central plateau (Yerevan / Gyumri / Vanadzor) and the southern Syunik highlands (Kapan area).

## Public access — current state

- **No public NTRIP host:port has been published.** Verified absent from rtk2go (monitor.use-snip.com), ntrip-list.com (no AM entries in Europe section), IGS station-resources, GitHub mvarga1989/The-list-of-GNSS-CORS-RTK-networks, and ArduSimple's country selector (Armenia not listed).
- **EuroGeographics member page** for the Cadastre Committee (re-fetched 2026-05-17) explicitly enumerates "Positioning Service: No" in the National Services table. This is the most authoritative current evidence that Armenia does not run an open positioning service.
- **cadastre.am and e-cadastre.am** portals (re-probed 2026-05-17, HTTP 200 via WebFetch) describe cadastre, registration, topographic mapping, and e-Government services. Neither surfaces RTK, NTRIP, ARMPOS, or any GNSS correction product. Latest news 2025-11-07 (cadastre service-office visit; reverse-mortgage law) — no GNSS content.
- **No active user community presence**: no Armenian-language surveyor forum threads, no rtk2go submissions, no Centipede submissions surfaced.

## IGS / EPN footprint

- **ARUC00ARM** — Aruch-Yerevan (40.286 N, 44.086 E, 1222 m). Active IGS station: Septentrio POLARX5 receiver, Ashtech ASH701945C_M / SCIS antenna, multi-constellation (GPS+GLO+GAL+BDS+QZS+IRNSS) in RINEX, GPS-only in real time. Real-time stream rebroadcast on `products.igs-ip.net:2101` (mountpoint `ARUC00ARM0` present in `data/igs_ip.sourcetable`, 39 km from Yerevan, verified 2026-05-17 via `py scripts/stations_by_country.py ARM`). **NOT on EUREF-IP** — local `data/euref_ip.sourcetable` grep for `ARUC` returns no matches (2026-05-17); IGS-IP is the only NTRIP rebroadcast path. IGS-IP registration required (BKG / `register.rtcm-ntrip.org`); use governed by IGS data-use policy — research/non-commercial. Datum: IGS20 (IGS realisation of ITRF2020) — declared by IGS, not by an Armenian authority, so it does **not** satisfy the operator-declaration rule for the AM datum_epoch field.
- **NSSP (NSSP00ARM)** — Nor-Spitak — former EPN station since 2010-07-11; historical RINEX in IGS / CDDIS archives only.
- **ARTU is NOT in Armenia** — ARTU is at Arti, Russia (Sverdlovsk Oblast).
- A Russian GLONASS ground complex exists on the Byurakan Astrophysical Observatory campus (announced 2018, news.am). Military/state, not a civilian NTRIP service.

## Volunteer / community / commercial casters

- **rtk2go**: zero AM stations (`scripts/stations_by_country.py ARM`, 2026-05-17 — only IGS-IP ARUC returned).
- **Centipede-RTK**: zero AM stations.
- **EarthScope / GAGE**: no AM stations (out of geography). Legacy NSSP RINEX held in IGS/CDDIS, not EarthScope.
- **IGS-IP**: 1 AM station — ARUC00ARM0 (Aruch, 39 km from Yerevan); single-base, scientific use; see preceding section.
- **Radius probe**: `scripts/stations_by_radius.py 40.18 44.51 100` (Yerevan, 100 km) → ARUC at 39.1 km on 2026-05-17 (was empty 2026-05-15 before IGS-IP sourcetable refresh added this row).
- **GEODNET / ONOCOY / RTKdata / Skylark**: no Armenia ground stations confirmed. Skylark is satellite-PPP, unrelated.

## Nearest viable cross-border alternatives (context, not within ~50 km of any major Armenian city)

- **Georgia — GeoCors** (~150 km north of Yerevan to Tbilisi): paid Leica SmartNet-style service, restricted.
- **Azerbaijan — AzPOS** (~150 km east to Baku core, but stations along the AM-AZ frontier are likely closer): paid via AzCarto subsidiary, restricted.
- **Turkey — TUSAGA-Aktif**: free of charge but residency / official-use restricted; stations exist along the AM-TR border but the closed AM-TR land border and registration restrictions make practical use unlikely for a hobbyist in Armenia.
- **Iran — IRPPP**: no public sourcetable located.
- **Practical takeaway**: there is no free, open-registration RTK option that covers Armenian territory from across the border within a meaningful baseline (<~35 km).

## Practical workarounds for hobbyists in Armenia

- Self-host a local base station (any L1/L2 or L1/L5 receiver published over Wi-Fi/cellular) and operate single-baseline RTK against your own rover.
- Use satellite-delivered PPP/SSR: Galileo HAS (free, ~20–40 cm horizontal after convergence), or paid services (Trimble RTX, Fugro StarFix). These do not require a local NTRIP caster.
- For post-processing-grade work, IGS/CDDIS holds historical NSSP RINEX (2002–2010); modern coverage is sparse.

## Live-probe results (2026-05-17)

| URL | Method | Result |
|---|---|---|
| https://www.cadastre.am/en | WebFetch | 200 — latest news 2025-11-07; no RTK content |
| https://www.e-cadastre.am/en | WebFetch | 200 — no RTK content |
| https://eurogeographics.org/member/state-committee-real-property-cadastre-government-ra/ | WebFetch | 200 — "Positioning Service: No" (verbatim) |
| https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-armenia/ | WebFetch | 200 — page explicitly states "Armenia is not among them" (no national RTK), lists rtk2go/IGS/Earthscope/Galileo-HAS as fallbacks |
| https://network.igs.org/ARUC00ARM | WebFetch | 200 — station info, Septentrio POLARX5, last RINEX 2026-05-13 |

## Sources

- 2013 ARMPOS tender / technical description (Mercell mirror): https://www.mercell.com/lt-lt/m/file/getfile.ashx?id=36925319
- Cadastre Committee of Armenia: https://www.cadastre.am/en
- e-Cadastre portal: https://www.e-cadastre.am/en
- EuroGeographics member page (Armenia): https://eurogeographics.org/member/state-committee-real-property-cadastre-government-ra/
- UN-GGIM Armenia 2024 country report (NSDI): https://ggim.un.org/country-reports/documents/Armenia_2024-country-report.pdf
- UNOOSA "GNSS: Armenian Experience" (2010, historical): https://www.unoosa.org/documents/pdf/psa/activities/2010/moldova/presentations/3-6.pdf
- ARKA news on 2013 Norwegian funding: https://arka.am/en/news/technology/armenia_s_real_estate_cadastre_will_receive_9_8_million_norwegian_krones_to_create_modern_geodetic_r/
- EPN Central Bureau station page (NSSP00ARM): http://www.epncb.oma.be/_networkdata/siteinfo4onestation.php?station=NSSP00ARM
- EUREF station list: https://epncb.oma.be/_networkdata/stationlist.php
- IGS network resources: https://igs.org/network-resources/
- GitHub mvarga1989 / GNSS CORS list: https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- ArduSimple country selector: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- NTRIP-list.com Europe: https://ntrip-list.com/europe/
- IGS station page (ARUC00ARM): https://network.igs.org/ARUC00ARM
- Ardusimple Armenia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-armenia/
- Local data verification (2026-05-17): `scripts/stations_by_country.py ARM` → 1 IGS-IP station (ARUC00ARM0); `scripts/stations_by_radius.py 40.18 44.51 100` → ARUC at 39.1 km
- news.am on Byurakan GLONASS station (context only, military): https://news.am/eng/news/486296.html
