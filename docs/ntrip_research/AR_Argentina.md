# Argentina [AR] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status

YES — free national government caster (RAMSAC-NTRIP, IGN). A handful of rtk2go
volunteer bases + IGS-IP / AUSCORS / MIRAI rebroadcasts of select Argentine IGS
stations exist; details for those casters live in their own files. No free or
hobbyist-priced commercial alternative verified.

## RAMSAC-NTRIP — Instituto Geográfico Nacional (IGN)

| Field | Value |
|---|---|
| operator | Instituto Geográfico Nacional (IGN), Argentina |
| landing_url | https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip |
| access_url | https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro |
| access_type | free-signup |
| sourcetable | `ntrip.ign.gob.ar:2101` — `curl --http0.9` 2026-05-23 returns 187 STR rows, 42,838 bytes; matches cached `data/ramsac.sourcetable` (186 STR) |
| coverage | All 23 provinces + CABA. Densest in Buenos Aires, Santa Fe, Córdoba, Mendoza. Patagonia (Chubut, Santa Cruz, Tierra del Fuego) sparse — single-base baselines >100 km common. No published VRS hull. |
| num_stations | 217 stations on IGN status page 2026-05-23 (169 ONLINE + 24 SIN NOVEDAD + 20 OFFLINE + 4 FUERA DE FUNCIONAMIENTO); ~193 effectively online. Live sourcetable advertises 187 STR rows: most stations publish both a `-v3.0` legacy stream and a `-v3.2` MSM stream, so mountpoint count ≠ station count. |
| vrs | no — single-base only; rover picks nearest mountpoint manually |
| tariff | not applicable — operator states "El uso del sistema es libre y gratuito" (2026-05-23 verified). No paid tier above free; same registration also unlocks the RINEX archive. |
| hobbyist_eligibility | yes — registration form collects username/email/profession/receiver; no licence, accreditation, or organisational affiliation gating |
| residency_required | no — registration form exposes a Country dropdown; no residency clause in operator page or ToS; foreign signup structurally allowed |
| datum_epoch | POSGAR 07 (IGS05 realisation via SIRGAS DGF08P01), epoch 2006.632 — adopted by IGN Disposición N° 20/2009 (15 May 2009). Operator page: https://www.ign.gob.ar/NuestrasActividades/Geodesia/Posgar07 |
| stations_source | https://www.ign.gob.ar/NuestrasActividades/Ramsac/EstacionesPermanentes (status table) + sourcetable above |

### Session policy

8-hour max per continuous connection (re-authenticate to extend); up to 3
simultaneous connections per credential (RAMSAC-NTRIP service page, re-quoted
2026-05-23).

### Formats / constellations

Each station typically published as both **RTCM 3.0** and **RTCM 3.2 MSM**
streams (mountpoint suffixes `-v3.0` / `-v3.2`); ten stations also expose legacy
**RTCM 2.3** (`BSEN`, `CFAG`, `EZZA`, `PEBA`, `PIAG`, `PWRO`, `SRLP`, `TUCU`,
`UNRO`, `VCON` — all `-v2.3` suffix) and one **RTCM 3.3** (`AZUL-v3.3`).
Sampled streams carry GPS+GLONASS; MSM variants expand to multi-constellation
where the receiver supports it. Single-frequency receivers reach metre-class
via DGPS legacy streams; cm RTK requires dual-frequency within ~30–50 km
baseline.

### Expansion programme

IGN strategic agreement (announced 2023) targets growth from 154 active sites
to 204. The 217-listing-with-193-effectively-online figure on 2026-05-23
reflects ongoing build-out, including a station hosted in **Asunción
(Paraguay)** donated by Tronix SRL — but the Asunción station is **not present
in the RAMSAC-NTRIP live sourcetable** as of 2026-05-23 (RINEX/contributing
node only). See `PY_Paraguay.md`.

## Commercial / alternative casters (none qualifying)

| Provider | Status in AR | Notes |
|---|---|---|
| **RTKArg** (rtkarg.com) | Operating | Public-internet landing alive; quote-by-contact only (WhatsApp +54 911 24940670, info@rtkarg.com). No published host, tariff, station count, or hobbyist signup path. Disqualified: no transparent pricing or self-service. |
| **Trimble VRS Now** | Not on Trimble's published AR coverage | Trimble's local commercial offer is RTX (PPP/SSR) — out of scope. |
| **Hexagon HxGN SmartNet** | No AR-specific node confirmed on operator portal. |
| **Topcon TopNET Live** | Some LATAM presence; no AR-specific mountpoint disclosure. |

No free or hobbyist-priced commercial-grade VRS service publicly advertised for
Argentina; RAMSAC-NTRIP is the only free national caster.

## Volunteer / international rebroadcasts

`scripts/stations_by_country.py ARG` 2026-05-23 — 5 sources, 204 stations:
ramsac 186, igs_ip 6, auscors 3, mirai 4, rtk2go 5. Overlap is heavy: RIO2,
RGDG, UNSA appear simultaneously on igs_ip / auscors / mirai (same physical
sites, three rebroadcast paths). Local rtk2go AR bases as of probe: CASISA
(Córdoba), MPBSAS001 (Greater Buenos Aires), PGDB-Arrias & PGDB-Luque
(Córdoba), PRNAMEI (Entre Ríos / Santa Fe border). Zero Centipede AR nodes,
zero EarthScope NOTA stations on Argentine soil in current pipeline data. See
`rtk2go.md`, `IGS-IP.md`, `EUREF-IP.md` (n/a here), `EarthScope.md` etc. for
those casters' details.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| RAMSAC RINEX archive (per-station daily / hourly) | https://www.ign.gob.ar/NuestrasActividades/Geodesia/Ramsac | Free (same IGN registration) |

## Sources Consulted (verified 2026-05-23)

- RAMSAC-NTRIP service page: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip — re-quoted operator phrasing ("libre y gratuito"), 8 h session, 3 concurrent, POSGAR 07 requirement
- RAMSAC-NTRIP registration: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro
- IGN station-status page: https://www.ign.gob.ar/NuestrasActividades/Ramsac/EstacionesPermanentes — 217 sites, breakdown 169 ONLINE / 24 SIN NOVEDAD / 20 OFFLINE / 4 FUERA DE FUNCIONAMIENTO, timestamp 2026-05-22
- POSGAR 07 declaration page: https://www.ign.gob.ar/NuestrasActividades/Geodesia/Posgar07
- POSGAR 07 / RAMSAC technical doc: https://ramsac.ign.gob.ar/posgar07_pg_web/documentos/POSGAR_07_RAMSAC.pdf
- SIRGAS bulletin on RAMSAC-NTRIP (2022): https://sirgas.org/fileadmin/docs/Boletines/Bol22/03-ServicioArgentino-RAMSAC-NTRIP.pdf
- IGN "Nueva estación GNSS permanente" (Asunción donation by Tronix SRL): https://www.ign.gob.ar/content/ramsac-nueva-estaci%C3%B3n-gnss-permanente
- RTKArg landing: https://www.rtkarg.com/
- ArduSimple AR caster list: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-argentina/
- Live caster probe `curl --http0.9 http://ntrip.ign.gob.ar:2101/` 2026-05-23 — 187 STR rows, 42,838 bytes, sourcetable headed by RAMSAC NET record
- Pipeline enumeration `scripts/stations_by_country.py ARG` 2026-05-23: 5 sources, 204 stations (ramsac 186, igs_ip 6, mirai 4, rtk2go 5, auscors 3)
