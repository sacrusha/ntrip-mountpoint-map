# Gabon [GA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-06 entry; no new CORS/NTRIP activity surfaced)

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

**IGN FI / ANINF — National Geomatic Plan, 2013–ongoing**: In 2011, IGN FI was selected by the Gabonese General Directorate for Budget to conduct the preliminary study for a National Geomatic Plan. Four pilot projects were completed. In 2013, ANINF (Agence Nationale des Infrastructures Numériques et des Fréquences) and IGN FI signed an assistance agreement to implement the plan on a national scale. The plan's scope includes geographic reference frameworks, cadastre, and "cartographic tools and satellite location systems." No CORS caster or NTRIP endpoint has been identified as a delivered output.

Source: https://www.ignfi.fr/en/portfolio-item/plan-national-geomatique-gabon/

**ANUTTC 2025 parcel delivery programme**: ANUTTC is delivering ~2,000 surveyed land parcels across Greater Libreville by end of 2025. This is a cadastral land-demarcation programme using survey-grade GNSS equipment, but operates with conventional base-rover or post-processed methods — no NTRIP caster endpoint has been announced.

Source: https://union.sonapresse.com/fr/anuttc-environ-2-000-parcelles-viabilisees-livrees-dici-fin-2025

**AFREF Workshop 2024** (RCMRD, Nairobi, August 2024): Gabon not listed among the ~22 African countries confirmed to have at least one operational CORS installation.
URL: https://ric2024.rcmrd.org/afref

## Context Notes

- **ANUTTC** (Agence Nationale de l'Urbanisme, des Travaux Topographiques et du Cadastre), created by decree 1500/PR/MHUEDD in 2011, is the principal geodetic and cadastral authority under the Ministry of Public Works and Construction. It manages land regularisation and topographic survey work for Gabon. Website: http://anuttc.ga/ (availability intermittent).
- **Direction Générale des Travaux Topographiques et du Cadastre** (DGTC) is the complementary directorate within the Ministry managing cadastral records.
- **IGN FI involvement**: Two documented projects — (1) the National Geomatic Plan (2011–2013 initial phases); (2) an information system for forest spatial planning. Neither confirms a CORS deployment or NTRIP service.
- **ANINF**: The national digital infrastructure agency co-signed the geomatic plan with IGN FI, suggesting future connectivity infrastructure could support CORS hosting — but no station or caster has materialised in public sources.
- **No CORS confirmed**: Gabon does not appear in the IGS network, ITRF2020, SONEL, AFREF confirmed-CORS country list, or any NTRIP listing as of 2026-05-12.
- **RTK2go / Centipede / EarthScope**: Zero GA / GAB stations in any sourcetable as of 2026-05-12 (verified via local `data/stations.json`).
- **Global commercial networks** (GEODNET, ONOCOY, Centipede, RTKdata): No GA coverage identified.
- **Infrastructure context**: Gabon has relatively high GDP per capita for the region and concentrated urban population in Libreville — better enabling conditions than many sub-Saharan peers, but no CORS has been publicly announced or confirmed as of the research date.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — no confirmed continuously-operated GA station in current archive | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) — GA data availability unconfirmed |

## Sources Consulted
- ANUTTC official site (Gabon): http://anuttc.ga/
- ANUTTC 2025 parcel programme: https://union.sonapresse.com/fr/anuttc-environ-2-000-parcelles-viabilisees-livrees-dici-fin-2025
- Ministry of Public Works — ANUTTC presentation: https://www.infrastructures.gouv.ga/303-habitat/305-organismes-sous-tutelles/306-agence-nationale-de-l-urbanisme-des-travaux-topographiques-et-du-cadastre/
- IGN FI portfolio — National Geomatic Plan Gabon: https://www.ignfi.fr/en/portfolio-item/plan-national-geomatique-gabon/
- IGN FI portfolio — Forest spatial planning Gabon: https://www.ignfi.fr/en/portfolio-item/systeme-dinformation-pour-lamenagement-forestier-gabon/
- AFREF 2024 Workshop / RCMRD: https://ric2024.rcmrd.org/afref
- IGS network (network.igs.org) — 0 GA results
- SONEL GNSS database — 0 GA results confirmed-continuous
- RTK2go sourcetable — 0 GA mountpoints
- Centipede-RTK sourcetable — 0 GA mountpoints
- GitHub mvarga1989 CORS list — no GA entry
- ntrip-list.com/africa/ — no GA entry
- WebSearch 2026-05-12 ("Gabon ANUTTC CORS GNSS NTRIP reference station 2025 2026") — no operational caster or 2025/2026 deployment announcement surfaced
