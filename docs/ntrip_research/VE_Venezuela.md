# Venezuela [VE] — NTRIP RTK
**Date:** 2026-05-17 re-verify: both portals 200 today; IGVSB `/servicios_geodesicos` page now in search index (same content as `/servicio/15`); still no public host:port; no project changes.

## Status
2 likely-active services, neither publishes public host:port. Both portals reachable.

| Field | acnovo.net | IGVSB REMOS |
|---|---|---|
| landing_url | https://acnovo.net/ | https://igvsb.gob.ve/ |
| access_url | https://cursos.acnovo.net/courses/curso-de-medicion-con-gnss-ntrip/ | https://igvsb.gob.ve/servicio/15 |
| host:port | unknown — credentials gated post-registration | unknown — host not public |
| operator | Acnovo (private, also acnovo.com) | IGVSB (Instituto Geográfico de Venezuela Simón Bolívar) |
| num_stations | not disclosed | 8 stations listed on /servicio/15: Puerto Ayacucho (Amazonas), Barinas, Caracas, Coro (Falcón), Barquisimeto (Lara), Maturín (Monagas), Maracaibo (Zulia), + 1 Amazonas. Historical claim: 29 permanent stations (unverified — no operator-side citation). |
| vrs | ? (single-base RTCM 3.x documented; VRS not advertised) | ? |
| tariff | ~USD 20 ("SERVICIO GNSS NTRIP EXPRESS" on cursos.acnovo.net); local-currency price not published; promo code `NTRIPEXPRESS` may zero | Free (Stonex VE FB: "GRATUITO servicio NTRIP"); not stated on /servicio/15 |
| hobbyist_eligibility | yes (open online registration) | ? (no licence requirement stated; registration path not publicly visible) |
| legal_residency_required | unclear | unclear |
| last_confirmed_alive | 2026-05-17: acnovo.net WebFetch 200. WordPress article:modified_time still 2025-07-01. | 2026-05-17: igvsb.gob.ve 200; /servicio/15 lists REMOS stations. No host:port reachable. |
| datum_epoch | omitted — no citable operator declaration | omitted — no citable operator declaration (SIRGAS-REGVEN historically; not declared on portal) |

## Recent project — SIRGAS integration (Dec 2025)

IGVSB reported progress integrating Venezuelan CORS into SIRGAS-RT caster network. Source: https://www.facebook.com/SirgasAmericas/posts/1437422241720820/. Timeline open.

## Context

- acnovo: private commercial CORS grid, 24/7 bases, RTCM 3.x, RTK/PPK drones. No public sourcetable. cursos.acnovo.net training portal lists USD 20 NTRIP Express; VES not published. Live HTTP 200 2026-05-17.
- IGVSB REMOS: gov free service per Stonex VE FB. MARA (Maracaibo) station feeds IGS global tier since 2008-10-31. /servicio/15 enumerates 8 REMOS sites + state-level breakdown but exposes no caster details.
- GPS jamming: significant jamming around VE territory Sep 2025 - Feb 2026; FAA warning MAIQUETIA FIR effective 2025-11-21 → 2026-02-19. Ground-based RTK less affected than PPP.
- 2026-01 Geo Week News: IGVSB lacks budget for full geodetic-network maintenance; REMOS NTRIP appears to have survived.
- Global commercial nets (GEODNET, ONOCOY, PointOne, Centipede): no VE coverage.

## Post-processing (RINEX)

| Service | URL | Cost |
|---|---|---|
| IGVSB REMOS RINEX (request) | https://igvsb.gob.ve/ | Free |
| MARA via IGS/EarthScope | https://www.earthscope.org/data/gnss-data/ | Free non-comm |

## Sources
- https://acnovo.net/ (HTTP 200 2026-05-17)
- https://cursos.acnovo.net/courses/curso-de-medicion-con-gnss-ntrip/
- https://acnovo.com NTRIP Express page
- https://igvsb.gob.ve/ (HTTP 200 2026-05-17)
- https://igvsb.gob.ve/servicio/15 — REMOS stations table
- https://igvsb.gob.ve/servicios_geodesicos — IGVSB services index
- Stonex Venezuela FB — IGVSB free NTRIP
- SIRGAS Americas FB post (Dec 2025): https://www.facebook.com/SirgasAmericas/posts/1437422241720820/
- Geo Week News (Jan 2026): "Mapping Venezuela Again"
- FAA / Bloomberg / RNTF: GPS jamming Sep-Dec 2025
- IGS station list (MARA, Maracaibo)
- SIRGAS station list (sirgas.ipgh.org)
- Project sources: zero VE stations in rtk2go/centipede/earthscope tracked sourcetables (2026-05-13).
