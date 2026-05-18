# Afghanistan [AF] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-15, originally 2026-05-06)

## Status: NO public NTRIP RTK caster — none ever documented; none plausible under current conditions

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **landing_url** | n/a — no operator |
| **access_url** | n/a — no operator |
| **host:port** | null |
| **tariff** | null |
| **num_stations** | 0 public real-time CORS; 1 research-only GNSS station (CAIAG, no NTRIP) |
| **vrs** | n/a |
| **hobbyist_eligibility** | n/a — no service exists |
| **legal_residency_required** | n/a — no service exists |
| **last_confirmed_alive** | n/a — no endpoint ever discovered |

## Why there is no caster

- **AGCHO** (Afghan Geodesy and Cartography Head Office, the national mapping authority, founded 1958) operates as a cartography / boundary-data agency. Its public geoservices are administrative-boundary tiles hosted by Information Technology Outreach Services (ITOS) under USAID funding, not geodetic CORS. No NTRIP caster, RTK product, or sourcetable has ever been associated with AGCHO in open sources.
- **Post-2021 break in international engagement.** Following the Taliban takeover (August 2021), USAID/USGS geospatial assistance to AGCHO was suspended; no successor donor programme for CORS deployment has been announced. AGCHO's operational status under the de-facto authorities is opaque.
- **No IGS / EUREF / AFREF membership** for any Afghan station; Afghanistan does not appear in the IGS network filter, EPN, or AFREF rosters.
- **No commercial coverage.** GEODNET, PointOne Polaris, Swift Skylark, Trimble VRS Now, Hexagon HxGN SmartNet, and Topcon TopNET Live publish no Afghanistan PoPs.
- **No volunteer coverage.** Local sourcetable archives in `data/` contain zero AF entries. Verified 2026-05-17 via `py scripts/stations_by_country.py AFG` (rtk2go: not listed; Centipede: not listed; EarthScope: not listed) and `py scripts/stations_by_radius.py 34.5 69.2 500` (no stations within 500 km of Kabul).

## Research-only GNSS infrastructure (not a caster)

| Detail | Value |
|---|---|
| **Network** | CAIAG (Central-Asian Institute for Applied Geosciences, Bishkek) regional GNSS network |
| **Afghan footprint** | 1 permanent GNSS station (location not published on the operator's public page) |
| **Purpose** | Tectonic / crustal-deformation monitoring (post-processed) |
| **NTRIP / real-time** | Not advertised; CAIAG's GNSS page describes monitoring use only |
| **Source** | http://www.caiag.kg/en/scientific-infrastructure/monitoring-systems/gnss-monitoring (fetched 2026-05-17, 200 OK; states "30 permanent stations … Afghanistan (1)") |
| **Field-work record** | Metzger et al., "Report of the GNSS field work in Afghanistan and Kyrgyzstan 2014–2018", GFZ Potsdam (data publication 10.5880.GFZ.4.1.2021.003) — PDF returned binary in sandbox; URL resolves. |

This station is a science instrument, not a public RTK service. There is no published NTRIP mountpoint, no RTCM stream, and no hobbyist eligibility path.

## Most recent project / announcement

**USGS Geospatial Infrastructure Development programme (pre-2021)** — USGS trained AGCHO staff and worked toward geodetic-infrastructure modernisation. Halted after August 2021; no public CORS or NTRIP output was confirmed before the programme ended.
Source: https://www.usgs.gov/special-topics/usgs-projects-in-afghanistan/science/geospatial-infrastructure-development

No post-2021 announcement of a public Afghan CORS or NTRIP caster has surfaced in open sources as of 2026-05-17.

## Nearest cross-border alternatives

None within ~50 km of any populated Afghan area. The closest IGS-class permanent stations are 400–800 km from Kabul:

| Station | Country | Approx. distance from Kabul | Network |
|---|---|---|---|
| ISBA (Islamabad) | Pakistan | ~390 km SE | IGS / SUPARCO |
| DUSH (Dushanbe) | Tajikistan | ~450 km NE | IGS |
| TASH (Tashkent) | Uzbekistan | ~580 km N | IGS |

These are useful for static post-processing only; the baselines are far too long for real-time RTK across the border.

## Post-processing (RINEX) fallback

| Service | URL | Notes |
|---|---|---|
| EarthScope GNSS data archive (IGS holdings, neighbours) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; nearest usable station 390+ km from Kabul |
| NASA CDDIS | https://cddis.nasa.gov/ | IGS/MGEX archive of ISBA / DUSH / TASH |

Datum/epoch: omitted — no citable, currently-issued Afghan national datum declaration found. USGS-era geoTIFFs used WGS 84 / UTM zones 41–43, but that is a mapping convention, not an official geodetic-reference-frame declaration from AGCHO.

## Sandbox reachability log (2026-05-17)
- WebFetch http://www.caiag.kg/en/scientific-infrastructure/monitoring-systems/gnss-monitoring — 200 OK, content read.
- WebFetch http://agcho.gov.af/en — ECONNREFUSED from sandbox. Independent search results list the site as live, but no NTRIP/RTK content is referenced in any cached page or external citation; treat reachability as unverified.
- WebFetch https://datapub.gfz-potsdam.de/.../2021-003_Metzger-et-al_ReportFieldWork.pdf — fetched as binary PDF (1.3 MB), content not parsed in sandbox; URL resolves.
- WebFetch https://network.igs.org/ — 200 OK; interactive map returned no Afghanistan results in the country filter.
- WebFetch https://rtk.geodnet.com/coverage/ — page loads but coverage tiles render client-side; no Afghan stations surfaced in the JS-stripped view.

## Sources consulted
- Afghan Geodesy and Cartography Head Office (Wikipedia): https://en.wikipedia.org/wiki/Afghan_Geodesy_and_Cartography_Head_Office
- AGCHO official site: http://agcho.gov.af/en (ECONNREFUSED from sandbox 2026-05-17)
- USGS Geospatial Infrastructure Development (Afghanistan): https://www.usgs.gov/special-topics/usgs-projects-in-afghanistan/science/geospatial-infrastructure-development
- CAIAG GNSS monitoring: http://www.caiag.kg/en/scientific-infrastructure/monitoring-systems/gnss-monitoring
- Metzger et al. 2021, GFZ field-work report: https://datapub.gfz-potsdam.de/download/10.5880.GFZ.4.1.2021.003vuRB/2021-003_Metzger-et-al_ReportFieldWork.pdf
- IGS network browser: https://network.igs.org/
- GEODNET coverage map: https://rtk.geodnet.com/coverage/
- EPSG coordinate-system index for Afghanistan: https://epsg.io/?q=Afghanistan.
- Local data verification 2026-05-17: `py scripts/stations_by_country.py AFG` (no entries on rtk2go / Centipede / EarthScope), `py scripts/stations_by_radius.py 34.5 69.2 500` (no stations within 500 km of Kabul)
