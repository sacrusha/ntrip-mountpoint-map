# Georgia [GE] - NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: RESTRICTED - national NTRIP caster (GEO-CORS / NAPR) operational; Leica Spider Business Center registration required; endpoint not publicly advertised. One rtk2go Tbilisi-area volunteer base for free.

## GEO-CORS - National Agency of Public Registry

| Field | Value |
|---|---|
| operator | National Agency of Public Registry (NAPR), Ministry of Justice of Georgia |
| landing_url | http://geocors.napr.gov.ge/SBC/spider-business-center |
| access_url | http://geocors.napr.gov.ge/SBC |
| access_type | paid |
| coverage | 26 continuously operating GNSS reference stations across Georgia, excluding the occupied regions of Abkhazia and South Ossetia. Spider Business Center delivers per-subscriber host/port/mountpoint credentials. |
| num_stations | 26 (expanded from 16 stations cited in NAPR's 2012 UNOOSA presentation; MKRN added 2019) |
| tariff | not published - SBC portal gates pricing behind login; no rate table published on napr.gov.ge or geocors.napr.gov.ge; contact Galaktion Hahubia at ghahubia@napr.gov.ge / +995 577 62 03 33 (checked: napr.gov.ge/en 2026-05-23; geocors.napr.gov.ge/SBC ECONNREFUSED from sandbox 2026-05-23; web search "GEO-CORS Georgia NAPR Spider 2025 datum" 2026-05-23) |
| hobbyist_eligibility | ? - registration via Spider Business Center is open to applicants; no explicit hobbyist restriction surfaced, but full terms only disclosed post-application; no public hobbyist tier (checked: napr.gov.ge/en 2026-05-23; ardusimple Georgia page 2026-05-16) |
| datum_epoch | Georgian Geodetic Datum tied to ITRS via ITRF2008 / IGS08 coordinates for 12 CORS stations at epoch 2011.353 (computed by IGN France; declared in the EU-ENPI-funded NAPR transformation help PDF at https://geotransform.napr.gov.ge/download_help.php?filename=HELP.pdf; surfaced via Google snippet 2026-05-23 since the PDF returns as binary in sandbox) |
| sourcetable | not reachable - geocors.napr.gov.ge:2101 historically ECONNREFUSED from sandbox; no third-party confirmation of geo-block / credential gating beyond closed port (checked: monitor.use-snip.com 2026-05-23; ntrip-list.com 2026-05-23) |
| vrs | ? - Leica GNSS Spider supports NRTK (VRS/MAC/iMAX); no operator declaration of NRTK product surfaced on napr.gov.ge or geocors.napr.gov.ge/SBC (checked: napr.gov.ge/en 2026-05-23; UNOOSA 2012 presentation; ADS EGU 2021 abstract 2026-05-23) |
| residency_required | ? - SBC registration is open to applicants in principle; whether non-residents can complete subscription is undocumented and full terms only disclosed post-application |
| stations_source | http://geocors.napr.gov.ge/SBC (login-gated SpiderWeb map; no public mountpoint list; station count 26 sourced from EGU 2020 Copernicus paper, refetched 2026-05-23) |

GEO-CORS was established when geodetic and cartographic functions transferred to NAPR in 2011; documented at 16 stations in the 2012 UNOOSA presentation; current count 26. The service uses Leica GNSS Spider + Spider Business Center (SBC) - real-time RTK + RINEX download via SpiderWeb + automatic computation + user/subscription management. There is no anonymous or open-access endpoint. The SBC portal `geocors.napr.gov.ge/SBC` was HTTP 200 on 2026-05-12; ECONNREFUSED from sandbox 2026-05-23 (likely transient network state, not service withdrawal - NAPR remains the operating agency per napr.gov.ge/en where "Continuously Operating Reference Stations" appears under the Geodesy, Geoinformation, and Cadastre section refetched 2026-05-23). Curl probe of `geocors.napr.gov.ge:2101` historically returned ECONNREFUSED / timeout consistent with a closed credential-gated caster. Scientific use of GEO-CORS data appears in 2021 EGU literature (Caucasus crustal-deformation studies). The 2024-2025 Georgian political situation has not been reported to affect technical operation.

## Volunteer fallback

| Source | Mountpoint | Lat / Lon | Notes |
|---|---|---|---|
| rtk2go | `geotimege` | 41.69 N, 44.86 E | Single volunteer base in Tbilisi area (verified 2026-05-23 in `data/rtk2go.sourcetable`, RTCM 3.2 GPS+GLO+GAL+BDS, single-base; rtk2go convention any-email / no password). Free, no signup. Usable within ~20 km of Tbilisi. |

No Centipede, EarthScope, GEODNET, ONOCOY stations have been observed inside Georgia as of 2026-05-23 (checked: local `scripts/stations_by_country.py GEO` 2026-05-23; centipede.fr station map 2026-05-23). Coverage of the occupied regions of Abkhazia and South Ossetia: no publicly accessible Georgian or Russian-side caster surfaced; SmartGEO and Russian FAGS networks do not publish open NTRIP endpoints reachable internationally.

## Hobbyist path

1. **Tbilisi area (<=20 km)** - try rtk2go `geotimege` (free, no signup, single-base RTK).
2. **Elsewhere in Georgia** - register at geocors.napr.gov.ge/SBC; pricing only after application. The IGN-computed datum/epoch make this the only cm-accurate option with documented frame ties.
3. **Self-host** - deploy a base; stream over rtk2go or run privately.
4. **PPP fallback** - Galileo HAS (~20 cm horizontal, free).

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| GEO-CORS RINEX archive (via SpiderWeb after registration) | http://geocors.napr.gov.ge/SBC | Governed by NAPR subscription terms; pricing not public |
| EarthScope / IGS archive (Caucasus stations) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA) |

## Sources

- NAPR official site (English): https://www.napr.gov.ge/en/ (refetched 2026-05-23; "Continuously Operating Reference Stations" present in service menu)
- GEO-CORS Spider Business Center portal: http://geocors.napr.gov.ge/SBC (HTTP 200 2026-05-12; ECONNREFUSED from sandbox 2026-05-23)
- GEO-CORS SBC service page: http://geocors.napr.gov.ge/SBC/spider-business-center
- NAPR EuroGeographics profile: https://eurogeographics.org/member/national-agency-of-public-registry/
- UNOOSA 2012 NAPR presentation: https://www.unoosa.org/documents/pdf/psa/activities/2012/un-latvia/ppt/4-21.pdf
- NAPR EU-ENPI transformation HELP.pdf (Georgian Geodetic Datum tied to ITRF2008/IGS08 at epoch 2011.353, 12 CORS computed by IGN France): https://geotransform.napr.gov.ge/download_help.php?filename=HELP.pdf
- ArduSimple Georgia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-georgia/
- ADS Caucasus crustal-deformation abstract (EGU 2021, GEO-CORS data use): https://ui.adsabs.harvard.edu/abs/2021EGUGA..23.2675K/abstract
- Local 2026-05-23: `data/rtk2go.sourcetable` row 217 `geotimege;Tbilisi;...;GEO;41.69;44.86` confirmed; `scripts/stations_by_country.py GEO` -> 1 rtk2go station only
