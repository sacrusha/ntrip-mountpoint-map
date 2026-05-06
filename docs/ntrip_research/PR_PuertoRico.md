# Puerto Rico [PR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: PARTIAL — real-time GNSS data via EarthScope NOTA NTRIP; no traditional RTK/VRS caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (geodetic, not RTK-VRS) — EarthScope NOTA streams Puerto Rico PBO stations at 1 Hz via NTRIP |
| **Operator** | EarthScope Consortium / NSF GAGE Facility (NOTA network, formerly UNAVCO) |
| **Network name** | NOTA (Network of the Americas) — includes Puerto Rico PBO stations (PRMI, PRGY, others) |
| **host:port — EarthScope NTRIP** | `ntrip.earthscope.org:2101` (RTCM 3.3) · `:2105` (BINEX) · `:2108` (point positioning) |
| **tariff** | Free for non-commercial use; commercial licensing: contact EarthScope. NOAA NCN RINEX: free |
| **hobbyist_eligibility** | Yes for non-commercial — EarthScope NTRIP is publicly accessible; note streams are 1 Hz geodetic data, not a VRS service optimized for rover RTK |
| **legal_residency_required** | No |
| **last_confirmed_alive** | EarthScope NOTA operational — Puerto Rico PBO stations (PRMI, PRGY confirmed in NCN/NOTA) streaming as of 2026-05-06 |

## Most Recent Project Announcement

**EarthScope NOTA NTRIP streaming confirmed** — The NSF GAGE Facility broadcasts 1 Hz GNSS data from ~1,100 NOTA stations including Puerto Rico PBO stations via NTRIP at `ntrip.earthscope.org`. Puerto Rico CORS stations PRMI and PRGY are confirmed NCN entries; PRGY was most affected by the January 2020 earthquake sequence (~5.6 cm northwest displacement), with updated coordinates published by NGS in February 2020. The NOAA NCN has operated Puerto Rico stations since at least 2011.

Source: https://www.earthscope.org/nota/ · https://geodesy.noaa.gov/web/news/coordinates-puerto-rico-earthquake.shtml

## Context Notes

- **Puerto Rico is a US territory** — geodetic infrastructure falls under NOAA/NGS federal programs. NOAA NCN itself does not operate a public NTRIP caster; it releases RINEX within ~1 hr for post-processing.
- **EarthScope NOTA NTRIP** (`ntrip.earthscope.org:2101`): Puerto Rico PBO stations stream 1 Hz GNSS data in RTCM 3.3 and BINEX formats. Free for non-commercial use. This is geodetic/science data, not a VRS service — rovers must handle their own baseline computation to the nearest streaming station. Useful for precise post-processing baselines and short-baseline RTK near a PR NOTA station.
- **Confirmed NCN/NOTA PR stations**: PRMI, PRGY (others exist — check NCN station list). PRGY coordinates updated after 2020 earthquake.
- **No RTK/VRS caster**: Puerto Rico has no public VRS or network RTK service equivalent to US mainland state RTN networks (e.g., InCORS, NC RTN). NGS encourages state DOTs and commercial partners to fill this gap; none confirmed as of 2026-05-06.
- **Commercial options** (Trimble VRS Now, Hexagon SmartNet): Puerto Rico coverage not confirmed — both networks are focused on continental US.
- **RTK2go**: No Puerto Rico base stations confirmed in sourcetable at research date.
- **Practical option for hobbyists**: set up own base station; Galileo HAS (~40 cm, no internet); GEODNET coverage unconfirmed but possible.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **NOAA NCN RINEX archive** — Puerto Rico stations; data within ~1 hr | https://geodesy.noaa.gov/CORS/ | Free |
| **UNAVCO/EarthScope GNSS archive** — NOTA Puerto Rico stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

## Sources Consulted
- NOAA NCN main page: https://geodesy.noaa.gov/CORS/
- NOAA NCN data and products: https://geodesy.noaa.gov/CORS/data.shtml
- NOAA NCN station page — PRMI: https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=PRMI
- NGS Puerto Rico earthquake coordinate update (2020): https://geodesy.noaa.gov/web/news/coordinates-puerto-rico-earthquake.shtml
- EarthScope NOTA network: https://www.earthscope.org/nota/
- EarthScope real-time GNSS data (NTRIP): https://www.earthscope.org/data/gnss-realtime/
- Legacy UNAVCO NTRIP caster: http://rtgpsout.unavco.org/
- ArduSimple USA page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-the-united-states-of-america-usa/
- RTK2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
