# Armenia [AM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (prior: 2026-05-12, 2026-05-06)

## Status: ARMPOS exists on paper (12 physical CORS commissioned 2013) but no public NTRIP host:port has ever been published; EuroGeographics lists Armenia's national positioning service as "No"

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
| **vrs** | no (single-base design per the 2013 tender) |
| **hobbyist_eligibility** | no |
| **legal_residency_required** | ? (no open registration form to inspect) |
| **last_confirmed_alive** | 2026-05-15 — cadastre.am operator portal reachable; no NTRIP endpoint to probe; EuroGeographics member page lists "Positioning Service: No" for Armenia |

(datum_epoch omitted — ARMREF02 is widely referenced in third-party sources but no official Armenian government declaration URL was locatable in 2026-05-15 research.)

## ARMPOS — what is known

- **Commissioning**: Installed by Leica Geosystems under a 2013 tender funded by the Norwegian government (NOK 9.8 million ≈ USD 1.6 million at 2013 rates), supervised by the Norwegian Mapping Authority (Statens kartverk). Sole owner: the Cadastre Committee.
- **Design**: 12 stations, single-base (the 2013 tender describes real-time NTRIP RTK at metre / sub-metre / centimetre tiers and post-processing at cm / sub-cm; no VRS or network-RTK module specified).
- **Constellations**: GPS + GLONASS (original Leica L1+L2 infrastructure; any multi-constellation upgrade is undocumented publicly).
- **Reference frame**: Third-party sources name ARMREF02 as Armenia's national rectangular system. No legal-instrument URL found; figure cited for context only.
- **Coverage area**: Stations distributed across the central plateau (Yerevan / Gyumri / Vanadzor) and the southern Syunik highlands (Kapan area).

## Public access — current state

- **No public NTRIP host:port has been published.** Verified absent from rtk2go (monitor.use-snip.com), ntrip-list.com (no AM entries in Europe section), IGS station-resources, GitHub mvarga1989/The-list-of-GNSS-CORS-RTK-networks, and ArduSimple's country selector (Armenia not listed).
- **EuroGeographics member page** for the Cadastre Committee (2026-05-15) explicitly enumerates "Positioning Service: No" in the National Services table. This is the most authoritative current evidence that Armenia does not run an open positioning service.
- **cadastre.am and e-cadastre.am** portals (probed 2026-05-15, HTTP 200 via WebFetch) describe cadastre, registration, topographic mapping, and e-Government services. Neither surfaces RTK, NTRIP, ARMPOS, or any GNSS correction product.
- **No active user community presence**: no Armenian-language surveyor forum threads, no rtk2go submissions, no Centipede submissions surfaced.

## IGS / EPN footprint (post-processing only)

- **NSSP (NSSP00ARM)** — Nor-Spitak (Spitak region) — was an EPN station operated by JPL. Per EPN Central Bureau, **former EPN station since 2010-07-11**; not part of the active EUREF network. Historical RINEX may still be available via the IGS / CDDIS archives.
- **ARTU is NOT in Armenia** — prior research conflated this. ARTU is the IGS station at Arti, Russia (Sverdlovsk Oblast). Removed.
- **No active IGS station in Armenia is currently listed** in the IGS network resources (2026-05-15).
- A Russian GLONASS ground complex exists on the Byurakan Astrophysical Observatory campus (announced 2018, news.am). It is a military/state station, not a civilian NTRIP service.

## Volunteer / community / commercial casters

- **rtk2go**: zero AM stations (`scripts/stations_by_country.py ARM` → "No stations for 'ARM'", 2026-05-15).
- **Centipede-RTK**: zero AM stations (same script; Centipede coverage in this repo's data is empty for Armenia).
- **EarthScope / GAGE**: no AM stations (same script). The legacy NSSP RINEX is held in IGS/CDDIS, not EarthScope's user-facing GNSS Archive.
- **Radius probe**: `scripts/stations_by_radius.py 40.18 44.51 100` (Yerevan, 100 km) → "No stations within 100 km" on 2026-05-15.
- **GEODNET / ONOCOY / RTKdata / Skylark**: no Armenia ground stations confirmed in 2026-05-15 searches. Swift Navigation's Skylark is a satellite-PPP product and is unrelated to a local NTRIP caster.

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

## Live-probe results (2026-05-15)

| URL | Method | Result |
|---|---|---|
| https://www.cadastre.am/en | WebFetch | 200 — no RTK content |
| https://www.e-cadastre.am/en | WebFetch | 200 — no RTK content |
| https://eurogeographics.org/member/state-committee-real-property-cadastre-government-ra/ | WebFetch | 200 — "Positioning Service: No" |
| https://www.ardusimple.com/rtk-correction-services-in-your-country/ | WebFetch | 200 — Armenia not in list (page is JS-rendered; visible portion shows no AM) |
| http://www.epncb.oma.be/_networkdata/siteinfo4onestation.php?station=NSSP00ARM | WebFetch | 403 from sandbox; WebSearch snippet confirms NSSP is a former EPN station as of 2010-07-11 |
| http://www.igs.org/igsnetwork/network_by_site.php?site=artu | WebFetch | 404 (URL deprecated) |
| https://monitor.use-snip.com/ | WebFetch | TLS cert SAN mismatch from sandbox; no AM streams expected (no AM submissions in any community list) |

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
- Local data verification (2026-05-15): `scripts/stations_by_country.py ARM` (no entries), `scripts/stations_by_radius.py 40.18 44.51 100` (no stations within 100 km of Yerevan)
- news.am on Byurakan GLONASS station (context only, military): https://news.am/eng/news/486296.html
