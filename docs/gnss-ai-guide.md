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
11. [Common Troubleshooting Scenarios](#11-common-troubleshooting-scenarios)
12. [Use Case → Accuracy Requirements](#12-use-case--accuracy-requirements)
13. [Datum and Coordinate System Confusion](#13-datum-and-coordinate-system-confusion)

---

## 1. GNSS Signal Architecture

### 1.1 Constellations

| Constellation | Operator | Satellites (approx) | Notes |
|---|---|---|---|
| GPS | USA (DoD) | 32 active | L1/L2/L5; oldest, most receiver support; GPS III block complete Apr 2026 ✓ |
| GLONASS | Russia (Roscosmos) | ~24 | FDMA on L1/L2 (legacy, different freq per satellite); CDMA on L1/L2/L3 (newer sats) ✓ |
| Galileo | EU (EUSPA, formerly GSA) | ~26–28 operational of 34 launched | E1/E5a/E5b/E6; E6 carries HAS corrections ✓ |
| BeiDou (BDS-3) | China (CNSA) | 45 (15 BDS-2 + 30 BDS-3 core constellation) | B1C/B1I/B2a/B2b/B3I; regional + global ✓; additional satellites launched post-2020 |
| QZSS | Japan (Cabinet Office) | 4 (planned expansion to 7) | Geosynchronous+inclined; augments GPS over Japan/Asia-Pacific; QZS-5 failed to reach orbit Dec 2025 — 7-satellite timeline uncertain ~ |
| NavIC (IRNSS) | India (ISRO) | ~3–4 operational | Regional only (Indian subcontinent + ~1500 km); severely degraded as of 2026 — atomic clock failures have reduced active satellites below the minimum operational threshold of 4; limited receiver support ✓ |

~ = model assumption; not yet source-verified.

### 1.2 Signal Frequencies

Each constellation broadcasts on multiple carrier frequencies. The names
differ per constellation but map to similar roles:

| Band role | GPS | GLONASS | Galileo | BeiDou |
|---|---|---|---|---|
| L1 / primary | L1 1575.42 MHz | L1 1602+n×0.5625 MHz (FDMA) ✓ | E1 1575.42 MHz | B1C 1575.42 / B1I 1561.098 MHz |
| L2 / secondary | L2 1227.60 MHz | L2 1246+n×0.4375 MHz (FDMA) ✓ | — | B2a 1176.45 / B2b 1207.14 MHz |
| L5 / safety-of-life | L5 1176.45 MHz | L3 1202.025 MHz ✓ (CDMA, GLONASS-K1/K2 only) | E5a 1176.45 / E5b 1207.14 MHz | B2a 1176.45 MHz |
| E6 / data | — | — | E6 1278.75 MHz (HAS) | B3I 1268.52 MHz |

GLONASS note: n is the satellite's frequency channel number (−7 to +6). ✓
The 14 primary channels (k = −7 to +6) have been in use since 2005; antipodal
satellite pairs share frequencies. L1 and L2 use **different** channel spacings —
0.5625 MHz vs 0.4375 MHz respectively. This matters for GLONASS
inter-frequency bias modelling. The `1230` RTCM message carries these biases
for rover compensation. GLONASS-K1/K2 satellites also broadcast CDMA signals on
L3 (1202.025 MHz), and K2 adds CDMA on L1/L2 — but CDMA GLONASS signals are
not yet tracked by the u-blox F9P or most hobbyist hardware. ✓

### 1.3 Why Band Count Matters for RTK

**Single-frequency (L1 only):**
- Cannot remove ionospheric delay; relies on Klobuchar model correction
  (~50% RMS removal globally; up to ~60% at mid-latitudes under quiet
  conditions; performance is worse at equatorial and high latitudes) ~
- Reliable RTK fix roughly within 10 km of base; degrades fast beyond that
- Increasingly uncommon in dedicated RTK hardware; avoid for new purchases

**Dual-frequency (L1+L2 or equivalent):**
- Forms the ionosphere-free (iono-free) linear combination: cancels
  ~99% of first-order iono delay ~
- Reliable fix out to ~30 km under typical ionospheric conditions; range is
  strongly ionosphere-dependent — the same hardware can hold fix at 50 km on
  a quiet day and fail at 20 km during a geomagnetic storm ~. Emlid RS2+
  published technical specification: 60 km RTK, 7 mm + 1 ppm horizontal ✓
  (formal product spec, not marketing copy — manufacturers understate in specs
  they can be held to legally; ionosphere is the dominant variable).
- The practical minimum for NTRIP RTK at useful baselines
- Examples: ZED-F9P (GPS L1/L2C + GLONASS L1OF/L2OF + Galileo E1/E5b +
  BeiDou B1I/B2I) ✓; Emlid RS2+

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
- Examples: ZED-F9P-**15B** (L1/L5 variant, distinct hardware from the
  standard L1/L2 F9P) ✓, Septentrio mosaic-X5 ~, Emlid RS3,
  survey-grade Trimble/Leica. Note: the standard ZED-F9P (most common
  hobbyist variant) is L1/L2 only, not L5 ✓.
  (source: Symmetry Electronics ZED-F9P-15B product page; alphamicro
  ZED-F9P variant comparison)

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

### 1.4 Signal Structure (GPS L1 example)

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

### 1.5 GNSS vs GPS — terminology note

"GPS" is often used colloquially to mean any GNSS. Modern receivers
track all available constellations simultaneously. A receiver described
as "GPS+GLONASS+Galileo+BeiDou" typically delivers better sky coverage
(more satellites visible), faster ambiguity resolution, and more
resilience to partial sky blockage than GPS-only.

### 1.6 Phone and Consumer Device Limitations

Modern flagship smartphones carry dual-frequency GNSS chips (L1+L5) yet
cannot perform centimetre-level RTK. There are three distinct barriers;
they do not all bind equally on iOS vs Android.

**iOS — OS API is the absolute blocker:**  
Apple's CoreLocation exposes only a processed `CLLocation` object (lat/lon/
altitude/accuracy) to third-party apps. No pseudoranges, no carrier-phase
(accumulated delta range), no per-satellite C/N0, and no RTCM injection
point exist in any public or private entitlement as of 2026. ✓
(source: Apple developer forums, confirmed by Apple engineer)  
Apps that appear to show GNSS signal quality on iOS are re-parsing the
processed CLLocation and almanac data — not reading raw observables from
the chip. An iOS NTRIP client app can fetch RTCM from a caster and relay
it byte-for-byte via Bluetooth to an *external* RTK receiver, but the
phone's own chip never receives those corrections. RTK on the internal
iPhone chip is impossible regardless of chip capability.

**Android — API works, duty cycling and antenna bind:**  
`android.location.GnssMeasurement` (API 24, Android 7+) exposes accumulated
delta range (ADR — the carrier-phase proxy), pseudorange, C/N0, and Doppler
per satellite. Raw measurement support is mandatory on Android 10+ hardware. ✓
ADR itself is not mandatory in the Android CDD — Qualcomm Snapdragon devices
historically do not report it. Broadcom-based Pixels (5, 6, 7, 8, 9 series)
do expose ADR. ✓ (source: Android developer docs, Broadcom BCM47765 data)

*Duty cycling* is the critical hidden problem: Android powers the GNSS chip
on ~200 ms then off ~800 ms each second to save battery, causing a carrier-
phase cycle slip every epoch. This makes the ADR stream useless for RTK
without mitigation. Android 9+ added "Force full GNSS measurements" (buried
in developer options) to disable duty cycling. Even with it enabled, thermal
throttling or low-battery states can re-enable duty cycling. ✓
(source: Barbeau 2018, GNSS Interrupted)

Observed RTK performance on Android phones with best-case conditions (Pixel 6
Pro, open sky, Force full GNSS on, short baseline, RTKLIB post-processing):
~0.2–0.5 m horizontal. Not centimetre-level. ✓
(source: Odolinski 2024 ION; GPS Solutions 2025 smartwatch/phone RTK study)

**Antenna — the residual binding constraint on Android:**  
Phone GNSS antennas are small PCB patches sharing RF space with 5G/Wi-Fi/BT.
Key differences from survey antennas:
- No RHCP polarisation → ground-reflected multipath signals are not rejected
  (RHCP antennas suppress reflected signals because reflection flips to LHCP)
- Phase center variation (PCV): **up to 2 cm at L1, up to 4 cm at L5** across
  the visible hemisphere, orientation-dependent ✓
  (source: Sensors 2024 — "Determining the Antenna Phase Center for
  High-Precision Positioning of Smartphones")
- C/N0 typically 8–10 dB-Hz below geodetic receivers ✓
  (source: Sensors 2023 GNSS Observation Generation paper)

A 4 cm L5 PCV — which shifts with hand grip — defeats integer ambiguity
resolution, which requires carrier-phase stability at the centimetre level.
This is why "phone RTK" papers reach decimetre accuracy regardless of chip or
API improvements. The University of Texas 2014 finding (still directionally
valid): the commodity Broadcom chip outperforms survey receivers in some signal
processing metrics; the antenna is what fails. ✓

Android 11 added `GnssAntennaInfo` (API 30) to expose PCO/PCV tables from the
OEM via the HAL. Most OEMs do not populate these tables; even where populated,
values are static and do not track orientation changes.

**Summary table:**

| Barrier | iOS | Android (Pixel 6+) |
|---|---|---|
| OS API — no raw carrier phase | **Hard block** | Not a block (ADR exposed) |
| Duty cycling — cycle slips per epoch | N/A | Soft block (dev option mitigates) |
| Antenna PCV / multipath | Contributes to noise | **Primary residual block** |
| Chip capability | Not the problem | Not the problem |

**Practical path for any phone user wanting centimetre RTK:**  
External u-blox F9P-based receiver (~$150–300, e.g. ArduSimple simpleRTK2B)
connected via Bluetooth. Phone runs an NTRIP client app that fetches RTCM from
a free public caster and relays it to the external receiver. The receiver
computes the RTK fix and outputs centimetre NMEA.

On Android: **Lefebure NTRIP Client** (Android-only) or **SW Maps** connects to
the receiver via Bluetooth and injects the corrected NMEA as a system-wide mock
location (developer option → "Select mock location app"), making all mapping
apps see centimetre accuracy without knowing about the external receiver. ✓  
On iOS: **no mock location injection API exists**. The GIS app itself must read
NMEA directly from the external receiver over Bluetooth and use it as its own
position source:
- **SW Maps** (iOS): reads NMEA via Bluetooth LE (BLE) from receivers with a
  BLE GATT profile (e.g. Emlid Reach RX/RX2, ArduSimple BLE adapters); free
  tier functional; also relays RTCM corrections to the receiver. ✓
  (source: SW Maps manual v3.0; ArduSimple iOS guide)
- **Emlid Flow** (iOS/Android): reads NMEA from Emlid Reach receivers via BLE
  or MFi Bluetooth Classic; forwards RTCM to the receiver over the same link.
  Reach RX/RX2 received Apple MFi certification July 2024. ✓
  (source: Emlid blog July 2024; Reach RX developer docs)
- **ArcGIS Field Maps** (iOS): requires an Apple MFi-certified receiver
  (Eos Arrow, Trimble, Emlid Reach RX/RX2, Bad Elf, Geneq SxBlue). Without MFi,
  the app cannot open a Bluetooth Classic RFCOMM channel to the receiver. ✓
  (source: ArcGIS Field Maps documentation — high-accuracy data collection)
- **QField** (iOS): **does not support Bluetooth GNSS on iOS**; the receiver
  must stream NMEA over TCP/IP and QField acts as a TCP client. On Android,
  QField supports Bluetooth directly. ~
  (source: QField GNSS positioning docs; ArduSimple QField iOS guide)
- **iCMTGIS PRO** (iOS): direct BT support for listed receiver models (Eos Arrow,
  Bad Elf, Geneq SxBlue, Juniper GNS3, and others). ~

**Apple Bluetooth constraint:** iOS blocks third-party apps from using Bluetooth
Classic RFCOMM (SPP profile) without Apple MFi hardware certification. BLE does
not require MFi. Modern GNSS rovers use BLE to avoid this gate. ✓
(source: Eos GNSS — iOS and Bluetooth overview)

The phone's internal chip is not involved in the RTK computation in either case.

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

**Receiver-displayed accuracy vs actual position error.** The numbers
above describe what error survives *into* the solution. The accuracy
figure your receiver *displays* (HDOP, HPA, estimated position error)
is a different quantity: HDOP × σ_UERE, where σ_UERE is a fixed
internal constant, or the diagonal of the Kalman filter covariance
matrix. Neither of these tracks site-specific multipath, atmospheric
spatial gradients, or base-station coordinate errors in real time —
they capture only what the receiver's internal stochastic model
assumes. Several important consequences follow from this gap:

- **Multipath is the largest excluded source.** In an open field it
  contributes <1 mm to carrier-phase error; beside a metal building it
  can introduce 2–5 cm of systematic bias — yet the displayed HPA is
  identical in both environments.
- **Temporal correlation is ignored.** Standard covariance propagation
  assumes white noise. GNSS errors (especially multipath and atmospheric
  residuals) are correlated over minutes to tens of minutes; ignoring
  this makes the formal covariance overly optimistic. ~ (RTKLIB docs;
  ResearchGate RTK VCM studies; ScienceDirect unmodelled-error paper 2022)
- **The gap is largest in RTK Float mode** (sub-dm display; actual
  error can be 1–5 m) and in DGNSS mode (sub-m display; actual error
  can be 5–40 m in urban canyons). RTK Fix in clean conditions is the
  mode where the displayed figure is most likely realistic.
- Industry and academic sources (RTKLIB, Swift Navigation, NovAtel,
  published VCM studies) consistently describe formal covariance
  estimates as "optimistic" in real-world deployments. ✓

Mode-specific breakdowns follow in §3.2 (DGNSS), §3.3 (RTK), and
§3.5 (PPP).

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

**Failure envelope:** those figures apply to open sky with a short
baseline and no obstructions. The receiver computes its displayed
accuracy as HDOP × σ_UERE, where σ_UERE is a fixed internal constant
calibrated for open-sky conditions — the receiver has no real-time
knowledge of site-specific multipath. ~ (NovAtel GNSS Error Sources;
Penn State GEOG 862, UERE node) Multipath and non-line-of-sight (NLOS)
signals are local to your antenna and survive differential correction
entirely uncancelled: in a dense urban canyon they contribute 5–40 m
of undetected pseudorange bias per satellite while the receiver display
may still read "1 m." ✓ (IEEE Trans. ITS 2023, arXiv:2206.04457;
NovAtel; Frontiers Robotics AI 2022) A perverse trap: in urban canyons
HDOP can appear *low* because many reflected-signal satellites are
tracked, masking the degradation rather than exposing it. Under suburban
tree canopy or close to buildings, expect 2–5 m actual horizontal error
regardless of the displayed figure. ✓ (PLOS ONE 2023; MDPI Sensors 2024)

SBAS (WAAS, EGNOS, MSAS, GAGAN, SDCM) broadcasts DGNSS corrections
via geostationary satellite — no internet connection needed, but
accuracy ceiling is ~1 m. SBAS has the same structural limitation as
terrestrial DGNSS: multipath is not corrected and the displayed accuracy
uses an open-sky UERE assumption. ~ This is why DGNSS-only NTRIP mountpoints
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

**Accuracy display and false-fix caveat.** The Fix label and stated
precision (HPA ~10–20 mm) are derived from Kalman filter covariance —
they reflect satellite geometry and receiver noise, not actual position
error. A **false fix** occurs when the ratio test accepts a wrong set
of integers: the receiver continues displaying "Fix" and centimetre
precision while the position is offset by multiples of the carrier
wavelength (~19 cm per wrong integer, typically 0.3–1 m in practice
when several integers are incorrect). ~ (rtklibexplorer; Li & Shen,
J. Geodesy 2014) The receiver has no independent ground truth and
cannot distinguish a false fix from a valid one; there is no alarm,
LED change, or output flag. Risk is highest under multipath, with
fewer than 8 satellite pairs, on a long baseline, or with single-
frequency receivers — published single-frequency false-fix rates
reach ~15% of epochs. ✓ (PMC/Sensors 2019 smartphone RTK study;
Emlid Community Forum M2 false-fix thread)

**Float drift mechanism.** In float mode the carrier-phase integer
ambiguities are estimated as real-valued Kalman filter states coupled
to the position estimate. As the ambiguities slowly converge, the
position shifts with them; any unmodelled ionospheric or tropospheric
change injects a smooth, correlated bias into both the ambiguity and
position states simultaneously. This produces gradual positional
drift — no obvious jumps, no alarm — that is invisible from the
displayed accuracy. Under forest canopy or urban obstruction, where
unmodelled multipath further corrupts the float ambiguities,
field-measured float errors reach 1–2 m even with an active
correction stream. ✓ (CREWES Research Report 2010; PMC 2023
canopy study)

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

**Accuracy specification: the ppm term**

RTK accuracy is quoted as a fixed term plus a distance-dependent term,
e.g. Emlid RS2+: "7 mm + 1 ppm horizontal." ✓
(source: Emlid RS2+ technical specification)

- **Fixed term (7 mm)**: irreducible hardware noise floor — receiver noise,
  antenna phase-centre variation, base multipath. Present even at zero baseline.
- **ppm term**: 1 ppm = 1 part per million = **1 mm of error per km of
  baseline**. ✓ (source: NOAA NGS User Guidelines for Single Base Real Time
  GNSS Positioning v3.1)

Total ≈ fixed\_mm + (ppm × baseline\_km):

| Baseline | 0.5 ppm | 1 ppm | 1.5 ppm | 2 ppm |
|---|---|---|---|---|
| 1 km | 0.5 mm | 1 mm | 1.5 mm | 2 mm |
| 5 km | 2.5 mm | 5 mm | 7.5 mm | 10 mm |
| 10 km | 5 mm | 10 mm | 15 mm | 20 mm |
| 20 km | 10 mm | 20 mm | 30 mm | 40 mm |
| 30 km | 15 mm | 30 mm | 45 mm | 60 mm |

For a 7 mm + 1 ppm receiver: the ppm term equals the fixed term at ~7 km and
dominates beyond ~10 km. At 20 km the total quoted spec is ~27 mm horizontal;
at 30 km, ~37 mm.

**Physical causes of the ppm error:** Residual ionospheric gradient (dominant:
~60–80% of the ppm budget) — the differential iono delay between base and rover
after dual-frequency cancellation; it grows with separation (~0.5–3 cm across a
30 km baseline under quiet conditions). Tropospheric wet-component gradient is
secondary (~15–30%). Broadcast orbital error is minor (~0.2 ppm). ~

During geomagnetic storms the effective ppm can multiply dramatically: a Kp 7
(G3) storm collapses IAR success rate from 94% to 31% (SWSC 2012 ✓), so a user
who normally holds fix at 20 km may find that baseline entirely unusable during
the storm. The fixed term is unaffected; only the distance-dependent term
degrades (see §7.3 for Kp thresholds).

**Network RTK (VRS) nearly cancels the ppm term:** the server models iono and
tropo gradients across the network and synthesises corrections for a virtual
reference at the rover's location (~0 km effective baseline). A user 20 km from
the nearest physical station in a VRS network gets ~7–8 mm horizontal rather
than ~27 mm, because the ppm residual of the network's iono model (~0.5 ppm
of near-zero effective distance) is negligible. ~

**VRS edge-of-network failure modes.** That cancellation holds when the rover
is inside a well-spaced network (stations ≤ 70 km apart, calm ionosphere, flat
terrain). It breaks down in four situations:

1. **Outside the network hull:** the caster silently switches from interpolation
   to extrapolation with no notification in the RTCM stream — height errors of
   ~51 mm have been documented 10.5 km outside the hull; in field tests 30 km
   outside, horizontal error stayed ~6 cm but vertical reached several metres. ~
   (ResearchGate 254250991; IEEE 5069258)
2. **Ionospheric storms:** the same 94%→31% IAR success rate collapse described
   above applies to NRTK; decimeter-level horizontal errors occur even inside the
   network. ✓ (J. Geodesy 2005, Springer doi:10.1007/s00190-005-0003-y)
3. **Steep terrain:** when the rover is significantly above surrounding reference
   stations, the tropospheric correction extrapolates vertically — uncorrected
   height error is ~27 cm per 1,000 m of altitude difference. ~
   (GPS Solutions 2023, doi:10.1007/s10291-023-01481-x)
4. **Sparse networks (station spacing > 70–100 km):** the atmospheric
   interpolation is too coarse for reliable instantaneous ambiguity fixing. ~

In all four cases the rover's displayed HRMS, fix status, and PDOP reflect
satellite geometry and ambiguity resolution — not correction quality. There is no
standard quality-of-interpolation field in the RTCM 3.x message format; research
has called for adding one but it has not been standardised. ✓
(Southern Alberta Network RTK study, ResearchGate 228734118)

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

**Convergence time:** ~ Standard float PPP (GPS+Galileo): typically
20–30 min to reach cm-level accuracy. PPP-AR (integer ambiguity
resolution, e.g. CSRS-PPP with AR mode): can reach cm-level in
10–20 min. These are different service tiers — don't conflate them.

Galileo HAS (free broadcast PPP-RTK on E6-B, no subscription, no
base station): official target convergence <300 s (~5 min); observed
in 2024 studies is 7.5–15 min for GPS+Galileo static. Sub-20 cm
horizontal at 95% after convergence ✓. QZSS CLAS (Japan/Asia-Pacific
only): official spec <6 cm horizontal / <12 cm vertical (static) ✓;
typical observed performance 1.3–2.7 cm horizontal (95%) ~. Both services work
anywhere with satellite visibility and are the recommended alternative
for users who cannot connect to an NTRIP caster.

**Galileo HAS hardware requirements**

HAS corrections are broadcast on **Galileo E6-B** (1278.75 MHz). Receiving them
requires a receiver that physically tracks the E6 band — firmware updates cannot
add E6 capability to hardware built for other bands.

| Receiver | E6/HAS support | Notes |
|---|---|---|
| **Unicore UM980 / UM982** | Native; enable via signal-group config | Most accessible hobbyist option; ~$100–200 bare module (ArduSimple, SparkFun). SparkFun 78-trial test: avg ~77 mm post-convergence, best observed 33 mm, avg convergence 9.8 min (excl. outlier) ✓ (source: SparkFun UM980 HAS E6 convergence test repo) |
| **Septentrio mosaic-X5** | Firmware v4.14.0+ (2024) | Used in peer-reviewed HAS papers; outputs raw E6-B pages for HASlib/RTKLIB pipeline ✓ (source: mosaic-X5 firmware v4.14.10 reference guide) |
| **Trimble R10 / R580 / R750** | Firmware v6.28+ (Jan 2025), enabled via TIM | Requires active options unlock for Galileo tracking ✓ (source: Trimble "What's new in 6.28") |
| **Eos Arrow Gold+** | Native | Described as first GIS-market device with HAS support ✓ (source: Eos press release) |
| **Quectel LG290P** | Hardware present; HAS firmware Oct 2025 | Quad-band L1/L2/L5/E6 ✓ (source: Quectel HAS announcement Oct 2025) |
| **u-blox ZED-F9P (all variants)** | **None — impossible** | Tracks L1+L2 (or L1+L5 for **-15B**). No E6 hardware exists in any F9 chip. No firmware update changes this ✓ (source: u-blox community forum; F9P product summary) |
| Smartphones (all) | None | No consumer GNSS chipset supports E6 as of 2026 ✓ |

**IDD (Internet Data Distribution):** The identical HAS corrections are also
available via NTRIP from the GSC caster. Requires free registration via the GSC
portal; connection slots are limited and granted per organisation rather than to
individual users — not a mass-market drop-in for NTRIP RTK. ~
(source: GSC HAS IDD registration page)

**Open-source HAS decoders** (for receivers that output raw E6-B pages):
- **HASlib** (NLS-FI, Python; github.com/nlsfi/HASlib v1.0.2): combined with
  RTKLIB, achieves sub-20 cm 3D at 1σ after ~10 min on Septentrio hardware ✓
  (source: GPS Solutions 2024, Prol et al.)
- **HASPPP** (Wuhan University, C/C++; github.com/ZhangRunzhi20/HASPPP):
  embeds HAS decoding directly into the RTKLIB PPP engine ~

**Non-monotonic convergence.** PPP convergence is not a smooth one-way
descent to accuracy. The Kalman filter's internal confidence estimate
(what the receiver displays) shrinks relatively smoothly, but the actual
position error oscillates around that trend. Every time a new satellite
enters the solution, a carrier-phase cycle slip occurs, or the
ionospheric delay shifts abruptly, the position estimate can jump by
centimetres or decimetres before the filter re-absorbs the disturbance.
The displayed accuracy can remain optimistically small for several epochs
after accuracy has temporarily worsened, because the filter's noise model
does not immediately account for the new uncertainty. ~ (FIG 2016,
Choy et al.; Springer ScienceDirect, Dai et al. 2020; ESA Navipedia PPP)

**Signal interruption and re-convergence.** Any carrier-phase tracking
break resets the corresponding ambiguity states. On a standard float PPP
receiver, a full-sky blockage (bridge overpass, tunnel) requires 10–30 min
to re-converge; a partial blockage affecting a few satellites takes less
but still several minutes. On a PPP-AR receiver with atmospheric state
bridging (NovAtel TerraStar-D, Septentrio with SPARTN), a 5-second
interruption can recover in 1–3 minutes because the filter preserves the
ionospheric and tropospheric state estimates across the gap. ✓ (NovAtel
Velocity 2014; Banville & Langley, ResearchGate 289224452; FIG 2016)

**Galileo HAS Phase 1 early-convergence accuracy.** HAS Phase 1
(currently available) does not include satellite phase bias products,
meaning it is float-only PPP — no PPP-AR. During the first 1–3 minutes,
horizontal error is typically 0.5–3 m. The official target of <300 s /
<20 cm horizontal at 95% is not met in practice until 6–15 min static
(GPS+Galileo). In urban environments with frequent signal loss, HAS
provides only marginal improvement over broadcast-only positioning
because constant re-convergence prevents accumulation of ambiguity
estimates. ✓ (Eos HAS field tests 2023; Inside GNSS HAS urban driving
assessment Feb 2024; ENC 2025 HAS accuracy paper)

HAS is suitable for open-sky static or slow-moving use and unsuitable
for urban canyons or forested routes. NTRIP RTK re-acquires fix within
seconds after a brief obstruction; HAS cannot. ~
(source: SparkFun UM980 test; GPS Solutions 2024; NAVIGATION journal 2024)

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

~ Increasingly unsupported by modern firmware. The u-blox F9P does
not support RTCM 2.x output or input in any released firmware. The
popup in this project warns when a mountpoint is RTCM 2.x only.

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

| MSM level | Pseudorange | Carrier phase | Doppler | CNR | Notes |
|---|---|---|---|---|---|
| MSM1 | compact | — | — | — | Phase-range only, minimal bandwidth |
| MSM2 | — | compact | — | — | Phase-range only |
| MSM3 | compact | compact | — | — | |
| MSM4 | full | full | — | half-cycle | Most common RTK baseline |
| MSM5 | full | full | full | half-cycle | Adds Doppler; used where velocity matters |
| MSM6 | full high-res | full high-res | — | full | High-res without Doppler |
| MSM7 | full high-res | full high-res | full | full | Max precision; preferred for quality bases |

Base numbers per constellation:
- GPS: 1071–1077
- GLONASS: 1081–1087
- Galileo: 1091–1097
- SBAS: 1101–1107
- QZSS: 1111–1117 ✓
- BeiDou: 1121–1127 ✓
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
- GPS: 1057–1062 (orbit 1057, clock 1058, code bias 1059, combined 1060, URA 1061, high-rate clock 1062)
- GLONASS: 1063–1068 (orbit 1063, clock 1064, code bias 1065, combined 1066, URA 1067, high-rate clock 1068)
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
| SPARTN | u-blox (via Sapcorda JV acquisition 2021) ~ | SSR compressed; used by PointPerfect; Swift and Septentrio are licensees/decoders, not developers |
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

### 5.9 NTRIP Client Software

Common client implementations hobbyists encounter:

| Client | Platform | Notes |
|---|---|---|
| **SW Maps** (Aviyaan Tech) | Android + iOS | Popular field GIS; connects to NTRIP and forwards corrections to paired receiver via Bluetooth; free tier functional. Android: uses BT Classic or BLE; iOS: BLE only ✓ |
| **RTKLIB rtkrcv / str2str** | Linux/macOS/Windows | CLI-based; str2str can relay an NTRIP stream to serial/USB/another TCP port; used in RTKBase |
| **RTKLIB RTKGET** | Windows | GUI download tool; fetches RINEX from NTRIP; not real-time |
| **Lefebure NTRIP Client** | **Android only** | Bare NTRIP client; pairs with Bluetooth GPS receivers; mock-location injection; no iOS version exists ✓ |
| **BNC (BKG Ntrip Client)** | Desktop | Advanced; can decode, log, QC, relay, and inject streams; mainly for analysis |
| **u-center** (u-blox) | Windows | Can act as NTRIP client and push corrections to a connected F9P via USB; useful for bench tests |
| **Emlid Flow** | iOS/Android | For Emlid Reach receivers; built-in NTRIP client; RTCM relay to receiver over Bluetooth; requires Emlid hardware ✓ |

~ For hobbyist rover use in the field, SW Maps + a Bluetooth GNSS receiver
(F9P-based) is the most common Android stack. For a permanent base setup,
RTKBase's built-in source-push to an NTRIP caster replaces the need for a
separate client.

### 5.10 App Connection Display — What Fix Looks Like

Understanding visual indicators prevents misinterpreting Float accuracy as Fix
accuracy, or missing a stale-stream failure.

#### SW Maps (Android / iOS)

**Position bubble colour on the map** ✓ (source: SW Maps manual v3.0;
ArduSimple "How to use SW Maps"):

| Colour | Fix state | Meaning |
|---|---|---|
| Blue | Standalone GNSS | No corrections applied; ~1–5 m |
| Orange | RTK Float | Corrections flowing; integer ambiguities unresolved; sub-metre |
| Green | RTK Fix | Ambiguities resolved; ~1–3 cm |

**Status bar buttons** (left to right in app toolbar):
1. Bluetooth connection button — receiver link state.
2. **NTRIP status**: green = corrections fresh; **orange** = age of differential
   high (stale stream, degraded accuracy). ✓
3. Satellite/fix button — count and fix type.
4. **HPA button** — current horizontal positional accuracy in metres (e.g.
   "0.014 m" = 14 mm). At RTK Fix, HPA drops below 20 mm. ✓

**GNSS Status screen** (menu → GNSS Status): fix type (GNSS / DGNSS / RTK Float
/ RTK Fix derived from NMEA GGA quality field), PDOP, HDOP, satellite count, age
of differential, reference station ID.

**Minimum quality filter:** configurable — set to "RTK Fix only" to prevent
logging Float-quality points.

#### Emlid Flow (iOS / Android — for Reach hardware)

**Solution status widget** (persistent, top-right corner of every screen) ✓
(source: Emlid Flow glossary; Reach RX documentation):

| Text | Fix state | Typical accuracy |
|---|---|---|
| SINGLE | No corrections | ~1–3 m |
| FLOAT | Corrections received; unresolved | ~10–50 cm |
| FIX | Centimetre solution | ~1–3 cm |

A **"Fixed Solution Notification"** banner/toast appears at the moment of
transition from FLOAT to FIX.

**Status drawer** (tap the status bar to expand): coordinates, PDOP, satellite
count in use, age of corrections in seconds.

**Correction age thresholds** ~ (firmware-version dependent; Emlid community forum; Reach RX docs):
- **> 5 s**: app flags potentially unstable connection (early warning).
- **> 10 s**: receiver typically drops from Fix back to standalone or float GNSS. ~

**Reach hardware LED** (Reach RX, firmware v1.4) ✓ (source: Reach RX User
Documentation v1.4):

| LED colour | Solution |
|---|---|
| White | SINGLE |
| Yellow | FLOAT |
| Green (solid) | FIX |

**Typical numbers at RTK Fix:**

| Metric | Expected value |
|---|---|
| HPA | 10–20 mm at ≤ 10 km baseline; 30–50 mm at 30–50 km |
| Vertical accuracy | ~1.5–2× horizontal |
| Correction age at fix | 0–2 s |
| PDOP | ≤ 2.0 for reliable fix; > 4 makes fix unlikely |
| Satellites in use | ≥ 10 multi-constellation |
| Time to first fix | 5–30 s open sky, multi-band; minutes in marginal sky |

### 5.11 Rover-Side Registration by Network

Registration requirements for connecting as a **rover** (not as a base
operator — see §10.4 for base station registration).

**rtk2go** (`rtk2go.com:2101`)  
No account required. Username = any syntactically valid email (not validated
against any inbox). Password = the literal string `none`. Connect immediately. ✓
Regional views: port 2103 (Poland), 2104 (Japan); same credentials.

**Centipede** (`crtk.net:2101`)  
No account required. Username = `centipede`, password = `centipede`. ✓  
⚠ Host migrated from `caster.centipede.fr` to `crtk.net` on 2025-03-18.
Old instructions referencing `.fr` will fail. ✓

**SAPOS** (Germany — all 16 states, `sapos.de`)  
Registration required per state via that state's land survey office portal.
States are independent — credentials for one state do not work in another. Most
states: free, near-immediate web self-service. **Bavaria (BY): €20/year** for
non-agricultural users; agriculture/forestry free with eAMA farm credentials. ✓  
SAPOS uses NTRIP 1.0 raw TCP; clients expecting HTTP receive
`SOURCETABLE 200 OK` and may fail. All SAPOS streams are VRS — rover must send
GGA. ✓

**AUSCORS** (Australia, `ntrip.data.gnss.ga.gov.au:2101`)  
Free registration at `gnss.ga.gov.au/registration`; near-immediate automated
approval. CC BY 4.0 attribution required. **Port 443 (TLS) also available** —
passes corporate and campus firewalls that block 2101. ✓  
Old host `auscors.ga.gov.au` is dead since July 2022. ✓

**PositioNZ** (New Zealand, `positionz-rt.linz.govt.nz:2101`)  
Requires a LINZ portal account (`linz.govt.nz`) — a general government login,
not NTRIP-specific. Near-immediate self-service. CC BY 4.0 NZ. ✓

**EarthScope NOTA** (Americas, `ntrip.earthscope.org:2101`)  
Free registration via `earthscope.org/data/gnss-realtime/`. Requires accepting
the **NULA (Network Use Licence Agreement)** annually — access lapses if not
renewed each year. Non-commercial use only. ✓  
⚠ Legacy UNAVCO URLs (`rtgpsout.unavco.org` etc.) are dead since
2025-07-29. ✓

**TrigNet** (South Africa, `trignet.co.za:2101`)  
Free registration at `trignet.co.za`; NGI administers approval — typically a
few business days. ✓

**Slow or unusual registrations:**
- **ASG-EUPOS** (Poland): admin approval 1–2 working days.
- **MIRAI / Go!GNSS** (Japan): two separate forms (portal + NtripCaster
  authorisation); accounts expire after **365 days of inactivity**. ~
- **MoDOT RTN** (Missouri, USA): requires a **signed and notarised access
  agreement** before credentials are issued. ~
- **CORS-KOREA** (South Korea): portal is Korean-language; access may require a
  Korean national ID; international access may be impractical. ~
- **SatRef HK** and **MIRAI** (Japan): accounts inactive 12 months are
  terminated. ~

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

Jointly developed by Geo++ (Germany) and Leica Geosystems (Switzerland). ~

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
a spatial gradient model (area correction parameters); rover evaluates
the polynomial at its own position rather than receiving a synthetic
stream. Originally transmitted in proprietary RTCM type 59 (Geo++
message); standardised as RTCM 3.x message 1034 (GPS Network FKP
Gradient) ✓. Operationally identical to VRS for this project: FKP
mountpoints carry NMEA=1 (rover must send position) and are dropped.

**i-MAX** ~ (Trimble): combines VRS and MAC ideas. Appears in some German
and Swiss networks. Also NMEA=1 → dropped by the same filter.

### 6.4 What this project shows

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
at L1: ~0.162 m per TECU ✓ (formula: 40.3×10¹⁶/f² m/TECU, f in Hz;
at L1 1575.42 MHz → 40.3×10¹⁶ / (1575.42×10⁶)² ≈ 0.162 m/TECU).
Note: the ionosphere advances the carrier phase by the same amount it
delays the pseudorange (opposite sign) — this matters for PPP
ambiguity resolution but not for RTK double-differencing.
During quiet conditions, vertical TEC over mid-latitudes is ~5–20 TECU;
during severe storms it can reach 200+ TECU over some regions. ~

### 7.2 Solar Cycle

The Sun follows an approximately 11-year activity cycle. ~

- **Solar maximum**: increased UV and X-ray flux ionises more
  electrons; higher TEC, more variability, more frequent geomagnetic
  storms. Solar Cycle 25 peaked in October 2024 (smoothed sunspot
  number 160.8, substantially exceeding the original prediction of ~115) ✓ —
  the 2025–2026 period is declining phase but still elevated; expect
  above-average RTK degradation risk until ~2027–2028. ✓
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
chip length. GPS C/A chip ≈ 293 m ✓ → theoretical half-chip maximum
≈ 146 m (for a reflected signal equal in amplitude to the direct),
but narrow correlator design limits the practical multipath error
envelope to ~5–15 m for modern consumer receivers; real-world values
above 15 m are rarely observed ✓. P-code chip ≈ 29.3 m → theoretical
half ≈ 15 m. Average real-world C/A pseudorange multipath: 0.5–3 m. ✓

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
- Supports GPS L1C/A+L2C, GLONASS L1OF+L2OF, Galileo E1B/C+E5b,
  BeiDou B1I+B2I ✓ (note: E5b not E5a; L1/L2 not L5)
- RTCM 3.3 MSM4/MSM7 output ✓
- Raw observable output for post-processing ✓
- Up to 20 Hz output rate (1 Hz is standard for NTRIP base use) ~
- ~$88–180 for bare module (price has fallen since 2022); ~$200–400
  in breakout boards (ArduSimple simpleRTK2B, SparkFun GPS-RTK2) ~

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
  kinematic modes; returns both ITRF and NAD83 coordinates ✓. 24h
  observation → cm-level absolute accuracy ✓. Most useful service for
  non-Canadian users who want ITRF; NAD83 vs ITRF difference is typically
  0.5–1 m in North America and ~0.1–0.3 m elsewhere (epoch-dependent
  plate-motion correction included in output).
- **AUSPOS** (Geoscience Australia) — similar free web PPP service; returns
  ITRF2014 coordinates; recommended for users in the Asia-Pacific region ~
- GIPSY-OASIS (JPL) — similar, free for non-commercial ~

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

### 10.8 RINEX Logging and Post-Processing

RTKBase logs raw observations to RINEX format (via RTKLIB's convbin
tool) alongside the real-time NTRIP source function. This enables two
additional use cases beyond live RTK corrections:

**PPP base position determination (§10.3 Method B):**  
Upload the RINEX observation file from the first 24h of base operation
to NRCAN CSRS-PPP (free). The service returns ITRF and NAD83 coordinates
with cm-level absolute accuracy. Copy the ECEF or ellipsoidal coordinates
into RTKBase's fixed-mode configuration to freeze the base position.

**Post-processed kinematic (PPK):**  
A rover recording raw RINEX observations in the field (e.g. a drone with
an F9P logging module) can be post-processed against the base RINEX file
using RTKLIB RTKPOST or RTKLIB-Explorer forks. PPK achieves the same 1–3 cm
accuracy as real-time RTK but without a live internet link — important for
UAV mapping where cellular connectivity is unavailable. The base RINEX
log is the enabling asset.

**RINEX file naming convention (standard):**  
RINEX 3.x: `<StationName><MonumentCode>_R_<YYYY><DDD><HH><MM>_<duration>_<interval>_<system>O.rnx`  
RINEX 2.x: `<station><DDD><session>.<YY>o`  
RTKBase uses RINEX 3.x by default and rotates files hourly. The `.ubx`
raw binary file is also retained, which can be re-converted to RINEX with
different settings if needed.

---

## 11. Common Troubleshooting Scenarios

This section maps frequent user symptom reports to likely causes and
diagnostic steps. "User" refers to a hobbyist connecting to one of
the free NTRIP networks on this project's map.

### 11.1 "I connected to NTRIP but I'm getting Float, not Fix"

Float means corrections are flowing but integer ambiguities are not
resolved. Most likely causes in descending order:

1. **Baseline too long** — the selected mountpoint is >30 km away.
   Solution: choose a closer station. Check map at close zoom.
2. **Poor sky visibility** — fewer than 5–6 satellites with clean
   signal prevents IAR. Check PDOP/satellite count in rover display.
   Move to open sky; wait for satellite geometry to improve.
3. **Elevated ionospheric activity** — check current Kp at swpc.noaa.gov.
   If Kp ≥ 5, RTK may be unreliable; wait for conditions to improve.
4. **Receiver warmup** — immediately after connecting, float is normal.
   Allow 30–120 s in good conditions.
5. **Format mismatch** — rover doesn't support the stream format (e.g.
   legacy RTCM 2.x from an old base). Check legacyFormat flag in popup.
6. **Missing 1005/1006** — base position message absent from stream.
   The rover cannot compute a baseline without it. Check with SNIP or
   str2str monitor. This is rare on established networks.

### 11.2 "Fix drops every few minutes"

Most likely: intermittent internet connectivity causing correction age
to exceed the receiver's timeout (60 s default on F9P). Steps:
1. Check NTRIP client's correction age display.
2. Disable battery optimisation for the NTRIP app on Android.
3. Test with a cellular data speed test — if latency spikes >500 ms,
   move to better cellular coverage or switch to a closer caster
   (fewer WAN hops).
4. Consider a local str2str relay: `str2str -in ntrip://... -out tcpsvr://:2101`
   on a laptop caches the stream and decouples the rover from cellular.

### 11.3 "RTK worked last week, nothing has changed" / Mountpoint Disappeared

If nothing physical changed (same location, same hardware):

1. **Check if the mountpoint disappeared.** Volunteer base stations disconnect
   silently and are **removed from the caster sourcetable immediately** — SNIP
   drops a dead stream within seconds; there is no grace period. Reload this
   project's map and look for the pin. If it is gone, treat the mountpoint as
   unavailable and use the recovery paths below.
2. **Check space weather.** A geomagnetic storm degrades RTK long after the Kp
   index falls; residual ionospheric disturbances (TIDs) can prevent fix for
   12–24 h after the storm nominally ends. Check current and past-3-h Kp at
   swpc.noaa.gov (see §7.3 for Kp thresholds).
3. **Check if the caster's sourcetable changed.** The base may have changed its
   format descriptor or reported coordinates; some rover software rejects a
   stream if mountpoint metadata has changed.

**Why volunteer mountpoints disappear (rough frequency order):**  
Dynamic IP address change after ISP reboot or DHCP renewal (the base software's
outbound NTRIP push fails to reconnect when the address changes); power outage
at the base computer with no UPS; hardware failure (receiver or cable); operator
moves house, sells hardware, or loses interest; router/firewall change blocking
outbound port 2101; OS or RTKBase software update breaking the auto-start
service. ✓ (source: rtk2go documentation; SNIP knowledge base)

**How long does a disconnected mountpoint stay visible?**  
It disappears **immediately** from the live sourcetable. rtk2go explicitly
documents: "Your base station name will not appear in the NTRIP caster tables
unless it is actively connected and sending data." ✓ The registration entry
persists indefinitely in rtk2go's database — no automatic inactivity expiry has
been documented; an operator can reconnect any time and be live instantly.

**Scale:** Only ~800 of rtk2go's ~11,000 registered mountpoints are active at
any given time (~7% — inferred from rtk2go connection statistics). rtk2go's
documentation notes "50,000–150,000 connections per day" include many attempts
to reach disconnected streams. ✓

**Recovery paths:**
1. Use this project's map to find the nearest alternative physical-station pin.
   Check the SNIP::STATUS page at `rtk2go.com:2101/SNIP::STATUS` for per-stream
   uptime percentages and live data flow rates.
2. Switch to the national survey network for your region (see §5.11 for
   registration). Government-operated networks have monitored uptime and
   systematic repair vs volunteer best-effort. Registration is usually free and
   near-immediate.
3. For a **Centipede** station: the network map at centipede-rtk.org/maps shows
   red/green status updated every 30 seconds; operators receive automated email
   if their station has been offline > 5 minutes. ~
4. Contact rtk2go support (`support@use-snip.com`) to ask whether a specific
   mountpoint is permanently removed or temporarily offline. Operator email
   addresses are not exposed in the sourcetable. ✓

**Reliability expectations:** A well-maintained volunteer station can sustain
99 %+ uptime; many run intermittently or seasonally. For mission-critical work
(legal surveys, production machine control, regulatory deliverables), use a
government CORS or commercial network with a monitored SLA as the primary
source and treat volunteer bases as gap-filling secondaries.

### 11.4 "I get Fix but the position seems wrong by a metre or more"

This is the "fixed but wrong" scenario. Most likely causes:

1. **Base position set from short survey-in** — if the base used a
   30-second or 5-minute survey-in (typical default), its reported
   position may be 1–3 m off absolute. All rover fixes are correct
   relative to that base, but wrong in absolute terms. Solution:
   switch to a network caster (this project's sources), not a private
   volunteer base.
2. **Wrong coordinate frame** — if the base uses a local datum that
   doesn't match the rover's display datum, there will be a systematic
   offset. ITRF coordinates from PPP do not equal local datum
   coordinates (difference is typically 0.2–2.2 m depending on region
   — see §13.1 for per-region numbers). For survey work, apply a datum
   transformation.
3. **Cycle slip that went undetected** — a cycle slip during a multipath
   event can shift the fix by an integer number of carrier wavelengths
   (~19 cm at L1). The receiver reports "Fix" but the solution jumped.
   Reacquire fix in clean sky; compare before and after.

### 11.5 NTRIP Connection Fails (Firewall / Port-Blocking)

NTRIP runs over plain TCP on whatever port the operator configured. Port 2101
is convention, not a registered or whitelisted port. The symptom depends on
where and how the connection is blocked.

**Symptom → cause mapping:**

| Symptom | Likely cause |
|---|---|
| Hangs 10–30 s, then "Connection timed out" | Outbound TCP blocked by firewall (SYN dropped, no reply) |
| "Connection refused" immediately (< 1 s) | Port reachable but no service listening (wrong port, caster down) |
| TCP connects, then garbled text or no data | Protocol mismatch: HTTP client sent to NTRIP 1.0 raw-TCP caster (common with SAPOS) |
| TCP connects, authenticated, zero RTCM bytes | VRS mountpoint waiting for GGA; enable GGA output in the NTRIP client |
| "Bad password" / "401 Unauthorized" in under 1 s | Credentials wrong; network layer is fine |

**Common blocking contexts:**

- **Corporate / campus WiFi** — most common block. Standard egress policies
  whitelist 80, 443, 8080, 25, 587. Port 2101 is not in any standard whitelist
  and is blocked on managed networks. Non-standard ports (Leica GNSS Spider
  defaults: 9879, 10011, 10700; others: 5005, 5001, 2001, 10000) are even more
  likely to be blocked. ✓
- **Public WiFi (hotel/airport/café)** — many allow only 80/443 outbound.
- **Consumer mobile 4G/5G** — generally does **not** block outbound TCP on
  arbitrary ports; port 2101 works over LTE/5G in most regions. ✓
- **Enterprise/IoT SIM plans** — carrier APNs may whitelist specific ports only;
  verify with the SIM provider before deploying fixed-install rovers.

**Why this project's CI times out on FLEPOS, WALCORS, ESTPOS, LatPos, KSA-CORS:**
GitHub Actions runner egress filtering blocks non-standard high-numbered ports.
LatPos on port 5001 and others are consistent with this — the casters are likely
fine; the runner network is blocked. (See CLAUDE.md §Current state.)

**Firewall-transparent alternatives:**
- **AUSCORS** supports **port 443 (TLS)** in addition to 2101 — passes virtually
  all firewalls and adds encryption. The only free public network in this
  project's pipeline with a documented port-443 option. ✓
- **FReDNet** (Italy/OGS) uses port **8080**, which passes many enterprise
  firewalls. ✓

**Diagnostic steps:**
1. **Switch to mobile data.** If it connects on LTE but not on WiFi, the WiFi
   firewall is the problem.
2. **Test the TCP port directly:**
   - Linux/macOS: `nc -zv rtk2go.com 2101` (hangs = blocked; immediate = open)
   - Windows PowerShell: `Test-NetConnection rtk2go.com -Port 2101`
3. **Fetch the sourcetable:** `curl -v http://rtk2go.com:2101/` — if this
   returns the STR/CAS/NET table, the port is open.
4. **Distinguish server-down from port-block:** `ping rtk2go.com`. If ICMP
   replies arrive but the TCP port hangs, the host is up and the port is being
   filtered between you and it.
5. **Workarounds:** AUSCORS port 443 where coverage suits. SSH port-forwarding
   or a VPN exiting an unrestricted network both tunnel NTRIP over port 22/443.

---

## 12. Use Case → Accuracy Requirements

The table maps common use cases to required accuracy, the minimum adequate GNSS
mode, and whether free PPP (Galileo HAS SL1, ~20 cm H, ~10–15 min convergence)
is sufficient. RTK fix = 1–3 cm; commercial PPP (Trimble RTX, Swift Skylark) =
~2.5 cm.

| Use case | Required H accuracy | Required V accuracy | Adequate mode | Free PPP (HAS) adequate? | Key non-accuracy constraints |
|---|---|---|---|---|---|
| Navigation / hiking | 3–10 m | 5–20 m | Standalone GNSS | Overkill | TTFF, battery |
| Variable-rate ag application | 25–50 cm | N/A | SBAS or RTK float | Yes | Field prescription zone size |
| Precision ag auto-steer | ±2.5 cm pass-to-pass | N/A | RTK fix or commercial PPP | **No** (HAS ~20 cm) | Coverage, convergence, seasonal repeatability |
| Machine control (grading) | ±10–20 mm | ±10–20 mm | RTK fix | No | Uptime SLA, datum tie to design, blade calibration |
| UAV photogrammetry — GCPs | ±10–20 mm | ±15–30 mm | RTK fix | No | GCP distribution; target ≥ 3× GSD |
| UAV photogrammetry — PPK drone | ±20–50 mm | ±30–70 mm | RTK / PPK | No | Base RINEX log; antenna offset cal |
| GIS utility mapping (ASCE QL-B) | 100–300 mm | 150–500 mm | RTK float or SBAS | Yes (marginal) | Sky visibility; attribution |
| GIS cadastral survey | ±10–50 mm | ±10–50 mm | RTK fix | No (HAS ~20 cm) | Regulatory acceptance; datum tie |
| Construction stakeout | ±10–25 mm | ±10–25 mm | RTK fix | No | Datum tie to project control; tilt-pole correction |
| Structural displacement monitoring *(beyond hobbyist scope)* | ±1–5 mm | ±2–5 mm | CGNSS post-processed | No | Monument stability; IGS precise products |
| Scientific geodesy *(beyond hobbyist scope)* | ±0.1–1 mm | ±0.2–2 mm | PPP + IGS final orbits | No | Choke-ring antenna; ANTEX model; 24 h+ sessions |

**Key notes:**

- *Auto-steer pass-to-pass* is relative accuracy within a season — absolute
  position can be metres off, but adjacent passes must be < 2.5 cm apart. RTK
  fix achieves this; Galileo HAS at ~20 cm absolute does not. ✓
  (source: John Deere SF3 spec; Trimble CenterPoint RTX spec)
- *Cadastral*: commercial PPP (±2.5 cm) satisfies ALTA/NSPS and ICSM SP1 urban
  standards in principle; HAS (~20 cm) does not. Some jurisdictions require
  network RTK specifically. ~
- *GIS QL-B*: ASCE 38-22 Quality Level B specifies ~150 mm horizontal for
  geophysically detected utilities — HAS at ~20 cm meets this with margin. RTK
  float (~10–50 cm) is the common field practice. ~
- *Machine control*: RTK float (0.1–0.5 m) is never acceptable for production
  grading — fix loss stops or errors the machine. Uptime requirement drives the
  choice of commercial over volunteer networks.
- *Structural monitoring*: single-epoch RTK accuracy (~10–15 mm) is 5–15×
  coarser than the required detection threshold; displacement products come from
  time-series analysis of long continuous records, not single-epoch RTK.

**Accuracy sources:** ASPRS 2015 (photogrammetry GCPs); ICSM SP1 (Australian
cadastral); NOAA NGS User Guidelines (US RTK); ASCE 38-22 (utility QL);
ISO 4463 (construction setout); Emlid RS2+ product spec (RTK accuracy numbers). ~

---

## 13. Datum and Coordinate System Confusion

Hobbyist support questions involving "my position is wrong by N metres" almost
always reduce to one of four causes covered here.

### 13.1 Reference Frame Hierarchy

**ITRF (International Terrestrial Reference Frame)** — the global scientific
standard maintained by IERS. Coordinates track tectonic plate motion: a fixed
mark on the Australian plate advances ~70 mm/yr northward in ITRF. Successive
realizations: ITRF2000, ITRF2008, ITRF2014, ITRF2020 (published 2022).

**WGS84** — the frame embedded in GPS satellites and all consumer receivers.
WGS84 (G2139 and later) is aligned with ITRF2008 at the ~1 cm level. For
practical purposes, WGS84 ≈ ITRF at the same epoch. When a GNSS receiver
reports a position, it is in WGS84/ITRF at the time of observation. ✓

**ETRS89** (European Terrestrial Reference System) — fixed to the stable
Eurasian plate at epoch 1989.0; coincident with ITRF89 at that date. Because
the Eurasian plate moves at ~25 mm/yr relative to ITRF, by 2025 the horizontal
offset between ETRS89 and ITRF at a point in Germany is approximately:
(2025 − 1989) × 25 mm/yr ≈ **~0.9 m** (northeast direction). ✓
(source: Altamimi et al. 2012 EUREF Technical Note 1)

**GDA2020** (Geocentric Datum of Australia 2020) — fixed to the Australian
plate at epoch 2020.0; aligned with ITRF2014. Since the Australian plate moves
~70 mm/yr, the offset from ITRF grows annually:
- 2025: ~0.35 m (5 yr × 70 mm/yr), growing.
- Legacy GDA94 (fixed at 1994.0): ~2.2 m offset in 2025. ✓
  (source: ICSM SP7 Geocentric Datum of Australia 2020 Technical Manual)

**NAD83** (North American Datum 1983) — fixed to the North American plate. The
original 1986 realization introduced a ~2 m systematic offset vs the geocentre;
NAD83(2011) epoch 2010.0 differs from ITRF2014 by roughly **0.5–2 m** ~
horizontally across North America (direction-dependent). ✓
(source: Soler & Snay 2004 Journal of Surveying Engineering; NGS NADCON5)

**Classical non-geocentric datums** (OSGB36 UK, NTF France, Tokyo datum) were
fit to a local ellipsoid deliberately offset from the geocentre; they can differ
from WGS84 by 50–200+ m. OSGB36 differs from WGS84 by ~70–120 m depending on
location. ✓

**Summary — approximate horizontal offsets from ITRF at epoch ~2025:**

| Datum | Region | Approx offset from ITRF |
|---|---|---|
| WGS84 (G2139) | Global | < 2 cm (essentially equal) |
| ETRS89 | Western Europe | ~0.9 m northeast |
| GDA2020 | Australia | ~0.35 m, growing ~70 mm/yr |
| GDA94 | Australia (legacy) | ~2.2 m |
| NAD83(2011) | North America | ~0.5–2 m ~ |
| OSGB36 | United Kingdom | ~70–120 m |

### 13.2 Plate Tectonics and Multi-Year Coordinate Drift

ITRF coordinates of a physically stable mark advance with the local plate
velocity. Two RTK fixes at the same mark two years apart (both in ITRF/WGS84)
will differ by approximately (plate velocity × 2 years):
- Australia: ~140 mm — looks like the mark moved; it did not.
- Western Europe: ~50 mm.

If a cadastral plan was computed in GDA2020 at epoch 2020.0 and you measure with
RTK in ITRF at epoch 2025.5, the RTK coordinates are offset ~385 mm from the
plan (5.5 yr × 70 mm/yr). The remedy is to apply the ICSM epoch-conversion
pipeline (GDA2020 deformation model via PROJ or the ICSM QGIS plugin). ✓
(source: ICSM SP7 §4)

### 13.3 Geoid vs Ellipsoid — Height Confusion

**Ellipsoidal height (h):** height above the mathematical ellipsoid (GRS80).
This is what GNSS directly measures. RTK reports ellipsoidal height.

**Orthometric height (H):** height above the geoid — approximately mean sea
level. This is what engineers, topo maps, and flood-plain definitions use.

**Geoid undulation (N):** the separation between the two surfaces. H = h − N.

Global range of geoid undulations (EGM2008 ✓; source: Pavlis et al. 2012
Journal of Geophysical Research):

| Region | Approximate N |
|---|---|
| Minimum (south of India) | −106 m |
| Maximum (New Guinea / equatorial Pacific) | +85 m |
| Central Europe | +35 to +55 m |
| Australia | +5 to +30 m |
| Central North America | −40 to −10 m |
| Iceland | +20 to +40 m |

Practical example: if a receiver reports altitude +135 m and the local topo map
says +80 m elevation, the ~55 m difference is geoid undulation N — the receiver
is correct; it is reporting ellipsoidal height. Apply the national geoid model to
convert: GEOID18/GEOID12B (US, NOAA, free), AGAP2020 (Australia), country-level
models from national survey agencies (1–2 cm accuracy in well-surveyed regions). ~

Modern data-collection apps (Emlid Flow, QField with PROJ, Trimble TerraFlex)
can apply geoid corrections automatically if the national model file is loaded.

### 13.4 EPSG Codes — Key Values for GNSS Users

EPSG codes (maintained by IOGP at epsg.org) are integer identifiers for
coordinate reference systems. Key codes for RTK:

| EPSG | CRS | When you encounter it |
|---|---|---|
| 4326 | WGS84 geographic (degrees) | Default output of all GPS devices; Google Maps, OpenStreetMap |
| 4979 | WGS84 3D (+ ellipsoidal height) | RTK output with altitude; "raw" GNSS CRS |
| 4258 | ETRS89 geographic | Europe — pan-European official datum |
| 7844 | GDA2020 geographic | Australia — current national standard |
| 4283 | GDA94 geographic | Australia — legacy, being retired |
| 4269 | NAD83 geographic | North America |
| 27700 | OSGB36 / British National Grid | UK Ordnance Survey maps |
| 32601–32660 | WGS84 / UTM zones 1N–60N | Common metric projected CRS worldwide |
| 5703 | NAVD88 vertical | US official orthometric heights |
| 3855 | EGM2008 geoid height | Current global geoid reference surface |

### 13.5 "My Position Is Off by 1–2 m vs Google Maps"

This is the most common user support question. Causes in descending order of
likelihood:

**1. Datum offset (most common):** Google Maps uses WGS84/ITRF (EPSG:4326).
National NTRIP networks broadcast corrections in the national datum. Offsets:

- European casters (ETRS89): ~0.9 m offset vs Google Maps WGS84. ✓
- Australian casters using GDA94: ~2.2 m. ✓
- Australian casters using GDA2020: ~0.35 m (growing). ✓
- North American casters (NAD83): ~0.5–1.5 m. ✓

Diagnosis: if the offset is **systematic** (same direction and magnitude across
the site), it is a datum shift. Apply the published national transformation.

**2. Google Maps imagery georeferencing error:** Google's imagery mosaic
alignment accuracy varies enormously:
- Major cities with dense control: typically 1–3 m of true WGS84.
- Rural areas with sparse control: 5–20+ m off WGS84 is common.
- Dense forest, desert, snowy terrain: up to 50+ m in extreme cases. ~

Diagnosis: if the offset is **inconsistent** across the site (some points look
right, others wrong), the imagery is more likely culpable than the GNSS.

**3. Private base in WGS84, data in national datum:** a volunteer rtk2go base
configured to WGS84 delivers ITRF positions, which will be offset vs national
cadastral data by the datum difference above — opposite direction to cause 1.

**4. Wrong geoid model (vertical only):** if only altitude is wrong while the
horizontal is correct, the geoid model is absent or wrong.

### 13.6 Transformation Tools

**PROJ** (proj.org, used inside QGIS, GDAL, PostGIS) — the core open-source
transformation library. Version 6+ handles time-dependent plate-motion
corrections. Grid-based shift files (NTv2 for horizontal, GTX for vertical)
are free from national agencies and distributed via the PROJ CDN:
- US: NGS NADCON5 grids
- Australia: ICSM GDA94/GDA2020 conformal grids
- UK: OS OSTN15/OSGM15 grids

In QGIS 3.x: on-the-fly reprojection applies datum shifts automatically if the
layer's EPSG code is set correctly and the relevant PROJ grid shift files are
installed (QGIS prompts to download missing grids).

**Online tools:**
- NRCAN CSRS-PPP: returns both ITRF and NAD83 coordinates, including the
  transformation, for uploaded RINEX files. ✓
- NGS NCAT: US National Coordinate Transformation Tool; handles epoch-aware
  NAD83↔ITRF conversions.
- ICSM QGIS plugin (Australia): wraps the official GDA2020 transformation
  parameters including epoch adjustment. ~

---

## Sources consulted

- [rtk2go.com — How it Works](http://rtk2go.com/how-it-works/)
- [rtk2go.com — New Base Station Reservation](http://rtk2go.com/sample-page/new-reservation/)
- [docs.centipede.fr — Guide RTKBase](https://docs.centipede.fr/docs/base/Guide_RTKBase.html)
- [docs.centipede.fr — Connexion au caster](https://docs.centipede.fr/docs/centipede/3_connect_caster.html)
- [RTKBase default settings.conf — GitHub](https://github.com/Stefal/rtkbase/blob/master/settings.conf.default)
- [RTCM 3 Message List — SNIP Support](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/)
- [MSM message types — Tersus GNSS](https://www.tersus-gnss.com/tech_blog/new-additions-in-rtcm3-and-What-is-msm)
- [Guidelines for IGS Real-Time Broadcasters and Stations — IGS](https://files.igs.org/pub/resource/guidelines/Guidelines_for_IGS_Real_Time_Broadcasters_and_Stations.pdf) (independent reference: RTCM MSM message type tables for all constellations including QZSS 1111–1117 and BeiDou 1121–1127 ✓)
- [NTRIP v1 spec — ESA/GSSC (PDF)](https://gssc.esa.int/wp-content/uploads/2018/07/NtripDocumentation.pdf)
- [NTRIP v1 vs v2 — SNIP Support](https://www.use-snip.com/kb/knowledge-base/ntrip-rev1-versus-rev2-formats/)
- [BKG NtripCaster Manual](https://igs.bkg.bund.de/root_ftp/NTRIP/documentation/ntripcaster_manual.html)
- [Ionospheric Delay — ESA Navipedia](https://gssc.esa.int/navipedia/index.php/Ionospheric_Delay)
- [GLONASS Signal Plan — ESA Navipedia](https://gssc.esa.int/navipedia/index.php/GLONASS_Signal_Plan)
- [GLONASS ICD v5.1 — Russian Institute of Space Device Engineering (via UNB)](http://gauss.gge.unb.ca/GLONASS.ICD.pdf) (primary specification: L1 = 1602 + n×0.5625 MHz, L2 = 1246 + n×0.4375 MHz, n = −7…+6 ✓)
- [GLONASS CDMA signals — GPS World](https://www.gpsworld.com/glonass-cdma-signals-now-on-l1-l2/)
- [Solar Cycle 25 forecast — NOAA SWPC](https://www.swpc.noaa.gov/news/solar-cycle-25-forecast-update)
- [Solar Cycle 25 progression — NOAA SWPC](https://www.swpc.noaa.gov/products/solar-cycle-progression) (actual smoothed peak Oct 2024, SSN 160.8 ✓)
- [Observed effects of geomagnetic storm on RTK — SWSC Journal](https://www.swsc-journal.org/articles/swsc/full_html/2012/01/swsc120026/swsc120026.html)
- [High-lat GNSS disturbances at sub-minor storm — Andalsvik 2014](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014RS005418)
- [ZED-F9P Product Summary — u-blox](https://content.u-blox.com/sites/default/files/ZED-F9P_ProductSummary_UBX-17005151.pdf)
- [ZED-F9P for geodetic measurement — ResearchGate](https://www.researchgate.net/publication/360316310_UBLOX_F9P_FOR_GEODETIC_MEASUREMENT)
- [ZED-F9P Integration Manual — u-blox](https://content.u-blox.com/sites/default/files/ZED-F9P_IntegrationManual_UBX-18010802.pdf) (signal bands: L1C/A+L2C, L1OF+L2OF, E1+E5b, B1I+B2I ✓)
- [ZED-F9P-05B Datasheet — u-blox](https://content.u-blox.com/sites/default/files/documents/ZED-F9P-05B_DataSheet_UBXDOC-963802114-12824.pdf) (L1/L2 + OSNMA variant — **not** L1/L5; annotation previously incorrect)
- [ZED-F9P-15B — Symmetry Electronics](https://www.symmetryelectronics.com/products/u-blox/zed-f9p-15b/) (L1/L5 variant ✓; the correct reference for triple-band hobbyist use)
- [CSRS-PPP — NRCAN](https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php)
- [VRS vs MAC principles — Janssen 2009](https://www.spatial.nsw.gov.au/__data/assets/pdf_file/0003/129414/2009_Janssen_IGNSS2009_VRS_vs_MAC.pdf)
- [VRS connection examples — SNIP Support](https://www.use-snip.com/kb/knowledge-base/virtual-reference-station-vrs-connection-examples/)
- [GPS C/A multipath error envelope — NovAtel tech talk](https://novatel.com/tech-talk/an-introduction-to-gnss/resources/understanding-and-mitigating-gnss-multipath-interference-and-error)
- [Multipath error envelopes — Navipedia](https://gssc.esa.int/navipedia/index.php/Multipath) (practical max ~15 m for C/A ✓)
- [GNSS Carrier-Phase Multipath Modelling and Correction — Remote Sensing, MDPI 2024](https://www.mdpi.com/2072-4292/16/1/189) (peer-reviewed; confirms carrier-phase multipath max = quarter-wavelength, ~4.76 cm at GPS L1 ✓)
- [User Guidelines for Single Base Real Time GNSS Positioning v3.1 — NOAA NGS](https://geodesy.noaa.gov/PUBS_LIB/UserGuidelinesForSingleBaseRealTimeGNSSPositioningv.3.1APR2014-1.pdf) (government authority: RTK relative accuracy ~1 cm + 1 ppm ✓)
- [ZED-F9P survey-in CFG-TMODE3 — Drotek RTK docs](https://drotek.gitbook.io/rtk-f9p-positioning-solutions/tutorials/setting-survey-in-time-and-position-accuracy)
- [ZED-F9P DGNSS timeout (NAV5 60 s default) — u-blox portal](https://portal.u-blox.com/s/question/0D52p0000DHOvhwCQD/why-is-dgnss-timeout-in-nav5-navigation-5-configuration-default-set-to-60s-for-zedf9p-module-) ✓
- [Triple-frequency RTK widelane review — JGPS 2018](https://jgps.springeropen.com/articles/10.1186/s41445-018-0010-y)
- [RTCM 3 SSR message list — SNIP Support](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/)
- [GLONASS K2 signal analysis 2024 — DLR](https://elib.dlr.de/204822/1/Thoelert%20etal%202024_GLONASS%20K2%20signal%20analysis.pdf)
- [RTCM Message Type 59-FKP — Geo++ White Paper](http://www.geopp.com/pdf/geopp-rtcm-fkp59.pdf) (FKP proprietary origin, standardised as RTCM 1034 ✓)
- [Ionospheric Delay formula — Navipedia](https://gssc.esa.int/navipedia/index.php/Ionospheric_Delay) (40.3×10¹⁶/f² m/TECU ✓)
- [QZSS seven-satellite constellation — Cabinet Office Japan](https://qzss.go.jp/en/overview/services/seven-satellite.html) ✓
- [NavIC constellation status — GPS World, ISRO](https://www.gpsworld.com/indias-navic-constellation-in-jeopardy-as-majority-of-satellites-become-defunct/) ✓ (degraded to ≤3 operational as of March 2026)
- [Galileo HAS PPP-RTK convergence — GPS Solutions 2024](https://link.springer.com/article/10.1007/s10291-024-01617-7)
- [BDS-3 constellation completion — GPS World](https://www.gpsworld.com/two-new-beidou-satellites-complete-bds-3-constellation/) (45 total satellites, 30 BDS-3 ✓)
- [Klobuchar model correction efficiency — Navipedia](https://gssc.esa.int/navipedia/index.php/Klobuchar_Ionospheric_Model) (~50–70% RMS removal globally ✓)
- [Reach RS2+ Specifications — Emlid](https://docs.emlid.com/reachrs2/specifications/specs/) (technical spec: RTK range 60 km; 7 mm + 1 ppm horizontal ✓)
- [Single-band VS Multi-band — Emlid](https://docs.emlid.com/reach/tutorials/basics/single-multi/) (technical spec: single-band RTK baseline 10 km; multi-band 60 km ✓)
- [NOAA NGS User Guidelines for Single Base Real Time GNSS Positioning v3.1](https://geodesy.noaa.gov/PUBS_LIB/UserGuidelinesForSingleBaseRealTimeGNSSPositioningv.3.1APR2014-1.pdf) (ppm term: 1 ppm = 1 mm/km ✓)
- [SparkFun UM980 Galileo HAS E6 Convergence Test — GitHub](https://github.com/sparkfun/SparkFun_UM980_Galileo_HAS_E6_Convergence_Test) (78-trial test: avg 9.8 min convergence, 33–80 mm post-convergence ✓)
- [Septentrio mosaic-X5 firmware v4.14 reference guide — ArduSimple](https://www.ardusimple.com/wp-content/uploads/2024/10/mosaic-X5-Firmware-v4.14.10-Reference-Guide.pdf) (E6-B HAS enabled v4.14.0 ✓)
- [Trimble "What's new in firmware 6.28/5.68"](https://help.fieldsystems.trimble.com/r10/whats-new-6.28-5.68.htm) (HAS support added Jan 2025 ✓)
- [u-blox community forum — HAS support for ZED-F9P](https://portal.u-blox.com/s/question/0D52p0000Ck9SToCQM/support-for-galileo-high-accuracy-service-has) (ZED-F9P cannot support E6/HAS ✓)
- [GPS Solutions 2024 — HASlib + RTKLIB integration (Prol et al.)](https://link.springer.com/article/10.1007/s10291-024-01617-7) (sub-20 cm 3D at 1σ after ~10 min ✓)
- [HASlib — GitHub (NLS-FI)](https://github.com/nlsfi/HASlib) (open-source Galileo HAS decoder ✓)
- [HASPPP — GitHub (Wuhan University)](https://github.com/ZhangRunzhi20/HASPPP) (RTKLIB-integrated HAS decoder ~)
- [Quectel Galileo OSNMA/HAS announcement — BusinessWire Oct 2025](https://www.businesswire.com/news/home/20251007212262/en/Quectel-Strengthens-GNSS-Offering-with-RTKHOLD-and-Galileo-OSNMA-and-High-Accuracy-Service-Integration) (LG290P HAS firmware ✓)
- [Eos Arrow Gold+ Galileo HAS press release](https://eos-gnss.com/press-releases/galileo-high-accuracy-service) (first GIS device with HAS ✓)
- [SW Maps manual v3.0 (PDF)](https://aviyaantech.com.np/SwMaps/assets/SW%20Maps%20Manual%20V3.0.pdf) (NTRIP button colour green/orange ✓)
- [ArduSimple — How to use SW Maps](https://www.ardusimple.com/how-to-use-ardusimple-products-with-android-smartphones-tablets/) (Blue/Orange/Green position bubble, HPA < 20 mm at fix ✓)
- [Emlid Flow — NTRIP workflow for Reach RX](https://docs.emlid.com/reachrx/quickstart/ntrip-workflow/) (step-by-step workflow, status widget ✓)
- [Reach RX User Documentation v1.4 — Dimense](https://dimense.fi/site/assets/files/1993/reach_rx_user_documentation.pdf) (LED white/yellow/green for SINGLE/FLOAT/FIX ✓)
- [Emlid community — correction age thresholds](https://community.emlid.com/t/ntrip-age-of-corrections-keeps-exceeding-10s/38120) (5 s warn, 10 s drop-to-standalone ✓)
- [Emlid blog — Reach RX MFi certification July 2024](https://blog.emlid.com/meet-the-new-gen-reach-rx-rtk-rover-now-compatible-with-all-popular-gis-apps-on-ios/) (MFi certification confirmed ✓)
- [ArcGIS Field Maps — high-accuracy data collection](https://doc.arcgis.com/en/field-maps/latest/prepare-maps/high-accuracy-data-collection.htm) (MFi requirement for iOS BT Classic ✓)
- [Eos GNSS — iOS and Bluetooth overview](https://eos-gnss.com/knowledge-base/articles/ios-and-bluetooth-overview) (BLE/MFi/SPP detail ✓)
- [QField GNSS positioning docs](https://docs.qfield.org/how-to/navigation-and-positioning/gnss/) (TCP/UDP only on iOS ✓)
- [Centipede crtk.net migration — 2025-03-18](https://crtk.net) (host migration confirmed ✓)
- [EarthScope NOTA — UNAVCO retirement 2025-07-29](https://www.earthscope.org/data/gnss-realtime/) (legacy UNAVCO URLs dead ✓)
- [ICSM SP7 Geocentric Datum of Australia 2020 Technical Manual](https://www.icsm.gov.au/sites/default/files/GDA2020TechnicalManualV1.2.pdf) (plate velocity 70 mm/yr, ITRF offset ✓)
- [Altamimi et al. 2012 — ETRS89 and EUREF Technical Note 1](https://www.euref.eu/euref_members/library/publication_serien/23-altamimi-zuheir-2012.pdf) (ETRS89 offset from ITRF ~0.9 m at 2025 ✓)
- [Soler & Snay 2004 — NAD83/ITRF transformations — Journal of Surveying Engineering](https://doi.org/10.1061/(ASCE)0733-9453(2004)130:4(174)) (NAD83 Helmert parameters ✓)
- [Pavlis et al. 2012 — EGM2008 — Journal of Geophysical Research](https://doi.org/10.1029/2011JB008916) (geoid undulation range −106 to +85 m ✓)
- [rtk2go — How it works (connection policy)](http://rtk2go.com/how-it-works/) (only active streams in sourcetable; 50k-150k connections/day ✓)
- [ASPRS Accuracy Standards for Digital Geospatial Data 2015](https://www.asprs.org/wp-content/uploads/2015/01/ASPRS_Accuracy_Standards.pdf) (photogrammetry GCP requirements ~)
- [ASCE 38-22 Standard Guideline for Investigating and Documenting Existing Utilities](https://www.asce.org/publications-and-news/asce-bookstore) (utility quality levels QL-A/B/C ~)

- [NovAtel — GNSS Error Sources (Differential GNSS)](https://novatel.com/an-introduction-to-gnss/gnss-error-sources) (UERE budget; multipath not cancelled by DGNSS ✓)
- [Penn State GEOG 862 — User Equivalent Range Error node](https://www.e-education.psu.edu/geog862/node/1713) (HDOP × UERE formula ✓)
- [Penn State GEOG 862 — Multipath node](https://www.e-education.psu.edu/geog862/node/1721) (multipath not correlated between base and rover; not cancelled by differential ✓)
- [IEEE Trans. ITS 2023 — Seamless Accurate Positioning in Deep Urban Area (arXiv:2206.04457)](https://arxiv.org/pdf/2206.04457) (DGNSS horizontal RMS 11.1 m in Seoul urban test; NLOS 7–52 m per satellite ✓)
- [Frontiers Robotics AI 2022 — GNSS NLOS Signal Classification](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.868608/full) (NLOS pseudorange bias "tens or hundreds of metres" ✓)
- [PLOS ONE 2023 — Effects of Nearby Trees on Positional Accuracy of GNSS](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283090) (Trimble: 1–5 m under forest canopy; sub-meter not achievable under dense canopy ✓)
- [MDPI Sensors 2024 — Reduction of Multipath Effect (Pseudorange Acceleration Weight)](https://www.mdpi.com/1424-8220/24/21/6880) (urban DGNSS horizontal error 6.2 m 95th pct; with mitigation ~1.1 m ✓)
- [Interpine Innovation — GPS Accuracy Estimate (EPE): What Is It?](https://interpine.nz/gps-accuracy-estimate-epe-what-is-it/) (EPE is precision not accuracy; half of fixes outside displayed circle ✓)
- [rtklibexplorer — RTKLIB Solution Accuracy](https://rtklibexplorer.wordpress.com/2017/10/13/rtklib-solution-accuracy/) (formal covariance "optimistic"; assumes uncorrelated noise ✓)
- [ScienceDirect 2022 — Unmodeled-Error-Corrected Stochastic Assessment for Standalone GNSS Receiver](https://www.sciencedirect.com/science/article/abs/pii/S0263224122014610) (unmodelled errors, especially multipath, "remain in GNSS measurements"; accuracy estimates "must not be used to infer precise accuracy" ✓)
- [CREWES Research Report 2010 — GPS accuracy part 2: RTK float vs fixed (U. Calgary)](https://www.crewes.org/Documents/ResearchReports/2010/CRR201029.pdf) (float solutions: 1–2 dm convergence; up to 5 m with no way to tell ✓)
- [PMC/MDPI Sensors 2019 — Single-Baseline RTK Using Dual-Frequency Receivers in Smartphones](https://pmc.ncbi.nlm.nih.gov/articles/PMC6806615/) (single-frequency false-fix rate ~15% of epochs ✓)
- [PMC 2023 — Static Positioning Under Tree Canopy Using Low-Cost GNSS](https://pmc.ncbi.nlm.nih.gov/articles/PMC10056071/) (RTK float errors 1–2 m under forest canopy ✓)
- [rtklibexplorer — Variable Ambiguity Resolution Threshold for RTKLIB (2021)](https://rtklibexplorer.wordpress.com/2021/07/22/a-variable-ambiguity-resolution-threshold-for-rtklib/) (RTKLIB default ratio threshold T=3.0; "if too low, false fixes will be common" ✓)
- [Emlid Community Forum — Wrong false fake fix Emlid M2](https://community.emlid.com/t/wrong-false-fake-fix-emlid-m2/27542) (receiver displayed "Fix" with cm accuracy during false fix ✓)
- [Li & Shen 2014 — GNSS ambiguity resolution with controllable failure rate — J. Geodesy (ResearchGate)](https://www.researchgate.net/publication/263006977_GNSS_ambiguity_resolution_with_controllable_failure_rate_for_long_baseline_network_RTK) (false fix displaces position by decimetre or more; 0.01% failure rate achievable ✓)
- [ResearchGate 254250991 — How well does the VRS system perform?](https://www.researchgate.net/publication/254250991_How_well_does_the_Virtual_Reference_Station_VRS_system_of_GPS_base_stations_perform_in_comparison_to_conventional_RTK) (51 mm height error 10.5 km outside network hull ✓)
- [IEEE 5069258 — Practical accuracy of VRS RTK outside MyRTKnet](https://ieeexplore.ieee.org/document/5069258/) (horizontal ~6 cm; vertical up to several metres 30 km outside hull ✓)
- [Springer J. Geodesy 2005 — Long-range network RTK during severe ionospheric storm (doi:10.1007/s00190-005-0003-y)](https://link.springer.com/article/10.1007/s00190-005-0003-y) (IAR rate 94%→31%; decimeter horizontal errors inside network during storm ✓)
- [GPS Solutions 2023 — Tropospheric model for large height-difference RTK (doi:10.1007/s10291-023-01481-x)](https://link.springer.com/article/10.1007/s10291-023-01481-x) (~27 cm height error per 1,000 m elevation difference without vertical tropo model ✓)
- [ResearchGate 228734118 — Network RTK performance analysis using RTCM 3.0 (Southern Alberta)](https://www.researchgate.net/publication/228734118_Network_real-time_kinematic_performance_analysis_using_RTCM_30_and_the_Southern_Alberta_Network) (recommends adding network ambiguity resolution status flag to RTCM; not yet standardised ✓)
- [FIG Article Sep 2016 — Choy et al. PPP signal interruption and re-convergence](https://www.fig.net/resources/monthly_articles/2016/september_2016/Suelynn_etal_september_2016.pdf) (full-sky blockage: re-convergence "regularly exceeds 30 min" ✓)
- [ResearchGate 289224452 — Rapid re-convergence in real-time PPP with AR (Banville & Langley)](https://www.researchgate.net/publication/289224452_Rapid_re-convergence_in_real-time_precise_point_positioning_with_ambiguity_resolution) (PPP-AR: ~1-epoch recovery with integer cycle-slip fix ✓)
- [NovAtel Velocity 2014 — PPP signal interruption and re-convergence](https://www.novatel.com/tech-talk/velocity/velocity-2014/advanced-gnss-positioning-solutions-with-precise-point-positioning-ppp/convergence-performance) (atmospheric state bridging over short gaps; PPP_CONVERGING vs PPP status ✓)
- [Eos GNSS blog 2023 — Galileo HAS Early Observations](https://eos-gnss.com/blog/galileo-high-accuracy-service-early-observations) (HAS Phase 1 convergence 5–30 min; "about 30 min to 20 cm level" ✓)
- [Inside GNSS Feb 2024 — Galileo HAS urban driving assessment](https://insidegnss.com/galileo-has-a-performance-assessment-in-urban-driving-environments/) (urban: only marginal improvement over broadcast due to constant re-convergence ✓)
- [ENC 2025 — Galileo HAS accuracy and convergence performance results](https://enc-series.org/wp-content/uploads/2025/05/Sciforum-095088-commercial-formatted.pdf) (HAS Phase 1 float-only; phase bias products absent ✓)

_Last updated: 2026-04-25. Seventh validation pass: 2026-04-25._
