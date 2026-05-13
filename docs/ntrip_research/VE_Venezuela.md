# Venezuela [VE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (re-verification of 2026-05-06 baseline)

## Status: YES — at least two active NTRIP services identified (private commercial + government free); neither publishes a public sourcetable URL

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private commercial + government free) |
| **host:port** | Unknown — acnovo.net credentials delivered post-registration; IGVSB REMOS host not publicly published |
| **tariff** | acnovo.net: ~USD 20 (one-time or per period, exact billing cycle unclear) — observed 2026-05 at cursos.acnovo.net. IGVSB REMOS: free |
| **num_stations** | acnovo.net: not disclosed publicly. IGVSB REMOS: 29 permanent stations (historical figure, current count not republished) |
| **vrs** | acnovo.net: ? (single-base RTCM 3.x is documented; VRS not advertised). IGVSB REMOS: ? |
| **hobbyist_eligibility** | acnovo.net: yes (open online registration); IGVSB REMOS: unclear (appears open, no license requirement stated) |
| **legal_residency_required** | unclear — neither service states a residency requirement explicitly |
| **registration** | acnovo.net: https://acnovo.net/ (contact form) + https://cursos.acnovo.net/courses/curso-de-medicion-con-gnss-ntrip/. IGVSB REMOS: contact via https://igvsb.gob.ve/ |
| **last_confirmed_alive** | acnovo.net: portal returned HTTP 200 on 2026-05-13 (HEAD probe); WordPress article:modified_time still cites 2025-07-01. igvsb.gob.ve: HTTP 200 on 2026-05-13. SIRGAS-RT integration: December 2025 (SIRGAS Americas Facebook). No sourcetable could be probed (host:port not public) |

## Most Recent Project Announcement

**IGVSB CORS → SIRGAS Caster integration** — December 2025 (date inferred from SIRGAS Americas Facebook post):
The IGVSB (Instituto Geográfico de Venezuela Simón Bolívar) reported important advances in incorporating Venezuelan CORS stations into the SIRGAS real-time caster network, thanks to collaborative work with specialists and institutional support.
URL: https://www.facebook.com/SirgasAmericas/posts/1437422241720820/

## Context Notes

- **acnovo.net** ("Servicio NTRIP" / "Acnovo"): Private commercial network operating a CORS grid across Venezuela. Website confirms 24/7 base stations, RTCM 3.x output, compatible with RTK receivers and PPK/RTK drones. No public sourcetable URL found — caster host, port, and mountpoint names are disclosed only after account approval. Website was live and recently updated (last modified 2025-07-01). Operates parallel brand at acnovo.com. Training/subscription portal at cursos.acnovo.net lists "SERVICIO GNSS NTRIP EXPRESS" at USD 20; a promotional coupon code (NTRIPEXPRESS) was cited that may reduce cost to zero — exact duration/validity unclear. Pricing in local currency (VES) not published.
- **IGVSB REMOS** (Red de Estaciones de Monitoreo Satelitar): Government-operated free NTRIP service. Stonex Venezuela's Facebook page advertises "GRATUITO servicio NTRIP para equipos RTK GNSS en tiempo real del IGVSB — alta precisión". The REMOS network has 29 permanent stations installed, with the MARA (Maracaibo) station transmitting to the IGS global NTRIP tier since 31 October 2008. As of the most recent sources, the free service required user registration with IGVSB; endpoint details not surfaced in public search results.
- **SIRGAS integration effort**: As of December 2025 IGVSB was actively integrating its CORS network into the SIRGAS-RT (real-time) caster. This is an ongoing process; full integration timeline unknown.
- **GPS/GNSS jamming caveat**: Significant GPS jamming around Venezuelan territory was reported from September through at least December 2025, driven by US-Venezuela military tensions in the Caribbean. The FAA issued a warning covering Venezuelan airspace (MAIQUETIA FIR) effective 21 November 2025 through 19 February 2026. Ground-based RTK over a local baseline (base + rover) is less affected than satellite-derived PPP, but the operating environment should be noted.
- **Historical context**: NTRIP experiments in Venezuela began circa 2008 (MARA station, Universidad del Zulia, PDVSA). The country has been represented in SIRGAS-RT literature since ~2011. Infrastructure degradation under economic stress was documented in a January 2026 Geo Week News article ("Mapping Venezuela Again"), which noted the IGVSB lacks budgetary means to maintain the entire geodetic network; however, the REMOS NTRIP service appears to have survived as an active offering.
- **Global commercial networks** (GEODNET, ONOCOY, Centipede-RTK, PointOne): No Venezuela coverage confirmed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGVSB REMOS** — static RINEX data from permanent stations (MARA and others); available on request via IGVSB geoportal | https://igvsb.gob.ve/ | Free (government service) |
| **IGS/EarthScope** — MARA station (Maracaibo) is an IGS/SIRGAS-CON station; archival RINEX retrievable via EarthScope | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); USD 1,000/seat/yr commercial |

## Verification (2026-05-13)

- HEAD probe `https://acnovo.net/` → HTTP 200 OK 2026-05-13
- HEAD probe `https://igvsb.gob.ve/` → HTTP 200 OK 2026-05-13
- No public NTRIP host:port could be tested (acnovo.net credentials gated; IGVSB REMOS host not published). No change in stations.json: zero VE stations in the project's tracked sourcetables (rtk2go/centipede/earthscope) as of 2026-05-13.
- WebSearch (2026-05-13) returned no new public 2026 announcement specific to a Venezuelan caster endpoint. SIRGAS-RT integration narrative unchanged from December 2025 baseline.

## Sources Consulted
- acnovo.net homepage (live, last modified 2025-07-01; HTTP 200 2026-05-13)
- cursos.acnovo.net product page — "SERVICIO GNSS NTRIP EXPRESS"
- acnovo.com NTRIP Express service page
- IGVSB official website (igvsb.gob.ve)
- Stonex Venezuela Facebook page — IGVSB free NTRIP announcement
- SIRGAS Americas Facebook post — IGVSB CORS integration, December 2025
- SIRGAS Bulletin 14: "NTRIP in South America Through the SIRGAS-RT Project" (Hoyer et al.)
- SIRGAS Bulletin 15: "Utilización del NTRIP en Venezuela" (Hoyer et al.)
- Revista IPGH/RCAR: "Red de transporte de datos en formato RTCM, vía protocolo de Internet (Ntrip)"
- SciELO Venezuela: "Mediciones GPS NTRIP: una nueva alternativa para el posicionamiento preciso en Venezuela" (2009)
- Geo Week News: "Mapping Venezuela Again: The State of a Broken Geospatial System" (January 2026)
- Bloomberg / RNTF / FAA: GPS jamming reports around Venezuela, Sep–Dec 2025
- NTRIP-list.com South America
- IGS station list (MARA, Maracaibo)
- SIRGAS station list (sirgas.ipgh.org)
