# Saint Kitts and Nevis [KN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: No national caster — UWI SRC cGPS internal only; nearest free RTK is EarthScope NOTA RDON (Redonda, AG territory) at ~36 km from Charlestown (Nevis), ~58 km from Basseterre (St. Kitts)

| Field | Value |
|---|---|
| Active public NTRIP RTK caster in KN territory | No |
| landing_url | n/a (no KN caster); nearest cross-border free stream is EarthScope NOTA — details in `EarthScope.md` |
| access_url | n/a |
| host:port | n/a |
| num_stations | 0 in KN territory |
| vrs | n/a |
| tariff | n/a |
| hobbyist_eligibility | n/a |
| legal_residency_required | n/a |
| last_confirmed_alive | 2026-05-22 — `data/earthscope.sourcetable` (refreshed 2026-05-21, source_health ok) contains no KN-tagged stations; UWI SRC geodesy page reachable, confirms "data repository is available by online request" |
| datum_epoch | omitted — no KN-operator caster; no national datum declaration located |

UWI Seismic Research Centre operates cGPS in the Eastern Caribbean (incl. St. Kitts and Nevis) for volcano/seismic monitoring, streamed to SRC Trinidad via internet/VSAT for internal use only. **No public NTRIP endpoint.** Archive data available "by online request" via uwiseismic.com/connect/data-request/.

## UWI Seismic Research Centre

The UWI Seismic Research Centre (Trinidad) has operated cGPS stations in St. Kitts and Nevis since 2007 as part of an Eastern Caribbean volcano-monitoring network. The SRC geodesy page (uwiseismic.com/volcanoes/volcano-monitoring/geodesy-gps-network/) describes the network without enumerating per-island station IDs publicly; SRC processing uses GAMIT/GLOBK and data are streamed to SRC Trinidad via internet and VSAT for internal seismological use. **No public NTRIP stream, sourcetable URL, or RTK data-sharing agreement.** Prior research material attributes station codes STKN (St. Kitts) and BATH (Nevis) to this network; these are not currently republished on the SRC public page.

The Soufrière Hills volcano network (referenced in older research notes) is on Montserrat, not KN — separate jurisdiction (Montserrat Volcano Observatory + UWI SRC). EarthScope NOTA Montserrat cluster (NWBL, OLVN, CN62, AIRS, TRNT, RCHY) sits 56–69 km from Nevis (see "cross-border alternates" below).

## National surveying authority

**Lands and Surveys Unit**, Government of St. Kitts and Nevis (`gov.kn/lands-and-surveys-unit/`). No NTRIP caster, CORS network, or real-time correction product on its public pages. No OECS / CARICOM regional GNSS project specific to KN identified.

## Cross-border free RTK alternates near KN

Per `py scripts/stations_by_radius.py 17.13 -62.62 100` (Nevis-centric, 2026-05-22) — 15 total hits across earthscope (9) + agrs_nl (4) + igs_ip (2):

| Mountpoint | Territory | ~km from Charlestown |
|---|---|---|
| RDON_RTCM3P3 | Antigua (Redonda) | 36 |
| NWBL_RTCM3P3 | Montserrat | 56 |
| OLVN_RTCM3P3, CN62_RTCM3P3, AIRS_RTCM3P3, TRNT_RTCM3P3, RCHY_RTCM3P3 | Montserrat | 59–69 |
| BGGY_RTCM3P3 | Antigua (Barbuda) | 81 |
| CN01_RTCM3P3 | Antigua main | 92 |

Plus 4 AGRS-NL/IGS stations in Saba/Statia (SEUS/SABY, BES) at 56–86 km. RDON (Antigua's Redonda dependency, 16.93 N / -62.35 W) is ~36 km from Charlestown (Nevis) and ~58 km from Basseterre (St. Kitts) — the only one inside reliable single-base RTK range for Nevis; the Montserrat cluster (six EarthScope mounts including NWBL at 56 km) is at 56–69 km — useful for redundancy with degraded fix probability at those baselines.

Operator details, tariffs, hobbyist eligibility, datum/epoch, and the NULA license workflow for these cross-border EarthScope and AGRS-NL/IGS streams are covered in their dedicated research files (`EarthScope.md`, `AGRS_NL.md`, `IGS_IP.md`).

## Sources
- UWI Seismic Research Centre — Geodesy & GPS Network: https://uwiseismic.com/volcanoes/volcano-monitoring/geodesy-gps-network/ (WebFetch 2026-05-22 — no public NTRIP host; "data repository is available by online request")
- UWI SRC data request: https://uwiseismic.com/connect/data-request/
- Government of St. Kitts and Nevis — Lands and Surveys Unit: https://www.gov.kn/lands-and-surveys-unit/
- EarthScope GNSS realtime: https://www.earthscope.org/data/gnss-realtime/ (ITRF2014, NOTA epoch 2026-03-30; $1,000/seat/yr commercial)
- EarthScope NOTA: https://www.earthscope.org/nota/
- Local pipeline 2026-05-22: `stations_by_country.py KNA` → no stations; `stations_by_radius.py 17.13 -62.62 100` → 15 cross-border hits across earthscope (9) + agrs_nl (4) + igs_ip (2); RDON at 36 km
