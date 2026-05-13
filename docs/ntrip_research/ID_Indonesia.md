# Indonesia [ID] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (updated 2026-05-12: live sourcetable captured at `nrtk.big.go.id:2001`)

## Status: YES — InaCORS (BIG) free national NTRIP caster operational; coverage outside Java/Bali sparse

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **host:port — InaCORS** | `nrtk.big.go.id:2001` (non-standard port; not 2101) |
| **caster software** | Leica `GNSS Spider 7.10.1.168/1.0` (sourcetable banner 2026-05-12) |
| **network type** | physical-coord-vrs — up to 5 nearest bases used per session; VRS computed corrections |
| **tariff** | Free — mandated by Law No. 4/2011 (Geospatial Information Law) |
| **hobbyist_eligibility** | Yes — registration open to government, academic, and private sector; no surveying licence required |
| **legal_residency_required** | Unclear — registration at nrtk.big.go.id; no documented residency or citizenship requirement, though the registration form is in Indonesian |
| **last_confirmed_alive** | 2026-05-12 — `nrtk.big.go.id:2001` returned `SOURCETABLE 200 OK Server: GNSS Spider 7.10.1.168/1.0` (Content-Length 445); 4 network-solution mountpoints enumerated: `max-rtcm3` (RTCM 3, GPS+GLO, near Jakarta 6.49 S 106.85 E), `Nearest-rtcm3` (full GNSS+QZSS, central Kalimantan 2.53 S 112.94 E), `imax-rtcm3` (full GNSS+QZSS, West Papua 2.92 S 132.30 E), `vrs-rtcm3` (full GNSS+QZSS, central Java 6.0 S 106.0 E) |

## InaCORS Network Details

- **Operator**: BIG — Badan Informasi Geospasial (Geospatial Information Agency), the Indonesian national mapping authority
- **Legal basis**: Law No. 4/2011 on Geospatial Information mandates free public access to the national spatial reference infrastructure
- **Station count (declared)**: BIG reported 397 physical CORS stations by end of 2022, targeting 435 by end of 2023; BPN (National Land Agency / ATR-BPN) separately operates ~186 CORS stations; integration of BPN stations into InaCORS is in progress
- **Station count (sourcetable)**: only 4 mountpoints appear in the live NTRIP sourcetable (confirmed 2026-05-12) — these are network solution products (`max`, `Nearest`, `imax`, `vrs`), not individual physical stations. The gap between declared (~400+ physical CORS) and exposed (4 network mounts) is by design: BIG runs Leica GNSS Spider in network-RTK mode where physical stations feed the network solution internally and individual single-base RTK mountpoints are not exposed publicly. This means the on-map "station count" derived from the sourcetable will always be 4 — actual physical coverage is much wider
- **Coverage**: physically denser on Java, Bali, Sumatra, and Sulawesi; Papua, Kalimantan, and eastern islands have documented gaps. BIG's 2022 development planning paper identified Papua, Kalimantan, and parts of Sulawesi/Sumatra as priority expansion areas
- **Registered users**: 16,800+ as of last published report (BIG)
- **Correction format**: RTCM; RINEX post-processing also offered via the same portal
- **Registration portal**: https://nrtk.big.go.id — click "Daftar" (Register); form fields in Indonesian; email verification required
- **Contact**: big.go.id contact page / pjkgg@big.go.id

## Coverage Gap and Volunteer Supplement

The InaCORS sourcetable coverage problem means that outside the Java/Bali core, practical RTK coverage is unreliable. rtk2go carries 8 Indonesian volunteer bases in the data/stations.json fetch 2026-05-12 — distribution: Java (`JavaIoT`, `RTK_BASE-ID_TJ1`, `SI-Indonesia`, `TECHNOGIS`), East Java/Madura (`GSM-Samudera`), Sumbawa (`Dispatch_batuhijau`), East Kalimantan (`PSP_Samudera`), South Kalimantan (`SVYKID`). No Centipede-RTK or EarthScope IDN nodes. Outer islands (Papua, Maluku, Nusa Tenggara Timur, most of Sulawesi) have no confirmed free RTK coverage outside InaCORS network mounts.

## ATR/BPN CORS

ATR/BPN (Ministry of Agrarian Affairs and Spatial Planning / National Land Agency) operates its own CORS network (~186 stations) for cadastral land registration work. This network is not independently accessible as a public NTRIP caster; BPN's GeoKKP system (a QGIS plugin used internally for land parcel cadastral processing) interfaces with the BPN CORS but this is a closed internal professional tool. Integration of BPN CORS data into InaCORS/BIG infrastructure is ongoing under national geospatial reference system harmonisation policy.

## Commercial Alternatives

No independent commercial NTRIP VRS network with Indonesia-wide coverage has been identified:
- GEODNET: no confirmed Indonesia production coverage as of 2026-05-06
- HxGN SmartNet / Trimble VRS Now: Indonesian distributors (GPS Lands IndoSolutions — Trimble; PT MSDI — Leica) sell and rent RTK hardware but no confirmed national commercial VRS caster is listed on their sites
- RTKdata / PointOne: no Indonesia production coverage confirmed
- ArduSimple Indonesia RTK page lists InaCORS and Galileo HAS as the available options; no domestic commercial NTRIP caster is identified

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **InaCORS / SRGI** — RINEX download from BIG reference stations | https://srgi.big.go.id/ | Free (account required) |
| **EarthScope / IGS** — BAKO (Bakosurtanal, Cibinong), COCO (Cocos Islands), YAR3, DARW — nearest IGS stations | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- InaCORS portal: https://nrtk.big.go.id
- Live caster sourcetable: `curl http://nrtk.big.go.id:2001/` → `SOURCETABLE 200 OK Server: GNSS Spider 7.10.1.168/1.0` (4 STR rows: max-rtcm3, Nearest-rtcm3, imax-rtcm3, vrs-rtcm3; 2026-05-12)
- BIG InaCORS product page: https://www.big.go.id/en/content/produk/inacors
- SRGI — InaCORS page: https://srgi.big.go.id/page/nrtk
- SRGI — service check: https://srgi.big.go.id/page/service-check
- SRGI — dataset (InaCORS station distribution): https://data.go.id/dataset/dataset/srgi-inacors-wilayah-indonesia
- ResearchGate — InaCORS distribution figure: https://www.researchgate.net/figure/Distribution-of-InaCORS-source-https-nrtkbiggoid_fig2_355391562
- "The Development Planning of the InaCORS BIG for Disaster Climate Environment and Hazard Mitigation" (2022): https://www.researchgate.net/publication/364394916_The_Development_Planning_of_the_InaCORS_BIG_for_Disaster_Climate_Environment_and_Hazard_Mitigation
- "InaCORS BIG Satu Referensi Pemetaan Indonesia": https://www.researchgate.net/publication/337705971_InaCORS_BIG_Satu_Referensi_Pemetaan_Indonesia
- Indosurta blog — free NTRIP services Indonesia: https://indosurta.co.id/blog/layanan-ntrip-gratis-yang-perlu-dicoba-untuk-pemetaan-topografi/
- ArduSimple — RTK correction services Indonesia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-indonesia/
- ATR/BPN official site: https://www.atrbpn.go.id/
- GeoKKP documentation: https://geokkp-gis.github.io/docs/
- country-survey.md ID stub (2026-04-29)
- networks.md `inacors` entry
