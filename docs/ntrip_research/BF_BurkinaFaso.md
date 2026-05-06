# Burkina Faso [BF] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: CORS network exists (BF-CORS / IGB); NO confirmed public NTRIP RTK caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (CORS infrastructure exists but no public NTRIP stream confirmed) |
| **host:port** | null — not publicly documented |
| **tariff** | null — no confirmed service |
| **hobbyist_eligibility** | null — no confirmed service |
| **legal_residency_required** | null — no confirmed service |
| **last_confirmed_alive** | null — NTRIP caster not confirmed; IGB website (igb.bf) reachable 2026-05-06 |

## Most Recent Project Announcement

**2011:** Réseau BF-CORS (9 stations) established with Millennium Challenge Account–Burkina Faso funding, managed by Institut Géographique du Burkina (IGB) since September 2012.
**2018:** Four additional stations added in the Ouagadougou metropolitan area with state budget financing, bringing the total to 13 stations.

- IGB GNSS-CORS page: https://www.igb.bf/?page_id=47
- IGB main site: https://www.igb.bf/

## Context Notes

- **Network stations (13 total):**
  - Original 9 (2011): Gampela, Manga, Fada, Diapaga, Dori, Ouahigouya, Dédougou, Bobo-Dioulasso, Gaoua
  - Added 4 (2018): Ouagadougou (IGB HQ), Koubri, Dapélogo, Tanguen-Dassouri
- **Purpose at launch:** Designed to support topography, cadastre, and cartography professionals in linking work to the national reference system. Post-processing (RINEX download) is the explicitly documented use case; no NTRIP real-time caster service has been publicly announced.
- **Research use:** Raw GNSS-CORS data from station BF01 (Ouagadougou) has been used in 2024 academic publications for ionospheric VTEC studies.
- **Security situation:** Since the 2022 military coup and ongoing security crisis in northern Burkina Faso, fieldwork and infrastructure maintenance are significantly constrained. Station operational continuity is uncertain.
- **IGB institutional status:** IGB remains the mapping/geodetic authority; its website is reachable but has limited recent updates.
- **Global commercial networks:** No Burkina Faso coverage confirmed for GEODNET, ONOCOY, Centipede-RTK, or PointOne.
- Practical workaround: Deploy a local base for single-base RTK; use PPP (Galileo HAS, Trimble RTX) for sub-metre positioning without a corrections service.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGB BF-CORS RINEX archive** — RINEX data available from 13 stations (contact IGB directly; no self-service portal confirmed) | https://www.igb.bf/?page_id=47 | Unknown |
| **SONEL archive** — OUAG station (Ouagadougou) for post-processing | https://www.sonel.org/spip.php?page=gps&idStation=2561 | Free |
| **IGS / EarthScope archive** — if IGB stations federate to IGS in future | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

## Sources Consulted
- IGB GNSS-CORS page (https://www.igb.bf/?page_id=47)
- IGB digital databases page (https://www.igb.bf/?page_id=85)
- IGB about page (https://www.igb.bf/?page_id=38)
- ResearchGate 2024 publication on BF01 ionospheric VTEC (https://www.researchgate.net/publication/379545036)
- SONEL GPS station OUAG (https://www.sonel.org/spip.php?page=gps&idStation=2561)
- RTK2GO monitor (monitor.use-snip.com) — no Burkina Faso mount points
- NTRIP-list.com Africa page — no Burkina Faso entries
- AFREF station map (ResearchGate)
