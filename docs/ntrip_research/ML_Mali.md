# Mali [ML] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-verified — still no national caster; conflict + AES governance unchanged. `py scripts/stations_by_country.py MLI` → empty; `py scripts/stations_by_radius.py 12.6 -8.0 1000` → 2 Centipede (CIV INP02, SEN GORA) + 1 rtk2go GIN Gine-Albrk — all far beyond RTK range.)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Most Recent Project Announcement

None found. No Mali-specific CORS/NTRIP announcement found in any public source up to 2026-05-06.

Nearest regional analog: **Senegal JICA CORS project** (Dec 2024) — 5 new stations planned for Senegal.
URL: https://anat.sn/actualites/modernisation-du-reseau-geodesique-le-senegal-va-se-doter-de-5-nouvelles-stations-cors-grace-a-la-jica/10619/

## Context Notes

- **BAMK** (Bamako IGS candidate station): Referenced in older AFREF literature, but NOT present in current IGS network database (zero results for country=ML). No station log file in IGS archive. Likely decommissioned or lapsed. Never confirmed as a public RTK NTRIP stream.
- **IGM** (Institut Géographique du Mali) and **Direction Nationale du Cadastre**: No publicly accessible GNSS/RTK/NTRIP service found.
- **Burkina Faso BF-CORS** (bfcors.net, Trimble Pivot Web): 9 stations deployed 2011 + 4 stations added 2018 = 13 stations, managed by Institut Géographique du Burkina (IGB) since Sep 2012. Network does not extend coverage into Mali. Source: https://www.igb.bf/?page_id=47 (re-fetched 2026-05-21).
- Global commercial networks (GEODNET, ONOCOY, Trimble VRS Now, Swift Skylark, Centipede-RTK): No Mali coverage confirmed.
- Note: Mali's ongoing security situation (Tuareg and jihadist conflicts as of May 2026) further limits infrastructure investment.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| Unknown — no confirmed RINEX archive for Mali. BAMK (Bamako) lapsed/decommissioned; not in any active archive. IGS/CDDIS has no Mali entry. | — | — |

## Sources Consulted
- IGS Network API (network.igs.org) — 0 results for ML
- IGS file archive (files.igs.org/pub/station/log/) — no BAMK log
- RTCM NTRIP Registration registry
- BKG NTRIP/GNSS Datacenter
- NTRIP-list.com Africa
- AFREF (UN-SPIDER)
- RTK2GO, GEODNET, ONOCOY, RTKdata
- GitHub mvarga1989 CORS list
- BF-CORS (Burkina Faso)
- CHCNAV Africa partner network
- World Bank Mali road project May 2025
- `py scripts/stations_by_radius.py 12.6 -8.0 1000` (2026-05-21) — 3 stations within 1000 km of Bamako: Centipede INP02 (CIV), Centipede GORA (SEN), rtk2go Gine-Albrk (GIN, stale); all >300 km from Bamako, far beyond RTK range
- Re-verified 2026-05-21 via WebSearch: still no announcement of a Mali national NTRIP/CORS network
