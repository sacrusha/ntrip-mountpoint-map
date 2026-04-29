# GNSS / RTK / NTRIP - AI Reference Guide

## 1. GNSS Signal Architecture

### 1.1 Constellations

| Constellation | Operator | Satellites (approx) | Notes |
| GPS | USA (DoD) | 32 active | L1/L2/L5; oldest, most receiver support; GPS III block complete Apr 2026 ✓ |
| GLONASS | Russia (Roscosmos) | ~24 | FDMA on L1/L2 (legacy, different freq per satellite); CDMA on L1/L2/L3 (newer sats) ✓ |
| Galileo | EU (EUSPA, formerly GSA) | ~26-28 operational of 34 launched | E1/E5a/E5b/E6; E6 carries HAS corrections ✓ |
| BeiDou (BDS-3) | China (CNSA) | 45 (15 BDS-2 + 30 BDS-3 core constellation) | B1C/B1I/B2a/B2b/B3I; regional + global ✓; additional satellites launched post-2020 |
| QZSS | Japan (Cabinet Office) | 4 (planned expansion to 7) | Geosynchronous+inclined; augments GPS over Japan/Asia-Pacific; QZS-5 failed to reach orbit Dec 2025 - 7-satellite timeline uncertain ~ |
| NavIC (IRNSS) | India (ISRO) | ~3-4 operational | Regional only (Indian subcontinent + ~1500 km); severely degraded as of 2026 - atomic clock failures have reduced active satellites below the minimum operational threshold of 4; limited receiver support ✓ |

~ = model assumption; not yet source-verified.

### 1.2 Signal Frequencies

Frequencies by role:

| Band role | GPS | GLONASS | Galileo | BeiDou |
| L1 / primary | L1 1575.42 MHz | L1 1602+n×0.5625 MHz (FDMA) ✓ | E1 1575.42 MHz | B1C 1575.42 / B1I 1561.098 MHz |
| L2 / secondary | L2 1227.60 MHz | L2 1246+n×0.4375 MHz (FDMA) ✓ | — | B2a 1176.45 / B2b 1207.14 MHz |
| L5 / safety-of-life | L5 1176.45 MHz | L3 1202.025 MHz ✓ (CDMA, GLONASS-K1/K2 only) | E5a 1176.45 / E5b 1207.14 MHz | B2a 1176.45 MHz |
| E6 / data | - | - | E6 1278.75 MHz (HAS) | B3I 1268.52 MHz |

GLONASS n = channel number (-7 to +6) ✓; 14 primary channels; antipodal pairs share. L1/L2 spacings differ (0.5625 vs 0.4375 MHz) -> inter-frequency bias modelling; RTCM `1230` carries biases. K1/K2 add CDMA L3 (1202.025 MHz); K2 adds CDMA L1/L2. CDMA GLONASS not tracked by F9P or most hobbyist hardware. ✓

### 1.3 Why Band Count Matters for RTK

Single-frequency (L1 only):
- Relies on broadcast iono models (Klobuchar GPS ~50% RMS removal; NeQuick Galileo ~2× better; both degrade at equatorial/high lat). ~
- Viability: <=5 km open sky calm iono -> fix probability ~= dual-freq ✓; 5-10 km -> TTFF lengthens (min vs sec); >10 km -> unreliable; Kp>=5 -> even short baselines lose fix. ~
- Use when: legacy M8P/M8N hardware; dense-array static; educational. Active market = F9P ~$50-100 more than M8P; avoid for new purchases.
- False-fix risk higher (~15% epochs smartphone-class environment) ~; directional argument against L1-only for consequential decisions.

Dual-frequency (L1+L2 or equivalent):
- Iono-free linear combination cancels ~99% first-order iono delay ~
- Reliable fix to ~30 km typical; iono-dependent (same hardware: fix at 50 km quiet day, fail at 20 km during storm ~). Emlid RS2+ spec: 60 km RTK, 7 mm + 1 ppm horizontal ✓ (formal spec, not marketing; iono is dominant variable).
- Practical minimum for NTRIP RTK at useful baselines
- Examples: ZED-F9P (GPS L1/L2C + GLONASS L1OF/L2OF + Galileo E1/E5b + BeiDou B1I/B2I) ✓; Emlid RS2+

Triple-band (L1+L2+L5 or L1+E5a+E5b etc.):
- EWL (L2+L5) ~3.4 m wavelength ✓; resolved near-instantaneously; widelane (L1+L2) ~86 cm resolves in seconds. Cascaded -> faster IAR.
- >99% wide-lane IAR in 20 s triple-freq vs 64% in 150 s dual-freq ✓; 78% fixed under multipath vs ~0 dual-freq ✓.
- Examples: ZED-F9P-15B (L1/L5, distinct from standard L1/L2 F9P) ✓, Septentrio mosaic-X5 ~, Emlid RS3. Standard F9P = L1/L2 only. ✓

Quad-constellation (GPS+GLONASS+Galileo+BeiDou): more sats -> faster IAR, fewer obstruction gaps. Quad+triple = hobbyist sweet spot.

Answering user questions: dual-band + slow TTFF/frequent fix loss -> triple-band valid. Single-freq -> dual-band = most impactful change.

### 1.4 Signal Structure (GPS L1 example)

~ Spread-spectrum carrier modulated with:
- PRN code (C/A or P(Y)): pseudorange measurement (~metre/epoch).
- Navigation message (LNAV/CNAV): ephemeris, clock corrections, Klobuchar iono model.
- Carrier phase: fractional + integer cycle count; ~19 cm wavelength L1; ~1-2 mm noise. Ambiguous: receiver knows fractional phase but not integer cycle count. RTK resolves integer ("ambiguity") via double-differencing.

### 1.5 GNSS vs GPS

"GPS" colloquially = any GNSS. Multi-constellation (GPS+GLONASS+Galileo+BeiDou): better sky coverage, faster IAR, more resilient to partial obstruction vs GPS-only.

### 1.6 Phone and Consumer Device Limitations

Flagship smartphones: dual-freq (L1+L5) but not cm RTK. Three barriers:

iOS: CoreLocation = `CLLocation` only; no ADR/pseudoranges/C/N0/RTCM injection in any entitlement. ✓ Internal RTK impossible regardless of chip. NTRIP app can relay RTCM via BT to external receiver only.

Android: `GnssMeasurement` API 24+ exposes ADR, pseudorange, C/N0, Doppler ✓; mandatory Android 10+ ✓; ADR not mandatory in CDD (Snapdragon historically none; Broadcom Pixels 5-9 expose ADR ✓). Duty cycling: chip 200 ms on / 800 ms off -> cycle slip per epoch, ADR useless; Android 9+ "Force full GNSS measurements" (dev options) disables; thermal/battery can re-enable. ✓ Best observed (Pixel 6 Pro, open sky, Force full, RTKLIB): ~0.2-0.5 m. Not cm. ✓

Antenna = residual block: no RHCP (LHCP multipath not rejected); PCV up to 4 cm L5 orientation-dependent ✓; C/N0 8-10 dB-Hz below geodetic ✓. 4 cm L5 PCV shifts with hand grip -> IAR fails. Phone RTK papers reach decimetre regardless of chip. ✓

Practical path: external F9P (~$150-300, ArduSimple simpleRTK2B) via BT; phone NTRIP client relays RTCM -> receiver computes fix -> cm NMEA. Phone chip not involved in RTK in either case.

Android: Lefebure/SW Maps injects NMEA as mock location (Dev Options -> "Select mock location app"). ✓
iOS: no mock location API; GIS app reads NMEA directly from receiver:
- SW Maps: BLE GATT ✓; relays RTCM to receiver.
- Emlid Flow: BLE or MFi BT Classic; Reach RX/RX2 MFi certified 2024-07. ✓
- ArcGIS Field Maps: requires MFi receiver (Eos Arrow, Trimble, Reach RX/RX2, Bad Elf, Geneq SxBlue). ✓
- QField (iOS): TCP/IP only (no BT); Android: BT direct. ~
- iCMTGIS PRO: direct BT for Eos Arrow, Bad Elf, Geneq SxBlue, Juniper GNS3. ~

iOS blocks SPP/RFCOMM without MFi; BLE no MFi required; modern rovers use BLE. ✓

## 2. Error Sources

RTK corrects most errors by differencing; residuals determine accuracy floor.

### 2.1 Ionospheric Delay

Dispersive (~1/f²); L1/L2 delays differ -> dual-freq cancels directly. Short baseline: common-mode iono cancels; long baseline: different iono columns -> residual = dominant error. L1 zenith: 1-10 m; severe storm 50+ m; gradient 30 km baseline: ~1-3 cm quiet, >10 cm/km severe storm. ~ L1-only: Klobuchar ~50-60% correction. ~

### 2.2 Tropospheric Delay

~2.3 m dry + ~0.2 m wet zenith. ~ Dry: Saastamoinen ~99% removal; wet: ~2-4 cm residual. ~ Short baselines/similar elevation: tropo cancels; long baseline or altitude diff: significant.

### 2.3 Satellite Clock and Orbit Errors

Broadcast ephemeris ~1-2 m; mostly cancels in short-baseline RTK. Long baseline (~100 km): ~1 cm residual. PPP/SSR sub-cm. ~

### 2.4 Multipath

Reflected signals corrupt pseudorange + carrier phase. See §9.

### 2.5 Receiver Noise

Carrier-phase noise ~1-2 mm geodetic; F9P sub-mm zero-baseline ✓. Pseudorange ~20-50 cm consumer, ~5-10 cm geodetic. ~ F9P accuracy floor = antenna + multipath, not receiver noise.

### 2.6 Error Budget Summary

| Error source | Standalone GPS | Single-base RTK 10 km | Single-base RTK 50 km |
| Iono | 1-10 m | ~cancelled (L1+L2) or ~2 cm (L1) | ~2-10 cm |
| Tropo | ~0.5 m | ~cancelled | ~2-5 cm |
| Orbit/clock | ~1-2 m | ~cancelled | ~1 cm |
| Multipath | ~0.5 m | 1-5 cm | 1-5 cm |
| Noise | ~0.3 m | ~1-3 mm | ~1-3 mm |
| Total (RMS) | 5-10 m | 1-5 cm | 5-15 cm |

~ All values model assumptions; depend on sky, receiver quality, geomagnetic activity.

Displayed accuracy vs actual: HDOP × σ_UERE or Kalman covariance - neither tracks multipath/atm gradients/base coord errors. Multipath = largest excluded source; open field <1 mm vs metal-building-adjacent 2-5 cm, HPA identical. Gap worst in Float (display sub-dm; actual 1-5 m) and DGNSS (display sub-m; actual 5-40 m urban). Formal covariance "optimistic" = industry/academic consensus. ✓ Mode details: §3.2, §3.3, §3.5.

## 3. Positioning Modes

### 3.1 Standalone GNSS (SPP)

Pseudoranges only; all §2 errors apply. ~5-10 m typical; 50+ m during iono storms. Consumer devices (phones, car GPS).

### 3.2 DGNSS / SBAS

Reference station broadcasts pseudorange corrections; rover applies them. Removes common-mode orbit/clock errors. ~0.3-1 m. No carrier phase.

Multipath/NLOS survive differential uncancelled: urban canyon -> 5-40 m bias while display reads "1 m." ✓ HDOP can appear *low* in canyons because reflected-signal sats are tracked, masking degradation rather than exposing it. Suburban canopy/buildings: 2-5 m actual. ✓

SBAS (WAAS, EGNOS, MSAS, GAGAN, SDCM): DGNSS via geostationary; no internet; ceiling ~1 m; same multipath limitation. ~ Galileo HAS = free, global, better.

### 3.3 RTK (Real-Time Kinematic)

Carrier-phase double-differences base↔rover and between satellite pairs. Critical step: integer ambiguity resolution (IAR) - finding integer carrier cycles per satellite-antenna path. Resolved = "fix"; accuracy 1-3 cm.

Fix states:
- Float: corrections applied; ambiguities as real numbers. ~0.1-0.5 m; can drift.
- Fix: IAR resolved. 1-3 cm. Stable.
- DGNSS: pseudorange fallback. ~0.5 m.

False fix: ratio test accepts wrong integers -> receiver shows "Fix" + cm precision offset by ~0.3-1 m (multiples of ~19 cm wavelength). No alarm/LED/flag; no ground truth. Risk highest: multipath, <8 sat pairs, long baseline, L1-only (~15% false-fix rate). ✓

Float drift: ambiguities real-valued Kalman states; converge -> position shifts with them; unmodelled iono/tropo injects smooth correlated bias -> gradual drift, invisible. Canopy/urban float errors 1-2 m even with active corrections. ✓

~ TTFF: 30-90 s (dual-band, open sky, short baseline); seconds warm start; minutes+ marginal sky/long baseline/iono.

Double-differencing eliminates sat clock + receiver clock + most atm errors:

```
DD_phase = (φ_rover_sat1 − φ_base_sat1) − (φ_rover_sat2 − φ_base_sat2)
```

Leaves: integer ambiguity + multipath + noise.

Accuracy: ppm term

RTK accuracy = fixed term + distance-dependent term, e.g. Emlid RS2+: "7 mm + 1 ppm horizontal." ✓
- Fixed term (7 mm): hardware noise floor (receiver noise, PCO variation, base multipath). Present at zero baseline.
- 1 ppm = 1 mm/km of baseline. ✓ (NOAA NGS User Guidelines)

Total ~ fixed_mm + (ppm × baseline_km). For 7mm + 1ppm: ppm equals fixed at ~7 km, dominates beyond ~10 km; at 20 km ~27 mm; at 30 km ~37 mm.

Ppm causes: residual iono gradient (~60-80% of budget; ~0.5-3 cm across 30 km quiet) + tropo wet gradient (~15-30%) + broadcast orbital error (~0.2 ppm). ~

Geomagnetic storms: Kp 7 (G3) -> IAR 94%->31% ✓; 20 km baseline that normally holds may become unusable. Fixed term unaffected; distance-dependent term degrades. (§7.3)

VRS nearly cancels ppm: server models iono/tropo gradients, synthesises corrections at rover location (~0 km effective baseline). User 20 km from nearest physical station gets ~7-8 mm horizontal rather than ~27 mm; network iono model residual (~0.5 ppm of near-zero effective distance) is negligible. ~

VRS edge-of-network failure modes (cancellation holds inside well-spaced network: stations <=70 km apart, calm iono, flat terrain):
1. Outside hull: caster silently switches interpolation -> extrapolation; no RTCM notification; ~51 mm height error 10.5 km outside; 30 km outside: horizontal ~6 cm, vertical several metres. ~ (ResearchGate 254250991; IEEE 5069258)
2. Ionospheric storms: same 94%->31% IAR collapse; dm horizontal errors even inside network. ✓ (J. Geodesy 2005)
3. Steep terrain: tropo correction extrapolates vertically; ~27 cm height error per 1000 m altitude difference. ~ (GPS Solutions 2023)
4. Sparse network (spacing >70-100 km): interpolation too coarse for reliable IAR. ~

All four cases: displayed HRMS/fix status/PDOP reflects sat geometry + IAR, not correction quality. No RTCM 3.x interpolation-quality field yet. ✓ (Southern Alberta RTK study)

### 3.4 Network RTK (NRTK)

Network of stations; server models atm spatial variation -> synthetic corrections; effective baseline ~0 km (VRS). See §6.

### 3.5 PPP (Precise Point Positioning)

Single receiver; no base station. Uses precise orbit/clock products (IGS, CNES, etc.) broadcast or downloaded. Must model all error sources independently. ~

Convergence: ~ float PPP (GPS+Galileo) 20-30 min to cm; PPP-AR (CSRS-PPP AR mode) 10-20 min. Different tiers - don't conflate.

Galileo HAS (free E6-B PPP-RTK; no subscription; no base): target <300 s convergence; observed 7.5-15 min GPS+Galileo static; <20 cm horizontal 95% post-convergence ✓. QZSS CLAS (Japan/Asia-Pacific): spec <6 cm H / <12 cm V static ✓; observed 1.3-2.7 cm H (95%) ~. Both work anywhere with satellite visibility; recommended alternative when NTRIP unavailable.

Galileo HAS hardware requirements: E6-B (1278.75 MHz) requires hardware that physically tracks E6; firmware cannot add E6 to non-E6 hardware.

| Receiver | E6/HAS support | Notes |
| Unicore UM980 / UM982 | Native; enable via signal-group config | Most accessible hobbyist option; ~$100-200 bare module (ArduSimple, SparkFun). SparkFun 78-trial test: avg ~77 mm post-convergence, best observed 33 mm, avg convergence 9.8 min (excl. outlier) ✓ (source: SparkFun UM980 HAS E6 convergence test repo) |
| Septentrio mosaic-X5 | Firmware v4.14.0+ (2024) | Used in peer-reviewed HAS papers; outputs raw E6-B pages for HASlib/RTKLIB pipeline ✓ (source: mosaic-X5 firmware v4.14.10 reference guide) |
| Trimble R10 / R580 / R750 | Firmware v6.28+ (Jan 2025), enabled via TIM | Requires active options unlock for Galileo tracking ✓ (source: Trimble "What's new in 6.28") |
| Eos Arrow Gold+ | Native | Described as first GIS-market device with HAS support ✓ (source: Eos press release) |
| Quectel LG290P | Hardware present; HAS firmware Oct 2025 | Quad-band L1/L2/L5/E6 ✓ (source: Quectel HAS announcement Oct 2025) |
| u-blox ZED-F9P (all variants) | None - impossible | Tracks L1+L2 (or L1+L5 for -15B). No E6 hardware exists in any F9 chip. No firmware update changes this ✓ (source: u-blox community forum; F9P product summary) |
| Smartphones (all) | None | No consumer GNSS chipset supports E6 as of 2026 ✓ |

IDD (Internet Data Distribution): same HAS corrections also via NTRIP from GSC caster. Free registration via GSC portal; slots limited, granted per organisation (not individual) - not mass-market drop-in for NTRIP RTK. ~ (GSC HAS IDD registration page)

Open-source HAS decoders: HASlib (NLS-FI, Python; github.com/nlsfi/HASlib v1.0.2): +RTKLIB -> sub-20 cm 3D 1σ after ~10 min on Septentrio ✓; HASPPP (Wuhan U, C/C++; github.com/ZhangRunzhi20/HASPPP): embedded HAS in RTKLIB PPP engine. ~

Non-monotonic convergence: Kalman displayed confidence shrinks smoothly; actual error oscillates. New sat/cycle-slip/iono shift -> position jumps cm-dm before filter re-absorbs. ~

Signal interruption: any carrier-phase break resets ambiguity states. Float PPP: full-sky blockage -> 10-30 min to re-converge. PPP-AR with atm bridging (TerraStar-C PRO, Septentrio+SPARTN, Trimble RTX FAST): 5 s gap -> ~30-90 s recovery. ✓

HAS Phase 1 = float-only PPP (no phase bias products -> no PPP-AR). First 1-3 min: H error 0.5-3 m. Target <300 s/<20 cm (95%) not met until 6-15 min static. Urban constant re-convergence -> marginal vs broadcast-only. ✓ HAS suits open-sky static; unsuitable urban/forest. NTRIP RTK re-acquires in seconds; HAS cannot. ~

~ PPP out of project scope (NTRIP RTK only); explains standalone cm accuracy.

PPP tiers (routinely conflated):
- Float PPP: orbit+clock only; ambiguities real-valued; no fix moment; display monotonic, actual error oscillates.
- PPP-AR: +phase bias products -> integer ambiguities -> widelane/narrowlane fix -> cm. Examples: CSRS-PPP AR ✓; TerraStar-C PRO; Trimble RTX; HAS Phase 2 (not committed). ~

Float-PPP never reaches cm in 2 min (math); PPP-AR can. First triage: which tier?

IGS precise products - latency vs accuracy ladder:

| Product | Latency | Orbit accuracy | Clock accuracy | Use |
| Ultra-rapid (predicted half) | Real-time (computed in advance) | ~5 cm RMS ~ | ~3 ns ~ | Real-time PPP via NTRIP feed (RTCM SSR) |
| Ultra-rapid (observed half) | 3-9 h | ~3 cm RMS ✓ | ~150 ps ✓ | Near-real-time PPP, hourly updates |
| Rapid | ~17 h | ~2.5 cm RMS ✓ | ~75 ps ✓ | Same-day batch PPP processing |
| Final | 12-18 days | ~2.5 cm RMS ✓ | ~20 ps ✓ | Reference-grade post-processing; geodesy |

Free PPP web services (CSRS-PPP, AUSPOS, OPUS, magicGNSS) use best available tier - usually rapid/final by time 24 h RINEX uploaded.

Atm bridging: iono+tropo Kalman states persist across interruption; only integer portion reconverges. Without: 5 s gap -> 10-30 min float. With bridging: 30-90 s. ~ IMU+bridging sustains cm through forest/tunnels. ~

Free vs commercial PPP-RTK (2026):

| Service | Cost | Tier | Convergence target | Coverage | Hardware |
| Galileo HAS SL1 | Free | Float PPP-RTK | <300 s spec / 6-15 min observed | Global | E6-B receiver (UM980, Mosaic-X5, Eos Arrow Gold+, LG290P) |
| QZSS CLAS | Free | PPP-AR (with state-space) | <60 s spec, ~30 s observed ✓ | Japan + ~1500 km | L6-D receiver |
| BeiDou PPP-B2b | Free | PPP-RTK | <30 min ~ | China + Asia-Pacific | B2b-tracking receiver |
| Trimble RTX (CenterPoint) | ~$1500/yr-equivalent | PPP-AR + bridging | <1 min (RTX FAST), ~5 min (RTX) | Global | Trimble GNSS hardware + subscription |
| NovAtel TerraStar-C PRO | Subscription | PPP-AR + bridging | 5-18 min | Global | NovAtel OEM7 / SMART7 + subscription |
| Hexagon HxGN SmartNet PPP | Subscription | PPP-AR | 5-10 min | Global | Multi-vendor with subscription |
| u-blox PointPerfect | Subscription | SPARTN PPP-RTK | <1 min | Continental US/EU + maritime | u-blox NEO-D9S + ZED-F9P/F9R |
| Swift Skylark | Subscription | PPP-RTK | <1 min | US/EU + selected | Skylark-compatible Swift hardware |
| CSRS-PPP (NRCan) | Free | PPP-AR (post-processed) | n/a (batch) | Global | Any RINEX upload |
| AUSPOS (GA) | Free | Precise differential (post-processed; double-differenced against IGS/APREF via Bernese) ~ | n/a (batch) | Global, Asia-Pacific tuned | Any RINEX upload |

NavIC SPS omitted: standalone positioning, not PPP-RTK. Galileo HAS / QZSS CLAS / BeiDou PPP-B2b = only free carrier-phase-driven corrections in active service. ~

### 3.6 SSR vs OSR

- OSR: station sends raw obs; rover differences them. Corrections implicitly spatial.
- SSR: orbit/clock/iono/tropo sent separately; rover reconstructs. Enables PPP-RTK. Used by: Galileo HAS, BDS PPP-B2b ~, QZSS CLAS ~, Skylark, Trimble RTX.

~ SPARTN = compressed SSR over NTRIP/PointPerfect; distinct from RTCM SSR.

## 4. RTCM Protocol

RTCM SC-104 = de-facto standard for differential corrections. Specs paywalled; descriptions from public docs + receiver SDKs.

### 4.1 RTCM 2.x (legacy)

30-bit word frames; GPS corrections type 1/9, GLONASS 31, carrier 18/19. ~ F9P has no 2.x support.

### 4.2 RTCM 3.x - Legacy messages

Frame: 3-byte header (preamble 0xD3, 6b reserved, 10b length), variable payload, 3-byte CRC-24Q. Self-framing; concatenatable.

Key legacy (non-MSM) messages:

| Msg | Content | Notes |
| 1001-1004 | GPS L1/L2 RTK observables | Older; prefer MSM |
| 1005 | Stationary antenna reference point (ARP), no height | Required for RTK |
| 1006 | ARP + antenna height | Preferred over 1005 |
| 1007 | Antenna descriptor | Antenna type/model |
| 1008 | Antenna serial number | |
| 1009-1012 | GLONASS L1/L2 RTK observables | |
| 1013 | System parameters / time offsets | |
| 1019 | GPS ephemeris | For standalone use |
| 1020 | GLONASS ephemeris | |
| 1033 | Receiver/antenna descriptor | |
| 1042 | BeiDou ephemeris ~ | |
| 1045/1046 | Galileo ephemeris ~ | |

1005/1006 frame metadata: 6-bit DF021 "ITRF Realisation Year" field exists but RTCM SC-104 never specified semantics ✓ (SNIP KB). F9P firmware leaves it 0; rtklib + most decoders ignore it. Broadcast XYZ carries no frame or epoch -> rover trusts the coordinate blindly. RTCM 3.1 added 1021-1027 datum-transformation messages (Helmert/Molodensky/grid/projection) ~; some Trimble/Leica casters + a few SAPOS Länder emit them for national-projection clients; F9P does not generate them; rtk2go and Centipede do not transmit them. Frame/epoch context lives in network docs only. See §13.7.

### 4.3 RTCM 3.x - MSM

Modern format (RTCM 3.2 ~); all constellations; consistent structure. MSM type = base + density:

| MSM level | Pseudorange | Carrier phase | Doppler | CNR | Notes |
| MSM1 | compact | - | - | - | Phase-range only, minimal bandwidth |
| MSM2 | - | compact | - | - | Phase-range only |
| MSM3 | compact | compact | — | — | |
| MSM4 | full | full | — | half-cycle | Most common RTK baseline |
| MSM5 | full | full | full | half-cycle | Adds Doppler; used where velocity matters |
| MSM6 | full high-res | full high-res | - | full | High-res without Doppler |
| MSM7 | full high-res | full high-res | full | full | Max precision; preferred for quality bases |

Base numbers per constellation:
- GPS: 1071-1077
- GLONASS: 1081-1087
- Galileo: 1091-1097
- SBAS: 1101-1107
- QZSS: 1111-1117 ✓
- BeiDou: 1121-1127 ✓
- NavIC: 1131-1137 ~

~ So `1074` = GPS MSM4, `1077` = GPS MSM7, `1097` = Galileo MSM7, etc.

RTK stream requirements for modern rover:
- Min MSM4 (or legacy 1001-1004) for GPS; MSM7 preferred.
- 1005 or 1006 required (base coords).
- Multi-constellation (GPS + Galileo or GLONASS) -> better fix reliability + TTFF.

Typical good stream: `1005, 1074, 1077, 1084, 1087, 1094, 1097, 1124, 1127` ~ (base pos + GPS/GLONASS/Galileo/BDS MSM4+7). Many networks broadcast just MSM4 or just MSM7; varies by network/caster config.

MSM1-7 share header layout:

```
Header:
  Message number       12 bits   (1071–1077, 1081–1087, ...)
  Reference station ID 12 bits
  GNSS epoch time      30 bits   (constellation-specific time scale)
  Multiple message bit  1 bit    (0 = last fragment of this epoch)
  IODS                  3 bits   (issue of data station)
  Reserved              7 bits
  Clock steering ind.   2 bits
  Ext. clock indicator  2 bits
  GNSS smoothing ind.   1 bit
  Smoothing interval    3 bits
  Satellite mask       64 bits   (bit i = 1 → satellite i present)
  Signal mask          32 bits   (bit j = 1 → signal j present)
  Cell mask           variable   (Nsats × Nsigs bits, one per cell)
```

Three masks = sparse 2-D (satellite, signal) cell matrix. Non-zero cell -> one obs entry. ✓ E.g. 8 GPS sats × 2 signals = 16 cells vs 64 × 32 = 2048 fixed slots. MSM bandwidth: MSM4 ~0.5 kbps/const; MSM7 ~1-2 kbps; 4 constellations 1 Hz = ~4-8 kbps. ~

Satellite mask: GPS bit 0->PRN 1, ..., bit 31->PRN 32; GLONASS bit 0->R01, ..., bit 23->R24 (FDMA channel not in mask, carried in 1020); Galileo bit i->ID(i+1). ~ Signal mask: GPS 1C (L1 C/A), 1P/1W/1L/1S (L1), 2C (L2C), 2P/2W/2S/2L/2X, 5I/5Q/5X. ~ Incorrect mapping -> carrier-phase silently attributed to wrong band ("stream valid but rover stays float" in legacy firmware).

Operationally: base broadcasting only `1077` silently drops GLONASS -> halves rover sat count; add `1087/1097/1127`. F9P respects all 4 constellations by default; can restrict via `CFG-SIGNAL-*`. Stream showing only `1074/1077` at 1 Hz = GPS-only base.

### 4.4 RTCM 3.x - SSR Messages

SSR ranges ✓: GPS 1057-1062, GLONASS 1063-1068, Galileo 1240-1245, QZSS 1246-1251 ~, BeiDou 1258-1263 ~. Content: orbit/clock corrections, code/phase biases, VTEC iono maps. Used by PPP-RTK services; not standard single-base RTK. Uncommon on free public NTRIP casters.

### 4.5 Proprietary Formats

| Format | Owner | Notes |
| CMR / CMR+ | Trimble | Older; legacy Trimble networks |
| sPace | Leica ~ | Leica SmartNet proprietary |
| SPARTN | u-blox (Sapcorda JV 2021) ~ | SSR compressed; PointPerfect; Swift/Septentrio = licensees/decoders |
| ProMark / LandXML | Various | Not correction formats |

~ Free public networks = RTCM 3.x exclusively. CMR/CMR+ on some older SAPOS + Leica-run casters.

## 5. NTRIP Protocol

NTRIP (Networked Transport of RTCM via Internet Protocol) defined in BKG Technical Note 1. ~ v2.0 current; v1.0 still used by many casters.

### 5.1 Architecture

Three roles:
- NtripSource (base): connects to caster, pushes RTCM via HTTP/1.1 POST (v2) or proprietary push method ~
- NtripCaster: HTTP server; accepts sources, serves clients; maintains sourcetable.
- NtripClient (rover): HTTP/1.1 GET; requests mountpoint; receives RTCM byte stream.

### 5.2 Sourcetable

Caster's index of available streams. HTTP GET `/` (no mountpoint). ~ Three record types:

STR (stream) record - key fields:

```
STR;mountpoint;identifier;format;format-details;carrier;nav-system;
    network;country;lat;lon;nmea;solution;generator;compr-encryp;
    authentication;fee;bitrate;misc
```

Key STR fields (0-indexed):

| Idx | Field | Meaning |
| 0 | "STR" | record type |
| 1 | mountpoint | stream name |
| 3 | format | RTCM version + msg set |
| 5 | carrier | 0=DGNSS, 1=L1, 2=L1+L2, 3=tri-band |
| 9 | lat | ref lat |
| 10 | lon | ref lon |
| 11 | nmea | 1 -> caster needs rover GGA (VRS/MAC/FKP/i-MAX) ✓ |
| 14 | fee | "N" = free |

NET: network name, operator, registration URL. ~
CAS: caster metadata. ~

### 5.3 NTRIP v1 vs v2

| Feature | v1 | v2 |
| HTTP version | HTTP/1.0 | HTTP/1.1 |
| Client request | GET /mountpoint | GET /mountpoint with Host header |
| Chunked transfer | No | Yes (Transfer-Encoding: chunked) |
| Client → caster position | Out-of-band (separate GGA) | In-band via NMEA GGA sentence in request body ~ |
| Sourcetable request | GET / | GET / |

~ Most casters remain backward-compatible with v1. rtk2go accepts
both. ~ Some clients (older Trimble firmware) send v1 only.

### 5.4 NMEA GGA Sentence (rover -> caster)

VRS mountpoints require rover position to synthesise virtual reference:

```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
```

Fields: time, lat, N/S, lon, E/W, fix quality, sats, HDOP, altitude, geoid sep, age DGPS, DGPS ID, checksum. ~ >50 km from VRS area -> caster may close connection.

### 5.5 Authentication

NTRIP: HTTP Basic Auth (base64 username:password). Sourcetable `authentication` field: B=basic, D=digest ~, N=none. Many open networks use fixed shared credentials (Centipede `centipede`/`centipede`; rtk2go any email/`none`). Base64 = trivially reversible; provides accountability, not security.

### 5.6 Caster Software

- NTRIP Caster (BKG): original reference; many national agencies ~
- SNIP (SCSC, commercial): powers rtk2go ~ and some SAPOS casters.
- str2str (RTKLIB): open-source caster/source/client; basis for RTKBase.
- BNC (BKG Network Combiner): analysis/QC/relay.

### 5.7 Port Conventions

Default port 2101 = convention only; NTRIP runs any TCP port. Public networks often use high ports (5005, 9879, 10011); some expose 443 TLS for firewall traversal.

### 5.8 NEAR and Auto-Select Mountpoints

Routing aliases, not physical stations:
- NEAR (rtk2go, Centipede): routes to closest base to rover's GGA position. Not a fixed point.
- VRS auto-selects: single entry-point triggers per-rover synthetic stream.

All aliases: `nmea=1` in sourcetable (require rover position); no meaningful fixed coords. Appear in client by name, not as map pins.

### 5.9 NTRIP Client Software

| Client | Platform | Notes |
| SW Maps (Aviyaan Tech) | Android + iOS | Field GIS; NTRIP -> BT to receiver; free tier. Android: BT Classic or BLE; iOS: BLE only ✓ |
| RTKLIB rtkrcv / str2str | Linux/macOS/Windows | CLI; str2str relays NTRIP to serial/USB/TCP; basis for RTKBase |
| RTKLIB RTKGET | Windows | GUI RINEX download from NTRIP; not real-time |
| Lefebure NTRIP Client | Android only | Bare NTRIP; mock-location; no iOS ✓ |
| BNC (BKG Ntrip Client) | Desktop | Decode/log/QC/relay; analysis |
| u-center (u-blox) | Windows | NTRIP client -> F9P via USB; bench tests |
| Emlid Flow | iOS/Android | Reach-only; NTRIP + RTCM relay over BT ✓ |

~ Field rover: SW Maps + BT F9P = most common Android stack. Permanent base: RTKBase source-push replaces separate client.

### 5.10 App Connection Display

SW Maps: bubble blue=standalone, orange=float, green=fix ✓. Status bar: BT state, NTRIP freshness, sat count, HPA (<20 mm at fix). Quality filter: "RTK Fix only" blocks float logging.

Emlid Flow (Reach hardware): SINGLE ~1-3 m, FLOAT ~10-50 cm, FIX ~1-3 cm ✓. Age: >5 s = warning, >10 s = drops to float. Reach RX LED: white=SINGLE, yellow=FLOAT, green=FIX. ✓

Typical RTK Fix numbers:
| Metric | Expected |
| HPA | 10-20 mm (<=10 km); 30-50 mm (30-50 km) |
| Vertical | ~1.5–2× horizontal |
| Correction age | 0-2 s |
| PDOP | <=2.0 for reliable fix; >4 = fix unlikely |
| Satellites in use | >=10 multi-constellation |
| TTFF | 5-30 s open sky multi-band; minutes marginal sky |

### 5.11 Rover-Side Registration (base operator: §10.4)

| Network | Host:port | Credentials | Notes |
| rtk2go | rtk2go.com:2101 | any email / `none` | No account; port 2103 (PL), 2104 (JP). ✓ |
| Centipede | crtk.net:2101 | `centipede`/`centipede` | Migrated from `.fr` 2025-03-18. ✓ |
| SAPOS (DE) | sapos.de (per state) | per-state portal | Free/immediate most states; Bavaria €20/yr non-ag; NTRIP 1.0 raw TCP; VRS only. ✓ |
| AUSCORS (AU) | ntrip.data.gnss.ga.gov.au:2101 | gnss.ga.gov.au/registration | Auto-approve; CC BY 4.0; port 443 TLS available; old host dead 2022-07. ✓ |
| PositioNZ (NZ) | positionz-rt.linz.govt.nz:2101 | linz.govt.nz portal | Near-immediate; CC BY 4.0 NZ. ✓ |
| EarthScope NOTA | ntrip.earthscope.org:2101 | earthscope.org/data/gnss-realtime/ | NULA annual; non-commercial; UNAVCO URLs dead 2025-07-29. ✓ |
| TrigNet (ZA) | trignet.co.za:2101 | trignet.co.za | NGI approval ~days. ✓ |

Slow/unusual: ASG-EUPOS 1-2 days admin; MIRAI 2 forms + 365d inactivity expiry; MoDOT RTN signed+notarised; CORS-KOREA Korean portal/national ID; SatRef HK + MIRAI 12-month inactivity termination. ~

## 6. Network RTK

NRTK: network of reference stations; server synthesises corrections from multiple real stations. Effective baseline error = distance to virtual reference (not nearest physical station, which can be 50-100 km away).

### 6.1 VRS - Virtual Reference Station

Trimble origin. ~ (1) Rover sends GGA to server; (2) server selects 3+ surrounding stations + runs network engine ~; (3) server synthesises RTCM as if real station at rover location (~0 km baseline); (4) rover RTK engine treats as normal single-base stream.

NTRIP signature: `nmea=1` (rover must send position). Any NMEA=1 = presumptively VRS or similar (MAC/FKP/i-MAX also require position).

VRS limits: unique stream per rover -> scales poorly at high rover counts; requires continuous GGA (stop sending -> server may drop stream ~); initialisation artefacts if rover moves significantly while connected. ~

### 6.2 MAC - Master-Auxiliary Concept

Geo++ + Leica, early 2000s; RTCM 3.1 (2007). ~ Server sends: (1) master station = full RTCM obs (identical to single-base); (2) auxiliary stations = differential (aux - master), dominated by atmospheric variation, ~10-20% of master bytes per aux. ~

RTCM messages: `1014` (network aux station data), `1015` (GPS iono corrections), `1016` (GPS geometric corrections), `1017` (combined 1015+1016), `1037-1039` (GLONASS parallels). ✓

Rover: receives master as single base; reconstructs aux obs from deltas; interpolates atm gradient at rover position; applies to RTK.

VRS vs MAC: VRS = server interpolates, rover sees single base; MAC = rover interpolates, aware of network geometry. Server scaling: MAC = broadcast to all (no per-rover synthesis); VRS = unique stream per rover. Firmware: MAC needs network-RTK engine (Trimble/Leica/Topcon/Septentrio support; F9P does not ✓). MAC nets also broadcast VRS fallback. Both carry `nmea=1` -> NMEA filter drops both.

### 6.3 FKP and i-MAX (other NRTK modes)

FKP (Flächen-Korrektur-Parameter; Geo++ SAPOS origin): server broadcasts polynomial atm gradient; rover evaluates at own coords. RTCM 1034 ~ (predates 3.x; standardisation assignment disputed). Separate N (geometric/tropo) + I (iono) coefficients per satellite, reference `(lat_ref, lon_ref)` = master station. Rover-side evaluation:

```
δ(lat, lon) = N₀ + N_lat × (lat − lat_ref) + N_lon × (lon − lon_ref)
            + I_lat × (lat − lat_ref) + I_lon × (lon − lon_ref)
```

FKP `nmea=1` (rover position needed) -> dropped by NMEA filter.

i-MAX (Trimble): server interpolates per-rover (VRS style) but emits MAC-format messages (degenerate single-base). Lets MAC-aware Trimble rovers consume VRS stream. ~ Pipeline: `nmea=1`, dropped.

Comparison summary:

| Mode | Where interpolation happens | Per-rover stream? | RTCM messages | Rover engine required |
| VRS | Server | Yes - unique per rover | 1004/1012, MSM, 1005/1006 (synthetic) | Standard RTK engine |
| MAC | Rover | No - broadcast to all | 1014-1017, 1037-1039, plus master MSM | Network-RTK engine |
| FKP | Rover | No - broadcast to all | 1034 + master MSM | Network-RTK or FKP-aware engine |
| i-MAX | Server | Yes | MAC-style (1014-1017) but degenerate | Standard MAC-aware RTK engine |

| Mode | Server load per rover | Bandwidth per rover | Origin | Common in |
| VRS | High (full epoch processing) | ~1-2 kbps | Trimble (early 2000s) | Most commercial NRTK; SAPOS BW; Italian regionals |
| MAC | Very low (broadcast) | ~3-8 kbps | Geo++ + Leica | German SAPOS states; Swiss swipos; some EUREF nodes |
| FKP | Very low (broadcast) | ~1-2 kbps | Geo++ (SAPOS heritage) | German SAPOS states (legacy); some Austrian networks |
| i-MAX | High (server interpolation) | ~3-8 kbps | Trimble | Some Trimble-supplied national networks |

All four modes look identical once fixed; operator's choice. MAC firmware question only matters when non-MAC rover gets float-only on MAC mountpoint.

## 7. Ionospheric Effects

### 7.1 Physical Mechanism

Ionosphere = solar-UV plasma. Free electrons slow group velocity ~1/f². 1 TECU = 10¹⁶ e/m²; L1 delay ~0.162 m/TECU ✓. Quiet mid-lat ~5-20 TECU; severe storm 200+ TECU. ~

### 7.2 Solar Cycle

~11-year cycle. ~ Cycle 25 peaked Oct 2024 (SSN 160.8) ✓; 2025-2026 elevated; above-avg RTK degradation risk until ~2027-2028. ✓ Affects: max baseline, TTFF, cycle slip frequency.

### 7.3 Geomagnetic Activity (Kp Index)

| Kp | Activity | RTK impact |
| 0-2 | Quiet | Minimal; normal RTK performance |
| 3-4 | Unsettled (G0-G1 onset) | Kp>3 considered active ✓; high-lat stations begin to show iono gradient growth |
| 5 | Minor storm (G1) | ~ Fix difficult at baselines >20 km, NRTK may degrade at high latitudes |
| 6 | Moderate storm (G2) | Noticeable mid-lat degradation confirmed ✓; IAR success rate can fall |
| 7 | Strong storm (G3) | IAR success rate can drop from 94% → 31% ✓; high-lat median error 2.4 cm → 9.0 cm ✓ |
| 8-9 | Severe/Extreme (G4-G5) | RTK fix near-impossible at affected latitudes; even NRTK degrades |

High-lat caveat: global Kp poor predictor for IceCORS/N.AUSCORS/TrigNet; Kp 3-4 = large local auroral gradients ✓; use NOAA wing-kp regional, not global Kp. ~

Real-time Kp: swpc.noaa.gov (3-day forecast available).

### 7.4 Ionospheric Scintillation

~±15° lat + auroral zone: rapid TEC fluctuations -> cycle slips, fading, IAR failure. ~ Worst ~sunset + solar max. Operationally observed in equatorial Indonesia, Colombia, Brazil, southern Africa, and the auroral oval.

### 7.5 Polar / High-Latitude

IceCORS, N.AUSCORS: auroral electrojet; fast TEC gradients. ~ NRTK partially compensates; solver can diverge in strong events. ~

### 7.6 Practical

"Fix yesterday not today": (1) Kp current + past 3-6 h (recovery hours after peak); (2) sunset scintillation? (3) closer station; (4) L1-only: dual-band = structural fix.

## 8. Latency and Fix Quality

### 8.1 Sources

End-to-end NTRIP RTK: base obs (~1 Hz) + RTCM encode (<5 ms) + base->caster TCP (5-200 ms) + internet (10-100 ms) + rover receiver (<10 ms) + RTK engine (<50 ms) = ~50-500 ms total. ~

### 8.2 Effect on RTK

Stationary: 1-2 s latency negligible. Moving: error = latency × velocity (10 m/s × 500 ms = ~5 m); Doppler/IMU reduce. ~ Sustained >60 s correction age -> F9P downgrades to float/autonomous. ✓

### 8.3 Observation Rate

1 Hz typical (free networks); 5/10 Hz some RTKBase installs. Static: 1 Hz adequate. Fast rovers (>5 m/s): higher rate reduces stale-correction error. ~

### 8.4 Practical Numbers

Urban 4G: 50-100 ms; rural 4G marginal: 100-500 ms; Starlink: 20-60 ms ~; geostationary: 500-800 ms (RTK marginal); home WiFi: 10-50 ms. ~

### 8.5 Diagnosis

Drops every few minutes: cellular latency spikes -> check correction age; closer caster; Android battery optimisation off; str2str relay.

## 9. Multipath

### 9.1 Mechanism

Reflected signal travels longer path; receiver sees direct + delayed superposition. ~

Pseudorange error: sinusoidal, up to half chip length. C/A ~293 m chip ✓; narrow correlator limits practical envelope ~5-15 m; >15 m rare ✓; avg 0.5-3 m. ✓ Carrier-phase error: up to quarter-wavelength (~5 cm L1). ~ RTK accuracy floor in non-ideal environments.

### 9.2 Characteristics

- Static: oscillation period tens of minutes; moving rover: seconds.
- Low-elevation sats more affected; 10-15° mask cuts severe multipath. ~
- Parking lots, metal roofs, water, facades = major reflectors.

### 9.3 Mitigation

Antenna: choke-ring (best, $1000+); ground plane (cheap, moderate); helical/back-cavity (some benefit). ~ Receiver: narrow correlator reduces code multipath; limited carrier-phase effect. Rule: choose site, not receiver.

Software: elevation-weighted; sidereal maps (repeat ~24h-4 min, subtract prev-day residuals). ~ NRTK averages atm corrections, not base multipath.

### 9.4 Practical Impact

Urban/suburban rover: ~2-5 cm floor from multipath, not IAR. Base site selection = most important. Rooftop near HVAC/parapets -> degrades corrections for all connected rovers.

## 10. Base Station Setup

Base quality affects all connected rover accuracy.

### 10.1 Hardware

Min: dual-freq + RTCM 3.x. ZED-F9P dominant: GPS L1C/A+L2C, GLONASS L1OF+L2OF, Galileo E1B/C+E5b, BDS B1I+B2I ✓; MSM4/7 + raw ✓; ~$88-180 bare / ~$200-400 on breakout (ArduSimple simpleRTK2B, SparkFun GPS-RTK2). ~ Permanent base: RPi4 ~5W 24/7. ~

Antenna (highest-impact decision): ANN-MB ~$30 poor; survey patch (Tallysman TW3742; Beitian/ArduSimple from ~$80) ~$80-250 moderate (good hobbyist base); helical ~$100-200 moderate (nearby obstructions); choke-ring ~$3-7k excellent (network grade, overkill single-user). Good survey patch + ground plane outperforms cheap patch + choke-ring. ~ Full table: §14.2.

Software: RTKBase (github.com/Stefal/rtkbase): RPi, web UI, NTRIP push+log+RINEX. Recommended. str2str (RTKLIB) CLI back-end. u-center: F9P config (run once).

### 10.2 Antenna Placement (base-specific; full checklist §14.7)

- 360° clear sky above 10-15°.
- No metallic surface within ~1 m.
- Rigid stable mount; radome from direct rain (~1 cm wet-radome error). ~

Bad: flat metal roof; HVAC-adjacent; under trees; tilted surface.

### 10.3 Base Position Determination

#### A: Average Over Time
1-24 h autonomous average; ~1-3 m absolute. Adequate relative; not national coord tie. Frame = broadcast-ephemeris realisation @ survey-in epoch (currently WGS84 G2139 ≈ ITRF2014); frozen at install instant -> drifts vs true ITRF at full plate rate after install. F9P TMODE3 SVIN does not refresh ✓ (F9P Integration Manual: "the reference datum cannot be changed and is always set to WGS84"). See §13.7.

#### B: PPP (recommended)
Upload 24h+ RINEX:
- CSRS-PPP (NRCan): free; ITRF+NAD83; 24h ~1-3 cm, 1 wk sub-cm. ✓
- AUSPOS (GA): ITRF2014, Asia-Pacific tuned. ~
- GIPSY-OASIS (JPL): free non-commercial. ~

Enter ECEF into RTKBase fixed-mode.

#### C: Known Benchmark
Occupy national benchmark; use published coords. Best absolute.

### 10.4 Registering with Public Casters

rtk2go: register at rtk2go.com/new; manual approval ~hours; push to `rtk2go.com:2101` with mountpoint name + assigned password; free non-commercial. ~

Centipede: register at crtk.net (GitHub-based); RTKBase integrates registration. ~

### 10.5 RTCM Message Selection for a Base Station

RTKBase default output ✓:
```
1004, 1005(10), 1006, 1008(10), 1012, 1019, 1020, 1033(10),
1042, 1045, 1046,
1077, 1087, 1097, 1107, 1127, 1230
```
Parentheses = interval in seconds; others 1 s. Key: `1005`/`1006` base pos; `1077/87/97/07/27` GPS/GLO/GAL/SBAS/BDS MSM7; `1019/20/42/45/46` ephemeris; `1230` GLONASS IFB. MSM7 = right F9P default (~1-2 kbps vs ~0.5-1 MSM4); only switch to MSM4 on GPRS/sat link.

Minimum viable constrained link: `1005(10), 1077, 1097`

### 10.6 Survey-In vs Fixed Mode

Base must know own position. Two modes:

Survey-in: averages autonomous positions. ZED-F9P CFG-TMODE3 ✓: `CFG-TMODE-SVIN_MIN_DUR` (default 300 s); `CFG-TMODE-SVIN_ACC_LIMIT` (default 500000 = 50 m -> effectively completes after 300 s). Quality base: set 20000-50000 (2-5 m), 300-600 s min.

PPP path: skip survey-in; configure fixed mode with ECEF from §10.3 Method B.

Failure mode: base stuck in survey-in (threshold never met) -> unstable reference -> rover drifts while displaying fix. Common "fixed but wrong" bug.

### 10.7 Monitoring a Running Base

Healthy signs: sats ~8-12; "Survey-in complete"/fixed mode active; RTCM rate matches config; no cycle slips (RTKBase graphical).

Problem signs:
- Sat count drops periodically -> obstruction/interference
- Phase noise elevated on specific sats at specific times -> multipath from fixed reflector (time-of-day repeatable)
- Base position drifting -> still in survey-in or autonomous (§10.6)
- Caster connection dropping -> check internet, caster-side limits

### 10.8 RINEX Logging

RTKBase logs RINEX (via RTKLIB convbin) alongside NTRIP. Uses:
- PPP base position: upload 24 h RINEX to CSRS-PPP -> ECEF -> fixed-mode config (§10.3B).
- PPK: drone logs RINEX in field, post-process against base RINEX in RTKPOST/demo5 (§16).

RINEX naming: 3.x `<StationName><MonumentCode>_R_<YYYY><DDD><HH><MM>_<duration>_<interval>_<system>O.rnx`; 2.x `<sta><DDD><sess>.<YY>o`. RTKBase: 3.x, hourly rotation, retains `.ubx` raw binary.

## 11. Troubleshooting

Symptom -> cause -> steps. "User" = hobbyist on free NTRIP networks.

### 11.1 Float not Fix

Corrections flowing; IAR unresolved. Likely causes:
1. Baseline >30 km -> choose closer station.
2. <5-6 clean sats (PDOP high) -> open sky; wait for geometry.
3. Kp>=5 (swpc.noaa.gov) -> wait for iono to settle.
4. Warmup (<30-120 s after connect) -> wait.
5. Format mismatch (RTCM 2.x old base) -> check legacyFormat flag.
6. Missing 1005/1006 -> verify with SNIP or str2str monitor.

### 11.2 Fix drops every few minutes

Correction age exceeds F9P timeout (60 s default).
1. Check correction age in client.
2. Android: disable battery optimisation for NTRIP app.
3. Latency spikes >500 ms -> better cellular or closer caster.
4. Local relay: `str2str -in ntrip://... -out tcpsvr://:2101` caches stream, decouples rover from cellular.

### 11.3 "RTK worked last week, nothing has changed" / Mountpoint Disappeared

1. Check if mountpoint disappeared. Volunteer bases disconnect silently; SNIP drops dead stream within seconds. Reload map - if pin gone, treat as unavailable.
2. Check space weather. Geomagnetic storm degrades RTK 12-24 h after Kp falls (residual TIDs). swpc.noaa.gov past-3-h Kp; see §7.3.
3. Check sourcetable changed. Base may have changed format descriptor or coordinates; some rover firmware rejects stream on metadata change.

Why volunteer mountpoints disappear (frequency order): dynamic IP change after ISP reboot/DHCP renewal -> NTRIP push fails; power outage without UPS; hardware failure; operator moves/sells/loses interest; router/firewall blocking port 2101; RTKBase auto-start broken by OS update. ✓ (rtk2go docs; SNIP KB)

How long visible: disappears immediately. rtk2go: "Your base station name will not appear in NTRIP caster tables unless actively connected and sending data." ✓ Registration persists indefinitely; operator can reconnect any time -> live instantly.

Scale: ~800 of ~11000 registered rtk2go mountpoints active at any time (~7%). rtk2go: "50000-150000 connections/day" include many attempts to dead streams. ✓

Recovery:
1. Map -> nearest alternative physical-station pin. Check `rtk2go.com:2101/SNIP::STATUS` for per-stream uptime %.
2. Switch to national survey network (§5.11). Government CORS = monitored uptime + systematic repair. Registration usually free and fast.
3. Centipede: centipede-rtk.org/maps shows red/green updated every 30 s; operators get auto-email on >5 min offline. ~
4. rtk2go support (`support@use-snip.com`): ask if mountpoint permanently removed or temporarily offline. Operator addresses not exposed in sourcetable. ✓

Volunteer reliability: well-maintained = 99%+ uptime; many run seasonally. Mission-critical work (legal survey, production machine control): use government CORS or commercial SLA; volunteer = gap-filler.

### 11.4 Fix but position off by >1 m

1. Short survey-in base (30 s or 5 min) -> base 1-3 m off absolute; rover correct relative, wrong absolute. Use network caster.
2. Datum mismatch: ITRF vs national datum 0.2-2.2 m (§13.1). Apply transformation.
3. Undetected cycle slip: multipath shifts fix by ~19 cm integer steps. Re-acquire in clean sky; compare.

### 11.5 NTRIP Connection Fails (Firewall)

NTRIP = plain TCP; port 2101 = convention only. Symptom -> cause:

| Symptom | Likely cause |
| Hangs 10-30 s, then "Connection timed out" | Outbound TCP blocked by firewall (SYN dropped, no reply) |
| "Connection refused" immediately (< 1 s) | Port reachable but no service listening (wrong port, caster down) |
| TCP connects, then garbled text or no data | Protocol mismatch: HTTP client sent to NTRIP 1.0 raw-TCP caster (common with SAPOS) |
| TCP connects, authenticated, zero RTCM bytes | VRS mountpoint waiting for GGA; enable GGA output in the NTRIP client |
| "Bad password" / "401 Unauthorized" in under 1 s | Credentials wrong; network layer is fine |

Blocking contexts:
- Corporate/campus WiFi: egress 80/443/8080; port 2101 not whitelisted; non-standard (9879/10011/10700) even less. ✓
- Public WiFi: 80/443 only.
- 4G/5G consumer: arbitrary TCP passes; port 2101 works. ✓
- Enterprise IoT SIM: APN may whitelist specific ports.

Firewall-friendly: port 443 TLS or 8080 traverses most corporate egress. ✓

Diagnostics:
1. LTE but not WiFi -> WiFi firewall.
2. `nc -zv rtk2go.com 2101` (Linux/mac) or `Test-NetConnection rtk2go.com -Port 2101` (PS).
3. `curl -v http://rtk2go.com:2101/` -> STR/CAS/NET = port open.
4. ping replies + TCP hangs = host up, port filtered.
5. VPN/SSH tunnel NTRIP over 22/443 as workaround.

### 11.6 Receiver Fix but mapping app wrong position

Android (3 mechanisms); iOS = #3 only:
1. Mock location not set: Developer Options -> "Select mock location app" must point to NTRIP client.
2. App rejects mock location (`Location.isFromMockProvider()`) -> silently reverts to phone GPS.
3. NMEA dialect mismatch: talker ID `GPGGA` vs `GNGGA`; app ignores fix-quality field. Fix: set firmware to emit `GNGGA`. ✓

Diagnostic: compare coords in receiver app vs mapping app. Different = source broken between receiver and app; §11.1-11.5 don't apply.

### 11.7 Base coordinates jumped after firmware update/reboot

Base re-entered survey-in; new position differs ~1-3 m. All rovers see coordinated step.

Causes:
1. `CFG-TMODE-MODE`=survey-in (1) re-runs on cold start. Fix: set =fixed (2) + `CFG-TMODE-ECEF-X/Y/Z`. ✓
2. Firmware update reset CFG store. Back up with u-center File->Config->Send before updates.
3. `CFG-TMODE-FIXED_POS_ACC` too tight (e.g. 1 mm) -> silent fall back to survey-in. Set 10-50 mm.
4. Config in RAM layer only; BBR/FLASH survive cold boot; RAM lost on power-cycle. ✓

Recovery: re-enter known ECEF (PPP report, RTKBase log), or re-run 24 h PPP (§10.3B).

### 11.8 NTRIP log garbled / NMEA parse errors

TCP up but byte stream not clean RTCM. Diagnostic:

| Symptom | Likely cause |
| First ~200 bytes are HTTP-like text (`SOURCETABLE 200 OK`, then table) | Client requested `/` instead of `/MOUNTPOINT`; reading the sourcetable. Restart with mountpoint URL. |
| Stream begins with `RTCM3` or `0xD3` byte then breaks | Likely stream is fine; client is mis-parsing - try `str2str` to log raw bytes and decode separately. |
| Stream is repeating identical 200-byte chunks | Caster sending keep-alive padding because base is offline. Pick a different mountpoint. |
| Mixed binary + ASCII in random places | Two streams interleaved on a misconfigured mountpoint, or a transparent proxy injecting HTML error pages on TCP errors. |
| Stream stops cleanly after N seconds, no error | Mountpoint reached its max-connection-time limit (some casters disconnect after 1 h). Reconnect. |
| GGA upstream produces "400 Bad Request" reply | NTRIP v1 caster expecting raw TCP; client sending HTTP/1.1 chunked GGA. Switch client to NTRIP v1 mode. |

Dev tools: `str2str -in ntrip://user:pass@host:2101/MOUNT -out file://dump.rtcm` logs raw bytes; `convbin dump.rtcm` validates; BNC shows per-message counts.

### 11.9 Velocity wrong / stationary but non-zero velocity

Stationary ~0.05-0.5 m/s = normal Kalman behaviour, not fault.

Actual problems:
- >1 m/s stationary -> multipath-corrupted sats. Common urban/canopy.
- Non-zero + position drifting at same rate -> float mode (§3.3).
- Exactly zero at moving rover -> static dynModel (`dynModel=2`). Fix: `dynModel=0` (Portable, default); `=4` (Automotive); `=6/7/8` (Airborne <1g/2g/4g). ✓

PPK: RTKLIB velocity from pos[n]-pos[n-1]/dt; inherits position noise. Drone pipelines ignore velocity field, re-derive from positions.

## 12. Use Case -> Accuracy Requirements

RTK fix = 1-3 cm; commercial PPP (RTX, Skylark) ~2.5 cm; HAS SL1 ~20 cm H, 10-15 min convergence.

| Use case | Required H accuracy | Required V accuracy | Adequate mode | Free PPP (HAS) adequate? | Key non-accuracy constraints |
| Navigation / hiking | 3-10 m | 5-20 m | Standalone GNSS | Overkill | TTFF, battery |
| Variable-rate ag application | 25-50 cm | N/A | SBAS or RTK float | Yes | Field prescription zone size |
| Precision ag auto-steer | ±2.5 cm pass-to-pass | N/A | RTK fix or commercial PPP | No (HAS ~20 cm) | Coverage, convergence, seasonal repeatability |
| Machine control (grading) | ±10-20 mm | ±10-20 mm | RTK fix | No | Uptime SLA, datum tie to design, blade calibration |
| UAV photogrammetry - GCPs | ±10-20 mm | ±15-30 mm | RTK fix | No | GCP distribution; target ≥ 3× GSD |
| UAV photogrammetry - PPK drone | ±20-50 mm | ±30-70 mm | RTK / PPK | No | Base RINEX log; antenna offset cal |
| GIS utility mapping (ASCE QL-B) | 100-300 mm | 150-500 mm | RTK float or SBAS | Yes (marginal) | Sky visibility; attribution |
| GIS cadastral survey | ±10-50 mm | ±10-50 mm | RTK fix | No (HAS ~20 cm) | Regulatory acceptance; datum tie |
| Construction stakeout | ±10-25 mm | ±10-25 mm | RTK fix | No | Datum tie to project control; tilt-pole correction |
| Structural displacement monitoring *(beyond hobbyist scope)* | ±1-5 mm | ±2-5 mm | CGNSS post-processed | No | Monument stability; IGS precise products |
| Scientific geodesy *(beyond hobbyist scope)* | ±0.1-1 mm | ±0.2-2 mm | PPP + IGS final orbits | No | Choke-ring antenna; ANTEX model; 24 h+ sessions |

Notes: auto-steer relative within season <2.5 cm; HAS (~20 cm) fails ✓. Cadastral: commercial PPP meets ALTA/NSPS in principle; HAS fails; some jurisdictions require network RTK specifically. ~ GIS QL-B: ~150 mm H; HAS meets with margin. ~ Machine control: float (0.1-0.5 m) never acceptable; uptime drives commercial choice. Structural: single-epoch RTK 5–15× coarser than detection threshold; time-series required.

Sources: ASPRS 2015; ICSM SP1; NOAA NGS; ASCE 38-22; Emlid RS2+ spec. ~

## 13. Datum and Coordinate System Confusion

"Position wrong by N metres" -> one of four causes below.

### 13.1 Reference Frame Hierarchy

- ITRF: global standard; tracks plate motion. Realizations ITRF2000/2008/2014/2020.
- WGS84 G2139+: aligned with ITRF2014 at ~1 cm; GNSS broadcast-ephemeris output = WGS84/ITRF at observation epoch ✓. NGA aligned WGS84 to ITRF2020 (G2296) Jan 2024 ✓.
- ETRS89: realised as ETRF2000; fixed to Eurasian plate at 1989.0; plate ~25 mm/yr -> 2026 offset ~0.93 m NE ✓.
- GDA2020: fixed Australian plate at 2020.0; 70 mm/yr -> 2026 offset ~0.42 m ✓. GDA94 (ep 1994.0): ~2.24 m @ 2026 ✓.
- NAD83(2011) ep 2010.0: fixed N. American plate; 0.5-2 m from ITRF2014, direction-dependent; Pacific margin worst (transform-fault smearing on top of plate-fixed offset) ✓.
- RGF93 v2b (France): = ETRF2000 ep 2019.0 ✓. Note: realisation epoch (2019.0) ≠ frame name's "2000". Easy mistake.
- SIRGAS2000 (BR + S. America): ep 2000.4; ~12-15 mm/yr drift vs current ITRF ~.
- JGD2011 (JP): ~10 cm vs current ITRF + post-Tōhoku co-seismic offsets up to several m in NE Honshu ~.
- Classical non-geocentric (OSGB36, NTF, Tokyo): local ellipsoid; 50-200+ m from WGS84. OSGB36 ~70-120 m ✓.

Approximate horizontal offsets from current ITRF @ 2026:

| Datum | Region | Offset @ 2026 | Drift rate |
| WGS84 (G2139/G2296) | Global | <2 cm (= ITRF2014/2020) | tracks ITRF ✓ |
| ETRS89 (ETRF2000) | Western Europe | ~0.93 m NE ✓ | 25 mm/yr ✓ |
| GDA2020 | Australia | ~0.42 m ✓ | 70 mm/yr ✓ |
| GDA94 (legacy) | Australia | ~2.24 m ✓ | 70 mm/yr |
| NAD83(2011) ep 2010.0 | North America | 0.5-2 m, dir-dependent ✓ | <2 cm/yr interior, up to 5 cm/yr Pacific margin |
| RGF93 v2b | France | ~0.93 m NE (= ETRF2000 ep 2019.0) ✓ | 25 mm/yr ✓ |
| SIRGAS2000 | Brazil + S. America | ~30-40 cm ~ | 12-15 mm/yr ~ |
| OSGB36 | United Kingdom | 70-120 m (datum, not epoch) | n/a |

### 13.2 Plate Tectonics / Multi-Year Drift

ITRF coords of a stable mark advance at plate velocity. Two RTK fixes 2 yr apart: AU ~140 mm; W. Europe ~50 mm.

GDA2020 plan (ep 2020.0) + RTK ITRF (2026.3) -> ~440 mm offset. Fix: ICSM epoch-conversion (PROJ time-dependent transform, ICSM QGIS plugin AU, NGS HTDP US) ✓. xyHt worked example: 2 cm/yr × 14 yr = 28 cm if epoch ignored ✓. Inside Unmanned Systems: 2005-surveyed reference station + 2019-frame project -> ~50 cm discrepancy ✓.

### 13.3 Geoid vs Ellipsoid

- h (ellipsoidal): above GRS80 ellipsoid. GNSS/RTK direct output.
- H (orthometric): above geoid (~MSL). Engineering/topo maps.
- N (undulation): H = h - N.

EGM2008 global N range ✓ (Pavlis et al. 2012 JGR):

| Region | Approx N |
| Minimum (south of India) | -106 m |
| Maximum (New Guinea / equatorial Pacific) | +85 m |
| Central Europe | +35 to +55 m |
| Australia | +5 to +30 m |
| Central North America | -40 to -10 m |
| Iceland | +20 to +40 m |

Receiver reports +135 m, topo map +80 m -> 55 m undulation; receiver correct. Apply national geoid: GEOID18/12B (US free), AGAP2020 (AU); ~1-2 cm accuracy. ~ Emlid Flow, QField+PROJ, Trimble TerraFlex apply automatically with model file.

### 13.4 EPSG Codes

Key RTK codes:

| EPSG | CRS | When you encounter it |
| 4326 | WGS84 geographic (degrees) | Default output of all GPS devices; Google Maps, OpenStreetMap |
| 4979 | WGS84 3D (+ ellipsoidal height) | RTK output with altitude; "raw" GNSS CRS |
| 4258 | ETRS89 geographic | Europe - pan-European official datum |
| 7844 | GDA2020 geographic | Australia - current national standard |
| 4283 | GDA94 geographic | Australia - legacy, being retired |
| 4269 | NAD83 geographic | North America |
| 27700 | OSGB36 / British National Grid | UK Ordnance Survey maps |
| 32601-32660 | WGS84 / UTM zones 1N-60N | Common metric projected CRS worldwide |
| 5703 | NAVD88 vertical | US official orthometric heights |
| 3855 | EGM2008 geoid height | Current global geoid reference surface |

### 13.5 Position off 1-2 m vs Google Maps

Causes (descending frequency):
1. Datum offset: Google Maps = WGS84/ITRF (EPSG:4326); national casters in national datum. ETRS89 ~0.93 m NE ✓; GDA94 ~2.24 m ✓; GDA2020 ~0.42 m ✓; NAD83 0.5-2 m ✓ (all @ 2026). Systematic offset same direction/magnitude across site -> datum shift. Apply national transform.
2. Imagery georeferencing: major cities 1-3 m; rural 5-20+ m; forest/desert up to 50+ m. ~ Inconsistent offset -> imagery, not GNSS.
3. Volunteer base (rtk2go, Centipede outside FR) = no declared frame, no declared epoch (§13.7). Per-base offset; direction/magnitude unpredictable across the network. RTCM stream does not signal which.
4. Same-base re-occupation across years = relative vector preserved (plate motion common-mode); absolute coord drifted ~25-70 mm/yr depending on plate. Different base between visits = apparent drift looks random.
5. Wrong geoid model: altitude wrong, horizontal correct.

### 13.6 Transformation Tools

PROJ (proj.org, inside QGIS/GDAL/PostGIS): v6+ time-dependent plate-motion. Grid shift files free from PROJ CDN: US NADCON5; AU ICSM GDA94/GDA2020; UK OSTN15/OSGM15. QGIS 3.x applies on-the-fly.

Online: CSRS-PPP (ITRF+NAD83 from RINEX) ✓; NGS NCAT (epoch-aware NAD83<->ITRF US); ICSM QGIS plugin (GDA2020+epoch). ~

### 13.7 Frame/epoch in free public NTRIP

Audience: hobbyist NTRIP user, decimetre target. Sub-decimetre + survey-grade users figure it out or pay; not the audience.

Core fact: RTCM 1005/1006 carries XYZ + dead DF021 (§4.2). No in-stream frame, no in-stream epoch -> rover blind to either. SW Maps / Emlid Flow / RTKLIB surface nothing ✓. Frame info lives in network docs only.

Hobbyist sanity check on connect:
- Stand on identifiable feature (road centreline, fence corner, marked path) -> get fix -> open Google Maps / OSM.
- Within ~1 m, same direction across site = frame offset, normal, carry on. Within-session relative geometry unaffected.
- Several m, varying = imagery georef (1-3 m city, 5-20 m rural, up to 50 m forest/featureless).
- 10s of m = something else broken (false fix, wrong MP, base misconfigured).

For decimetre work the check is the whole answer.

Time-extended hobbyist work (palaeontology re-visits, plant demography year-over-year, monitoring quadrats, drone re-flights) = different problem: base may not exist next year, and fix value alone carries no record of which frame produced it. Three tiers ordered by extra effort:

[tier 1] record metadata alongside coordinate: caster host:port, mountpoint, network, date, gear. Zero extra time. Lets future user reconstruct frame *if* network still exists. Doesn't help if volunteer base gone.

[tier 2] tie to persistent local feature each visit: road junction, boundary stone, fence-post corner in concrete, rock face. Take fix on local feature + fix on each find/patch every visit. Store finds as offset from feature. Future visits re-occupy feature with whatever gear/base, apply stored offset. Robust to base churn. Workhorse protocol for botany year-over-year + palaeontology re-visits.

[tier 3] bypass volunteer-base churn:
- Use national survey network where coverage reaches (SAPOS, AUSCORS, EarthScope NOTA, ERGNSS, RBMC, RAMSAC, FReDNet, etc.) -> declared frame, monitored uptime, persists. Collapses tier 1+2 for users in coverage.
- Pay for commercial network with declared epoch (swipos CH, HxGN SmartNet, Trimble VRS Now, Leica SmartNet). Out of free scope; only path in CH (no free public NTRIP).
- Set up own base with documented coordinate + epoch (§10.3). User controls frame, persistence, records.
- Galileo HAS = different gear path: free, global, ~20 cm horizontal, time-stable across years (derived from satellite ephemeris + live precise-orbit products), no base. Convergence 7-15 min. Requires E6-tracking hardware (UM980/UM982, Mosaic-X5, LG290P, Eos Arrow Gold+); F9P cannot do E6 ✓. Right answer for users buying gear specifically for time-extended work.

PPP post-processing of raw observations (CSRS-PPP, AUSPOS) = professional path, not hobbyist tier; F9P-class users rarely do this. Mention in passing only.

Network-tier reality:

[gov-network] Frame + epoch declared in writing; cross-station consistency enforced:
- AUSCORS: GDA2020 ep 2020.0 (plate-fixed AU); MP name encodes frame ✓.
- EarthScope NOTA: ITRF2014 current ep, refreshed regularly; non-NOTA MPs "best estimate, no precise epoch" ✓.
- SAPOS: ETRS89/ETRF2000 per Land; some Länder broadcast 1021/1023 for national-projection clients ~.
- ERGNSS, FReDNet, RBMC-IP, RAMSAC, TrigNet, etc.: ETRS89 / SIRGAS2000 / Hartebeesthoek94 / etc., per network website; never in stream.
- RAMSAC + FReDNet + MnCORS = exceptions: declare frame in sourcetable misc field or MP name ✓ (own grep, data/*.sourcetable, 4200+ STR records).

[centipede-FR] Strict workflow: 24 h+ RINEX -> IGN online service -> RGF93 v2b report (= ETRF2000 ep 2019.0) -> RTKBase fixed mode ✓. "2000" in ETRF2000 = realisation year, not epoch. Frame consistent across French Centipede bases. Not declared in RTCM. 1-2 wk registration review = real for FR (IGN report auditable); weaker outside FR.

[centipede-intl] Recipe-only: docs tell EU operators ETRF2000 via EUREF ECTT; rest-of-world ITRF20 current ep direct. No central post-processing, no enforcement. Some operators inherit published frame from local infrastructure (parts of HU, PL bases mirroring state VRS).

[rtk2go] No enforced frame, no enforced epoch. SNIP "PFAT" (Position File Adjustment Tool) = paid SNIP feature + opt-in ✓ (SNIP KB: "PFAT translation ... only available on paid models of SNIP"); rare in practice. Many volunteer bases: F9P TMODE3 SVIN -> autonomous fix (~1-3 m absolute) -> broadcast 1005 internally labelled "WGS84" but frozen at survey-in instant ✓ (F9P Integration Manual). After 2-5 yr antenna has moved at full plate speed in true ITRF; broadcast 1005 has not. Some operators do PPP install + maintain coords; sourcetable does not distinguish.

Hobbyist consequences (calibrated, not worst-case):

1. Same volunteer base, same point, weeks-month later: cm if base still streaming. Often the case.
2. Same volunteer base, same point, year+ later: few cm if base still there + coord unchanged.
3. Different volunteer base, same point, year+ later: usually within few cm; sometimes 10-30 cm if bases set up in different frames or different epochs; occasionally worse if one was autonomous SVIN. No in-stream signal which case applies.
4. Centipede-FR vs Google Earth/OSM @ 2026: ~93 cm NE systematic (RGF93 v2b = ETRF2000 ep 2019.0 vs ITRF current); PROJ EUREF transform fixes it.
5. AU rtk2go autonomous-SVIN'd 2020 + project in GDA2020: lucky cancellation ~0 cm. Same base + WGS84/Google Earth: ~42 cm @ 2026, growing.

What well-run free networks tell users about epoch:
- AUSCORS: GDA2020 plate-fixed @ ep 2020.0; no per-flight epoch math within AU; HTDP-equivalent only for ITRF tie.
- EarthScope NOTA: refreshed epoch published per stream; for stable frame use derived NAM14 product, not real-time stream.
- SAPOS: stays ETRS89 (plate-fixed Eurasia); convert only for ITRF comparison.

Documented real-world:
- StephaneP (OSM diary): measured ~70-80 cm offset between RTK fix + French BDOrtho, traced to RGF93 vs WGS84; OSM database de-facto mixed-datum because contributors merge ETRS89/NAD83/WGS84 without transformation ✓.
- AgOpenGPS Discourse: multiple "10 m off after RTK2GO coordinates" + "RTK status but drifting" threads root-caused to base coord quality ✓.
- Emlid community: NRCan CSRS-PPP outputs NAD83(CSRS) or ITRF, never literal "WGS84"; entering NAD83 into Reach as if WGS84 -> silent ~1 m offset ✓.
- Inside Unmanned Systems: 2005-surveyed reference + 2019-frame project = ~50 cm discrepancy ✓.

Project-internal sourcetable evidence (2026-04, data/*.sourcetable):
- rtk2go (883 STR): zero frame/epoch identifiers in any field.
- centipede (1223 STR): zero frame/epoch identifiers in any field.
- ramsac: declares "Marco POSGAR07-ITRF2005(2006.632)" in misc field — frame + decimal-year epoch.
- frednet: declares "Reference System ETRS89" in misc field on legacy single-base streams.
- mncors: encodes datum in MP name (CMR_Plus_NAD83(1996), CMR_Plus_NAD83(2011)).
- AUSCORS, EarthScope, RBMC-IP, TrigNet, gcgc_rtn: zero in sourcetable; declared on website only.
3 of 66 networks declare frame anywhere a rover-side parser can see.

Evidence thin on:
- Fraction of rtk2go bases SVIN vs PPP — inferred from forum tone.
- Cross-base agreement among rtk2go bases — no formal study.

User-facing surfacing: guide.html `#archival` (recording protocol) + `#precision-limits` (tectonic / epoch explainer). Help topic `position-off-vs-google-maps` rewritten to branch by network type + cross-link guide. is-this-for-me preamble flags time-extended use cases. AI-guide depth lives here.

## 14. Antennas

Antenna = largest RTK accuracy determinant after baseline length. F9P-class hardware: noise floor set by antenna, not chip. §1.6 = phone antenna; this section = external antenna selection, mounting, calibration.

### 14.1 Why GNSS antenna differs from generic radio

GNSS signals ~-130 dBm (below thermal noise floor); recovered by PRN despreading. ✓ Three properties:

- RHCP. GNSS satellites transmit RHCP. Direct path = RHCP; single specular bounce off flat conductive surface -> LHCP. ✓ Diffuse/off-angle reflections = elliptical (partial RHCP retained). Well-designed GNSS antenna has high cross-polar discrimination (~15-25 dB ~) -> LHCP reflections attenuated. Main mechanism rejecting first-bounce ground multipath.
- Stable phase center across azimuth, elevation, frequency. RTK measures carrier phase to ~1-2 mm; phase center motion injects cm-scale error. See §14.3.
- Hemispherical gain with low-elevation roll-off. Ideally ~+5 dBic zenith, attenuating to horizon, sharp cutoff below. Geodetic antennas approach this; consumer patches do not.

### 14.2 Antenna families

| Family | Approx cost | Bands | Multipath rejection | Where it fits |
| Cellular/IoT GPS patch (Mokoradar, generic) | ~$10 | L1 only | Poor | Vehicle-tracking GPS, not RTK |
| u-blox ANN-MB-00 | ~$30 | L1+L2 (GNSS) | Poor | Bench testing, cheap mobile rover |
| ArduSimple / Beitian survey patch (BT-560/845, Tallysman TW3742, Harxon HX-CHX600A class) | ~$80-250 | L1+L2 (some L5) | Moderate | Hobbyist permanent base, RTK rover; the practical default ✓ |
| Helical with cavity backing (ArduSimple SurveyXYZ; Calian/Tallysman HC871/HC880) | ~$120-250 | Multi-band | Moderate-good | Compact rover where horizon obstructions exist |
| Geodetic survey antenna (Trimble Zephyr Geodetic, Leica AS10, Topcon CR-G5) | ~$1500-3500 | All bands | Good | Network reference station, mid-range survey |
| Choke-ring (Leica AR25, JPL D&M choke-ring) | ~$3000-7000 | All bands | Excellent | IGS, EarthScope, national CORS network reference monuments ✓ |
| 3D choke-ring with ROBOT-calibrated phase model (Leica AR20, Septentrio PolaNt-x MF) | $5000-10000+ | All bands | Best published | Scientific reference / fundamental geodesy |

~ Numerical separation: survey patch on 30 cm ground plane -> carrier-phase multipath ~5-8 mm RMS clean rooftop; choke-ring same site ~2-3 mm; receiver noise floor ~1 mm. ~ Public NTRIP reference stations nearly always geodetic/choke-ring; rover limits user accuracy.

### 14.3 Phase center: PCO and PCV

Phase center = apparent reception/radiation point. Not a fixed mechanical point; varies with frequency (L1/L2 sit several mm apart ✓), elevation (zenith vs 10° see different centers), and azimuth (less pronounced in well-designed antennas).

- PCO (Phase Center Offset): fixed 3D vector from ARP (mounting thread bottom) to mean electrical phase center, per band. Vertical PCO 50-90 mm; horizontal <2 mm for survey antennas. ~ ARP entered as "antenna height"; receiver applies PCO internally.
- PCV (Phase Center Variation): angle-dependent residual after PCO removal. Geodetic: <1-3 mm peak-to-peak L1 ~; survey patches: 5-15 mm ~; consumer patches: tens of mm, often uncalibrated.

Hobbyist base impact: uncalibrated PCO/PCV -> constant systematic offset on all rover positions (5-10 cm vertical plausible at L1); identical across rovers -> hides until tied to external benchmark. Antenna model in RTCM 1007/1033 must match ANTEX file (§14.4); mismatch/omission silently disables correction. ✓ (RTCM catalog; rcvr_ant.tab)

### 14.4 ANTEX calibration files

ANTEX (Antenna Exchange Format) = IGS-standardised ASCII PCO/PCV tables. ✓ `*.atx` files. Each entry: antenna name (16-char IGS convention + 4-char radome code); PCO per frequency; PCV grid (typically 5°×5° elevation × azimuth, 1°×1° for robot calibrations); calibration method code (ROBOT/FIELD/CHAMBER/COPIED/CONVERTED).

Sources: NGS calibrations (geodesy.noaa.gov; free; most major geodetic antennas; radome-specific variants) ✓; IGS combined calibration (`igs20.atx` aligned with ITRF2020; used by CSRS-PPP and AUSPOS) ✓.

Access: RTKLIB `pos1-ant1/pos1-ant2`; without ANTEX = PCO/PCV=0. F9P-class NTRIP firmware: no ANTEX files; applies built-in correction if antenna name set, else treats ARP = phase center. Matters for sub-2 cm absolute; cancels for pass-to-pass relative.

### 14.5 Ground planes

Flat conductive disc below patch: reduces sub-horizon reflections; stabilises phase center. Choke-ring has built-in.

Sizing: ~30 cm disc for L1; below 20 cm degrades quickly. ~ Hobbyist: aluminium sheet or satellite-dish back-plate. Must be flat, continuous (no perforations/paint).

### 14.6 Cabling, LNAs, bias-T

Active antennas have built-in LNA; DC power via bias-T on same coax. ~

- Voltage: ANN-MB-00 + ZED-F9P both 3.3 V (match). Survey antennas 5 V; legacy geodetic 12 V. 3.3 V antenna + 5 V bias-T -> LNA damage. Verify before connecting unfamiliar antenna. ~
- Cable loss at 1.5 GHz: RG-174 ~1.3 dB/m; RG-58 ~0.9 dB/m; LMR-240 ~0.27 dB/m; LMR-400 ~0.13 dB/m. ~ >5 m to rooftop -> LMR-240/400.
- >20 m run -> in-line LNA. Permanent rooftop: surge protector (PolyPhaser GT-NFF-A). ~

Connectors: SMA female most common; TNC (Trimble/Leica); N-type (choke-rings). SMA torque 8 lbf-in / 0.9 N-m permanent. ~

### 14.7 Antenna placement: rapid checklist

(§10.2 = base-specific; this checklist covers base + rover.) Priority order:
1. Sky above 10° completely clear 360°.
2. >=1 m from any metallic surface (HVAC, parapets, lightning rods, adjacent antennas).
3. Rigid, mass-loaded mount. Wood masts flex; thin-wall steel vibrates -> micro-cycle-slips. Concrete pillars/geodetic monuments best for permanent bases.
4. >=1 m above any flat surface to reduce ground-bounce; up to ~3 m helps; diminishing returns beyond. ~
5. Levelled + azimuth-aligned (geodetic antennas have north mark; alignment improves PCO/PCV model match).

### 14.8 Practical implications

Rover accuracy lever (after baseline): (1) dual-band; (2) ground plane; (3) antenna outside; (4) closer mountpoint. No choke-ring for hobbyists. Base: Tallysman/Harxon/ArduSimple survey patch tier correct.

## 15. Jamming, Spoofing, Interference

Post-2022 operational concern. Baltic farmer with hourly RTK failures or Black Sea boater shown 200 km inland = interference, not hardware.

### 15.1 Definitions

- Jamming: RF overpowers signal; sat count drops, fix lost, position freezes.
- Spoofing: fake GNSS signal well-formed enough for receiver to track; wrong position without dropping lock.
- Meaconing: recorded genuine signal rebroadcast delayed; receiver reports delayed/wrong position.
- Unintentional interference: out-of-band emissions (cellular, TV, LED drivers, chargers, drone telemetry). Dominant globally.

### 15.2 Jamming patterns

| Source class | Mechanism | Range | Detect by |
| PPDs (personal privacy devices) - eBay/AliExpress 12 V cigarette-lighter jammers, $20-80 | Wide-band noise across L1 (and sometimes L2/L5) | ~10-500 m line-of-sight ~ | Local outage that follows a moving vehicle; resolves when vehicle leaves |
| State / military jamming - high-power GNSS denial | Wide-band; structured patterns; may spoof simultaneously | 100s of km | Persistent over hours-days; aligns with airspace events |
| Faulty consumer electronics | Narrowband harmonic of a switching converter | ~1-10 m | Outage tied to a specific device powering on |
| Cellular / DTV out-of-band | Adjacent-band leakage filtered poorly by the antenna LNA | Site-specific | Outage tied to a specific azimuth toward a tower |

### 15.3 Geographic hotspots (post-2022)

- Eastern Baltic (EE, LV, LT, E.Poland, FI, NO, SE): Kaliningrad/Russian jamming; EASA SIB 2022-02R3. ✓
- Black Sea / E.Mediterranean / Cyprus / TR / IL / LB / SY: spoofing affecting aviation; positions 100s km off. ✓
- Persian Gulf (UAE, Iran-adjacent): chronic; airline avionics-recovery procedures.
- Korean peninsula: N. Korean jamming, coastal districts/shipping; ITU complaints 2010/11/12/16. ✓
- Conflict zones (Ukraine, Gaza, Sudan): GNSS denial routine.
- Major US airports (Newark, DFW): PPD-driven events. ~

Real-time: gpsjam.org (Clements) ADS-B NIC/NACp -> daily heatmap. ✓

### 15.4 Spoofing signatures

1. Position teleport to far-away coordinate (often major airport decoy).
2. Receiver clock disagrees with phone/NTP by seconds after onset.
3. Near-uniform C/N0 across all sats (real sats vary 10+ dB-Hz by elevation). ~

RTK + spoofing: rover tracks spoofed sats, base real -> differential cancels nothing, output meaningless. Fix/Float flags reflect IAR against whatever signals, not authenticity. Septentrio Mosaic-X5 + F9P HPG 1.50+ have OSNMA/RAIM-FDE; most hobbyist hardware does not.

### 15.5 Mitigation

Hardware:
- OSNMA: chain-of-trust nav-message auth. Detects data spoofing; not signal replay/meaconing. Operational 2023; F9P HPG 1.50+ ✓, Mosaic-X5, LG290P ✓.
- CRPA: array nulls jammers by direction-of-arrival. Aviation/military. ~
- Multi-band harder to jam: PPD must cover L1+L2+L5+E5/E6; triple-band continues on L2+L5 if L1 jammed. ~

Behavioural:
- Cross-check: cellular trilateration/IMU/Wi-Fi; divergence >100 m -> one is wrong.
- C/N0 spread: real sats 10+ dB-Hz range; spoofed ~2-3 dB.
- Receiver clock vs NTP disagreement by seconds -> spoofing suspect.
- Baltic/Black Sea/Persian Gulf/Korean: time-of-day fix-loss = jamming, not multipath/iono.

### 15.6 Implications

- Baltic volunteer outages = regional jamming, not station fault; operator contact won't help.
- Unexplained intermittent outages in affected regions -> gpsjam.org.
- OSNMA-capable hobbyist hardware (2026): F9P HPG 1.50+, Mosaic-X5, LG290P. ✓
- Fix + cm precision + 10 km error = spoofing or false-fix (§3.3).

## 16. PPK - Post-Processed Kinematic

Same carrier-phase double-differencing as RTK, post-hoc on logged raw observations. Common for UAV photogrammetry, ag surveying without cellular, or any field collection where live corrections impractical. Base RINEX log (§10.8) = enabling asset.

### 16.1 PPK vs RTK: what changes

| Property | RTK | PPK |
| Correction link | Live NTRIP, cellular, or radio | None during collection |
| Result delivery | Real-time, in field | After return to office (minutes-hours) |
| Field UI | Fix/Float status visible | None - looks like standalone GNSS |
| Forward + reverse pass | No (forward only) | Yes - both directions then combined |
| Cycle-slip recovery | Re-converges going forward | Bridges from both sides of slip |
| Accuracy floor (open sky, <=10 km baseline) | ~10-20 mm horizontal | ~5-15 mm horizontal ~ |
| Field connectivity | Needed | Not needed |

Forward+reverse: cycle slip interrupting RTK fix for 30 s is invisible in PPK (ambiguities fixed before+after, combined). ~ More robust under canopy/intermittent sky.

### 16.2 Workflow

1. Base logs RINEX/UBX while streaming RTCM for live rovers.
2. Rover logs raw; no correction link. UAVs: Reach M2, ArduSimple simpleRTK2B ✓. DJI Zenmuse L1/L2 LiDAR = closed-ecosystem; Phantom 4 RTK uses DJI toolchain.
3. Logs must overlap. Pitfall: local-time vs UTC; RINEX = UTC.
4. Process in PPK software (§16.3) -> per-epoch positions.

### 16.3 Software

Free/open-source:
- RTKLIB (Takasu, github.com/tomojitakasu/RTKLIB): reference implementation ✓. `rnx2rtkp` (CLI) + `rtkpost` (GUI): static/kinematic, forward/backward/combined. Upstream dev paused ~2017.
- RTKLIB-Explorer / demo5 (github.com/rtklibexplorer/RTKLIB) ✓: actively maintained fork; better single-freq handling, cycle-slip detection, F9P config presets. Hobbyist PPK default.
- PRIDE PPP-AR (Wuhan U, github.com/PrideLab/PRIDE-PPPAR ~): PPP-AR for solo-receiver static post-processing.

Commercial:
- Emlid Studio (free): drag-and-drop; Reach logs + third-party RINEX ✓. Lowest-friction for non-technical Reach users.
- Trimble Business Center: full survey workflow, PPK + photogrammetry. Paid.
- Inertial Explorer (NovAtel/Hexagon): PPK + IMU tightly coupled; mobile mapping standard. Paid.
- Topcon MAGNET Office / Leica Infinity: vendor-tied, format-native ingest.

### 16.4 Drone mapping

Workflow: drone carries F9P (Reach M2, simpleRTK2Blite); camera shutter time-tagged via hot-shoe; post-flight: drone log + base RINEX processed in RTKPOST/Emlid Studio -> camera positions CSV; 2-5 cm H / 3-7 cm V ~ -> control for Metashape/Pix4D/OpenDroneMap.

PPK preferred over RTK on drones: cellular unreliable at altitude; live loss = invalid segment; fwd+rev recovers RF interference.

Free RINEX base: EarthScope NOTA, IGS, AUSCORS, IBGE RBMC, ERGNSS publish archives -> use nearest CORS post-flight. rtk2go/Centipede = live-only. Own free base: RTKBase RINEX+RTCM simultaneously (§10.8).

### 16.5 Practical accuracy expectations

~ F9P + survey patch + RTKLIB demo5:
- Open-sky static, 5-10 km baseline: 5-10 mm horizontal RMS (RTK and PPK indistinguishable).
- Drone 50-80 m AGL, 5-10 km baseline: 15-30 mm horizontal, 20-50 mm vertical (camera position; GCPs needed for absolute photogrammetry tie). ~
- Forest canopy, walking antenna: PPK 3-10 cm where RTK loses fix entirely. ~ (PMC 2023 canopy study; demo5 forum)

PPK has same false-fix + iono-storm vulnerabilities as RTK. Bidirectional pass mitigates random cycle slips; not systematic errors (multipath, antenna model mismatch, base coord error).

## 17. Tilt Compensation and IMU-Aided RTK

### 17.1 Problem

Traditional pole must be vertical. 2° tilt at 2 m -> ~70 mm H error; 5° -> ~175 mm. ✓ Tilt compensation lets operator hold pole at any angle -> faster fieldwork, constrained-location access. Removes levelling overhead; does not improve absolute accuracy beyond a properly levelled pole.

### 17.2 How it works

GNSS position + IMU (3-axis accel/gyro/mag) + Kalman fusion -> antenna orientation -> pole-tip vector -> subtract offset.

Hard part = yaw-from-IMU. Magnetometers biased by ferromagnetic objects. Modern implementations (R12i, GS18 T, RS3, Altus NR3) derive yaw from GNSS heading during motion (magnetic-free). ✓

### 17.3 Calibration

Magnetic-free: walk ~5-10 m straight line to align GNSS heading with IMU. Magnetic-based: "compass dance"; drifts near metal.

Tilt range: ±30° typical ~; >45° degrades to cm. ~ Pole-length error = direct horizontal error per point; 1 cm error = 1 cm offset on every shot. Pole tip wears; re-measure for mm work. ~

### 17.4 Implementations

| Receiver | Tilt method | Notes |
| Emlid Reach RS3 | IMU + magnetometer-free heading | First sub-$3000 hobbyist tilt rover; full iOS/Android support via Emlid Flow ✓ |
| Leica GS18 T / GS18 I | IMU; visual-inertial in GS18 I | GS18 I uses a built-in camera for visual-inertial heading - it resolves pole *orientation* in environments where magnetometers and GNSS-derived heading fail; position still comes from GNSS + IMU, not photogrammetry ~ |
| Trimble R12i | TIP - Trimble Inertial Platform | Magnetic-free; advertised pole tilt up to 60° ✓ |
| Topcon HiPer VR / GR-i3 | TILT-AS / IMU | ~ |
| Septentrio Altus NR3 | IMU | OEM tilt feature ~ |
| CHC i93 / Stonex S700A / Geomax Zenith60 Pro | IMU | Mid-tier alternatives ✓ |
| u-blox ZED-F9R | IMU but heading-aided RTK, not tilt compensation | F9R is for vehicle navigation (UDR/ADR fusion); does not compute pole-tip. ✓ - common confusion |

ZED-F9R trap: "F9R has IMU, therefore tilt compensation." Wrong. F9R fuses IMU into position for vehicle GNSS outages (UDR/ADR); no concept of pole geometry. Tilt compensation = commercial firmware or external pole-tip math software.

### 17.5 DIY tilt

F9P + IMU (BNO055/ICM-20948) + Kalman + pole-tip math = possible; no DIY matches commercial accuracy. ~ Hobbyist tilt + free-NTRIP: Reach RS3 = cheapest commercial entry.

## 18. Data Licensing

"Free" networks vary in permitted uses.

### 18.1 What matters

3 legal artefacts (risk ascending):
1. RTCM stream: licensed by registration; redistribution forbidden or written permission required.
2. Position output: most networks = user's data; some require attribution on published surveys.
3. RINEX archives: same licence as live stream; factual mountpoint+coord lists = outside copyright.

### 18.2 Licence families seen in NTRIP networks

| Family | Requires | Typical examples |
| CC BY 4.0 | Cite operator when publishing | AU, NZ national agencies |
| ODbL / community-share-alike | Attribute + share-alike | Community-pool networks |
| Custom non-commercial (NULA-style) | Annual acceptance; non-commercial; no redistribution | Research consortia |
| National-survey free-use | Free in issuing country; foreign use sometimes restricted | Most European national CORS, BR, CO |
| Volunteer-pool implicit | "Use freely; don't abuse"; no formal text | rtk2go-style, community Centipede nodes |
| Restricted / paid | Commercial or government-only | Some Länder paid tiers, Gulf-state networks |

### 18.3 NULA

EarthScope NOTA: annual click-through; missed renewal -> access lost ✓; non-commercial only ✓; citation in publications ✓. "Non-commercial" = real: landscaper with paid work -> not free.

### 18.4 Rebroadcast

- Same workflow (rover+drone, same user): permissible.
- Re-serving via own caster (pulling national-CORS or community feeds): forbidden under nearly all terms. str2str ease != legal permission.

## Sources consulted

- [rtk2go.com - How it Works](http://rtk2go.com/how-it-works/)
- [rtk2go.com - New Base Station Reservation](http://rtk2go.com/sample-page/new-reservation/)
- [docs.centipede.fr - Guide RTKBase](https://docs.centipede.fr/docs/base/Guide_RTKBase.html)
- [docs.centipede.fr - Connexion au caster](https://docs.centipede.fr/docs/centipede/3_connect_caster.html)
- [RTKBase default settings.conf - GitHub](https://github.com/Stefal/rtkbase/blob/master/settings.conf.default)
- [RTCM 3 Message List - SNIP Support](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/)
- [MSM message types - Tersus GNSS](https://www.tersus-gnss.com/tech_blog/new-additions-in-rtcm3-and-What-is-msm)
- [Guidelines for IGS Real-Time Broadcasters and Stations - IGS](https://files.igs.org/pub/resource/guidelines/Guidelines_for_IGS_Real_Time_Broadcasters_and_Stations.pdf) (independent reference: RTCM MSM message type tables for all constellations including QZSS 1111-1117 and BeiDou 1121-1127 ✓)
- [NTRIP v1 spec - ESA/GSSC (PDF)](https://gssc.esa.int/wp-content/uploads/2018/07/NtripDocumentation.pdf)
- [NTRIP v1 vs v2 - SNIP Support](https://www.use-snip.com/kb/knowledge-base/ntrip-rev1-versus-rev2-formats/)
- [BKG NtripCaster Manual](https://igs.bkg.bund.de/root_ftp/NTRIP/documentation/ntripcaster_manual.html)
- [Ionospheric Delay - ESA Navipedia](https://gssc.esa.int/navipedia/index.php/Ionospheric_Delay)
- [GLONASS Signal Plan - ESA Navipedia](https://gssc.esa.int/navipedia/index.php/GLONASS_Signal_Plan)
- [GLONASS ICD v5.1 - Russian Institute of Space Device Engineering (via UNB)](http://gauss.gge.unb.ca/GLONASS.ICD.pdf) (primary specification: L1 = 1602 + n×0.5625 MHz, L2 = 1246 + n×0.4375 MHz, n = −7…+6 ✓)
- [GLONASS CDMA signals - GPS World](https://www.gpsworld.com/glonass-cdma-signals-now-on-l1-l2/)
- [Solar Cycle 25 forecast - NOAA SWPC](https://www.swpc.noaa.gov/news/solar-cycle-25-forecast-update)
- [Solar Cycle 25 progression - NOAA SWPC](https://www.swpc.noaa.gov/products/solar-cycle-progression) (actual smoothed peak Oct 2024, SSN 160.8 ✓)
- [Observed effects of geomagnetic storm on RTK - SWSC Journal](https://www.swsc-journal.org/articles/swsc/full_html/2012/01/swsc120026/swsc120026.html)
- [High-lat GNSS disturbances at sub-minor storm - Andalsvik 2014](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014RS005418)
- [ZED-F9P Product Summary - u-blox](https://content.u-blox.com/sites/default/files/ZED-F9P_ProductSummary_UBX-17005151.pdf)
- [ZED-F9P for geodetic measurement - ResearchGate](https://www.researchgate.net/publication/360316310_UBLOX_F9P_FOR_GEODETIC_MEASUREMENT)
- [ZED-F9P Integration Manual - u-blox](https://content.u-blox.com/sites/default/files/ZED-F9P_IntegrationManual_UBX-18010802.pdf) (signal bands: L1C/A+L2C, L1OF+L2OF, E1+E5b, B1I+B2I ✓)
- [ZED-F9P-05B Datasheet - u-blox](https://content.u-blox.com/sites/default/files/documents/ZED-F9P-05B_DataSheet_UBXDOC-963802114-12824.pdf) (L1/L2 + OSNMA variant - not L1/L5; annotation previously incorrect)
- [ZED-F9P-15B - Symmetry Electronics](https://www.symmetryelectronics.com/products/u-blox/zed-f9p-15b/) (L1/L5 variant ✓; the correct reference for triple-band hobbyist use)
- [CSRS-PPP - NRCAN](https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php)
- [VRS vs MAC principles - Janssen 2009](https://www.spatial.nsw.gov.au/__data/assets/pdf_file/0003/129414/2009_Janssen_IGNSS2009_VRS_vs_MAC.pdf)
- [VRS connection examples - SNIP Support](https://www.use-snip.com/kb/knowledge-base/virtual-reference-station-vrs-connection-examples/)
- [GPS C/A multipath error envelope - NovAtel tech talk](https://novatel.com/tech-talk/an-introduction-to-gnss/resources/understanding-and-mitigating-gnss-multipath-interference-and-error)
- [Multipath error envelopes - Navipedia](https://gssc.esa.int/navipedia/index.php/Multipath) (practical max ~15 m for C/A ✓)
- [GNSS Carrier-Phase Multipath Modelling and Correction - Remote Sensing, MDPI 2024](https://www.mdpi.com/2072-4292/16/1/189) (peer-reviewed; confirms carrier-phase multipath max = quarter-wavelength, ~4.76 cm at GPS L1 ✓)
- [User Guidelines for Single Base Real Time GNSS Positioning v3.1 - NOAA NGS](https://geodesy.noaa.gov/PUBS_LIB/UserGuidelinesForSingleBaseRealTimeGNSSPositioningv.3.1APR2014-1.pdf) (government authority: RTK relative accuracy ~1 cm + 1 ppm ✓)
- [ZED-F9P survey-in CFG-TMODE3 - Drotek RTK docs](https://drotek.gitbook.io/rtk-f9p-positioning-solutions/tutorials/setting-survey-in-time-and-position-accuracy)
- [ZED-F9P DGNSS timeout (NAV5 60 s default) - u-blox portal](https://portal.u-blox.com/s/question/0D52p0000DHOvhwCQD/why-is-dgnss-timeout-in-nav5-navigation-5-configuration-default-set-to-60s-for-zedf9p-module-) ✓
- [Triple-frequency RTK widelane review - JGPS 2018](https://jgps.springeropen.com/articles/10.1186/s41445-018-0010-y)
- [RTCM 3 SSR message list - SNIP Support](https://www.use-snip.com/kb/knowledge-base/rtcm-3-message-list/)
- [GLONASS K2 signal analysis 2024 - DLR](https://elib.dlr.de/204822/1/Thoelert%20etal%202024_GLONASS%20K2%20signal%20analysis.pdf)
- [RTCM Message Type 59-FKP - Geo++ White Paper](http://www.geopp.com/pdf/geopp-rtcm-fkp59.pdf) (FKP proprietary origin, standardised as RTCM 1034 ✓)
- [Ionospheric Delay formula - Navipedia](https://gssc.esa.int/navipedia/index.php/Ionospheric_Delay) (40.3×10¹⁶/f² m/TECU ✓)
- [QZSS seven-satellite constellation - Cabinet Office Japan](https://qzss.go.jp/en/overview/services/seven-satellite.html) ✓
- [NavIC constellation status - GPS World, ISRO](https://www.gpsworld.com/indias-navic-constellation-in-jeopardy-as-majority-of-satellites-become-defunct/) ✓ (degraded to <=3 operational as of March 2026)
- [Galileo HAS PPP-RTK convergence - GPS Solutions 2024](https://link.springer.com/article/10.1007/s10291-024-01617-7)
- [BDS-3 constellation completion - GPS World](https://www.gpsworld.com/two-new-beidou-satellites-complete-bds-3-constellation/) (45 total satellites, 30 BDS-3 ✓)
- [Klobuchar model correction efficiency - Navipedia](https://gssc.esa.int/navipedia/index.php/Klobuchar_Ionospheric_Model) (~50-70% RMS removal globally ✓)
- [Reach RS2+ Specifications - Emlid](https://docs.emlid.com/reachrs2/specifications/specs/) (technical spec: RTK range 60 km; 7 mm + 1 ppm horizontal ✓)
- [Single-band VS Multi-band - Emlid](https://docs.emlid.com/reach/tutorials/basics/single-multi/) (technical spec: single-band RTK baseline 10 km; multi-band 60 km ✓)
- [NOAA NGS User Guidelines for Single Base Real Time GNSS Positioning v3.1](https://geodesy.noaa.gov/PUBS_LIB/UserGuidelinesForSingleBaseRealTimeGNSSPositioningv.3.1APR2014-1.pdf) (ppm term: 1 ppm = 1 mm/km ✓)
- [SparkFun UM980 Galileo HAS E6 Convergence Test - GitHub](https://github.com/sparkfun/SparkFun_UM980_Galileo_HAS_E6_Convergence_Test) (78-trial test: avg 9.8 min convergence, 33-80 mm post-convergence ✓)
- [Septentrio mosaic-X5 firmware v4.14 reference guide - ArduSimple](https://www.ardusimple.com/wp-content/uploads/2024/10/mosaic-X5-Firmware-v4.14.10-Reference-Guide.pdf) (E6-B HAS enabled v4.14.0 ✓)
- [Trimble "What's new in firmware 6.28/5.68"](https://help.fieldsystems.trimble.com/r10/whats-new-6.28-5.68.htm) (HAS support added Jan 2025 ✓)
- [u-blox community forum - HAS support for ZED-F9P](https://portal.u-blox.com/s/question/0D52p0000Ck9SToCQM/support-for-galileo-high-accuracy-service-has) (ZED-F9P cannot support E6/HAS ✓)
- [GPS Solutions 2024 - HASlib + RTKLIB integration (Prol et al.)](https://link.springer.com/article/10.1007/s10291-024-01617-7) (sub-20 cm 3D at 1σ after ~10 min ✓)
- [HASlib - GitHub (NLS-FI)](https://github.com/nlsfi/HASlib) (open-source Galileo HAS decoder ✓)
- [HASPPP - GitHub (Wuhan University)](https://github.com/ZhangRunzhi20/HASPPP) (RTKLIB-integrated HAS decoder ~)
- [Quectel Galileo OSNMA/HAS announcement - BusinessWire Oct 2025](https://www.businesswire.com/news/home/20251007212262/en/Quectel-Strengthens-GNSS-Offering-with-RTKHOLD-and-Galileo-OSNMA-and-High-Accuracy-Service-Integration) (LG290P HAS firmware ✓)
- [Eos Arrow Gold+ Galileo HAS press release](https://eos-gnss.com/press-releases/galileo-high-accuracy-service) (first GIS device with HAS ✓)
- [SW Maps manual v3.0 (PDF)](https://aviyaantech.com.np/SwMaps/assets/SW%20Maps%20Manual%20V3.0.pdf) (NTRIP button colour green/orange ✓)
- [ArduSimple - How to use SW Maps](https://www.ardusimple.com/how-to-use-ardusimple-products-with-android-smartphones-tablets/) (Blue/Orange/Green position bubble, HPA < 20 mm at fix ✓)
- [Emlid Flow - NTRIP workflow for Reach RX](https://docs.emlid.com/reachrx/quickstart/ntrip-workflow/) (step-by-step workflow, status widget ✓)
- [Reach RX User Documentation v1.4 - Dimense](https://dimense.fi/site/assets/files/1993/reach_rx_user_documentation.pdf) (LED white/yellow/green for SINGLE/FLOAT/FIX ✓)
- [Emlid community - correction age thresholds](https://community.emlid.com/t/ntrip-age-of-corrections-keeps-exceeding-10s/38120) (5 s warn, 10 s drop-to-standalone ✓)
- [Emlid blog - Reach RX MFi certification July 2024](https://blog.emlid.com/meet-the-new-gen-reach-rx-rtk-rover-now-compatible-with-all-popular-gis-apps-on-ios/) (MFi certification confirmed ✓)
- [ArcGIS Field Maps - high-accuracy data collection](https://doc.arcgis.com/en/field-maps/latest/prepare-maps/high-accuracy-data-collection.htm) (MFi requirement for iOS BT Classic ✓)
- [Eos GNSS - iOS and Bluetooth overview](https://eos-gnss.com/knowledge-base/articles/ios-and-bluetooth-overview) (BLE/MFi/SPP detail ✓)
- [QField GNSS positioning docs](https://docs.qfield.org/how-to/navigation-and-positioning/gnss/) (TCP/UDP only on iOS ✓)
- [Centipede crtk.net migration - 2025-03-18](https://crtk.net) (host migration confirmed ✓)
- [EarthScope NOTA - UNAVCO retirement 2025-07-29](https://www.earthscope.org/data/gnss-realtime/) (legacy UNAVCO URLs dead ✓)
- [ICSM SP7 Geocentric Datum of Australia 2020 Technical Manual](https://www.icsm.gov.au/sites/default/files/GDA2020TechnicalManualV1.2.pdf) (plate velocity 70 mm/yr, ITRF offset ✓)
- [Altamimi et al. 2012 - ETRS89 and EUREF Technical Note 1](https://www.euref.eu/euref_members/library/publication_serien/23-altamimi-zuheir-2012.pdf) (ETRS89 offset from ITRF ~0.9 m at 2025 ✓)
- [Soler & Snay 2004 - NAD83/ITRF transformations - Journal of Surveying Engineering](https://doi.org/10.1061/(ASCE)0733-9453(2004)130:4(174)) (NAD83 Helmert parameters ✓)
- [Pavlis et al. 2012 - EGM2008 - Journal of Geophysical Research](https://doi.org/10.1029/2011JB008916) (geoid undulation range -106 to +85 m ✓)
- [rtk2go - How it works (connection policy)](http://rtk2go.com/how-it-works/) (only active streams in sourcetable; 50k-150k connections/day ✓)
- [ASPRS Accuracy Standards for Digital Geospatial Data 2015](https://www.asprs.org/wp-content/uploads/2015/01/ASPRS_Accuracy_Standards.pdf) (photogrammetry GCP requirements ~)
- [ASCE 38-22 Standard Guideline for Investigating and Documenting Existing Utilities](https://www.asce.org/publications-and-news/asce-bookstore) (utility quality levels QL-A/B/C ~)

- [NovAtel - GNSS Error Sources (Differential GNSS)](https://novatel.com/an-introduction-to-gnss/gnss-error-sources) (UERE budget; multipath not cancelled by DGNSS ✓)
- [Penn State GEOG 862 - User Equivalent Range Error node](https://www.e-education.psu.edu/geog862/node/1713) (HDOP × UERE formula ✓)
- [Penn State GEOG 862 - Multipath node](https://www.e-education.psu.edu/geog862/node/1721) (multipath not correlated between base and rover; not cancelled by differential ✓)
- [IEEE Trans. ITS 2023 - Seamless Accurate Positioning in Deep Urban Area (arXiv:2206.04457)](https://arxiv.org/pdf/2206.04457) (DGNSS horizontal RMS 11.1 m in Seoul urban test; NLOS 7-52 m per satellite ✓)
- [Frontiers Robotics AI 2022 - GNSS NLOS Signal Classification](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.868608/full) (NLOS pseudorange bias "tens or hundreds of metres" ✓)
- [PLOS ONE 2023 - Effects of Nearby Trees on Positional Accuracy of GNSS](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283090) (Trimble: 1-5 m under forest canopy; sub-meter not achievable under dense canopy ✓)
- [MDPI Sensors 2024 - Reduction of Multipath Effect (Pseudorange Acceleration Weight)](https://www.mdpi.com/1424-8220/24/21/6880) (urban DGNSS horizontal error 6.2 m 95th pct; with mitigation ~1.1 m ✓)
- [Interpine Innovation - GPS Accuracy Estimate (EPE): What Is It?](https://interpine.nz/gps-accuracy-estimate-epe-what-is-it/) (EPE is precision not accuracy; half of fixes outside displayed circle ✓)
- [rtklibexplorer - RTKLIB Solution Accuracy](https://rtklibexplorer.wordpress.com/2017/10/13/rtklib-solution-accuracy/) (formal covariance "optimistic"; assumes uncorrelated noise ✓)
- [ScienceDirect 2022 - Unmodeled-Error-Corrected Stochastic Assessment for Standalone GNSS Receiver](https://www.sciencedirect.com/science/article/abs/pii/S0263224122014610) (unmodelled errors, especially multipath, "remain in GNSS measurements"; accuracy estimates "must not be used to infer precise accuracy" ✓)
- [CREWES Research Report 2010 - GPS accuracy part 2: RTK float vs fixed (U. Calgary)](https://www.crewes.org/Documents/ResearchReports/2010/CRR201029.pdf) (float solutions: 1-2 dm convergence; up to 5 m with no way to tell ✓)
- [PMC/MDPI Sensors 2019 - Single-Baseline RTK Using Dual-Frequency Receivers in Smartphones](https://pmc.ncbi.nlm.nih.gov/articles/PMC6806615/) (single-frequency false-fix rate ~15% of epochs ✓)
- [PMC 2023 - Static Positioning Under Tree Canopy Using Low-Cost GNSS](https://pmc.ncbi.nlm.nih.gov/articles/PMC10056071/) (RTK float errors 1-2 m under forest canopy ✓)
- [rtklibexplorer - Variable Ambiguity Resolution Threshold for RTKLIB (2021)](https://rtklibexplorer.wordpress.com/2021/07/22/a-variable-ambiguity-resolution-threshold-for-rtklib/) (RTKLIB default ratio threshold T=3.0; "if too low, false fixes will be common" ✓)
- [Emlid Community Forum - Wrong false fake fix Emlid M2](https://community.emlid.com/t/wrong-false-fake-fix-emlid-m2/27542) (receiver displayed "Fix" with cm accuracy during false fix ✓)
- [Li & Shen 2014 - GNSS ambiguity resolution with controllable failure rate - J. Geodesy (ResearchGate)](https://www.researchgate.net/publication/263006977_GNSS_ambiguity_resolution_with_controllable_failure_rate_for_long_baseline_network_RTK) (false fix displaces position by decimetre or more; 0.01% failure rate achievable ✓)
- [ResearchGate 254250991 - How well does the VRS system perform?](https://www.researchgate.net/publication/254250991_How_well_does_the_Virtual_Reference_Station_VRS_system_of_GPS_base_stations_perform_in_comparison_to_conventional_RTK) (51 mm height error 10.5 km outside network hull ✓)
- [IEEE 5069258 - Practical accuracy of VRS RTK outside MyRTKnet](https://ieeexplore.ieee.org/document/5069258/) (horizontal ~6 cm; vertical up to several metres 30 km outside hull ✓)
- [Springer J. Geodesy 2005 - Long-range network RTK during severe ionospheric storm (doi:10.1007/s00190-005-0003-y)](https://link.springer.com/article/10.1007/s00190-005-0003-y) (IAR rate 94%→31%; decimeter horizontal errors inside network during storm ✓)
- [GPS Solutions 2023 - Tropospheric model for large height-difference RTK (doi:10.1007/s10291-023-01481-x)](https://link.springer.com/article/10.1007/s10291-023-01481-x) (~27 cm height error per 1000 m elevation difference without vertical tropo model ✓)
- [ResearchGate 228734118 - Network RTK performance analysis using RTCM 3.0 (Southern Alberta)](https://www.researchgate.net/publication/228734118_Network_real-time_kinematic_performance_analysis_using_RTCM_30_and_the_Southern_Alberta_Network) (recommends adding network ambiguity resolution status flag to RTCM; not yet standardised ✓)
- [FIG Article Sep 2016 - Choy et al. PPP signal interruption and re-convergence](https://www.fig.net/resources/monthly_articles/2016/september_2016/Suelynn_etal_september_2016.pdf) (full-sky blockage: re-convergence "regularly exceeds 30 min" ✓)
- [ResearchGate 289224452 - Rapid re-convergence in real-time PPP with AR (Banville & Langley)](https://www.researchgate.net/publication/289224452_Rapid_re-convergence_in_real-time_precise_point_positioning_with_ambiguity_resolution) (PPP-AR: ~1-epoch recovery with integer cycle-slip fix ✓)
- [NovAtel Velocity 2014 - PPP signal interruption and re-convergence](https://www.novatel.com/tech-talk/velocity/velocity-2014/advanced-gnss-positioning-solutions-with-precise-point-positioning-ppp/convergence-performance) (atmospheric state bridging over short gaps; PPP_CONVERGING vs PPP status ✓)
- [Eos GNSS blog 2023 - Galileo HAS Early Observations](https://eos-gnss.com/blog/galileo-high-accuracy-service-early-observations) (HAS Phase 1 convergence 5-30 min; "about 30 min to 20 cm level" ✓)
- [Inside GNSS Feb 2024 - Galileo HAS urban driving assessment](https://insidegnss.com/galileo-has-a-performance-assessment-in-urban-driving-environments/) (urban: only marginal improvement over broadcast due to constant re-convergence ✓)
- [ENC 2025 - Galileo HAS accuracy and convergence performance results](https://enc-series.org/wp-content/uploads/2025/05/Sciforum-095088-commercial-formatted.pdf) (HAS Phase 1 float-only; phase bias products absent ✓)

- [IGS antenna calibration - antex14 format definition](https://files.igs.org/pub/data/format/antex14.txt) (ANTEX field structure; PCO/PCV per-frequency tables ✓)
- [NGS Antenna Calibration Programme - NOAA NGS](https://geodesy.noaa.gov/ANTCAL/) (US authority; published ANTEX files for major geodetic antennas ✓)
- [IGS antenna naming convention rcvr_ant.tab](https://files.igs.org/pub/station/general/rcvr_ant.tab) (16-char antenna + 4-char radome convention ✓)
- [Times Microwave LMR cable attenuation reference](https://www.timesmicrowave.com/calculator/) (RG-174/RG-58/LMR-240/LMR-400 loss at 1.5 GHz ~)
- [EASA SIB 2022-02R3 - GNSS Outages and Alterations](https://ad.easa.europa.eu/ad/2022-02R3) (Baltic and Black Sea regional GNSS denial documented for civil aviation ✓)
- [OPSGROUP GPS Spoofing Working Group](https://ops.group/blog/gps-spoofing-working-group/) (multi-region 2023-2025 spoofing event database; airport-decoy patterns ✓)
- [IATA - GNSS interference industry stance](https://www.iata.org/en/programs/ops-infra/navigation/) (airline operational risk from spoofing; the specific Sep 2024 position paper is not directly linkable from a public landing page - claim is widely covered in trade press but the precise document URL is unverified) ~
- [gpsjam.org - Daily maps of GPS interference](https://gpsjam.org/about) (ADS-B NIC/NACp degradation as GNSS-interference proxy; methodology page ✓)
- [Galileo OSNMA Service Definition Document - GSC](https://www.gsc-europa.eu/sites/default/files/sites/all/files/Galileo_OSNMA_SDD_v1.1.pdf) (navigation-message authentication; signal-level replay not detected ✓)
- [u-blox F9 HPG 1.50 Interface Description (UBX-22010984)](https://content.u-blox.com/sites/default/files/documents/u-blox-F9-HPG-1.50_InterfaceDescription_UBX-22010984.pdf) (authoritative source for OSNMA support in HPG 1.50 firmware ✓)
- [ITU complaints on North Korean GPS jamming - Republic of Korea filings](https://www.itu.int/en/ITU-R/space/Pages/news.aspx) (2010, 2011, 2012, 2016 events ✓)
- [RTKLIB-Explorer (demo5 fork) - GitHub](https://github.com/rtklibexplorer/RTKLIB) (actively maintained PPK fork; F9P-class config presets ✓)
- [Emlid Studio - Reach raw-log post-processing](https://emlid.com/studio/) (free desktop PPK; native Reach UBX ingest ✓)
- [Reach RS3 launch - Emlid](https://blog.emlid.com/meet-the-new-reach-rs3-survey-grade-rtk-rover-with-tilt-compensation/) (sub-$3k tilt rover; magnetometer-free heading ✓)
- [Leica GS18 T product page](https://leica-geosystems.com/products/gnss-systems/smart-antennas/leica-gs18-t) (Leica's product overview; magnetic-immune tilt and pole-tip workflow are described at marketing-summary level; the underlying white papers are linked from the page) ~
- [Trimble R12i datasheet - TIP Inertial Platform](https://geospatial.trimble.com/products-and-solutions/r12i) (60° pole tilt advertised; magnetic-free heading ✓)
- [u-blox ZED-F9R product summary](https://www.u-blox.com/en/product/zed-f9r-module) (UDR/ADR for vehicles; not survey tilt compensation ✓)
- [EarthScope NULA - Network Use Licence Agreement](https://www.earthscope.org/data/data-policy/) (annual acceptance; non-commercial only; citation required ✓)
- [Centipede community licence and contribution rules](https://docs.centipede.fr/) (community-share-alike intent; per-node operator discretion ~)
- [LINZ - PositioNZ data licensing terms](https://www.linz.govt.nz/data/linz-data/use-and-share-data) (CC BY 4.0 NZ ✓)
- [Geoscience Australia - AUSCORS NTRIP portal](https://gnss.ga.gov.au/) (operational entry point; the specific CC BY 4.0 + additional-ToS terms are described on Geoscience Australia's general copyright page ~)
- [SAPOS - Free use vs paid commercial tier overview](https://sapos.de/) (per-state landesvermessungsamt portals; Bavaria €20/yr non-ag ✓)
- [IGS Products - Orbit/clock latency tiers](https://igs.org/products/) (ultra-rapid predicted/observed, rapid, final accuracy ladder; Final clock ~20 ps ✓)
- [Galileo HAS Phase 2 roadmap - GSC service definition](https://www.gsc-europa.eu/galileo/services/galileo-high-accuracy-service-has) (HAS Phase 2 includes phase bias products; not yet committed ~)
- [QZSS CLAS Interface Specification IS-QZSS-L6-001 - Cabinet Office Japan](https://qzss.go.jp/en/technical/ps-is-qzss/ps-is-qzss.html#is-qzss-l6) (CLAS PPP-AR convergence target <60 s; the document index page links to the L6 spec PDF ~)
- [BeiDou PPP-B2b service](http://en.beidou.gov.cn/SYSTEMS/Officialdocument/) (B2b PPP-RTK service definition ~)
- [Trimble RTX positioning service](https://positioningservices.trimble.com/services/rtx/) (CenterPoint RTX/RTX FAST convergence specs ✓)
- [u-blox PointPerfect SPARTN service](https://www.u-blox.com/en/product/pointperfect) (SPARTN PPP-RTK; <1 min convergence with NEO-D9S ✓)
- [Swift Skylark precise positioning](https://www.swiftnav.com/precise-positioning-service) (Skylark PPP-RTK service specs ✓)
- [SNIP knowledge base - RTCM 3 MSM message structure detail](https://www.use-snip.com/kb/knowledge-base/an-rtcm-3-message-cheat-sheet/) (header, satellite/signal/cell mask layout ✓)
- [Tersus GNSS - RTCM3 MSM detailed reference](https://www.tersus-gnss.com/tech_blog/new-additions-in-rtcm3-and-What-is-msm) (MSM cell-mask sparse-matrix structure ✓)
- [VRS vs MAC principles - Janssen 2009 IGNSS](https://www.spatial.nsw.gov.au/__data/assets/pdf_file/0003/129414/2009_Janssen_IGNSS2009_VRS_vs_MAC.pdf) (RTCM MAC message types 1014-1017; rover-side network reconstruction ✓)
- [u-blox F9 Interface Description - UBX-CFG-VALSET layer flags + CFG-NAV5 + CFG-TMODE3](https://content.u-blox.com/sites/default/files/documents/u-blox-F9-HPG-1.50_InterfaceDescription_UBX-22010984.pdf) (authoritative source for RAM/BBR/FLASH layer persistence, CFG-NAV5 dynModel values 0/2/4/6-8, and CFG-TMODE-MODE survey-in vs fixed ✓)
- [Geoscience Australia - AUSPOS processing methodology](https://gnss.ga.gov.au/auspos) (Bernese-based double-difference network solution against IGS/APREF; not PPP-AR ~)
- [NMEA 0183 talker IDs - multi-constellation receivers emit GN prefix](https://gpsd.gitlab.io/gpsd/NMEA.html) (`GNGGA` for combined GPS+GLONASS+Galileo; `GPGGA` GPS-only ✓)
- [rtklibexplorer - L1-only RTK feasibility](https://rtklibexplorer.wordpress.com/2017/04/26/rtklib-and-low-cost-l1-receivers/) (M8N + RTKLIB short-baseline single-frequency RTK ✓)
- [Galileo NeQuick ionospheric model - ESA](https://www.gsc-europa.eu/sites/default/files/sites/all/files/Galileo_Ionospheric_Model.pdf) (NeQuick correction efficiency vs Klobuchar ~)
