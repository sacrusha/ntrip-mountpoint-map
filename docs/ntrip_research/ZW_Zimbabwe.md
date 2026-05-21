# Zimbabwe [ZW] — NTRIP RTK Caster Research

## Status
CORS network operational but NTRIP endpoint NOT publicly published. Access gated through ZINGSA contact. Statutory fee US$200/yr.

## Caster: ZINGSA CORS Network

| Field | Value |
|---|---|
| landing_url | https://zingsa.ac.zw/ |
| access_url | https://zingsa.ac.zw/django-test/cors (CORS-RINEX Data Services portal; no host:port published) |
| host:port | not publicly disclosed; access via ZINGSA contact channels (see landing_url) |
| tariff | **US$200/yr flat** — Statutory Instrument 47 of 2023 (Land Survey (Surveyor-General's Office) (Prescribed Fees) (Amendment) Notice, 2023, First Schedule Item 17). VAT not stated in SI. Date observed: 2023-04-07 (gazette). |
| num_stations | unknown — operator portal claims CORS "established and operationalized" + 2024 Herald densification cite, but no published station count. Initial build was 5 stations (EU/UNDP-funded, Mlambo & Ali 2020 planning paper); current state not disclosed. |
| vrs | ? — not documented publicly |
| hobbyist_eligibility | ? — ZINGSA describes broad user pool ("surveyors, GIS users, engineers, scientists and other people who collect GNSS data"); no published hobbyist policy or exclusion |
| legal_residency_required | ? — no published ToS |
| last_confirmed_alive | 2026-05-21 — `https://zingsa.ac.zw/` WebFetch 200; portal confirms CORS Network operational ("Continuously Operating Reference Stations (CORS) Network across Zimbabwe, providing accurate real-time positioning data for surveying, precision agriculture, and geophysical research"); `/django-test/cors` portal still indexed; `py scripts/stations_by_country.py ZW`/`ZWE` 2026-05-21 → "No stations"; no public NTRIP host:port disclosed |
| datum_epoch | omitted — no citable declaration on ZINGSA portal or in SI 47/2023 |

## Operator

**ZINGSA — Zimbabwe National Geospatial and Space Agency**
Web: https://zingsa.ac.zw/ (contact channels listed on portal)

**Fee-administering co-authority:** Surveyor-General's Office, Ministry of Lands, Agriculture, Fisheries, Water and Rural Development (agric.gov.zw). Land Survey Act [Cap. 20:12] §10 vests fee-setting in the Minister; SI 47/2023 First Schedule Item 17 sets the US$200/yr CORS fee. SG branches: Harare + Bulawayo.

## Context

- 2018 — ZINGSA established under Research Act [Chapter 10:22].
- 2020 — Mlambo & Ali academic paper: ZW in CORS planning phase; EU/UNDP funded initial 5 stations.
- 2021 — Public launch by Mnangagwa at UZ Science Park.
- 2023-04-07 — SI 47/2023 gazetted; US$200/yr CORS fee.
- 2024-02-04 — Herald: ZINGSA densifying CORS network.
- 2024-03 — US terminates ZW sanctions programme (EO 13288/13391/13469 revoked); selected re-designations under GLOMAG. No remaining sanctions barrier to GNSS hardware import.
- 2025 — ZiG 64.22M (~USD 1.78M) allocated to ZINGSA space programme incl. CORS.
- Volunteer / commercial alternatives: zero ZW coverage on rtk2go, Centipede, EarthScope NOTA, IGS-IP (HARB is ZAF, not ZWE), EUREF-IP, GEODNET, ONOCOY, ArduSimple, HxGN. AFREF 2016 map showed central-southern Africa devoid of CORS; ZINGSA build-out superseded but operator-side data still gated.
- TrigNet (ZA): closest station >300 km from southern ZW border; out of single-base range.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| ZINGSA CORS-RINEX service | https://zingsa.ac.zw/django-test/cors | unknown; access via ZINGSA contact channels |

## Sources
- ZINGSA portal: https://zingsa.ac.zw/
- ZINGSA CORS-RINEX page: https://zingsa.ac.zw/django-test/cors
- SI 47/2023 (full text, Item 17 = US$200/yr CORS fee): https://www.veritaszim.net/sites/veritas_d/files/SI%202023-047%20Land%20Survey%20(Surveyor-General%E2%80%99s%20Office)%20(Prescribed%20Fees)%20(Amendment)%20Notice,%202023%20(No.%2020).pdf
- Surveyor-General page (Ministry of Lands): https://www.agric.gov.zw/wordpress/?page_id=7971
- Herald Zimbabwe (Feb 2024, densification): https://www.heraldonline.co.zw/technology-to-enhance-countrys-ability-to-solve-challenges/
- Mlambo & Ali 2020 (planning-phase paper, 5 initial stations): https://doaj.org/article/835a37dd28564728869ad42dcde830d2
- Space in Africa (2025 budget): https://spaceinafrica.com/2025/01/10/zimbabwes-2025-space-budget-a-strategic-leap-for-zingsa/
- Space in Africa (2021 launch context): https://spaceinafrica.com/2021/09/24/zingsa-to-tackle-local-socio-economic-problems-using-geospatial-and-space-technologies/
- OFAC 2024-04-16 (sanctions termination): https://ofac.treasury.gov/recent-actions/20240416
- Dentons brief on sanctions termination + GLOMAG transition: https://www.dentons.com/en/insights/alerts/2024/march/5/us-terminates-zimbabwe-sanctions-program-transitions-certain-designations-to-glomag
