# Oman [OM] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

One nationwide government NRTK network — OmanCORSnet (NSGIA, 46 CORS
sites, expanding past 60), Leica GNSS Spider caster on
`omancorsnet.gov.om:2101` with an open sourcetable (8 mountpoints,
2026-05-23). Streaming requires credentials issued via the Spider
Business Center after registration. ArduSimple categorises it as a free
national service "Recommended for any type of work in Oman"; NSGIA
itself does not publish a tariff. No explicit hobbyist tier, but no
licensed-surveyor-only clause has been retrieved either; gating is the
SBC registration approval.

No rtk2go / Centipede / EarthScope / IGS-IP stations in Oman 2026-05-23.
Cross-border / global fallback: Galileo HAS (free PPP, no caster
connectivity, ~20–40 cm converged).

## Casters

### OmanCORSnet — Oman Continuously Operating Reference Stations Network

- operator: NSGIA — National Survey and Geospatial Information Authority
  (successor to NSA, National Survey Authority, under Ministry of Defence)
- landing_url: https://www.nsaomangeoportal.gov.om/en/oman-corsnet
  (NSGIA geoportal OmanCORSnet page; WebFetch returned 502 from sandbox
  2026-05-23 — content corroborated via WebSearch snippets and the
  FIG 2024 paper)
- access_url: https://www.omancorsnet.gov.om/SBC/Account/Register
  (Spider Business Center registration; identified by ArduSimple
  2026-05-23 as the registration entry point)
- access_type: free-signup — ArduSimple Oman page (WebFetch 200
  2026-05-23) categorises OmanCORSnet as a "Free national service" and
  notes *"register on the website or send them an email"*. NSGIA itself
  publishes no tariff and the SBC pricing surface (if any) is only
  visible post-approval — `free-signup` rests on ArduSimple's editorial
  characterisation, not an NSGIA declaration, and could in principle
  resolve to paid after login. No reports of charges encountered in
  practice 2026-05-23.
- coverage: full Sultanate of Oman (~309,500 km²); Leica GNSS Spider
  network-RTK output (VRS / MAX / Nearest) is operationally available
  across populated areas
- num_stations: 46 (NSGIA / OmanCORSnet, established 2016; FIG 2024
  paper *"A New Reference Frame for Oman"* uses the OmanCORSnet set
  through end-2022 and cites 46 stations). The NSGIA page describes a
  plan to expand beyond 60 — 60 is a planning figure, 46 is the
  operational figure documented in the FIG 2024 abstract.
- hobbyist_eligibility: ? — ArduSimple notes "The registration process
  is not always very user-friendly, so it might take some effort"; no
  explicit licensed-surveyor restriction is published, but no clear
  hobbyist tier either (checked: ArduSimple Oman page 2026-05-23
  WebFetch; nsaomangeoportal.gov.om OmanCORSnet page 2026-05-23 (502);
  FIG 2024 paper 2026-05-23 WebFetch)
- residency_required: ? — no explicit restriction found on the NSGIA
  page or the ArduSimple cross-reference; non-resident eligibility
  unconfirmed (checked: ArduSimple Oman 2026-05-23 WebFetch;
  nsaomangeoportal.gov.om 2026-05-23 (502); GIM International "Oman
  Launches New Geodetic Datum" 2026-05-23 via WebSearch)
- sourcetable: `omancorsnet.gov.om:2101` — direct TCP probe 2026-05-23
  returned `SOURCETABLE 200 OK`, server `GNSS Spider 7.11.1.109/1.0`,
  8 mountpoints, total 778 bytes:
  - `Nearest` (single-base routing, RTCM 3, GPS+GLO, nmea=1, solution=0)
  - `MAX` (Master-Auxiliary / iMAX NRTK, GPS+GLO, nmea=1, solution=1)
  - `VRS` (Virtual Reference Station, GPS+GLO, nmea=1, solution=1)
  - `UTM-40-Auto-Geoid`, `UTM-39-Auto-Geoid` (UTM 40N / 39N projected
    NRTK with geoid applied)
  - `MAX-Geoid-39`, `MAX-Geoid-40` (NRTK with geoid in UTM 39N / 40N)
  - `ONGD23` (native ONGD23 datum stream)

  Constellations in the public sourcetable are GPS+GLO only;
  Galileo/BeiDou are not exposed externally. Unusual for a Leica
  GNSS Spider 7.11 caster — could be a deliberate broadcast-policy
  choice, a sourcetable-filter configuration, or limitations on some
  station receivers. Neither the NSGIA OmanCORSnet page nor the FIG
  2024 paper documents multi-constellation policy (checked: NSGIA
  page 2026-05-23 WebFetch 502; FIG 2024 abstract 2026-05-23 WebFetch
  — does not address constellation broadcast). Authentication required
  to actually pull RTCM bytes.
- vrs: yes — confirmed in the live sourcetable (mounts `VRS`, `MAX`,
  `Nearest`); Leica GNSS Spider platform
- stations_source: sourcetable advertises only routing mountpoints (no
  per-station mounts); the NSGIA OmanCORSnet page is the canonical
  station list (sandbox cannot read it 2026-05-23, only WebSearch
  excerpts available). FIG 2024 paper lists 46 sites with positions and
  velocities for the ONGD23 frame.
- datum_epoch: ONGD23 — Oman National Geodetic Datum 2023, **ITRF2020 at
  epoch 2023.0**, derived from OmanCORSnet long-term processing through
  end-2022 (Al Balushi et al., FIG 2024 *"A New Reference Frame for
  Oman, Derived by Precise Processing of the CORS"*,
  https://www.fig.net/resources/proceedings/fig_proceedings/fig2024/papers/ts08f/TS08F_al_balushi_abolghasem_et_al_12396_abs.pdf;
  WebFetch 200 2026-05-23). The FIG abstract states: *"application of
  rotations and rotation rates to ITRF20, so that the velocity of Oman
  block is minimized"* with positions at epoch 2023.0. The sourcetable
  mountpoint `ONGD23` confirms the operator broadcasts this frame
  natively. The previous ONGD17 (ITRF2014 @ 2017.0) remains documented
  on the NSGIA ONGD17 page but is being superseded operationally.

NSGIA brand evolution: NSA (National Survey Authority) → NSGIA
(National Survey and Geospatial Information Authority); geoportal at
`nsaomangeoportal.gov.om`. The Oman geoid model is OMANGEOID, part of
the Oman National Spatial Reference System alongside OmanCORSnet and
ONGD23.

### IGS / EarthScope — no Oman station

No Muscat IGS station appears in `data/igs_ip.sourcetable` 2026-05-23
under codes MUSC / MUSK / OMAN / MUSCT. Prior research mentioned a
Muscat IGS site as a RINEX/raw observation source; not currently
exposed as a real-time NTRIP stream from any tracked IGS rebroadcaster.

## Disqualified / not applicable

- **rtk2go** — 0 OM mountpoints 2026-05-23
  (`py scripts/stations_by_country.py OMN` → "No stations for 'OMN'").
- **Centipede, EarthScope NOTA, IGS-IP** — 0 OM-coded stations 2026-05-23.
- **GEODNET, onocoy, PointOne, HxGN SmartNet, Trimble VRS Now** — no
  Oman coverage advertised in public documentation 2026-05-23.
- **"NAGSN"** acronym used in older project notes does not appear in
  current NSGIA documentation; the official name is OmanCORSnet.

## Post-Processing (RINEX) fallback

| Service | URL | Notes |
|---|---|---|
| OmanCORSnet RINEX (via the same SBC portal) | https://omancorsnet.gov.om/ | Registration required; fee unknown |
| NSGIA Geoportal — OmanCORSnet page | https://www.nsaomangeoportal.gov.om/en/oman-corsnet | Information page |
| IGS / EarthScope | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; no Muscat real-time NTRIP stream in tracked rebroadcasters 2026-05-23 |

## Sources Consulted

- NSGIA OmanCORSnet page (WebFetch 502 from sandbox 2026-05-23;
  content reproducible via WebSearch snippet, ArduSimple cross-ref,
  and FIG 2024 paper):
  https://www.nsaomangeoportal.gov.om/en/oman-corsnet
- NSGIA About page: https://www.nsaomangeoportal.gov.om/en/about-nsa
- NSGIA ONGD17 page (legacy datum):
  https://www.nsaomangeoportal.gov.om/en/ongd17
- NSGIA Oman Geospatial Manual:
  https://www.nsaomangeoportal.gov.om/en/oman-geospatial-manual
- OmanCORSnet Spider Business Center login:
  https://www.omancorsnet.gov.om/SBC/Account/Index?returnUrl=/SBC
- OmanCORSnet SBC registration: https://www.omancorsnet.gov.om/SBC/Account/Register
- FIG 2024 — "A New Reference Frame for Oman, Derived by Precise
  Processing of the CORS" (Al Balushi, Abolghasem et al.):
  https://www.fig.net/resources/proceedings/fig_proceedings/fig2024/papers/ts08f/TS08F_al_balushi_abolghasem_et_al_12396_abs.pdf
  (and full paper TS08F_…_12396.pdf)
- Oman Geospatial Forum — Latest Geospatial Infrastructure in Oman:
  http://omangeospatialforum.org/presentation/latest-geospatial-infrastructure-in-Oman-national-development-benefits.pdf
- GIM International — Oman Launches New Geodetic Datum (ONGD17 era):
  https://www.gim-international.com/content/article/oman-launches-new-geodetic-datum
- Geospatial World — Oman Moves Ahead with New Geodetic Datum:
  https://geospatialworld.net/article/oman-moves-ahead-with-new-geodetic-datum/
- ArduSimple Oman NTRIP page (WebFetch 200 2026-05-23 — confirms free
  national service, SBC registration, recommended for any work in Oman):
  https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-oman/
- Direct TCP probe 2026-05-23 of `omancorsnet.gov.om:2101` →
  `SOURCETABLE 200 OK`, server `GNSS Spider 7.11.1.109/1.0`, 8
  mountpoints unchanged from prior pass.
- Local data 2026-05-23: `py scripts/stations_by_country.py OMN` →
  no stations on any tracked source.
