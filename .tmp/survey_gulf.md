# Free RTK survey — Gulf states: Qatar, Kuwait, Bahrain, Oman, Yemen

_Research date: 2026-04-21. All findings based on local data (sourcetables,
`docs/networks.md`, `data/stations.json`) plus training-data knowledge up to
Aug 2025. No live network fetches performed._

---

## QA — Qatar

- **Free government RTK**: None confirmed with a public NTRIP endpoint.
  Qatar's national geodetic infrastructure is managed by the Ministry of
  Municipality (formerly Ministry of Municipality and Environment), which
  operates a network of CORS tied to the Qatar National Spatial Reference
  System (QNSRS / QND95). The network is used internally by licensed
  surveyors and contractors on government projects. No public caster URL
  or hobbyist access path has been identified; access appears to require
  a government-issue survey licence. Geoid model QG2010 is distributed
  separately via the ministry portal.
- **Volunteer**: none. Zero rtk2go or Centipede stations with country code
  `QAT` in local sourcetables.
- **Paid / commercial**: Trimble VRS Now and Hexagon SmartNet each cover
  the GCC as an add-on region; pricing not publicly listed for Qatar alone.
- **Gap**: no free NTRIP path for hobbyists or small shops. Qatar is a
  small country (~11,600 km²); a single reference station at Doha would
  theoretically cover the whole territory, but no such public stream exists.

---

## KW — Kuwait

- **Free government RTK**: None confirmed with a public NTRIP endpoint.
  The Public Authority for Civil Information (PACI) and the Kuwait
  Municipality operate GNSS reference stations primarily for cadastral and
  infrastructure use. A small national CORS network (sometimes referenced
  under the Kuwait Geodetic Network or KGN) exists but is not publicly
  accessible — streams are issued only to licensed surveying firms under
  contract with the municipality. No public caster host:port identified.
- **Volunteer**: none. Zero rtk2go or Centipede stations with country code
  `KWT` in local sourcetables.
- **Paid / commercial**: regional GCC commercial VRS services (Trimble, Hexagon)
  technically cover Kuwait but are not specifically marketed for hobbyist use.
- **Gap**: no free NTRIP path. Kuwait is small (~17,800 km²) and flat;
  a modest CORS network would suffice for national RTK coverage if opened,
  but no open-access mandate exists.

---

## BH — Bahrain

- **Free government RTK**: None confirmed with a public NTRIP endpoint.
  The Survey and Land Registration Bureau (SLRB) under the Ministry of
  Justice, Islamic Affairs and Awqaf manages geodetic infrastructure and
  operates a small number of CORS, tied to the Bahrain Geodetic Datum 2000
  (BGD2000). Bahrain's entire territory is ~765 km² — smaller than many
  individual city CORS deployments elsewhere. No public NTRIP caster has
  been identified; access appears restricted to licensed surveyors.
- **Volunteer**: none. Zero rtk2go or Centipede stations with country code
  `BHR` in local sourcetables.
- **Paid / commercial**: regional commercial VRS may offer partial coverage
  from neighbouring Saudi Arabia (KSA-CORS reaches ~50 km into Bahrain
  given its proximity to Dammam and Al-Ahsa stations, though that service
  is Saudi-licensed and VRS-only). → networks.md: `ksa_cors`
- **Gap**: no free NTRIP path. At Bahrain's scale, a single reference
  station would cover the whole island; the practical barrier is policy,
  not infrastructure cost.

---

## OM — Oman

- **Free government RTK**: None confirmed with a public NTRIP endpoint.
  The National Centre for Statistics and Information (NCSI), formerly in
  collaboration with the Ministry of Housing and Urban Planning, has built
  out the National Accurate Geodetic Survey Network (NAGSN) — a network of
  CORS supporting the Oman National Geodetic Datum (ONGD14) and geoid model
  OmG2016. NAGSN is operationally managed by the National Survey Authority.
  Streams are issued to licensed surveying companies via a formal application
  process; no public NTRIP caster URL has been identified for hobbyist or
  small-shop use. IGS-affiliated stations at Muscat (MUSK) broadcast raw
  GNSS observations through EarthScope and IGS-IP, but those are not RTK
  streams. Oman's land area is large (~309,500 km²) and mountainous (Al
  Hajar range), so baseline distances from any sparse network are
  significant.
- **Volunteer**: none. Zero rtk2go or Centipede stations with country code
  `OMN` in local sourcetables.
- **Paid / commercial**: no GCC commercial VRS is confirmed to offer Oman
  coverage in hobbyist pricing tiers.
- **Gap**: no free NTRIP path. Oman's size and topography mean useful
  national coverage would require ~20–30 stations; NAGSN appears to exist
  at that scale but remains closed to public access.

---

## YE — Yemen

- **Free government RTK**: None. Yemen's geodetic agency (General Authority
  for Survey, GAS — known also as the General Survey Authority) operated a
  small CORS network pre-conflict, but civil war since 2015 has severely
  disrupted all public infrastructure. GAS facilities in Sanaa have been
  damaged or displaced; no functioning public NTRIP caster is known.
- **Volunteer**: rtk2go has **1 base station** in Yemen: `s9123A22404`
  located in Sanaa (15.29°N, 44.24°E), broadcasting RTCM 3.2
  (messages 1005, 1008, 1033, 1074, 1124 — GPS + BDS dual-frequency,
  no GLONASS). No Centipede stations with country code `YEM`. This
  single station appears to be an independent hobbyist installation.
  Connectivity and uptime are unreliable given ongoing conflict.
- **Gap**: effectively no RTK coverage for hobbyists. The single
  rtk2go station provides a ~50–70 km useful radius under good conditions
  but cannot be relied upon. The conflict context means recommending RTK
  activity in Yemen is not appropriate; note for map completeness only.

---

## Summary table

| Country | ISO2 | Free gov NTRIP | Volunteer | Practical path |
|---------|------|----------------|-----------|----------------|
| Qatar   | QA   | None           | 0         | None           |
| Kuwait  | KW   | None           | 0         | None           |
| Bahrain | BH   | None           | 0         | None (KSA-CORS spill may reach ~50 km) |
| Oman    | OM   | None (NAGSN closed) | 0   | None           |
| Yemen   | YE   | None (conflict) | 1 rtk2go (Sanaa) | 1 unreliable volunteer base |

---

## Notes for country-survey.md integration

These five countries share a common pattern: government CORS networks
exist but are restricted to licensed surveyors; no open-data GNSS mandate;
no volunteer ecosystem. Recommended section heading placement:

- QA, KW, BH, OM: add under **Middle East & Africa**, alongside existing
  AE (UAE), SA (Saudi Arabia), IQ (Iraq), IR (Iran) entries.
- YE: add under **Middle East & Africa**, before or after IQ.

For YE, the single rtk2go station (`s9123A22404`, Sanaa) is already
captured in the pipeline via the global rtk2go source — no new ingestion
needed. The country entry should note the conflict context and that
the volunteer pin appears in the map automatically via rtk2go.

For all five, `docs/networks.md` entries are not needed (no candidate
or deferred networks to track) unless a future session finds a public
NTRIP endpoint.
