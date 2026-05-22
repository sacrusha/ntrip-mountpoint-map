# Curaçao [CW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-probed; prior: 2026-05-17)

## Status: NO national caster. Free options = 1 EarthScope NOTA station (CN40) + 3 rtk2go volunteer JAJO bases — all clustered within ~8 km of Willemstad.

Kadaster Curaçao (`kadaster.cw`) is a parcel-map viewer; no GNSS / NTRIP section. NSGI (Netherlands) explicitly excludes Curaçao from its mandate — Curaçao is a constituent country, not a Dutch municipality. AGRS.BES does **not** cover Curaçao. Sister files: `BQ_Bonaire.md` (BES free caster), `AW_Aruba.md`, `SX_SintMaarten.md`.

## Active free streams

### EarthScope NOTA — CN40
| Field | Value |
|---|---|
| **landing_url** | https://www.earthscope.org/data/gnss-realtime/ |
| **access_url** | https://www.earthscope.org/data/gnss-realtime/ (free NULA account for non-commercial; commercial seat = US$1,000/seat/yr) |
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3) |
| **mountpoint** | `CN40_RTCM3P3` (single-base, RTCM 3.3) at 12.18°N, –68.96°W (Willemstad) |
| **tariff** | Non-commercial: free under NULA (observed 2026-05-21). Commercial: US$1,000 / seat / year. Trial: 5 seats for 2 weeks. EarthScope is a US-based service; Curaçao does not levy VAT on cross-border digital services delivered from the US, and EarthScope does not state a VAT rate on its pricing page. |
| **num_stations** | 1 |
| **vrs** | no — single-base RTCM 3.3 |
| **hobbyist_eligibility** | yes — hobbyist / educational / humanitarian use qualifies under NULA |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-21 — `CN40_RTCM3P3` present in project EarthScope snapshot at 12.18°N, –68.96°W; EarthScope NTRIP host responds (ingested global, not re-probed directly per primer rule). |
| **datum_epoch** | ITRF2014 @ best-estimate epoch (NOTA stations use the ITRF2014 reference frame per EarthScope realtime page; specific per-station epoch published as "best estimates" — only NOTA-network-wide epoch declaration on the page is 2026-03-30, with note that other stations use best estimates) — https://www.earthscope.org/data/gnss-realtime/ |

### rtk2go volunteer — JAJO cluster
| Field | Value |
|---|---|
| **landing_url** | http://rtk2go.com/ |
| **access_url** | http://rtk2go.com/how-to-connect/ (open caster, no registration; email-as-username convention) |
| **host:port** | `rtk2go.com:2101` |
| **mountpoints** (sourcetable verified 2026-05-22) | `CWM_JAJO_RTK_RTCM3_X` (Willemstad, 12.12, –68.91, RTCM 3.3); `UTE_JAJO_RTK_RTCM3_X` (Willemstad, 12.15, –68.91, RTCM 3.2). Earlier probes (2026-05-21) also saw `MPA_JAJO_RTK_RTCM3_X` at 12.17, –68.98 (RTCM 3.2); not present on re-probe. |
| **tariff** | free (community-funded, donations only); rtk2go operates from the US, no VAT applied / not stated |
| **num_stations** | 2 (sourcetable verified 2026-05-22; an earlier `MPA_JAJO_RTK_RTCM3_X` mountpoint observed 2026-05-21 was absent on re-probe — rtk2go volunteer bases come and go) |
| **vrs** | no |
| **hobbyist_eligibility** | yes |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-21 — `curl --http0.9 http://rtk2go.com:2101/` returned all 3 JAJO STR with country `CUW` |
| **datum_epoch** | omitted — rtk2go does not declare a global frame; each base broadcasts whatever its host receiver was surveyed-in on |

JAJO mountpoint prefix is reasonably inferred to denote Mijnmaatschappij Curaçao (a limestone quarrying subsidiary of the Dutch JAJO group, `miningcompanycuracao.com`, headquartered Newport / Willemstad). Neither `miningcompanycuracao.com` nor `jajo.com/en/companies/mining-company-curacao/` mention CORS / RTK / NTRIP activity — the operator linkage is therefore plausible-but-unverified, drawn solely from the mountpoint naming convention. All free streams (rtk2go + CN40) sit within ~8 km on the south coast around Willemstad. Westpunt (NW tip) and Oostpunt (SE tip) baselines stretch >25–30 km → marginal single-base; deploy a personal F9P/Mosaic-X5 base for those areas.

## Context Notes

- Kadaster Curaçao (`kadaster.cw`) website is parcel registry / maps only; no NTRIP, no GNSS infrastructure section (HTTP 200, content cross-checked).
- Curaçao is **not** in AGRS.BES (Kadaster NL Caribbean caster). NSGI mandate scope: NL mainland + North Sea + BES special municipalities only.
- No commercial NTRIP service (HxGN SmartNet, Trimble VRS Now, Topcon NetG5, Orphéon, GEODNET, ONOCOY) confirmed in Curaçao via 2026-05 searches.
- No SIRGAS-CON, IGS or BKG real-time stations physically in Curaçao beyond CN40.

## Sources Consulted

- EarthScope GNSS realtime portal (host, ports, ITRF2014, NULA + commercial pricing): https://www.earthscope.org/data/gnss-realtime/
- rtk2go sourcetable (curl probe 2026-05-21, 3 CUW STR confirmed): http://rtk2go.com:2101/
- rtk2go connect docs: http://rtk2go.com/how-to-connect/
- rtk2go SNIP live monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Kadaster Curaçao (no GNSS section): https://kadaster.cw/
- Mining Company Curaçao / JAJO (operator of JAJO* bases): https://miningcompanycuracao.com/ + https://www.jajo.com/en/companies/mining-company-curacao/
- NSGI Dutch Caribbean scope FAQ (BES only): https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams
- `py scripts/stations_by_country.py CUW` 2026-05-21 → 4 stations (1 earthscope CN40 + 3 rtk2go JAJO); re-probe of `rtk2go.com:2101/` 2026-05-22 found only 2 active JAJO mountpoints (`CWM_*` + `UTE_*`); MPA_JAJO mountpoint not present at re-probe.

## Gaps

- CN40 datum / epoch: EarthScope page declares network-wide ITRF2014 but station-level epoch is "best estimate" not separately published.
- rtk2go JAJO bases: host receiver type and survey-in method not declared by operator (rtk2go convention).
- No public Curaçao government roadmap for a national CORS network located in 2026 searches.
