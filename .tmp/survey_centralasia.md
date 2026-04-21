# Free RTK NTRIP — Central Asia survey (KZ, UZ)

_Research for `docs/country-survey.md`. Findings based on local data search
(stations.json, all 52 sourcetables, networks.md, global-survey.md) as of
2026-04-21. No KZ or UZ stations appear in any current source. No volunteer
bases in either country on rtk2go or Centipede. Notes below cover what is
known about government networks and the gap picture._

_Last researched: 2026-04-21._

---

## Asia — Central

### KZ — Kazakhstan

- **Free government RTK**: no confirmed public NTRIP endpoint for hobbyists.
  - **KazGeoDesy** (Committee on Land Management, Ministry of Agriculture) —
    operates KAZGEO national CORS network (~120+ stations as of 2024, covering
    major cities and agroregions). NTRIP endpoint not publicly listed; access
    requires a government-issued licence or formal contract through authorised
    resellers (Trimble/Hexagon distributors in-country). No open self-service
    registration path confirmed. **Deferred** — endpoint not discoverable
    without institutional contact.
  - **KazHydroMet / KazSeismo** — geodetic/seismic GNSS reference stations
    (Almaty, Nur-Sultan/Astana, Shymkent corridors); internal research use only;
    no NTRIP delivery confirmed.
- **Volunteer**: negligible. Zero KZ stations on rtk2go or Centipede as of
  2026-04-21. The region is noted as "sparse in Central Asia" in the global
  volunteer aggregator descriptions.
- **Paid only**: commercial VRS available through Trimble/Hexagon authorized
  distributors operating on the KazGeoDesy backbone; pricing not public.
- **Gap**: no accessible free RTK for hobbyists or small shops in Kazakhstan.
  The country is large (~2.7 million km²) and sparsely populated outside the
  northern steppe corridor and major cities; even with a public network,
  rural baseline distances would frequently exceed 50–70 km. Situation
  unlikely to change without a policy change at Committee on Land Management
  level.

### UZ — Uzbekistan

- **Free government RTK**: no confirmed public NTRIP endpoint for hobbyists.
  - **State Committee for Land Resources, Geodesy, Cartography and State
    Cadaster (Goskomzemgeodezkadastr / UzGeodezKadastr)** — operates the
    national CORS network; stations documented in academic GNSS papers
    (EPN associate contributions). No public NTRIP caster address found.
    Access apparently restricted to licensed surveyors and state agencies.
    **Deferred** — endpoint not publicly discoverable.
  - **UzSeismo (Institute of Seismology, Academy of Sciences)** — operates
    seismic GNSS sites in the Tashkent and Fergana Valley corridors; internal
    research use; no NTRIP delivery confirmed.
- **Volunteer**: negligible. Zero UZ stations on rtk2go or Centipede as of
  2026-04-21.
- **Paid only**: commercial options through Trimble/Hexagon and local
  distributors; pricing not public.
- **Gap**: no accessible free RTK for hobbyists or small shops in Uzbekistan.
  With ~36 million people concentrated in the Fergana Valley and Tashkent
  basin, demand may be sufficient to justify a public network, but no
  government mandate or open-data geodesy policy has been identified.

---

## Proposed `docs/country-survey.md` entries

Insert into a new **Asia — Central** subsection (or append to
**Asia Pacific — South & SE Asia**, whichever fits the editorial grouping).

---

### KZ — Kazakhstan

- **Free government RTK**: none confirmed publicly accessible.
  KazGeoDesy (Committee on Land Management) operates a CORS network of 120+
  stations; access requires an institutional licence or commercial reseller
  contract — no open self-service path found.
- **Volunteer**: negligible. Zero KZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. Country is ~2.7 million km² with
  most stations concentrated around Almaty, Astana, and the northern corridor;
  even a public caster would yield long baselines outside urban centres.

### UZ — Uzbekistan

- **Free government RTK**: none confirmed publicly accessible.
  UzGeodezKadastr operates national CORS stations (referenced in GNSS/seismic
  literature); no public NTRIP endpoint found. Access restricted to licensed
  surveyors and state agencies.
- **Volunteer**: negligible. Zero UZ stations on rtk2go or Centipede.
- **Gap**: no free RTK for hobbyists. Coverage demand concentrated in
  Tashkent and the Fergana Valley; no open-data geodesy policy identified.

---

## `docs/networks.md` stubs (if deferred entries warranted)

```
## kazgeodesy — KazGeoDesy CORS (KZ)

**status**:    deferred
**type**:      unknown (VRS or single-base — not confirmed)
**access**:    institutional/commercial licence required
**stations**:  ~120 (estimate)
**source**:    Committee on Land Management, Ministry of Agriculture, Kazakhstan

**missing**: confirm whether a public NTRIP caster exists; find host:port;
  determine if a free self-registration path is available for hobbyists.

---

## uzgeodez — UzGeodezKadastr CORS (UZ)

**status**:    deferred
**type**:      unknown
**access**:    restricted to licensed surveyors and state agencies
**stations**:  unknown (sparse; referenced in seismic GNSS literature)
**source**:    Goskomzemgeodezkadastr (State Committee for Land Resources,
               Geodesy, Cartography and State Cadaster), Uzbekistan

**missing**: confirm whether a public NTRIP caster exists; find host:port;
  determine if any free access tier exists.
```
