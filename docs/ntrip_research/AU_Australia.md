# Australia [AU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (originally 2026-05-06)

## Status: YES — free national NTRIP (AUSCORS / Geoscience Australia); state networks are paid via commercial resellers

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator — national** | Geoscience Australia (GA) |
| **host:port — AUSCORS** | `ntrip.data.gnss.ga.gov.au:443` (TLS, primary) · `ntrip.data.gnss.ga.gov.au:2101` (plain TCP, also active as of 2026-05-06) |
| **VRS — AUSCORS** | No — single-base physical station streams only |
| **tariff — AUSCORS** | Free — account registration required (gnss.ga.gov.au/registration) |
| **hobbyist_eligibility** | Yes — GA states "free and open access"; registration only requires name, email, stated use-case |
| **legal_residency_required** | No |
| **last_confirmed_alive** | `ntrip.data.gnss.ga.gov.au:443` returned SOURCETABLE with 914 streams on 2026-05-06 (curl confirmed) |

## AUSCORS Technical Details

- **Protocol:** NTRIP v2.0 over TLS (port 443 primary); plain NTRIP v1.0 on port 2101 also accepted
- **Format:** RTCM 3.3 with MSM (multi-signal messages); GPS+GLO+GAL+BDS+QZS on most modern stations
- **Station count:** 914 mountpoints confirmed via sourcetable 2026-05-06
- **Mountpoint convention:** `<STA4>00AUS0` (e.g. `ALIC00AUS0` = Alice Springs NT, `SYDN00AUS0` = Sydney NSW)
- **Coverage:** Nationwide including WA interior, NT, QLD outback; most stations sparse in interior but ~100+ in populated coastal zones
- **Authentication:** Basic HTTP auth with GA credentials; email-as-username recommended; password set via GA portal
- **Note:** Geoscience Australia migrated to TLS broadcaster in ~2022; older NTRIP clients that lack TLS support require the port 2101 fallback or a local TLS-stripping proxy

## State/Territory Networks (Commercial, Paid via Resellers)

AUSCORS physical stations are spread across all states and territories but provide only single-base corrections. State governments and private operators offer VRS/network RTK at higher density and accuracy:

| State/Territory | Network | Access Model | Notes |
|---|---|---|---|
| NSW | CORSnet-NSW | Paid via authorised resellers (Spatial NSW portal) | RTCM 3.1; VRS; GDA2020/GDA94; ~200+ stations |
| VIC | Vicmap Position / GPSnet | Paid via Value Added Resellers (VARs); no new direct govt subs since Jan 2019 | VRS; 120+ stations; gnss.vicpos.com.au |
| WA | Landgate CORS | Paid; contact Landgate; 2024-25 fee increase ~3% | State-operated; reseller model |
| SA | SA CORS (DHUD) | Mixed; some free single-base via AUSCORS; paid VRS via commercial providers | dhud.sa.gov.au |
| QLD, TAS, NT, ACT | Commercial resellers | SmartNet Aus (HxGN), Topnet, AllDayRTK, Positioned RTK | Paid subscription via NTRIP |

- **HxGN SmartNet Aus** (`smartnetna.com`): National commercial VRS network covering all populated zones; subscription-based pricing (not publicly listed; contact vendor); supports RTCM 3.2 MSM.
- **Positioned RTK** (`positioned.com.au`): Subscription service leveraging GA CORS + additional stations; consumer-friendly onboarding; pricing not publicly listed.
- **AllDayRTK** (`aptella.com/alldayrtk`): Commercial VRS product; requires reseller subscription.

## Hobbyist Path

For Australian hobbyists, AUSCORS is the practical zero-cost entry point. Single-base RTK from the nearest AUSCORS station (often within 50–100 km in populated areas) gives cm-level horizontal accuracy under good baseline conditions. No paid state network offers a free hobbyist tier.

**Volunteer supplement**: 24 AUS-coded rtk2go bases + 3 Centipede AUS nodes (per `scripts/stations_by_country.py AUS`, 2026-05-12). Notable rtk2go clusters: Western Australia (REDCLIFFE_PERTH_WA, RFBYCkeanespoint, UWA_Campus, Sheoak_Range, SG1NEW), Queensland (Mossman_Base, McCaffreyField, SGMCSURATRTCM cluster, MtRavensbourne, Cadarga), South Australia (Maptek, Sheoak_Range), Victoria (warrakam, MtBuffalo_001), Tasmania (Beautypoint, Nelsonbay), NSW (Codemortk, HillcrestCandelo), NT/Pilbara (SG1NEW). Centipede AUS nodes: CADA (Queensland, co-located near Cadarga), FARM48 (NSW/VIC border region).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **AUSPOS** (GA online post-processing) | https://gnss.ga.gov.au/auspos | Free |
| **GA CORS RINEX archive** | https://data.gnss.ga.gov.au | Free (registration) |
| **EarthScope / NOTA** (selected AUS stations) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- GA GNSS Data Centre authentication page: https://data.gnss.ga.gov.au/docs/home/auth.html (observed 2026-05-06)
- GA GNSS stream portal: https://gnss.ga.gov.au/stream (observed 2026-05-06)
- AUSCORS main page: https://www.auscors.ga.gov.au/ (observed 2026-05-06)
- Emlid community (AUSCORS TLS migration): https://community.emlid.com/t/new-auscors-ntrip-broadcaster-requires-tls-certificate/27313 (observed 2026-05-06)
- ArduSimple Australia caster list: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-australia/ (observed 2026-05-06)
- Vicmap Position / GPSnet: https://gnss.vicpos.com.au/ (observed 2026-05-06)
- Spatial NSW CORSnet-NSW: https://www.spatial.nsw.gov.au/surveying/corsnet-nsw (observed 2026-05-06)
- Landgate WA 2024-25 fee update: https://www.landgate.wa.gov.au/about-us/customer-news-and-media/news-and-media-articles/2024/may/landgate-customer-update-publishing-of-2024-25-landgate-regulated-and-associated-fees-increase/ (observed 2026-05-06)
- SA CORS / DHUD: https://www.dhud.sa.gov.au/our-department/office-of-the-surveyor-general/surveying/geodetic-surveying/gnss-cors (observed 2026-05-12)
- GA GNSS data and site logs: https://www.ga.gov.au/scientific-topics/positioning-navigation/positioning-australia/geodesy/gnss-networks/data-and-site-logs (observed 2026-05-12)
- curl probe of `ntrip.data.gnss.ga.gov.au:443` — SOURCETABLE 200 OK, 914 STR entries confirmed 2026-05-06
- Local data verification (2026-05-12): `scripts/stations_by_country.py AUS` — 24 rtk2go + 3 Centipede stations enumerated
