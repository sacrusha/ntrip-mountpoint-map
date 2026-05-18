# Antigua and Barbuda [AG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-15)

## Status: No national NTRIP caster — EarthScope NOTA single-base streams active on Antigua, Barbuda, and Redonda

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS streams in AG territory** | Yes — EarthScope NOTA: **CN01** (Bethesda, Antigua main island; 17.05, -61.76), **BGGY** (Codrington, Barbuda; 17.05, -61.86), **RDON** (Redonda Island; 16.93, -62.35). All RTCM 3.3, GPS+GLO+BDS+GAL+SBAS+QZS, single-base raw, on `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | Yes — non-commercial NULA accepts individual accounts; no surveying licence required |
| **legal_residency_required** | No — NULA imposes no nationality/residency restriction |
| **last_confirmed_alive** | 2026-05-17: local `data/earthscope.sourcetable` (refreshed today by scripts/fetch_stations.py) lists all 3 ATG mountpoints. Source health: ok. EarthScope landing page reachable from sandbox; NULA PDF returned but text content was non-extractable (binary stream). |

---

## EarthScope NOTA — Caribbean single-base stations in AG territory

| Mountpoint | Sourcetable lat/lon | Receiver | Notes |
|---|---|---|---|
| **CN01_RTCM3P3** | 17.05, -61.76 (Bethesda, Antigua main island) | Trimble NetR9 | Original COCONet site; primary single-base for Antigua main island |
| **BGGY_RTCM3P3** | 17.05, -61.86 (Codrington, Barbuda) | Trimble NetR9 | UNAVCO/GAGE DOI 10.7283/T5PK0D9W records site coords 17.0451, -61.8612, "still collecting data" through 2026-05-14. Legacy COCONet code CN00 superseded by BGGY. |
| **RDON_RTCM3P3** | 16.93, -62.35 (Redonda Island, uninhabited AG dependency) | Septentrio PolaRx5 | COCONet expansion-phase install; ~60 km SW of CN01 |

Mountpoint format: 4-char station code + `_RTCM3P3` suffix. Stream: raw 1 Hz multi-constellation RTCM 3.3 MSM7 (msgs 1077/1087/1097/1107/1117), plus 1005/1007 station coords and 1013/1029/1033 metadata. **Single-base** — NOT VRS / network-RTK.

| Field | Value |
|---|---|
| **landing_url** | https://www.earthscope.org/data/gnss-realtime/ |
| **access_url** | https://www.earthscope.org/data/gnss-realtime/ (sign-up flow + license terms on same page) |
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); also port 2105 (BINEX), port 2108 (onboard PPP, GGK/GSOF) |
| **num_stations** | 3 in AG territory (CN01, BGGY, RDON), all physical CORS; verified 2026-05-17 against `data/earthscope.sourcetable` |
| **vrs** | No (single-base raw streams) |
| **hobbyist_eligibility** | Yes — non-commercial NULA accepts individuals for scientific, educational, or humanitarian use; charging for derived data prohibited |
| **legal_residency_required** | No |
| **tariff — non-commercial** | Free (USD $0.00); annual NULA acceptance required. Date observed: 2026-05-17. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **tariff — commercial** | USD $1,000 per seat per year (one seat = one concurrent connection); 5-seat minimum for direct billing; 2-week 5-seat trial available once per account. EarthScope is a US 501(c)(3) nonprofit; no VAT. Date observed: 2026-05-17. Source: https://www.earthscope.org/data/gnss-realtime/ and https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ (announcement dated 2024-03-07; service live since 2024-05-01). |
| **NULA reference** | https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf (PDF served; text content not machine-extractable from this sandbox — version date not confirmed in this run) |
| **last_confirmed_alive** | 2026-05-17 — local sourcetable refresh succeeded for all 3 ATG mountpoints |

**Practical positioning notes**
- CN01 (Bethesda, Antigua) is the only usable single-base for cm-grade work on Antigua's main island (baselines <20–30 km).
- BGGY (Codrington, Barbuda) serves Barbuda directly; ~30 km north of CN01, marginal for southern Antigua.
- RDON (Redonda) is useful only for work on Redonda itself (~56 km SW of CN01, too long for reliable L1+L2 ambiguity resolution from the main islands).
- Cross-border fallback: 5 EarthScope stations on Montserrat (CN62, TRNT, RCHY, AIRS, OLVN — 50–60 km from CN01/RDON) can be used as alternates with degraded fix probability at those baselines.

**Legacy platform**: `rtgpsout.unavco.org` retired 2025-07-29; all NOTA streams now on `ntrip.earthscope.org`.

---

## Commercial / volunteer overlay check (2026-05-17)

- **rtk2go**: zero AG/B mountpoints. Verified 2026-05-17: `py scripts/stations_by_country.py ATG` → only the 3 EarthScope stations.
- **Centipede-RTK**: zero AG/B nodes (same script; not in stations.json).
- **GEODNET**: zero AG/B stations. Coverage map (`rtk.geodnet.com/coverage/`) renders client-side; sandbox cannot extract tiles, but no AG/B station cited in any web result and GEODNET is not in local pipeline sources.
- **ONOCOY**: zero AG/B stations. Coverage map (`console.onocoy.com`) renders client-side; no AG/B station cited in any web result.
- **Trimble VRS Now**: not advertised for AG/B on Trimble's published coverage map.
- **Hexagon HxGN SmartNet / Topcon TopNET Live**: no AG/B node confirmed on operator portals.

---

## National surveying authority

The **Lands and Survey Division** (Ministry of Lands, Housing and Agriculture) operates a Landfolio public-access portal at `lands.gov.ag` for cadastral records. Direct WebFetch to `lands.gov.ag` and the Landfolio sub-path failed from this sandbox (ECONNREFUSED). No public announcement of a national CORS/NTRIP service, no NTRIP caster, and no real-time correction product is referenced from any English-language search result targeting the domain. No OECS- or CARICOM-wide real-time CORS programme specific to AG was identified.

---

## Datum / epoch

Omitted. No citable official declaration of geodetic datum or epoch by the Antigua and Barbuda government was located. EPSG and general references list WGS84 as the customary coordinate frame for AG, but no governmental publication tying cadastre, surveying regulation, or CORS metadata to a specific datum realisation and epoch was found in this round of research.

---

## Most recent project announcement

None identified for a dedicated AG national CORS/NTRIP service. No 2024–2026 procurement, donor-funded project, or operator portal launch surfaced in WebSearch.

---

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| EarthScope GNSS Data Archive (RINEX for BGGY, CN01, RDON) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial under NULA; USD $1,000/seat/yr commercial |

---

## Live-probe results (this sandbox, 2026-05-17)

| URL | Result |
|---|---|
| https://www.earthscope.org/data/gnss-realtime/ | 200 — content extracted |
| https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ | 200 — content extracted (pub. 2024-03-07) |
| https://www.earthscope.org/nota/ | 200 — content extracted |
| https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf | 200 — binary PDF returned; text non-extractable here |
| https://www.unavco.org/data/doi/10.7283/T5PK0D9W (BGGY DOI page) | 200 — content extracted |
| https://lands.gov.ag/ | ECONNREFUSED |
| https://lands.gov.ag/landfolio.publicaccess.web/Contents/about_us.aspx | ECONNREFUSED |
| http://ntrip.earthscope.org:2101/ (sourcetable HTTP) | TLS/certificate error from sandbox; local copy in `data/earthscope.sourcetable` is the source of truth |

Sandbox network limits (per CLAUDE.md) prevent direct caster probing; the `data/earthscope.sourcetable` refresh path (scripts/fetch_stations.py, run 2026-05-17) is the canonical liveness check and reports all 3 ATG mountpoints present.

---

## Sources consulted
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/
- EarthScope Network of the Americas: https://www.earthscope.org/nota/
- EarthScope commercial licensing announcement (2024-03-07): https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- EarthScope NULA PDF: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf
- UNAVCO/GAGE BGGY station DOI page: https://www.unavco.org/data/doi/10.7283/T5PK0D9W
- Antigua and Barbuda Lands and Survey Landfolio portal (unreachable from sandbox): https://lands.gov.ag/landfolio.publicaccess.web/Contents/about_us.aspx
- Local verification: `data/earthscope.sourcetable` lines 83 (BGGY), 118 (CN01), 970 (RDON); `scripts/stations_by_country.py ATG` returns same 3 stations; `scripts/source_health.py earthscope` = ok at 2026-05-17
- rtk2go and Centipede sourcetables — zero AG stations
