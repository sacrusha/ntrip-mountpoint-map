# Republic of the Congo [CG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revising 2026-05-06 entry — no material changes; volunteer counts re-verified)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Most Recent Project Announcement

**IGN FI / CERGEC geomatics cooperation, June 2024**: The regional director of IGN FI (Institut Géographique National, France International), Aude Areste, announced in Brazzaville on 26 June 2024 that IGN FI would accompany CERGEC in implementing geomatics projects. The cooperation scope covers cartographic document digitisation, remote sensing, GIS training, and "other applications involving cartographic tools and satellite location systems" — but no specific CORS network or NTRIP caster is named or timed.

Sources:
- https://www.faapa.info/blog/congo-linstitut-geographique-francais-entend-accompagner-le-cergec-pour-des-projets-geomatiques/
- https://www.recherchescientifique.gouv.cg/ign-fi-pour-un-accompagnement-du-cergec-dans-la-mise-en-place-des-projets-geomatiques/

**Earlier cooperation**: A protocol was signed between the Congolese Ministry of Scientific Research and IGN / IGN FI to transform CERGEC into a modern National Geographic Institute. This earlier framework (c. 2019) also included geodetic infrastructure support and satellite location, but no CORS deployment was confirmed.

Source: https://www.recherchescientifique.gouv.cg/le-ministere-et-lign-renforcent-la-cooperation-dans-la-production-de-linformation-geographique/

**AFREF Workshop 2024** (RCMRD, Nairobi, August 2024): Republic of the Congo not listed among the ~22 African countries confirmed as having at least one CORS installation.
URL: https://ric2024.rcmrd.org/afref

## Context Notes

- **CERGEC** (Centre de Recherche Géographique et de Production Cartographique) is the official national mapping and geodetic authority, operating under the Ministry of Scientific Research and Innovation. It is responsible for cartographic reference data and geodesy for the country.
- **No CORS, no NTRIP**: No CORS installation, IGS-affiliated permanent station, or NTRIP caster has been identified for CG. CG does not appear in the IGS network, ITRF2020, SONEL, or the AFREF confirmed-CORS country list.
- **IGN FI partnership scope** as of 2024: The announced cooperation covers GIS, digitisation, and "satellite location systems" broadly — not a committed CORS deployment schedule. No host:port or caster endpoint has been published.
- **RTK2go / Centipede**: Zero CG/COG stations in either sourcetable (re-verified 2026-05-12 against `data/stations.json` fetched 2026-05-12T18:17Z).
- **Global commercial networks** (GEODNET, ONOCOY, Centipede, RTKdata): No coverage of the Republic of the Congo.
- **Infrastructure constraints**: Electricity access is limited outside Brazzaville and Pointe-Noire; internet penetration is low in rural areas — both constrain continuous CORS operation outside urban centres.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — no confirmed CG monument in current archive | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) — CG data availability unconfirmed |

## Sources Consulted
- FAAPA / Recherchescientifique.gouv.cg — IGN FI / CERGEC 2024 announcement
- Ministère de la Recherche Scientifique et de l'Innovation Technologique (CG) — IGN FI cooperation protocol page
- IGN FI border-delimitation portfolio (Congo): https://www.ignfi.fr/en/portfolio-item/aide-delimitation-frontiere-congo/
- AFREF 2024 Workshop / RCMRD confirmed-CORS country list: https://ric2024.rcmrd.org/afref
- IGS network (network.igs.org) — 0 CG results
- SONEL GNSS database — 0 CG results
- RTK2go sourcetable — 0 CG mountpoints
- Centipede-RTK sourcetable — 0 CG mountpoints
- GitHub mvarga1989 CORS list — no CG entry
- ntrip-list.com/africa/ — no CG entry
