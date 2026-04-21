# Free RTK NTRIP — East Africa survey (ET, TZ, UG, SD, MZ)

_Research for `docs/country-survey.md`. Findings based on local data search
(stations.json, all sourcetables, networks.md, global-survey.md) and web
research as of 2026-04-21. Notes below cover what is known about government
geodetic agencies, CORS activity, and the gap picture for hobbyists and small
shops._

_Last researched: 2026-04-21._

---

## Research summary

Across the five countries only **Uganda** has a confirmed, operational,
free-for-registration public NTRIP service (UGRF, 40 government CORS stations,
Leica Spider Business Center). **Ethiopia** launched its first CORS network
(ETCORS/SSGI) in late 2025 with ~10 installed stations; NTRIP host:port is
not yet publicly discoverable — deferred. Tanzania, Sudan, and Mozambique have
no confirmed public NTRIP caster; CORS infrastructure is internal-use or
research-only in each case.

Volunteer coverage is effectively zero for all five countries:

| Country | rtk2go stations | Centipede stations | Notes |
|---|---|---|---|
| ET — Ethiopia | 0 | 0 | One AUSCORS IGS station in Djibouti (DJIG00DJI0) at lon 43.56°, not in Ethiopia |
| TZ — Tanzania | 0 | 0 | Zero country=TZA in any sourcetable |
| UG — Uganda | 1 | 0 | MBAR00UGA0 (AUSCORS, Mbarara) — raw obs only, non-commercial NULA |
| SD — Sudan | 0 | 0 | Zero country=SDN in any sourcetable |
| MZ — Mozambique | 0 | 0 | Four TrigNet stations at MZ border edge (Nspt, Pbwa, Sprt, Tdou) are ZA-side |

The TrigNet border stations assigned `country=ZAF` by coordinate-lookup
fall inside or immediately adjacent to Mozambique by coordinate but are
South African TrigNet installations in the Limpopo region, not Mozambican.

Key structural constraints shared across the region:
- No country has enacted an open-data geodesy mandate comparable to
  Indonesia's Law No. 4/2011 or Colombia's Law 1955/2019.
- Station density, where CORS infrastructure exists, is far below RTK
  operational thresholds. Baselines of 200–600 km are typical.
- Internet connectivity is improving but remains a barrier in rural areas,
  compounding the difficulty of sustaining continuous NTRIP streaming.

---

## Middle East & Africa (extension)

### ET — Ethiopia

- **Free government RTK**: nascent. **ETCORS** (Space Science and Geospatial
  Institute / SSGI, formerly Ethiopian Space Science and Technology Institute
  ESSTI, formerly Ethiopian Mapping Agency EMA) launched a first batch of
  approximately 10 CORS stations in December 2025, covering Addis Ababa,
  Sheger, Bonga, Semera, Jigjiga, Debre Berhan, and Jimma. SSGI announced
  targets of 30 stations within two years and a long-run goal of ~200 to
  achieve national coverage.
  - The service is intended "not only for Ethiopia but also for neighboring
    countries and the global community" (ENA state news agency, Dec 2025),
    but as of April 2026 no NTRIP host:port has been published in any
    technical forum, aggregator directory, or caster sourcetable. Access
    model not confirmed (free vs. registration vs. paid).
  - Academic assessment (J. Surveying Eng. 2026) documents only 2 operational
    CORS stations in the country prior to the ETCORS launch, covering ~6.6% of
    Ethiopia's area on a 70 km buffer — confirming the December 2025 launch as
    the real start of public infrastructure.
  - SSGI (`ssgi.gov.et`) is the agency to contact; `ethionsdi.gov.et` hosts
    the national SDI portal.
- **Volunteer**: none. Zero ET stations on rtk2go or Centipede.
- **Gap**: no confirmed public NTRIP for hobbyists as of April 2026. ETCORS
  is operational in a limited sense but endpoint is not publicly findable.
  Ethiopia's ~1.1 million km² requires roughly 200 stations for national RTK
  coverage; the current ~10 leave the vast majority of the country uncovered
  even once the endpoint is published.

### TZ — Tanzania

- **Free government RTK**: none confirmed. The **Survey and Mapping Division**
  (under the Ministry of Lands) operates geodetic control infrastructure and
  the Tanzania National Geo-innovation Centre (TNGC, `tngc.lands.go.tz`).
  TNGC lists "National Geodetic Networks" and "Observation of the National
  Control Points" among its services, but no NTRIP caster or real-time RTK
  streaming endpoint has been identified in any public source, aggregator
  directory, or technical forum.
  - Tanzania has CORS stations contributing to the AFREF continental reference
    frame and at least one IGS-affiliated tracking station. These are
    raw-observation archives only (post-processing); not hobbyist-accessible
    NTRIP.
  - EagleCORS (a commercial Ugandan provider) lists Tanzania as a future
    expansion target; no Tanzania stream is present in any public sourcetable.
- **Volunteer**: none. Zero TZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists anywhere in Tanzania. Tanzania's
  ~945,000 km² has no confirmed public CORS caster. The geodetic
  infrastructure that exists is internal-use, survey-grade, and not
  exposed over NTRIP to outside parties.

### UG — Uganda

- **Free government RTK**: **UGRF CORS** (Uganda Geodetic Reference Framework,
  Ministry of Lands, Housing & Urban Development / Surveys and Mapping Dept,
  `ugrf.mlhud.go.ug`) — 40 government CORS stations + 38 private stations
  integrated into the network (78 total). NTRIP via Leica GNSS Spider
  Business Center (`ugrf.go.ug/SBC`). Stated as free of charge ("absolutely
  free of charge with no payment required") as of 2024; fee implementation
  announced as a future possibility.
  - Registration: web account creation at ugrf.mlhud.go.ug → Spider Business
    Center; credentials (NTRIP username + password) emailed on approval.
  - Host:port: NTRIP caster hostname not publicly listed as a bare string in
    web search results; Spider Business Center provides the connection details
    after login. Single-base mountpoints include ENTB, GULU, SRTI, MBRA.
  - Network covers ~80% of Uganda; Phase I was 12 stations, current build-out
    40 government + 38 private stations. Network RTK (VRS) also available in
    addition to single-base.
  - 2024 national workshop confirmed ongoing expansion; service aligned to
    ITRF/Uganda Geodetic Reference Frame.
  - **Commercial parallel**: EagleCORS / EDAS (Eagle CORS Data Access Service,
    `eaglecors.com`) — 17+ stations in Uganda; commercial subscription;
    separate from UGRF. Not in scope.
- **Volunteer**: 1 station — MBAR00UGA0 (AUSCORS, Mbarara, -0.60°, 30.74°).
  This is a Geoscience Australia IGS station transmitting raw multi-GNSS
  observations under AUSCORS NULA; usable for RTK in principle but requires
  a short enough baseline. Free (AUSCORS non-commercial registration).
- **Gap**: UGRF is the only confirmed free government NTRIP in East Africa.
  The host:port is withheld until post-registration, making it a **deferred**
  candidate for the pipeline. Single-base RTK usable within ~30–40 km of each
  of the 40 government stations. Network (VRS) corrections available but
  polygon deferred.

### SD — Sudan

- **Free government RTK**: none confirmed. The **Sudan Survey Authority (SSA)**,
  established 1899 and one of Africa's oldest survey institutions, is the
  mandated agency for surveying, mapping, and charting. Published geodetic
  work (J. Surveying Eng.) shows SSA planning a GNSS CORS network as part of
  national ITRF infrastructure and AFREF participation, with 55 potential
  geodetic station sites identified. No operational NTRIP caster, host:port,
  or public RTK streaming service has been found in any public source.
  - Ongoing political instability (the conflict that began April 2023 between
    SAF and RSF has caused widespread infrastructure disruption) makes the
    near-term establishment of a functioning public CORS network uncertain.
  - No IGS or AFREF CORS station in Sudan currently appears in any public
    real-time sourcetable.
- **Volunteer**: none. Zero SD stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists anywhere in Sudan. The conflict since
  April 2023 has severely disrupted civil administration and infrastructure;
  even pre-conflict, no public NTRIP endpoint was identified. Do not pursue
  pipeline inclusion until political and infrastructure situation stabilises.

### MZ — Mozambique

- **Free government RTK**: none confirmed. **CENACARTA** (Centro Nacional de
  Cartografia e Teledetecção — National Cartography and Remote Sensing Centre)
  is the mapping authority. CENACARTA has at least one CORS station documented
  in the Corsmap Africa crowdsourcing initiative (Sofala station) and appears
  in AFREF continental reference literature, but no public NTRIP caster or
  real-time RTK streaming endpoint has been found.
  - Mozambique has ~25 CORS installations documented across the AFREF/Corsmap
    Africa dataset; these are internal-use reference monuments and research
    instruments, not hobbyist-accessible NTRIP streams.
  - No open-data geodesy mandate or RTK streaming policy has been identified.
- **Volunteer**: none. Zero MZ stations on rtk2go or Centipede. Four TrigNet
  South Africa stations (Nspt, Pbwa, Sprt, Tdou) are located near the
  Mozambique border but are South African government installations in
  Limpopo province — not Mozambican infrastructure. They are in pipeline via
  TrigNet and provide single-base RTK within ~30–40 km of each site for
  cross-border areas of southern Mozambique (Gaza/Maputo provinces), but this
  is incidental coverage, not a Mozambique service.
- **Gap**: no free RTK for hobbyists within Mozambique proper. Cross-border
  coverage from TrigNet is the only practical free option, and only for the
  southernmost provinces within range of those border stations.

---

## Proposed `docs/country-survey.md` entries

Insert after the existing **ZA — South Africa** entry, within the
**Middle East & Africa** section.

---

### ET — Ethiopia

- **Free government RTK**: nascent. ETCORS (SSGI, `ssgi.gov.et`) — ~10 stations
  launched December 2025 in Addis Ababa and six regional cities; aims for 30
  stations within 2 years, 200 for national coverage. Intended as free public
  service ("for Ethiopia and neighboring countries") but NTRIP host:port not
  yet publicly discoverable. Deferred.
- **Volunteer**: none. Zero ET stations on rtk2go or Centipede.
- **Gap**: no confirmed public NTRIP for hobbyists as of April 2026. Even once
  the endpoint is published, only ~6–7 stations serve Ethiopia's 1.1 million km²;
  coverage will be extremely sparse outside the capital and the handful of
  instrumented cities for the foreseeable future.

### TZ — Tanzania

- **Free government RTK**: none. Survey and Mapping Division / TNGC
  (`tngc.lands.go.tz`) operate national geodetic control; no public NTRIP caster
  found. AFREF/IGS contributions are raw-observation archives, not RTK streaming.
- **Volunteer**: none. Zero TZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists anywhere in Tanzania.

### UG — Uganda

- **Free government RTK**: UGRF CORS (Ministry of Lands, Housing & Urban
  Development, `ugrf.mlhud.go.ug`, 40 government + 38 private stations, VRS +
  single-base) — stated free as of 2024 ("absolutely free of charge"); web
  registration via Spider Business Center (`ugrf.go.ug/SBC`); host:port
  disclosed post-registration. Single-base mountpoints: ENTB, GULU, SRTI, MBRA.
  Deferred (endpoint withheld until post-registration).
- **Volunteer**: 1 AUSCORS station (MBAR00UGA0, Mbarara) via EarthScope/AUSCORS;
  raw observations under non-commercial NULA — functional for RTK within range.
- **Gap**: UGRF is the only confirmed free government NTRIP in East Africa but
  is not yet in pipeline (endpoint not publicly findable). EagleCORS (`eaglecors.com`)
  is a separate commercial service — out of scope.

### SD — Sudan

- **Free government RTK**: none. Sudan Survey Authority (SSA) planned a GNSS CORS
  network as part of AFREF participation (55 station sites identified) but no
  operational public caster has been found. Ongoing armed conflict (April 2023–)
  severely disrupts civil infrastructure; status unknown.
- **Volunteer**: none. Zero SD stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. Do not pursue until conflict ends and
  infrastructure is confirmed operational.

### MZ — Mozambique

- **Free government RTK**: none. CENACARTA (national mapping authority) has CORS
  stations in the AFREF/Corsmap continental dataset but no public NTRIP caster
  or RTK streaming endpoint found.
- **Volunteer**: none. Zero MZ stations on rtk2go or Centipede. Four TrigNet ZA
  stations near the Limpopo border (Nspt, Pbwa, Sprt, Tdou) are in pipeline via
  TrigNet and provide incidental single-base RTK coverage in southern Mozambique
  (Gaza/Maputo provinces) — not a Mozambique service.
- **Gap**: no free RTK for hobbyists within Mozambique proper. Southernmost
  provinces may benefit from nearby TrigNet coverage.

---

## Networks.md deferred entries

Two networks from this survey warrant a deferred entry in `docs/networks.md`:

### ugrf — UGRF CORS (UG)

**status**:    deferred
**host:port**: withheld until post-registration (Spider Business Center at `ugrf.go.ug/SBC`)
**type**:      physical-coord-vrs (single-base + VRS)
**access**:    free ("absolutely free of charge, no payment required" — ugrf.mlhud.go.ug);
               web registration at ugrf.mlhud.go.ug → Spider Business Center
**stations**:  40 (government); 78 total incl. 38 private stations integrated in network
**source**:    ugrf.mlhud.go.ug (Ministry of Lands, Housing & Urban Development,
               Surveys and Mapping Department)

Uganda Geodetic Reference Framework. Leica GNSS Spider software. Single-base
mountpoints include ENTB, GULU, SRTI, MBRA. Network RTK (VRS) also available.
~80% national coverage. ITRF-aligned reference frame. National workshop 2024
confirmed ongoing expansion; fee implementation mooted as future possibility
but not yet implemented. EagleCORS (`eaglecors.com`) is a separate commercial
service with ~17 stations — not in scope.

**missing**: NTRIP caster host:port — register at ugrf.mlhud.go.ug or contact
Surveys and Mapping Dept; check Spider Business Center after login; also search
Alberding EUPOS/African caster directories.

### etcors — ETCORS (ET)

**status**:    deferred
**host:port**: not yet publicly listed
**type**:      unknown (likely single-base initially)
**access**:    intended free public service; access model not confirmed
**stations**:  ~10 (as of December 2025 launch; targets 30 within 2 years, 200 long-run)
**source**:    ssgi.gov.et (Space Science and Geospatial Institute / SSGI);
               ethionsdi.gov.et (national SDI portal)

Ethiopia's first public CORS network, launched December 2025 by SSGI (successor
to ESSTI/EMA). Sites: Addis Ababa, Sheger, Bonga, Semera, Jigjiga, Debre Berhan,
Jimma. Prior to this launch, only 2 CORS were operational in the country, covering
~6.6% of Ethiopia's area on a 70 km buffer. Intended for Ethiopia, neighboring
countries, and global community per ENA state news agency. No NTRIP host:port
found in any public aggregator or technical forum as of April 2026.

**missing**: NTRIP caster host:port and access model — contact SSGI via ssgi.gov.et
or check Alberding African caster directory; search for "ETCORS" in GNSS forums
after mid-2026.
