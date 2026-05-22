# Gabon [GA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (re-verified — no operational change). NKLG IGS station (Libreville, 0.35/9.67) is on AUSCORS+IGS-IP+MIRAI rebroadcast per local stations.json — IGS post-processing site, not a Gabonese caster.

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (no Gabonese caster); NKLG (IGS) is rebroadcast — see below |
| **landing_url** | null — no Gabonese operator portal exposes a caster (anuttc.ga, incgabon.ga both describe non-streaming services) |
| **access_url** | null — no service exists |
| **host:port** | null (no Gabonese caster). NKLG (IGS, Libreville) is rebroadcast on AUSCORS, IGS-IP and MIRAI casters — see Cross-Border Alternative below for endpoints. |
| **tariff** | null |
| **num_stations** | 0 (national); 1 IGS station (NKLG) is hosted on Gabonese territory but is operated and streamed by IGS / BKG / partners, not a Gabonese caster |
| **vrs** | N/A |
| **hobbyist_eligibility** | N/A for any Gabonese service; NKLG is accessible to any rover able to register with the operating IGS rebroadcaster (AUSCORS / IGS-IP / MIRAI) |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no Gabonese caster has ever been confirmed alive |

## Most Recent Project Announcement

**IGN FI / ANINF — National Geomatic Plan, 2013–ongoing**: In 2011, IGN FI was selected by the Gabonese General Directorate for Budget to conduct the preliminary study for a National Geomatic Plan. Four pilot projects were completed. In 2013, ANINF (Agence Nationale des Infrastructures Numériques et des Fréquences) and IGN FI signed an assistance agreement to implement the plan on a national scale. The plan's scope includes geographic reference frameworks, cadastre, and "cartographic tools and satellite location systems." No CORS caster or NTRIP endpoint has been identified as a delivered output.

Source: https://www.ignfi.fr/en/portfolio-item/plan-national-geomatique-gabon/

**ANUTTC 2025 parcel delivery programme**: ANUTTC is delivering ~2,000 surveyed land parcels across Greater Libreville by end of 2025. This is a cadastral land-demarcation programme using survey-grade GNSS equipment, but operates with conventional base-rover or post-processed methods — no NTRIP caster endpoint has been announced.

Source: https://union.sonapresse.com/fr/anuttc-environ-2-000-parcelles-viabilisees-livrees-dici-fin-2025

**AFREF Workshop 2024** (RCMRD, Nairobi, August 2024): Gabon not listed among the African countries confirmed to have at least one operational CORS installation. GIM International "Fully-Fledged CORS Map for Africa" (re-checked 2026-05-22) likewise does not include Gabon in the 25 mapped-CORS countries.
URLs: https://ric2024.rcmrd.org/afref · https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa

## Context Notes

- **ANUTTC** (Agence Nationale de l'Urbanisme, des Travaux Topographiques et du Cadastre), created by decree 1500/PR/MHUEDD in 2011, is the principal geodetic and cadastral authority. Re-checked 2026-05-22: `anuttc.ga` homepage reachable; pages describe land regularisation, topography, and cadastre services. No mention of NTRIP, RTK, CORS, or real-time GNSS service.
- **INC (Institut National de Cartographie, Gabon)** at `incgabon.ga` (re-checked 2026-05-22) maintains a "Réseau des Points Géodésiques du Gabon" — described as a 1st/2nd-order point network observed with GNSS equipment. This is a **static passive geodetic network**, not a real-time service. No NTRIP/CORS reference.
- **AGEOS** (Agence Gabonaise d'Études et d'Observations Spatiales, ground station at Nkok ~17 mi east of Libreville) operates an X-band satellite Earth-observation reception facility (2800 km coverage radius). AGEOS is **Earth-observation only**, no GNSS CORS or NTRIP product is published.
- **IGN FI involvement**: Two documented projects — (1) the National Geomatic Plan (2011–2013 initial phases); (2) an information system for forest spatial planning. Neither confirms a CORS deployment or NTRIP service.
- **ANINF**: The national digital infrastructure agency co-signed the geomatic plan with IGN FI; no station or caster has materialised in public sources.
- **No CORS confirmed**: Gabon does not appear in the IGS network, ITRF2020, SONEL, AFREF confirmed-CORS country list, or the GIM International Africa CORS map as of 2026-05-22.
- **RTK2go / Centipede / EarthScope**: Zero GA/GAB stations in any volunteer sourcetable (verified 2026-05-22 via live probes and local `data/stations.json`).
- **IGS rebroadcast (significant for Libreville-area hobbyists)**: NKLG (Libreville, 0.354/9.672) appears on AUSCORS, IGS-IP, and MIRAI rebroadcasts of select IGS stations (local `data/stations.json`, verified 2026-05-22 via `stations_by_country.py GAB` returning 1 entry from each of the three rebroadcasters). Not a Gabonese caster; raw 1 Hz single-base IGS site streamed by BKG/GA/JAXA infrastructure. **NKLG is ~25 km from central Libreville (0.39, 9.45)** — that distance is well inside single-base RTK working range (typical hobbyist hardware: 7 mm + 1 ppm → ~32 mm expected accuracy at 25 km). A hobbyist in or near Libreville with a ZED-F9P / Mosaic-X5 / Emlid rover able to register with any of the three IGS rebroadcasters can operate single-base RTK against NKLG today; this is the de facto only free RTK option on Gabonese soil. It does not constitute a national NTRIP service (no operator-published Gabonese host:port, no operator support, no SLA), and degrades fast outside Libreville: at >100 km from NKLG single-base RTK becomes marginal, and most of southern, central, and eastern Gabon is outside that range.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede, RTKdata): No GA coverage identified.
- **Infrastructure context**: Gabon has relatively high GDP per capita for the region and concentrated urban population in Libreville — better enabling conditions than many sub-Saharan peers, but no public CORS has been announced or confirmed as of the research date.

## Cross-Border / On-Soil IGS Alternative — NKLG via IGS Rebroadcast

NKLG is the only real-time RTK-capable GNSS stream on Gabonese soil. It is not a Gabonese caster but is rebroadcast on three independent international casters per local `data/stations.json` (verified 2026-05-22):

| Rebroadcaster | host:port | Notes |
|---|---|---|
| AUSCORS (Geoscience Australia) | `ntrip.data.gnss.ga.gov.au:2101` | Free with registration; international rebroadcast list |
| IGS-IP (BKG, on behalf of IGS) | `www.igs-ip.net:2101` | Free with registration via BKG NTRIP user portal |
| MIRAI (JAXA) | `ntrip.go.gnss.go.jp:2101` | Free with registration |

NKLG appears with a Gabon (GAB) country tag in each rebroadcaster's sourcetable. Exact mountpoint name varies per rebroadcaster (typically `NKLG` or `NKLG0` variant); confirm via live sourcetable fetch before configuring rover.

Effective for Libreville-region hobbyists; degrades to single-base ppm error past ~30 km from NKLG.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS NKLG RINEX (CDDIS / IGN data centres)** | https://cddis.nasa.gov/ | Free; long-baseline anchor for any Gabonese static occupation |
| **EarthScope GNSS Data Archive** — no confirmed continuously-operated GA-additional station in current archive | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) — GA data availability unconfirmed |

## Sources Consulted (2026-05-22)
- ANUTTC official site: http://anuttc.ga/ (live, no NTRIP reference)
- INC Gabon: https://www.incgabon.ga/ (re-checked 2026-05-22: static geodetic point network only)
- AGEOS: https://www.economie-numerique.gouv.ga/2-ministere/2078-secretariat-general/2084-entites-sous-tutelles/2103-agence-gabonaise-d-etudes-et-d-observations-spatiales-ageos-/
- ANUTTC 2025 parcel programme: https://union.sonapresse.com/fr/anuttc-environ-2-000-parcelles-viabilisees-livrees-dici-fin-2025
- Ministry of Public Works — ANUTTC presentation: https://www.infrastructures.gouv.ga/303-habitat/305-organismes-sous-tutelles/306-agence-nationale-de-l-urbanisme-des-travaux-topographiques-et-du-cadastre/
- IGN FI portfolio — National Geomatic Plan Gabon: https://www.ignfi.fr/en/portfolio-item/plan-national-geomatique-gabon/
- IGN FI portfolio — Forest spatial planning Gabon: https://www.ignfi.fr/en/portfolio-item/systeme-dinformation-pour-lamenagement-forestier-gabon/
- AFREF 2024 Workshop / RCMRD: https://ric2024.rcmrd.org/afref
- GIM International — Africa CORS map: https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa (Gabon absent)
- IGS network (network.igs.org) — only NKLG (IGS reference, not a Gabonese caster)
- SONEL GNSS database — 0 GA results confirmed-continuous
- RTK2go live sourcetable probe (2026-05-22) — 0 GA mountpoints
- Centipede-RTK live sourcetable probe (2026-05-22) — 0 GA mountpoints
- GitHub mvarga1989 CORS list — no GA entry
- ntrip-list.com/africa/ — no GA entry
- WebSearch 2026-05-22 ("Gabon ANUTTC CORS NTRIP RTK 2026", "Gabon AGEOS GNSS station permanente") — no operational caster or deployment announcement surfaced
