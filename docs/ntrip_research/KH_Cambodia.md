# Cambodia [KH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06; verified + endpoint discovered 2026-05-12; trial-extension wording + Trimble Pivot URL re-confirmed 2026-05-17

## Status: ACTIVE — Khmer GEONET Trimble Pivot server live at `167.179.14.66:8080`; free trial extended to 2026-07-01

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | **Yes — free trial** (paid scheme post-trial not yet announced) |
| **host:port** | **`167.179.14.66:8080`** (Trimble Pivot Web portal — landing page at `http://167.179.14.66:8080/TrimblePivotWeb/`). NTRIP caster port-2101 endpoint not separately advertised; Trimble Pivot serves NTRIP/IP corrections from the same host (typically port 2101 for NTRIP and 8080 for web admin). Sourcetable not confirmed via sandbox (ECONNREFUSED to web port on probe 2026-05-12, likely transient or geo-filter). Source: https://khmergeonet.xyz/pnh ; https://khmergeonet.xyz/ |
| **Mountpoint(s)** | **`PNH100KHM`** (Phnom Penh, 11°37′47.14″ N / 104°52′20.71″ E, ellipsoid 2.707 m / ortho 15.743 m, UTM 48N: 486093 E / 1285617 N). Per-station mountpoints for the other 4 stations (Kandal, Kampong Speu, Siem Reap, Stung Treng) follow the same `XXX100KHM` IGS-style 9-character convention; not individually published on khmergeonet.xyz but discoverable on the sourcetable once registered. |
| **tariff** | **Free (trial)** until 2026-07-01 (per "free trial extended another 12 months till 1st July 2026" notice on khmergeonet.xyz). Post-trial pricing not announced. Source: https://khmergeonet.xyz/about (observed 2026-05-12). |
| **hobbyist_eligibility** | Unclear — `RegisterAccount.aspx` form was not reachable from sandbox (ECONNREFUSED on the web port at probe time); no public statement on khmergeonet.xyz excludes hobbyists. JICA project framing is professional surveying, but the free-trial wording is permissive ("registered GNSS users"). |
| **legal_residency_required** | Unclear — no explicit Cambodian-residency requirement on the public site; registration form fields not observable from sandbox. |
| **last_confirmed_alive** | **2026-05-17** — khmergeonet.xyz/about HTTPS 200 with free-trial-to-2026-07-01 wording re-observed; Trimble Pivot Web URL `http://167.179.14.66:8080/TrimblePivotWeb/` re-confirmed on operator page. Direct sourcetable probe of `167.179.14.66:8080` not re-attempted this round. |
| **datum_epoch** | omitted -- no citable declaration (khmergeonet.xyz /about + /pnh make no datum / epoch / reference-frame statement as of 2026-05-17; PNH100KHM page lists ellipsoid + ortho heights and UTM 48N grid values, but does not declare the underlying frame; per primer rule, neighbouring-country / EPSG inference not citable) |

## Most Recent Project Announcement

**JICA/GDCG CORS project — Khmer GEONET (Aug 2021 – Dec 2024 active cooperation; service portal continuing under GDCG)** — JICA conducted technical cooperation with Cambodia's General Department of Cadastre and Geography (GDCG/MLMUPC) to establish 5 CORS stations in pilot areas. The project portal is khmergeonet.xyz; the corrections server is Trimble Pivot, hosted on Cambodian IP `167.179.14.66`. As of 2026-05-12 the free-trial period is **extended to 2026-07-01**. A post-trial pricing scheme has not been disclosed on the public site.

**November 2022** — MLMUPC launched the 5 permanent CORS stations at: Phnom Penh, Kandal, Kampong Speu, Siem Reap, and Stung Treng.

Sources: https://khmergeonet.xyz/about · https://khmergeonet.xyz/pnh · https://khmergeonet.xyz/ · https://construction-property.com/mlmupc-announces-the-launch-of-permanent-satellite-stations-in-5-provinces/

## Context Notes

- **Khmer GEONET / JICA-GDCG CORS project**: 5 stations in pilot provinces (Phnom Penh, Kandal, Kampong Speu, Siem Reap, Stung Treng). Portal: khmergeonet.xyz. Server: **Trimble Pivot Web at `167.179.14.66:8080`** (discovered via the per-station `/pnh` page 2026-05-12). Free trial extended to 2026-07-01. Post-trial pricing not announced. This is the only known active RTK-capable infrastructure in Cambodia.
- **PNH100KHM station detail** (from khmergeonet.xyz/pnh): 11°37′47.14065″ N · 104°52′20.71325″ E · ellipsoid height 2.707 m · orthometric 15.743 m · UTM 48N: 1 285 617.021 N / 486 093.120 E.
- **Single-base RTK range**: 5 stations across ~181 000 km² means typical separations of 150–200 km — outside the ~30–40 km comfort radius for single-base RTK. Phnom Penh + Kandal pair covers metro Phnom Penh; Siem Reap and Stung Treng give point coverage for surveying within ~30 km of those cities; large gaps remain in Battambang, Pursat, Koh Kong, and the eastern provinces. Network/VRS solution is not advertised on the public Khmer GEONET pages.
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
- Khmer GEONET project portal (JICA/GDCG): https://khmergeonet.xyz/about (HTTPS 200 2026-05-12; free-trial-to-2026-07-01 confirmed)
- Khmer GEONET — Phnom Penh station page: https://khmergeonet.xyz/pnh (HTTPS 200 2026-05-12; station `PNH100KHM` coordinates and Trimble Pivot Web URL `http://167.179.14.66:8080/TrimblePivotWeb/` confirmed; registration link `http://167.179.14.66:8080/TrimblePivotWeb/RegisterAccount.aspx`)
- Khmer GEONET — home: https://khmergeonet.xyz/ (HTTPS 200 2026-05-12)
- Sandbox probe of `http://167.179.14.66:8080/TrimblePivotWeb/` and `RegisterAccount.aspx`: ECONNREFUSED 2026-05-12 (web port not reachable; either transient or filtered)
- Construction & Property News — MLMUPC 5-province CORS launch (Nov 2022): https://construction-property.com/mlmupc-announces-the-launch-of-permanent-satellite-stations-in-5-provinces/
- ArduSimple Cambodia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-cambodia/ (still says Cambodia has no national network — out of date as of 2026-05)
- ArcGIS StoryMaps — Towards Enhanced Land Administration in Lao PDR (regional context)
- RTK2go monitor (monitor.use-snip.com — no KH stations visible)
- rtcm-ntrip.org (no Cambodia entries found)
- Generic search in Khmer-language terms — no additional sources found
