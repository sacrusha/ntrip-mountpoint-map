# Cambodia [KH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster — CORS station deployment begun (2022), NTRIP streaming unconfirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (not confirmed) |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no NTRIP caster confirmed |

## Most Recent Project Announcement

**JICA/GDCG CORS project — Khmer GEONET (Aug 2021 – Dec 2024)** — JICA conducted technical cooperation with Cambodia's General Department of Cadastre and Geography (GDCG/MLMUPC) to establish 5 CORS stations in pilot areas. The project portal is khmergeonet.xyz. As of 2026-05-06, the free trial period is extended to 2026-07-01. No NTRIP host:port is publicly listed on the site; tariff structure post-trial not disclosed.

**November 2022** — MLMUPC launched the 5 permanent CORS stations at: Phnom Penh, Kandal, Kampong Speu, Siem Reap, and Stung Treng.

Sources: https://khmergeonet.xyz/about · https://construction-property.com/mlmupc-announces-the-launch-of-permanent-satellite-stations-in-5-provinces/

## Context Notes

- **Khmer GEONET / JICA-GDCG CORS project**: 5 stations in pilot provinces (Phnom Penh, Kandal, Kampong Speu, Siem Reap, Stung Treng). Portal: khmergeonet.xyz. Free trial extended to 2026-07-01. No public NTRIP host:port or post-trial pricing disclosed. This is the only known active RTK-capable infrastructure.
- **MLMUPC / GDCG**: Ministry of Land Management, Urban Planning and Construction (through the General Department of Cadastre and Geography) owns and operates the network with JICA technical cooperation.
- ArduSimple's Cambodia page (ardusimple.com/rtk-correction-services-and-ntrip-casters-in-cambodia/) states Cambodia has no national RTK network — this was accurate as of the Aug 2025 snapshot; Khmer GEONET is a pilot/trial phase only.
- Five CORS stations across ~181,000 km² provides very sparse coverage (~200 km station spacing) — insufficient for reliable VRS; single-base RTK at 50 km range would cover limited areas only.
- **NSSC** (National Spatial Sciences Commission) is referenced in older land administration documents but no CORS/NTRIP activity found.
- Regional context: neighboring Vietnam has a mature national CORS/NTRIP network (VNGeonet); Thailand has the DOL-RTK network. Cambodia's infrastructure is several years behind.
- RTK2go: no Cambodia base stations confirmed.
- Practical alternative for hobbyists: deploy a local base station; Galileo HAS (~40 cm, no internet); GEODNET or Onocoy (coverage in Cambodia not confirmed).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **MLMUPC GNSS/CORS data** — contact ministry directly | https://www.mlmupc.gov.kh | Unknown |
| **IGS/EarthScope archive** (any IGS stations in Cambodia) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

## Sources Consulted
- Khmer GEONET project portal (JICA/GDCG): https://khmergeonet.xyz/about
- Construction & Property News — MLMUPC 5-province CORS launch (Nov 2022): https://construction-property.com/mlmupc-announces-the-launch-of-permanent-satellite-stations-in-5-provinces/
- ArduSimple Cambodia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-cambodia/
- ArcGIS StoryMaps — Towards Enhanced Land Administration in Lao PDR (regional context)
- RTK2go monitor (monitor.use-snip.com — no KH stations visible)
- rtcm-ntrip.org (no Cambodia entries found)
- Generic search in Khmer-language terms — no additional sources found
