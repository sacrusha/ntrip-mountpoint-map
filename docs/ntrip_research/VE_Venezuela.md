# Venezuela [VE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — at least two active NTRIP casters identified

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private commercial + government free) |
| **host:port** | Unknown — acnovo.net credentials delivered post-registration; IGVSB REMOS host not publicly published |
| **tariff** | acnovo.net: ~USD 20 (one-time or per period, exact billing cycle unclear) — observed 2026-05 at cursos.acnovo.net. IGVSB REMOS: free |
| **hobbyist_eligibility** | acnovo.net: yes (open online registration); IGVSB REMOS: unclear (appears open, no license requirement stated) |
| **legal_residency_required** | unclear — neither service states a residency requirement explicitly |
| **last_confirmed_alive** | acnovo.net: 2025-07-01 (WordPress article:modified_time in page header). IGVSB: December 2025 (SIRGAS Americas Facebook post confirming CORS integration progress) |

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

## Sources Consulted
- acnovo.net homepage (live, last modified 2025-07-01)
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
