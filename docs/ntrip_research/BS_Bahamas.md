# Bahamas [BS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: No national caster — EarthScope scientific streams available on two outer islands

| Field | Value |
|---|---|
| **National NTRIP RTK caster** | No |
| **Scientific GNSS streams in BS territory** | Yes — EarthScope NOTA (former COCONet) CN13 (San Salvador Island) and CN14 (Mathew Town, Great Inagua); all on `ntrip.earthscope.org:2101` |
| **hobbyist_eligibility** | **Yes** (noncommercial tier — no surveying licence required, individual account accepted) |
| **legal_residency_required** | **No** — no nationality or residency restriction in NULA |
| **last_confirmed_alive** | 2026-05-06 (EarthScope portal reachable; NULA dated v. 2025-05-30) |

---

## EarthScope NOTA — COCONet Stations in Bahamas Territory

| Station | Location | Notes |
|---|---|---|
| **CN13** | San Salvador Island, central Bahamas | ~460 km SE of Nassau |
| **CN14** | Mathew Town, Great Inagua, southernmost Bahamas | ~525 km SE of Nassau; ~80 km NE of Haiti/Cuba channel |

| Field | Value |
|---|---|
| **host:port** | `ntrip.earthscope.org:2101` (RTCM 3.3); port 2105 (BINEX); port 2108 (PPP) |
| **Stream type** | Raw 1 Hz multi-constellation RTCM 3.3 MSM7 (single-base reference, NOT VRS/Network-RTK) |
| **Tariff — noncommercial** | **Free (USD $0.00)** — account + annual NULA acceptance required. Date observed: 2026-05-06. Source: https://www.earthscope.org/data/gnss-realtime/ |
| **Tariff — commercial** | **USD $1,000 per seat per year** (EarthScope 501(c)(3); no VAT). Date observed: 2026-05-06. Source: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/ |
| **NULA version** | v. 2025-05-30 — https://www.earthscope.org/user/NoncommercialLicenseAgreement.pdf |

**Practical caveat**: CN13 and CN14 are both located on outer islands far from Nassau (New Providence) and Grand Bahama, where most commercial and survey activity occurs. Nassau is ~460 km from the nearest COCONet station; single-base RTK is not viable at that distance. Users in Nassau and the northern Bahamas have no practical COCONet coverage for RTK.

**Note on legacy platform**: Old UNAVCO caster (`rtgpsout.unavco.org`) retired 2025-07-29; all streams now at `ntrip.earthscope.org`.

---

## National Surveying Authority

The **Department of Lands and Surveys** (Bahamas Government) is the responsible body for geodetic and cadastral work. No NTRIP caster, CORS endpoint, or real-time GPS correction service was found associated with the department as of 2026-05-06. No public announcement of a planned national RTK/CORS network was found. NOAA's National Geodetic Survey database lists an AUTEC (Atlantic Underwater Test and Evaluation Center) CORS station in Andros, Bahamas, operated by the US Navy, but this is a US Federal installation and not a Bahamian national service.

---

## Most Recent Project Announcement

None found for a dedicated Bahamian national CORS/NTRIP service. No CARICOM or regional geodetic CORS project specific to the Bahamas was identified.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope GNSS Data Archive** — COCONet CN13 and CN14 RINEX | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

## Sources Consulted
- EarthScope GNSS real-time data page: https://www.earthscope.org/data/gnss-realtime/
- EarthScope commercial licensing: https://www.earthscope.org/news/new-gnss-offering-and-licensing-details-for-commercial-use/
- COCONet site info (station list including CN13, CN14): https://coconet.unavco.org/site-info/site-info.html
- COCONet network overview: https://coconet.unavco.org/
- NOAA NGS CORS database (AUTEC Andros reference): https://geodesy.noaa.gov/CORS/
- NTRIP-list.com North America — no BS entry found
- RTK2go / Centipede sourcetables — no BS stations found
