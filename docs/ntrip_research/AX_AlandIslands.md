# Åland Islands [AX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES (limited) — 2 Centipede volunteer nodes; FINPOS (Finland NLS) covers Åland territory but RTK access is restricted to research/test only; no dedicated Åland CORS

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Partial — Centipede volunteer nodes only for hobbyist use |
| **Volunteer (Centipede)** | ~2 nodes in Åland archipelago (country code `ALA`) — `caster.centipede.fr:2101` |
| **Volunteer (rtk2go)** | 0 AX bases confirmed |
| **FINPOS (Finland NLS)** | host: `gnss-finland.nls.fi` / `finpos.nls.fi`; RTK service restricted to research/test use; DGNSS and RINEX services open; see notes |
| **SWEPOS (Sweden, Lantmäteriet)** | Separate subscription; mainland Swedish coverage; Åland proximity varies — not confirmed to cover AX territory |
| **hobbyist_eligibility** | Centipede: yes — free, open; FINPOS RTK: no (research/test only, 3-month term, requires justification) |
| **legal_residency_required** | Centipede: no; FINPOS: no residency requirement stated, but registration on maanmittauslaitos.fi required |
| **last_confirmed_alive** | Centipede caster `caster.centipede.fr:2101` is continuously operated; ALA node status confirmed present in Centipede sourcetable at time of research |
| **tariff** | Centipede: free; FINPOS: free of charge (if granted) |

## FINPOS Coverage and Access

The FINPOS positioning service of the National Land Survey of Finland (Maanmittauslaitos / NLS) uses ~90 FinnRef and FINPOS reference stations across Finland and neighbouring countries. Åland Islands is an autonomous territory of Finland geographically located between Finland and Sweden; FINPOS service coverage nominally extends to Åland.

**Key access restriction**: The RTK service (real-time, centimetre-level) is granted only for research, testing and development — not for production or routine operational use. Applications must be justified; access granted for 3-month periods. This effectively makes FINPOS RTK unsuitable for hobbyist or routine drone/survey work.

**FINPOS services open to all registered users (free)**:
- DGNSS (sub-metre, RTCM 2.3) — no justification required
- RINEX raw data download (E2-service)
- Real-time raw observation streams (Raw data service)

Registration at https://finpos.nls.fi/ or https://maanmittauslaitos.fi/en/finpos/register.

## Centipede Volunteer Nodes

Centipede-RTK is the practical free RTK option for Åland. Two nodes with country code `ALA` in the Centipede sourcetable cover portions of the archipelago. Coverage depends on node locations within the 6,500-island archipelago (~1,528 km²); the practical RTK radius per node is ~20–40 km. The main island (Fasta Åland) is ~70 km long; two nodes may leave gaps in the outer archipelago.

## No Dedicated Åland CORS

No Åland-specific government CORS or NTRIP programme has been identified. The autonomous government of Åland (Ålands landskapsregering) has not announced any geodetic correction service. Finland's Lantmäteriet-equivalent (Maanmittauslaitos) administers FINPOS for all Finnish territory including Åland.

## SWEPOS (Sweden) Proximity

Lantmäteriet's SWEPOS network covers Sweden. The nearest SWEPOS stations to Åland are on the Swedish east coast (Stockholm archipelago, ~200 km). SWEPOS VRS corrections via `swepos.lantmateriet.se:2101` require a paid subscription (Swedish Lantmäteriet pricing); coverage geometry for Åland is marginal at that distance.

## Most Recent Project Announcement

No Åland-specific RTK project found. Finland NLS published a 30-year FinnRef anniversary article (2024) noting plans to continue expanding FINPOS capabilities including PPP-RTK (SSR) — relevant to Åland coverage quality but no operational change announced.

## Context Notes

- **Åland autonomous status**: Åland has its own parliament and administration but is part of Finland for geodetic infrastructure purposes.
- **EUREF station**: EPN station `MARI` (Mariehamn, Åland) is a EUREF Permanent Network station; RINEX data available via EPN; may stream real-time RTCM via euref-ip.net — usable as a single-base stream for RTK.
- **GEODNET**: No confirmed GEODNET node in Åland; not ruled out (would require checking rtk.geodnet.com coverage map directly).
- **Hobbyist RTK summary**: The two Centipede nodes are the only no-restriction real-time RTK option in Åland today. FINPOS DGNSS (free, open) provides sub-metre corrections. A hobbyist needing cm-level accuracy should use Centipede, or contact NLS to determine whether their use case qualifies as "testing" for FINPOS RTK.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **FINPOS / FinnRef RINEX** (E2-service, ~90 stations including Åland-area stations) | https://finpos.nls.fi/ | Free (account required) |
| **EPN MARI station** (Mariehamn) | https://epncb.oma.be/ | Free with EPN registration |

## Sources Consulted
- FINPOS service overview: https://www.maanmittauslaitos.fi/en/finpos
- FINPOS RTK service page: https://www.maanmittauslaitos.fi/en/finpos/rtk
- FINPOS registration: https://www.maanmittauslaitos.fi/en/finpos/register
- FINPOS Terms of Use: https://www.maanmittauslaitos.fi/en/finpos/kayttoehdot
- FinnRef 30-year article: https://www.maanmittauslaitos.fi/en/topical_issues/30-year-old-network-finnref-stations-forms-basis-finlands-geospatial-data
- FINPOS portal: https://finpos.nls.fi/
- Centipede-RTK network: https://www.centipede-rtk.org/ · https://map.centipede-rtk.org/
- EUREF Permanent GNSS Network: https://epncb.oma.be/
- ArduSimple Finland RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-finland/
