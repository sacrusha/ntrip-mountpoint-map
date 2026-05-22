# Haiti [HT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior: 2026-05-12)

## Status

No active public Haitian NTRIP RTK caster. The Centre National de l'Information Géo-Spatiale (CNIGS) site (`cnigs.ht`) does not advertise any NTRIP service; latest news on the operator site dates back to 2018. One EarthScope NOTA station (`JME2`, Jacmel) appears in the EarthScope sourcetable today (single-base raw RTCM 3.3, noncommercial under NULA); this is a scientific stream rather than a Haitian national service.

| Field | Value |
|---|---|
| Active national NTRIP caster | No |
| Scientific GNSS stream in HT territory | Yes — `JME2_RTCM3P3` (Jacmel, 18.24, -72.54) on `ntrip.earthscope.org:2101` |
| landing_url | n/a (no national operator page advertising NTRIP); EarthScope: https://www.earthscope.org/data/gnss-realtime/ |
| access_url | n/a (no national signup); EarthScope: https://data.earthscope.org/ |
| host:port | n/a (no national caster); EarthScope: `ntrip.earthscope.org:2101` |
| num_stations | 0 national; 1 EarthScope NOTA station in HT territory (`JME2`) |
| vrs | n/a national; EarthScope: No (raw single-base RTCM 3.3 MSM7) |
| hobbyist_eligibility | EarthScope: yes (noncommercial NULA, individual account) |
| legal_residency_required | EarthScope: no |
| last_confirmed_alive | 2026-05-21 — `ntrip.earthscope.org:2101` SOURCETABLE 200 OK (curl probe); `JME2_RTCM3P3` present in pipeline snapshot via `py scripts/stations_by_country.py HTI`. CNIGS page reachable (HTTP 200) but contains no NTRIP/CORS reference. |
| datum_epoch | EarthScope NOTA: ITRF2014, epoch 2026-03-30 (per operator FAQ; FAQ does not state whether this date is fixed for the lifetime of the stream or refreshed as NOTA positions are reprocessed). Operator declaration: https://www.earthscope.org/data/gnss-realtime/ ("All raw data streams use the ITRF2014 reference frame. For NOTA stations, the epoch date is 2026-03-30."). |

## Project History

- **2010-2016 earthquake response**: UNAVCO (now EarthScope) installed and maintained continuous GNSS stations in Haiti for tectonic monitoring under the COCONet programme. JME2 (Jacmel, on the police HQ roof) and CN09 (Cap-Haïtien) were both serviced in July 2016 by CNIGS + UNAVCO field teams. JME2 was the closest station to the 2021 Mw 7.2 earthquake. No public NTRIP service was advertised by UNAVCO at the time; only post-processing RINEX. Sources: https://www.unavco.org/highlights/2016/haiti.html ; https://www.unavco.org/news/supporting-the-science-response-to-the-2021-haiti-earthquake/
- **2015 SIRGAS planning**: a 23-station national CORS network with Trimble NetR9 + Pivot + VRS was scoped for end-of-2016 delivery (Sauveur, "Geodetic Infrastructure in Haiti", SIRGAS Boletín 20, https://sirgas.ipgh.org/docs/Boletines/Bol20/11_Sauveur_2015_Geodetic_infrastructure_in_Haiti.pdf). Plan never materialised.
- **2018-09-26**: Spectra Geospatial / Ashtech donation article — CNIGS and partners stated intention to expand from a single Port-au-Prince CORS station to a national NTRIP CORS system. No implementation date, no public update since. https://spectrageospatial.com/haiti-reconstruction-aid-with-ashtech-donation/
- **2026-05-21**: CNIGS website (`cnigs.ht`) reachable but the most recent news items still date to 2018; the UN-SPIDER profile of CNIGS confirms the 2006 founding decree and current mandate but lists no GNSS service.

## Volunteer / Global Coverage

- `py scripts/stations_by_country.py HTI` (2026-05-21): 1 earthscope station (`JME2_RTCM3P3`, 18.24, -72.54). Zero rtk2go, igs_ip, centipede HTI nodes.
- GEODNET / ONOCOY: no Haiti stations visible on public coverage maps.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| EarthScope GNSS Data Archive — `JME2` (Jacmel, live); `CN09` (Cap-Haïtien, active in 2016 UNAVCO maintenance visit, current real-time status not in 2026-05-21 sourcetable snapshot); archival RINEX | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); USD 1,000/seat/yr commercial |

## Sources

- EarthScope GNSS real-time: https://www.earthscope.org/data/gnss-realtime/ (2026-05-21, HTTP 200; ITRF2014 + epoch 2026-03-30 declared in FAQ)
- EarthScope NTRIP sourcetable: `ntrip.earthscope.org:2101` (curl 2026-05-21, SOURCETABLE 200 OK; `JME2_RTCM3P3` HTI station present)
- UNAVCO Haiti station recovery (JME2 Jacmel + CN09 Cap-Haïtien): https://www.unavco.org/highlights/2016/haiti.html
- UNAVCO 2021 Haiti earthquake response: https://www.unavco.org/news/supporting-the-science-response-to-the-2021-haiti-earthquake/
- CNIGS official site: https://cnigs.ht/ (2026-05-21 — no NTRIP/CORS content; latest news 2018)
- UN-SPIDER CNIGS profile: https://www.un-spider.org/centre-national-de-linformation-g%C3%A9o-spatiale-cnigs
- Spectra Geospatial 2018-09-26 donation article: https://spectrageospatial.com/haiti-reconstruction-aid-with-ashtech-donation/
- SIRGAS Boletín 20 (Sauveur 2015 plan): https://sirgas.ipgh.org/docs/Boletines/Bol20/11_Sauveur_2015_Geodetic_infrastructure_in_Haiti.pdf
