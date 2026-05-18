# Zimbabwe [ZW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verification of 2026-05-16 baseline)

## Status: CORS network operational but NTRIP endpoint NOT publicly published. Access gated through ZINGSA contact. Statutory fee US$200/yr.

## Caster: ZINGSA CORS Network

| Field | Value |
|---|---|
| landing_url | https://zingsa.ac.zw/ |
| access_url | https://zingsa.ac.zw/django-test/cors (CORS-RINEX Data Services portal; no host:port published) |
| host:port | not publicly disclosed; access via ZINGSA contact channels (see landing_url) |
| tariff | **US$200/yr flat** — Statutory Instrument 47 of 2023 (Land Survey (Surveyor-General's Office) (Prescribed Fees) (Amendment) Notice, 2023, First Schedule Item 17). VAT not stated in SI. Date observed: 2023-04-07 (gazette). |
| num_stations | unknown; ZINGSA marketing claims "established and operationalized"; Feb 2024 Herald confirms densification ongoing. Known station: ZINH (Harare) — referenced in internal ZINGSA DJI M300 setup document. |
| vrs | ? — not documented publicly |
| hobbyist_eligibility | ? — ZINGSA describes broad user pool ("surveyors, GIS users, engineers, scientists and other people who collect GNSS data"); no published hobbyist policy or exclusion |
| legal_residency_required | ? — no published ToS |
| last_confirmed_alive | 2026-05-17 — `https://zingsa.ac.zw/` HTTP 200; `/django-test/cors` portal still indexed; `py scripts/stations_by_country.py ZWE` 2026-05-17 → "No stations for 'ZWE'"; no public NTRIP host:port disclosed |
| datum_epoch | omitted — no citable declaration on ZINGSA portal or in SI 47/2023 |

## Operator

**ZINGSA — Zimbabwe National Geospatial and Space Agency**
Web: https://zingsa.ac.zw/ (contact channels listed on portal)

**Fee-administering co-authority:** Surveyor-General's Office, Ministry of Lands, Agriculture, Fisheries, Water and Rural Development (agric.gov.zw). Land Survey Act [Cap. 20:12] §10 vests fee-setting in the Minister; SI 47/2023 First Schedule Item 17 sets the US$200/yr CORS fee. SG branches: Harare + Bulawayo.

## Timeline

| Date | Event |
|---|---|
| 2018 | ZINGSA concept under Research Act [Chapter 10:22]; Mnangagwa announcement |
| Sep 2020 | Academic paper (Mlambo & Ali): ZW "planning phase" for CORS; EU/UNDP funded initial 5 stations |
| Sep 2021 | Public launch by Mnangagwa at UZ Science Park (10 Jul opening, Sep inauguration) |
| 2023-04-07 | SI 47/2023 gazetted — Item 17 sets **US$200/yr flat fee** for CORS use |
| 2024-02-04 | Herald: ZINGSA "embarked on densification of CORS" — network operational + expanding |
| 2024-03-04 | US terminates ZW sanctions programme (EO 13288/13391/13469 revoked); 11 persons + 3 entities re-designated under GLOMAG. No remaining sanctions barrier to GNSS hardware import. |
| 2025-01-10 | 2025 budget: ZiG 64.22M (~USD 1.78M) to ZINGSA space programme incl. CORS |
| 2026-04-27 | ZINGSA DG vacancy advertised (applynow.co.zw) — agency proof-of-life 2026 |
| 2026-05-16 | Homepage Last-Modified 2026-04-29; marketing still claims CORS "established and operationalized"; densification still cited |
| 2026-05-17 | Re-verify: ZINGSA portal HTTP 200; WebSearch "ZINGSA CORS Zimbabwe NTRIP 2026" returns no new public NTRIP endpoint or tariff change beyond SI 47/2023; no ZW stations in any ingested sourcetable |

## Volunteer / Global Coverage

- rtk2go: zero ZW (ingested).
- Centipede: zero ZW.
- EarthScope NOTA: zero ZW.
- IGS-IP: zero ZW (HARB is HARB00ZAF Pretoria, ZA — not ZW).
- EUREF-IP: zero ZW.
- TrigNet (ZA): closest station >300 km from southern ZW border; out of single-base range; ZA-only.
- AFREF 2016: central-southern Africa incl. ZW "devoid of CORS installations"; superseded by ZINGSA build-out but operator-side data still gated.
- GEODNET, ONOCOY, ardusimple, HxGN: zero ZW.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| ZINGSA CORS-RINEX service | https://zingsa.ac.zw/django-test/cors | unknown; access via ZINGSA contact channels (see landing_url) |

## Sources
- ZINGSA portal: https://zingsa.ac.zw/ (HEAD 200, 2026-05-16)
- ZINGSA CORS-RINEX page: https://zingsa.ac.zw/django-test/cors
- SI 47/2023 (full text, Item 17 = US$200/yr CORS fee): https://www.veritaszim.net/sites/veritas_d/files/SI%202023-047%20Land%20Survey%20(Surveyor-General%E2%80%99s%20Office)%20(Prescribed%20Fees)%20(Amendment)%20Notice,%202023%20(No.%2020).pdf
- Surveyor-General page (Ministry of Lands): https://www.agric.gov.zw/wordpress/?page_id=7971
- Herald Zimbabwe (Feb 2024, densification): https://www.heraldonline.co.zw/technology-to-enhance-countrys-ability-to-solve-challenges/
- Mlambo & Ali 2020 (planning-phase paper): https://doaj.org/article/835a37dd28564728869ad42dcde830d2
- Space in Africa (2025 budget): https://spaceinafrica.com/2025/01/10/zimbabwes-2025-space-budget-a-strategic-leap-for-zingsa/
- Space in Africa (2021 launch context): https://spaceinafrica.com/2021/09/24/zingsa-to-tackle-local-socio-economic-problems-using-geospatial-and-space-technologies/
- OFAC 2024-04-16 (sanctions termination): https://ofac.treasury.gov/recent-actions/20240416
- Dentons brief on sanctions termination + GLOMAG transition: https://www.dentons.com/en/insights/alerts/2024/march/5/us-terminates-zimbabwe-sanctions-program-transitions-certain-designations-to-glomag
- ZINGSA DG vacancy (proof of life Apr 2026): https://applynow.co.zw/2026/04/27/zingsa-2/
- `py scripts/stations_by_radius.py -17.83 31.05 200` 2026-05-16 — zero
- `py scripts/stations_by_country.py ZW` 2026-05-16 — "No stations for 'ZW'"
- `py scripts/stations_by_country.py ZWE` 2026-05-17 — "No stations for 'ZWE'"
