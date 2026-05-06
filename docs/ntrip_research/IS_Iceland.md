# Iceland [IS] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free national NTRIP RTK caster operating (IceCORS); no registration fee; operated by national mapping authority

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — free of charge |
| **Network name** | IceCORS |
| **Operator** | Landmælingar Íslands (LMÍ) — National Land Survey of Iceland; operated technically in partnership with Náttúrufræðistofnun (Natural Science Institute of Iceland) for the GNSS web interface |
| **host:port** | `178.19.53.126:2101` (primary; Geo++ GNNET platform); web interface at `moe.lmi.is` |
| **VRS** | No — single-station RTK streams only; users connect to the nearest available station's mountpoint (e.g., HRNC_RTK, LAVI_RTK, SENG_RTK, GEVK_RTK, AUSV_RTK) |
| **tariff** | Free — open access |
| **hobbyist_eligibility** | Yes — open to all; no registration required |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-06 (moe.lmi.is returned HTTP 200; Geo++ GNNET page confirmed operational; station reference coordinates updated as recently as February 2024 per network metadata) |

## Service Details

IceCORS consists of approximately 33 GNSS reference stations distributed across Iceland's mainland and major inhabited areas. The network serves the dual purpose of maintaining the national coordinate system (ISN2016) and providing real-time RTK corrections to users.

**Accuracy**: Better than 5 cm typical; 2–5 cm with dual-frequency GNSS equipment. Single-station RTK; baseline distance to nearest station is the main accuracy determinant.

**Reference system**: ISN2016 (Icelandic coordinate reference system, ITRF2014 epoch 2016.0). Iceland sits astride the Mid-Atlantic Ridge and the coordinate frame is regularly updated to account for ongoing tectonic movement.

**Mountpoints**: Each physical reference station has its own mountpoint (format: `STATIONCODE_RTK`). Example active mountpoints include HRNC_RTK (formerly HRAC), LAVI_RTK (formerly LAHV), SENG_RTK, GEVK_RTK, AUSV_RTK. Full sourcetable available at `http://178.19.53.126:2101/`.

**Software platform**: Geo++ GNNET.

## Context Notes

- **Tectonic caveat**: Iceland is geologically active. The ISN2016 coordinate frame is referenced to a specific epoch (2016.0). Users requiring millimeter-level geodetic accuracy should consult LMÍ for current deformation corrections. For centimeter RTK surveying, the system is fully adequate without adjustment.
- **Coverage gaps**: Iceland's interior (the Highlands, Vatnajökull glacier area) has limited or no cellular internet coverage, making NTRIP reception impractical despite the presence of nearby IceCORS stations in some areas.
- **Agriculture/farming use**: IceCORS is promoted for precision agriculture in Iceland. Bændablaðið (the Icelandic farming newspaper) published a feature on IceCORS enabling precision fertiliser guidance on farms.
- **No VRS**: Unlike many European national networks, IceCORS does not offer network RTK / VRS. Users must connect to a single station. Iceland's station spacing (~50–60 km) is adequate for most practical RTK use.
- **IGS station**: The REYK IGS continuous monitoring station in Reykjavík is a separate geodetic station maintained in cooperation with LMÍ, providing data to the global IGS network. It is not an IceCORS user-service mountpoint.
- **Hobbyist note**: IceCORS is entirely free with no login, no registration, and no time limits. Unique among national RTK services in Europe for having zero barriers to access.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **LMÍ Geo-service / RINEX download** | https://www.lmi.is/is/maelingar/gogn-til-nidurhals/geo-service | Free |
| **IGS station REYK data** | https://www.igs.org/ | Free |

## Sources Consulted
- IceCORS Geo++ GNNET page: https://moe.lmi.is/index_en.html (redirects to moe.lmi.is; HTTP 200 confirmed 2026-05-06)
- IceCORS webservices: https://moe.lmi.is/
- LMÍ IceCORS service page: https://www.lmi.is/is/maelingar/thjonustur/icecors
- LMÍ RINEX/Geo-service: https://www.lmi.is/is/maelingar/gogn-til-nidurhals/geo-service
- NKG Iceland national report (ISN2016 context): https://www.nordicgeodeticcommission.com/wp-content/uploads/2021/03/NKG_WGRF2020_3-4_NatRep-Iceland.pdf
- Bændablaðið IceCORS agriculture article: https://www.bbl.is/skodun/a-faglegum-notum/betri-nyting-aburdar-med-hjalp-icecors-leidrettingarkerfis-landmaelinga-islands
- Reykhólahreppur IceCORS station news: https://gamli.reykholar.is/frettir/Landmaelingar_med_IceCORS-stod_a_Reykholum/
- LMÍ AMAP project profile: https://projects.amap.no/project/landmaelingar-islands-the-national-land-survey-of-iceland-lmi-lmi/
- ArduSimple Iceland: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-iceland/
- EPNCB station REYK: https://www.epncb.oma.be/_networkdata/siteinfo4onestation.php?station=REYK00ISL
