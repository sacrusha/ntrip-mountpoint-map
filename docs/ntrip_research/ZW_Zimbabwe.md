# Zimbabwe [ZW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (re-verification of 2026-05-06 baseline)

## Status: CORS exists — NTRIP endpoint NOT publicly disclosed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown / probably yes (semi-operational; access gated through direct contact) |
| **host:port** | Not publicly published — CORS portal at https://zingsa.ac.zw/django-test/cors does not expose NTRIP host:port |
| **tariff** | **US$200/year flat fee** for CORS use — published in Statutory Instrument 47 of 2023 (Land Survey (Surveyor-General's Office) (Prescribed Fees) (Amendment) Notice, 2023, Item 17). Not advertised on the ZINGSA website; contact still required for credentials and host:port. |
| **hobbyist_eligibility** | Unclear — ZINGSA describes users broadly ("surveyors, GIS users, engineers, scientists and other people who collect GNSS data") but no published hobbyist policy |
| **legal_residency_required** | Unclear — no published terms of service |
| **registration** | Not self-service; email publicrelations@zingsa.ac.zw or phone +263-8677009885 / +263-8677009884 |
| **last_confirmed_alive** | 2026-05-13 — `https://zingsa.ac.zw/` HTTP 200 confirmed (HEAD probe); CORS portal page still indexed by search engines on 2026-05-13; no ZW mountpoint found in any public NTRIP sourcetable; stations_by_radius.py -17.83 31.05 200 (Harare) returns zero results |

## Operator

**ZINGSA — Zimbabwe National Geospatial and Space Agency**
630 Churchill Avenue, Mount Pleasant, Harare, Zimbabwe
Phone: +263 8677009885 / +263 8677009884
Email: publicrelations@zingsa.ac.zw
Website: https://zingsa.ac.zw/

**Co-administering authority for fee collection:** Surveyor-General's Office,
Ministry of Lands, Agriculture, Fisheries, Water and Rural Development
(agric.gov.zw). The Land Survey Act [Cap. 20:12] § 10 vests fee-setting
in the Minister of Lands; SI 47/2023 First Schedule Item 17 sets the
CORS fee. The Surveyor-General's Office operates from Harare and
Bulawayo branches and lists CORS among its geodetic services.

## Timeline

| Date | Event |
|------|-------|
| 2018 | ZINGSA concept established under the Research Act [Chapter 10:22]; initial Mnangagwa announcement |
| Sep 2020 | Academic paper: Zimbabwe in "planning phase" for CORS; EU/UNDP funding earmarked for initial 5 stations |
| Sep 2021 | ZINGSA publicly launched by President Mnangagwa alongside the Zimbabwe Science Park at the University of Zimbabwe (10 July opening; September 2021 inauguration event) |
| Apr 7, 2023 | Statutory Instrument 47 of 2023 (Land Survey (Surveyor-General's Office) (Prescribed Fees) (Amendment) Notice, 2023, No. 20) gazetted by the Minister of Lands, Agriculture, Fisheries, Water and Rural Development under s.10 Land Survey Act [Cap. 20:12]. **Item 17 of the new First Schedule: "A flat fee of US$200 per year, shall be charged for the use of Continuously Operating Reference Stations (CORS)."** Confirms a published, paid-only access model administered by the Surveyor-General's Office. |
| Feb 4, 2024 | Herald Zimbabwe confirms ZINGSA "has embarked on densification of CORS" — network described as operational but expanding |
| Mar 4, 2024 | US terminates the Zimbabwe sanctions programme (E.O. 13288/13391/13469 revoked); SDN List delistings under the country programme. 11 individuals (incl. President Mnangagwa) and 3 entities re-designated under the Global Magnitsky programme (GLOMAG, E.O. 13818). No sanctions barrier to ordinary GNSS hardware import after this date. |
| Jan 10, 2025 | 2025 national budget allocates ZiG 64.22 million (~USD 1.78M) to ZINGSA space programme including CORS |
| Apr 27, 2026 | ZINGSA advertises Director General vacancy (applynow.co.zw) — confirms agency still operating in 2026; ZINGSA homepage marketing still describes CORS network as "established and operationalized" |

## Known Station

- **ZINH** (Harare) — referenced in internal ZINGSA DJI M300 RTK setup document. Connection parameters not publicly disclosed.

## Negative Findings

- RTK2GO: No ZW mountpoints in any public sourcetable
- IGS: No Zimbabwe stations in network. Note: "HARB" is HARB00ZAF in Pretoria, South Africa — not Zimbabwe.
- AFREF (2016 docs): Central-southern Africa including Zimbabwe "devoid of CORS installations"
- HartRAO: No Zimbabwe stations in 28-station African archive
- TrigNet: South Africa only; RTK range does not reach Zimbabwe
- GEODNET, ONOCOY, ArduSimple: Zimbabwe not listed
- ntrip-list.com Africa: Zimbabwe not listed

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **ZINGSA CORS RINEX data service** — portal page exists; access method and cost not publicly disclosed | https://zingsa.ac.zw/django-test/cors | Unknown — contact publicrelations@zingsa.ac.zw |

## Sources
- https://zingsa.ac.zw/ (CORS portal; HTTP 200 re-confirmed 2026-05-13)
- https://zingsa.ac.zw/django-test/cors (CORS-RINEX Data Services page)
- https://www.heraldonline.co.zw/technology-to-enhance-countrys-ability-to-solve-challenges/ (Feb 2024)
- https://doaj.org/article/835a37dd28564728869ad42dcde830d2 (Mlambo & Ali 2020)
- https://spaceinafrica.com/2025/01/10/zimbabwes-2025-space-budget-a-strategic-leap-for-zingsa/
- https://spaceinafrica.com/2021/09/24/zingsa-to-tackle-local-socio-economic-problems-using-geospatial-and-space-technologies/ (Sep 2021 — public launch context)
- https://businesschief.eu/leadership-and-strategy/president-mnangagwa-launches-space-agency-zimbabwe (launch event context)
- https://www.veritaszim.net/sites/veritas_d/files/SI%202023-047%20Land%20Survey%20(Surveyor-General%E2%80%99s%20Office)%20(Prescribed%20Fees)%20(Amendment)%20Notice,%202023%20(No.%2020).pdf — SI 47/2023 full text; Item 17 sets US$200/yr CORS fee
- https://www.agric.gov.zw/wordpress/?page_id=7971 — Surveyor-General page, Ministry of Lands, Agriculture, Fisheries, Water and Rural Development
- https://ofac.treasury.gov/recent-actions/20240416 — OFAC publication removing the Zimbabwe Sanctions Regulations
- https://www.dentons.com/en/insights/alerts/2024/march/5/us-terminates-zimbabwe-sanctions-program-transitions-certain-designations-to-glomag — March 2024 sanctions termination and GLOMAG transition
- https://applynow.co.zw/2026/04/27/zingsa-2/ (DG vacancy April 2026 — proof of life)
- ntrip-list.com/africa, ArduSimple country directory
