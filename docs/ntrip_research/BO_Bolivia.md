# Bolivia [BO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: YES — three subscription-gated NTRIP networks operate (RED-GEO, GEOEQUIPOS Red CORS, IGM MARGEN-ROC). No free public caster, no hobbyist-open tier. No rtk2go / Centipede / GEODNET / onocoy stations in-country.

`py scripts/stations_by_country.py BOL` 2026-05-22 returns only 1 station (`SCRZ00BOL0` via igs_ip, the SIRGAS-CON / IGS reference station at Santa Cruz). No volunteer / hobbyist-open Bolivian feed exists in any of the project's ingested global casters.

## redgeo_bo — RED-GEO CORS NTRIP (GeoBolivia SRL, commercial)

| Field | Value |
|---|---|
| **Operator** | GeoBolivia SRL — commercial; governance via COTOBOL (Colegio de Topógrafos de Bolivia) under Ley 2997 del Topógrafo |
| **landing_url** | https://www.geoboliviasrl.info/redgeo |
| **access_url** | https://www.geoboliviasrl.info/redgeo (CTA "Solicitar Datos" → WhatsApp via wa.link/jap8ap; phone via Facebook "GeoBolivia SRL - Geomática") |
| **host:port** | not publicly disclosed; **port 6060** referenced in operator literature; credentials issued post-subscription |
| **tariff** | not published — direct-contact only (Bolivianos, undisclosed amount and VAT treatment) |
| **num_stations** | **11+ confirmed** as of 2026-05-22. Original 7 listed on `/redgeo` (GEO1 La Paz, GEO2 Cochabamba, GEO3 Oruro, GEO4 Sacaba, GEO5 Tarija, GEO6 Santa Cruz, GEO7 Ivirgarzama) plus 4 Santa Cruz metro expansion stations confirmed on the COTOBOL Santa Cruz blog 2026-04: GEO20 (La Guardia), GEO26 (Warnes), GEO28 (Montero), GEO29 (Cotoca). The 2026-04-21 blog post declares full metropolitan coverage live from 2026-05-15. The main `/redgeo` page has not been updated to list the new stations. |
| **vrs** | ? |
| **hobbyist_eligibility** | no (effective) — governed by COTOBOL under Ley 2997 del Topógrafo (2005-03-14); credentials issued via professional surveyor channels |
| **legal_residency_required** | ? — not stated; surveyor licensing is the practical gate |
| **last_confirmed_alive** | 2026-05-22 — `https://www.geoboliviasrl.info/redgeo` HTTP 200; COTOBOL Santa Cruz blog 2026-04-14/-20/-21 documents GEO28/GEO29 activation and 2026-05-15 metropolitan coverage milestone |
| **datum_epoch** | MARGEN frame tie declared by operator (https://www.geoboliviasrl.info/redgeo states the network is "enlazada a los puntos de Clase 'A' y 'B' de la Red 'MARGEN'"); operator does not declare the epoch separately. Epoch **2010.2** in MARGEN-SIRGAS (IGS05 / ITRF2005) comes from the IGM-coauthored SIRGAS Boletín 15 Echalar/Sánchez (https://www.sirgas.org/fileadmin/docs/Boletines/Bol15/30a_Echalar_Sanchez_Reporte_MARGEN_SIRGAS.pdf). Per primer `[datum-epoch]` ("declared only, not inferred"), the operator-side declaration is the frame tie only; the epoch citation rests on the IGM-authored regional bulletin, not a strict operator portal page. |

## geoequipos_bo — GEOEQUIPOS Red CORS (GEOEQUIPOS SRL, commercial)

| Field | Value |
|---|---|
| **Operator** | GEOEQUIPOS SRL (La Paz) |
| **landing_url** | https://geoequipossrl.com/red-cors/ |
| **access_url** | https://geoequipossrl.com/red-cors/ (CTA "ACCEDER A RED CORS" → portal behind login) |
| **host:port** | not publicly disclosed; credentials issued post-subscription |
| **tariff** | not published; payment via QR-code mobile transfer in Bolivianos, capped at 500 Bs per transaction; verification 10–60 minutes; no annual price posted |
| **num_stations** | not disclosed — landing page counter shows placeholder "0+" |
| **vrs** | ? |
| **hobbyist_eligibility** | ? |
| **legal_residency_required** | ? |
| **last_confirmed_alive** | 2026-05-22 — `https://geoequipossrl.com/red-cors/` HTTP 200; contact: +591 78866188, info@geoequipossrl.com, Calle Pinilla 2588, La Paz |
| **datum_epoch** | omitted — no operator declaration |

## margen_bolivia — MARGEN-ROC NTRIP (IGM Bolivia / CEPAG, institutional)

| Field | Value |
|---|---|
| **Operator** | IGM Bolivia — Instituto Geográfico Militar; CEPAG (Centro de Procesamiento y Análisis de Datos GNSS) |
| **landing_url** | https://www10.igmbolivia.gob.bo/ (IGM); https://cposirgasbol.igmbolivia.gob.bo/ (CPAG data portal). `http://margen-igmbolivia.geo.gob.bo/` (MARGEN site) is sandbox-unreachable (ECONNREFUSED) but referenced from public IGM navigation. |
| **access_url** | https://www10.igmbolivia.gob.bo/?page_id=5088 (CEPAG page; access via formal written request + annual fee; contact insgeomilbol@gmail.com or institutional WhatsApp) |
| **host:port** | not publicly disclosed — released only after request approval |
| **tariff** | "annual payment" stated; amount not published |
| **num_stations** | **10 stations** publicly enumerable via the CPAG SIRGAS-BOL consult portal (2026-05-22): AMDE, BLOV, CAMR, LRIB, RDEO, SCRZ, SJCH, SJMA, TPZA, TRJA. The wider MARGEN-ROC physical inventory is larger: SIRGAS Boletín 20 (Echalar, 2015) explicitly states "MARGEN está conformado por una red GPS de operación continua de 42 estaciones continuas", and the 2010 baseline (SIRGAS Bol. 15) was 8 continuous + 9 semi-continuous + 125 passive vertices. The CPAG public portal exposes a subset (10) for free RINEX consult; the remaining MARGEN-ROC stations either feed only the institutional CEPAG processing chain, are not RINEX-public, or are off-line — IGM Bolivia does not publish a per-station status list. |
| **vrs** | no — single-base RINEX / RTK from named stations |
| **hobbyist_eligibility** | no (effective) — institutional procedure oriented to government, academic, and licensed surveying users |
| **legal_residency_required** | ? — not stated; the formal-request workflow effectively filters non-institutional users |
| **last_confirmed_alive** | 2026-05-22 — `https://www10.igmbolivia.gob.bo/` HTTP 200; `https://cposirgasbol.igmbolivia.gob.bo/consult` returns the 10-station picker |
| **datum_epoch** | MARGEN-SIRGAS, IGS05 / ITRF2005, epoch **2010.2** per IGM-authored SIRGAS Boletín 15 (link above). IGM Bolivia CEPAG page (`?page_id=5088`) does not separately publish a datum/epoch string for the NTRIP broadcast. |

## Most recent project announcement

**2026-04-14 to 2026-05-15** — GeoBolivia SRL + COTOBOL Santa Cruz + BESSEL + SITCO alliance:
- 2026-04-14: COTOBOL blog announces GEO28 (Montero) activation, scheduled for May operation
- 2026-04-20: agreement formalized for GEO29 (Cotoca) installation
- 2026-04-21: COTOBOL blog declares "UN HITO HISTÓRICO: COBERTURA TOTAL EN EL ÁREA METROPOLITANA DE SANTA CRUZ" with full metropolitan signal coverage from 2026-05-15
- Stations: GEO6 (Santa Cruz de la Sierra), GEO20 (La Guardia), GEO26 (Warnes), GEO28 (Montero), GEO29 (Cotoca)

Source: https://cotobolscz.blogspot.com/

## Global commercial / crowdsourced networks

| Network | Bolivia coverage (2026-05-22) |
|---|---|
| rtk2go | 0 |
| Centipede-RTK | 0 |
| GEODNET | 0 |
| onocoy | 0 |
| IGS / EarthScope | 1 station SCRZ (Santa Cruz; SIRGAS-CON / IGS reference) — global archive, no hobbyist-open RTK service |
| PointOne / Swift Skylark | not advertised for Bolivia |

Nearest cross-border free or low-friction alternatives are >500 km from any major Bolivian city (Brazil RBMC, Argentina RAMSAC, Peru REGPMOC, Chile CSN); none within ~50 km of a population centre.

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| IGM Bolivia / CEPAG MARGEN-ROC RINEX (10 stations) | https://cposirgasbol.igmbolivia.gob.bo/consult | Fee + formal request |
| EarthScope / SIRGAS-CON | https://www.earthscope.org/data/gnss-data/ | Free for non-commercial; USD 1,000/seat/yr commercial |
| SIRGAS-CON network (IGS-affiliated) | https://www.sirgas.org/ | Free academic/scientific use |

## Sandbox reachability notes

- `http://margen-igmbolivia.geo.gob.bo/` → ECONNREFUSED from sandbox; other IGM hosts (`www10.igmbolivia.gob.bo`, `cposirgasbol.igmbolivia.gob.bo`) return HTTP 200. Bolivian users reach the missing host normally per IGM nav + academic theses references.
- All three operators' caster hostnames remain undisclosed pre-subscription; no DNS records exist for `ntrip.*` / `caster.*` / `rtk.*` subdomains under any of the three operators (probed 2026-05-15).

## Sources

- GeoBolivia SRL RED-GEO: https://www.geoboliviasrl.info/redgeo
- GeoBolivia SRL GEO 6 station detail: https://www.geoboliviasrl.info/geo6
- COTOBOL Santa Cruz blog (2026-04 expansion posts): https://cotobolscz.blogspot.com/
- GEOEQUIPOS SRL Red CORS: https://geoequipossrl.com/red-cors/
- IGM Bolivia: https://www10.igmbolivia.gob.bo/ and https://www10.igmbolivia.gob.bo/?page_id=5088 (CEPAG)
- IGM CPAG SIRGAS-BOL consult portal: https://cposirgasbol.igmbolivia.gob.bo/consult (10 stations enumerated)
- SIRGAS Boletín 15 (Echalar/Sánchez) — MARGEN datum/epoch citation: https://www.sirgas.org/fileadmin/docs/Boletines/Bol15/30a_Echalar_Sanchez_Reporte_MARGEN_SIRGAS.pdf
- SIRGAS Boletín 20 (Echalar et al., 2015) — "42 estaciones continuas" MARGEN-ROC physical inventory: https://www.sirgas.org/fileadmin/docs/Boletines/Bol20/16_Echalar_Reporte_Bolivia.pdf
- SIRGAS Boletín 21 (Hoyer et al., 2016) — NTRIP network installation, Bolivia. Notes "Las estaciones de la red de observación continua [MARGEN] no transmiten ningún tipo de corrección en Tiempo Real" as of 2016; private-sector and municipal networks filled the gap. URL: https://www.sirgas.org/fileadmin/docs/Boletines/Bol21/39_Hoyer_et_al_2016_RedNtripBolivia.pdf
- IGM YouTube tutorial "Procedimiento para el acceso al servicio NTRIP" (https://www.youtube.com/watch?v=4yuH1W05eII) — video content not extractable via WebFetch (page returns only YouTube footer scaffold); user with browser/JS can view directly, but host:port / credentials shown there were not extractable from this research environment
- ArduSimple Bolivia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bolivia/
- Local data probes 2026-05-22: `py scripts/stations_by_country.py BOL` returns 1 station (`SCRZ00BOL0` via igs_ip)

## Known data gaps

- **Caster host:port for all three networks** — none of the three operators publishes an unauthenticated NTRIP endpoint; only port 6060 (RED-GEO) is referenced in literature
- **Tariff amounts** — none of the three operators publishes pricing publicly
- **VRS / single-base architecture for RED-GEO and GEOEQUIPOS** — operator pages describe RTK / NTRIP corrections without specifying single-base vs network
- **Foreign-resident eligibility** — none of the three operators addresses non-resident access explicitly; in practice the licensed-surveyor or formal-institutional workflow filters most non-Bolivian users
