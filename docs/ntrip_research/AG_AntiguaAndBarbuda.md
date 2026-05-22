# Antigua and Barbuda [AG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: No national caster — EarthScope NOTA single-base streams on Antigua, Barbuda, and Redonda

| Field | Value |
|---|---|
| National NTRIP RTK caster | No |
| Public scientific caster in AG | EarthScope NOTA — `ntrip.earthscope.org:2101` |
| landing_url | https://www.earthscope.org/data/gnss-realtime/ |
| access_url | https://www.earthscope.org/data/gnss-realtime/ (sign-up flow + license terms on same page) |
| host:port | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX), port 2108 (PPP) |
| num_stations | 3 in AG territory — CN01 (17.05, -61.76, Bethesda, Antigua main), BGGY (17.05, -61.86, Codrington, Barbuda), RDON (16.93, -62.35, Redonda) |
| vrs | No — raw 1 Hz multi-constellation RTCM 3.3 MSM7 single-base |
| tariff — noncommercial | Free (USD $0.00); EarthScope account + annual NULA acceptance required. Observed 2026-05-22. Source: https://www.earthscope.org/data/gnss-realtime/ |
| tariff — commercial | USD $1,000 per seat per year ("Commercial licenses are priced at $1,000 per seat and are valid for one year"); per the 2024-03-07 announcement min 5 seats for direct billing; 5-seat 2-week trial available once per account. US 501(c)(3) nonprofit; no VAT. Observed 2026-05-22. |
| hobbyist_eligibility | Yes — NULA accepts individuals; charging for derived data prohibited |
| legal_residency_required | No |
| last_confirmed_alive | 2026-05-22 — local `data/earthscope.sourcetable` refreshed 2026-05-21 (source_health ok); CN01 line 123, BGGY line 88, RDON line 976 |
| datum_epoch | ITRF2014; NOTA epoch 2026-03-30 — operator-declared at https://www.earthscope.org/data/gnss-realtime/. Cited 2026-05-22. |

## EarthScope NOTA stations in AG territory

| Mountpoint | Lat/Lon | Receiver | Notes |
|---|---|---|---|
| CN01_RTCM3P3 | 17.05, -61.76 | Trimble NetR9 | Bethesda, Antigua main island; original COCONet site; primary single-base for Antigua positioning |
| BGGY_RTCM3P3 | 17.05, -61.86 | Trimble NetR9 | Codrington, Barbuda; current code (legacy COCONet CN00 superseded) |
| RDON_RTCM3P3 | 16.93, -62.35 | Septentrio PolaRx5 | Redonda Island (uninhabited dependency); expansion-phase install; ~60 km SW of CN01 |

Stream format: RTCM 3.3 msgs 1077/1087/1097/1107/1117 (MSM7 GPS+GLO+BDS+GAL+SBAS+QZS) + 1005/1007/1013/1029/1033 metadata, all 1 Hz. Single-base — no VRS / Network-RTK on this caster.

Practical baseline notes:
- CN01 (Bethesda) is the only usable single-base for cm-grade work on Antigua main (<20–30 km).
- BGGY serves Barbuda directly; ~30 km north of CN01, marginal for southern Antigua.
- RDON useful only for Redonda itself; ~56 km from CN01 → too long for reliable L1+L2 ambiguity resolution from the main islands.
- Cross-border alternates: 5 EarthScope NOTA mounts on Montserrat (CN62, TRNT, RCHY, AIRS, OLVN) sit 50–60 km from CN01/RDON.

Legacy platform: `rtgpsout.unavco.org` retired 2025-07-29; all NOTA streams on `ntrip.earthscope.org`.

## Volunteer / commercial overlay (2026-05-22)

Zero AG mountpoints on rtk2go, Centipede, GEODNET, ONOCOY. Trimble VRS Now, Hexagon SmartNet, Topcon TopNET Live not advertised for AG/B. Verified via `py scripts/stations_by_country.py ATG` → only the 3 EarthScope stations; no other tracked source has AG hits.

## National surveying authority

**Lands and Survey Division** (Ministry of Lands, Housing and Agriculture) operates the Landfolio public-access portal at `lands.gov.ag` for cadastral records. Domain unreachable from sandbox 2026-05-22 (consistent with 2026-05-17 ECONNREFUSED). No NTRIP caster announced in any English-language search result targeting the domain. No OECS / CARICOM real-time CORS programme specific to AG identified.

## Datum / epoch (AG-national)

Omitted — no citable AG-government declaration of geodetic datum/epoch located. EPSG lists WGS84 as customary but no governmental publication ties cadastre or surveying regulation to a specific datum realisation + epoch.

## Sources
- EarthScope GNSS realtime: https://www.earthscope.org/data/gnss-realtime/ (WebFetch 2026-05-22 — `ntrip.earthscope.org:2101`, ITRF2014, NOTA epoch 2026-03-30, $1,000/seat/yr commercial)
- EarthScope commercial announcement (2024-03-07): https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ ("Starting on May 1, 2024, we will be allowing access to a dedicated NTRIP caster delivering low-latency RTCM positions and MSM messages")
- EarthScope NOTA: https://www.earthscope.org/nota/
- EarthScope NULA PDF: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf
- UNAVCO/GAGE BGGY station DOI: https://www.unavco.org/data/doi/10.7283/T5PK0D9W
- Antigua Lands and Survey Landfolio (unreachable from sandbox): https://lands.gov.ag/
- Local pipeline 2026-05-22: `data/earthscope.sourcetable` lines 88/123/976; `stations_by_country.py ATG` returns same 3 stations; rtk2go + centipede return zero AG
