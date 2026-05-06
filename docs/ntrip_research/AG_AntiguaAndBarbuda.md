# Antigua and Barbuda [AG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: No national caster — EarthScope scientific streams available on two islands

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS streams in AG territory** | Yes — EarthScope NOTA (former COCONet) CN00 (Codrington, Barbuda) and CN01 (Bethesda, Antigua), plus a third site on Redonda Island (belongs to Antigua); all on `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | **Yes** (noncommercial tier — no surveying licence required, individual account accepted) |
| **legal_residency_required** | **No** — no nationality or residency restriction in NULA |
| **last_confirmed_alive** | 2026-05-06 (EarthScope portal reachable; NULA dated v. 2025-05-30) |

---

## EarthScope NOTA — COCONet Stations in Antigua and Barbuda Territory

| Station | Location | Notes |
|---|---|---|
| **CN00** | Codrington, Barbuda | COCONet original site |
| **CN01** | Bethesda, Antigua (main island) | COCONet original site |
| **Redonda site** | Redonda Island (~56 km SW of Antigua) | Remote uninhabited dependency of Antigua; installed during COCONet expansion phase; station code not confirmed in search results |

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT a VRS/Network-RTK service) |
| **Tariff — noncommercial** | **Free (USD $0.00)** — account + annual NULA acceptance required. Date observed: 2026-05-06. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **Tariff — commercial** | **USD $1,000 per seat per year** (EarthScope is US 501(c)(3) nonprofit; no VAT). Min 5 seats for direct billing. Date observed: 2026-05-06. Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |

**Practical note on CN01 (Bethesda, Antigua)**: This is the most useful station for positioning on Antigua's main island. Single-base RTK accuracy is good within ~20–30 km of the station. CN00 on Barbuda (~60 km north) is at the edge of single-base reliable range from most of Antigua.

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
- EarthScope commercial licensing announcement: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- EarthScope NULA v. 2025-05-30: https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf
- COCONet site info page (UNAVCO/GAGE): https://coconet.unavco.org/site-info/site-info.html
- COCONet Redonda Island expansion news: https://www.unavco.org/news/coconet-gps-network-expansion-redonda-island/
- Antigua and Barbuda Lands and Survey Division portal: https://www.lands.gov.ag/landfolio.publicaccess.web/Contents/about_us.aspx
- RTK2go / Centipede sourcetables — no AG stations found
- NTRIP-list.com North America — no AG entry found
