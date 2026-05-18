# Estonia [EE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; original 2026-05-06)

## Status: YES — free national NTRIP (ESTPOS); free until 31 August 2026 per director-general order 1-17/26/131; tariff TBD afterward (re-verified 2026-05-17: portal still describes service as "free to use for anyone until 31.08.2026"; 40 CORS confirmed; ESTPOS user manual reissued 12.03.2026)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | Maa- ja Ruumiamet (Estonian Land and Spatial Development Board; formerly Maaamet / Estonian Land Board) |
| **landing_url** | https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html (mirror: https://geoportaal.maaruum.ee/...) |
| **access_url** | https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html (same page describes account creation + ordering flow; portal account at geoportaal.maaamet.ee) |
| **host:port** | `gnss-rtk.maaamet.ee:8083` (IP 213.184.51.72; domain migrating to maaruum.ee — check geoportaal.maaruum.ee if maaamet.ee fails) |
| **VRS** | Yes — iMAX, VRS, and nearest-station solutions available |
| **Mountpoints** | `DGNSS_iMAX`, `DGNSS_VRS`, `DGNSS_Nearest`; `RTCM2_iMAX`, `RTCM2_VRS`, `RTCM2_Nearest`; `RTCM3_iMAX`, `RTCM3_VRS`, `RTCM3_Nearest`; `MSM5_iMAX`, `MSM5_VRS`, `MSM5_Nearest` |
| **tariff** | **Free until 31 August 2026** per Estonian Land and Spatial Development Board director-general directive; post-August 2026 tariff not yet announced. Date observed: 2026-05-06. Source: https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html |
| **hobbyist_eligibility** | **Yes** — "free to use for anyone" (per directive); ESTPOS portal account required; no professional licence check |
| **legal_residency_required** | ? — internationally accessible per current portal language; no geographic restriction explicitly published, but earlier ESTPOS versions had Estonia-only IP filter and current status with expanded network is not confirmed. Verify before relying on cross-border access. |
| **last_confirmed_alive** | ESTPOS geoportal (geoportaal.maaamet.ee) HTTP 200 confirmed 2026-05-17; user manual reissued 2026-03-12; NTRIP port `gnss-rtk.maaamet.ee:8083` TCP-timed-out from this sandbox 2026-05-17 (likely geo/IP filter — not authoritative as a liveness signal) |
| **datum_epoch** | **EUREF-EST97** — national realization of ETRS89 per operator-published Geodetic System page (https://geoportaal.maaamet.ee/eng/Spatial-Data/Geodetic-Data/Geodetic-System-p668.html). Epoch not stated as a citable value on that page; operator-declaration of an explicit epoch not located. Earlier inference that ETRS89 coincides with ITRS at 1989.0 is editorial and removed per [datum-epoch] citation rule. |

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
- ESTPOS geoportal (Maaamet): https://geoportaal.maaamet.ee/eng/Spatial-Data/ESTPOS-national-GNSS-satellite-data-center-p839.html
- ESTPOS user manual 2026 PDF: https://geoportaal.maaamet.ee/docs/Geodeesia/ESTPOS_user_manual_2026.pdf
- ESTPOS user manual (maaruum domain): https://geoportaal.maaruum.ee/docs/Geodeesia/ESTPOS_user_manual_2026.pdf
- Estonian Permanent GNSS network article: https://geoportaal.maaamet.ee/eng/Spatial-Data/Geodetic-Data/Geodetic-Networks/Estonian-Permanent-GNSS-Reference-Station-Network-p671.html (40 stations; 4 in EPN; all 40 in EPOS)
- Estonian Geodetic System (datum citation): https://geoportaal.maaamet.ee/eng/Spatial-Data/Geodetic-Data/Geodetic-System-p668.html
- Inside GNSS — "Estonia Expands ESTPOS": https://insidegnss.com/estonia-expands-estpos-to-strengthen-gnss-resilience/
- ArduSimple Estonia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-estonia/
