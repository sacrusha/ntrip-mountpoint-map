# Antigua and Barbuda [AG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (originally 2026-05-06)

## Status: No national caster — EarthScope scientific streams active on Antigua, Barbuda, and Redonda

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS streams in AG territory** | Yes — EarthScope NOTA: **CN01** (Bethesda, Antigua main island; lat 17.05, lon -61.76), **BGGY** (Codrington area, Barbuda; lat 17.05, lon -61.86), **RDON** (Redonda Island; lat 16.93, lon -62.35). All RTCM 3.3, GPS+GLO+BDS+GAL+SBAS+QZS, on `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | **Yes** (noncommercial tier — no surveying licence required, individual account accepted) |
| **legal_residency_required** | **No** — no nationality or residency restriction in NULA |
| **last_confirmed_alive** | 2026-05-12: 3 ATG stations confirmed in `data/earthscope.sourcetable` (CN01, BGGY, RDON; receivers Trimble NetR9 / Septentrio PolaRx5); NULA dated v. 2025-05-30 |

---

## EarthScope NOTA — COCONet/NOTA Stations in Antigua and Barbuda Territory

| Mountpoint | Location (sourcetable lat/lon) | Receiver | Notes |
|---|---|---|---|
| **CN01_RTCM3P3** | 17.05, -61.76 (Bethesda, Antigua main island) | Trimble NetR9 | COCONet original site; primary station for Antigua positioning |
| **BGGY_RTCM3P3** | 17.05, -61.86 (Barbuda; Codrington area) | Trimble NetR9 | COCONet Barbuda site (legacy code CN00 has been superseded by BGGY in the current sourcetable) |
| **RDON_RTCM3P3** | 16.93, -62.35 (Redonda Island; ~56 km SW of Antigua) | Septentrio PolaRx5 | Uninhabited dependency of Antigua; COCONet expansion-phase install |

Mountpoint naming convention: legacy 4-char COCONet code + `_RTCM3P3` suffix. Format RTCM 3.3 MSM (1077/1087/1097/1107/1117) + station coordinates (1005/1007), 60 s intervals on metadata streams. Single-base raw observations — not a VRS / network-RTK service.

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT a VRS/Network-RTK service) |
| **Tariff — noncommercial** | **Free (USD $0.00)** — account + annual NULA acceptance required. Date observed: 2026-05-06. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **Tariff — commercial** | **USD $1,000 per seat per year** (EarthScope is US 501(c)(3) nonprofit; no VAT). Min 5 seats for direct billing. Date observed: 2026-05-06. Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |

**Practical note on CN01 (Bethesda, Antigua)**: This is the most useful station for positioning on Antigua's main island. Single-base RTK accuracy is good within ~20–30 km. BGGY on Barbuda (~30 km north of Antigua) is at the edge of single-base reliable range from southern Antigua but ideal for users on Barbuda itself. RDON on Redonda (~56 km SW of Antigua) is too distant for cm-accuracy single-base from the main islands but useful for any work on Redonda.

**Cross-territory cluster (Montserrat)**: 5 additional EarthScope stations on Montserrat (CN62, TRNT, RCHY, AIRS, OLVN — all MSR territory) lie 50–60 km from Redonda and Antigua; they can be used as alternate single-base mountpoints if CN01/BGGY are unavailable, though baselines of 50+ km degrade L1+L2 fix probability.

**Note on legacy platform**: Old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

---

## National Surveying Authority

The **Lands and Survey Division** (also referred to as the Survey Department) is the government body responsible for geodetic and cadastral surveys in Antigua and Barbuda. A **Landfolio** land management portal is operated at `lands.gov.ag`. No NTRIP caster, CORS endpoint, or real-time GPS correction service was found on or linked from that portal as of 2026-05-06. No public announcement of a planned national RTK/CORS network was found.

---

## Most Recent Project Announcement

None found for a dedicated Antigua and Barbuda national CORS/NTRIP service. No OECS or CARICOM-wide CORS/NTRIP project specific to Antigua was identified.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive** — COCONet CN00 and CN01 RINEX archive | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

## Sources Consulted
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/
- EarthScope Network of the Americas (NOTA): https://www.earthscope.org/nota/
- EarthScope commercial licensing announcement: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- EarthScope NULA v. 2025-05-30: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf
- COCONet site info page (UNAVCO/GAGE): https://coconet.unavco.org/site-info/site-info.html
- COCONet Redonda Island expansion news: https://www.unavco.org/news/coconet-gps-network-expansion-redonda-island/
- Antigua and Barbuda Lands and Survey Division portal: https://www.lands.gov.ag/landfolio.publicaccess.web/Contents/about_us.aspx
- Local data verification (2026-05-12): `data/earthscope.sourcetable` lines 86 (BGGY), 122 (CN01), 973 (RDON) — 3 ATG mountpoints; `scripts/stations_by_country.py ATG` confirms same 3 stations
- RTK2go / Centipede sourcetables — no AG stations found
- NTRIP-list.com North America — no AG entry found
