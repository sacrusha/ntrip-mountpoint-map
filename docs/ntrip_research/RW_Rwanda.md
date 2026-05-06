# Rwanda [RW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: PARTIAL — national CORS network operational; public NTRIP RTK endpoint not confirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — CORS network exists; NTRIP RTK streaming status unclear |
| **host:port** | Not publicly documented |
| **tariff** | CORS data stated as free of charge (distributed by RLMUA) |
| **hobbyist_eligibility** | Unclear — no public sign-up portal found |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | CORS network confirmed operational; last update found 2024 (lands.rw article) |

## Most Recent Project Announcement

The Rwanda Land Management and Use Authority (RLMUA / formerly RLMA) has operated the Rwanda Geodetic Network (RGN) — a network of 10 Continuously Operating Reference Stations (CORS) — with data stated to be distributed free of charge. The network supports DGPS and RTK corrections.

An academic pilot project report (Academia.edu) on the establishment of the CORS geodetic network in Rwanda is the foundational documentation. RLMUA's website (lands.rw) published a plain-language explainer article: "What is Geodetic Network and how it works," describing real-time RTK positioning for surveyors and engineers.

A 2026-01 news article noted a backlog of 50,000+ land surveying applications in Rwanda, implying the CORS network is actively relied upon for cadastral surveys.

## Context Notes

- **10 CORS sites**: Confirmed operational, spread across Rwanda. The recommended density of 1 station per 70–100 km suggests 15–18 stations would be needed for full coverage; current network may have gaps in mountainous zones.
- **RTK vs. RINEX**: RGN's stated purpose covers real-time (DGPS/RTK) and post-processing (RINEX) use. However, no public NTRIP caster hostname, port, or sign-up form has been documented in open sources.
- **Access pathway**: Likely requires contact with RLMUA directly (lands.rw or rlma.rw) to obtain NTRIP credentials. The network is stated to be free of charge.
- **CORSmap**: Rwanda's 10 CORS sites appear on corsmap.com/location/rwanda/ with metadata; that page links back to RLMUA rather than providing direct NTRIP access.
- **Challenges noted**: Power instabilities, insufficient user training, and limited system sustainability are documented challenges (RLMUA's own reporting).
- **Practical workaround**: Contact RLMUA for CORS/NTRIP access, or deploy a local base station. Satellite PPP (Galileo HAS, Trimble RTX) is a viable fallback.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **Rwanda Land Authority / RLMUA** — RINEX data from RGN CORS stations | https://www.lands.rw | Unknown — contact agency |
| **EarthScope GNSS Data Archive** — any Rwanda IGS-affiliated stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |

## Sources Consulted
- Rwanda Land Authority (lands.rw) — "What is Geodetic Network and how it works"
- rlma.rw — same article (mirror)
- Academia.edu — "Report on Pilot Project, Establishment of CORS Geodetic Network in Rwanda"
- AllAfrica — "Rwanda: Land Surveying Faces Backlog of Over 50,000 Pending Applications" (Jan 2026)
- Africa-Press — same article
- CORSmap.com — Rwanda location page
- GIM International — "Developing a Fully Fledged CORS Map for Africa"
- RTK2go monitor — no Rwanda NTRIP streams confirmed
- NTRIP-list.com — no Rwanda entry
- ArduSimple country selector — no Rwanda page found
