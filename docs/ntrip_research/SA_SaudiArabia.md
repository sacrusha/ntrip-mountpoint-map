# Saudi Arabia [SA] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

One nationwide free government VRS network — KSA-CORS (GEOSA), 209 stations,
self-service registration, automatically-renewed free subscription. From a
non-Saudi IP, the caster TCP-resets on connect (firewall observed
2026-05-23 — connection established to `ksacors.geoportal.sa:2101 (212.62.124.118)` then
Recv reset, consistent with IP-geo gating). No commercial alternative
publishes Saudi coverage. No rtk2go / Centipede / EarthScope nodes
in-country 2026-05-23. RINEX fallback via the same GEOSA portal after
registration.

## Casters

### KSA-CORS — Kingdom of Saudi Arabia Continuously Operating Reference Station Network

- operator: GEOSA — General Authority for Survey and Geospatial Information
  (formerly GCS / GASGI)
- landing_url: https://www.geosa.gov.sa/en/products/geodesy/pages/ksa-cors.aspx
  (operator product page; describes the service. WebFetch returned 404 from
  sandbox 2026-05-23 — geoportal index has reorganised; same content
  republished on the `geoportal.sa` landings below and on Saudipedia.)
- access_url: https://www.geoportal.sa/pdf/How_to_Register_to_KSA-CORS_Network_v.1.0.pdf
  (operator-owned How-to-Register PDF; registration via online form on
  `ksacors.geoportal.sa/RegisterAccount.aspx` or by emailing the signed
  PDF to info@geosa.gov.sa)
- access_type: free-signup — GEOSA FAQ
  (geosa.gov.sa/En/Products/Geodesy/FAQ/Pages/FAQAboutKSA-CORS.aspx, WebSearch
  snippet 2026-05-23): *"The subscription is currently free and shall be
  automatically renewed."* FAQ page itself returns 404 from sandbox; text is
  retrievable only via cached search snippets. Saudipedia article 2026-05-23
  separately describes the service as a free subscription but does not
  reproduce the FAQ wording.
- coverage: full Kingdom — high-density national grid; service portal exposes
  4 sourcetable mountpoints at the operations centre coordinate
  (24.40, 46.41), no per-station mountpoints. Of those four, only
  NRTK_VRS and NEAREST_RTK are RTK in this project's sense; NDGPS_VRS is
  code-only DGNSS (out of scope) and NRTK_RTX is the Trimble RTX
  PPP/SSR-via-NTRIP stream (out of scope per CLAUDE.md).
- num_stations: 209 (operator-declared on the GEOSA KSA-CORS product page;
  333 CORS were used in the KSA-GRF17 determination per FIG 2023 — the
  larger figure mixes operational CORS with historical / one-shot
  collocations and is not the current real-time count)
- hobbyist_eligibility: yes — registration accepts any user; no
  licensed-surveyor or commercial-entity gate. Saudipedia describes
  applications including "navigation, machine control, asset tracking,
  vehicle navigation, fleet management" alongside professional survey.
- residency_required: ? — registration form requires national/organisational
  details; no explicit nationality clause has been confirmed or denied
  on either the geoportal How-to-Register PDF or the GEOSA FAQ
  (checked: geoportal.sa How-to-Register 2026-05-23 via WebSearch;
  saudipedia 2026-05-23 via WebFetch; ksacors.geoportal.sa portal
  2026-05-23 via direct TCP probe — caster reachable but TCP-resets
  Recv on non-SA IP)
- sourcetable: `ksacors.geoportal.sa:2101` — TCP probe 2026-05-23
  established connection to 212.62.124.118:2101 then Recv reset before
  any response bytes returned. Consistent with IP-geo gating; sourcetable
  unreadable from outside Saudi Arabia / GCC. Mountpoint inventory
  (NRTK_VRS / NEAREST_RTK / NDGPS_VRS / NRTK_RTX) is reproduced from
  prior in-country fetches and the Getting Started v2.0 PDF.
- vrs: yes — KSA-CORS Getting Started v2.0 specifies VRS as the primary
  network-RTK service; NEAREST_RTK is single-base routing. NRTK_RTX is
  the Trimble RTX-style PPP/SSR stream (out of project scope).
- stations_source: operator station map at
  https://apps.geoportal.sa/KSA-CORS/ (gated — login required to view
  individual CORS coordinates; map renders no station markers without
  authentication). 333-CORS GRF17 station listing only in FIG 2023 PDF.
- datum_epoch: KSA-GRF17 — operator-declared frame for the Saudi National
  Spatial Reference System (SANSRS v2.0, December 2022;
  https://www.geoportal.sa/pdf/SANSRS_Implementation_Guidelines_V_2_0.pdf).
  Epoch is not stated alongside the frame on the operator landing; FIG
  2023 / academic literature refers to "KSA-GRF17" with realisation
  year 2017 but the canonical epoch is not declared on the cited
  operator pages.

### rtk2go, Centipede, EarthScope, IGS-IP — no Saudi-coded stations

- rtk2go: 0 mountpoints in SAU. Verified 2026-05-23:
  `py scripts/stations_by_country.py SAU` → "No stations for 'SAU'".
- Centipede: 0 SA nodes 2026-05-23 (same script). KHAY (25.72, 39.30)
  was briefly present in 2026-05-12 archive but is no longer tagged
  SAU; not relied on.
- EarthScope NOTA: not applicable (NOTA = Americas).
- IGS-IP: no SA-tagged station in `data/igs_ip.sourcetable` 2026-05-23.

## Disqualified / not applicable

- **GEODNET, onocoy, PointOne, HxGN SmartNet, Trimble VRS Now** — no Saudi
  coverage advertised on public coverage maps 2026-05-23.
- **Commercial NTRIP resellers in KSA** — no independent paid NTRIP service
  with confirmed Saudi coverage has been identified; ArduSimple's Saudi
  page lists only KSA-CORS + the global trio (rtk2go, IGS, EarthScope).

## Post-Processing (RINEX) fallback

| Service | URL | Notes |
|---|---|---|
| KSA-CORS RINEX | https://ksacors.geoportal.sa/ | Same free registration as the real-time service |
| IGS / EarthScope | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; select Saudi IGS stations historically contributed |

## Sources Consulted

- GEOSA KSA-CORS product page (404 from sandbox 2026-05-23; cached content
  via WebSearch snippet + Saudipedia):
  https://www.geosa.gov.sa/en/products/geodesy/pages/ksa-cors.aspx
- GEOSA KSA-CORS Phase One page (also 404 from sandbox 2026-05-23):
  https://www.geosa.gov.sa/En/Products/Products_v1/GeodesyandLandSurvey/pages/cors.aspx
- KSA-CORS Web service portal: https://ksacors.geoportal.sa/
- KSA-CORS legacy portal: https://ksacors.gcs.gov.sa/
- KSA-CORS Network Web Login (geosa subdomain): https://ksacors.geosa.gov.sa/Login.aspx
- KSA-CORS Getting Started v1.0 (geoportal.sa):
  https://www.geoportal.sa/pdf/Getting_Started_with_KSA-CORS_Network_v1.0.pdf
- KSA-CORS Getting Started v2.0:
  https://ksacors.geosa.gov.sa/WelcomePage/Getting%20Started%20with%20KSA-CORS%20Network_v.2.0.pdf
- How to Register v1.0:
  https://www.geoportal.sa/pdf/How_to_Register_to_KSA-CORS_Network_v.1.0.pdf
- Saudipedia KSA-CORS article (2026-05-23 WebFetch 200; confirms 209
  stations, KSA-GRF17, free subscription, automatic renewal):
  https://saudipedia.com/en/article/4075/government-and-politics/communication-and-information-technology/saudi-arabia-continuously-operating-reference-station-ksa-cors-network
- SANSRS v2.0 implementation guidelines (Dec 2022):
  https://www.geoportal.sa/pdf/SANSRS_Implementation_Guidelines_V_2_0.pdf
- Establishment of KSA-CORS Network, FIG 2023 (333-CORS GRF17 set):
  https://www.fig.net/resources/proceedings/fig_proceedings/fig2023/papers/ts04g/TS04G_al-qahtani_salawu_et_al_12208.pdf
- KSA-CORS apps portal (login-gated map):
  https://apps.geoportal.sa/KSA-CORS/
- ArduSimple Saudi Arabia RTK page:
  https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-saudi-arabia/
- Direct TCP probe 2026-05-23 of `ksacors.geoportal.sa:2101` →
  connection established to 212.62.124.118:2101, Recv reset before
  bytes returned (IP-geo gate observed)
- Local data 2026-05-23: `py scripts/stations_by_country.py SAU` →
  no stations on any tracked source.
