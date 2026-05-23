# Afghanistan [AF] - NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: NO public NTRIP RTK caster - none ever documented; none plausible under current conditions. Afghan Geodesy and Cartography Head Office (AGCHO) historically administered legacy CORS stations under USGS / USAID assistance (decommissioned per NOAA NGS records); USAID/USGS support halted post-2021. One CAIAG research-only GNSS station exists. RTK2go / Centipede / EarthScope / IGS / commercial: zero AF stations within 500 km of Kabul.

## Why there is no caster

- **AGCHO** (Afghan Geodesy and Cartography Head Office, founded 1958) is the national mapping authority. Its public geoservices through USAID-funded ITOS hosting were administrative-boundary tiles, not geodetic CORS. Web-search references to AGCHO-administered CORS in Kabul and Herat (decommissioned) appear in third-party survey summaries; NOAA NGS's CORS network at geodesy.noaa.gov is US-only and would not normally list Afghan stations - any Afghan CORS holdings of that era are more likely archived in IGS / EarthScope. No active NTRIP caster, RTK product, or sourcetable is associated with AGCHO in open sources (checked: agcho.gov.af 2026-05-23; network.igs.org 2026-05-23; monitor.use-snip.com 2026-05-23; ntrip-list.com 2026-05-23; mvarga1989 GNSS CORS list 2026-05-23).
- **Post-2021 break in international engagement**: Following the Taliban takeover (August 2021), USAID/USGS geospatial assistance to AGCHO was suspended; no successor donor programme for CORS deployment has been announced. AGCHO's operational status under the de-facto authorities is opaque. WebFetch of agcho.gov.af returns ECONNREFUSED from sandbox 2026-05-23 (could be domain-not-resolving rather than service-down; no third-party reachability confirmation surfaced).
- **No IGS / EUREF / AFREF membership** for any Afghan station. Afghanistan does not appear in the IGS network filter (refetched 2026-05-23), EPN, or AFREF rosters.
- **No commercial coverage**: GEODNET, PointOne Polaris, Swift Skylark, Trimble VRS Now, Hexagon HxGN SmartNet, Topcon TopNET Live publish no Afghanistan PoPs.
- **No volunteer coverage**: Local 2026-05-23 - `scripts/stations_by_country.py AFG` returns no stations across any ingested source; `scripts/stations_by_radius.py 34.5 69.2 500` returns no stations within 500 km of Kabul.

## Research-only GNSS infrastructure (not a caster)

CAIAG (Central-Asian Institute for Applied Geosciences, Bishkek) regional network operates 1 permanent GNSS station inside Afghanistan for tectonic / crustal-deformation monitoring (post-processed). CAIAG's GNSS page states "30 permanent stations ... Afghanistan (1)" (fetched 2026-05-17, 200 OK). Not NTRIP, not real-time. GFZ Potsdam field-work report Metzger et al. 2014-2018 (DOI 10.5880.GFZ.4.1.2021.003) documents the deployment context.

## Most recent project / announcement

**USGS Geospatial Infrastructure Development programme (pre-2021)** trained AGCHO staff and worked toward geodetic-infrastructure modernisation. Halted after August 2021; no public CORS or NTRIP output was confirmed before the programme ended. No post-2021 announcement of a public Afghan CORS or NTRIP caster has surfaced in open sources as of 2026-05-23.

Source: https://www.usgs.gov/special-topics/usgs-projects-in-afghanistan/science/geospatial-infrastructure-development

## Nearest cross-border alternatives

None within ~50 km of any populated Afghan area. Closest IGS-class permanent stations 400-800 km from Kabul:

| Station | Country | Approx. distance from Kabul | Network |
|---|---|---|---|
| ISBA (Islamabad) | Pakistan | ~390 km SE | IGS / SUPARCO |
| DUSH (Dushanbe) | Tajikistan | ~450 km NE | IGS |
| TASH (Tashkent) | Uzbekistan | ~580 km N | IGS |

Distances from coordinate calc (Kabul 34.5/69.2); useful for static post-processing only; baselines far too long for cross-border real-time RTK. SUPARCO (Pakistan Space and Upper Atmosphere Research Commission) operates ISBA via IGS; no public Pakistani NTRIP RTK service surfaces in open sources. Iran SHAMIM (NCC) covers eastern Iran (Herat is ~120 km from the Iranian border) but is subscription-only for Iranian users; functionally unreachable for foreign hobbyists.

## Hobbyist path

1. **Cm-class** - none. Deploy a personal base for single-baseline RTK if hardware + power + connectivity permit.
2. **Sub-decimetre** - Galileo HAS (~20-40 cm horizontal, satellite-delivered, free) - the only practical sub-metre option for any user in Afghanistan.
3. **Post-processing only** - ISBA / DUSH / TASH IGS holdings via EarthScope or CDDIS.

## Post-processing (RINEX) fallback

| Service | URL | Notes |
|---|---|---|
| EarthScope GNSS data archive (IGS holdings, neighbours) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; nearest usable station 390+ km from Kabul |
| NASA CDDIS | https://cddis.nasa.gov/ | IGS / MGEX archive of ISBA / DUSH / TASH |

datum_epoch: omitted - no citable, currently-issued Afghan national datum declaration found. USGS-era geoTIFFs used WGS 84 / UTM zones 41-43, but that is a mapping convention, not an official geodetic-reference-frame declaration from AGCHO.

## Sources

- AGCHO (Wikipedia): https://en.wikipedia.org/wiki/Afghan_Geodesy_and_Cartography_Head_Office
- AGCHO official site: http://agcho.gov.af/en (ECONNREFUSED from sandbox 2026-05-23)
- USGS Geospatial Infrastructure Development (Afghanistan, pre-2021): https://www.usgs.gov/special-topics/usgs-projects-in-afghanistan/science/geospatial-infrastructure-development
- CAIAG GNSS monitoring (1 Afghan station): http://www.caiag.kg/en/scientific-infrastructure/monitoring-systems/gnss-monitoring
- Metzger et al. 2021 GFZ field-work report: https://datapub.gfz-potsdam.de/download/10.5880.GFZ.4.1.2021.003vuRB/2021-003_Metzger-et-al_ReportFieldWork.pdf
- IGS network browser (no AF entry): https://network.igs.org/
- GEODNET coverage map: https://rtk.geodnet.com/coverage/
- EPSG coordinate-system index for Afghanistan: https://epsg.io/?q=Afghanistan
- NOAA NGS CORS site list (AGCHO Kabul / Herat decommissioned): https://geodesy.noaa.gov/CORS/sort_sites.shtml
- WebSearch "Afghanistan AGCHO GNSS CORS RTK NTRIP geodesy 2024 2025" 2026-05-23 - no current service
- Local data 2026-05-23: `scripts/stations_by_country.py AFG` -> no stations; `scripts/stations_by_radius.py 34.5 69.2 500` -> no stations within 500 km of Kabul
