# Free RTK NTRIP — multi-country and global networks

_Landscape context for networks that span more than one country or operate as
a global service. Answers: what is it, who runs it, where does it cover, what
is the access model, and is it in scope?_

_Technical detail (endpoints, credentials, pipeline status) lives in
`docs/networks.md`. Per-country analysis of how these networks contribute
to national coverage lives in `docs/country-survey.md`. Network references
use the pattern `→ networks.md: \`id\`` at the end of the relevant bullet —
preserving this exact form lets you audit coverage with
`grep "networks.md:" docs/global-survey.md`._

_Last updated: 2026-04-20._

---

## Community volunteer aggregators

### RTK2GO (global)

Operated by SNIP / use-snip.com (USA) as a free community service. Volunteer
base station owners push streams to a shared caster; any rover can pull any
stream. No commercial restrictions; no account needed for rovers. Dense in USA,
western Europe, Japan, and Australia; sparse in Africa, Central Asia, and Latin
America. Quality and uptime vary widely — hardware ranges from survey-grade to
hobbyist DIY. `NEAR` mountpoint auto-routes to nearest base from rover's NMEA
GGA. Regional country-filtered views (Poland `:2103`, Japan `:2104`) are the
same server — not separate endpoints. → networks.md: `rtk2go`

### CentipedeRTK (global, France-centric)

Initiated by INRAE (France, 2019); now operated by the non-profit
Centipede-RTK association (formed Aug 2024). Fully open-source stack (Millipede
caster, BSD-3). Originally France-centric; now 30+ countries. Densest coverage
in France (~719 mainland volunteer bases), but significant presence in Hungary
(~223 nodes — single largest non-France country), UK (~43), Finland (~14), and
many other countries. All known nodes, including DOM-TOM territories, feed through
`crtk.net` via Millipede federation — no separate country-specific instances.
Fully open; no commercial restriction. → networks.md: `centipede`

---

## Multi-country government networks

### EarthScope NOTA (Americas)

Operated by EarthScope Consortium (merger of UNAVCO + IRIS, 2023). Geophysical
sensor network spanning 20+ countries in the Americas. Dense in western USA;
thinner in Mexico, Caribbean, and South America. Free for non-commercial,
scientific, educational, or humanitarian use under annual NULA. Commercial use
requires per-seat licensing. Hobbyist and small-shop use confirmed in scope.
Legacy UNAVCO platform retired 2025-07-29; all users must migrate to
`ntrip.earthscope.org`. → networks.md: `earthscope`

### FReDNet (IT + SI + AT)

Operated by OGS (Istituto Nazionale di Oceanografia e Geofisica Sperimentale,
Trieste). Crustal-deformation science network for Friuli-Venezia Giulia (NE
Italy), with coverage extending into Slovenia and western Austria. Free with
email registration. Included here because it serves rovers across three countries.
→ networks.md: `frednet`

---

## Out of scope — raw observation broadcasters

Documented here to prevent re-investigation.

### EUREF-IP / EPN (Europe)

Operated by BKG (Germany) with mirrors at ROB (Belgium) and ASI (Italy).
Broadcasts raw GNSS observations from the EUREF Permanent Network. Explicitly
not suitable for real-time kinematic positioning — no RTK or VRS streams.
Useful for PPP post-processing and monitoring. Free with registration. **Out of scope.**

### IGS-IP / products.igs-ip.net (global)

Operated by BKG on behalf of the International GNSS Service. `igs-ip.net`
broadcasts raw observations from the IGS global network (research/PPP only).
`products.igs-ip.net` provides IGS Real-Time Service SSR corrections — enables
PPP, not RTK; requires PPP-capable receiver. Hobbyists wanting free global
corrections should use Galileo HAS instead. **Both out of scope.**

---

## Paid global services

Documented for UI fallback context (sparse-coverage areas).

### GEODNET (global)

Decentralised Physical Infrastructure Network (DePIN) operated by HYFIX.AI.
20,000+ nodes across 153 countries; full-constellation triple-frequency.
Paid after 30-day free trial ($40/month). Seasonal use (4 months = $160) is
under the $200/yr affordability cutoff. Four regional AWS servers (USA, EU,
Australia, S. America) all on port 2101. Added to pipeline to test whether
the sourcetable is publicly accessible without auth — if so, stations can be
displayed as a paid-service layer. → networks.md: `geodnet_*`

### Emlid Caster

Point-to-point relay for a single user's own base station and their rovers.
Not a shared public network; no sourcetable to parse. Not applicable.

### RTKdata.online / RTKdata.com

RTKdata.com is a paid aggregator (Kansi Solutions GmbH). RTKdata.online was
presented as a free companion but visually reused rtk2go/Centipede data with
no independent value. Removed from pipeline 2026-04-20: server unreachable
since launch, 0 stations ever collected. → networks.md: `rtkdata_online` (rejected)
