# Armenia [AM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (originally 2026-05-06)

## Status: ARMPOS exists (12 physical CORS) but access restricted; no public NTRIP host:port

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No public endpoint |
| **Network name** | ARMPOS — Armenian Continuously Operating Reference Station network |
| **Operator** | State Committee for Real Property Cadastre of the Republic of Armenia (Անշարժ Գույքի Կադաստրի Պետական Կոմիտե / Cadastre Committee) |
| **host:port** | Not publicly listed — application required |
| **tariff** | Not publicly listed (intended for licensed surveyors and government cadastre users) |
| **num_stations** | 12 physical single-base CORS (full national coverage; ~50 km spacing across ~30,000 km²) |
| **VRS** | No — single-base design |
| **hobbyist_eligibility** | No confirmed hobbyist path; access restricted to licensed surveyors / government users |
| **legal_residency_required** | Unclear; no open registration form found |
| **registration** | None public — contact `cadastre.am` |
| **last_confirmed_alive** | cadastre.am portal reachable 2026-05-12; NTRIP endpoint not publicly probable |

## ARMPOS — Network Details

**Commissioning**: Installed by Leica Geosystems in 2013 under funding from the Norwegian government (NOK 9.8 million, ~$1.6 million at 2013 rates) and supervision of the Norwegian Mapping Authority (Statens kartverk / Kartverket).

**Sole owner**: State Committee for Real Property Cadastre — legal and technical mandate for establishment, operations, and maintenance.

**Reference frame**: ARMREF02 (Armenian national datum, ITRF-aligned).

**Capabilities (per project documentation)**: Real-time NTRIP RTK at metre, sub-metre, and centimetre tiers; post-processing at centimetre / sub-centimetre. Signals: GPS + GLONASS (original Leica L1+L2 infrastructure; multi-constellation upgrade status not publicly documented).

**Coverage**: 12 stations spaced ~50 km apart across Armenian territory (~30,000 km²) — adequate inter-station spacing for L1+L2 single-base RTK if access were open. Network includes stations across the densely populated central plateau (Yerevan, Gyumri, Vanadzor regions) and southern highlands (Syunik / Kapan area).

**Public access**: No open self-service registration. No NTRIP host:port has been published in any NTRIP directory (rtk2go, ntrip-list.com, IGS, mvarga1989 GitHub list, ArduSimple country selector). The Cadastre Committee operates the e-cadastre.am and cadastre.am portals but does not surface RTK as a user-facing service. The intended user base is the licensed-surveyor / cadastre community.

## Most Recent Project Announcement

No public announcement of an open hobbyist tier or expansion as of 2026-05-12. Armenia's NSDI programme (supported by EuroGeographics, ADB project 54388-001) and Cadastre Committee modernisation efforts continue, but real-time RTK corrections remain a restricted-access service.

- e-cadastre.am cadastral portal: https://www.e-cadastre.am/en (live 2026-05-12)
- cadastre.am main portal: https://www.cadastre.am/en
- ADB project 54388-001 (NSDI support): https://www.adb.org/projects/54388-001/main

## Context Notes

- **maparmenia.am geoportal** (launched July 2022) — national cadastral, orthophoto, hydrographic layers. No real-time GNSS correction service surfaced.
- **EPN / IGS stations**: at least one IGS site historically (ARTU, Artashat) provides post-processing RINEX through the IGS global archive; not operated as a hobbyist NTRIP stream.
- **EuroGeographics cooperation**: The Cadastre Committee is an EuroGeographics member; cooperation focuses on NSDI implementation, not real-time RTK.
- **Regional context**: Armenia is bracketed by AzPOS (Azerbaijan, ~37 CORS, paid via AzCarto subsidiary) to the east and GeoCors (Georgia, 26 CORS, paid Leica SBC) to the north — both restricted/paid. The South Caucasus has no free open-registration RTK network.
- **ArduSimple country selector**: Armenia not listed as having a national RTK network. Skylark Nx RTK (Swift Navigation) global commercial PPP coverage advertised; pricing via subscription.
- **Global commercial networks (GEODNET, ONOCOY, RTKdata)**: No Armenia coverage confirmed.
- **Volunteer**: zero AM stations on rtk2go; zero on Centipede; confirmed via `scripts/stations_by_country.py ARM` (no entries) and `scripts/stations_by_radius.py 40.18 44.51 100` (no stations within 100 km of Yerevan) on 2026-05-12.
- **Practical workaround**: Deploy a local base station for single-base RTK; or use satellite-based PPP (Trimble RTX, Fugro StarFix, Galileo HAS at ~40 cm).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope / GAGE GNSS Archive** — ARTU station (Artashat, Armenia); IGS continuous RINEX data | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); commercial fee applies |
| **ARMPOS RINEX** (Cadastre Committee) | Contact cadastre.am | Unknown — restricted distribution |

## Sources Consulted
- ARMPOS tender / technical description (Mercell): https://www.mercell.com/lt-lt/m/file/getfile.ashx?id=36925319
- e-cadastre.am / cadastre.am (Armenian Cadastre Committee)
- EuroGeographics Armenia profile: https://eurogeographics.org/member/state-committee-real-property-cadastre-government-ra/
- EuroGeographics Armenia NSDI news: https://eurogeographics.org/news/implementing-the-national-spatial-data-infrastructure-in-armenia/
- ADB project 54388-001: https://www.adb.org/projects/54388-001/main
- UNOOSA Armenia NSDI presentation: https://ggim.un.org/2unwgic/documents/Vahagn_Muradyan_Lusine_Yeghiyan.pdf
- ArduSimple country selector: https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2GO monitor (monitor.use-snip.com): no Armenia mount points visible
- NTRIP-list.com: no Armenia entries
- IGS network resources: https://igs.org/network-resources/
- GitHub mvarga1989 GNSS CORS list: https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- Local data verification (2026-05-12): `scripts/stations_by_country.py ARM` (no entries), `scripts/stations_by_radius.py 40.18 44.51 100` (no stations within 100 km of Yerevan)
- networks.md entry `armpos` (project internal, 2026-04-29)
- country-survey.md entry `AM — Armenia` (project internal, 2026-04-29)
