# Mozambique [MZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: Physical CORS exists but NO confirmed public NTRIP endpoint

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (CORS hardware exists; no public NTRIP endpoint found) |
| **host:port** | null — no NTRIP caster endpoint published publicly |
| **tariff** | null |
| **hobbyist_eligibility** | Unclear — no public registration portal or access policy found |
| **legal_residency_required** | Unclear — no access policy published |
| **last_confirmed_alive** | null — no NTRIP sourcetable confirmed reachable |

## Existing CORS Infrastructure (CENACARTA — 8 stations)

| ID | Location |
|----|----------|
| SOFL | Beira (Sofala Province) |
| MPTB | Maputo |
| CHMO | Chimoio |
| LCNG | Lichinga |
| XXAI | Xai-Xai |
| MTND | Tete |
| QLMN | Quelimane |
| NACL | Nacala |

Operated by **CENACARTA** (Centro Nacional de Cartografia e Teledetecção), Ministry of Agriculture. Appears built for post-processing/RINEX access (land administration, geodetic reference frame) — real-time NTRIP layer not publicly exposed.

## Most Recent Project Announcements

| Date | Event | URL |
|------|-------|-----|
| Dec 2018 | World Bank approves **Terra Segura** (P164551) — includes CORS densification component | https://projects.worldbank.org/en/projects-operations/project-detail/P164551 |
| ~2021 | World Bank ISR reports CORS densification "on track" | https://documents.worldbank.org/en/publication/documents-reports/documentdetail/516481620089494937 |
| ~2018 | SEGAL (Univ. Beira Interior, Portugal) collaboration with CENACARTA — SUGGEST-AFRICA geodetic infrastructure upgrade | https://segal.ubi.pt/tag/cenacarta/ |

No announcement of a live public NTRIP service or subscription portal found through 2026-05-06.

## Context Notes

- Corsmap.com (previously documented Mozambique's stations) is now offline — domain redirects to HugeDomains reseller.
- CENACARTA website (cenacarta.gov.mz) returned connection refused at research date.
- No Mozambique mountpoints on RTK2GO, BKG NTRIP, GEODNET, ONOCOY, or any global caster directory.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **CENACARTA** — 8-station CORS network built primarily for RINEX/post-processing (land administration, geodetic reference frame); direct contact required for access | cenacarta.gov.mz (offline at research date) | Unknown — contact +258 21 300 486 / +258 21 321 959 |

## Contact for Access Enquiries
CENACARTA, Av. Josina Machel 537, Maputo
Tel: +258 21 300 486 / +258 21 321 959

## Sources Consulted
- RTK2GO / SNIP monitor
- NTRIP-list.com Africa
- GIM International CORS Africa article
- Corsmap.com (offline)
- CENACARTA (UN-SPIDER, GIM International directory)
- World Bank Terra Segura P164551
- AFREF (UN-SPIDER)
- ArduSimple country selector, GitHub mvarga1989 list
- GEODNET, ONOCOY
