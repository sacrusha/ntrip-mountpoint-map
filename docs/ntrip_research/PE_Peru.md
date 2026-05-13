# Peru [PE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh; prior pass 2026-05-06)

## Status: YES — active government NTRIP caster (REGPMOC / IGN-Peru); license required; **public-internet TCP reach unconfirmed from outside Peru**

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government-operated; license + payment required) |
| **Operator** | Instituto Geográfico Nacional (IGN) del Perú — Ministerio de Defensa |
| **Network name** | REGPMOC (Red Geodésica Peruana de Monitoreo Continuo) |
| **host:port** | `190.12.71.75:2101` (documented in IGN NTRIP license PDF; subdomain `regpmoc.ign.gob.pe` resolves to 209.45.65.186 — note different IP, possibly behind a WAF or only routable inside PE) |
| **tariff** | Fee required; amount not published publicly. Credentials (IP, port, username, password) issued by email after payment and license approval. Contact IGN Subdirección de Geodesia. |
| **hobbyist_eligibility** | Possible in principle — license does not explicitly restrict to professionals; requires payment, attribution to "Instituto Geográfico Nacional, IGN-NTRIP," and formal acceptance of terms. Process is bureaucratic. |
| **legal_residency_required** | Not stated in public license document |
| **last_confirmed_alive** | Operationally active per IGN public docs (REGPMOC station MQ04 added 2026-03-17). Direct TCP probe **failed from research sandbox** on 2026-05-12: `190.12.71.75:2101` → connection timeout (15s); `regpmoc.ign.gob.pe:2101` (209.45.65.186) → connection timeout. Consistent with port being firewalled outside PE or to authorised IPs only. This matches a license-gated access model. |

## Most Recent Project Announcement

**MQ04 (Mariscal Nieto, Moquegua) added March 2026** — IGN Peru added station MQ04 to REGPMOC with GNSS data available from 2026-03-17, as listed in the IDEP GeoVisor (idep.gob.pe/geovisor/ERP/). The network comprised 70 permanent tracking stations total (35 active, 1 in maintenance) as of October 2024 per IGN document portal references (doc IDs 2634 and 2845).

**Resolución Jefatural 149-2022/IGN/DIG/SDPG** (November 2022) — formally updated the index and detail records for all REGPMOC Estaciones de Rastreo Permanente (ERP). Published in El Peruano official gazette.

## Context Notes

- **REGPMOC** is Peru's official continuous GNSS monitoring network, operated by the IGN Subdirección de Geodesia under the Ministry of Defense. Distinct from Argentina's RAMSAC and Ecuador's REGME despite similar regional naming conventions across SIRGAS networks.
- **Caster endpoint**: `190.12.71.75:2101`. The license document states: *"La conexión al servidor Caster Ntrip, es únicamente a través de una dirección IP, Puerto, usuario y contraseña."* NTRIP 1.0 protocol; up to 100 simultaneous users per station.
- **Correction formats**: RTCM 3.1 and CMR+. Optimal rover range: ≤50 km dual-frequency L1/L2; ≤20 km single-frequency L1. Latency: ≤2 seconds theoretical.
- **VRS mountpoints (Lima/Callao area)**: Ancón (LI02), Chaclacayo (LI03), Callao (LI06), Surquillo, Pucusana (LI04).
- **License terms**: Users must acknowledge IGN as the authoritative source; prohibition on misrepresenting data origin or falsely claiming government endorsement for derived products. License is a formal administrative document.
- **Network size**: 70 registered ERP stations across Peru; 35+ active as of late 2024; MQ04 the most recently confirmed addition (March 2026).
- **SIRGAS-RT**: Peru does not appear as a SIRGAS-RT real-time caster node; IGN operates its own national caster independently. Selected IGN stations participate in the global IGS network.
- **ArduSimple assessment** (ardusimple.es, 2026): States Peru has no national RTK network — reflects the limited public visibility of the licensed REGPMOC service, not an actual absence of a caster.
- **Hobbyist alternatives**: rtk2go now hosts 2 Peruvian volunteer mountpoints (confirmed via `scripts/stations_by_country.py PER` 2026-05-12): `ALMAR` (−17.99°N, −70.24°W, Tacna region) and `LIMA1_RTCM3` (−12.03°N, −76.98°W, Lima). Centipede-RTK: no Peru stations; GEODNET: partial coverage; Galileo HAS free PPP-AR (~20 cm) covers the whole country.
- **Contact**: IGN OEINFO / IDEP — idep@ign.gob.pe; transparency contact: lmaurip@ign.gob.pe. Main office: Av. Andrés Aramburú 1184, Surquillo, Lima. Technical support Mon–Fri 08:00–16:00 (Lima, PET = UTC−5).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **REGPMOC RINEX archive** — contact IGN IDEP portal; daily and sub-daily files | https://www.idep.gob.pe/ | Unknown; likely requires same license as NTRIP |
| **SIRGAS station data** — stations shared with the SIRGAS network | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |
| **IGS / EarthScope GNSS archive** — stations also in the IGS network | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; USD 1,000/seat/yr commercial |

## Sources Consulted
- IGN Peru NTRIP license PDF (pdfcoffee.com mirror): https://pdfcoffee.com/download/licencia-gnss-ntrip-ign-peru-pdf-pdf-free.html
- IGN document portal — doc 2634 (REGPMOC technical reference): https://app8.ign.gob.pe/GestionDocumental/Documento.aspx?id=2634
- IGN document portal — doc 2845 (station details): https://app8.ign.gob.pe/GestionDocumental/Documento.aspx?id=2845
- El Peruano — Resolución Jefatural 149-2022: https://busquedas.elperuano.pe/normaslegales/actualizan-el-indice-e-informacion-de-los-detalles-de-las-es-resolucion-jefatural-no-149-2022igndigsdpg-2123842-1/
- IDEP GeoVisor ERP (station MQ04 / Mariscal Nieto, data from 2026-03-17): https://www.idep.gob.pe/geovisor/ERP/
- REGPMOC station portal: http://regpmoc.ign.gob.pe/rastreo_permanente/index.php
- SIRGAS-RT bulletin 17: https://sirgas.ipgh.org/docs/Boletines/Bol17/Noguera_Perez_Reporte_SIRGAS_RT.pdf
- ArduSimple.es Peru page: https://www.ardusimple.es/rtk-correction-services-and-ntrip-casters-in-peru/
- IGN / Plataforma del Estado Peruano: https://www.gob.pe/ign
- IDEP / IGN geospatial portal: https://www.idep.gob.pe/
- curl probe of `190.12.71.75:2101` — Connection timed out after 15 s (2026-05-12). curl probe of `regpmoc.ign.gob.pe:2101` (DNS → 209.45.65.186) — Connection timed out after 15 s (2026-05-12). The caster is either firewalled to authorised IPs only or geofenced to Peru. Earlier WebFetch attempt (2026-05-06) likewise returned ECONNREFUSED. Reachability for unauthenticated users outside PE is NOT confirmed; service status is inferred from IGN's own current documentation (MQ04 added March 2026).
