# Sint Maarten [SX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no territory-operated NTRIP; nearest free option is EarthScope CN59 on Anguilla (~20 km); Kadaster NL AGRS does NOT cover SX

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Operator** | — |
| **Nearest free option** | EarthScope NOTA station CN59 on Anguilla (~20 km) via `ntrip.earthscope.org:2101`; free noncommercial (account + NULA required) |
| **VRS** | No — single-base stream only |
| **tariff — EarthScope noncommercial** | Free |
| **tariff — EarthScope commercial** | USD $1,000/seat/year |
| **hobbyist_eligibility** | Yes (EarthScope noncommercial account) |
| **legal_residency_required** | No |
| **last_confirmed_alive** | EarthScope portal alive 2026-05-06 |

## Kadaster NL AGRS — Does NOT Cover SX

The Dutch Caribbean AGRS (Actief GNSS Referentiesysteem) caster (`ntrip.kadaster.nl:2101`) covers the BES islands — Bonaire (BQ), Sint Eustatius (SE), and Saba (SA) — but **not** Sint Maarten (SX). Sint Maarten is a separate constituent country of the Kingdom of the Netherlands, not a special municipality like the BES islands. Confirmed: no SX endpoint found on ntrip.kadaster.nl. See `CW_Dutch_Caribbean.md` for BES details.

As of February 2026, Kadaster St. Maarten and Kadaster Netherlands signed a Letter of Intent toward a Caribbean Cadaster Association (CCA), but this is focused on cadastral cooperation — no GNSS NTRIP infrastructure announced.

## Context Notes

- Sint Maarten is a constituent country of the Kingdom of the Netherlands occupying the southern ~40% of the island of Saint Martin. Total land area ~34 km².
- Kadaster St. Maarten became GIS-ready in 2025 (deployed in-house ArcGIS GIS platform) but no GNSS RTK service is mentioned.
- The island is shared with French Saint Martin (MF), which similarly has no NTRIP caster.
- No rtk2go or Centipede volunteer bases found for SX.
- No IGS permanent station on the island.
- Practical fallback: EarthScope NOTA station ANG1 or CN59 on Anguilla (~20 km northeast) or ABMF/GNSS stations in Guadeloupe (~200 km south) — too far for reliable RTK but usable for PPK.

## Most Recent Project Announcement

**Kadaster St. Maarten Caribbean Cadaster Association (CCA) LOI — 2026-02**
Kadaster St. Maarten and Kadaster Netherlands (BES) signed a Letter of Intent toward a Caribbean Cadaster Association. No NTRIP or GNSS infrastructure component.
Source: https://www.721news.com/2026/02/kadaster-st-maarten-and-kadaster-netherlands-bes-advance-regional-cooperation-with-letter-of-intent-for-caribbean-cadaster-association/

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope NOTA** — ANGUILLA-ANG1 or nearest NOTA station | https://www.earthscope.org/data/gnss-realtime/ | Free noncommercial (NULA) |
| **IGS MGEX / BKG** — nearest stations | https://register.rtcm-ntrip.org/ | Free |

## Sources Consulted
- Kadaster St. Maarten: https://kadaster.sx/ (observed 2026-05-06; no GNSS RTK service mentioned)
- Kadaster NL AGRS (observed 2026-05-06) — no SX endpoint; BES only
- CW_Dutch_Caribbean.md (existing research file confirming BES coverage)
- Caribbean Cadaster Association LOI: https://www.721news.com/2026/02/kadaster-st-maarten-and-kadaster-netherlands-bes-advance-regional-cooperation-with-letter-of-intent-for-caribbean-cadaster-association/
- Kadaster St. Maarten GIS-ready news: https://www.721news.com/2025/07/kadaster-st-maarten-now-officially-gis-ready/
- EarthScope NOTA portal: https://www.earthscope.org/data/gnss-realtime/
