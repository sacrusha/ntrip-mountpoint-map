# Israel [IL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-12 entry; APN/mapigps.co.il + Survey of Israel govil portal both ECONNREFUSED from sandbox 2026-05-17 — geo-block pattern unchanged; spoofing environment unchanged)

## Status: YES (nominally) — APN caster is live; rejected from pipeline due to pervasive military GNSS spoofing making RTK unreliable

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — APN (`mapigps.co.il`) is operational |
| **host:port** | `mapigps.co.il` (port not published; conventionally 2101; Geo++ Nt caster). Direct TCP probe from sandbox timed out 2026-05-12; WebFetch returned ECONNREFUSED 2026-05-17 — consistent geo-block pattern (caster accessible inside IL but not from many external networks). |
| **network type** | VRS — virtual reference station; powered by Geo++ Nt software |
| **tariff** | not publicly listed; believed free for licensed Israeli surveyors; contact apn@mapi.gov.il / 03-6231697 |
| **hobbyist_eligibility** | Unclear — primary user base is licensed surveyors registered with Survey of Israel (MAPI); no documented open self-service sign-up path for non-licensed users |
| **legal_residency_required** | Unclear — registration appears tied to Israeli surveyor licensing; foreign hobbyists have no documented access path |
| **last_confirmed_alive** | APN/mapigps.co.il caster: WebFetch ECONNREFUSED 2026-05-17 (sandbox geo-block consistent with prior — caster was HTTP 200 on 2026-05-06 from a different vantage); service continuously referenced in academic/professional literature through 2025. ArduSimple Israel page (docs/ardusimple/IL_Israel.md 2026-05-16) lists Israel Mapping Center as paid national service (registration auth-required from external vantage). Centipede has 1 IL station (ARKG, 32.65,35.29 — Golan); rtk2go has 1 IL station (misgav_dov, 31.81,34.74 — Shfela); igs_ip carries BSHM00ISR0 (Haifa, 32.78,35.02) |
| **pipeline status** | REJECTED — pervasive military GNSS spoofing active since Oct 2023 renders RTK unreliable regardless of NTRIP access |
| **datum_epoch** | omitted — no citable operator declaration. `mapigps.co.il` unreachable from sandbox; ArduSimple landing URL points at `gov.il/he/departments/survey_of_israel/govil-landing-page` (auth-required). Israeli national grid is ITM/IG05 but no operator real-time-service datum statement obtainable |

## Spoofing Environment — Critical Context

Israel has been operating military GPS/GNSS spoofing continuously since October 2023 as a defensive electronic warfare measure against missile and drone threats. The spoofing does not affect RTK correction data delivery via NTRIP, but it corrupts the raw satellite observables that RTK receivers depend on — making a valid RTK fix impossible or unreliable across Israel and an extended region.

**Geographic extent of disruption (as of 2026-05-06):**
- Core affected area: Israel, Lebanon, the Sinai Peninsula, Cyprus, and parts of Jordan and southern Syria
- Extended disruption during active conflict: The June 2025 "Twelve-Day War" (IDF strikes on Iranian nuclear and military facilities, 13–24 June 2025) caused a major surge in GNSS jamming and spoofing across the broader Middle East and Persian Gulf
- An estimated 50,000+ commercial aviation flights were affected by GNSS disruption in 2024; maritime disruption in Q2 2025 exceeded 10,000 vessel reports

**Why NTRIP cannot compensate for spoofing:** RTK corrections supplied via NTRIP correct for atmospheric and orbital errors in the satellite signals; they cannot correct for false carrier-phase observables introduced by a spoofing transmitter. A receiver locked to a spoofed signal will compute a false position regardless of the correction stream being used.

## APN Network Details

- **Operator**: Survey of Israel (MAPI — המרכז למיפוי ישראל), under Israel's Ministry of Housing and Construction
- **Software**: Geo++ Nt CORS system (confirmed by mapigps.co.il splash page attribution)
- **Station network**: The SOI-APN network has ~30–35 permanent GNSS reference stations distributed across Israel; ResearchGate figures show coverage spanning from Eilat (south) to the Golan Heights (north)
- **Service type**: VRS — virtual reference station corrections generated from the network of physical bases; user connects and receives corrections for a virtual station near their location
- **Correction format**: RTCM; RINEX data also available for post-processing
- **Contact**: apn@mapi.gov.il · phone 03-6231697

## Commercial NTRIP Alternatives

No commercial or volunteer NTRIP network with confirmed Israel coverage and foreign-hobbyist eligibility has been identified:
- No Israeli commercial NTRIP caster (beyond APN) is listed on NTRIP-list.com or ArduSimple's Israel page
- GEODNET, PointOne, RTKdata: no confirmed Israel production coverage found
- The spoofing environment makes any commercial offering equally unreliable in practice

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **APN / mapigps.co.il** — RINEX data download from SOI reference stations | https://mapigps.co.il/ | Likely free for registered users; registration requirements unclear for non-licensed foreign users |
| **EarthScope / IGS** — TELA (Tel Aviv) IGS station RINEX archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **EUREF Permanent Network (EPN)** — TELA and RAMO (Ramon crater) EPN stations | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- Survey of Israel CORS site (Geo++ Nt): https://mapigps.co.il/
- ArduSimple RTK correction services Israel: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-israel/
- Survey of Israel (MAPI) administration: https://www.mapi.gov.il/en/Heritage/Pages/ministration1-and-Services-of-the-Survey-Department--Survey-of-Israel.aspx
- Israel's SOI-APN GPS network (ResearchGate diagram): https://www.researchgate.net/figure/Israels-SOI-APN-GPS-network-The-network-is-maintained-by-the-Survey-of-Israel-MAPI_fig1_328049994
- "The Permanent GNSS Network and its RTK Application in Israel" (FIG 2009): https://www.fig.net/resources/proceedings/fig_proceedings/fig2009/papers/ts01c/ts01c_salmon_3248.pdf
- GPS World — electronic warfare and GNSS spoofing by Israel: https://www.gpsworld.com/electronic-warfare-takes-centerstage-with-gnss-spoofing-by-israel/
- GPS World — GPS jamming in Israel: https://www.gpsworld.com/gps-jamming-in-israel/
- Steptoe — GPS Jamming during Israel-Iran War: https://www.steptoe.com/en/news-publications/stepwise-risk-outlook/gps-jamming-during-israel-iran-war-demonstrates-risks-to-civilian-operations.html
- Wikipedia — Twelve-Day War: https://en.wikipedia.org/wiki/Twelve-Day_War
- CNN — GPS jamming and the Iran war (2026-03-06): https://www.cnn.com/2026/03/06/science/gps-jamming-ships-planes-iran-war
- GPSJAM interference map: https://gpsjam.org/
- country-survey.md IL stub (2026-04-29)
- networks.md `apn` entry (status: weird)
- Centipede IL stations: 1 (ARKG, Golan area) — 2026-05-17 pipeline snapshot via `scripts/stations_by_country.py ISR`
- rtk2go IL stations: 1 (misgav_dov, Shfela area) — 2026-05-17 pipeline snapshot
- igs_ip IL stations: 1 (BSHM00ISR0, Haifa Technion) — 2026-05-17 pipeline snapshot
- ArduSimple Israel cache (docs/ardusimple/IL_Israel.md 2026-05-16): lists Israel Mapping Center as paid national service via gov.il landing page
- GPS World — GPS disruptions in Tel Aviv (2025): https://www.gpsworld.com/gps-disruptions-in-tel-aviv-as-israel-braces-for-possible-iranian-attacks/
- Times of Israel — Israel's GPS warfare: https://www.timesofisrael.com/israels-gps-warfare-aims-to-keep-its-own-drones-flying-and-enemies-baffled/
- Middle East Monitor — Israel as source of GPS disruption: https://www.middleeastmonitor.com/20240704-israel-identified-as-source-of-gps-disruption-across-the-middle-east/
