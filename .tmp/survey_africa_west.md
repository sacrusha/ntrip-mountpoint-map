# Free RTK NTRIP — West/Central Africa survey (GH, CM, AO, CD, NE)

_Research for `docs/country-survey.md`. Findings based on local data search
(stations.json, all sourcetables, networks.md, global-survey.md) as of
2026-04-21. None of these five countries have stations in any current
sourcetable (rtk2go, Centipede, or any government network in pipeline).
Notes below cover what is known about government geodetic agencies, CORS
activity, and the gap picture for hobbyists and small shops._

_Last researched: 2026-04-21._

---

## Research summary

Across all five countries, the picture is uniform: **no free public NTRIP
caster exists, and no volunteer bases appear in any current sourcetable.**
The closest analogue is Nigeria's NIGNET (11–15 stations, far too wide for
RTK, no public caster), already documented in `docs/country-survey.md`.

Key structural constraints shared across the region:
- Geodetic CORS networks, where they exist, are operated under
  national surveying agencies or national mapping offices as internal
  infrastructure for cadastral and engineering work. Access is restricted
  to licensed surveyors or government institutions.
- No country in this group has enacted an open-data geodesy mandate or a
  public RTK streaming policy comparable to Brazil's Law No. 4/2011
  (InaCORS) or Colombia's Law 1955/2019 (IGAC).
- Station density, where networks exist, is far below RTK operational
  thresholds (~50 km baseline limit). Spacing of 300–800 km is typical
  for the handful of documented networks.
- Volunteer activity on rtk2go and Centipede is zero for all five
  countries (confirmed against all 50+ sourcetables cached in
  `data/*.sourcetable`).

---

## Middle East & Africa (extension)

### GH — Ghana

- **Free government RTK**: no confirmed public NTRIP endpoint.
  - **Survey and Mapping Division (Lands Commission / OASL)** — Ghana's
    national mapping authority. No public CORS network or NTRIP caster
    has been identified. A handful of CORS sites contributed to AFREF
    (African Reference Frame) and IGS tracking stations exist at Accra
    (NSRS/ACRA), but these are raw-observation archives only — not RTK
    streaming.
  - **Ghana Space Science and Technology Institute (GSSTI)** — operates
    Ghana's IGS station (NSRG); purely scientific, no NTRIP delivery
    to external users.
- **Volunteer**: none. Zero GH stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists anywhere in Ghana. The country's
  ~240,000 km² is served by at most a handful of CORS sites with
  baselines far exceeding RTK limits. No indication of an imminent
  public NTRIP launch.

### CM — Cameroon

- **Free government RTK**: no confirmed public NTRIP endpoint.
  - **Institut National de Cartographie (INC)** — national mapping
    authority; operates geodetic reference infrastructure. No public
    CORS network or NTRIP caster found. INC contributes to AFREF with
    a handful of monumented control points, but no streaming RTK service
    is documented.
  - **DORIS/IGS tracking stations** at Libreville vicinity (Gabon) and
    Douala are purely scientific archives, not hobbyist-accessible NTRIP.
- **Volunteer**: none. Zero CM stations on rtk2go or Centipede.
- **Gap**: no free RTK anywhere in Cameroon. Geography (dense rainforest
  basin, limited road infrastructure in east and south) would make a
  physical-coord VRS network expensive to build; no public-access policy
  identified.

### AO — Angola

- **Free government RTK**: no confirmed public NTRIP endpoint.
  - **Instituto Geográfico e Cadastral de Angola (IGCA)** — national
    mapping and cadastral agency. No public CORS network or NTRIP caster
    has been identified. Angola was rebuilding its geodetic infrastructure
    after the 1975–2002 civil war; GNSS CORS stations contributed to
    AFREF as part of post-conflict reconstruction, but no NTRIP delivery
    to external users has been documented.
  - Limited academic GNSS literature references reference stations in
    Luanda and Lubango; all are internal-use or research-only.
- **Volunteer**: none. Zero AO stations on rtk2go or Centipede.
- **Gap**: no free RTK anywhere in Angola. Large country (~1.25 million
  km²) with much of the interior sparsely instrumented. No policy
  pathway to public RTK identified.

### CD — DR Congo

- **Free government RTK**: no confirmed public NTRIP endpoint.
  - **Institut Géographique du Congo (IGC)** — national mapping
    authority; formally responsible for geodetic infrastructure. No
    public CORS network or NTRIP caster has been identified. DR Congo
    contributes a small number of stations to the AFREF continental frame,
    but network capacity and connectivity constraints in the country make
    continuous streaming RTK infrastructure very unlikely in the short
    term.
  - GNSS tracking sites referenced in scientific literature (Kinshasa,
    Lubumbashi, Kisangani) are internal or partner-agency research
    instruments, not hobbyist-accessible.
- **Volunteer**: none. Zero CD stations on rtk2go or Centipede.
- **Gap**: no free RTK anywhere in DR Congo. Second-largest country in
  Africa (~2.34 million km²); connectivity and power infrastructure
  constraints compound the policy gap. No indication of an imminent
  public NTRIP launch.

### NE — Niger

- **Free government RTK**: no confirmed public NTRIP endpoint.
  - **Institut Géographique National du Niger (IGNN)** — national
    mapping authority. No public CORS network or NTRIP caster has been
    found. Niger is one of the least instrumented countries for GNSS in
    the AFREF continental frame; a few IGS-affiliated stations exist
    but are research-only and not NTRIP-accessible.
  - The Saharan geography (landlocked, ~80% desert, severe power and
    connectivity constraints in the north) makes a distributed physical
    CORS network with RTK streaming capacity extremely difficult to
    sustain without sustained international funding.
- **Volunteer**: none. Zero NE stations on rtk2go or Centipede.
- **Gap**: no free RTK anywhere in Niger. The country's ~1.27 million
  km² has negligible GNSS infrastructure beyond a handful of research
  monuments. No policy pathway to public RTK identified.

---

## Proposed `docs/country-survey.md` entries

Insert after the existing **ZA — South Africa** entry, within the
**Middle East & Africa** section.

---

### GH — Ghana

- **Free government RTK**: none. Survey and Mapping Division (Lands
  Commission) and GSSTI operate a handful of IGS/AFREF reference sites
  (Accra); raw-observation archives only — no NTRIP streaming.
- **Volunteer**: none. Zero GH stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Ghana.

### CM — Cameroon

- **Free government RTK**: none. Institut National de Cartographie (INC)
  manages geodetic infrastructure; no public CORS caster found. AFREF
  contributions are raw archives, not streaming RTK.
- **Volunteer**: none. Zero CM stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Cameroon.

### AO — Angola

- **Free government RTK**: none. Instituto Geográfico e Cadastral de
  Angola (IGCA) is rebuilding post-conflict geodetic infrastructure;
  AFREF reference sites exist but are internal/research-only — no
  public NTRIP delivery.
- **Volunteer**: none. Zero AO stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Angola.

### CD — DR Congo

- **Free government RTK**: none. Institut Géographique du Congo (IGC)
  formally responsible for geodesy; limited AFREF contributions. No
  public CORS caster found; connectivity and power constraints make
  continuous RTK streaming very unlikely near-term.
- **Volunteer**: none. Zero CD stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in DR Congo.

### NE — Niger

- **Free government RTK**: none. Institut Géographique National du
  Niger (IGNN) is responsible for geodesy; sparse IGS-affiliated
  research stations only — no public NTRIP delivery. Saharan geography
  and infrastructure constraints make a sustained physical RTK network
  very difficult.
- **Volunteer**: none. Zero NE stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. No confirmed public CORS network
  or NTRIP caster anywhere in Niger.
