# Argentina [AR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (originally 2026-05-06)

## Status: YES — free national government caster (RAMSAC-NTRIP) + commercial alternatives

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **host:port — RAMSAC-NTRIP** | `ntrip.ign.gob.ar:2101` |
| **tariff — RAMSAC-NTRIP** | Free; registration required at ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro |
| **session cap** | 8 hours per connection; re-authentication required |
| **type** | Single-base (not VRS) |
| **hobbyist_eligibility** | Yes — open to any user; no professional licence required |
| **legal_residency_required** | No — foreign users may register; no explicit residency requirement stated |
| **last_confirmed_alive** | ign.gob.ar RAMSAC pages HTTP 200 on 2026-05-06; sourcetable endpoint confirmed in pipeline CI |

## Network Coverage

RAMSAC-NTRIP is operated by the Instituto Geográfico Nacional (IGN) of Argentina. As of 2026-05-12 the network lists approximately 203 stations in the pipeline sourcetable, consistent with the publicly announced modernisation programme that expanded RAMSAC from 154 to ~204 permanent GNSS stations under an IGN strategic agreement (announced 2024–2025). Stations span all 23 provinces plus CABA, with densest coverage in Buenos Aires, Córdoba, Santa Fe, and Mendoza provinces. Coverage is thinner in Patagonia (La Pampa, Chubut, Santa Cruz, Tierra del Fuego) where communications constraints limit real-time streaming; IGN has announced plans to add additional Patagonia-region sites as cellular/satellite connectivity improves. Reference frame: POSGAR 07 (aligned to SIRGAS, ITRF-compatible).

## Commercial Alternatives

| Provider | Host:port | Type | Tariff | Notes |
|---|---|---|---|---|
| **RTKArg** | not published (contact via rtkarg.com) | network RTK | not publicly listed | Commercial caster serving agriculture, surveying, drone ops; details require registration |
| **Trimble RTX** | PPP/SSR via satellite/internet | PPP-RTX (not networkRTK) | subscription; pricing via trimble.com/positioningservices | Sub-decimeter PPP; not NTRIP-RTCM network RTK |
| **HxGN SmartNet+** | regional via Hexagon | VRS | not publicly listed for AR | No confirmed Argentine-specific nodes; enquire via hexagongeosystems.com |
| **TopNET Live** | topconpositioning.com | network RTK | subscription; regional pricing not published | Some South America coverage; AR-specific node count unconfirmed |

No confirmed free VRS / network-RTK service operates in Argentina beyond RAMSAC. All commercial VRS options require vendor-direct contact for pricing and coverage confirmation.

## Provincial CORS Initiatives

Several Argentine provincial institutions (Catastros, universities, professional engineering councils) contributed stations to RAMSAC; these stations feed the national caster rather than operating independent provincial casters. No confirmed independent provincial NTRIP caster (separate from RAMSAC) identified as of 2026-05-06.

## Context Notes

- **RAMSAC origin**: Established 2010 by IGN with contributions from national and provincial institutions, cadastral offices, universities, professional councils, and private companies. Originally ~69 GPS stations; grown to ~203 by 2026.
- **Single-base limitation**: RAMSAC does not offer VRS; users must select the nearest mountpoint manually. Hobbyist use requires re-connection every 8 hours.
- **Volunteer**: 6 AR-coded bases on rtk2go (CASISA, LACU-COR-ARGENTINA, MPBSAS001, PGDB-Arrias, PGDB-Luque, PRNAMEI) — mostly Córdoba province (Cba/Luque/PGDB) plus 1 Buenos Aires metro (MPBSAS001) and 1 Entre Ríos (PRNAMEI). Zero AR-coded Centipede nodes. Confirmed via `scripts/stations_by_country.py ARG` on 2026-05-12.
- **Coverage gap**: Patagonia (south of ~40°S) has sparse RAMSAC coverage; nearest station baselines can exceed 100 km in parts of Chubut and Santa Cruz provinces.
- **Currency note**: Any Argentine commercial pricing would be quoted in ARS (Argentine peso), subject to high inflation; always confirm current rates directly.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **RAMSAC RINEX** (IGN) — full archive per station | https://www.ign.gob.ar/NuestrasActividades/Geodesia/Ramsac | Free (same registration as NTRIP) |
| **EarthScope NOTA** — selected Argentine stations | https://www.earthscope.org/data/gnss-realtime/ | Free non-commercial (NULA) |

## Sources Consulted
- IGN RAMSAC-NTRIP service page: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip
- IGN RAMSAC network map: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Mapa
- IGN RAMSAC registration: https://www.ign.gob.ar/NuestrasActividades/Geodesia/RamsacNtrip/Registro
- ArduSimple RTK correction services Argentina: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-argentina/
- RTKArg commercial caster: https://www.rtkarg.com/
- SIRGAS RAMSAC-NTRIP paper (2010): https://www.ign.gob.ar/descargas/geodesia/ServicioNTRIPArgentina2011.pdf
- SIRGAS bulletin RAMSAC (2022): https://sirgas.ipgh.org/docs/Boletines/Bol22/03-ServicioArgentino-RAMSAC-NTRIP.pdf
- History and future of RAMSAC (2018 paper): https://www.ign.gob.ar/descargas/geodesia/2018_The_history_state_and_future_of_RAMSAC.pdf
- IGN modernisation agreement (154→204 stations expansion): https://www.ign.gob.ar/content/el-ign-firm%C3%B3-un-convenio-estrat%C3%A9gico-para-modernizar-la-red-argentina-de-monitoreo-satelital
- IGN RAMSAC station status: https://www.ign.gob.ar/NuestrasActividades/Ramsac/EstacionesPermanentes
- Pipeline CI sourcetable probe — ~203 AR stations confirmed 2026-05-06
- Local data verification (2026-05-12): `scripts/stations_by_country.py ARG` — 6 rtk2go AR bases enumerated
