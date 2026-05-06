# Guatemala [GT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: UNKNOWN — CORS network exists; public NTRIP streaming unconfirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown |
| **Operator** | Instituto Geográfico Nacional (IGN) Guatemala |
| **Network name** | Red CORS IGN Guatemala (17 stations) |
| **host:port** | Not publicly documented; NTRIP streaming status unconfirmed |
| **tariff** | RINEX data via Marketing & Sales; no NTRIP tariff published. Contact: info@ign.gob.gt · +502 2248-8100 |
| **hobbyist_eligibility** | Unknown — data access requires contacting IGN Marketing & Sales; no individual/hobbyist process described |
| **legal_residency_required** | Unknown |
| **last_confirmed_alive** | Unknown — CORS stations operational (website references active as of ~2024); NTRIP streaming not confirmed |

## Most Recent Project Announcement

**IGN Guatemala Red CORS** — 17-station national network, RINEX 2.11, data quality reviewed by NOAA. The CORS project page (ignguatemala5.webnode.es/red-cors/) was last updated 2013-06-03 and contains no NTRIP information. The official IGN site (ign.gob.gt) returned ECONNREFUSED on 2026-05-06. No NTRIP caster or real-time service has been announced publicly.

Source: https://ignguatemala5.webnode.es/red-cors/ (last updated 2013-06-03)

## Context Notes

- **17 CORS stations** distributed nationally; primary purpose is cadastral surveying and relating field measurements to Guatemala's national reference frame (GTM / GTRS). Data distributed in RINEX 2.11.
- NOAA's NGS CORS network lists a Guatemala City station (GUAT) in the CORS catalog — this is a single shared station, not the IGN national CORS network.
- There is **no evidence** in any public NTRIP registry (BKG sourcetable, rtcm-ntrip.org, RTK2go monitor) of a Guatemalan NTRIP caster actively streaming, as of 2026-05-06.
- ArduSimple's Guatemala page explicitly states: "As far as we know, Guatemala does not have a National RTK Network. If you know of any, please contact us." (as of Aug 2025 snapshot).
- **Registro Nacional** (RNP) of Guatemala operates its own GNSS stations for cadastral purposes (rnpdigital.com) — these appear to feed RINEX data for post-processing only; no NTRIP streaming found.
- Practical alternative for hobbyists: Set up a local base station for single-base RTK; Galileo HAS for ~40 cm; GEODNET or Onocoy (global networks, coverage uncertain in Guatemala).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGN Guatemala CORS RINEX** — contact Marketing & Sales: info@ign.gob.gt · +502 2248-8100 | http://www.ign.gob.gt (ECONNREFUSED 2026-05-06) | Unknown (institutional purchase) |
| **NOAA NGS CORS — GUAT station** (Guatemala City) | https://geodesy.noaa.gov/CORS/ | Free |
| **SIRGAS station data** | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |

## Sources Consulted
- IGN Guatemala official site (ECONNREFUSED 2026-05-06): http://www.ign.gob.gt
- IGN Guatemala Red Geodésica page: http://www.ign.gob.gt/redgeodesica.html
- IGN Guatemala CORS Webnode mirror (last updated 2013-06-03): https://ignguatemala5.webnode.es/red-cors/
- ArduSimple Guatemala (no national RTK listed): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-guatemala/
- NOAA NGS CORS — GUAT station: https://geodesy.noaa.gov/CORS/
- SIRGAS station list: https://sirgas.ipgh.org/en/gnss-network/stations/station-list/
