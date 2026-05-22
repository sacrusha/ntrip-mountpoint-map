# Ecuador [EC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: YES — free public single-base NTRIP RTK service (REGME-IP / IGM Ecuador), live; 27 mountpoints advertised on caster, 30 stations registered in operator listing (1 in maintenance)

## regme_ec — REGME-IP

| Field | Value |
|---|---|
| **Operator** | IGM — Instituto Geográfico Militar del Ecuador (`igm.gob.ec`) |
| **Network name** | REGME-IP — Red GNSS Ecuatoriana de Monitoreo Continuo, protocolo IP |
| **landing_url** | https://www.geoportaligm.gob.ec/ntrip/ |
| **access_url** | https://www.geoportaligm.gob.ec/ntrip/public/register (self-service registration; terms PDF linked from the same portal) |
| **host:port** | `ntrip.igm.gob.ec:2101` — `SOURCETABLE 200 OK` 2026-05-22, Content-Length 5132, **27 STR mountpoints** (SNIP simpleNTRIP_Caster [wPRO] R3.19.00 of:Dec 19 2025) |
| **tariff** | Free — service stated as "totalmente libre y gratuito" (entirely free and open) on the operator portal; no subscription tiers, no usage fees. USD 0.00. |
| **num_stations** | **30** registered stations per the operator's `listado_estaciones` page (29 active, 1 in maintenance — Chone/CNEC). 27 advertised live on the NTRIP sourcetable 2026-05-22 (delta with 30 reflects stations registered but not currently streaming to the caster). |
| **vrs** | No — sourcetable shows only single-station mountpoints (`<Town>-<CODE>-IGM`); no VRS/MAC/FKP rows. Mounts carry `nmea=1` but the primer notes this is unreliable as a VRS indicator (SNIP caster's metadata default); coords are genuine physical antenna positions (verified per-station against city locations). Pipeline needs `nmea_filter: false` on `regme_ec` to surface the station pins. |
| **format** | RTCM 3 (typically 1004, 1006, 1008, 1012, 1013, 1019, 1020, 1033, 1230); multi-GNSS GPS+GLO+GAL+BDS+QZS+SBAS |
| **hobbyist_eligibility** | Yes — open online registration, no surveying licence required; service explicitly extends to "national and international" users |
| **legal_residency_required** | ? — registration is online and includes international users per operator statement; no explicit residency restriction documented |
| **last_confirmed_alive** | 2026-05-22 — `ntrip.igm.gob.ec:2101` returns `SOURCETABLE 200 OK` with 27 STR rows; SNIP build of 2025-12-19 confirms recent maintenance |
| **datum_epoch** | SIRGAS-ECUADOR — ITRF2008 @ 2016.4. Citable basis: IGM Resolución IGM-2016-005-e-1 (September 2016) adopting ITRF2008 epoch 2016.4 as the official Ecuadorian frame, reformed by Resolución 2017-011-IGM-JUR (June 2017). Resolución 2019-037-IGM-JUR (2019-12-20) is a separate later resolution ratifying SIRGAS adoption and the PSAD 56 → SIRGAS transition. RINEX files for REGME stations are published in this frame. Confirmed via SIRGAS-ECUADOR_IGM presentation (https://www.geoportaligm.gob.ec/geodesia/wp-content/uploads/2020/05/SIRGAS-ECUADOR_IGM_EC_2016.pdf, operator-hosted). |

## Station listing (operator-declared 2026-05-22)

Per https://www.geoportaligm.gob.ec/ntrip/public/estaciones/listado_estaciones — 30 total. The portal table publishes both an RTCM2 and an RTCM3 stream identifier per station (e.g. ALEC2 + ALEC3) — but the live caster sourcetable on 2026-05-22 advertises **RTCM 3 only**; the RTCM2 mounts listed on the portal are not currently broadcast. Whether RTCM2 was discontinued or the portal text simply lags the live caster is not stated by IGM.

ALEC (Alausi), ABEC (Ambato), BHEC (Babahoyo), **CNEC (Chone — in maintenance)**, CXEC (Cotopaxi/Latacunga), CUEC (Cuenca), DPEC (Data de Posorja), ECEC (El Carmen), CHEC (El Chaco), EREC (ERSA Riobamba), ESEC (Esmeraldas), EPEC (ESPE/Sangolquí), FOEC (Francisco de Orellana), GQEC (Guayaquil), IKEC (Ikiam), LAEC (Lago Agrio/Nueva Loja), LJEC (Loja), MAEC (Macas), MHEC (Machala), MUEC (Muisne), NJEC (Naranjal), JNEC (Paján), PSEC (Pedernales), PIEC (Pimampiro), INEC (Piñas), POEC (Portoviejo), QVEC (Quevedo), QUI1 (Quito), SEEC (Santa Elena), SIEC (Santa Isabel).

## Network details

- **Architecture:** Single-station / nearest-station model. Hobbyist must select the closest `<Town>-<CODE>-IGM` mountpoint manually. No VRS/CERCANA-style auto-routing mountpoint is published.
- **Main server:** IGM Quito; backup at ESPOCH Riobamba
- **Availability:** 365 days/year; technical support window Mon–Fri 07:30–16:30 (Ecuador time)
- **Single unified domain** `ntrip.igm.gob.ec` introduced February 2024 (per IGM news)
- **NMEA GGA upstream:** Not strictly required by single-base mountpoints; SNIP marks `nmea=1` on STR rows as a metadata default

## Registration

- URL: https://www.geoportaligm.gob.ec/ntrip/public/register
- Online self-registration; account required to receive credentials
- Support: regme.igm@geograficomilitar.gob.ec / procesogeodesia.igm@geograficomilitar.gob.ec / +593 02-3975100 ext 4421

## Alternative coverage (2026-05-22)

`py scripts/stations_by_country.py ECU`:
- **rtk2go** — 3 Ecuador-coded nodes: `EAOP_EC` Ibarra, `GEOE_LS_EC` Quito, `INGLOCIVIL` Cuenca. All RTCM 3.2, blank carrier field → pipeline keeps as carrier 2; nodes appear on the map. Publicly accessible to any hobbyist via shared rtk2go credentials (any-email/none). Likely institutional re-feeds (university / civil-engineering school towers) — coverage is point-like, not regional, but freely usable for rovers within ~10-20 km of Ibarra/Quito/Cuenca.
- **auscors + igs_ip** — 1 station GLPS00ECU0 (Galápagos archive/global only)
- **Centipede / GEODNET / onocoy** — no Ecuador-coded nodes observed

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| IGM REGME RINEX archive (daily) | https://www.geoportaligm.gob.ec/ (account required) | Free |
| SIRGAS-CON / EarthScope Ecuador stations | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; USD 1,000/seat/yr commercial |

## Recent project announcements

- **2024-02** — Single-domain consolidation to `ntrip.igm.gob.ec` (http://www.geograficomilitar.gob.ec/unico-dominio-servicio-ntrip/)
- **Earlier expansion** — IGM news posts document 4-station integration to REGME-IP (Guayas + El Oro provinces) and Puerto Baquerizo Moreno installation (Galápagos), under cooperation with the Galápagos Government Council
- **2026-05-22 sourcetable** — 27 STR mountpoints live; up from 26 on 2026-05-17 (Muisne MUEC newly streaming)

## Sources

- IGM Ecuador NTRIP registration: https://www.geoportaligm.gob.ec/ntrip/public/register
- IGM Ecuador station listing: https://www.geoportaligm.gob.ec/ntrip/public/estaciones/listado_estaciones (30 stations, 29 active + Chone in maintenance, fetched 2026-05-22)
- IGM Ecuador NTRIP monitor: https://geoportaligm-ec.github.io/NTRIP-monitor/
- IGM news — "Único dominio servicio NTRIP": http://www.geograficomilitar.gob.ec/unico-dominio-servicio-ntrip/
- IGM news — "Integración de 4 estaciones al servicio REGME-IP": http://www.geograficomilitar.gob.ec/integracion-de-4-estaciones-al-servicio-regme-ip-protocolo-ntrip/
- IGM SIRGAS-ECUADOR adoption documentation: https://www.geoportaligm.gob.ec/geodesia/wp-content/uploads/2020/05/SIRGAS-ECUADOR_IGM_EC_2016.pdf
- Licencia y políticas de uso PDF: https://www.geoportaligm.gob.ec/ntrip/public/manual/licencia_gnss_ntrip.pdf
- SIRGAS 2022 bulletin: https://sirgas.ipgh.org/docs/Boletines/Bol14/10.cisneros.pdf
- Live sourcetable probe of `ntrip.igm.gob.ec:2101` — 2026-05-22 (27 STR; Content-Length 5132)

## Known data gaps

- **Pipeline vs operator-listed delta:** Operator portal lists 30 stations (29 active); caster sourcetable advertises 27. Delta likely reflects stations registered with metadata but not currently piped into the public NTRIP caster (Pedernales/PSEC, Ikiam/IKEC, Chone/CNEC absent from live 2026-05-22 sourcetable).
