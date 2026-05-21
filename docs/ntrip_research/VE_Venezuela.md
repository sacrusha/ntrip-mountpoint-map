# Venezuela [VE] — NTRIP RTK

## Status
2 likely-active services, neither publishes public host:port. Both portals reachable.

| Field | acnovo.net | IGVSB REMOS |
|---|---|---|
| landing_url | https://acnovo.net/ | https://igvsb.gob.ve/ |
| access_url | https://acnovo.net/precio/ (pricing + signup-info page) | https://igvsb.gob.ve/servicio/15 (REMOS service description + station list) |
| host:port | unknown — credentials gated post-registration | unknown — host not public |
| operator | Acnovo (private, also acnovo.com) | IGVSB (Instituto Geográfico de Venezuela Simón Bolívar) |
| num_stations | not disclosed | 7 stations confirmed on https://igvsb.gob.ve/servicio/15 (Puerto Ayacucho/Amazonas, Barinas, Caracas/Distrito Capital, Coro/Falcón, Barquisimeto/Lara, Maturín/Monagas, Maracaibo/Zulia). Historical claim of 29 permanent stations exists in older sources but no operator-side citation; current operator page shows 7. |
| vrs | ? (single-base RTCM 3.x documented; VRS not advertised) | ? |
| tariff | USD 30/month — single tier on https://acnovo.net/precio/ ("$30 mensuales", "acceso 24/7 a nuestra red de correcciones NTRIP", "centimeter-level real-time precision", 2026-05-21). VES not published. Older cursos.acnovo.net "NTRIP Express" training listing showed ~USD 20 — superseded by operator pricing page. | Free per Stonex Venezuela Facebook post ("GRATUITO servicio NTRIP para equipos RTK GNSS en tiempo real del IGVSB", https://www.facebook.com/stonexvenezuela/posts/732126826897978/); not stated on /servicio/15. |
| hobbyist_eligibility | yes (open online registration) | yes — Stonex VE FB advertises service as `GRATUITO` (free) with no licence requirement stated; IGVSB /servicio/15 does not impose hobbyist exclusion. |
| legal_residency_required | unclear | unclear |
| last_confirmed_alive | 2026-05-21: acnovo.net WebFetch 200; acnovo.net/precio/ 200 with $30/mo tier. | 2026-05-21: igvsb.gob.ve 200; /servicio/15 lists 7 REMOS stations (WebFetch result). No host:port reachable. |
| datum_epoch | omitted — no citable operator declaration | omitted — no citable operator declaration (SIRGAS-REGVEN historically; not declared on portal) |

## Recent project — SIRGAS-RT integration (Dec 2025)

SIRGAS Americas FB post (Dec 2025) describes progress integrating Venezuelan CORS into the SIRGAS-RT realtime caster network. Source: https://www.facebook.com/SirgasAmericas/posts/1437422241720820/. Timeline open. If integration completes, VE stations may become hobbyist-accessible via SIRGAS-RT caster (whose own hobbyist-eligibility / registration model needs separate verification).

## Context

- **acnovo:** private commercial CORS grid, 24/7 bases, RTCM 3.x, RTK/PPK drones. No public sourcetable. Operator pricing page (https://acnovo.net/precio/) lists single tier USD $30/month; VES not published. Live HTTP 200 2026-05-21.
- **IGVSB REMOS:** government free service per Stonex VE FB. MARA (Maracaibo) station feeds IGS global tier since 2008-10-31. /servicio/15 enumerates 7 REMOS sites + state-level breakdown but exposes no caster details (host:port not visible without auth/contact).
- **GPS jamming:** significant jamming around VE territory Sep 2025 - Feb 2026; FAA warning MAIQUETIA FIR effective 2025-11-21 → 2026-02-19. Ground-based RTK less affected than PPP.
- **Funding:** 2026-01 Geo Week News reported IGVSB lacks budget for full geodetic-network maintenance; REMOS NTRIP appears to have survived.
- **Global commercial networks** (GEODNET, ONOCOY, PointOne, Centipede): no VE coverage.

## Post-processing (RINEX)

| Service | URL | Cost |
|---|---|---|
| IGVSB REMOS RINEX (request) | https://igvsb.gob.ve/ | Free |
| MARA via IGS/EarthScope | https://www.earthscope.org/data/gnss-data/ | Free non-comm |

## Sources
- https://acnovo.net/
- https://acnovo.net/precio/ ($30/month single tier)
- https://cursos.acnovo.net/courses/curso-de-medicion-con-gnss-ntrip/ (older training-course listing)
- https://acnovo.com NTRIP Express page
- https://igvsb.gob.ve/
- https://igvsb.gob.ve/servicio/15 — 7 REMOS stations (Puerto Ayacucho, Barinas, Caracas, Coro, Barquisimeto, Maturín, Maracaibo)
- https://igvsb.gob.ve/servicios_geodesicos — IGVSB services index
- Stonex Venezuela FB (free NTRIP service): https://www.facebook.com/stonexvenezuela/posts/732126826897978/
- SIRGAS Americas FB post (Dec 2025): https://www.facebook.com/SirgasAmericas/posts/1437422241720820/
- Geo Week News (Jan 2026): "Mapping Venezuela Again"
- FAA / Bloomberg / RNTF: GPS jamming Sep-Dec 2025
- IGS station list (MARA, Maracaibo)
- SIRGAS station list (sirgas.ipgh.org)
- Project sources: zero VE stations in rtk2go/centipede/earthscope/auscors/igs_ip; `stations_by_country.py VE`/`VEN` 2026-05-21 → "No stations".
