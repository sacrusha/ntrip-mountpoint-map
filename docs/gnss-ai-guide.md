# GNSS / RTK / NTRIP — AI Reference Guide

> **Audience:** future AI sessions working on this codebase.  
> **Depth:** one level below product UX — enough to reason about pipeline
> decisions, data quality, and user support answers without being a
> firmware engineer.  
> **Epistemic status:** claims are marked ✓ (sourced), ~ (model assumption
> likely correct), ? (unverified hypothesis). A validation pass is noted
> at the bottom of each section.

---

## Contents

1. [GNSS Signal Architecture](#1-gnss-signal-architecture)
2. [Error Sources](#2-error-sources)
3. [Positioning Modes](#3-positioning-modes)
4. [RTCM Protocol](#4-rtcm-protocol)
5. [NTRIP Protocol](#5-ntrip-protocol)
6. [Network RTK](#6-network-rtk)
7. [Ionospheric Effects](#7-ionospheric-effects)
8. [Latency and Fix Quality](#8-latency-and-fix-quality)
9. [Multipath](#9-multipath)
10. [Base Station Setup](#10-base-station-setup)

---

## 1. GNSS Signal Architecture

### 1.1 Constellations

| Constellation | Operator | Satellites (approx) | Notes |
|---|---|---|---|
| GPS | USA (DoD) | 31 active | L1/L2/L5; oldest, most receiver support |
| GLONASS | Russia (Roscosmos) | ~24 | FDMA on L1/L2 (legacy, different freq per satellite); CDMA on L1/L2/L3 (newer sats) ✓ |
| Galileo | EU (GSA/EUSPA) | ~30 | E1/E5a/E5b/E6; E6 carries HAS corrections |
| BeiDou (BDS-3) | China (CNSA) | ~45 | B1C/B1I/B2a/B2b/B3I; regional + global |
| QZSS | Japan (JAXA/Cabinet Office) | 4 | Geosynchronous+inclined; augments GPS over Japan/Asia-Pacific ~ |
| NavIC (IRNSS) | India (ISRO) | 7 | Regional only (Indian subcontinent + ~1500 km); limited receiver support ~ |

~ = model assumption; not yet source-verified.

### 1.2 Signal Frequencies

Each constellation broadcasts on multiple carrier frequencies. The names
differ per constellation but map to similar roles:

| Band role | GPS | GLONASS | Galileo | BeiDou |
|---|---|---|---|---|
| L1 / primary | L1 1575.42 MHz | L1 1602+n×0.5625 MHz (FDMA) ✓ | E1 1575.42 MHz | B1C 1575.42 / B1I 1561.098 MHz |
| L2 / secondary | L2 1227.60 MHz | L2 1246+n×0.4375 MHz (FDMA) ✓ | — | B2a 1176.45 / B2b 1207.14 MHz |
| L5 / safety-of-life | L5 1176.45 MHz | L3 1202.025 MHz ✓ (CDMA, newer sats) | E5a 1176.45 / E5b 1207.14 MHz | B2a 1176.45 MHz |
| E6 / data | — | — | E6 1278.75 MHz (HAS) | B3I 1268.52 MHz |

GLONASS note: n is the satellite's frequency channel number (−7 to +6). ✓
L1 and L2 use **different** channel spacings — 0.5625 MHz vs 0.4375 MHz
respectively. This matters for GLONASS inter-frequency bias modelling.
The `1230` RTCM message carries these biases for rover compensation.

### 1.3 Why Band Count Matters for RTK

**Single-frequency (L1 only):**
- Cannot remove ionospheric delay; relies on Klobuchar model correction
  (~50–60% removal) ~
- Reliable RTK fix roughly within 10 km of base; degrades fast beyond that
- Increasingly uncommon in dedicated RTK hardware; avoid for new purchases

**Dual-frequency (L1+L2 or equivalent):**
- Forms the ionosphere-free (iono-free) linear combination: cancels
  ~99% of first-order iono delay ~
- Reliable fix out to ~30 km under normal conditions
- The practical minimum for NTRIP RTK at useful baselines
- Examples: ZED-F9P (GPS+GLONASS+Galileo+BeiDou L1/L2), Emlid RS2+

**Triple-band (L1+L2+L5 or L1+E5a+E5b etc.):**
- The extra-widelane (EWL) combination of L2+L5 has a wavelength of
  ~3.4 m ✓ and can be resolved near-instantaneously ✓. The widelane
  L1+L2 (~86 cm ✓, derived: c/|f_L1−f_L2|) then resolves in seconds. This cascaded approach
  dramatically shortens ambiguity resolution time compared to dual-band.
- Demonstrated: wide-lane IAR >99% within 20 s triple-freq vs 64% within
  150 s dual-freq for the same conditions ✓
- Under strong multipath: ambiguity-fixed solutions achieved 78% of epochs
  triple-freq vs near-zero dual-freq ✓
- Practical benefits over dual-band:
  - Faster TTFF and re-init after signal loss
  - Better performance under canopy and in urban canyons
  - More robust during elevated ionospheric activity
- Examples: ZED-F9P variants with L5 ~, Septentrio mosaic-X5 ~,
  Emlid RS3, survey-grade Trimble/Leica

**Quad-constellation (GPS+GLONASS+Galileo+BeiDou):**
- More satellites visible at any sky position → faster ambiguity
  resolution; fewer gaps from partial obstruction
- Benefits compound with more bands; a quad-constellation triple-band
  receiver is the current hobbyist-accessible sweet spot (ZED-F9P or
  similar)

**For answering user questions:** if a user has a dual-band receiver and
reports slow TTFF or frequent fix loss in marginal conditions (urban,
canopy, solar-max periods), upgrading to triple-band is a valid
recommendation. If they have a single-frequency receiver, the most
impactful hardware change is moving to dual-band, not antenna or
software changes.

### 1.3 Signal Structure (GPS L1 example)

~ A GNSS signal is a spread-spectrum carrier modulated with:
- **PRN code (C/A or P(Y))** — enables pseudorange measurement (~metre
  accuracy per epoch)
- **Navigation message (NAV/LNAV/CNAV)** — satellite ephemeris, clock
  corrections, ionospheric model parameters (Klobuchar for GPS)
- **Carrier phase** — the fractional + integer cycle count of the carrier
  wave (~19 cm wavelength for L1); carrier phase is what RTK exploits

The carrier phase measurement is extremely precise (~1–2 mm noise) but
ambiguous: the receiver knows the fractional phase but not the integer
number of full cycles between satellite and antenna. RTK resolves that
integer — the "ambiguity" — using double-differencing across satellites
and between base/rover.

### 1.4 GNSS vs GPS — terminology note

"GPS" is often used colloquially to mean any GNSS. Modern receivers
track all available constellations simultaneously. A receiver described
as "GPS+GLONASS+Galileo+BeiDou" typically delivers better sky coverage
(more satellites visible), faster ambiguity resolution, and more
resilience to partial sky blockage than GPS-only.

---

## 2. Error Sources

GNSS ranging errors come from several distinct physical sources. RTK
corrects most of them by differencing; understanding which ones remain
is important for diagnosing poor fix quality.

### 2.1 Ionospheric Delay

The ionosphere (roughly 60–1000 km altitude) is a plasma layer that
slows the group velocity of GNSS signals. The delay is dispersive —
it varies with frequency as ~1/f². ~ This means:

- L1 and L2 experience different delays
- The difference between L1 and L2 pseudoranges gives a direct
  measurement of the ionospheric delay (TEC — Total Electron Content)
- Single-difference (base−rover) removes ~common-mode iono for short
  baselines; for long baselines the rover and base look through
  different iono columns and residual iono is the dominant error

~ Typical L1 delay: 1–10 metres at zenith, can reach 50+ m during
severe geomagnetic storms.

Gradient across a 30 km baseline under quiet conditions: ~1–3 cm ~;
during a severe storm it can exceed 10 cm/km of baseline, preventing
RTK fix entirely.

Single-frequency RTK relies on the Klobuchar model (GPS) or NeQuick
model (Galileo) broadcast in the navigation message — these correct
roughly 50–60% of iono delay. ~ Dual-frequency receivers compute and
remove it directly.

### 2.2 Tropospheric Delay

The neutral atmosphere (troposphere + stratosphere) introduces a
non-dispersive delay (~2.3 m zenith dry + ~0.2 m zenith wet). ~

- **Dry component**: proportional to air pressure; relatively stable
  and well-modelled (e.g. Saastamoinen model ~ removes ~99%)
- **Wet component**: water vapour; spatially variable, harder to model;
  residual after modelling ~2–4 cm ~

For short baselines (<30 km, similar elevation), tropo largely cancels
in double-differencing. For long baselines or sites at very different
altitudes, tropo gradient is a significant error source.

### 2.3 Satellite Clock and Orbit Errors

~ Broadcast ephemeris errors (orbit + clock) are typically 1–2 m for
GPS and slightly larger for GLONASS. These are correlated between base
and rover (both see the same satellite) and cancel almost completely in
short-baseline RTK double-differencing. For long baselines (~100 km)
residual orbital error can be ~1 cm. PPP corrections (SSR) deliver
sub-cm orbit + clock corrections.

### 2.4 Multipath

Signals reflected off surfaces near the antenna arrive slightly later
than the direct signal and corrupt both pseudorange and carrier phase.
See section 9 for detail.

### 2.5 Receiver Noise and Hardware Biases

Carrier-phase measurement noise floor: ~1–2 mm for geodetic receivers.
The u-blox ZED-F9P achieves sub-mm carrier phase noise in zero-baseline
tests ✓, with RTK positioning spec of 1 cm + 1 ppm. Pseudorange noise:
~20–50 cm for consumer-grade, ~5–10 cm for geodetic. ~ Hardware biases
(antenna phase centre offsets, inter-frequency biases) are calibrated
out in geodetic equipment; the ZED-F9P's practical accuracy floor is
dominated by antenna quality and multipath rather than receiver noise.

### 2.6 Error Budget Summary

| Error source | Standalone GPS | Single-base RTK 10 km | Single-base RTK 50 km |
|---|---|---|---|
| Iono | 1–10 m | ~cancelled (L1+L2) or ~2 cm (L1) | ~2–10 cm |
| Tropo | ~0.5 m | ~cancelled | ~2–5 cm |
| Orbit/clock | ~1–2 m | ~cancelled | ~1 cm |
| Multipath | ~0.5 m | 1–5 cm | 1–5 cm |
| Noise | ~0.3 m | ~1–3 mm | ~1–3 mm |
| **Total (RMS)** | **5–10 m** | **1–5 cm** | **5–15 cm** |

~ All values are model assumptions. Actual values depend on sky
conditions, receiver quality, and geomagnetic activity.

---

## 3. Positioning Modes

### 3.1 Standalone GNSS (SPP)

Single-point positioning using pseudoranges only. Accuracy limited by
all error sources in §2. ~5–10 m typical; can degrade to 50+ m during
ionospheric storms. Consumer devices (phones, car GPS) use this mode.

### 3.2 DGNSS / SBAS

Differential GNSS: a reference station broadcasts pseudorange
corrections; rover applies them. Removes common-mode satellite clock
and orbit errors. Accuracy ~0.3–1 m. Does **not** use carrier phase.

SBAS (WAAS, EGNOS, MSAS, GAGAN, SDCM) broadcasts DGNSS corrections
via geostationary satellite — no internet connection needed, but
accuracy ceiling is ~1 m. This is why DGNSS-only NTRIP mountpoints
are filtered out of this project: Galileo HAS is free, global, and
better.

### 3.3 RTK (Real-Time Kinematic)

Uses carrier-phase double-differences between base and rover, and
between satellite pairs. The critical step is **integer ambiguity
resolution (IAR)**: finding the integer number of carrier cycles on
each satellite–antenna path. Once resolved (a "fix"), positional
accuracy is 1–3 cm.

**Fix states:**
- **Float**: corrections applied, ambiguities estimated as real numbers
  (not integers). Accuracy ~0.1–0.5 m. Can drift.
- **Fix**: integer ambiguities resolved. Accuracy 1–3 cm. Stable.
- **DGNSS**: pseudorange-only fallback, ~0.5 m.

~ Time to first fix (TTFF) after connecting to corrections: typically
30–90 s in good conditions (dual-band, open sky, short baseline).
Can be seconds if the rover previously had a fix on the same site
(warm start with saved ambiguities). Can be several minutes or never
if baseline is long, sky is obscured, or iono is disturbed.

**Double-differencing** eliminates satellite clock errors, receiver
clock errors, and most atmospheric errors simultaneously:

```
DD_phase = (φ_rover_sat1 − φ_base_sat1) − (φ_rover_sat2 − φ_base_sat2)
```

This leaves only: integer ambiguity + multipath + noise.

### 3.4 Network RTK (NRTK)

Multiple reference stations in a network; a server models the spatial
variation of atmospheric errors and broadcasts synthetic corrections.
The rover's effective baseline to the virtual reference is short (~0
km for VRS mode), removing most spatially-varying errors. See §6 for
network types (VRS, MAC, FKP, i-MAX).

### 3.5 PPP (Precise Point Positioning)

Single receiver; no base station. Uses precise satellite orbit and
clock products (IGS, CNES, etc.) broadcast or downloaded. Must model
or estimate all error sources independently. ~

**Convergence time:** ~ Standard float PPP: typically 30–45 min to
reach cm-level accuracy. PPP-AR (integer ambiguity resolution, e.g.
CSRS-PPP with AR mode, Galileo HAS with PPP-AR): can reach cm-level
in 10–20 min. These are different service tiers — don't conflate them.
Galileo HAS and QZSS CLAS are free broadcast PPP services — cm-level
after convergence, no subscription, no base station, works anywhere
with satellite visibility.

~ PPP is not covered by this project's map (scope: NTRIP network RTK),
but understanding it clarifies why "standalone" devices can still
achieve cm accuracy without any internet connection.

### 3.6 SSR vs OSR

- **OSR (Observation Space Representation)**: traditional RTK — the
  reference station sends its own raw observations; rover differences
  them. Corrections are implicitly spatial and can't easily be
  disaggregated.
- **SSR (State Space Representation)**: server disaggregates
  corrections into orbit, clock, iono, tropo components and sends them
  separately. Rover reconstructs a synthetic reference observation.
  Enables PPP-RTK (fast-converging PPP using network iono/tropo models).
  Used by: Galileo HAS (E6-B), BeiDou PPP-B2b ~, QZSS CLAS ~, and
  commercial services (Swift Navigation Skylark, Trimble RTX, etc.).

~ SPARTN is a compressed SSR message format used over NTRIP and
u-blox PointPerfect / Thingstream — distinct from RTCM SSR.

---

## 4. RTCM Protocol

RTCM SC-104 is the de-facto standard for broadcasting differential GNSS
corrections. The standard is owned by RTCM (Radio Technical Commission
for Maritime Services) and is not free; message specs are paywalled.
The descriptions below are from public documentation and receiver SDKs.

### 4.1 RTCM 2.x (legacy)

Variable-length 30-bit word frames. Includes message types for GPS
pseudorange corrections (type 1, 9), GLONASS (type 31), and carrier
phase (type 18/19 for RTK). ~

~ Increasingly unsupported by modern firmware. u-blox F9P dropped
RTCM 2.x reception in firmware 1.x ~. The popup in this project
warns when a mountpoint is RTCM 2.x only.

### 4.2 RTCM 3.x — Legacy messages

Frame format: 3-byte header (preamble 0xD3, 6-bit reserved, 10-bit
message length), variable payload, 3-byte CRC-24Q. Messages are
self-framing and can be concatenated in a stream.

Key legacy (non-MSM) messages:

| Msg | Content | Notes |
|---|---|---|
| 1001–1004 | GPS L1/L2 RTK observables | Older; prefer MSM |
| 1005 | Stationary antenna reference point (ARP), no height | Required for RTK |
| 1006 | ARP + antenna height | Preferred over 1005 |
| 1007 | Antenna descriptor | Antenna type/model |
| 1008 | Antenna serial number | |
| 1009–1012 | GLONASS L1/L2 RTK observables | |
| 1013 | System parameters / time offsets | |
| 1019 | GPS ephemeris | For standalone use |
| 1020 | GLONASS ephemeris | |
| 1033 | Receiver/antenna descriptor | |
| 1042 | BeiDou ephemeris ~ | |
| 1045/1046 | Galileo ephemeris ~ | |

### 4.3 RTCM 3.x — MSM (Multiple Signal Messages)

MSM is the modern format, introduced in RTCM 3.2 ~. Supports all
constellations with a consistent structure.

MSM type number = base + signal density:

| MSM level | Pseudorange | Carrier phase | Doppler | Signal-to-noise | Notes |
|---|---|---|---|---|---|
| MSM1 | compact | — | — | — | Low bandwidth |
| MSM2 | — | compact | — | — | |
| MSM3 | compact | compact | — | — | |
| MSM4 | full | full | — | half-cycle | Common RTK baseline |
| MSM5 | full | full | full | half-cycle | Adds Doppler |
| MSM6 | full high-res | — | — | full | |
| MSM7 | full high-res | full high-res | full | full | Max precision; preferred |

Base numbers per constellation:
- GPS: 1071–1077
- GLONASS: 1081–1087
- Galileo: 1091–1097
- SBAS: 1101–1107
- QZSS: 1111–1117 ~
- BeiDou: 1121–1127 ~
- NavIC: 1131–1137 ~

~ So `1074` = GPS MSM4, `1077` = GPS MSM7, `1097` = Galileo MSM7, etc.

**For an RTK stream to be useful to a modern rover:**
- Must include at least MSM4 (or equivalent legacy 1001–1004) for GPS
- MSM7 preferred for best accuracy
- 1005 or 1006 required (base station coordinates)
- Multi-constellation (GPS + Galileo or + GLONASS) significantly
  improves fix reliability and TTFF

**Typical "good" RTCM 3 stream contents:**  
`1005, 1074, 1077, 1084, 1087, 1094, 1097, 1124, 1127` ~  
(Base position + GPS MSM4+7 + GLONASS MSM4+7 + Galileo MSM4+7 + BDS MSM4+7)

In practice many networks broadcast just MSM4 or just MSM7 per
constellation; the combination varies by network and caster config.

### 4.4 RTCM 3.x — SSR Messages

SSR message ranges per constellation ✓:
- GPS: 1057–1068 (orbit 1057, clock 1058, code bias 1059, …)
- GLONASS: 1063–1068 (orbit 1063, clock 1064, code bias 1065, …)
- Galileo: 1240–1245 (orbit 1240, clock 1241, code bias 1242, …)
- QZSS: 1246–1251 ~
- BeiDou: 1258–1263 ~

Content: orbit corrections, clock corrections, code/phase biases, VTEC
iono maps. Used by PPP-RTK services, not by standard single-base RTK.
These messages are uncommon on the free public casters this project covers.

### 4.5 Proprietary Formats

| Format | Owner | Notes |
|---|---|---|
| CMR / CMR+ | Trimble | Older; common on legacy Trimble networks |
| sPace | Leica ~ | Leica SmartNet proprietary |
| SPARTN | u-blox / Swift / Septentrio ~ | SSR compressed; used by PointPerfect |
| ProMark / LandXML | Various | Not correction formats |

~ Most free public networks use RTCM 3.x exclusively. CMR/CMR+ appears
on some older SAPOS and Leica-run casters.

---

## 5. NTRIP Protocol

NTRIP (Networked Transport of RTCM via Internet Protocol) is defined
in BKG Technical Note 1 (Bundesamt für Kartographie und Geodäsie). ~
Version 2.0 is current; version 1.0 is still used by many casters.

### 5.1 Architecture

Three roles:
- **NtripSource (base station)**: connects to caster and pushes RTCM
  stream via HTTP/1.1 POST (NTRIP v2) or a proprietary push method ~
- **NtripCaster**: HTTP server; accepts sources on one side, serves
  clients on the other; maintains sourcetable
- **NtripClient (rover)**: HTTP/1.1 GET; requests a mountpoint;
  receives RTCM byte stream

### 5.2 Sourcetable

The caster's index of available streams. Fetched via HTTP GET `/` ~
(no mountpoint). Returns three record types:

**STR (stream) record — key fields:**

```
STR;mountpoint;identifier;format;format-details;carrier;nav-system;
    network;country;lat;lon;nmea;solution;generator;compr-encryp;
    authentication;fee;bitrate;misc
```

Fields used by this project's pipeline (0-indexed):

| Index | Field | Project use |
|---|---|---|
| 0 | "STR" | record type filter |
| 1 | mountpoint | station name |
| 9 | lat | pin location |
| 10 | lon | pin location |
| 11 | nmea | VRS filter (nmea=1 → caster requires GGA → drop) ✓ |
| 3 | format | RTCM 2 legacy warning; carrier inference |
| 5 | carrier | 0=DGNSS drop, 1=L1, 2=L1+L2, 3=tri-band |
| 14 | fee | "N" = no fee |

**NET (network) record**: describes the network owning a group of STR
entries; contains network name, operator, registration URL. ~

**CAS (caster) record**: describes the caster itself. ~ Not used by
this project's pipeline.

### 5.3 NTRIP v1 vs v2

| Feature | v1 | v2 |
|---|---|---|
| HTTP version | HTTP/1.0 | HTTP/1.1 |
| Client request | GET /mountpoint | GET /mountpoint with Host header |
| Chunked transfer | No | Yes (Transfer-Encoding: chunked) |
| Client → caster position | Out-of-band (separate GGA) | In-band via NMEA GGA sentence in request body ~ |
| Sourcetable request | GET / | GET / |

~ Most casters remain backward-compatible with v1. rtk2go accepts
both. ~ Some clients (older Trimble firmware) send v1 only.

### 5.4 NMEA GGA Sentence (rover → caster)

For VRS mountpoints, the rover must send its approximate position so
the network can synthesise a virtual reference nearby. This is done
by the client sending an NMEA GGA sentence upstream to the caster:

```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
```

Fields: time, lat, N/S, lon, E/W, fix quality, sats, HDOP, altitude,
geoid separation, age of DGPS, DGPS station ID, checksum.

~ If the client sends a position >50 km from the VRS service area, the
caster may close the connection or send no data.

### 5.5 Authentication

NTRIP basic auth uses HTTP Basic Authentication (base64 username:password).
The sourcetable `authentication` field indicates whether auth is
required (B = basic, D = digest ~, N = none).

Many "open" networks use a fixed shared credential (e.g. Centipede:
`centipede`/`centipede`; rtk2go: any email / `none`). The password
is transmitted in base64, which is trivially reversible — these
credentials provide token accountability, not security.

### 5.6 Caster Software

Common caster implementations:
- **NTRIP Caster (BKG)**: original reference implementation, used by
  many national survey agencies ~
- **SNIP** (SCSC, commercial): widely used; powers rtk2go ~ and some
  SAPOS casters
- **str2str** (RTKLIB): open-source; can act as caster, source, or
  client; basis for RTKBase
- **BNC** (BKG Network Combiner): more complex, designed for analysis

### 5.7 Port Conventions

Default NTRIP port is 2101. Non-standard ports are a caster operator
choice, not a spec deviation — NTRIP runs over any TCP port; 2101 is
convention only. Examples in public networks: 5005 (SPSLux), 2001
(InaCORS), 9879 (ORGN).

### 5.8 NEAR and Auto-Select Mountpoints

Some casters publish special mountpoints that are routing aliases, not
physical stations:

- **NEAR** (rtk2go, Centipede): the caster routes the connection to
  whichever base is closest to the rover's reported GGA position.
  Requires the client to send a GGA sentence. Not a fixed geographic
  point.
- **Network auto-selects** (various names per network): similar idea;
  VRS networks sometimes publish a single entry-point mountpoint that
  triggers the per-rover synthetic stream generation.

These aliases share a defining NTRIP characteristic with VRS: they carry
`nmea = 1` in the sourcetable (they require rover position) and have
no meaningful fixed coordinates. Rovers use them by typing the name
directly into the NTRIP client — they do not appear as map pins.

---

## 6. Network RTK

Network RTK (NRTK) services operate a network of reference stations
and broadcast corrections that are synthesised from multiple real
stations rather than a single base. The key benefit: the effective
baseline error (especially iono and tropo gradients) is the distance
to the virtual reference, not to the nearest physical station, which
can be 50–100 km away.

### 6.1 VRS — Virtual Reference Station

Originally developed by Trimble. ~

1. Rover sends its approximate position (GGA) to the network server.
2. Server selects 3+ surrounding real stations and runs a network
   GNSS processing engine (Trimble GPSNet or equivalent) ~.
3. Server synthesises RTCM observations as if there were a real
   station at the rover's location (~0 km baseline).
4. Server streams these synthetic RTCM observations to the rover.
5. Rover's RTK engine treats them as a normal single-base stream.

**Defining NTRIP characteristic:** NMEA field = 1 in sourcetable
(rover must send position). Any NMEA=1 mountpoint is presumptively VRS
or similar (MAC/FKP/i-MAX also require rover position).

**VRS limitations:**
- Each rover gets a unique stream; scales poorly at very high rover
  counts (server CPU, bandwidth)
- Requires continuous GGA feedback; if client stops sending, server
  may terminate the stream ~
- Not all RTK engines handle the implicit baseline correctly —
  initialisation artefacts can occur if the rover moves significantly
  while connected ~

### 6.2 MAC — Master-Auxiliary Concept

Developed by Geo++ (Germany). ~

Instead of synthesising observations, the server sends:
- Full observations from a master station
- Difference observations (auxiliary − master) for each auxiliary
  station in a compressed delta format

The rover's RTK engine reconstructs the full network correction
internally. Fewer server computations per rover; better scales to
many simultaneous rovers. ~

MAC is the basis for RTCM 3 message types 1014–1017 ~. Used by
several European national networks including some SAPOS states. ~

### 6.3 FKP and i-MAX (other NRTK modes)

**FKP** (Flächen-Korrektur-Parameter, German origin / SAPOS): broadcasts
a spatial gradient model; rover evaluates the polynomial at its own
position rather than receiving a synthetic stream. RTCM msg 1034 ✓.
Operationally identical to VRS for this project: mountpoints carry
NMEA=1 and are dropped.

**i-MAX** ~ (Trimble): combines VRS and MAC ideas. Appears in some German
and Swiss networks. Also NMEA=1 → dropped by the same filter.

### 6.5 What this project shows

This project filters all NMEA=1 mountpoints as VRS/NRTK and shows
the network as a coloured circle (if in-pipeline) or grey circle
(deferred). Physical single-base stations (NMEA=0) show as pins.

Two known real-world exceptions to the NMEA=0 = physical rule:
- **rtk2go**: caster-wide misconfiguration; all physical stations
  tagged NMEA=1 despite being fixed single-base stations.
- **GeoRTK**: 2 physical F9P stations incorrectly tagged NMEA=1.

Networks using only VRS (0 physical pins): CROPOS, ASG-EUPOS, FLEPOS,
WALCORS, ESTPOS, LatPos, KSA-CORS, 10 SAPOS states, 6 US DOT networks.

---

## 7. Ionospheric Effects

### 7.1 Physical Mechanism

The ionosphere is a layer of solar-UV-ionised plasma. Free electrons
slow the GNSS signal group velocity (advance phase velocity) by an
amount proportional to Total Electron Content (TEC) and inversely
proportional to f². ~

TEC is measured in TECU (1 TECU = 10¹⁶ electrons/m²). Range delay
at L1: ~0.16 m per TECU ✓ (formula: 40.3×10¹⁶/f² m/TECU, f in Hz). ~ During quiet conditions, vertical TEC
over mid-latitudes is ~5–20 TECU; during severe storms it can reach
200+ TECU over some regions. ~

### 7.2 Solar Cycle

The Sun follows an approximately 11-year activity cycle. ~

- **Solar maximum**: increased UV and X-ray flux ionises more
  electrons; higher TEC, more variability, more frequent geomagnetic
  storms. Solar Cycle 25 peaked in October 2024 (smoothed sunspot
  number ~161, exceeding the original prediction of 115) ✓ — the
  2025–2026 period is early decline but still elevated; expect above-
  average RTK degradation risk until ~2027–2028.
- **Solar minimum**: lower TEC, quieter iono, longer RTK baselines
  work more reliably.

Solar cycle affects:
- Baseline length at which fix is achievable (shorter during max)
- Time to first fix (longer during disturbed conditions)
- Frequency of sudden fix loss (cycle slips)

### 7.3 Geomagnetic Activity — Kp Index

The Kp index (0–9 scale, global) measures geomagnetic storm intensity:

| Kp | Activity | RTK impact |
|---|---|---|
| 0–2 | Quiet | Minimal; normal RTK performance |
| 3–4 | Unsettled (G0–G1 onset) | Kp>3 considered active ✓; high-lat stations begin to show iono gradient growth |
| 5 | Minor storm (G1) | ~ Fix difficult at baselines >20 km, NRTK may degrade at high latitudes |
| 6 | Moderate storm (G2) | Noticeable mid-lat degradation confirmed ✓; IAR success rate can fall significantly |
| 7 | Strong storm (G3) | IAR success rate can drop from 94% → 31% ✓; high-lat median error 2.4 cm → 9.0 cm ✓ |
| 8–9 | Severe/Extreme (G4–G5) | RTK fix near-impossible at affected latitudes; even NRTK degrades |

**Important latitude caveat:** global Kp is a poor predictor for
high-latitude sites (IceCORS, northern AUSCORS, TrigNet). Weak events
(Kp 3–4) can still cause large local iono gradients within the auroral
oval. ✓ Users at high latitudes should use regional space weather
products (e.g. NOAA wing-kp) rather than global Kp. ~

Real-time Kp: NOAA Space Weather Prediction Center (swpc.noaa.gov).
3-day forecast also available.

### 7.4 Ionospheric Scintillation

Near the magnetic equator (~±15° latitude) and at high latitudes
(auroral zone), the ionosphere can exhibit rapid, irregular TEC
fluctuations — **scintillation**. ~

Effects on RTK:
- Rapid carrier phase fluctuations → cycle slips (sudden loss of
  phase lock)
- Amplitude fading → signal loss on individual satellites
- Can prevent ambiguity resolution entirely during strong events

~ Equatorial scintillation is worst around sunset local time and
during solar maximum. Equatorial regions where this project has
sources: Indonesia (InaCORS), Colombia (IGAC), Brazil (RBMC-IP),
parts of Africa (TrigNet southern edges). Users in these regions
should expect more frequent fix loss around local sunset.

### 7.5 Polar / High-Latitude Effects

Arctic and sub-Arctic regions (Iceland IceCORS, northern AUSCORS
sites) experience auroral electrojet interference. ~ TEC gradients
across a baseline can be large and fast-changing. Network RTK (VRS/MAC)
partially compensates if station spacing is close enough, but the
solver can diverge during strong events. ~

### 7.6 Practical Implications for This Project

When a user reports "I had RTK fix yesterday and can't get it today,
nothing changed":
1. Check Kp index (current and past 3–6 hours) — storm recovery can
   take hours after Kp drops
2. Check time of day relative to the user's magnetic latitude
   (sunset scintillation)
3. Suggest switching to a closer station (shorter baseline is more
   iono-tolerant)
4. For L1-only users, dual-band upgrade is the structural fix

---

## 8. Latency and Fix Quality

### 8.1 Where Latency Comes From

End-to-end latency in an NTRIP RTK link:

```
GNSS satellite signal
  → base station receiver (obs epoch, ~1 Hz or 5 Hz)
  → base station encoding (RTCM frame build, <5 ms ~)
  → base → caster TCP (LAN or WAN, 5–200 ms ~)
  → caster → rover client (internet, 10–100 ms ~)
  → rover receiver processing (internal, <10 ms ~)
  → RTK engine (epoch processing, <50 ms ~)
Total: typically 50–500 ms end-to-end ~
```

### 8.2 Effect of Latency on RTK

RTK engines use a **prediction model** to account for the age of
corrections. ~ The correction age (time since reference epoch) is
embedded in some RTCM messages or tracked by the receiver.

~ For a stationary receiver: latency up to ~1–2 s has negligible
effect — the base station's ionosphere and tropo don't change that
fast.

For a moving rover (vehicle, drone):
- Position error from latency = latency × rover velocity
- At 10 m/s and 500 ms latency: ~5 m positional offset if corrections
  are stale
- Receiver firmware compensates using Doppler (IMU-augmented receivers
  compensate better) ~

**Fix loss from high latency:**  
If correction age exceeds the receiver's timeout threshold (configurable
in most firmware), the receiver downgrades to float or autonomous.
~ u-blox F9P DGNSS timeout default is approximately 60 s (NAV5
configuration parameter); geodetic receivers are often similar or longer.
This means brief cellular dropouts of a few seconds typically do **not**
cause fix loss — the receiver coasts. Sustained gaps >60 s on the F9P
will trigger a downgrade. Always verify the actual default from the
Interface Description for the firmware version in use.

### 8.3 Observation Rate

Most free network casters broadcast at **1 Hz** (one epoch per second).
Some broadcast at 5 Hz or 10 Hz (typically professional networks or
RTKBase with configured high-rate output).

~ For static survey applications, 1 Hz is adequate. For fast-moving
rovers (vehicles, drones > ~5 m/s) higher rate corrections reduce
the position error from latency-induced stale corrections.

### 8.4 Practical Latency Numbers

~ Based on typical public internet:
- Urban 4G LTE to nearby caster: 50–100 ms
- Rural 4G with marginal signal: 100–500 ms + frequent drops
- Starlink (fixed): 20–60 ms, low jitter ~
- Satellite internet (geostationary, legacy): 500–800 ms — RTK
  marginal at best
- WiFi via home router to caster: 10–50 ms

### 8.5 Diagnosis

User symptom: "Fix keeps dropping every few minutes."  
Most likely: cellular latency spikes or disconnects. Steps:
1. Check NTRIP client's correction age display (if available)
2. Test with a closer caster to reduce WAN hops
3. On Android: disable battery optimisation for the NTRIP client app
4. Consider caching the raw stream locally (str2str relay) if
   connectivity is intermittent

---

## 9. Multipath

### 9.1 Mechanism

A reflected or diffracted signal arrives at the antenna having
travelled a longer path than the direct signal. The receiver sees the
superposition of the direct signal and one or more delayed copies. ~

Effect on pseudorange: sinusoidal error with amplitude up to half the
chip length. GPS C/A chip ≈ 293 m ✓ → theoretical half-chip ≈ 147 m,
but correlator design limits the practical multipath error envelope to
~15–30 m for consumer receivers. ~ P-code chip ≈ 29.3 m → half ≈ 15 m.
Average real-world C/A pseudorange multipath: 0.5–3 m.

Effect on carrier phase: sinusoidal error with amplitude up to a
quarter-wavelength (~5 cm at L1 ~). This is the critical number for
RTK — multipath is often the floor on RTK accuracy in non-ideal
environments.

### 9.2 Characteristics

- **Frequency**: multipath signal oscillates with a period depending
  on geometry change rate. For static receivers, a full cycle may take
  tens of minutes (as satellite moves across sky); for moving rovers,
  seconds.
- **Elevation dependence**: low-elevation satellites experience more
  multipath (longer signal path, more reflective surfaces). ~
  Elevation masks of 10–15° cut most severe multipath.
- **Environment-specificity**: parking lots, metal roofs, water
  surfaces, building facades are major reflectors. Open fields are
  best.

### 9.3 Mitigation Techniques

**Antenna design:**
- ~ Choke-ring antennas (geodetic) have concentric conductive rings
  that attenuate signals arriving from below the horizon — highly
  effective against ground bounce, adds ~500 g and $1,000+ to
  antenna cost
- Ground planes (flat conductive surface below the antenna) provide
  some benefit for consumer setups at low cost
- ~ Helical and patch antennas with back-cavity provide some
  multi-path rejection versus simple patch designs

**Receiver-side:** Modern receivers use narrow correlator spacing and
various internal multipath mitigation algorithms. ~ For RTK users,
these techniques reduce code multipath but have limited effect on
carrier-phase multipath, which is what ultimately limits fix accuracy
in reflective environments. The practical takeaway: choose the site,
not the receiver, to solve multipath.

**Software / algorithmic:**
- Elevation-dependent weighting: down-weight low-elevation
  observations where multipath is worse
- Multipath maps: if the antenna is stationary, multipath repeats
  with sidereal period (~24h minus ~4 min for GPS ~); subtract
  previous-day residuals to reduce the error
- NRTK partially mitigates base-station multipath by network-averaging
  atmospheric corrections — but each physical reference station still
  has its own multipath environment

### 9.4 Practical Impact on This Project's Users

For a rover user in a typical urban/suburban environment:
- ~ RTK accuracy floor is 2–5 cm due to multipath, not ambiguity
  resolution errors
- Moving along a route repeatedly (survey, agriculture) will see
  repeatable error patterns tied to fixed reflectors

For base station operators (see §10):
- Site selection is the most important multipath mitigation
- Rooftop mounting near HVAC equipment, parapets, or metal structures
  introduces multipath that degrades corrections for all rovers
  connected to that base

---

## 10. Base Station Setup

This section is intentionally more thorough than the hobbyist guide
(`guide.html`) because base station quality directly affects rover
accuracy for everyone connected to that base.

### 10.1 Hardware

#### Receiver

Minimum: dual-frequency (L1+L2) with RTCM 3.x output. The u-blox
ZED-F9P is the dominant hobbyist reference receiver:
- ~ Supports GPS L1/L2, GLONASS L1/L2, Galileo E1/E5b, BeiDou B1/B2
- ~ RTCM 3.3 MSM4/MSM7 output
- ~ Raw observable output for post-processing
- ~ Up to 20 Hz output rate (1 Hz is standard for NTRIP base use)
- ~ ~$130–180 for bare module; ~$250–400 in breakout boards (ArduSimple,
  SparkFun, Ardusimple simpleRTK2B)

For a permanent base feeding the public casters, a dedicated computer
(Raspberry Pi 4 or equivalent) runs 24/7 — Pi consumes ~5W ~.

#### Antenna

This is the highest-impact decision for base quality:

| Type | Cost (approx) | Multipath rejection | Notes |
|---|---|---|---|
| u-blox ANN-MB patch | ~$30 | Poor | Adequate for temp/mobile use only |
| Survey patch (e.g. Tallysman TW3742) | ~$150–250 | Moderate | Good hobbyist permanent base |
| Helical (e.g. ArduSimple SurveyXYZ) | ~$100–200 | Moderate | Good for rooftop with nearby obstructions |
| Choke-ring (geodetic, e.g. Leica AR25) | ~$2,000–5,000 | Excellent | Network station grade; overkill for single-user base |

~ A good survey patch with a ground plane outperforms a cheap patch
with a choke ring if the ground plane is installed correctly (flat,
conductive, min ~30 cm diameter ~).

#### Computer / Software

- **RTKBase** (github.com/Stefal/rtkbase): open-source; Raspberry Pi;
  web UI; handles NTRIP source push, local RTCM logging, RINEX
  conversion. Recommended for permanent hobbyist bases.
- **RTKLIB str2str**: CLI tool; no web UI; used as back-end by
  RTKBase; can multiplex one receiver to multiple casters
  simultaneously. ~
- **u-center** (Windows): u-blox config tool; configure receiver
  RTCM output, baud rate, message types. Run once to configure;
  not needed during operation.

### 10.2 Antenna Placement

**Non-negotiable requirements:**
- 360° clear sky view above ~10–15° elevation mask
- No metallic surface within ~1 m horizontally (reflector)
- Stable, rigid mount — even sub-mm daily motion is detectable in
  PPP solutions; for cm-RTK it matters less but thermal expansion
  cycles still add noise ~
- Shelter from direct rain impact on radome (for patch antennas) —
  wet radome can add ~1 cm error ~

**Common bad placements:**
- On a metal roof flat — ground bounce from the roof itself
- Next to HVAC units — metallic surfaces + vibration
- Under trees — phase centre variation from wet foliage, signal blockage
- On a tilted surface — phase centre offset changes with tilt

### 10.3 Base Position Determination

The base must know its own position accurately; all rover corrections
are relative to it. Three methods:

#### Method A: Average Over Time (simplest)

Let the receiver collect autonomous positions for 1–24 hours and
average them. ~ Accuracy: roughly 1–3 m under typical conditions,
potentially worse during elevated ionospheric activity (solar-max
periods push autonomous accuracy toward 3–5 m). This is adequate
for relative positioning (rover accuracy relative to the base is
still cm) but the absolute position of the base is only metre-level. If your
workflow requires absolute positions (connecting to a national
coordinate system), this is insufficient.

#### Method B: PPP (recommended for hobbyists wanting good absolute accuracy)

Upload a RINEX file of 24h+ raw observations to a free PPP service:
- **NRCAN CSRS-PPP** (Natural Resources Canada) — free automated web
  service; supports GPS+GLONASS, dual and single frequency, static and
  kinematic modes; returns ITRF coordinates ✓. 24h observation →
  cm-level absolute accuracy ✓.
- GIPSY-OASIS (JPL) — similar, free for non-commercial ~
- BKG's AUSPOS-type services ~

After 24h processing, absolute accuracy: ~1–3 cm. ~
After 1 week: sub-cm absolute. ~

Enter the resulting ECEF or geodetic coordinates as the fixed position
in RTKBase / str2str config.

#### Method C: Occupy a Known Benchmark

If a national survey benchmark is accessible, occupy it and use the
published coordinates directly. Best absolute accuracy, requires
field access to the benchmark.

### 10.4 Registering with Public Casters

#### rtk2go.com

- Register the mountpoint at rtk2go.com/new (form submission)
- ~ Approval is manual but typically within a few hours
- Credentials provided: password for your mountpoint
- Base station pushes via NTRIP source connection to `rtk2go.com:2101`
  using: username = mountpoint name, password = assigned password
- ~ rtk2go runs on SNIP software; max connection count per mountpoint
  and max bitrate limits exist (check current rtk2go documentation)
- Terms: free for non-commercial; base must be public and listed

#### Centipede

- Register at crtk.net (GitHub-based signup process ~)
- Open-source community; most nodes are in France + EU
- Centipede runs its own NTRIP server and also aggregates into
  the `crtk.net` caster
- ~ RTKBase integrates Centipede registration directly in its web UI

### 10.5 RTCM Message Selection for a Base Station

RTKBase default output (confirmed from source config) ✓:
```
1004, 1005(10), 1006, 1008(10), 1012, 1019, 1020, 1033(10),
1042, 1045, 1046,
1077, 1087, 1097, 1107, 1127, 1230
```
Numbers in parentheses = interval in seconds; others at 1 s.

Key messages explained:
- `1005(10)` / `1006` — base position every 10 s
- `1077` GPS MSM7, `1087` GLONASS MSM7, `1097` Galileo MSM7,
  `1107` SBAS MSM7, `1127` BeiDou MSM7 — full-res observations
- `1019`, `1020`, `1042`, `1045`, `1046` — GPS/GLONASS/BDS/Galileo
  ephemeris (allows rover to init without separate nav data download)
- `1230` — GLONASS L1/L2 code-phase biases (improves GLONASS RTK
  on some receivers)

RTKBase uses MSM7 by default, not MSM4. MSM7 is the right default
for hobbyist use with F9P — the bandwidth difference is manageable
on any modern network connection (a full MSM7 epoch for 4 constellations
is ~1–2 kbps ~ vs ~0.5–1 kbps for MSM4). Only bandwidth-constrained
links (narrow GPRS, satellite internet) would favour MSM4.

Minimum viable stream for a constrained link:
```
1005(10), 1077, 1097   — base position + GPS MSM7 + Galileo MSM7
```

### 10.6 Receiver Position Modes: Survey-In vs Fixed

Before a base station can broadcast useful corrections, the receiver
must know its own position. Two modes:

**Survey-in mode:** the receiver collects autonomous positions over a
configurable time/accuracy window. On the ZED-F9P, configured via
CFG-TMODE3 with two parameters ✓:
- `CFG-TMODE-SVIN_MIN_DUR` — minimum duration in seconds (default: 300 s)
- `CFG-TMODE-SVIN_ACC_LIMIT` — accuracy target in 0.1 mm units (default:
  500000 = 50 m, which is effectively "complete after 300 s regardless")

For a quality permanent base, set the accuracy limit to 2–5 m
(20000–50000) and minimum duration to 300–600 s. For a high-quality
base, use PPP instead (§10.3 Method B) and skip survey-in entirely.
The receiver locks the averaged position and switches to **fixed mode**,
outputting RTCM corrections relative to that locked point.
RTKBase displays "Survey-in in progress" then "Survey-in complete". ✓

If you enter a base position from PPP (§10.3 Method B), you bypass
survey-in entirely by configuring the receiver in "fixed mode" directly
with the known ECEF or geodetic coordinates.

**Why it matters:** a base stuck in survey-in mode (accuracy threshold
never met due to obstruction or interference) outputs an unstable
reference position. All rover corrections are relative to this moving
reference — the rover's absolute position drifts even if RTK fix is
reported. This is a common source of "fixed but wrong" position bugs.

### 10.7 Monitoring a Running Base

Signs of a healthy base station in logs/web UI:
- Stable number of tracked satellites (~8–12 for 4-constellation receiver)
- RTKBase shows "Survey-in complete" or fixed position mode active
- RTCM output rate matches configured rate (inspect with RTKLIB RTKPLOT
  or u-center's RTCM monitor)
- No cycle slips in raw phase (RTKBase shows this graphically)

Signs of problems:
- Satellite count drops periodically → obstruction or interference
- Phase noise elevated on specific satellites at specific times →
  multipath from a specific reflector (time-of-day repeatable)
- Base position drifting → receiver not in fixed mode; still in
  survey-in or autonomous — see §10.6
- Caster connection dropping → check internet, caster-side limits

---

---

## Sources consulted

- [rtk2go.com — How it Works](http://rtk2go.com/how-it-works/)
- [rtk2go.com — New Base Station Reservation](http://rtk2go.com/sample-page/new-reservation/)
- [docs.centipede.fr — Guide RTKBase](https://docs.centipede.fr/docs/base/Guide_RTKBase.html)
- [docs.centipede.fr — Connexion au caster](https://docs.centipede.fr/docs/centipede/3_connect_caster.html)
- [RTKBase default settings.conf — GitHub](https://github.com/Stefal/rtkbase/blob/master/settings.conf.default)
- [RTCM 3 Message List — SNIP Support](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/)
- [MSM message types — Tersus GNSS](https://www.tersus-gnss.com/tech_blog/new-additions-in-rtcm3-and-What-is-msm)
- [NTRIP v1 spec — ESA/GSSC (PDF)](https://gssc.esa.int/wp-content/uploads/2018/07/NtripDocumentation.pdf)
- [NTRIP v1 vs v2 — SNIP Support](https://www.use-snip.com/kb/knowledge-base/ntrip-rev1-versus-rev2-formats/)
- [BKG NtripCaster Manual](https://igs.bkg.bund.de/root_ftp/NTRIP/documentation/ntripcaster_manual.html)
- [Ionospheric Delay — ESA Navipedia](https://gssc.esa.int/navipedia/index.php/Ionospheric_Delay)
- [GLONASS Signal Plan — ESA Navipedia](https://gssc.esa.int/navipedia/index.php/GLONASS_Signal_Plan)
- [GLONASS CDMA signals — GPS World](https://www.gpsworld.com/glonass-cdma-signals-now-on-l1-l2/)
- [Solar Cycle 25 forecast — NOAA SWPC](https://www.swpc.noaa.gov/news/solar-cycle-25-forecast-update)
- [Solar Cycle 25 progression — NOAA SWPC](https://www.swpc.noaa.gov/products/solar-cycle-progression) (actual smoothed peak Oct 2024, SSN ~161)
- [Observed effects of geomagnetic storm on RTK — SWSC Journal](https://www.swsc-journal.org/articles/swsc/full_html/2012/01/swsc120026/swsc120026.html)
- [High-lat GNSS disturbances at sub-minor storm — Andalsvik 2014](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014RS005418)
- [ZED-F9P Product Summary — u-blox](https://content.u-blox.com/sites/default/files/ZED-F9P_ProductSummary_UBX-17005151.pdf)
- [ZED-F9P for geodetic measurement — ResearchGate](https://www.researchgate.net/publication/360316310_UBLOX_F9P_FOR_GEODETIC_MEASUREMENT)
- [CSRS-PPP — NRCAN](https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php)
- [VRS vs MAC principles — Janssen 2009](https://www.spatial.nsw.gov.au/__data/assets/pdf_file/0003/129414/2009_Janssen_IGNSS2009_VRS_vs_MAC.pdf)
- [VRS connection examples — SNIP Support](https://www.use-snip.com/kb/knowledge-base/virtual-reference-station-vrs-connection-examples/)
- [GPS C/A multipath error — NovAtel tech talk](https://novatel.com/tech-talk/an-introduction-to-gnss/resources/understanding-and-mitigating-gnss-multipath-interference-and-error)
- [ZED-F9P survey-in CFG-TMODE3 — Drotek RTK docs](https://drotek.gitbook.io/rtk-f9p-positioning-solutions/tutorials/setting-survey-in-time-and-position-accuracy)
- [ZED-F9P integration manual — u-blox](https://content.u-blox.com/sites/default/files/ZED-F9P_IntegrationManual_UBX-18010802.pdf)
- [Triple-frequency RTK widelane review — JGPS 2018](https://jgps.springeropen.com/articles/10.1186/s41445-018-0010-y)
- [RTCM 3 SSR message list — SNIP Support](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/)
- [GLONASS Signal Plan — ESA Navipedia](https://gssc.esa.int/navipedia/index.php/GLONASS_Signal_Plan)

_Last updated: 2026-04-24. Second validation pass: 2026-04-24._
