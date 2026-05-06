# Bolivia [BO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — multiple paid, subscription-gated NTRIP RTK casters operating; no free public caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private commercial + government, all paid/gated) |
| **host:port — RED-GEO** | hostname not publicly documented; port **6060**; credentials provided post-subscription |
| **host:port — IGM MARGEN-ROC** | not public; access via formal request to IGM Bolivia |
| **host:port — GEOEQUIPOS** | not public |
| **tariff** | All three networks: pricing not published — direct-contact only. GEOEQUIPOS uses QR-code mobile payments in Bolivianos (≤500 Bs per transaction). |
| **hobbyist_eligibility** | RED-GEO: unclear (COTOBOL professional-surveyor mandate, Ley 2997 del Topógrafo); GEOEQUIPOS: appears more open; IGM: institutional |
| **legal_residency_required** | unclear for all three networks |
| **last_confirmed_alive** | `geoboliviasrl.info/redgeo` returned HTTP 301 on 2026-05-06; `geoequipossrl.com/red-cors/` active per search results 2026-05-06 |

## Most Recent Project Announcement

No new public-facing project announcement identified. Active networks have been operating; IGM MARGEN-ROC access procedure is documented in a YouTube walkthrough at https://www.youtube.com/watch?v=4yuH1W05eII.

## Context Notes

- **RED-GEO CORS NTRIP** (operated by GeoBolivia SRL, governed by COTOBOL — Colegio de Topógrafos de Bolivia): ~7 stations across La Paz, Cochabamba, Oruro, Sacaba, Tarija, Santa Cruz. Multi-constellation (GPS + GLONASS + Galileo + BeiDou). Port 6060. Operates under Ley 2997 del Topógrafo, which establishes professional-surveyor governance — practical implication is that hobbyist sign-up may be restricted in practice. Hostname not surfaced publicly; provided after subscription.
- **IGM MARGEN-ROC NTRIP**: Operated by the Instituto Geográfico Militar de Bolivia (national geodetic authority). 42 continuous reference stations. Annual fee + formal written request required for access. No public host:port; the access procedure is documented on YouTube (`youtube.com/watch?v=4yuH1W05eII`).
- **GEOEQUIPOS SRL Red CORS**: Second private commercial network. Mobile-payment friendly via QR codes in local currency (Bolivianos), capped at 500 Bs per transaction. Host, port, and pricing not publicly documented; `geoequipossrl.com/red-cors/` is active per search index but specifics behind contact gate.
- **No free public national caster** is confirmed for Bolivia.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede-RTK, PointOne, RTK2go): no Bolivia coverage confirmed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive / SIRGAS-CON** — Bolivia CORS in the SIRGAS-CON tier | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); USD 1,000/seat/yr commercial |
| **IGM Bolivia (MARGEN-ROC)** — RINEX retrievable per institutional procedure | direct contact via IGM | Fee/request-based |

## Sources Consulted
- GeoBolivia SRL / RED-GEO landing (geoboliviasrl.info/redgeo)
- COTOBOL (Colegio de Topógrafos de Bolivia) communications referencing Ley 2997
- IGM Bolivia (igmbolivia.gob.bo) — URL drift observed
- YouTube walkthrough — IGM MARGEN-ROC access procedure (`youtube.com/watch?v=4yuH1W05eII`)
- GEOEQUIPOS SRL (`geoequipossrl.com/red-cors/`)
- NTRIP-list.com South America
- GEODNET, ONOCOY coverage maps
- ArduSimple Bolivia page
