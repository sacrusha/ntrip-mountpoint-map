# Mexico [MX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (Hi-Target Mexico monthly tariff bump observed: MXN 2,350 → MXN 2,368 IVA inc.; INEGI RGNA datum/epoch now citable from CALE2024_itrf2008.pdf — ITRF2008 epoch 2010.0; Survey+ MX canonical URL `cors-m%C3%A9xico` returns HTTP 404 on probe 2026-05-22 — operator page may be temporarily down or restructured, parent domain `en.surveyplusmx.com` reachable)

## Status: PARTIAL — no free national NTRIP RTK. INEGI RGNA is RINEX-only (post-processing). Real-time RTK in Mexico is sold by private resellers (Red CORS México, Survey+ MX, Hi-Target Red CORS, TopNET Live). Free real-time hobbyist path: 15 EarthScope NOTA stations + 4 rtk2go community bases (per local pipeline 2026-05-22).

| Field | Value |
|---|---|
| Free national NTRIP RTK | No — INEGI RGNA is post-processing RINEX only |
| Free real-time alternatives | EarthScope NOTA (15 MEX-tagged single-base streams, NULA), rtk2go (4 community bases — all currently `nmea=1` flagged, see caveat below) |
| Commercial national NTRIP RTK | Yes — Red CORS México (DTM/Aeros/La Casa del Topógrafo resold), Survey+ MX (GeoCORS), Hi-Target Red CORS, TopNET Live México |
| hobbyist_eligibility | RGNA RINEX: Yes (anonymous FTP). Commercial NTRIP: Yes — no surveyor licence; subscription open to any buyer; Mexican payment methods required |
| legal_residency_required | No explicit residency requirement; all commercial operators use WhatsApp/local-phone sales + MXN billing — practical friction for foreign hobbyists |

## INEGI RGNA — national post-processing reference (not NTRIP)

| Field | Value |
|---|---|
| Operator | Instituto Nacional de Estadística y Geografía (INEGI), DGGMA |
| landing_url | https://en.www.inegi.org.mx/temas/geodesia_activa/ |
| access_url | https://inegi.org.mx/app/geo2/rgna/ (RINEX selector + station info — anonymous SFTP credentials below) |
| Service | RINEX 2.11 + RINEX 3.04 + raw Trimble T02 (hourly + 15s); post-processing only — no real-time NTRIP |
| FTP/SFTP | `sftp://rgnaftp:rgnaftp@geodesia.inegi.org.mx` (open creds; FTP→SFTP migration October 2024) |
| num_stations | ~30 RGNA stations (calendar CALE2024_itrf2008.pdf enumerates ~30 site codes: CHET COL2 CULC CULN ICAM ICEP ICHI ICHS ICMX ICVT IDGO IHER IHID IIEG IMIE IMIP INAY INEG IPAZ ISLP ITLA IZAC MERI MEXI MTY2 OAX2 TAMP TOL2 UGTO UQRO UVER VIL2) covering all 32 entidades federativas |
| datum_epoch | **ITRF2008, epoch 2010.0** — INEGI calendar PDF title "COORDENADAS GEODÉSICAS DE LAS ESTACIONES DE LA RGNA (ITRF2008, ÉPOCA 2010.0)" CALE2024_itrf2008.pdf (https://www.inegi.org.mx/contenidos/temas/geodesia_activa/doc/CALE2024_itrf2008.pdf, 2024-05-01 update); meta-keywords on https://en.www.inegi.org.mx/temas/geodesia_activa/ also list "ITRF2008" |
| tariff | Free, no registration required for FTP/SFTP read |
| last_confirmed_alive | 2026-05-22 — `en.www.inegi.org.mx/temas/geodesia_activa/` HTTP 200; CALE2024 PDF parseable |

A 2013 SIRGAS bulletin documented INEGI intent to publish a BKG NTRIP caster. No live INEGI-operated public NTRIP host has materialised through 2026-05-22.

## Commercial NTRIP RTK (paid, real-time)

| Reseller | Branded service | Coverage claim | Tariff (observed 2026-05-22) | Source URL |
|---|---|---|---|---|
| DTM Topografía | Red CORS México | "más de 85 ciudades", 24/7 | (no public tariff; quote-on-contact) | https://dtmtopografia.com/cors-mexico/ |
| Aeros | Red CORS México (reseller) | National | MXN 2,042/month (IVA inclusion not stated) | https://aeros.com.mx/product/servicio-red-cors-mensual/ |
| La Casa del Topógrafo | Red CORS México (12-month plan) | "60 ciudades", optimal <80 km, tested up to 250 km | MXN 20,500/year (IVA inclusion not stated) | https://www.topografia.com/wptopo/producto/corsmexico-12meses/ |
| Survey+ MX | GeoCORS (Survey+) | "55+ stations" — Mexico City, Monterrey, Guadalajara, Tijuana, Morelia and many others (operator copy) | MXN 1,320/month + IVA · MXN 13,200/year + IVA (Hi-Target/GeoMax); MXN 1,760/month + IVA · MXN 17,600/year + IVA (other brands) | https://en.surveyplusmx.com/ (parent reachable; canonical `/cors-m%C3%A9xico` and legacy `/corsmexico` both HTTP 404 on probe 2026-05-22) |
| Punto Visado | Hi-Target Red CORS (1-month) | Hi-Target-aligned national | MXN 2,368/month, IVA inc. (observed 2026-05-22; prior MXN 2,350 in May 2026) | https://www.puntovisado.com/producto/licencia-red-cors-1-mes/ |
| topografiaguadalajara.com | TopNET Live México (Topcon distributor) | Topcon global, Mexico subscription | USD 1,200/year + IVA | https://topografiaguadalajara.com/estacion-de-referencia-topnet-live-guadalajara/ |

**Common shape:** All commercial resellers withhold the host:port until subscription is paid; credentials are issued by email/WhatsApp post-purchase. None publish a sourcetable. None publish a datum/epoch declaration on the product page — `datum_epoch` is therefore omitted for every commercial caster (no operator declaration exists).

**Identity note:** "Red CORS México" appears to be a single underlying physical network resold by DTM Topografía / Aeros / La Casa del Topógrafo (same product description across all three). Survey+ MX runs its own separate GeoCORS infrastructure ("31 states, expanding to ~60 cities" / "55+ stations"). Hi-Target Red CORS (Punto Visado) and TopNET Live are distinct again.

**num_stations** for every commercial network: unknown — coverage is marketed in "cities" not citable station counts.

**vrs** for every commercial network: not explicitly advertised as VRS — reseller copy describes "correcciones NTRIP desde estaciones de referencia" with operator-recommended ≤40 km baseline; some operators report acceptable accuracy out to 80–250 km, consistent with single-base + extrapolation (no NRTK product language).

## Free real-time alternatives (snapshot via `py scripts/stations_by_country.py MEX` 2026-05-22 = 15 EarthScope + 4 rtk2go = 19 stations across 2 sources)

**EarthScope NOTA** — 15 MEX-tagged single-base RTCM 3 streams on `ntrip.earthscope.org:2101`. Coverage: northern border belt (BDLA, GUAX, NAYX, PALX, PB1Y, PHJX, PLTX, QUEX), Pacific seismic line (TNAT, TNCC, TNCN, TNIF, TNLC), and southern Mexico (CN24 Yucatán, CN25 Chiapas). Free non-commercial with EarthScope account + NULA acceptance. Commercial USD 1,000/seat/yr (5-seat minimum, 2-week 5-seat trial). datum_epoch: ITRF2014, NOTA epoch 2026-03-30 — declared at https://www.earthscope.org/data/gnss-realtime/. Source: TLALOCNet legacy (rtk_inventory historically references ~40 MEX TLALOCNet stations; current realtime count is 15 — the gap reflects offline, decommissioned or de-tagged stations; not addressed here as upstream archive-vs-realtime accounting).

**rtk2go** — 4 MEX-tagged streams (2026-05-22 snapshot): `BASE2_SG_ST1` (Ciudad Madero, Tamaulipas 22.27 N -97.85), `HelgenTestStation` (Querétaro 20.59 N -100.35), `RTK_BASE_IBERO` (Tlazcalancingo, Puebla 19.03 N -98.24), `ZEFE` (Ensenada, Baja California 31.79 N -116.59). All 4 are flagged `nmea=1` in the rtk2go sourcetable; rtk2go is on the pipeline `nmea_filter:false` override (per `data/rtk_map.json`) so they remain visible, but most operators that set `nmea=1` on rtk2go bases are misconfigured single-base stations rather than VRS. A hobbyist client that strictly honours the NTRIP `nmea` flag will refuse to connect without sending GGA; configure the rover to send a one-shot GGA after connect, or pick a base with proper `nmea=0` advertising. Coverage sparse; usable within ~30 km of each base.

**Centipede**: 0 MEX bases.

## Most Recent Project Announcement

No announced project to deploy a free national NTRIP RTK caster as of 2026-05-22. INEGI's 2024 SFTP migration is a maintenance update to the existing RINEX service. Mettatec marketing copy describing INEGI "real-time NTRIP corrections" is not corroborated by INEGI's own pages — keep as marketing, not evidence.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| INEGI RGNA — RINEX via SFTP | `sftp://rgnaftp:rgnaftp@geodesia.inegi.org.mx` | Free |
| INEGI RGNA — info page (EN) | https://en.www.inegi.org.mx/temas/geodesia_activa/ | Free |
| INEGI RGNA — selector + datum reference | https://inegi.org.mx/app/geo2/rgna/ | Free |
| EarthScope — TLALOCNet RINEX archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |

## Sources

- INEGI RGNA English page: https://en.www.inegi.org.mx/temas/geodesia_activa/ (HTTP 200 2026-05-22; meta-keywords list ITRF2008)
- INEGI RGNA RINEX selector: https://inegi.org.mx/app/geo2/rgna/ (post-processing service)
- INEGI CALE2024_itrf2008.pdf — declares datum ITRF2008 / epoch 2010.0: https://www.inegi.org.mx/contenidos/temas/geodesia_activa/doc/CALE2024_itrf2008.pdf
- DTM Topografía Red CORS México: https://dtmtopografia.com/cors-mexico/ (HTTP 200 2026-05-22)
- Aeros Red CORS monthly product page (MXN 2,042): https://aeros.com.mx/product/servicio-red-cors-mensual/ (HTTP 200 2026-05-22)
- La Casa del Topógrafo 12-month CORS México (MXN 20,500): https://www.topografia.com/wptopo/producto/corsmexico-12meses/ (HTTP 200 2026-05-22)
- Survey+ MX CORS México: https://en.surveyplusmx.com/ (parent reachable; canonical `/cors-m%C3%A9xico` slug and legacy `/corsmexico` both HTTP 404 on probe 2026-05-22 — may be temporary or page restructured); coverage info page https://en.surveyplusmx.com/cobertura-e-informacion-cors-mexico still loads
- Punto Visado Hi-Target 1-month licence (MXN 2,368 IVA inc.): https://www.puntovisado.com/producto/licencia-red-cors-1-mes/ (HTTP 200 2026-05-22)
- TopNET Live México (topografiaguadalajara.com): https://topografiaguadalajara.com/estacion-de-referencia-topnet-live-guadalajara/
- ArduSimple Mexico (operator listing): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-mexico/
- EarthScope NOTA realtime: https://www.earthscope.org/data/gnss-realtime/ (datum ITRF2014 / NOTA epoch 2026-03-30)
- EarthScope commercial licensing (USD 1,000/seat/yr): https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- Local pipeline `py scripts/stations_by_country.py MEX` 2026-05-22: 15 EarthScope + 4 rtk2go = 19 stations across 2 sources
