# Mexico [MX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; commercial tariffs unchanged from 2026-05-12/14 snapshot. rtk2go now shows 6 MEX-tagged streams including one spurious `BASE_PAB` at lat 89.87 — misconfigured base, exclude from coverage)

## Status: PARTIAL — no free national NTRIP RTK; INEGI RGNA is RINEX-only; commercial NTRIP RTK is available via several private national resellers (Red CORS México, Survey+, La Casa del Topógrafo, Aeros)

| Field | Value |
|---|---|
| **Public free NTRIP RTK caster** | No — INEGI's national network (RGNA) provides RINEX/PPK only, no real-time RTK stream |
| **Commercial NTRIP RTK (paid)** | Yes — multiple private resellers run nationwide NTRIP networks covering 60–85+ Mexican cities |
| **landing_url — INEGI RGNA** | https://en.www.inegi.org.mx/temas/geodesia_activa/ (operator-owned RGNA description; RINEX-only — out of RTK scope) |
| **access_url — INEGI RGNA** | Skip — RINEX-only; access is anonymous SFTP (`sftp://rgnaftp:rgnaftp@geodesia.inegi.org.mx`), no NTRIP signup portal exists |
| **landing_url — Red CORS México (DTM Topografía)** | https://dtmtopografia.com/cors-mexico/ (reseller landing) |
| **access_url — Red CORS México (Aeros, monthly)** | https://aeros.com.mx/product/servicio-red-cors-mensual/ |
| **landing_url — Survey+ MX** | https://en.surveyplusmx.com/corsmexico (reseller landing; current canonical slug uses é) |
| **access_url — Survey+ MX** | Skip — credentials delivered after purchase via the same product URL; no separate access portal |
| **landing_url — TopNET Live MX** | https://topografiaguadalajara.com/estacion-de-referencia-topnet-live-guadalajara/ (Topcon reseller landing) |
| **access_url — TopNET Live MX** | Skip — credentials issued post-purchase, no separate signup page |
| **landing_url — Punto Visado / Hi-Target Red CORS** | https://www.puntovisado.com/producto/licencia-red-cors-1-mes/ (reseller product page) |
| **access_url — Punto Visado / Hi-Target Red CORS** | Skip — credentials issued post-purchase |
| **num_stations — INEGI RGNA** | ~30 RGNA reference stations + denser RGN integration covering all 32 entidades federativas (RINEX-only, not NTRIP) |
| **num_stations — Red CORS México** | unknown — reseller pages cite coverage of "60–85+ Mexican cities" without a citable physical-station count |
| **num_stations — Survey+ MX** | unknown — reseller cites "31 states, expanding to ~60 cities"; no citable physical-station count |
| **num_stations — TopNET Live MX** | unknown — Topcon's global TopNET Live network publishes no Mexico-specific physical count on the reseller page |
| **num_stations — Hi-Target Red CORS (Punto Visado)** | unknown — reseller publishes no physical-station count |
| **datum_epoch — INEGI RGNA** | omitted — no citable declaration on the indexed INEGI RGNA / geodesia pages; RGNA is RINEX-only and out of RTK scope. Per primer, do NOT infer from SIRGAS or ITRF. |
| **datum_epoch — commercial casters (Red CORS México / Survey+ MX / TopNET Live MX / Hi-Target)** | omitted — no reseller publishes a datum/epoch declaration on its product page; the underlying physical network and datum tie is undocumented in public sources as of 2026-05-17 |
| **host:port — RGNA** | n/a (no NTRIP). Data: SFTP `geodesia.inegi.org.mx` (RINEX), credentials `rgnaftp` / `rgnaftp` (migrated from FTP to SFTP in October 2024) |
| **host:port — commercial** | Not published on product pages; delivered after subscription purchase via the reseller |
| **VRS** | Commercial: not explicitly advertised as VRS — described as "correcciones NTRIP desde estaciones de referencia" with up to ~40 km baseline from nearest station (some operators report acceptable results out to 80–250 km) |
| **tariff — RGNA RINEX** | Free, no registration required for FTP/SFTP read |
| **tariff — Red CORS México (DTM Topografía / Aeros, monthly)** | MXN 2,042 / month (Aeros product page, observed 2026-05-12; VAT/IVA inclusion not stated) |
| **tariff — Red CORS México 12 months (La Casa del Topógrafo)** | MXN 20,500 / year (observed 2026-05-12; VAT/IVA inclusion not stated) — also sells 7-day, 1, 3, 6, 12-month options |
| **tariff — Survey+ MX (Hi-Target / GeoMax devices)** | MXN 1,320 / month + IVA · MXN 13,200 / year + IVA (observed 2026-05-12) |
| **tariff — Survey+ MX (other GNSS brands)** | MXN 1,760 / month + IVA · MXN 17,600 / year + IVA (observed 2026-05-12) |
| **tariff — Hi-Target Red CORS MX (Punto Visado 1-month)** | MXN 2,350 / month, IVA incluido (observed 2026-05-14 via puntovisado.com) |
| **tariff — TopNET Live MX (Topcon-branded reseller)** | USD 1,200 / year + IVA per subscription (observed 2026-05-12 via topografiaguadalajara.com) |
| **hobbyist_eligibility** | RGNA RINEX: Yes (anonymous FTP). Commercial NTRIP: Yes — no surveyor's licence required; subscription is sold to any buyer, paid via Mexican payment methods (Mexican phone numbers in vendor sign-up flow) |
| **legal_residency_required** | RGNA: No. Commercial: No explicit residency requirement, but every operator uses WhatsApp/local-phone sales and bills in MXN — practical friction for foreign hobbyists is high |
| **last_confirmed_alive** | INEGI RGNA English page (en.www.inegi.org.mx/temas/geodesia_activa/) reachable 2026-05-12; Aeros, DTM, La Casa del Topógrafo, Survey+ MX product pages all reachable 2026-05-12 |

## INEGI RGNA (national network, RINEX only)

- **Operator**: Instituto Nacional de Estadística y Geografía (INEGI), Dirección General de Geografía y Medio Ambiente.
- **Network**: ~30 RGNA reference stations + denser RGN integration, covering all 32 entidades federativas.
- **Service**: 15-second RINEX for post-processing only. October 2024 migration FTP → SFTP at `geodesia.inegi.org.mx` (user `rgnaftp` / pass `rgnaftp`). INEGI's English page explicitly markets the service as "post-processing" / "PPK" — no real-time NTRIP product is offered.
- **Historical note**: A 2013 SIRGAS bulletin recorded INEGI's intent to publish an NTRIP caster (in-house BKG NTRIP Caster), but no live INEGI-operated public NTRIP host has been documented through 2026-05-12.

## Commercial NTRIP RTK (paid)

| Reseller | Branded service | Coverage claim | Annual price | Source URL |
|---|---|---|---|---|
| DTM Topografía | Red CORS México | "más de 85 ciudades", 24/7 | n/a — monthly only | https://dtmtopografia.com/cors-mexico/ |
| Aeros | Red CORS México (reseller) | National | MXN 2,042 / month | https://aeros.com.mx/product/servicio-red-cors-mensual/ |
| La Casa del Topógrafo | CORS México (12-month plan) | "60 ciudades de México", ~80 km optimal, up to 250 km tested | MXN 20,500 / year | https://www.topografia.com/wptopo/producto/corsmexico-12meses/ |
| Survey+ MX | GeoCORS / Red CORS | 31 states, expanding to ~60 cities | MXN 13,200–17,600 / year + IVA depending on receiver brand | https://en.surveyplusmx.com/corsmexico |
| TopNET Live MX (Topcon distributor) | TopNET Live | Topcon-aligned national | USD 1,200 / year + IVA | https://topografiaguadalajara.com/estacion-de-referencia-topnet-live-guadalajara/ |
| Punto Visado | Hi-Target Red CORS 1-month licence | Hi-Target-aligned national | MXN 2,350 / month (IVA incluido) | https://www.puntovisado.com/producto/licencia-red-cors-1-mes/ |

**Note on identity**: "Red CORS México" appears to be a single physical commercial network resold under multiple vendor product pages (DTM Topografía, Aeros, La Casa del Topógrafo all market the same product description). Survey+ MX appears to be a separate parallel network (their own GeoCORS infrastructure across 31 states). TopNET Live is the Topcon-operated global network with a Mexico subscription.

## Volunteer & Open Coverage

- **rtk2go**: 6 MEX-tagged streams as of 2026-05-17 — BASE2_SG_ST1 (Tampico area 22.27 N -97.85), Casantrip305 + mp1854021 (Monterrey/Coahuila area 25.82 N -100.60, twin entries), HelgenTestStation (Querétaro area 20.59 N -100.35), RTK_BASE_IBERO (Puebla 19.03 N -98.24), and a spurious `BASE_PAB` at lat 89.87 N (mis-tagged MEX in caster metadata; physically near North Pole, not usable). ZEFE (Tijuana area 31.79 N -116.59) observed earlier has dropped off the sourcetable. Coverage is sparse; useful only within ~30 km of each legitimate base. (palmitasrtk in Sinaloa, observed 2026-05-12, has since dropped off.)
- **EarthScope (NOTA)**: 18 stations tagged MEX in EarthScope's NTRIP sourcetable (e.g. BDLA/CN24/CN25/GUAX/PALX/QUEX/TNMT etc.), free with EarthScope NULA seat for non-commercial; $1,000/seat/yr for commercial. NOTA Mexico stations cluster along the northern border and a research line in the south.
- **Centipede**: No MEX stations.
- **Galileo HAS**: Free PPP-RTK globally (decimetre-class, ~5 min convergence) — not RTK, but a viable hobbyist alternative.

## Most Recent Project / Announcement

No announced project to deploy a free national NTRIP RTK caster in Mexico was found as of 2026-05-12. INEGI's 2024 SFTP migration is an infrastructure maintenance update for the RINEX service, not a real-time service launch.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **INEGI RGNA** — RINEX via SFTP | `sftp://rgnaftp:rgnaftp@geodesia.inegi.org.mx` | Free, no registration |
| **INEGI RGNA** — information page (EN) | https://en.www.inegi.org.mx/temas/geodesia_activa/ | Free |
| **EarthScope** — Mexican station RINEX archive (TNxx, CNxx, etc.) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA + seat) |

## Sources Consulted
- INEGI RGNA English page: https://en.www.inegi.org.mx/temas/geodesia_activa/ (observed 2026-05-12)
- INEGI Geodesia: https://geodesia.inegi.org.mx
- Red CORS México (DTM Topografía): https://dtmtopografia.com/cors-mexico/ (observed 2026-05-12)
- Aeros Red CORS monthly product page: https://aeros.com.mx/product/servicio-red-cors-mensual/ (observed 2026-05-12)
- La Casa del Topógrafo 12-month CORS Mexico: https://www.topografia.com/wptopo/producto/corsmexico-12meses/ (observed 2026-05-12)
- Survey+ MX CORS México: https://en.surveyplusmx.com/corsm%C3%A9xico (current slug uses é; legacy slug `/corsmexico` now 404s as of 2026-05-14; pricing re-confirmed)
- TopNET Live México (topografiaguadalajara.com): https://topografiaguadalajara.com/estacion-de-referencia-topnet-live-guadalajara/ (observed 2026-05-12)
- ArduSimple Mexico: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-mexico/
- SIRGAS 2013 bulletin on INEGI NTRIP aspirations: sirgas.ipgh.org
- Local data: `py scripts/stations_by_country.py MEX` — 6 rtk2go (one spurious lat 89.87) + 18 EarthScope MEX-tagged streams = 24 MPs across 2 sources (2026-05-17 snapshot)
