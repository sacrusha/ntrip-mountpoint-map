# Peru [PE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: YES — official government NTRIP caster (REGPMOC / IGN-Peru) operational; licence + payment required; **public-internet TCP reach unconfirmed from outside Peru**

## regpmoc — REGPMOC (IGN Peru)

| Field | Value |
|---|---|
| **Operator** | Instituto Geográfico Nacional (IGN) del Perú — Ministerio de Defensa, Subdirección de Geodesia |
| **Network name** | REGPMOC — Red Geodésica Peruana de Monitoreo Continuo |
| **landing_url** | http://regpmoc.ign.gob.pe/rastreo_permanente/index.php (REGPMOC station portal) |
| **access_url** | https://www.idep.gob.pe/ (IDEP / IGN geospatial portal; licence + credential request via IGN Subdirección de Geodesia, email idep@ign.gob.pe) |
| **host:port** | `190.12.71.75:2101` — listed for "IGN-Perú / PER / http://ign.gob.pe" in SIRGAS Boletín 17 (IPGH-published SIRGAS-RT inventory of national casters, https://sirgas.ipgh.org/docs/Boletines/Bol17/Noguera_Perez_Reporte_SIRGAS_RT.pdf). The IGN NTRIP licence PDF (Scribd / pdfcoffee mirrors) carries the same IP. Subdomain `regpmoc.ign.gob.pe` resolves to a different IP (209.45.65.186) which also exposes port 2101 per public DNS, but both endpoints fail TCP connect from the research environment. |
| **tariff** | Fee required; amount not published on any public IGN page. Credentials (IP, port, username, password) issued by email after payment and licence approval. Direct-contact only. |
| **num_stations** | 70 registered ERP per IGN document portal (doc IDs 2634 + 2845, late 2024). MQ04 (Mariscal Nieto, Moquegua) most recent confirmed addition with data from 2026-03-17. Cojata + Ananea (Puno) implementation works are referenced from October 2023 IGN news. The IGN H1-2024 Informe de Evaluación Institucional (doc 3134) targets 91.8 % ERP operativity but does not publish an absolute active count; an external (web) summary of that report cites 73 ERP active with connectivity at 92.4 % in H1 2024 — current 2026 active count is not separately published. The IDEP GeoVisor banner names 16 ERP in active maintenance (TU02, PI03, LB03, LL04, AN02, LI07, HC03, PA01, JU03, TC04, TC03, AQ01, AQ03, AY02, IC03, SM01). |
| **vrs** | Yes — operator-declared VRS mountpoints in Lima/Callao: LI02 (Ancón), LI03 (Chaclacayo), LI06 (Callao), Surquillo, LI04 (Pucusana) per IGN NTRIP licence document |
| **hobbyist_eligibility** | ? — licence does not explicitly exclude individuals but requires payment, formal attribution to "Instituto Geográfico Nacional, IGN-NTRIP," and signed acceptance of terms; no documented case of a hobbyist subscription being approved or rejected. |
| **legal_residency_required** | ? — not stated in the public licence document |
| **last_confirmed_alive** | Operationally active per IGN public docs (MQ04 with data from 2026-03-17). Direct TCP probes from research sandbox fail: `190.12.71.75:2101` and `regpmoc.ign.gob.pe:2101` (209.45.65.186) both timed out 15 s on 2026-05-12, 2026-05-17, 2026-05-22. Behaviour consistent with geofencing / authorised-IP filtering matching the licence-gated access model — not evidence the caster is down. |
| **datum_epoch** | omitted — no citable operator declaration of the NTRIP broadcast frame. REGPMOC station coordinates have historically been published via SIRGAS-CON in ITRF realisations but the IGN NTRIP licence document does not explicitly publish a datum/epoch for the broadcast. Per primer `[datum-epoch]` rule, omit. |

## Recent project announcements

- **2026-03-17** — Station MQ04 (Mariscal Nieto, Moquegua) added to REGPMOC, GNSS data available from this date per IDEP GeoVisor (idep.gob.pe/geovisor/ERP/)
- **2023-10** — IGN news (https://www.gob.pe/institucion/ign/noticias/855204) reported implementation of two new ERP stations in Cojata and Ananea (Puno Department), published October 2023. Not a 2026 announcement.
- **Resolución Jefatural 149-2022/IGN/DIG/SDPG** (November 2022) — formally updated the index and detail records for REGPMOC ERP; published in El Peruano

## Network details

- **Protocol:** NTRIP 1.0; up to 100 simultaneous users per station
- **Correction formats:** RTCM 3.1 and CMR+
- **Optimal rover range:** ≤50 km dual-frequency L1/L2; ≤20 km single-frequency L1
- **Latency:** ≤2 seconds (operator claim)
- **Licence terms:** Users must acknowledge IGN as the authoritative source; prohibition on misrepresenting data origin or claiming government endorsement for derived products
- **Geofencing:** Public-internet reach from outside Peru unconfirmed — repeated TCP probes from US-egress sandbox time out; consistent with the licence-gated access model and noted in `docs/rtk_inventory.md` for `regpmoc`
- **SIRGAS-RT:** Peru does not appear as a SIRGAS-RT real-time caster node; IGN operates its own national caster independently. Selected IGN stations participate in IGS.

## Alternative coverage (`py scripts/stations_by_country.py PER` 2026-05-22)

- **rtk2go:** 1 Peruvian volunteer mountpoint — `LIMA1_RTCM3` (−12.03°N, −76.98°W). The earlier `ALMAR` (Tacna) is no longer listed.
- **auscors:** 1 station AREG (Arequipa)
- **igs_ip:** 2 stations AREG + PIUR (Piura)
- **mirai:** 1 station AREG
- **Centipede-RTK / GEODNET:** no Peruvian nodes
- **onocoy:** no Peru-coded nodes confirmed via local data; user can verify via the onocoy explorer (console.onocoy.com/explorer)
- **Swift Skylark / Point One Polaris:** South America (incl. Peru) is not in the published coverage list as of 2026 (Swift FAQ + Point One coverage map)
- ArduSimple's 2026 Peru page still states "as far as we know Peru is not among" countries with national networks — reflects the practical invisibility of REGPMOC's licence-gated service to hobbyists.

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| REGPMOC RINEX archive | https://www.idep.gob.pe/ | Unknown; likely under the same licence as NTRIP |
| SIRGAS station data | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |
| IGS / EarthScope archive (Peru IGS stations) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; USD 1,000/seat/yr commercial |

## Contact

- IGN OEINFO / IDEP — idep@ign.gob.pe; transparency contact: lmaurip@ign.gob.pe
- Main office: Av. Andrés Aramburú 1184, Surquillo, Lima
- Technical support: Mon–Fri 08:00–16:00 (PET, UTC−5)

## Sources

- IGN Peru NTRIP licence PDF (pdfcoffee mirror): https://pdfcoffee.com/download/licencia-gnss-ntrip-ign-peru-pdf-pdf-free.html
- IGN document portal — doc 2634 (REGPMOC technical reference): https://app8.ign.gob.pe/GestionDocumental/Documento.aspx?id=2634
- IGN document portal — doc 2845 (station details): https://app8.ign.gob.pe/GestionDocumental/Documento.aspx?id=2845
- IGN Informe de Evaluación Institucional H1 2024 (doc 3134, REGPMOC operativity targets): https://app8.ign.gob.pe/GestionDocumental/Documento.aspx?id=3134
- El Peruano — Resolución Jefatural 149-2022: https://busquedas.elperuano.pe/normaslegales/actualizan-el-indice-e-informacion-de-los-detalles-de-las-es-resolucion-jefatural-no-149-2022igndigsdpg-2123842-1/
- IDEP GeoVisor ERP: https://www.idep.gob.pe/geovisor/ERP/
- REGPMOC station portal: http://regpmoc.ign.gob.pe/rastreo_permanente/index.php
- IGN news — Cojata + Ananea works (2023-10): https://www.gob.pe/institucion/ign/noticias/855204-el-ign-realiza-trabajos-tecnicos-para-ampliar-la-cobertura-de-la-red-geodesica-peruana-de-monitoreo-continuo-regpmoc
- SIRGAS-RT bulletin 17: https://sirgas.ipgh.org/docs/Boletines/Bol17/Noguera_Perez_Reporte_SIRGAS_RT.pdf
- ArduSimple Peru page: https://www.ardusimple.es/rtk-correction-services-and-ntrip-casters-in-peru/
- IGN institutional page: https://www.gob.pe/ign
- IDEP / IGN geospatial portal: https://www.idep.gob.pe/
- TCP probes of `190.12.71.75:2101` and `regpmoc.ign.gob.pe:2101` — all attempts time out after 15 s on 2026-05-12 / 2026-05-17 / 2026-05-22

## Known data gaps

- **Active-station count** — IGN publishes operativity *percentage* (target 91.8 %, H1 2024 achieved 92.4 % per external citation of doc 3134) but not an absolute live count; the prior "~35 active" wording in earlier inventory was an unsourced inference and has been removed
- **Public-internet reachability** — no confirmation the caster is reachable from outside Peru without an authorised-IP whitelist; sandbox timeouts are consistent with geofencing but do not prove it
- **Tariff amount** — IGN does not publish licence cost on any public page; one Peruvian integrator's reseller indication of ~USD 85/month exists in `docs/rtk_inventory.md` but is not authoritative
- **Foreign-resident eligibility** — licence document does not explicitly include or exclude non-residents
