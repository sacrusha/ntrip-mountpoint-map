# Mozambique [MZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-14 (re-verified; status unchanged from 2026-05-06)

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
- **CENACARTA web presence is currently broken** (re-verified 2026-05-14):
  - `cenacarta.gov.mz` — ECONNREFUSED on HTTPS; remains unreachable since at least 2026-05-06.
  - `www.cenacarta.com` — the domain still resolves but the content is now an unrelated Thai/English content-farm blog (articles about plumbing, SEO, ERP software etc.); the `/pmapper/` path returns HTTP 404. The domain appears to have been sold or hijacked since the 2018 datahub.io snapshot that listed it as the Mozambique WebMapper. UN-SPIDER still describes CENACARTA but no longer publishes a working URL.
  - Net effect: there is no currently-reachable CENACARTA web property (no portal, no WebMapper, no contact form). Direct phone/email contact (numbers below) is the only remaining channel.
- A separate national SDI portal `www.mozgis.gov.mz` exists (Rede Nacional SIG / ArcGIS-based) — geospatial layers only, no NTRIP product.
- **MIRASpaco connection**: The Nigerian operator MIRASpaco lists Mozambique as one of three countries where it installs/rehabilitates GNSS CORS networks (alongside Nigeria and Angola). This suggests the CENACARTA stations are MIRASpaco-installed; whether MIRASpaco hosts a corresponding MZ NTRIP caster has not been confirmed publicly.
- No Mozambique mountpoints on RTK2GO, BKG NTRIP, GEODNET, ONOCOY, or any global caster directory. Nearest rtk2go bases: mabuda_farm (Eswatini, 85 km from Maputo) and LouwNPP (north-east ZAF, 226 km) — practical for southern Maputo Province only.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **CENACARTA** — 8-station CORS network built primarily for RINEX/post-processing (land administration, geodetic reference frame); direct contact required for access | cenacarta.gov.mz (offline 2026-05-06 → 2026-05-14); cenacarta.com (domain no longer hosts CENACARTA content as of 2026-05-14) | Unknown — contact +258 21 300 486 / +258 21 321 959 |

## Contact for Access Enquiries
CENACARTA, Av. Josina Machel 537, Maputo
Tel: +258 21 300 486 / +258 21 321 959

## Sources Consulted
- RTK2GO / SNIP monitor
- NTRIP-list.com Africa
- GIM International CORS Africa article
- Corsmap.com (offline — domain parked)
- CENACARTA WebMapper: https://www.cenacarta.com/pmapper/ (was the active operator URL per 2018 datahub.io; HTTP 404 / domain repurposed to content-farm content by 2026-05-14)
- UN-SPIDER CENACARTA: https://www.un-spider.org/mozambique-national-cartography-and-remote-sensing-centre-cenacarta
- Mozambique national SDI: https://www.mozgis.gov.mz/
- MIRASpaco GNSS service portfolio (lists Mozambique as deployment country): https://miraspaco.com/gnss/
- World Bank Terra Segura P164551
- AFREF (UN-SPIDER)
- ArduSimple country selector, GitHub mvarga1989 list
- GEODNET, ONOCOY
- Local data: `py scripts/stations_by_radius.py -25.97 32.58 800` — 0 MOZ stations, 2 nearby (SWZ, ZAF), all 2026-05-12
