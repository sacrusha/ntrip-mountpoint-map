# EarthScope Network of the Americas [US-NOTA] — NTRIP RTK Caster Research

## Status: YES — operational, free non-commercial, hobbyist-eligible

Single-operator Americas-wide caster. Real-time NTRIP, ~1100 STR, RTCM 3.3 single-base.
Multiple country files cite NOTA as their fallback; this file is the canonical operator-scope entry.

| Field | Value |
|---|---|
| Operator | EarthScope Consortium (formed Jan 2023 from UNAVCO + IRIS merger; NSF GAGE facility awardee since 2013) |
| Network name | Network of the Americas (NOTA). Predecessors federated into NOTA in 2013: PBO (Plate Boundary Observatory, 2003 — US/AK/PR), TLALOCNet (~40 MX stations, MRI-funded), COCONet (~85 Caribbean stations) |
| landing_url | https://www.earthscope.org/nota/ |
| access_url | https://www.earthscope.org/data/gnss-realtime/ — operator real-time service page; routes to user license portal |
| host:port (rover) | `ntrip.earthscope.org:2101` (RTCM 3.3 raw GNSS observations); `:2105` (BINEX raw); `:2108` (onboard GGK/GSOF position solutions) |
| caster software | NTRIP Earthscope Kafka Caster/2.0 |
| platform launch | 2025-04-29 (new platform); legacy `rtgpsout.earthscope.org` retired 2025-07-29; multi-GNSS service officially launched 2024-05-01 |
| tariff | Free non-commercial (NULA, annual auto-renew); commercial USD 1,000/seat/yr (CULA, 5-seat minimum) |
| vrs | No — every mountpoint a single-base physical station; no NRTK product |
| num_stations | ~1,100 STR mountpoints (1097 STR 2026-05-18); ~1,140 GPS-capable stations total per 2025 anniversary article; >1,200 instruments incl. boreholes/seismic/tilt. PBO+COCONet+TLALOCNet federation |
| hobbyist_eligibility | Yes — NULA explicitly permits "academic, research, educational, humanitarian, or other public benefit" use without charge. Hobbyist personal RTK fits non-commercial. Charging *any* fee for derived positions/products triggers CULA |
| legal_residency_required | No — global registration; account at earthscope.org User Access Portal |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK` 1097 STR; NTRIP Earthscope Kafka Caster/2.0 |
| datum_epoch | **ITRF2014 reference frame** declared on operator page (earthscope.org/data/gnss-realtime/). NOTA station epoch: **2026-03-30** (operator-declared for in-NOTA stations; updated periodically). Non-NOTA stations on caster: "best estimates without precise epoch dates" per operator. **Plate-fixed national frames not used; rover must transform to local datum (e.g. NAD83(2011) ep 2010.0, GDA2020 ep 2020.0) before survey use** |

## Geographic coverage

Aleutian Islands → continental US → Caribbean → Mexico → Pacific. >20 countries. Densest in seismically active regions (PBO heritage: western US Cordillera, Alaska, southern California, Pacific NW). Sparse in plate-stable interior (eastern/central US, northern MX). Caribbean coverage via COCONet (former 85 stations); Mexico via TLALOCNet (former 40 stations).

Per-region density pointers (research files):
- AK ~140 NOTA stations (Aleutians + mainland + Arctic) — see `US-AK_Alaska.md`
- W ~600 stations Cordillera (WA/OR/CA/NV/UT/AZ/MT/WY/ID/CO/NM) — see `US-W_West.md`
- SE/MW/NE: sparse single-base, geodetic spacing (~200–400 km between stations); not NRTK-substitute — see respective files
- Caribbean: CN5x-CN6x COCONet legacy stations (Anguilla, Trinidad, Hispaniola, etc.) — see country-specific files

For per-state/per-radius queries from inside the pipeline (primer [ingested-globals]):

```
py scripts/stations_by_country.py US --source earthscope
py scripts/stations_by_country.py MX --source earthscope
py scripts/stations_by_radius.py <lat> <lon> <km>
```

## Pipeline status

Source id `earthscope` in `scripts/fetch_stations.py`. Ingested as in-pipeline single-base global caster. Per primer [ingested-globals], operator-scope details live here; per-country files cross-reference, do not re-detail.

## Licensing — NULA verbatim

`https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf` v2025.5.30, key clauses:

- **§3.a Restriction**: "USER may not reverse engineer, decompile, disassemble, copy, distribute, sell, transfer, or disseminate the Data, Streams, or access to either, to any other party for any profit, fee, or charge."
- **§3.c Permitted publication**: "USER may publish, distribute, share, or disseminate fee-free results and findings derived from the Data or Data Streams for academic, research, educational, humanitarian, or other public benefit or greater good usage."
- **§4.a Term**: "valid for one (1) year from the Effective Date"; auto-renews unless terminated.
- **§4.d Commercialisation trigger**: "Should USER commence collecting fees for any products, value-add, distributions, or dissemination of any Data collected or accessed under this NULA, USER's access to Data shall be terminated and USER shall be required to acquire a commercial account for Data access."

**Hobbyist read**: personal RTK with no fee output = NULA-eligible. Landscaper-for-pay or paid survey work = CULA required (no free-tier carve-out for incidental commercial use).

## Licensing — CULA (commercial)

Per operator news 2024-05-01 commercial launch + 2026-05-18 fetch:
- USD 1,000 per seat per year. "Seat permits one concurrent connection."
- Direct billing requires 5-seat minimum (USD 5,000/yr floor).
- Trial: 5-seat 2-week license, one-per-account. Trial fix bug 2025-06 (was non-functional initially).
- Per-position derived products (RTK Fix coordinates, ag swath data) under CULA can be charged for/redistributed; NULA cannot.
- Contact: `commercial-use@earthscope.org`.

## Stream parameters

| Parameter | Value |
|---|---|
| Format | RTCM 3.3 (port 2101); BINEX (port 2105); GGK/GSOF (port 2108) |
| Rate | 1 Hz raw observations |
| Constellations | Multi-GNSS post-2024-05-01 service launch (GPS, GLO, GAL, BDS, QZS, SBAS depending on station receiver hardware) |
| Mountpoint naming | `{FCID}_RTCM3P3` (4-char station code + format suffix); legacy `{FCID}_RTCM3` retired 2025-07-29 |
| Auth | EarthScope account; HTTP Basic over NTRIP |
| Solution flag | 0 (single-base, true physical antenna) — caster does *not* compute VRS/MAC/iMAX/FKP/NEAR |

## Migration history (2024–2025)

| Date | Event |
|---|---|
| 2024-05-01 | Multi-constellation real-time service official launch |
| 2025-04-29 | New platform (`ntrip.earthscope.org`, Kafka Caster/2.0) live in production |
| 2025-06-01 | Trial license bug fix; users can re-create trials |
| 2025-07-29 | Legacy `rtgpsout.earthscope.org` (UNAVCO platform) retired |

Re-registration required for users who only held legacy credentials. Mountpoint suffix change `_RTCM3` → `_RTCM3P3`. RTCM 3.1 dropped.

## Hosts & partner network

NSF National Geophysical Facility funds the GAGE award; EarthScope Consortium operates. Station hosts (landowners, universities, agencies) receive hosting agreement + occasional travel/site visits. NOTA stations on US federal land overlap several NPS units (see `US-NPS_NationalParkService.md`); NPS network is operationally distinct but geographically and historically intertwined (PBO/UNAVCO collaboration).

ShakeAlert® EEW integration: NOTA GPS stations in CA/OR/WA stream into USGS earthquake early-warning system; civilian RTK use of those stations does not affect EEW path.

## Notes

- Single-base only. Effective baseline ~10–30 km depending on rover hardware; degrades ppm beyond. Not a substitute for state DOT NRTK inside state-network hulls. Where state offers free NRTK (FL/WI/MS/VT/etc.) state network = better RTK; NOTA = fallback or PPK/RINEX source.
- ITRF2014 frame vs NAD83(2011) ep 2010.0 (most US state networks): conversion needs operator-provided station velocities. NOTA stations carry per-station ITRF velocity in IGS-style sitelogs; absolute-to-NAD83 transform ≠ trivial (~10–40 cm offset depending on plate motion since 2010). Survey-grade users in NAD83 jurisdictions should prefer state NRTK over NOTA for plan-grade work.
- Caribbean: NOTA is the *only* free real-time RTK source for most Caribbean islands. Coverage varies by island (Anguilla CN59 strong; some islands no station).
- Some non-NOTA observations (IGS-cooperative stations) also flow through this caster; those carry no operator-declared epoch.
- ~1100 mountpoints is real, no NRTK aliases — primer [stations-vs-mps] mapping is 1:1.

## Unresolved / pointers

- **Per-country sub-coverage**: not catalogued here; use `py scripts/stations_by_country.py <CC> --source earthscope` to enumerate.
- **Hawaii**: handful of NOTA stations Big Island + Maui (volcanic monitoring KOKB, MKEA, MAUI, HILO area). No other free Pacific real-time RTK; see `US-W_West.md`.
- **Mexico**: TLALOCNet legacy 40 stations cover Mexico City + central plateau + Gulf + Pacific coastal seismic zones. Country-level entry: `MX_Mexico.md` (separate research; not in this batch).
- **Borehole/strain/seismic/tilt data**: ~80 boreholes + non-GNSS instruments accessible via earthscope.org/data/ portal, not via this NTRIP caster — separate products, out of project scope (project = RTK NTRIP only).
- **ITRF2020 transition**: declared frame still ITRF2014 on operator page 2026-05-18; NGS NSRS modernisation (NATRF2022/NAPGD2022, vote Feb 2026) does not directly affect NOTA broadcast frame. Monitor `earthscope.org/data/gnss-realtime/` for re-declaration.

## Sources

- Operator real-time data page: https://www.earthscope.org/data/gnss-realtime/
- NOTA overview: https://www.earthscope.org/nota/
- 2024-05-01 platform launch / licensing details: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- 2025-04-29 platform transition: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- NOTA anniversary article (history, PBO/COCONet/TLALOCNet federation 2013): https://www.earthscope.org/news/quite-accomplished-for-a-22-year-old-celebrating-the-network-of-the-americas/
- Commercial fee pilot 2023 announcement: https://www.earthscope.org/news/piloting-fees-for-commercial-use-of-positioning-and-correction-data/
- NULA PDF (v2025.5.30; verbatim §3.a, §3.c, §4.a, §4.d): https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf
- Live sourcetable probe 2026-05-18: `curl --http0.9 -A 'NTRIP/1.0' http://ntrip.earthscope.org:2101/` → SOURCETABLE 200 OK, 1097 STR, server NTRIP Earthscope Kafka Caster/2.0
- Pipeline source id: `earthscope` in `scripts/fetch_stations.py`
- Cross-references: `docs/ntrip_research/US-AK_Alaska.md`, `US-W_West.md`, `US-MW_Midwest.md`, `US-NE_Northeast.md`, `US-SE_Southeast.md`, `US-NPS_NationalParkService.md`, plus Caribbean/MX country files
