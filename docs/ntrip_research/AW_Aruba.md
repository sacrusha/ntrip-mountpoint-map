# Aruba [AW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-check; 2026-05-15 deep research unchanged)

## Status: NO national NTRIP caster. Free coverage = 1 EarthScope NOTA station (CN19) + 1 rtk2go volunteer base (PINOST1)

## Active free streams

### EarthScope NOTA — CN19_RTCM3P3
| Field | Value |
|---|---|
| **landing_url** | https://www.earthscope.org/data/gnss-realtime/ |
| **access_url** | https://www.earthscope.org/data/gnss-realtime/ (free non-commercial NULA account; commercial = seat-based US$1,000/seat/yr) |
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); legacy `rtgpsout.unavco.org` retired 2025-07-29 |
| **mountpoint** | `CN19_RTCM3P3` (single-base, RTCM 3.3) |
| **tariff** | Non-commercial: free (no VAT, observed 2026-05-15, source: earthscope.org/data/gnss-realtime/). Commercial: US$1,000 / seat / year, no VAT stated. Two-week trial = 5 seats |
| **num_stations** | 1 in Aruba (NW coast near California Lighthouse, 12.61°N -70.05°W) |
| **vrs** | no (single-base RTCM 3.3) |
| **hobbyist_eligibility** | yes — hobbyist/educational/humanitarian use qualifies under NULA |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-17 — `CN19_RTCM3P3` present in `data/stations.json` earthscope snapshot at 12.61°N -70.05°W (per `scripts/stations_by_country.py ABW`); ingested-global, not re-probed directly per research_task.txt rules |
| **datum_epoch** | ITRF2014, epoch 2026-03-30 (NOTA stations) — https://www.earthscope.org/data/gnss-realtime/ |

### rtk2go — PINOST1
| Field | Value |
|---|---|
| **landing_url** | http://rtk2go.com/ |
| **access_url** | http://rtk2go.com/how-to-connect/ (open caster, no registration; email = `none@example.com` convention) |
| **host:port** | `rtk2go.com:2101` |
| **mountpoint** | `PINOST1` (Santa Cruz area, 12.50°N -69.98°W) |
| **tariff** | free; community-funded, donations only |
| **num_stations** | 1 in Aruba |
| **vrs** | no |
| **hobbyist_eligibility** | yes |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-17 — `PINOST1` present in `data/stations.json` rtk2go snapshot at 12.50°N -69.98°W (per `scripts/stations_by_country.py ABW`); ingested-global, not re-probed directly per research_task.txt rules |
| **datum_epoch** | not citable — rtk2go does not declare a global frame; output equals whatever the host base broadcasts |

## Coverage Geometry

Aruba is ~30 km × 9 km. The two free bases — CN19 (NW coast, California Lighthouse) and PINOST1 (centre / Santa Cruz) — are ~16 km apart and together cover the entire island within typical RTK baseline (<20 km). Either base alone gives cm-level positioning over essentially the whole island.

## Context Notes

- **No Aruban national RTK service.** Aruba (ISO 3166-1 AW) is an autonomous constituent country of the Kingdom of the Netherlands but is **not** in Kadaster/NSGI AGRS, which serves only the BES special municipalities (Bonaire, Sint Eustatius, Saba). Aruba, Curaçao, and Sint Maarten have separate constitutional status. See `CW_Dutch_Caribbean.md` and `BQ_Bonaire.md`.
- **DIP (Directie Infrastructuur en Planning, `dip.aw`)** is Aruba's land-registration / planning authority; site content is limited to land-rental applications, subdivision plans, and a ROPV GIS map link. No CORS / NTRIP / RTK content (verified 2026-05-15). The legacy DLV (Dienst Landmeetkunde en Vastgoedregistratie) merged into DIP; `gob.aw` / `gobierno.aw` likewise have no NTRIP content.
- **CN19 / NOTA**: Installed by UNAVCO engineers John Sandru and Mike Fend, 2–9 June 2013, near California Lighthouse on Aruba's NW tip, in cooperation with the Meteorological Department of Aruba. Part of EarthScope's Network of the Americas (NOTA, ex-COCONet).
- **2025 EarthScope platform transition**: Legacy real-time platform `rtgpsout.unavco.org` retired 2025-07-29. New host `ntrip.earthscope.org`, mountpoint format changed `{ID}_RTCM3` → `{ID}_RTCM3P3`, RTCM 3.1 discontinued. Source: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- **PINOST1**: Open rtk2go volunteer base; uptime depends on the host. Check `monitor.use-snip.com` for live status before use.
- **Cross-border alternatives within ~50 km**: None. Nearest free Kadaster AGRS streams (Bonaire) are ~130 km east — well beyond usable RTK baseline. Practical fallbacks if both free streams are down: deploy a local base/rover pair, or use Galileo HAS (~20–40 cm) / a commercial PPP service.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / NOTA** — CN19 RINEX archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |
| **UNAVCO GAGE archive** — historical CN19 dataset | https://www.unavco.org/data/doi/10.7283/T5HD7SZB | Free |

## Sources Consulted (2026-05-15)
- EarthScope GNSS realtime page (host, ports, NOTA datum/epoch, licensing): https://www.earthscope.org/data/gnss-realtime/ — WebFetch OK
- EarthScope platform transition announcement (legacy retired 2025-07-29; mountpoint rename): https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/ — WebFetch OK
- UNAVCO CN19 install report (date, location, partners): https://www.unavco.org/news/unavco-installs-coconet-cgps-site-in-aruba/ — WebFetch OK
- DIP Aruba authority website (no NTRIP/CORS content): https://www.dip.aw/ — WebFetch OK
- Kadaster BES sourcetable (confirms no AW entries; not reachable from this sandbox but referenced by `BQ_Bonaire.md`): http://ntrip.kadaster.nl:2101/sourcetable.htm
- RTK2go connect page: http://rtk2go.com/how-to-connect/
- `data/stations.json` 2026-05-15 — `PINOST1` [ABW] (12.50, -69.98) and `CN19_RTCM3P3` [ABW] (12.61, -70.05) confirmed via `scripts/stations_by_country.py ABW`
- RTK2go SNIP monitor (live host status): http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101 (TLS-cert mismatch from this sandbox; reachable for end users)
