# Burkina Faso [BF] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: CORS network exists (BF-CORS / IGB, ~13 stations); NO confirmed public NTRIP RTK caster; security situation continues to constrain field operations

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (CORS infrastructure exists for post-processing; no public NTRIP RTK stream confirmed) |
| **host:port** | null — not publicly documented |
| **tariff** | The country-survey.md entry notes the BF-CORS service is "free with registration"; this appears to refer to post-processing RINEX access — request via IGB directly. No public RTK NTRIP tariff or endpoint published |
| **hobbyist_eligibility** | Unknown — registration is by contact with IGB, conducted in French; no public self-service portal |
| **legal_residency_required** | Not stated; in practice expect IGB to favour locally established professional users |
| **last_confirmed_alive** | 2026-05-12 — `igb.bf` reachable; IGB GNSS-CORS page (`igb.bf/?page_id=47`) still served, but content unchanged from 2024 |

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
- **Volunteer free coverage**: zero. No rtk2go BF entries; no Centipede BFA-coded nodes; no EarthScope/NOTA coverage (BF outside the Americas-region NOTA scope). Verified against `data/stations.json` 2026-05-12 — no stations within 200 km of Ouagadougou (12.36°N, −1.53°W) on any tracked free source.
- **Political/security context**: see `docs/country-survey.md` BF entry — Burkina Faso left ECOWAS January 2025, ongoing jihadist insurgency affecting ~40–60% of national territory as of April 2026, reduced bilateral technical-cooperation partnerships. Station operational continuity is uncertain.
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
