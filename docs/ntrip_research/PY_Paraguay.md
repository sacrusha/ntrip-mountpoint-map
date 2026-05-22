# Paraguay [PY] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status

NO national caster, no commercial caster with hobbyist signup, no SIRGAS-RT
node. Practical options are: (1) free RAMSAC-NTRIP (Argentina) cross-border
along the western / southern Paraguay border — single-base baselines as
short as ~115 km from Asunción, much shorter near the Argentine bank;
(2) free RBMC-IP (Brazil, IBGE) cross-border for eastern PY — `ITAI0`
Foz do Iguaçu sits ~10 km from Ciudad del Este; (3) the three rtk2go
volunteer bases in Alto Paraguay / Alto Paraná; (4) a locally hosted base
station; (5) PPP / Galileo HAS (~40 cm).

| Field | Value |
|---|---|
| Active public PY-operated NTRIP RTK caster | none confirmed |
| host:port | n/a |
| tariff | n/a |
| hobbyist_eligibility | n/a |
| residency_required | n/a |
| datum_epoch | omitted — no operating PY NTRIP service to cite |

## Most Recent Project Announcement

No formal project announcement for a Paraguay national NTRIP / RTK caster
found in any government, development-bank, UN, SIRGAS, or geospatial
trade-press source as of 2026-05-23. The closest signal is an ITAIPU/PTI
agreement with the Dirección del Servicio Geográfico Militar (DISERGEMIL) to
modernise the national geographic-information system — no NTRIP/RTK product
named, no timeline.

## Cross-border practical option — RAMSAC-NTRIP (Argentina, IGN)

Free, free-signup, brand-agnostic. See `AR_Argentina.md` for full caster
details. Geographic adjacency to Paraguay is good along the western and
southern borders:

- `py scripts/stations_by_radius.py -25.28 -57.63 400` (Asunción 400 km, 2026-05-23) finds: 11 RAMSAC mountpoints [ARG], 3 rbmc_ip mountpoints [BRA], 1 rtk2go [PRY]. Nearest:
  - **FOSA-v3.0 / FOSA-v3.2** at (-26.19, -58.17), ~115 km geodesic from Asunción centre (Formosa, AR — directly across the Río Paraguay)
  - **EBY1-v3.0** (-27.50, -56.41) at ~278 km (Encarnación/Posadas area)
  - **CHAC-v3.0 / -v3.2** (-27.42, -58.95) at ~286 km (Resistencia / Chaco, AR)
  - **ITAI-v3.2** (-25.42, -54.59) at ~294 km (Itaipú area, AR side)
- Argentine border cities (Clorinda, Posadas, Resistencia) host RAMSAC stations close enough that Paraguayan users in adjacent border districts (Pilar, Encarnación) can get cm-class single-base RTK if within ~30–50 km of a physical RAMSAC site.
- **For eastern PY (Ciudad del Este, Alto Paraná) Brazilian RBMC-IP is closer than RAMSAC**: Foz do Iguaçu RBMC station `ITAI0` (-25.42, -54.59) sits ~10 km from Ciudad del Este, and `GUAI0` Guaíra (-24.08, -54.26) is ~160 km north. Free with gov.br signup; see `BR_Brazil.md`. `UFPR0/UFPR1` Curitiba (-25.45, -49.23) and `PPTE0/PPTE1` Presidente Prudente (-22.12, -51.41) sit just outside single-base range from PY soil.
- RAMSAC has an Asunción-hosted contributing station donated by Tronix SRL (IGN news page), but as of the 2026-05-23 live sourcetable probe (`ntrip.ign.gob.ar:2101`, 187 STR rows) **no Asunción / Paraguay mountpoint is present** — Asunción appears to be a RINEX/contributing node only, not an NTRIP stream.

## rtk2go volunteer bases in PY

`py scripts/stations_by_country.py PRY` 2026-05-23 — 3 bases, single source:

- `NPPCentralTorre` at (-21.08, -60.32) — Boquerón / Alto Paraguay area
- `NPPPetronaTorre` at (-21.07, -60.21) — same vicinity
- `SenioRTK` at (-25.23, -54.70) — Alto Paraná (Ciudad del Este area)

All volunteer single-base streams, no operator quality guarantees. See
`rtk2go.md` for caster-level details.

## Other operators investigated (excluded)

- **GEOEQUIPOS SRL** (geoequipossrl.com): Bolivian geomatics firm (Calle Pinilla 2588, La Paz, +591 78866188); the "Red CORS" page refers to Bolivia, not Paraguay. Prior research version of this file incorrectly listed it as Paraguayan.
- **Geodesical Paraguay** (geodesicalparaguay.com): equipment retailer/reseller in Limpio, PY; no CORS or NTRIP service operated.
- **DINAC** (Dirección Nacional de Aeronáutica Civil): manages aviation GNSS reference stations; no public NTRIP stream in any registry.
- **SNC** (Servicio Nacional de Catastro, catastro.gov.py): national cadastre under Ministry of Economy and Finance; no CORS/NTRIP service announced (re-checked 2026-05-23).
- **DISERGEMIL / Servicio Geográfico Militar**: cartographic products; no NTRIP/RTK service announced.
- **SIRGAS-RT**: Paraguay has a SIRGAS-CON-affiliated station in Asunción (referenced in SIRGAS bulletins) but is not a SIRGAS-RT caster node. SIRGAS-RT covers AR / BR / UY / VE — does not extend to PY in 2026-05.
- No commercial CORS/RTK network identified for Paraguay in surveying industry directories, ArduSimple country pages, NTRIP-list.com, rtcm-ntrip.org, Centipede sourcetables.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| SIRGAS station data (Asunción + regional) | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |
| IGS / EarthScope GNSS archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| RAMSAC RINEX archive (cross-border AR stations near PY border) | https://www.ign.gob.ar/NuestrasActividades/Geodesia/Ramsac | Free (IGN registration) |

## Sources Consulted

- GEOEQUIPOS SRL website: https://geoequipossrl.com/ (Bolivian address confirmed)
- GEOEQUIPOS SRL "Red CORS": https://geoequipossrl.com/red-cors/ (refers to Bolivia)
- Geodesical Paraguay: https://geodesicalparaguay.com/
- SIRGAS-RT bulletins: https://sirgas.ipgh.org/
- NTRIP-list.com South America (no PY entries)
- rtcm-ntrip.org (no PY entries)
- RTK2go monitor (monitor.use-snip.com) — three PY-tagged volunteer bases visible
- ArduSimple country search — no Paraguay-specific page found
- SNC Paraguay: https://www.catastro.gov.py/ — no CORS/NTRIP service mentioned (2026-05-23)
- DISERGEMIL: https://www.disergemil.mil.py/ — no CORS/NTRIP product (2026-05-23)
- WebSearch in Spanish: "Paraguay CORS NTRIP RTK 2026 estaciones permanentes red nacional" — no operator identified (2026-05-23)
- IGN-AR news on RAMSAC station in Asunción (Tronix SRL donation): https://www.ign.gob.ar/content/ramsac-nueva-estaci%C3%B3n-gnss-permanente
- Live RAMSAC sourcetable probe (`ntrip.ign.gob.ar:2101`, 2026-05-23): 187 STR rows, no Asunción / PY mountpoint
- Local: `py scripts/stations_by_country.py PRY` 2026-05-23 → 3 rtk2go bases; `stations_by_radius.py -25.28 -57.63 400` 2026-05-23 → 11 RAMSAC + 3 RBMC + 1 rtk2go within 400 km of Asunción
