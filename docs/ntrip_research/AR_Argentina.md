# Argentina [AR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: YES — free national government caster (RAMSAC-NTRIP) + small rtk2go fringe

## RAMSAC-NTRIP (IGN)

| Field | Value |
|---|---|
| **landing_url** | https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip |
| **access_url** | https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro |
| **host:port** | `ntrip.ign.gob.ar:2101` |
| **tariff** | Free; no fee for registration, use, or RINEX archive (operator page, observed 2026-05-15). No tier above free. |
| **num_stations** | 186 sites on operator status page 2026-05-15 (138 ONLINE / 29 OFFLINE / 17 SIN NOVEDAD / 2 FUERA DE FUNCIONAMIENTO), of which ~155 producing data (ONLINE + SIN NOVEDAD). Live sourcetable `ntrip.ign.gob.ar:2101` 2026-05-15: 192 STR rows. |
| **vrs** | No — single-base only; user picks nearest mountpoint manually |
| **hobbyist_eligibility** | Yes — registration form requests username/email/profession/receiver; no professional license or organizational affiliation checked |
| **legal_residency_required** | No — registration form has a Country dropdown and no explicit residency clause; foreign signup is structurally allowed but not affirmatively documented in the ToS |
| **last_confirmed_alive** | 2026-05-15 — operator pages return HTTP 200; live curl `ntrip.ign.gob.ar:2101` returned SOURCETABLE 200 OK with 192 STR rows |
| **datum_epoch** | POSGAR 07, ITRF2005 (IGS05) realization, epoch 2006.632 — adopted by IGN Disposición N° 20/2009 (15 May 2009). Source: https://www.ign.gob.ar/NuestrasActividades/Geodesia/Posgar07 |

**Session policy:** 8-hour max per continuous connection (re-authenticate to extend); up to 3 simultaneous connections per credential (operator page, 2026-05-15).

**Formats / constellations:** RTCM 2.3 and RTCM 3.0 streams; GPS+GLONASS on the sampled mountpoint (`25MA-v3.0`). Single-frequency receivers reach metre-class via DGPS streams; cm RTK requires dual-frequency within ~50 km baseline.

## Network Coverage

RAMSAC is operated by Instituto Geográfico Nacional (IGN). Stations span all 23 provinces + CABA; densest in Buenos Aires, Santa Fe, Córdoba, Mendoza. Patagonia (Chubut, Santa Cruz, Tierra del Fuego) remains sparse — baselines >100 km occur. No VRS / network-RTK product is published; corrections are emitted per physical station.

## Commercial Alternatives

| Provider | Status in AR | Notes |
|---|---|---|
| **RTKArg** (rtkarg.com) | Operating; no public sourcetable | Quote-by-contact only (WhatsApp/email). No published host, tariff, or station count. Targets surveying / drone / precision-ag professionals. Hobbyist eligibility unconfirmed. |
| **Trimble VRS Now** | Not listed on Trimble's published coverage map for Argentina (2026-05-15). Trimble RTX (PPP/SSR) is the commercial option Trimble offers locally; not networkRTK NTRIP. |
| **Hexagon HxGN SmartNet** | No Argentina-specific node confirmed on operator portal. |
| **Topcon TopNET Live** | Some LATAM presence; no AR-specific mountpoint disclosure found. |

No free commercial-grade VRS service is publicly advertised for Argentina; RAMSAC-NTRIP is the only free national caster.

## Volunteer / Community Casters

`scripts/stations_by_country.py ARG` (2026-05-15) — 5 AR-tagged rtk2go bases:

| Mountpoint | Lat | Lon | Region |
|---|---|---|---|
| CASISA | -31.45 | -64.35 | Córdoba |
| MPBSAS001 | -34.94 | -58.81 | Greater Buenos Aires |
| PGDB-Arrias | -30.29 | -63.64 | Córdoba |
| PGDB-Luque | -31.65 | -63.34 | Córdoba |
| PRNAMEI | -31.72 | -60.52 | Entre Ríos / Santa Fe border |

Zero AR-tagged Centipede nodes. Zero EarthScope NOTA stations in Argentina (EarthScope tags ARG-relevant only for Caribbean/Central America in this pipeline, 2026-05-15).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **RAMSAC RINEX archive** (per-station daily/hourly files) | https://www.ign.gob.ar/NuestrasActividades/Geodesia/Ramsac | Free (same IGN registration) |

## Sources Consulted (verified 2026-05-15)

- IGN RAMSAC-NTRIP service: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip — reachable (200)
- IGN RAMSAC-NTRIP registration: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro — reachable (200)
- IGN station-status page (186 sites, online/offline breakdown): https://www.ign.gob.ar/nuestrasactividades/ramsac/estacionespermanentes — reachable (200)
- POSGAR 07 official declaration page: https://www.ign.gob.ar/NuestrasActividades/Geodesia/Posgar07 — reachable (200)
- Datum technical doc (RAMSAC adoption of POSGAR 07): https://ramsac.ign.gob.ar/posgar07_pg_web/documentos/POSGAR_07_RAMSAC.pdf
- SIRGAS bulletin on RAMSAC-NTRIP (2022): https://www.sirgas.org/fileadmin/docs/Boletines/Bol22/03-ServicioArgentino-RAMSAC-NTRIP.pdf
- Pino & co. NTRIP Service in Argentina (2011 launch paper): https://www.ign.gob.ar/descargas/geodesia/ServicioNTRIPArgentina2011.pdf
- RTKArg landing page: https://www.rtkarg.com/ — reachable (200); no public technical or pricing detail
- ArduSimple AR caster list: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-argentina/ — reachable (200)
- Pipeline sourcetable fetch (data/stations.json via `scripts/stations_inspect.py ramsac`): 196 mountpoints on 2026-05-15
- Pipeline volunteer-caster enumeration (`scripts/stations_by_country.py ARG`): 5 rtk2go bases on 2026-05-15
