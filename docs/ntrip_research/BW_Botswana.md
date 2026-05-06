# Botswana [BW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: CORS network exists (DSM, ~55 stations); NTRIP endpoint NOT publicly disclosed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — physical CORS network operational; no public host:port found |
| **Network name** | Botswana National CORS Network (DSM) |
| **Operator** | Department of Surveys and Mapping (DSM), Ministry of Lands and Water Affairs (`gov.bw`), Gaborone |
| **host:port** | Not publicly published — no caster endpoint found in any directory or sourcetable |
| **tariff** | Not publicly listed; access expected through institutional channel (licensed surveyors) |
| **hobbyist_eligibility** | Unclear — network is described in cadastral surveying policy documents; no published hobbyist policy |
| **legal_residency_required** | Unclear — no published terms of service found |
| **last_confirmed_alive** | gov.bw reachable 2026-05-06; no BW mountpoint in any public NTRIP sourcetable |

## Operator

**Department of Surveys and Mapping (DSM)**
Ministry of Lands and Water Affairs
Private Bag 0037, Gaborone, Botswana
Website: https://www.gov.bw/ (DSM sub-pages under lands/surveys)

## Network Details

- **Station count:** ~55 physical CORS; project commenced 2011, approximately 10 stations added per year
- **Coverage:** ~582,000 km²; average inter-station spacing ~30–40 km
- **Geodetic framework:** Botswana National Geodetic Reference System 2002 (BNGRS02); legacy Botswana Terrestrial Reference System (BTRS) based on Cape Datum / Modified Clark 1880 ellipsoid also in use
- **Operational status (2017 snapshot):** A 2017 academic map (Hisab University / DiVA portal) showed only 28 of installed stations operating correctly; remainder malfunctioning or offline — reliability has historically been a concern
- **RTK baseline limit:** DSM technical documentation permits GNSS RTK from CORS with baselines up to 40 km for cadastral surveys
- **Caster software / host:port:** Not published; no public sourcetable or registration portal found

## Negative Findings

- RTK2GO / Centipede: Zero BW mountpoints in any public sourcetable
- NTRIP-list.com Africa: Botswana not listed
- ArduSimple country directory: Botswana not listed with any NTRIP service
- mvarga1989 GNSS CORS list (GitHub): No Botswana NTRIP endpoint
- GIM International Africa CORS map / Corsmap: Botswana described as "unmapped" (no catalogued public CORS)
- No public caster address found in any indexed source, academic paper, or news article as of 2026-05-06

## Most Recent Project Reference

**2017 academic thesis (Hisab University / DiVA portal):** Documents DSM CORS station layout with BTRS operational-status map; notes 28 of ~40 stations operating correctly at that time. No more recent public announcement of NTRIP rollout found.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **DSM Botswana** — RINEX archive availability not confirmed; contact DSM directly | https://www.gov.bw/ | Unknown |
| **IGS / EarthScope** — BOTSWANA (HRAO network) archive station; check EarthScope for any BW stations | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |

## Sources Consulted
- DiVA portal — Botswana CORS academic thesis (2017): https://www.diva-portal.org/smash/get/diva2:1137711/FULLTEXT02
- GIM International — Developing a Fully Fledged CORS Map for Africa: https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- DSM / gov.bw (lands and survey pages) — confirmed reachable 2026-05-06
- RTK2GO monitor (monitor.use-snip.com) — no BW mountpoints visible
- NTRIP-list.com/africa — Botswana not listed
- ArduSimple RTK correction services directory — Botswana not listed
