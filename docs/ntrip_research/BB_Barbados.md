# Barbados [BB] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: NO public NTRIP RTK caster — no national or volunteer station; nearest free streams ~158 km away on Saint Lucia (EarthScope NOTA), beyond usable RTK baseline

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **National geodetic authority** | Lands and Surveys Department (Ministry of Housing, Lands and Maintenance) — maintains Barbados National Grid and "Lamont Datum"; no real-time CORS or NTRIP service publicly advertised |
| **Volunteer rtk2go coverage** | None — zero BRB-coded stations (verified 2026-05-15 via `data/stations.json` snapshot) |
| **Centipede coverage** | None within Barbados; nearest Centipede station is `DEPZ` on Martinique (~249 km) |
| **EarthScope / NOTA coverage in BB** | None — historical NGS CORS station `BDOS` (June 2005 – December 2013) decommissioned; no successor installed |
| **hobbyist_eligibility** | n/a (no caster) |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | n/a |
| **datum_epoch** | omitted (no real-time RTK service to declare a datum/epoch for; local cadastral work uses Barbados 1938 / Barbados National Grid on Clarke 1880 RGS — not a real-time GNSS reference frame) |
| **Most recent project announcement** | None found 2014–2026 for a Barbados national CORS/NTRIP service |

---

## National Surveying Authority

The **Lands and Surveys Department** (Ground Floor East, Warrens Office Complex, St. Michael; `landsandsurveys.gov.bb`) is the geodetic authority. Its public Surveying Services page states the department is "responsible for the development and maintenance of the Barbados National Grid and the Lamont Datum" but lists no GNSS reference stations, NTRIP service, or RTK correction product. The **Barbados Geoportal** (ArcGIS Hub, `geoportal-bds-lsdept.hub.arcgis.com`) hosts vector/raster spatial data only — no real-time GNSS feed.

No public announcement (cadastral, donor-funded, or regional) of a planned national RTK/CORS network for Barbados was located 2014–2026. No World Bank or Caribbean Development Bank project mentions a Barbados GNSS reference network.

---

## Historical Station — BDOS (Decommissioned)

| Field | Value |
|---|---|
| **Station ID** | BDOS |
| **Operator** | NGS (NOAA CORS Network) |
| **Online** | 2005-06-05 (DOY 156) |
| **Offline** | 2013-12-12 (DOY 346) |
| **Status** | Decommissioned — no replacement |
| **Source** | https://www.ngs.noaa.gov/CORS/sort_sites.shtml |

BDOS was an NOAA CORS sampling at 30-minute intervals (not a real-time NTRIP stream). It went offline at the end of 2013 and was never replaced. EarthScope's COCONet expansion in the Eastern Caribbean (2013–2014) installed sites on neighbouring islands (Saint Lucia, Grenada, Martinique) but not on Barbados.

---

## Nearest Free Streams (cross-border, beyond reliable RTK baseline)

Reliable cm-accuracy single-base RTK is typically limited to ~20–30 km baselines. All nearest free streams are well beyond this for any point in Barbados.

| Station | Network | Country | Distance from Bridgetown | host:port |
|---|---|---|---|---|
| `CN47_RTCM3P3` | EarthScope NOTA | Saint Lucia | ~158 km | `ntrip.earthscope.org:2101` |
| `CN04_RTCM3P3` | EarthScope NOTA | Saint Lucia | ~178 km | `ntrip.earthscope.org:2101` |
| `CN46_RTCM3P3` | EarthScope NOTA | Grenada | ~208 km | `ntrip.earthscope.org:2101` |
| `DEPZ` | Centipede | Martinique | ~249 km | `caster.centipede.fr:2101` |

EarthScope streams require an account + annual NULA (free non-commercial; USD $1,000/seat/yr commercial). All four stations are useful only for low-precision DGNSS or post-processing reference — not RTK cm-accuracy positioning anywhere in Barbados.

---

## Practical Options for a Hobbyist in Barbados

- **Run your own base/rover pair**: only practical path to cm-accuracy on the island today. Set up a local ZED-F9P (or equivalent) base on a known point; rover within ~10 km.
- **Optional**: share your own base on rtk2go or Centipede (no Barbados streams exist today — first to publish).
- **Global PPP / SSR alternatives** (out of project scope but worth noting for users): Galileo HAS (~20–40 cm, free, no infrastructure) is the only no-infrastructure free option with broadcast corrections covering Barbados. Commercial SSR services (PointPerfect, TerraStar, Skylark) — Caribbean coverage is provider-specific and not verified here.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost | Notes |
|---|---|---|---|
| **NOAA CORS Archive — BDOS historical** | https://geodesy.noaa.gov/CORS/ | Free | Data 2005-06-05 to 2013-12-12 only |
| **EarthScope GNSS Data Archive** — CN04, CN46, CN47 RINEX | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA); $1,000/seat/yr commercial | Stations on Saint Lucia / Grenada — useful for regional post-processing only |
| **Barbados Lands and Surveys Department** | https://landsandsurveys.gov.bb/ | Unknown — contact department directly (LSDept@Barbados.gov.bb) | No RINEX archive publicly advertised |

---

## Sources Consulted

- NGS All CORS Sites listing (BDOS Decommissioned 2005156–2013346): https://www.ngs.noaa.gov/CORS/sort_sites.shtml — fetched 2026-05-15, returned BDOS record
- NOAA CORS NCN station page template: https://geodesy.noaa.gov/CORS/ncn_station_pages/index.html?stationID=BDOS — fetched 2026-05-15, page is a template; no per-station data returned to sandbox
- Lands and Surveys Department, Barbados: https://landsandsurveys.gov.bb/ — fetched 2026-05-15, no GNSS/CORS/NTRIP infrastructure mentioned
- Surveying Services page (cites Barbados National Grid and Lamont Datum): https://www.landsandsurveys.gov.bb/pages/SurveyingServices.html — fetched 2026-05-15
- Barbados Geoportal: https://geoportal-bds-lsdept.hub.arcgis.com/ — fetched 2026-05-15, vector/raster portal only, no real-time GNSS
- EarthScope GNSS real-time data: https://www.unavco.org/data/gps-gnss/real-time/real-time.html — fetched 2026-05-15, confirms station list not enumerated on page; verified via local sourcetable
- COCONet site overview: https://coconet.unavco.org/people/station-info.html — fetched 2026-05-15, no Barbados station listed in network description
- EPSG Barbados 1938 datum: https://epsg.io/4212 (Clarke 1880 RGS) — local cadastral datum; not a real-time GNSS reference frame
- Local pipeline verification (2026-05-15):
  - `py scripts/stations_by_country.py BRB` → "No stations for 'BRB'"
  - `py scripts/stations_by_radius.py 13.10 -59.62 100` → "No stations within 100 km"
  - `py scripts/stations_by_radius.py 13.10 -59.62 250` → 3 EarthScope LCA/GRD + 1 Centipede MTQ stations, all >150 km
