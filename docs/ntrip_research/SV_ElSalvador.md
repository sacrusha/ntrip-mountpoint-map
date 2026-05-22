# El Salvador [SV] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (Survey3G page HTTP 200, 2026 tariff schedule reconfirmed: $15/7d $30/15d $45/30d $135/3mo $450/12mo; SSIA station also rebroadcast on BKG IGS-IP with RTCM 3.3 MSM7 — wider format support than EarthScope direct)

## Status: YES — one private commercial NTRIP caster (Survey3G); no government NTRIP. One free scientific station (SSIA, San Salvador) accessible via either EarthScope NULA seat or BKG IGS-IP free registration.

## Service A — Survey3G (private commercial)

| Field | Value |
|---|---|
| Operator | Survey GC SA. de C.V. (trading as **Survey3G**), San Miguel, El Salvador |
| Network | NTRIP SURVEY — El Salvador |
| landing_url | https://survey3g.com/ (homepage with company info) |
| access_url | https://survey3g.com/servicios-de-ntrip/ (tariff schedule + product page; subscription requires email/WhatsApp follow-up — survey3g@hotmail.com / +503 7031-5173) |
| Service policies | https://survey3g.com/politicas-de-servicios-ntrip/ (activation lead times, coverage notes) |
| host:port | Not published — IP/port/credentials disclosed by email after subscription payment |
| num_stations | 6 CORS — SAN MIGUEL, PERKÍN, LA UNIÓN, SAN SALVADOR (UES — research/education, labelled temporary), SANTA ANA, COJUTEPEQUE (per `politicas-de-servicios-ntrip/`, confirmed 2026-05-22). Each station ~50 km coverage radius. Operator-claimed ~90% national territory |
| vrs | ? — operator copy uses "RTCM corrections from reference stations" without VRS/NRTK product language. Users manually select the nearest mountpoint (operator policy). Treat as single-base until operator declares otherwise |
| Constellations | GPS + GLONASS + BeiDou + Galileo L1/L2/L5 at SAN MIGUEL/PERKÍN/LA UNIÓN/SAN SALVADOR. SANTA ANA/UES equivalent multi-constellation support per operator page |
| tariff (2026, USD) | USD 15/7d · USD 30/15d · USD 45/30d (monthly) · USD 135/3mo · USD 450/12mo (page label explicitly "2026"; observed 2026-05-22). El Salvador uses USD; no IVA line-itemed on published schedule. Tariffs are re-published every 6 months per operator |
| Activation lead time | New subscriber: 48 h advance notice for config/testing. Existing subscriber: 32 h. Renewal: ≥3 days before expiry |
| hobbyist_eligibility | Yes — subscription open to individuals; no surveyor licence or professional registration required |
| legal_residency_required | No explicit residency gate; service targets El Salvador-based users but allows online sign-up |
| last_confirmed_alive | 2026-05-22 — `survey3g.com/servicios-de-ntrip/` HTTP 200, 2026 price schedule re-read inline ($15/$30/$45/$135/$450). No public host:port to TCP-probe |
| datum_epoch | omitted — no citable declaration. Survey3G NTRIP page describes RTCM corrections + national CORS but does not state frame/epoch. El Salvador uses a SIRGAS-tied national frame in cadastral practice but no operator-side declaration found |

## Service B — SSIA scientific stream (free, NULA OR BKG account)

The IGS station `SSIA` (13.70°N, -89.12°W) sits on the SNET (Servicio Nacional de Estudios Territoriales) campus in San Salvador. It is rebroadcast on two free real-time casters with different format ceilings:

| Path | Caster | Mountpoint | Format | Notes |
|---|---|---|---|---|
| EarthScope NOTA direct | `ntrip.earthscope.org:2101` | `SSIA_RTCM3P3` | RTCM 3 single-base | Requires EarthScope account + NULA seat |
| BKG IGS-IP rebroadcast | `www.igs-ip.net:2101` | `SSIA00SLV0` | RTCM 3.3 + MSM7 (1077/1087/1097/1127), Galileo NAV msgs 1045/1046, GPS+GLO+GAL+BDS | Source field references back to `rtgpsout.earthscope.org:2101/SSIA_RTCM3`; auth Basic, free BKG account registration |

| Field | Value (BKG IGS-IP rebroadcast) | Value (EarthScope direct) |
|---|---|---|
| landing_url | https://igs.bkg.bund.de/ntrip/ | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://igs.bkg.bund.de/ntrip/register | https://data.earthscope.org/ |
| tariff | Free (BKG account, no charge) | Free non-commercial via NULA; USD 1,000/seat/yr commercial (5-seat min, 2-week 5-seat trial) |
| hobbyist_eligibility | Yes | Yes (non-commercial use) |
| legal_residency_required | No | No |
| num_stations (SLV-tagged) | 1 (SSIA) | 1 (SSIA) |
| vrs | No (single-base) | No |
| datum_epoch | omitted — BKG IGS-IP does not publish per-mountpoint datum (primer rule: do not infer ITRF from caster identity) | ITRF2014, NOTA epoch 2026-03-30 (declared at https://www.earthscope.org/data/gnss-realtime/). **Note: SSIA is an IGS site, not a NOTA station** — the NOTA epoch declaration nominally applies only to NOTA stations; SSIA's epoch is not separately declared on the EarthScope realtime page |
| last_confirmed_alive | 2026-05-22 — IGS-IP sourcetable curl returns the STR row for `SSIA00SLV0` (RTCM 3.3, MSM7, source `rtgpsout.earthscope.org:2101/SSIA_RTCM3`) | EarthScope realtime page HTTP 200; SSIA appears in `igs_ip` pipeline data with country tag SLV |

A second EarthScope station, CN21, sits ~194 km east of San Salvador on the Honduras side — too far for single-base RTK but usable for PPK/post-processing in eastern El Salvador.

## Volunteer & open coverage

- rtk2go: 0 SV-coded bases 2026-05-22
- Centipede: 0 SV nodes 2026-05-22
- GEODNET / ONOCOY / HxGN SmartNet / Topcon TopNET Live / Trimble VRS Now: no SV coverage on public-facing product pages
- Local pipeline `py scripts/stations_by_country.py SLV` 2026-05-22: 1 station (SSIA00SLV0) on igs_ip; EarthScope's `SSIA_RTCM3P3` not tagged SLV in this snapshot (pipeline source attribution lives on IGS-IP record)

## Most Recent Project Announcement

No formal government announcement. Survey3G describes itself as "el primer proveedor de NTRIP en El Salvador," operating continuously since launch. 2026 tariff schedule is the most recent dated artifact; March-2026 coverage imagery for LA UNION / SAN SALVADOR / PERKIN stations still posted to `servicios-de-ntrip`. Legacy `survey3g.com/ntrip/` slug remains 404.

**Government context**: Centro Nacional de Registros (CNR) manages geodetic infrastructure for El Salvador but does not publish an NTRIP stream. El Salvador appears in historical SIRGAS-RT cooperation documents for Central America but no active SIRGAS-RT caster node for El Salvador is in public registries.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| EarthScope NOTA SSIA + CN21 RINEX | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA); USD 1,000/seat/yr commercial |
| SIRGAS station data | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |
| NOAA NGS CORS | https://geodesy.noaa.gov/CORS/ | Free |

## Sources

- Survey3G services page (2026 tariff schedule): https://survey3g.com/servicios-de-ntrip/ (HTTP 200 2026-05-22, prices reconfirmed)
- Survey3G homepage: https://survey3g.com/
- Survey3G NTRIP policy (6 stations enumerated): https://survey3g.com/politicas-de-servicios-ntrip/
- EarthScope NOTA realtime: https://www.earthscope.org/data/gnss-realtime/ (datum/epoch declaration)
- EarthScope NULA + commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- IGS station SSIA metadata: https://network.igs.org/SSIA00SLV
- BKG IGS-IP sourcetable (curl probe 2026-05-22): `www.igs-ip.net:2101` — STR `SSIA00SLV0` RTCM 3.3 MSM7 confirmed
- BKG NTRIP service: https://igs.bkg.bund.de/ntrip/
- BKG NTRIP registration: https://igs.bkg.bund.de/ntrip/register
- Local pipeline `py scripts/stations_by_country.py SLV` 2026-05-22: 1 station on igs_ip (SSIA00SLV0)
