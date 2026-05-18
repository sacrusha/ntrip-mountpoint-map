# Bolivia [BO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: YES — three paid, subscription-gated NTRIP RTK networks operate; no free public caster, no hobbyist-open tier

Bolivia has an active commercial + institutional NTRIP ecosystem (RED-GEO, GEOEQUIPOS Red CORS, IGM MARGEN-ROC). None publish caster host:port, mountpoints, or pricing online; all three gate access behind direct contact and (for RED-GEO) professional-surveyor governance under Ley 2997. No free public national caster. No rtk2go / Centipede / GEODNET / ONOCOY / EarthScope-NOTA stations in-country (`scripts/stations_by_country.py BOL` and `stations_by_radius.py -16.50 -68.15 200` both return zero, 2026-05-15).

## Networks

### 1. RED-GEO CORS NTRIP — GeoBolivia SRL (commercial)
| Field | Value |
|---|---|
| **landing_url** | https://www.geoboliviasrl.info/redgeo |
| **access_url** | https://www.geoboliviasrl.info/redgeo (CTA "Solicitar Datos" → WhatsApp wa.link/jap8ap; phone via Facebook "GeoBolivia SRL - Geomática") |
| **host:port** | hostname not publicly disclosed; **port 6060**; credentials issued post-subscription |
| **tariff** | not published — direct-contact only (Bolivianos, undisclosed amount and VAT treatment) |
| **num_stations** | **12+ confirmed** as of 2026-05-15: original 7 (GEO1 La Paz, GEO2 Cochabamba, GEO3 Oruro, GEO4 Sacaba, GEO5 Tarija, GEO6 Santa Cruz, GEO7 Ivirgarzama) **plus** 2026 Santa Cruz metro expansion GEO20, GEO26, GEO28, GEO29 (Cotoca) — alliance signed 2026-04-20 with COTOBOL-SCZ, BESSEL, SITCO; full operational coverage of Santa Cruz metro area announced for 2026-05-15 (source: cotobolscz.blogspot.com) |
| **vrs** | ? |
| **hobbyist_eligibility** | **no (effective)** — governed by COTOBOL under Ley 2997 del Topógrafo (2005-03-14); credentials issued via professional surveyor channels |
| **legal_residency_required** | ? — not stated; surveyor licensing is the practical gate, not residency |
| **last_confirmed_alive** | 2026-05-15 — `https://www.geoboliviasrl.info/redgeo` HTTP 200, footer © 2026 GEOBOLIVIA SRL; partner blog (cotobolscz.blogspot.com) posted 2026-04 and 2026-05 expansion news |
| **datum_epoch** | MARGEN-SIRGAS = SIRGAS continental frame equivalent to IGS05 (ITRF2005), epoch **2010.2** (source: SIRGAS Boletín 15, Echalar/Sánchez — sirgas.org/fileadmin/docs/Boletines/Bol15/30a_Echalar_Sanchez_Reporte_MARGEN_SIRGAS.pdf). Station coordinates tied to Class A/B MARGEN points. |

### 2. GEOEQUIPOS Red CORS — GEOEQUIPOS SRL (commercial)
| Field | Value |
|---|---|
| **landing_url** | https://geoequipossrl.com/red-cors/ |
| **access_url** | https://geoequipossrl.com/red-cors/ (CTA "ACCEDER A RED CORS" → portal behind login) |
| **host:port** | not publicly disclosed; credentials issued post-subscription |
| **tariff** | not published; payment via QR-code mobile transfer in Bolivianos, capped at 500 Bs per transaction; no annual price posted |
| **num_stations** | not disclosed — landing counter shows placeholder "0 +" |
| **vrs** | ? |
| **hobbyist_eligibility** | ? |
| **legal_residency_required** | ? |
| **last_confirmed_alive** | 2026-05-15 — HTTP 200; contact: +591 78866188, info@geoequipossrl.com, Calle Pinilla 2588, La Paz |
| **datum_epoch** | omitted — no operator declaration |

### 3. MARGEN-ROC NTRIP — IGM Bolivia / CEPAG (institutional)
| Field | Value |
|---|---|
| **landing_url** | https://www10.igmbolivia.gob.bo/ (IGM); https://cposirgasbol.igmbolivia.gob.bo/ (CPAG data portal); http://margen-igmbolivia.geo.gob.bo/ (MARGEN site — sandbox-unreachable, presumed internal/IPv4-only) |
| **access_url** | https://www10.igmbolivia.gob.bo/?page_id=5088 (CEPAG page; access via formal written request + annual fee; contact insgeomilbol@gmail.com or institutional WhatsApp) |
| **host:port** | not publicly disclosed — released only after request approval |
| **tariff** | "annual payment" stated; amount not published |
| **num_stations** | **10 stations** confirmed actively serving data via the CPAG SIRGAS-BOL consult portal (2026-05-15): AMDE, BLOV, CAMR, LRIB, RDEO, SCRZ, SJCH, SJMA, TPZA, TRJA. (Marketing text on IGM site refers to a broader "MARGEN-ROC" densification; only these 10 surface in the public RINEX-availability consult tool.) |
| **vrs** | no — single-base RINEX/RTK from named stations |
| **hobbyist_eligibility** | **no (effective)** — institutional procedure; oriented to government, academic, and licensed surveying users |
| **legal_residency_required** | ? — not stated; in practice the formal-request workflow filters non-institutional users |
| **last_confirmed_alive** | 2026-05-15 — `https://www10.igmbolivia.gob.bo/` HTTP 200; `https://cposirgasbol.igmbolivia.gob.bo/consult` returns the 10-station picker. RINEX archive sales active per CEPAG page. |
| **datum_epoch** | MARGEN-SIRGAS, IGS05/ITRF2005, epoch **2010.2** (SIRGAS Boletín 15, link above) |

## Most Recent Project Announcement

**2026-04-20 → 2026-05-15** — GeoBolivia SRL + COTOBOL Santa Cruz + BESSEL + SITCO alliance, installation of CORS GEO29 (Cotoca, Santa Cruz dept.) plus GEO20/GEO26/GEO28; declared "total signal coverage of the Santa Cruz metropolitan area" effective 2026-05-15. Source: cotobolscz.blogspot.com (COTOBOL Santa Cruz departmental blog).

## Global Commercial / Crowdsourced Networks

| Network | Bolivia coverage (2026-05-15) |
|---|---|
| rtk2go | none in `scripts/stations_by_country.py BOL` |
| Centipede-RTK | none |
| GEODNET | none |
| ONOCOY | none |
| EarthScope NOTA | none (NOTA scope is Western Hemisphere but stations are USA/Caribbean-focused; SIRGAS-CON tier covers Bolivia for static RINEX, see below) |
| PointOne / Swift Skylark | not advertised for Bolivia |

Nearest cross-border free/low-friction alternatives are >500 km from any Bolivian city (Brazil RBMC, Argentina RAMSAC, Peru REGGEN, Chile CSN); none within ~50 km of a Bolivian population centre. No cross-border alternative listed.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGM Bolivia / CEPAG** — MARGEN-ROC RINEX (10 stations: AMDE, BLOV, CAMR, LRIB, RDEO, SCRZ, SJCH, SJMA, TPZA, TRJA) | https://cposirgasbol.igmbolivia.gob.bo/consult | Fee + formal request (sale of CRUDO/RINEX per CEPAG terms) |
| **EarthScope GNSS Data Archive / SIRGAS-CON** | https://www.earthscope.org/data/gnss-data/ | Free for noncommercial (account + NULA); commercial seats USD 1,000/yr |
| **SIRGAS-CON network** (IGS-affiliated) | https://www.sirgas.org/ | Free academic/scientific use of contributing Bolivian stations |

## Sandbox Reachability Notes

- `http://margen-igmbolivia.geo.gob.bo/` → ECONNREFUSED from this sandbox (TCP-level refusal, not DNS). Other IGM hosts on www10.igmbolivia.gob.bo / cposirgasbol.igmbolivia.gob.bo return HTTP 200; sandbox egress is inconsistent for `geo.gob.bo` subdomains. Target users on Bolivian residential / mobile networks reach it normally (referenced from public IGM nav and academic theses).
- All caster hostnames remain undisclosed pre-subscription; no DNS records exist for `ntrip.*` / `caster.*` / `rtk.*` subdomains under any of the three operators (probed 2026-05-15).

## Sources Consulted (2026-05-15)

- GeoBolivia SRL: https://www.geoboliviasrl.info/redgeo (HTTP 200; © 2026)
- COTOBOL Santa Cruz blog: https://cotobolscz.blogspot.com/ (2026-04-20 and 2026-05 posts on CORS-GEO29 alliance + Santa Cruz coverage)
- GEOEQUIPOS SRL Red CORS: https://geoequipossrl.com/red-cors/ (HTTP 200)
- IGM Bolivia: https://www10.igmbolivia.gob.bo/ and https://www10.igmbolivia.gob.bo/?page_id=5088 (CEPAG)
- IGM CPAG SIRGAS-BOL consult portal: https://cposirgasbol.igmbolivia.gob.bo/consult (10 active CORS stations enumerated)
- SIRGAS Boletín 15 (Echalar/Sánchez), MARGEN adjustment — datum & epoch citation: https://www.sirgas.org/fileadmin/docs/Boletines/Bol15/30a_Echalar_Sanchez_Reporte_MARGEN_SIRGAS.pdf
- ArduSimple Bolivia page (confirms no national hobbyist-open network): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bolivia/
- Local data probes: `py scripts/stations_by_country.py BOL` (empty), `py scripts/stations_by_radius.py -16.50 -68.15 200` (empty)
