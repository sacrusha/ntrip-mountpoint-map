# Turkmenistan [TM] - NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: NO public NTRIP RTK caster. Government CORS infrastructure under construction via FAO-supported "Digital Land Cadastre" project (2022-2025) - 65 stations procured + 3-province pilot + finalization ceremony 2025-04-09 in Ashgabat. Public access not announced and unlikely in the near term given Turkmenistan's closed information regime. RTK2go / Centipede / EarthScope / IGS-IP / AUSCORS: zero TM stations within 500 km of Ashgabat.

## Why there is no public caster

- **Closed information regime**: Turkmenistan severely restricts internet access; external search engines cannot index domestic geodetic portals if they exist. English-language and Russian-language searches returned no NTRIP / public RTK service information 2026-05-13 / 2026-05-23. A Turkmen-language probe ("Turkmen geodezia CORS GNSS NTRIP 2025 Ashgabat") returned no follow-up announcement to the 2025-04-09 FAO finalization.
- **FAO Digital Land Cadastre CORS project (2022-2025)** supported Turkmengeodezija (the state geodesy service under the Ministry of Agriculture's Land Resources Service) in building a national CORS network for cadastre modernization. The government procured 65 reference stations and 97 GNSS receivers; FAO contributed 3 pilot stations + 4 receivers + control software installed in 3 provinces as a model (specific provinces not named in the FAO / newscentralasia.net coverage). Finalization ceremony 2025-04-09 in Ashgabat per newscentralasia.net (2025-04-17). The horizon for public access is governed by the "Concept for the Development of Digital State Land Cadastre 2025-2030" (FAO source); public NTRIP availability is not announced and unlikely under the closed-information regime even within that horizon.
- **No IGS / EUREF / AFREF membership** for any TM station; no IGS permanent station on Turkmenistan territory confirmed as of 2026.
- **No commercial coverage**: GEODNET, PointOne Polaris, Swift Skylark, Trimble VRS Now, Hexagon HxGN SmartNet publish no Turkmenistan PoPs.
- **No volunteer coverage**: Local 2026-05-23 - `scripts/stations_by_country.py TKM` returns no entries; `scripts/stations_by_radius.py 37.95 58.38 500` (Ashgabat, 500 km) returns no stations on any ingested source (rtk2go, Centipede, EarthScope, IGS-IP, AUSCORS).
- **Iran SHAMIM cross-border**: NCC SHAMIM (Iranian national CORS) has stations within ~30 km of the Turkmen border in NE Iran (Khorasan-e Razavi). Not publicly accessible to non-Iranian users; National Cartographic Center distributes corrections via internal subscription only. Functionally unreachable for foreign hobbyists.

## Most recent project / announcement

**FAO Digital Land Cadastre CORS Project - finalization 2025-04-09, Ashgabat.** 65 CORS + 97 receivers procured by Government of Turkmenistan; FAO 3-province pilot. No public NTRIP access announced. No follow-up announcement located via Turkmen-language search 2026-05-23.

Source: https://www.newscentralasia.net/2025/04/17/from-farmers-to-government-officials-everyone-benefits-from-a-digital-land-cadastre/

## Hobbyist path

1. **Cm-class** - none. Deploy a local base for single-baseline RTK.
2. **Sub-decimetre** - Galileo HAS (~20-40 cm horizontal, satellite-delivered, free) - the only practical option for non-resident hobbyists.
3. **Post-processing only** - nearest IGS/EPN stations in Kazakhstan, Iran (KIT3, TEHN, ARTU) - 500-1,500 km baselines, usable for PPP only.

## Post-processing (RINEX) fallback

None confirmed inside Turkmenistan. Nearest options 500+ km away.

## Sources

- FAO Turkmenistan CORS project (newscentralasia.net 2025-04-17, finalization 2025-04-09 Ashgabat, 65 stations + 97 receivers): https://www.newscentralasia.net/2025/04/17/from-farmers-to-government-officials-everyone-benefits-from-a-digital-land-cadastre/
- WebSearch "Turkmenistan GNSS geodesy survey authority CORS reference station 2024" (2026-05-06) - no public service found
- WebSearch "Turkmenistan CORS GNSS NTRIP RTK network Ashgabat 2024" (2026-05-06) - no public service found
- WebSearch "Turkmen geodezia CORS GNSS NTRIP 2025 Ashgabat" 2026-05-13 - no follow-up to 2025-04-09 finalization
- WebSearch "Turkmenistan FAO CORS GNSS NTRIP RTK public access 2026" 2026-05-13 + "Turkmenistan FAO CORS GNSS 2025 RTK NTRIP public" 2026-05-23 - no public access announced
- ArduSimple Turkmenistan: HTTP 404 (no country page exists)
- Local 2026-05-23: `scripts/stations_by_country.py TKM` -> no stations; `scripts/stations_by_radius.py 37.95 58.38 500` -> no stations within 500 km of Ashgabat
