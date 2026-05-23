# Kuwait [KW] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

No public NTRIP RTK caster confirmed for Kuwait 2026-05-23. A government
CORS network of ~14 stations is operated jointly by PACI (Public Authority
for Civil Information) and Kuwait Municipality; access is described in
academic literature as restricted to licensed surveying firms under
municipal/government contract. No public host:port, no published tariff,
no individual/hobbyist registration path indexed on any operator or
third-party surface 2026-05-23.

No rtk2go / Centipede / EarthScope / IGS-IP node in-country 2026-05-23.
Cross-border spill from KSA-CORS to the south is theoretically possible
~50 km from Kuwait's southern border but KSA-CORS gates non-SA IPs, so
unusable in practice (see `SA_SaudiArabia.md`). Hobbyist fallbacks reduce
to deploying a private base or Galileo HAS (~40 cm).

## Casters

### PACI / Kuwait Municipality CORS — government-only

- operator: Public Authority for Civil Information (PACI) and Kuwait
  Municipality (joint)
- landing_url: https://www.paci.gov.kw/en (PACI English landing; WebFetch
  ECONNREFUSED from sandbox 2026-05-23 — site appears IP-gated, no
  English mirror found)
- access_url: omitted — no public self-service registration surface
  exists; the published path for licensed surveyors is direct contract
  with the municipality. There is no signup page to link.
- access_type: restricted — academic citations consistently describe
  access as limited to licensed surveying firms operating under
  municipal/government contract; no published self-service path. Tariff
  not published (checked: paci.gov.kw 2026-05-23 WebFetch ECONNREFUSED;
  ScienceDirect Kuwait geoid 2026-05-23 via WebSearch; GPS World
  Kuwait-BeiDou 2026-05-23 via WebSearch; ArduSimple no KW page).
- coverage: full Kuwait (~17,818 km², flat terrain — a 14-CORS network
  at typical ~30–40 km spacing covers the country)
- num_stations: ~14 (secondary citation: Mahdi & Ahmed 2024 academic
  study processed 14 days of GNSS data for "the 14 Kuwait CORS"
  integrated with 27 IGS stations using Bernese; no operator portal
  declaration confirmed)
- hobbyist_eligibility: no — closed to licensed firms; no individual
  tier published
- residency_required: ? — no individual path exists at any price, so
  the question is moot in practice; PACI's mandate is Kuwaiti civil
  registration, suggesting any future opening would be residency-
  bound (checked: paci.gov.kw 2026-05-23 ECONNREFUSED; ScienceDirect
  Kuwait geoid paper 2026-05-23; mvarga1989 CORS list 2026-05-23 —
  Kuwait not listed)
- datum_epoch: omitted — no operator-portal declaration to cite. The
  academic literature references the "KW-FWGM2022" geoid model (Kuwait
  Free-air with Modified Stokes' kernel, 2022; <1.8 cm σ) as the
  national orthometric-height reference, but per the operator-citation
  rule this is not a citable NTRIP-frame declaration.

## Disqualified / not applicable

- **rtk2go** — 0 mountpoints in KW 2026-05-23
  (`py scripts/stations_by_country.py KWT` → "No stations for 'KWT'").
- **Centipede, EarthScope, IGS-IP** — 0 KW-coded stations 2026-05-23
  (same script).
- **GEODNET, onocoy, PointOne, HxGN SmartNet, Trimble VRS Now** — no
  Kuwait coverage advertised in public documentation 2026-05-23.
- **ArduSimple Kuwait** — no dedicated `…in-kuwait/` country page
  indexed 2026-05-23.
- **KSA-CORS cross-border spill** — see `SA_SaudiArabia.md`. Nearest
  Saudi CORS in the Al-Hafuf / Dammam / Al-Wafrah corridor are ~50 km
  from Kuwait's southern border and may provide marginal VRS coverage
  in southernmost Kuwait inside KSA-CORS hull extrapolation, but the
  caster IP-gates non-SA addresses so this is unusable from a Kuwait IP
  in practice.

## Post-Processing (RINEX) fallback

| Service | URL | Notes |
|---|---|---|
| IGS / EarthScope | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; no IGS station in Kuwait 2026-05-23, nearest in KSA and IR |

## Sources Consulted

- PACI landing: https://www.paci.gov.kw/en (WebFetch ECONNREFUSED from
  sandbox 2026-05-23; site reachable only from KW-region resolvers per
  prior probes)
- ScienceDirect — Refinement of the Kuwait geoid (KW-FWGM2022):
  https://www.sciencedirect.com/science/article/pii/S1110982323000261
- GPS World — Kuwait high-rise BeiDou construction CORS:
  https://www.gpsworld.com/kuwait-high-rise-goes-up-with-assist-from-beidou/
- GIM International — Core Wall Control Survey in Kuwait:
  https://www.gim-international.com/content/article/core-wall-control-survey
- mvarga1989 GitHub — community CORS/RTK networks list (Kuwait not
  listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- ArduSimple country listing (Kuwait not present, 2026-05-23):
  https://www.ardusimple.com/rtk-correction-services-in-your-country/
- EPSG — coordinate reference systems for Kuwait:
  https://epsg.io/?q=Kuwait
- SA_SaudiArabia.md (project internal) — KSA-CORS context.
- Local data 2026-05-23: `py scripts/stations_by_country.py KWT` →
  no stations on any tracked source.
