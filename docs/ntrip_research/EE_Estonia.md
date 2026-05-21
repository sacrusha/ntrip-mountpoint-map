# Estonia [EE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-06)

## Status: YES — free national NTRIP (ESTPOS); free until 31 August 2026 per director-general order 1-17/26/131; tariff TBD afterward (re-verified 2026-05-21: portal still describes the service as "free to use for anyone until 31.08.2026"; 40 CORS confirmed)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Maa- ja Ruumiamet (Estonian Land and Spatial Development Board; formerly Maaamet / Estonian Land Board) |
| **landing_url** | https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html (mirror at geoportaal.maaruum.ee) |
| **access_url** | https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html — same page documents the three-step access flow (portal account → order in shop → sign contract); contact `estpos@maaruum.ee` |
| **host:port** | `gnss-rtk.maaamet.ee:8083` (IP 213.184.51.72; domain migrating to maaruum.ee — check geoportaal.maaruum.ee if maaamet.ee fails) |
| **num_stations** | 40 CORS — operator-stated "40 GNSS reference stations evenly covering Estonia"; all 40 in EPOS, 4 in EPN |
| **vrs** | Yes — VRS, iMAX, and nearest-station solutions available |
| **Mountpoints** | `DGNSS_iMAX`, `DGNSS_VRS`, `DGNSS_Nearest`; `RTCM2_iMAX`, `RTCM2_VRS`, `RTCM2_Nearest`; `RTCM3_iMAX`, `RTCM3_VRS`, `RTCM3_Nearest`; `MSM5_iMAX`, `MSM5_VRS`, `MSM5_Nearest` |
| **tariff** | Free until 31 August 2026 per Maa- ja Ruumiamet director-general order 1-17/26/131; post-August 2026 tariff not announced. Source: https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html (observed 2026-05-21) |
| **hobbyist_eligibility** | Yes — "free to use for anyone" (per directive); ESTPOS portal account required; no professional licence check |
| **legal_residency_required** | ? — current portal language sets no explicit residency restriction ("free to use for anyone"); the access flow requires a portal account + signed ESTPOS contract, and earlier ESTPOS releases enforced an Estonia-only IP filter. Foreign access plausible but not explicitly confirmed; ask `estpos@maaruum.ee` before relying on it cross-border. |
| **last_confirmed_alive** | 2026-05-21 — geoportal landing page returns ESTPOS narrative with the unchanged "free until 31.08.2026" clause; NTRIP port `gnss-rtk.maaamet.ee:8083` did not respond from this sandbox (consistent with prior probes — likely geo/IP filter, not authoritative as a liveness signal) |
| **datum_epoch** | Datum ETRS89 (national realization EUREF-EST97); epoch 1989.0 declared by operator — "ETRS89 coincides with the International Terrestrial Reference System (ITRS) of the International Earth Rotation Service (IERS) on epoch 1989.0". Source: https://geoportaal.maaamet.ee/eng/Spatial-Data/Geodetic-Data/Geodetic-System-p668.html |

## Registration Process

1. Go to the ESTPOS portal: https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html
2. Create an ESTPOS user account
3. Order the desired service through the portal shop
4. Sign an ESTPOS contract
5. Receive NTRIP credentials via email
6. Connect to `gnss-rtk.maaamet.ee:8083` using provided credentials

## Network Details

- **Stations:** 40 continuously operating reference stations (CORS) as of June 2025; even nationwide coverage
- **Infrastructure:** Rebuilt 2024–2025 with EU NextGenerationEU funding
- **Constellations:** Multi-constellation (GPS, GLONASS, Galileo, BeiDou)
- **Part of:** EUREF Permanent Network (EPN) — aligns Estonia's national reference frame (EST97/ETRS89) with European geodetic infrastructure
- **Services:** Real-time RTK corrections (RTCM 3.x MSM), RINEX archives, Virtual RINEX, transformation tools, live station status
- **Note on free period:** The free-until-August-2026 window was extended from an earlier trial that began April 2025; the Board has framed GNSS as "an essential public good." Monitor maaruum.ee/announcements for future tariff decisions.

## Domain Migration Note

The Land Board (Maaamet) has rebranded to Maa- ja Ruumiamet with domain maaruum.ee. Both the old (maaamet.ee) and new domains are active simultaneously during the transition period. ESTPOS user manual 2026 is available at geoportaal.maaruum.ee as well as geoportaal.maaamet.ee.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ESTPOS RINEX archive** — free per 2026 directive; download via portal | https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html | **Free** until 31 Aug 2026 |
| **EUREF/EPN archive** — Estonian EPN stations | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- ESTPOS geoportal (Maaamet): https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html (observed 2026-05-21; free-until-31.08.2026 clause + three-step access flow + contact `estpos@maaruum.ee` unchanged)
- ESTPOS user manual 2026 PDF: https://geoportaal.maaamet.ee/docs/Geodeesia/ESTPOS_user_manual_2026.pdf
- ESTPOS user manual (maaruum mirror): https://geoportaal.maaruum.ee/docs/Geodeesia/ESTPOS_user_manual_2026.pdf
- Estonian Permanent GNSS network article: https://geoportaal.maaamet.ee/eng/Spatial-Data/Geodetic-Data/Geodetic-Networks/Estonian-Permanent-GNSS-Reference-Station-Network-p671.html (40 stations; 4 in EPN; all 40 in EPOS; 2024–2025 reconstruction funded by EU NextGenerationEU)
- Estonian Geodetic System (datum + epoch citation): https://geoportaal.maaamet.ee/eng/Spatial-Data/Geodetic-Data/Geodetic-System-p668.html (ETRS89 / EUREF-EST97 / coincides with ITRS at epoch 1989.0)
- Inside GNSS — "Estonia Expands ESTPOS": https://insidegnss.com/estonia-expands-estpos-to-strengthen-gnss-resilience/
- ArduSimple Estonia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-estonia/
