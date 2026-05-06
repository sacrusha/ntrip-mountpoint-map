# Belarus [BY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid national GNSS RTK network (ССТП РБ / Belgeodeziya); contract required; no free or self-service hobbyist tier; NTRIP protocol confirmed; host not published

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid; contract-gated) |
| **Operator** | GP "Belgeodeziya" (State Enterprise Белгеодезия / Государственное предприятие «Белгеодезия») |
| **Service name** | ССТП РБ (Система Спутниковых Технологий Позиционирования Республики Беларусь — Satellite Precision Positioning System of the Republic of Belarus) |
| **host:port** | Not publicly listed — provided to users after contract signing with Belgeodeziya |
| **VRS** | Likely yes — documentation describes network corrections delivered via GNSS Spider software (GeoMax); corrections type not confirmed VRS vs. MAC |
| **Stations** | 98 reference stations nationwide (full territory coverage) |
| **RTCM format** | RTCM 3.x (confirmed in documentation); CMR+ also referenced |
| **tariff** | Paid — "unified tariffs of GP 'Belgeodeziya' agreed with the State Committee on Property of the Republic of Belarus" (Госкомитет по имуществу); no public rate schedule found as of 2026-05-06 |
| **hobbyist_eligibility** | No — institutional/commercial contract required; no individual self-service registration path identified |
| **legal_residency_required** | Unclear — state enterprise contract implies Belarusian legal entity; no confirmed mechanism for foreign individual access; Western sanctions (EU/US, post-2022) create practical barriers |
| **last_confirmed_alive** | geo.by website HTTP 200 on 2026-05-06; ССТП service page confirmed active at geo.by/services/sstp; no public NTRIP endpoint to probe |

## Technical Details (from documentation)

- Protocol: NTRIP via GSM/GPRS mobile internet (documented in geo.by/about/Manual_RTK.pdf and nca.by guidance PDFs)
- Data: GNSS Spider software computes RTK corrections in real time; satellite cutoff angle 5°
- Coordinate systems delivered: ITRS, SK-95, SK-63 (Belarusian state systems)
- Use cases: cadastral surveying, construction, forestry, precision agriculture, GIS
- User avoids needing a second receiver as base station — network corrections replace local base

## Belarus and EUREF

As of March 1, 2020, Belgeodeziya began uploading GNSS data to EUREF Permanent Network (EPN) processing centres, making selected Belarusian reference station RINEX data available to the scientific community via the EPN archive. This is a one-way contribution and does not grant access to real-time NTRIP streams.

## Post-Processing (RINEX) Fallback

- **geo.by RINEX download:** Available via contract; procedure documented at geo.by/about/Manual_RINEX.pdf
- **EUREF EPN archive:** Selected Belarusian stations contributed since 2020; free download via https://www.epncb.oma.be/

## Context Notes

- No free public NTRIP tier exists. Belarus follows a state-enterprise commercial model for RTK correction data.
- No rtk2go or Centipede volunteer bases found for Belarus (BY country code).
- Contact for access: info@belgeodesy.by / +375 17 334 79 49 (geo.by)
- Western sanctions (EU, US, UK — post-Feb 2022 Russia-Ukraine war) impose restrictions on technology services with Belarus; practical feasibility of foreign entities accessing this service is unclear.

## Sources Consulted
- Belgeodeziya official site: https://geo.by/en/ (observed 2026-05-06)
- Belgeodeziya ССТП service: https://geo.by/services/sstp (observed 2026-05-06; host/port not published)
- Geoportal Belarus (connection instructions): https://geoportal.by/katalog/gps_gnss_priemniki_dlja_geodezii/podklyuchenie-k-seti-bazovyh-stanciy-74/ (observed 2026-05-06)
- State Committee on Property (NCA) GNSS user guide: https://nca.by/upload/medialibrary/b65/5vk1ph5lep7lx7ap9fn2lbq9glnn4utf/prilozhenie_2_rukovodstvo_po_ispol_zovaniu_gnss.pdf (PDF binary — not extractable; 2026-05-06)
- RTK user guide on geo.by: https://geo.by/about/Manual_RTK.pdf (PDF binary — confirmed exists, sourced from geo.by; Russian-language; 2026-05-06)
- BELTA news (EPN data sharing 2020): https://eng.belta.by/economics/view/belarus-about-to-start-sharing-gnss-data-with-european-network-128634-2020/ (observed 2026-05-06)
- GPS World (EPN sharing announcement): https://www.gpsworld.com/belarus-to-start-sharing-gnss-data-with-european-network/ (observed 2026-05-06)
