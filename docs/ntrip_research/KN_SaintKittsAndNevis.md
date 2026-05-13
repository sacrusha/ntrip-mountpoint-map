# Saint Kitts and Nevis [KN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06; verified + UWI station names and EarthScope cross-border check added 2026-05-12

## Status: No national caster — UWI SRC scientific CORS (STKN on St. Kitts, BATH on Nevis) present since 2007 but not publicly streamed via NTRIP. EarthScope NOTA stations on neighbouring Montserrat and Antigua provide RTK corrections within ~50 km of southern Nevis.

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS stream in KN territory** | **STKN** (St. Kitts), **BATH** (Nevis) — UWI Seismic Research Centre cGPS stations operating since 2007 for volcano / seismic monitoring. Data are streamed to SRC Trinidad via internet and VSAT for internal scientific use. **No public NTRIP correction stream.** GPS data repository available "by online request" via uwiseismic.com/connect/data-request/. |
| **COCONet / EarthScope NOTA station in KN itself** | None confirmed in KN territory. |
| **Nearest cross-border RTK NTRIP** | **EarthScope NOTA** — `RDON_RTCM3P3` on Redonda (Antigua territory) at 16.93 N / -62.35 E is **~35 km** from southern Nevis (Charlestown) and ~62 km from Basseterre, St. Kitts. Six further EarthScope NOTA RTCM3 mountpoints on Montserrat (CN62, OLVN, AIRS, TRNT, RCHY) and Antigua (BGGY) are within 60–100 km of Nevis. Per project rule (~50 km), `RDON_RTCM3P3` is a viable single-base option for Nevis. Source: stations.json earthscope source, 2026-05-12. |
| **hobbyist_eligibility** | N/A for KN-territory casters. EarthScope NOTA RDON is free for non-commercial use with NULA account; $1 000/seat/yr commercial. |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | UWI SRC geodesy page HTTPS 200 (2026-05-12); EarthScope RDON live in stations.json 2026-05-12 fetch. |

---

## UWI Seismic Research Centre (SRC) CORS

Since 2007 the UWI Seismic Research Centre (SRC), headquartered in Trinidad, has operated a network of Continuously Operating Reference Stations (CORS) across the Eastern Caribbean for volcano and seismic monitoring. Confirmed stations on KN territory: **STKN** (St. Kitts) and **BATH** (Nevis). Wider regional cGPS network: DOMP / DOMR / DOMI (Dominica), CN04 (Saint Lucia), SVGB / SVGK (St. Vincent), GRE0 (Grenada). Data are streamed to SRC in Trinidad via internet and VSAT for internal seismological use. **No public NTRIP endpoint, sourcetable URL, or data-sharing agreement for RTK corrections from these stations has been found.** GPS data repository: archived RINEX available "by online request" through uwiseismic.com/connect/data-request/.

**Note on Soufrière Hills (Montserrat)**: The research note for this entry references "Soufrière Hills cGPS NTRIP status." Soufrière Hills volcano is on **Montserrat** (British Overseas Territory), not on St. Kitts or Nevis. The Montserrat Volcano Observatory (MVO) and UWI SRC jointly monitor it with cGPS, but this is in a different jurisdiction (MS, not KN) and no public NTRIP endpoint for MVO cGPS was found. The EarthScope NOTA RTCM3 mountpoints on Montserrat (CN62, OLVN, AIRS, TRNT, RCHY) are separately discoverable in stations.json under the earthscope source — see "Nearest cross-border RTK NTRIP" row above.

---

## Lands and Surveys Unit

The **Lands and Surveys Unit** of the Government of St. Kitts and Nevis (gov.kn) is responsible for geodetic and cadastral work. The unit's official page (gov.kn/lands-and-surveys-unit/) contains no reference to an NTRIP caster, CORS network, or real-time GPS correction service as of 2026-05-06.

---

## Most Recent Project Announcement

No announcement of a national CORS or NTRIP service for Saint Kitts and Nevis was found in any source. No OECS or CARICOM regional GNSS project specific to KN was identified.

---

## Post-Processing (RINEX) Fallback

No confirmed public RINEX download service for KN-territory stations identified. The UWI SRC archives data internally; public access paths not documented.

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Archive** — check for any KN-adjacent NOTA stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial; $1,000/seat/yr commercial |

## Sources Consulted
- UWI Seismic Research Centre — Geodesy & GPS Network page: https://uwiseismic.com/volcanoes/volcano-monitoring/geodesy-gps-network/ (HTTPS 200 2026-05-12)
- UWI SRC homepage: https://uwiseismic.com/
- UWI SRC data request: https://uwiseismic.com/connect/data-request/
- Government of St. Kitts and Nevis — Lands and Surveys Unit: https://www.gov.kn/lands-and-surveys-unit/
- COCONet site info (UNAVCO/GAGE) — no KN station listed: https://coconet.unavco.org/site-info/site-info.html
- EarthScope NOTA network overview: https://www.earthscope.org/nota/
- NTRIP-list.com North America — no KN entry found
- RTK2go / Centipede sourcetables — no KN stations found
- stations.json earthscope source 2026-05-12: RDON_RTCM3P3 (16.93 N / -62.35 E, ATG) ~35 km from southern Nevis; cluster of 6 further NOTA stations on Montserrat / Antigua within 60–100 km. `scripts/stations_by_radius.py 17.15 -62.58 100` lists all.
