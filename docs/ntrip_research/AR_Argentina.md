# Argentina [AR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-15)

## Status: YES — free national government caster (RAMSAC-NTRIP) + small rtk2go fringe; select RAMSAC stations also rebroadcast on IGS-IP / AUSCORS / MIRAI (ingested in pipeline as global sources)

## RAMSAC-NTRIP (IGN)

| Field | Value |
|---|---|
| **landing_url** | https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip |
| **access_url** | https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro |
| **host:port** | `ntrip.ign.gob.ar:2101` |
| **tariff** | Free; no fee for registration, use, or RINEX archive. Date observed 2026-05-17. Source: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip (operator page). No tier above free. |
| **num_stations** | 173 sites on operator status page 2026-05-17 (down from 186 on 2026-05-15 — operator page now lists 173 active rows, breakdown not enumerated in the same form; "FUERA DE FUNCIONAMIENTO" still 3). Pipeline `ramsac` source reports 196 mountpoints (each station typically published as both v3.0 and v3.2 streams; see `scripts/stations_by_country.py ARG` 2026-05-17). |
| **vrs** | No — single-base only; user picks nearest mountpoint manually |
| **hobbyist_eligibility** | Yes — registration form requests username/email/profession/receiver; no professional license or organizational affiliation checked |
| **legal_residency_required** | No — registration form has a Country dropdown and no explicit residency clause; foreign signup is structurally allowed but not affirmatively documented in the ToS |
| **last_confirmed_alive** | 2026-05-17 — operator pages return HTTP 200; raw-socket fetch of `ntrip.ign.gob.ar:2101` returned a sourcetable with the RAMSAC NET row and STR rows starting `25MA-v3.0` (timestamp Sun May 17 16:40 WEDT 2026) |
| **datum_epoch** | POSGAR 07, IGS05 realization (densified through SIRGAS solution DGF08P01), epoch 2006.632 — adopted by IGN Disposición N° 20/2009 (15 May 2009), verbatim from operator page. Source: https://www.ign.gob.ar/NuestrasActividades/Geodesia/Posgar07 |

**Session policy:** 8-hour max per continuous connection (re-authenticate to extend); up to 3 simultaneous connections per credential (operator page, re-confirmed 2026-05-17).

**Formats / constellations:** Each station typically published as both **RTCM 3.0** and **RTCM 3.2 MSM** streams (suffixes `-v3.0` / `-v3.2`); a few stations also carry legacy **RTCM 2.3** (e.g. `BSEN-v2.3`, `CFAG-v2.3`) and one isolated **RTCM 3.3** (`AZUL-v3.3`) per live sourcetable 2026-05-17. GPS+GLONASS on the sampled mountpoint (`25MA-v3.0`); MSM streams typically expand to multi-constellation. Single-frequency receivers reach metre-class via DGPS streams; cm RTK requires dual-frequency within ~50 km baseline.

## Network Coverage

RAMSAC is operated by Instituto Geográfico Nacional (IGN). Stations span all 23 provinces + CABA; densest in Buenos Aires, Santa Fe, Córdoba, Mendoza. Patagonia (Chubut, Santa Cruz, Tierra del Fuego) remains sparse — baselines >100 km occur. No VRS / network-RTK product is published; corrections are emitted per physical station.

**Expansion programme:** IGN strategic agreement (announced 2023, ongoing) targets growth from 154 active stations to 204, densifying southern provinces. The 173-active count on the operator status page 2026-05-17 reflects in-progress build-out, not steady-state.

## Commercial Alternatives

| Provider | Status in AR | Notes |
|---|---|---|
| **RTKArg** (rtkarg.com) | Operating; no public sourcetable | Quote-by-contact only (WhatsApp/email). No published host, tariff, or station count. Targets surveying / drone / precision-ag professionals. Hobbyist eligibility unconfirmed. |
| **Trimble VRS Now** | Not listed on Trimble's published coverage map for Argentina (2026-05-15). Trimble RTX (PPP/SSR) is the commercial option Trimble offers locally; not networkRTK NTRIP. |
| **Hexagon HxGN SmartNet** | No Argentina-specific node confirmed on operator portal. |
| **Topcon TopNET Live** | Some LATAM presence; no AR-specific mountpoint disclosure found. |

No free commercial-grade VRS service is publicly advertised for Argentina; RAMSAC-NTRIP is the only free national caster.

## Volunteer / Community / International Rebroadcasts

`scripts/stations_by_country.py ARG` (2026-05-17) — 5 sources, 215 stations total:

| Source | Count | Notes |
|---|---|---|
| `ramsac` | 196 | National caster, per-station mountpoints (v3.0/v3.2 pairs typical) |
| `igs_ip` | 6 | AGGO, CORD, OAFA, RGDG, RIO2, UNSA — IGS reference stations rebroadcast on `products.igs-ip.net:2101` |
| `auscors` | 4 | LPGS, RGDG, RIO2, UNSA — AUSCORS (Geoscience Australia) selectively rebroadcasts a few ARG IGS stations |
| `mirai` | 4 | MGUE, RGDG, RIO2, UNSA — Japanese Trimble Mirai caster, same rebroadcast pattern |
| `rtk2go` | 5 | CASISA (-31.45,-64.35, Córdoba), MPBSAS001 (-34.94,-58.81, Greater Buenos Aires), PGDB-Arrias (-30.29,-63.64, Córdoba), PGDB-Luque (-31.65,-63.34, Córdoba), PRNAMEI (-31.72,-60.52, Entre Ríos / Santa Fe border) |

Note on overlaps: RIO2, RGDG, UNSA appear on all of igs_ip / auscors / mirai (same underlying physical station, three rebroadcast paths). For an Argentine hobbyist the **primary** access is RAMSAC-NTRIP directly; IGS-IP/AUSCORS/MIRAI rebroadcasts are useful only if RAMSAC registration is unavailable.

Zero AR-tagged Centipede nodes. Zero EarthScope NOTA stations in Argentina (EarthScope tags ARG-relevant only for Caribbean/Central America in this pipeline, 2026-05-17).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **RAMSAC RINEX archive** (per-station daily/hourly files) | https://www.ign.gob.ar/NuestrasActividades/Geodesia/Ramsac | Free (same IGN registration) |

## Sources Consulted (verified 2026-05-17)

- IGN RAMSAC-NTRIP service: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip — 200; confirms host `ntrip.ign.gob.ar:2101`, 8 h session cap, 3 concurrent connections, POSGAR 07 requirement
- IGN RAMSAC-NTRIP registration: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro — 200
- IGN station-status page: https://www.ign.gob.ar/nuestrasactividades/ramsac/estacionespermanentes — 200; 173 sites on 2026-05-17
- POSGAR 07 official declaration page: https://www.ign.gob.ar/NuestrasActividades/Geodesia/Posgar07 — 200; IGS05 + SIRGAS DGF08P01, epoch 2006.632, Disp. N° 20/2009
- Datum technical doc (RAMSAC adoption of POSGAR 07): https://ramsac.ign.gob.ar/posgar07_pg_web/documentos/POSGAR_07_RAMSAC.pdf
- SIRGAS bulletin on RAMSAC-NTRIP (2022): https://www.sirgas.org/fileadmin/docs/Boletines/Bol22/03-ServicioArgentino-RAMSAC-NTRIP.pdf — also at https://sirgas.ipgh.org/docs/Boletines/Bol22/03-ServicioArgentino-RAMSAC-NTRIP.pdf (returned as binary in sandbox)
- Pino & co. NTRIP Service in Argentina (2011 launch paper): https://www.ign.gob.ar/descargas/geodesia/ServicioNTRIPArgentina2011.pdf
- RTKArg landing page: https://www.rtkarg.com/ — 200; quote-by-contact only (WhatsApp +54911-24940670, info@rtkarg.com)
- ArduSimple AR caster list: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-argentina/ — 200; lists only RAMSAC as AR-specific
- Live caster probe: `curl --http0.9 ntrip.ign.gob.ar:2101` 2026-05-17 — sourcetable with RAMSAC NET row + STR rows
- Pipeline enumeration (`scripts/stations_by_country.py ARG`, 2026-05-17): 5 sources, 215 stations (ramsac 196, igs_ip 6, auscors 4, mirai 4, rtk2go 5)
