# Benin [BJ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: CORS network upgraded to RTK NTRIP mode (2022); public access and caster endpoint NOT confirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unclear — network upgraded to RTK NTRIP capability in 2022; public caster endpoint not publicly documented |
| **host:port** | Not publicly documented |
| **tariff** | Not publicly documented |
| **hobbyist_eligibility** | Unclear — upgrade purpose is land-rights / cadastral; individual hobbyist access not confirmed |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | 2026-05-12 — IGN Bénin `ign.bj/lign/` HTTP 200 (nginx); no public NTRIP caster URL surfaced via the site or via web search; no Benin entries in rtk2go monitor or NTRIP-list.com Africa |

## Most Recent Project Announcement

**2022:** The 7-station Benin CORS network (established ~2010 under MCA/IGN programme) underwent a substantial upgrade enabling RTK NTRIP mode operation, per academic analysis published in 2025 (American Journal of Science, Engineering and Technology).

- 2025 academic paper (land rights / RTK NTRIP in Benin): https://www.sciencepublishinggroup.com/article/10.11648/j.ajset.20251003.15
- RUDN University analysis of Benin permanent GNSS stations: https://journals.rudn.ru/structural-mechanics/article/view/10965
- IGN Bénin: https://ign.bj/lign/
- Benin public service GNSS file: https://service-public.bj/public/services/service/PS01085

## Context Notes

- **Network stations (7):** Cotonou, Abomey, Parakou, Natitingou, Savalou, Nikki, Kandi — covering the north-south extent of Benin.
- **Establishment:** ~2010, IGN Bénin with MCA (Millennium Challenge Account) and US expert support.
- **2022 upgrade:** Network modernised to support RTK NTRIP mode. Field surveys in the Cotonou region have used RTK NTRIP data for land-rights confirmation research (2025 paper).
- **Public access unknown:** Despite RTK NTRIP capability, no public-facing caster host/port or self-service subscription page has been found. Access may be restricted to licensed surveyors or government bodies.
- **IGN Bénin:** The national mapping authority (ign.bj) is the institutional home; no NTRIP service page is visible on the public website.
- **AFREF:** Benin CORS stations are expected to contribute to the African Geodetic Reference Frame; no confirmed real-time NTRIP AFREF stream from Benin.
- **Global commercial networks:** No Benin coverage confirmed for GEODNET, ONOCOY, Centipede-RTK, or PointOne.
- Practical workaround: Contact IGN Bénin directly for access to the RTK NTRIP service; deploy a local base for single-base RTK; use Galileo HAS / PPP.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGN Bénin GNSS archive** — RINEX from 7 CORS stations (contact IGN Bénin directly) | https://ign.bj/lign/ | Unknown |
| **IGS / EarthScope archive** — BJCO (Cotonou) IGS station | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account required) |

## Sources Consulted
- 2025 academic paper on RTK NTRIP land rights in Benin (https://www.sciencepublishinggroup.com/article/10.11648/j.ajset.20251003.15)
- RUDN University CORS Benin analysis (https://journals.rudn.ru/structural-mechanics/article/view/10965)
- IGN Bénin (https://ign.bj/lign/)
- Benin public service GNSS file (https://service-public.bj/public/services/service/PS01085)
- ArduSimple country selector — Benin not listed as having national RTK network
- RTK2GO monitor (monitor.use-snip.com) — no Benin mount points visible
- NTRIP-list.com Africa page — no Benin entries
- AFREF literature (ResearchGate)
