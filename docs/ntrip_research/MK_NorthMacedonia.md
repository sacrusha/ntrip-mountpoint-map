# North Macedonia [MK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — MAKPOS national RTK network active; registration required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — MAKPOS (Macedonian Positioning System), operated by the Agency for Real Estate Cadastre (AREC) |
| **host:port** | makpos.katastar.gov.mk : 9001 |
| **tariff** | Subscription required; specific MKD amounts not publicly posted. MAKPOS users with compatible GNSS devices on 3G/GPRS reportedly offered free-of-charge access per one source — unclear if still current. Contact AREC to confirm. |
| **hobbyist_eligibility** | Unclear — registration via Spider Business Center portal (makpos.katastar.gov.mk/sbc/); individual sign-up appears available |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | makpos.katastar.gov.mk SBC login portal confirmed live (2026-05-06); Alberding GmbH worldwide datastream map confirms MAKPOS caster reachable |

## Most Recent Project Announcement

MAKPOS was upgraded for Galileo multi-constellation support in April 2020 (AREC announcement: https://www.katastar.gov.mk/en/2020/04/08/makpos-system-upgraded-for-galileo-functionalities/).

The system consists of 14 reference base stations positioned 50–70 km apart, a control center using Leica GNSS Spider software (RT Proxi Server + NTRIP Caster), and a web portal at makpos.katastar.gov.mk/SpiderWeb/frmIndex.aspx.

Services offered:
- **DGPS**: 0.3–0.5 m accuracy, RTCM 2.x, via GPRS + NTRIP
- **RTK**: 0.02–0.04 m accuracy, RTCM 2.x and RTCM 3.x, via GPRS + NTRIP
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
- Alberding GmbH worldwide NTRIP casters map (confirms makpos.katastar.gov.mk:9001): https://www.alberding.eu/cgi-bin/map.cgi
- ArduSimple North Macedonia RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-macedonia/
- EuroGeographics — AREC member profile: https://eurogeographics.org/member/agency-for-real-estate-cadastre/
- GitHub sctg-development RtkGps issue thread (MAKPOS user discussion): https://github.com/sctg-development/RtkGps/issues/14
- NTRIP-list.com Europe page — no North Macedonia entries found
- RTK2go monitor (monitor.use-snip.com) — no North Macedonia streams confirmed
