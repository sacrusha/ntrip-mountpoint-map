# Rwanda [RW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior versions: 2026-05-12, 2026-05-06)

## Status: PARTIAL — national CORS network operational; public NTRIP RTK endpoint not confirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — CORS network exists; NTRIP RTK streaming status unclear |
| **host:port** | Not publicly documented |
| **tariff** | CORS data stated as free of charge (distributed by RLMUA) |
| **hobbyist_eligibility** | Unclear — no public sign-up portal found |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | 2026-05-17 — lands.rw geodetic article URL now returns 404 (article moved/removed since 2026-05-12 fetch); no RGN NTRIP host:port disclosed in any 2026 public source. EarthScope fallback (3 stations) re-confirmed in local archive 2026-05-17 |
| **datum / epoch** | No operator declaration found on lands.rw / rlma.rw / geodata.rw → `omitted -- no citable operator declaration`. Rwanda is on Africa plate; AFREF aligns with ITRF, but RLMUA has not published a portal-level declaration. |

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
- **EarthScope NOTA presence in Rwanda (re-verified 2026-05-17)**: `py scripts/stations_by_country.py RWA` → 3 EarthScope stations clustered in western Rwanda near DRC border: KMBR_RTCM3P3 (-1.83, 29.29), NYBA_RTCM3P3 (-1.76, 29.35), RUBO_RTCM3P3 (-1.73, 29.26). 1 Hz raw RTCM single-base at `ntrip.earthscope.org:2101` — useful for short-baseline RTK near Lake Kivu / Rubavu / Karongi, free under NULA non-commercial. For hobbyist surveying in western Rwanda this is the only confirmed free real-time fallback while RLMUA's RGN endpoint remains undisclosed.

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
- WebSearch 2026-05-12 — "Rwanda RGN CORS NTRIP RLMUA host port lands.rw 2026 caster" — no NTRIP host:port disclosed in any public source; RLMUA article date not visible on the page
- WebFetch lands.rw geodetic article 2026-05-12: 10 CORS stations confirmed, data "free of charge", "real time accurate positioning" mentioned as a trend; no host:port, no registration URL, no RTK confirmation
- WebFetch lands.rw / news-detail / what-is-geodetic-network-and-how-it-works 2026-05-17: HTTP 404 (article URL removed); homepage no longer surfaces RGN-related technical detail
- WebFetch geodata.rw 2026-05-17: empty/blank content returned
- Local: `py scripts/stations_by_country.py RWA` → 3 EarthScope stations near Lake Kivu (re-verified 2026-05-17)
