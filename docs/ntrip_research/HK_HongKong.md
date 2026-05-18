# Hong Kong [HK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (updated 2026-05-17: SMO `whatsnew` page confirms 2 new SatRef product additions — IM RTCM raw streams 2025-07-02 and IM NMEA streams 2026-03-02 — both already enumerated in 2026-05-12 sourcetable; live re-probe of `ntrip.geodetic.gov.hk:2101` blocked from this sandbox so prior 2026-05-12 capture stands)

## Status: YES — free government NTRIP RTK caster operating (SatRef); application required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — free of charge |
| **Network name** | SatRef (Hong Kong Satellite Positioning Reference Station Network) |
| **Operator** | Survey and Mapping Office (SMO), Lands Department, HKSAR Government |
| **landing_url** | https://www.geodetic.gov.hk/en/satref/satref.htm (operator-owned) |
| **access_url** | https://www.geodetic.gov.hk/en/satref/ntrip.htm (NTRIP service page; links to PDF application form, submitted to geodetic@landsd.gov.hk) |
| **host:port** | `ntrip.geodetic.gov.hk:2101` (caster banner identifies as `GNCASTER` at `59.152.234.19:2103` internally; new public domain active from 1 June 2023; legacy `www.geodetic.gov.hk:2101` also documented; HTML sourcetable at `http://183.178.46.138:2101/sourcetable.htm`) |
| **num_stations** | 19 physical CORS — 16 reference stations + 3 Integrity Monitoring (IM) stations per SatRef Network RTK page; 18 of 19 visible in public sourcetable (TCHK suspended for maintenance since 2025-08-05; entry retained, stream offline) |
| **vrs** | yes — Network RTK service provides VRS corrections, but the VRS network solution is a **separate credentialed product not exposed in the public sourcetable**. The 18 public RTCM 3.2 MSM5 mounts (`HKxx_32` / `T430_32` / `*_NMEA`) are single-base / IM streams; the VRS mount is published only to authenticated users. |
| **datum_epoch** | omitted — no citable operator declaration of frame+epoch on geodetic.gov.hk pages. SatRef coordinates are widely reported as HK1980 Grid (local) with ITRF96 epoch 1997.0 underlying realisation; 7-parameter HK1980↔WGS84 transformation is published by SMO, but no operator URL explicitly declares the caster's correction-stream frame+epoch. |
| **tariff** | Free of charge |
| **hobbyist_eligibility** | Yes — application open to any user; form submitted to geodetic@landsd.gov.hk; no professional licence requirement |
| **legal_residency_required** | No — no explicit residency requirement; application is an email/form submission open internationally |
| **last_confirmed_alive** | 2026-05-12 — `ntrip.geodetic.gov.hk:2101` returned `SOURCETABLE 200 OK Server: NTRIP GNSMART_Caster 2.0/1.0` (Content-Length 4261); 21 STR rows enumerated including 18 RTCM3.2 MSM5 single-base streams + 3 NMEA streams |

## Mountpoint Catalogue — SatRef (sourcetable 2026-05-12)

18 single-base RTCM 3.2 MSM5 streams (GPS+GLO+BDS+GAL+QZSS) + 3 NMEA position streams = 21 STR rows. Each `HKxx_32` / `T430_32` mount corresponds to a physical Trimble Alloy or Leica GR50 reference station; latitude/longitude in the sourcetable matches the documented station location.

| Mount | Station | Lat (N) | Lon (E) | Receiver |
|---|---|---|---|---|
| `HKCL_32` | Chek Lap Kok | 22.30 | 113.91 | Trimble Alloy |
| `HKFN_32` / `HKFN_NMEA` | Fanling (IM) | 22.49 | 114.14 | Trimble Alloy |
| `HKKS_32` | Kau Sai Chau | 22.37 | 114.31 | Leica GR50 |
| `HKKT_32` | Kam Tin | 22.45 | 114.07 | Leica GR50 |
| `HKLM_32` | Lamma Island | 22.22 | 114.12 | Leica GR50 |
| `HKLT_32` | Lam Tei | 22.42 | 114.00 | Leica GR50 |
| `HKMW_32` | Mui Wo | 22.26 | 114.00 | Trimble Alloy |
| `HKNP_32` | Ngong Ping | 22.25 | 113.89 | Leica GR50 |
| `HKOH_32` | Obelisk Hill | 22.25 | 114.23 | Leica GR50 |
| `HKPC_32` | Peng Chau | 22.29 | 114.04 | Leica GR50 |
| `HKQT_32` / `HKQT_NMEA` | Quarry Bay (IM) | 22.29 | 114.21 | Trimble Alloy |
| `HKSC_32` | Stonecutters Island | 22.32 | 114.14 | Leica GR50 |
| `HKSL_32` | Siu Lang Shui | 22.37 | 113.93 | Leica GR50 |
| `HKSS_32` | Shap Sze Heung | 22.43 | 114.27 | Leica GR50 |
| `HKST_32` | Shatin | 22.39 | 114.18 | Leica GR50 |
| `HKTK_32` | Sha Tau Kok | 22.55 | 114.22 | Leica GR50 |
| `HKWS_32` | Wong Shek | 22.43 | 114.33 | Leica GR50 |
| `T430_32` | Fanling (T430) | 22.50 | 114.14 | Leica GR50 |
| `TCHK_32` / `TCHK_NMEA` | Tate's Cairn (IM) — *under maintenance since 2025-08-05* | 22.36 | 114.22 | Trimble Alloy |

`HKFN_NMEA`, `HKQT_NMEA`, `TCHK_NMEA` carry GPGGA position strings from the three Integrity Monitoring stations — separately announced product launched 2026-03-02 (SMO Whatsnew). Companion IM RTCM raw streams (the `HKFN_32` / `HKQT_32` / `TCHK_32` MSM5 mounts above) were the earlier 2025-07-02 launch. Both products are intended for network-integrity / research use rather than as primary RTK correction sources.

## Service Details

### Network RTK (centimeter-level)
SatRef Network RTK uses 19 Continuously Operating Reference Stations (CORS): 16 reference stations plus 3 Integrity Monitoring (IM) stations evenly distributed across Hong Kong. The network delivers centimeter-level corrections via NTRIP using the VRS method. RTCM 3.2 MSM5 single-base streams enumerated above; the VRS network solution is a separate **credentialed** product not visible in the public 18-stream sourcetable — hobbyists must apply for SatRef credentials and request the VRS mount specifically to use Network RTK.

### Differential GNSS (DGNSS, meter-level)
SatRef also provides a DGNSS stream (~1–2 m accuracy) via the same NTRIP server. Out of scope for RTK research but noted.

### Connection Settings (from official page, observed 2026-05-06)
- **Hostname:** `ntrip.geodetic.gov.hk` (from 1 June 2023 onward)
- **Port:** `2101`
- **Login:** Username and Password issued after application approval

### Application Process
Fill in the application form (PDF: `Satref_NTRIP_application_form.pdf` linked from the official page) and submit by fax or email to `geodetic@landsd.gov.hk`. Accounts inactive for 12 months are terminated without notice.

### Account Expiry — 2026-06-30 Mass Renewal
All SatRef NTRIP accounts issued **before July 2025** expire on **2026-06-30**; users must re-apply (same PDF form to geodetic@landsd.gov.hk) to retain access. Accounts issued from July 2025 onward follow the standard 12-month inactivity rule only. Relevant for any current user whose account predates the cutoff — silent loss of access otherwise.

## Context Notes

- **SatRef history**: Launched 21 June 2007. The network has been progressively upgraded from GPS-only to full GNSS (GPS, GLONASS, Galileo, BeiDou).
- **TCHK maintenance**: The Tate's Cairn Integrity Monitoring Station (TCHK) has been under maintenance since 5 August 2025 — confirmed still in effect on the geodetic.gov.hk Whatsnew page as of 2026-05-17. Its Network RTK Integrity Monitoring function and GNSS Raw Data Streams are suspended until further notice. The TCHK_32 / TCHK_NMEA entries remain in the sourcetable but the data stream is offline; the main RTK correction service across the remaining 18 stations continues to operate.
- **IM raw-stream product additions**: SMO Whatsnew lists two relevant launches — 2025-07-02 RTCM raw streams for Fanling, Quarry Bay, Tate's Cairn IM stations (now `HKFN_32` / `HKQT_32` / `TCHK_32`); 2026-03-02 companion NMEA streams (`*_NMEA`). Both products were already present in the 2026-05-12 sourcetable capture above.
- **Domain change (2023)**: SMO migrated from `www.geodetic.gov.hk` to `ntrip.geodetic.gov.hk` from 1 June 2023. Users with the old hostname in their receiver settings must update.
- **GNSS Raw Data Streams**: SatRef also provides open RTCM raw data streams for research/post-processing via the Data.gov.hk open-data portal (dataset: `hk-landsd-openmap-satref-raw-data-rtcm`). This is separate from the credentialed NTRIP RTK service.
- **Reference system**: HK1980 Grid (local), ITRF96 epoch 1997.0; datum transformation parameters (7-P) published for conversion to WGS84/ITRF.
- **Hobbyist note**: SatRef is entirely free and open to all. It is one of the few genuinely free, government-operated RTK NTRIP services in Asia.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SatRef RINEX data download** | https://www.geodetic.gov.hk/en/satref/ (login required) | Free (same account) |
| **GNSS Raw RTCM streams (open data)** | https://data.gov.hk/en-data/dataset/hk-landsd-openmap-satref-raw-data-rtcm | Free, no login |

## Sources Consulted
- SatRef home: https://www.geodetic.gov.hk/en/satref/satref.htm
- SatRef NTRIP service page: https://www.geodetic.gov.hk/en/satref/ntrip.htm (observed 2026-05-06)
- SatRef Network RTK page (connection settings confirmed): https://www.geodetic.gov.hk/en/satref/Net_RTK.htm (curl 200, 2026-05-06)
- SatRef Whatsnew (IM RTCM stream launch 2025-07-02; IM NMEA stream launch 2026-03-02; TCHK maintenance ongoing): https://www.geodetic.gov.hk/en/whatsnew.htm (fetched 2026-05-17)
- Data.gov.hk open RTCM dataset: https://data.gov.hk/en-data/dataset/hk-landsd-openmap-satref-raw-data-rtcm
- ArduSimple HK overview: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-hong-kong/
- Sourcetable reference: http://183.178.46.138:2101/sourcetable.htm
