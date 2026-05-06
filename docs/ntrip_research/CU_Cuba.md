# Cuba [CU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no public NTRIP caster; GEOCUBA operates a GNSS network but no hobbyist-accessible endpoint found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Operator** | GEOCUBA (Grupo Empresarial GEOCUBA — Empresa de Geoinformática y Cartografía) |
| **host:port** | Not published — no public endpoint found |
| **VRS** | Unknown |
| **tariff** | Institutional/governmental access only; no public pricing |
| **hobbyist_eligibility** | No — self-service registration not available |
| **legal_residency_required** | Yes (implied — institutional accounts only) |
| **last_confirmed_alive** | GEOCUBA corporate site (geocuba.cu) HTTP 200 confirmed 2026-05-06; no NTRIP endpoint reachable |
| **Most recent project announcement** | None found specific to a public NTRIP launch as of 2026-05-06 |

## Context Notes

- **GEOCUBA** was established on May 1, 1995, merging the former Instituto Cubano de Hidrografía and the Instituto Cubano de Geodesia y Cartografía. It operates under the Ministerio de las Fuerzas Armadas Revolucionarias (MINFAR).
- Academic literature (Revista Cubana de Geomática, 2025 Vol. 7 No. 1 — 30th anniversary issue) confirms GEOCUBA has a GNSS network and conducts RTK research, but no public endpoint is referenced.
- Prior research referenced ~13 GNSS reference stations; specific details (station names, exact locations) are not published on any accessible portal.
- **US trade embargo** (OFAC regulations) restricts import of most GNSS survey equipment and software to Cuba, compounding the barrier to RTK adoption by hobbyists.
- Cuba participates in **SIRGAS** (Sistema de Referencia Geocéntrico para las Américas) — a few Cuban stations appear in the SIRGAS CORS list for academic/geodetic use, but these are not accessible as public NTRIP streams.
- No rtk2go or Centipede volunteer bases identified for Cuba.
- No project announcement for a future public RTK service found as of 2026-05-06.

## Post-Processing (RINEX) Fallback

No publicly accessible RINEX download service identified for Cuba. SIRGAS provides access to data from the limited SIRGAS-Cuba stations for academic users.

| Service | URL | Cost |
|---|---|---|
| **SIRGAS station archive** — limited Cuban CORS data | https://sirgas.ipgh.org/ | Free (research/academic) |

## Sources Consulted
- GEOCUBA corporate site: http://www.geocuba.cu/
- MINFAR / GEOCUBA: https://www.minfar.gob.cu/sistema-empresarial/grupo-empresarial-geocuba
- Revista Cubana de Geomática 2025: https://geomatica.geocuba.cu/rcg
- SIRGAS station list (Cuba): https://sirgas.ipgh.org/en/gnss-network/stations/station-list/
- WebSearch: "Cuba GNSS CORS NTRIP RTK geodesia 2024 2025" — no public endpoint found
- WebSearch: "Cuba Instituto Geodesia IGT tiempo real RTK 2024 2025" — no public endpoint found
