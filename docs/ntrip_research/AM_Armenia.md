# Armenia [AM] - NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: NO public NTRIP RTK caster - ARMPOS hardware (12 CORS, 2013 Norwegian-funded) exists but the Cadastre Committee does not expose a public positioning service. One IGS station (ARUC00ARM) is rebroadcast via IGS-IP for scientific use. RTK2go / Centipede / EarthScope: zero AM stations.

## ARMPOS - Armenian Positioning System (no public NTRIP)

| Field | Value |
|---|---|
| operator | Cadastre Committee of the Republic of Armenia (Anshazh Guyki Kadastri Komite) - successor to the State Committee for Real Property Cadastre |
| landing_url | https://www.cadastre.am/en |
| access_url | https://eurogeographics.org/member/state-committee-real-property-cadastre-government-ra/ |
| access_type | restricted |
| coverage | 12 single-base CORS, ~50 km spacing across ~30,000 km^2: central plateau (Yerevan, Gyumri, Vanadzor) + southern Syunik (Kapan area). No public coverage map; no public NTRIP host:port. |
| num_stations | 12 (2013 Leica buildout; ~50 km spacing) |
| hobbyist_eligibility | no - no public registration channel; Cadastre Committee does not list a positioning service in its EuroGeographics member profile (verified 2026-05-23: "Positioning Service: No" in the National Services table) |
| sourcetable | none found - no public host:port published (checked: monitor.use-snip.com 2026-05-23; ntrip-list.com 2026-05-23; mvarga1989 GNSS CORS list 2026-05-23; ardusimple Armenia page 2026-05-23) |
| vrs | no - 2013 Mercell tender specifies single-base RTK + RINEX architecture; no NRTK upgrade documented (checked: Mercell tender doc 2026-05-23; cadastre.am 2026-05-23) |
| residency_required | yes - access is via the Cadastre Committee's bilateral channel; no remote / non-resident signup channel exists |
| stations_source | none published - no operator map or list; 12-station count and coverage inferred from 2013 tender document (checked: cadastre.am 2026-05-23; EuroGeographics profile 2026-05-23) |

ARMPOS was commissioned in 2013 by Leica Geosystems under a Norwegian-government-funded tender (NOK 9.8 million ~= USD 1.6 million at 2013 rates) supervised by Statens kartverk. Original design was single-base RTK + RINEX on GPS+GLONASS; any multi-constellation upgrade is undocumented publicly (checked: cadastre.am 2026-05-23; EuroGeographics member profile 2026-05-23; ardusimple Armenia page 2026-05-23; UN-GGIM 2024 country report 2026-05-23; WebSearch "ARMPOS Armenia Galileo BeiDou upgrade" 2026-05-23). cadastre.am (refetched 2026-05-23) describes cadastre, registration, topographic mapping, and e-Government services - no RTK, NTRIP, ARMPOS, or GNSS correction product surfaced. EuroGeographics member profile (refetched 2026-05-23) explicitly enumerates "Positioning Service: No" in the National Services table, which is the most authoritative current evidence that Armenia does not run an open positioning service. The ardusimple Armenia page (refetched 2026-05-23) explicitly states Armenia is not among countries with a national RTK service and lists no paid or commercial alternative. The earlier ARMREF02 frame reference appears only in third-party academic sources; no legal-instrument URL was located, so datum_epoch is omitted. The unrelated `armpos.online` domain is Ugandan inventory-management software, not the Armenian positioning service.

## IGS / EPN footprint

ARUC00ARM (Aruch village, 40.286 N, 44.086 E per network.igs.org refetched 2026-05-23) is an active IGS station: Septentrio POLARX5, Ashtech ASH701945C_M / SCIS antenna, multi-constellation in RINEX, GPS-only in real time. Mountpoint `ARUC00ARM0` is rebroadcast on `products.igs-ip.net:2101` (verified 2026-05-23 in local `data/igs_ip.sourcetable`; `py scripts/stations_by_country.py ARM` returns this single station). Baseline from ARUC to central Yerevan is ~46 km (great-circle from 40.286/44.086 to 40.18/44.51), marginal for single-base RTK (~53 mm + ppm at this distance, primer accuracy rules). IGS-IP registration required (BKG `register.rtcm-ntrip.org`); use governed by IGS data-use policy - research / non-commercial. Frame: IGS20 (IGS realisation of ITRF2020) - declared by IGS, not by an Armenian authority, so does not satisfy the operator-declaration rule for AM. The historical NSSP00ARM (Nor-Spitak, EPN since 2010-07-11) is RINEX-archive only.

## Hobbyist path

No free RTK option covers Armenian territory from a meaningful baseline:

- **rtk2go / Centipede / EarthScope** - zero AM stations (verified 2026-05-23 via `scripts/stations_by_country.py ARM` and ardusimple's Armenia page explicitly stating "Armenia is not among them").
- **Cross-border**: Georgia GeoCors (paid, ~270 km north to Tbilisi from Yerevan), Azerbaijan AzPOS (restricted, ~450 km east to Baku from Yerevan; closer Karabakh stations not open to Armenian users), Turkey TUSAGA-Aktif (free of charge but TC Kimlik No required; AM-TR land border closed) - none provide a free, open-registration, hobbyist-reachable baseline below NRTK hull limits.
- **Self-host** a personal base, or use Galileo HAS (~20-40 cm horizontal after convergence, satellite-delivered, free) where RTK is unavailable.

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| IGS station ARUC00ARM RINEX archive (CDDIS) | https://cddis.nasa.gov/ | Free non-commercial (account) |
| EarthScope GNSS data archive (NSSP legacy + ARUC) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA) |

## Sources

- Cadastre Committee of Armenia: https://www.cadastre.am/en (refetched 2026-05-23, no positioning content)
- EuroGeographics member profile (Armenia): https://eurogeographics.org/member/state-committee-real-property-cadastre-government-ra/ ("Positioning Service: No", refetched 2026-05-23)
- 2013 ARMPOS tender / technical description (Mercell mirror): https://www.mercell.com/lt-lt/m/file/getfile.ashx?id=36925319
- ArduSimple Armenia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-armenia/
- UN-GGIM Armenia 2024 country report: https://ggim.un.org/country-reports/documents/Armenia_2024-country-report.pdf
- IGS station page (ARUC00ARM): https://network.igs.org/ARUC00ARM
- ARKA news on 2013 Norwegian funding: https://arka.am/en/news/technology/armenia_s_real_estate_cadastre_will_receive_9_8_million_norwegian_krones_to_create_modern_geodetic_r/
- Local data 2026-05-23: `scripts/stations_by_country.py ARM` -> 1 IGS-IP station (ARUC00ARM0); rtk2go / Centipede / EarthScope return zero AM rows
