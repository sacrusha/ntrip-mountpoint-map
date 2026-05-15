# North Macedonia [MK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-12)

## Status: YES — MAKPOS national RTK network active; quasi-geoid (height) corrections live since Feb 2026; registration required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — MAKPOS (Macedonian Positioning System), operated by the Agency for Real Estate Cadastre (AREC) |
| **landing_url** | `https://makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx` — operator-owned MAKPOS SpiderWeb portal landing. Alternative: `https://www.katastar.gov.mk/en/data/services/` (AREC agency services overview including MAKPOS). |
| **access_url** | Skip — pricing/tariff is not published in open web; access is via the SBC portal. The SBC entry at `https://makpos.katastar.gov.mk/sbc/Account/Register` is a bare registration form, not a service description page. |
| **host:port** | makpos.katastar.gov.mk : 9001 |
| **Sample mountpoint** | `iMAX-GNSS` — iMAX-style network RTK, GPS+GLONASS+Galileo (per ArduSimple / community reporting) |
| **tariff** | Subscription required; specific MKD amounts not publicly posted. MAKPOS users with compatible GNSS devices on 3G/GPRS reportedly offered free-of-charge access per one source — unclear if still current. Contact AREC to confirm. |
| **hobbyist_eligibility** | Unclear — registration via Spider Business Center portal (makpos.katastar.gov.mk/sbc/); individual sign-up appears available |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | makpos.katastar.gov.mk SBC login portal confirmed live (2026-05-06). Note: Alberding worldwide-datastreams probe of port 9001 on 2026-05-12 returned "Caster not available" — could indicate transient outage or that the public sourcetable is no longer exposed to Alberding's probe. Service announcements as recent as Feb 2026 confirm the network is operational. |

## Most Recent Project Announcement

**2026-02-23 — First official quasi-geoid model MK_HREF2022 deployed**: AREC put the new hybrid quasi-geoid into operation by Government Decision of 25 November 2025. The MK_HREF2022 model ("Macedonian Height Reference Surface 2022") was produced by AREC with the Norwegian Mapping Authority (Kartverket) and verified by Lantmäteriet (Sweden), based on 2,470 gravimetric points (all NVT3 benchmarks plus a 5×5 km grid). **The quasi-geoid is integrated into MAKPOS — RTK clients now receive both position AND height (grid + quasi-geoid) corrections in real time**, plus a desktop coordinate-transformation app for registered users. Source: https://www.katastar.gov.mk/en/2026/02/23/the-first-official-quasi-geoid-model-has-been-put-into-use-for-the-territory-of-the-republic-of-north-macedonia/

**2020-04-08 — Galileo upgrade**: MAKPOS upgraded for Galileo multi-constellation support (AREC announcement: https://www.katastar.gov.mk/en/2020/04/08/makpos-system-upgraded-for-galileo-functionalities/).

The system consists of 14 reference base stations positioned 50–70 km apart, a control center using Leica GNSS Spider software (RT Proxi Server + NTRIP Caster), and a web portal at makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx.

Services offered:
- **DGPS**: 0.3–0.5 m accuracy, RTCM 2.x, via GPRS + NTRIP
- **RTK**: 0.02–0.04 m accuracy, RTCM 2.x and RTCM 3.x, via GPRS + NTRIP (now with real-time quasi-geoid height correction as of Feb 2026)
- **Precise positioning**: <0.01 m accuracy, RINEX, internet distribution

## Context Notes

- **NTRIP endpoint confirmed**: Alberding GmbH's worldwide NTRIP caster map independently confirms the MAKPOS caster at makpos.katastar.gov.mk on port 9001. This is the most reliable external confirmation of the caster being reachable.
- **Access procedure**: Register via the Spider Business Center at https://makpos.katastar.gov.mk/sbc/Account/Register. The ArduSimple Macedonia page notes the website is not always user-friendly; email contact with AREC may be needed.
- **Tariff**: One source referenced that MAKPOS is free of charge for users with compatible GNSS devices connected via 3G — but this may be outdated or conditional on equipment purchase. Current pricing should be confirmed directly with AREC.
- **Sector for Geodetic Works**: The AREC Sector for Geodetic Works (katastar.gov.mk/en/about-us/contact/sectors-in-arec/sector-for-geodetic-works/) administers MAKPOS.
- **Coverage**: 14 reference stations for a country of ~25 700 km² — good spatial density for flat to rolling terrain; mountainous areas may see reduced VRS performance.
- **Galileo support**: Upgraded in 2020; supports GPS + Galileo (and possibly GLONASS) multi-constellation corrections.
- **Practical workaround**: Register at makpos.katastar.gov.mk/sbc/, or use Galileo HAS / deploy a local base station.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **MAKPOS** — RINEX data via Spider Business Center | https://makpos.katastar.gov.mk/sbc/ | Contact AREC |
| **EUREF Permanent GNSS Network** — regional stations near North Macedonia | https://epncb.oma.be/ | Free (account required) |

## Sources Consulted
- AREC MAKPOS SpiderWeb portal: https://makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx
- AREC Spider Business Center login / sign-up: https://makpos.katastar.gov.mk/sbc/Account/Register
- MAKPOS Galileo upgrade announcement (Apr 2020): https://www.katastar.gov.mk/en/2020/04/08/makpos-system-upgraded-for-galileo-functionalities/
- MK_HREF2022 quasi-geoid deployment announcement (Feb 2026): https://www.katastar.gov.mk/en/2026/02/23/the-first-official-quasi-geoid-model-has-been-put-into-use-for-the-territory-of-the-republic-of-north-macedonia/
- AREC data and services overview: https://www.katastar.gov.mk/en/data/services/
- Alberding GmbH worldwide NTRIP casters map (probe of port 9001 returned "Caster not available" 2026-05-12; previously confirmed): https://www.alberding.eu/cgi-bin/map.cgi?caster=makpos.katastar.gov.mk&port=9001&lang=en
- ArduSimple North Macedonia RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-macedonia/
- EuroGeographics — AREC member profile: https://eurogeographics.org/member/agency-for-real-estate-cadastre/
- GitHub sctg-development RtkGps issue thread (MAKPOS user discussion; mentions `iMAX-GNSS` mountpoint): https://github.com/sctg-development/RtkGps/issues/14
- NTRIP-list.com Europe page — no North Macedonia entries found
- RTK2go monitor (monitor.use-snip.com) — no North Macedonia streams confirmed
- py scripts/stations_by_radius.py 41.6 21.7 200 (2026-05-12) — nearest rtk2go bases Pernik / MESTY in Bulgaria, both ~155 km from Skopje (out of useful RTK range)
