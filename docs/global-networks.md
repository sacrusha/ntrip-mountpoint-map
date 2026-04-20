# Free RTK NTRIP — multi-country and global networks

_Purpose: companion to `country-survey.md`. Covers networks whose sourctable
spans more than one country, volunteer aggregators, scientific raw-data
broadcasters, and PPP/SSR correction services. Each entry records: what it is
· endpoint · free/paid status · registration path · pipeline status · gotchas._

_Last updated: 2026-04-20._

---

## 1. Community volunteer aggregators

### RTK2GO (`rtk2go.com:2101`)

Operated by **SNIP / use-snip.com** (USA) as a free community service running
SNIP Pro software. Volunteer base station owners push their streams to the
caster; any rover can pull any stream. No commercial backing; operators absorb
the SNIP Pro cost.

- **Scale (Apr 2026):** 800+ simultaneous active streams; 10,000+
  registered mountpoints; 250,000+ registered users; 150,000–250,000
  connections/day; 5–20 GB/day served; ~400 million total sessions.
- **Geographic spread:** Global. Dense in USA, western Europe, Japan, and
  Australia. Sparse in Africa, Central Asia, and Latin America outside
  Brazil/Argentina. Station quality and uptime vary widely — volunteer
  hardware ranges from survey-grade to Raspberry Pi + patch antenna.
- **Protocol / formats:** NTRIP 1.0 and 2.0; RTCM 3.x MSM dominant; some
  RTCM 2.x legacy streams still present.
- **Rover credentials:** Username = any valid email address; Password =
  `none` (leave blank). No account creation required.
- **NEAR mountpoint:** SNIP Pro feature. Rover connects to mountpoint
  `NEAR` and sends a NMEA `$GGA` sentence; caster routes to the nearest
  active base. Requires client to send GGA — most modern receivers do so
  automatically. `NEAR4` is a legacy-compatible variant for older
  proprietary displays (John Deere, etc.).
- **Base station registration:** Required for operators (not rovers).
  Register unique mountpoint name at rtk2go.com. Instant; free.
- **TOS:** Free for all uses (no commercial restriction stated). Base
  station operators agree not to stream copyrighted/restricted data.
- **Pipeline status:** **In pipeline.** `id: rtk2go`, URL
  `http://rtk2go.com:2101/`. Carrier-inference fallback active (see
  CLAUDE.md gotchas) — most rtk2go entries have a blank carrier field
  despite broadcasting RTCM 3.x MSM.
- **Regional sub-casters:** rtk2go exposes country-filtered views on
  separate ports: `:2103` (Poland), `:2104` (Japan). Same US server,
  same station set — no latency benefit, just a smaller sourcetable.
  Not added as separate SOURCES (would duplicate stations). Popup UI
  should surface the regional port as a secondary connection option for
  stations whose country code matches, using the dual-mountpoint display.
- **Gotcha:** Mountpoint churn is high — volunteer bases go offline
  frequently. Fingerprint-based idempotency check catches this correctly.
  The `NEAR` mountpoint itself appears in the sourcetable as a synthetic
  STR entry; the parser drops it (0/0 coords) correctly.

### Centipede-RTK (`crtk.net:2101`)

Initiated by **INRAE** (French national agricultural research institute) in
2019; now operated by the **Centipede-RTK association** (non-profit, France,
formed Aug 2024). Fully open-source stack: Millipede NTRIP caster (BSD-3)
+ open hardware base station designs + ODbL-licensed station database.
Partnership with Packet Clearing House (PCH) for global expansion.

- **Scale (Feb 2025):** 1,485+ bases total — 625 in mainland France,
  860 across 30 countries. Dense coverage in France (most areas within
  20 km of a base). Growing clusters in Senegal, Serbia, UK, Ireland,
  Norway, Denmark, and Canada.
- **Geographic spread:** Originally France-centric; now actively
  internationalising. French overseas territories (DOM-TOM) included:
  4 Réunion stations confirmed in main sourcetable. Volunteer quality
  comparable to rtk2go.
- **Separate Millipede instances:** None confirmed. Millipede supports
  federation/proxy to merge sourcetables from regional deployments, but
  all known nodes (including DOM-TOM and international clusters) appear
  in the single `crtk.net:2101` sourcetable. No independent country-
  specific caster hostnames found. Non-ISO country codes in sourcetable
  (ENG, CHZ, SER, DAN, ROM) are quirks of Centipede's registration form,
  not separate deployments.
- **Protocol / formats:** NTRIP 1.0 and 2.0; RTCM 3.x MSM.
- **Rover credentials:** Username = `centipede` (or `c`); Password =
  `centipede` (or `c`). `NEAR` requires NMEA GGA from rover; `NEAR4`
  for older proprietary displays.
- **Base station registration:** Operators register via centipede-rtk.org.
  Open documentation guides DIY setup (Raspberry Pi + u-blox F9P or
  equivalent).
- **TOS:** Fully open, no commercial restriction. Station database ODbL;
  documentation CC BY-SA 4.0.
- **Migration (2025-03-18):** Moved from `caster.centipede.fr:2101` to
  `crtk.net:2101`. Old host is dead.
- **Pipeline status:** **In pipeline.** `id: centipede`, URL
  `http://crtk.net:2101/`. Comment in `SOURCES` records migration date.
- **Gotcha:** Like rtk2go, volunteer bases go offline. NEAR requires GGA.

### GeoRTK (`geortk.jp:2101`)

Operated by **Geosense Co., Ltd.** (株式会社ジオセンス), a Tokyo-based
geospatial tech company. Japan-only volunteer caster analogous to rtk2go,
running BKG Professional NtripCaster software. Launched as a domestic
alternative for when rtk2go is unreachable from Japan.

- **Scale:** ~338 STR lines in sourcetable; ~200 have valid (non-zero)
  coordinates; ~130–140 active at any given time. Japan only.
- **Protocol / formats:** RTCM 3.x MSM.
- **Rover credentials:** None required. Connect to `geortk.jp:2101` and
  select a mountpoint from the list at geortk.jp/mountpoint.
- **Base station registration:** Operators must register and apply for
  a mountpoint. Rover access is open (no registration).
- **Free status:** Confirmed free indefinitely. Geosense has stated 1-year
  advance notice if the policy changes.
- **TOS:** Free for all uses; data provided as-is.
- **Pipeline status:** **In pipeline.** `id: geortk`, URL
  `http://geortk.jp:2101/`. Parser drops ~130 entries with 0/0 coords
  (these are registered but currently offline bases).

---

## 2. Government networks spanning multiple countries

### SAPOS — Germany (13 state casters)

Each of Germany's 16 Bundesländer runs its own SAPOS caster; the
Zentrale Stelle SAPOS (ZSS) coordinates standards but does not operate a
single unified caster. The pipeline ingests 13 confirmed free state
casters (SN — Sachsen — omitted, endpoint unconfirmed).

- **Hosts:** State-specific subdomains, e.g. `sapos-bw-ntrip.de:2101`,
  `sapos-th-ntrip.de:2101`, etc. See `SOURCES` in
  `scripts/fetch_stations.py` for all 13.
- **Scale:** ~270 stations total across all 16 Bundesländer; VRS network.
- **Free status:** Most states free for all uses; Bayern (BY) ~€20/yr;
  Rheinland-Pfalz (RP) has commercial tiers. All require per-state web
  registration.
- **Protocol / formats:** RTCM 3.x; VRS (HEPS ~1–2 cm), EPS (~0.3–0.8 m).
  Also a federal SSRZ stream via `bkg1.positioning-service.net:2101`
  (PPP-RTK, requires SSR-capable receiver or Geo++ SSR2OBS — not
  suitable for standard hobby receivers; see country-survey.md DE entry).
- **Pipeline status:** **In pipeline** (sapos_SH_HH, sapos_NI, sapos_NW,
  sapos_HE, sapos_RP, sapos_BW, sapos_BY, sapos_SL, sapos_BE, sapos_BB,
  sapos_MV, sapos_LSA, sapos_TH). Sourcetables publicly readable;
  streams require per-state credentials (not fetched by the pipeline).

---

## 3. Scientific raw-observation broadcasters

These casters provide raw GNSS observations (code + carrier phase) for
scientific use. They are **not suitable for direct rover RTK use**
because: (a) station reference coordinates are not guaranteed correct
for real-time positioning; (b) baselines to European or global fiducial
stations are typically 100–2,000 km — far too long for RTK; (c) the
casters themselves state this limitation explicitly. They are useful for
PPP post-processing (RTKLIB, CSRS-PPP) and monitoring apps. Included
here for completeness and as a "why this map doesn't show them" record.

### EUREF-IP (`euref-ip.net:2101`, also `:443` TLS)

Operated by **BKG** (Bundesamt für Kartographie und Geodäsie, Germany),
with mirror casters at ROB (Belgium) and ASI (Italy). Backbone of the
EUREF Permanent GNSS Network (EPN).

- **Scale:** ~608 streams; ~2,500 registered users from 96 countries;
  ~8,500 simultaneous accesses.
- **Data type:** Raw GNSS observations (RTCM 3.x). No RTK/VRS stream.
  **Explicitly not suitable for real-time kinematic positioning.**
- **Registration:** Free; online form at `register.rtcm-ntrip.org`
  (same form covers euref-ip.net, igs-ip.net, products.igs-ip.net).
  Manual approval during business hours; short description of use
  required.
- **Coverage:** Primarily Europe; some global partner stations.
- **Pipeline status:** **Out of scope** for this map. No RTK streams.
  Included here so future contributors don't re-investigate.

### IGS-IP and products.igs-ip.net

Also operated by **BKG** on behalf of the International GNSS Service.

- **igs-ip.net:2101** — raw GNSS observations from the IGS global
  network (~500 stations). Same registration as EUREF-IP. Not suitable
  for RTK; research/PPP use only.
- **products.igs-ip.net:2101** — IGS Real-Time Service (RTS) SSR
  corrections (satellite orbit + clock + bias corrections in RTCM-SSR
  format). Mountpoints follow naming convention `SSRX00XXXF` (e.g.
  `SSRA00IGS0`). Enables real-time PPP (not RTK). Accuracy ~5–10 cm
  (orbit/clock only) to ~3 cm (with ionosphere corrections, multi-
  constellation). Requires PPP-capable receiver or software (BNC, RTKLIB
  PPP mode). **Out of scope for this map** (target accuracy >50 cm with
  standard receivers; PPP convergence ~5–20 min, not instant like RTK).
  Included here for reference; hobbyists should see Galileo HAS instead.
- **Registration:** Same form at `register.rtcm-ntrip.org`.

---

## 4. Paid global correction services (drop — recorded for reference)

### GEODNET (`ntrip.geodnet.com:2101`)

Decentralised Physical Infrastructure Network (DePIN) operated by
**HYFIX.AI** / Geodnet Foundation. Blockchain-based (Polygon / GEOD
token): station operators earn GEOD tokens for contributing data;
subscribers pay for RTK corrections.

- **Scale (Dec 2025):** 20,000+ active nodes across 153 countries;
  triple-frequency, full-constellation (GPS+GLO+GAL+BDS+QZSS).
- **Accuracy:** 1 cm + 1 ppm (VRS/network RTK).
- **Free tier:** 30-day free trial (full access). After trial:
  $40/month or $400/year via HYFIX.AI resellers. No ongoing free tier.
- **TOS:** Paid subscription required for continued use. Token-earning
  model for base station operators.
- **Paid source cutoff:** This project uses a cutoff of **< $200/year**
  for typical hobbyist usage (< 4 months/year, < 90 hours/year), using
  yearly pricing unless monthly is massively cheaper for that pattern.
  GEODNET: $400/year exceeds the cutoff. Monthly at $40 × 4 months =
  $160 < $200 — qualifies seasonally. Worth surfacing in a "paid
  alternatives" banner note for users in areas with sparse free coverage.
- **Pipeline status:** **DROP — not fetched.** No public sourcetable
  without an active subscription. GEODNET's dense global coverage makes
  it the best paid fallback; mention it in the UI for users whose area
  has no free sources within 50 km.

### Emlid Caster (`caster.emlid.com`)

Private caster service operated by **Emlid Ltd.** for relaying base→rover
corrections between a single user's own devices. Not a public shared
network of community bases.

- **Purpose:** Point-to-point relay (one base, up to 5 rovers) for
  Emlid Reach receivers and any other NTRIP-compatible device.
- **Free tier:** Free for personal use. No community base station
  sourcetable to parse; no shared mountpoints.
- **Pipeline status:** **Not applicable** — no public sourcetable.

### RTKdata.com / RTKdata.online

**RTKdata.com** is a paid correction aggregator (~$40/month) run by
Kansi Solutions GmbH (DE). **RTKdata.online** was their free-tier
companion site that visually aggregated rtk2go/Centipede stations with
no independent data. Removed from the pipeline 2026-04-20 (server
unreachable since launch; 0 stations ever collected; adds no value over
directly ingesting rtk2go and Centipede).

---

## 5. EarthScope NOTA — Americas multi-country network

### EarthScope NOTA (`ntrip.earthscope.org:2101`)

Operated by **EarthScope Consortium** (merger of UNAVCO + IRIS, USA).
Network of the Americas (NOTA) — geophysical sensor network spanning
20+ countries.

- **Scale:** 1,200+ continuously operating stations; ~1,000 with
  real-time GNSS streams. Dense coverage in western USA; thinner in
  Mexico, Caribbean, and South America.
- **Formats / ports:**
  - `:2101` — raw RTCM 3.3 MSM (for RTK rover use)
  - `:2105` — raw BINEX (research)
  - `:2108` — onboard PPP solutions
- **Free status:** Free for non-commercial, scientific, educational,
  or humanitarian use under annual NULA (Non-commercial User License
  Agreement). Commercial use requires per-seat licensing.
- **Registration:** Annual NULA renewal at earthscope.org/data/gnss-
  realtime/. Automated; confirms non-commercial intent.
- **Legacy:** UNAVCO platform fully retired 2025-07-29. All users
  must use `ntrip.earthscope.org`.
- **TOS caveat:** "Non-commercial" — hobbyist and small shop use is
  within scope of this map's target audience; commercial surveying
  firms need a paid seat. The map should note this restriction.
- **Pipeline status:** **Candidate — registration required.** This
  project is non-commercial; the NULA confirmed in scope. Obtain
  credentials and store as GitHub Actions secret to activate ingestion.

---

## 6. FReDNet — Italy (NE / cross-border)

### FReDNet (`gnsscaster.regione.fvg.it:8080`)

Operated by **OGS** (Istituto Nazionale di Oceanografia e Geofisica
Sperimentale) / Centro di Ricerche Sismologiche. Primarily a crustal-
deformation science network for Friuli-Venezia Giulia; also covers
the Slovenia and Austria border zone.

- **Scale:** 16 stations; VRS (network RTK).
- **Sourcetable:** Publicly readable (no auth). 39 STR lines confirmed.
  Streams: free with email registration.
- **Registration:** Email `rete.gnss.marussi@regione.fvg.it`. Free;
  no approval delay reported.
- **Pipeline status:** **In pipeline.** `id: frednet`. Sourcetable
  fetch confirmed working. Stream credentials are not required for the
  sourcetable fetch; station metadata captured for display without
  stream access.
- **Why included here:** Crosses into cross-border territory (stations
  in FVG serve rovers in NE Italy, Slovenia, and W Austria) making it
  a regional rather than purely national network.

---

## 7. Resolved questions (global networks)

1. **EarthScope NOTA NULA + automated fetch:** ✓ Closed. This project
   is non-commercial; the NULA covers non-commercial, educational, and
   humanitarian use. Automated sourcetable fetch for metadata display
   is within scope. Activate by obtaining credentials and adding as
   GitHub Actions secret.

2. **GEODNET affordability:** ✓ Closed. Paid source cutoff set at
   < $200/year for < 4 months / < 90 hours annual use (monthly pricing
   applies when massively cheaper than yearly). GEODNET at $40/month
   × 4 months = $160 qualifies as an affordable seasonal fallback.
   Not in pipeline (no public sourcetable). Surface as a "paid
   alternative" in the UI for areas with no free sources within 50 km.

3. **Centipede non-France station coords:** ✓ Closed — non-issue.
   Verified from live data: 485 of 1,203 centipede stations are non-
   France; all have valid (non-zero) coordinates. No GeoRTK-style
   0/0 offline-base problem in the international nodes.

4. **rtk2go regional sub-casters:** ✓ Closed. Confirmed filtered views
   on the same US server: `:2103` Poland, `:2104` Japan. No latency
   benefit; just a smaller sourcetable. Do NOT add as separate SOURCES.
   Plan: popup dual-mountpoint display should offer the regional port as
   a secondary connection option for stations whose country code matches.

5. **EUREF-IP / EPN RTK capability:** ✓ Closed — confirmed no RTK.
   EPN broadcasts raw GNSS observations only; operators explicitly state
   "not suitable for real-time kinematic positioning". ROB mirror
   (euref-ip.be:2101) carries the same streams — same out-of-scope
   ruling. Multiple independent sources agree; no conflicting evidence.

6. **Separate Millipede instances / Centipede DOM-TOM:** ✓ Closed.
   No independent country-specific Millipede instances found. Millipede
   uses federation/proxy to aggregate regional deployments into the main
   `crtk.net` sourcetable. DOM-TOM confirmed present: 4 Réunion (REU)
   stations visible in live data. Caribbean territories not yet in
   sourcetable — likely not yet deployed, not a separate caster.

---

## Pipeline status summary (global networks)

| Status | Network |
|---|---|
| **In pipeline** | rtk2go, Centipede-RTK, GeoRTK (JP), FReDNet (IT), SAPOS ×13 (DE) |
| **Candidate — registration required** | EarthScope NOTA (US/Americas; non-commercial NULA confirmed in scope) |
| **Out of scope — scientific raw obs** | EUREF-IP, IGS-IP, products.igs-ip.net (confirmed no RTK) |
| **Paid — mention as fallback** | GEODNET ($40/mo; $160 for 4-month season < $200 cutoff — no pipeline, UI note only) |
| **Paid — not applicable** | Emlid Caster (point-to-point relay, no shared sourcetable) |
| **Removed** | RTKdata.online (server unreachable; no independent data) |

