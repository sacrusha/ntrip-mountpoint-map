# Free RTK NTRIP — multi-country and global networks

_Landscape context for networks spanning more than one country. Describes
what each network is, who it serves, and access model. Technical details
(endpoints, credentials, station counts) → `docs/networks.md`._

_Last updated: 2026-04-20._

---

## Community volunteer aggregators

### RTK2GO

Operated by SNIP / use-snip.com (USA) as a free community service. Volunteer
base station owners push streams to a shared caster; any rover can pull any
stream. No commercial restrictions. Dense in USA, western Europe, Japan, and
Australia; sparse in Africa, Central Asia, and Latin America. Quality and
uptime vary widely — volunteer hardware ranges from survey-grade to hobbyist.
No account needed for rovers.

Regional country-filtered views exist (Poland, Japan) on separate ports — same
server, no latency benefit. See networks.md for connection details.

### Centipede-RTK

Initiated by INRAE (France) in 2019; now operated by the non-profit
Centipede-RTK association (formed Aug 2024). Fully open-source stack
(Millipede caster, BSD-3). Originally France-centric; now 30+ countries with
dense France coverage. Fully open, no commercial restriction. All known nodes
including DOM-TOM feed through a single caster via Millipede federation — no
separate country-specific instances found.

### GeoRTK

Japan-only volunteer caster operated by Geosense Co., Ltd. Domestic
alternative to rtk2go for Japan. Open rover access, no registration. Free
indefinitely (1-year advance notice if policy changes). Sourcetable has
shrunk over time; a portion of entries report 0/0 coordinates (offline bases).

---

## Government networks spanning multiple countries

### SAPOS — Germany

Each of Germany's 16 Bundesländer runs its own SAPOS caster. Most states
free for all uses. Bayern charges €20/yr for non-agricultural use (free for
agriculture) — under the project's $200/yr affordability cutoff. Sachsen (SN)
endpoint now confirmed. All 16 states now in pipeline. Sourcetables publicly
readable; streams require per-state registration. VRS network — sourcetables
expose physical station coordinates for most states; some states report a
single coordinate for all virtual mountpoints and produce 0 map stations.

---

## Scientific raw-observation broadcasters

These casters are **out of scope**. Recorded here to prevent
re-investigation.

### EUREF-IP / EPN

Operated by BKG (Germany) with mirrors at ROB (Belgium) and ASI (Italy).
Broadcasts raw GNSS observations from the EUREF Permanent Network. Explicitly
not suitable for real-time kinematic positioning — no RTK or VRS streams.
Useful for PPP post-processing and monitoring. Free with registration.
ROB mirror carries identical streams; same ruling.

### IGS-IP / products.igs-ip.net

Also operated by BKG on behalf of the International GNSS Service.
igs-ip.net: raw observations from the IGS global network — research/PPP only.
products.igs-ip.net: IGS Real-Time Service SSR corrections — enables PPP,
not RTK; requires PPP-capable receiver. Both out of scope.
Hobbyists wanting free global corrections should use Galileo HAS instead.

---

## Paid global correction services

Recorded for reference. Affordable paid services (under $200/yr cutoff)
are worth surfacing in the UI as fallback options for users with no free
coverage nearby.

### GEODNET

Decentralised Physical Infrastructure Network (DePIN) operated by HYFIX.AI.
20,000+ nodes across 153 countries; full-constellation triple-frequency.
Paid after 30-day free trial. At $40/month, seasonal use (4 months = $160)
falls under the $200/yr affordability cutoff. Added to pipeline to test
whether the sourcetable is publicly accessible without auth. If readable,
station locations can be displayed as a paid-service layer.

### Emlid Caster

Point-to-point relay for a single user's own base and rovers. Not a shared
public network. No sourcetable to parse. Not applicable.

### RTKdata.com / RTKdata.online

RTKdata.com is a paid aggregator. RTKdata.online was a free companion that
visually reused rtk2go/Centipede data with no independent value. Removed
from pipeline 2026-04-20 — server unreachable since launch, 0 stations
collected.

---

## EarthScope NOTA — Americas

Operated by EarthScope Consortium (merger of UNAVCO + IRIS). Geophysical
sensor network spanning 20+ countries in the Americas. Dense in western USA;
thinner in Mexico, Caribbean, and South America. Free for non-commercial,
scientific, educational, or humanitarian use under annual NULA. Commercial
use requires per-seat licensing. Hobbyist and small shop use confirmed in
scope. UNAVCO legacy platform retired 2025-07-29.

---

## FReDNet — NE Italy / cross-border

Operated by OGS (Istituto Nazionale di Oceanografia e Geofisica Sperimentale).
Crustal-deformation science network for Friuli-Venezia Giulia; coverage
extends into Slovenia and W Austria. Free with email registration.
Included here (rather than country survey) because it serves rovers across
three countries.

---

## Resolved questions

1. **EarthScope NULA:** ✓ Non-commercial project confirmed in scope.
2. **GEODNET affordability:** ✓ $40/mo × 4 months = $160 < $200/yr cutoff.
   Testing sourcetable accessibility. UI fallback note for sparse-coverage areas.
3. **Centipede non-France coords:** ✓ Non-issue. 485/1203 international
   stations all have valid coordinates in live data.
4. **rtk2go regional sub-casters:** ✓ Filtered views, same server. Not
   separate SOURCES. Plan: dual-mountpoint display for matching country stations.
5. **EUREF-IP / EPN RTK:** ✓ Confirmed no RTK streams. Raw observations only.
6. **Separate Millipede instances:** ✓ None found. All nodes via crtk.net
   federation. DOM-TOM present (4 Réunion stations). Caribbean not yet deployed.
