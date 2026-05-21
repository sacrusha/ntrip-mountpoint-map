# Indonesia [ID] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (SRGI visual GNSS station monitor noted; prior versions: 2026-05-17, 2026-05-13)

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
| **last_confirmed_alive** | 2026-05-17 — `nrtk.big.go.id:2001` re-verified `SOURCETABLE 200 OK Server: GNSS Spider 7.10.1.168/1.0` (Content-Length 445); identical 4 network-solution mountpoints: `max-rtcm3` (RTCM 3, GPS+GLO, near Jakarta 6.49 S 106.85 E), `Nearest-rtcm3` (full GNSS+QZSS, central Kalimantan 2.53 S 112.94 E), `imax-rtcm3` (full GNSS+QZSS, West Papua 2.92 S 132.30 E), `vrs-rtcm3` (full GNSS+QZSS, central Java 6.0 S 106.0 E) |
| **datum_epoch** | SRGI2013 — BIG operates as authority on SRGI2013; epoch not declared on portal pages. Source: `srgi.big.go.id/page/service-check` ("BIG selaku penyelenggara SRGI2013 telah membangun 397 stasiun CORS") |

## InaCORS Network Details

- **Operator**: BIG — Badan Informasi Geospasial (Geospatial Information Agency), the Indonesian national mapping authority
- **Legal basis**: Law No. 4/2011 on Geospatial Information mandates free public access to the national spatial reference infrastructure
- **Station count (declared, verified 2026-05-13)**:
  - End of 2022: 397 stations (BIG SRGI service-check page — "BIG selaku penyelenggara SRGI2013 telah membangun 397 stasiun CORS terhitung sampai akhir tahun 2022")
  - Aug 2023: 396 stations operational per PJKGG news ("PJKGG telah membangun 396 stasiun CORS"); the announced 2023 target of 435 was NOT met that year
  - SRGI `jaring-kontrol-geodesi` page (observed 2026-05-13): still cites 397 as of 2023
  - End of 2024: 432 stations operational with 41 additional stations under construction (≈473 total planned by end-2025); 81.62% of Indonesia's urban+rural area within 50 km of an InaCORS station; Java and Bali fully served, Sumatra/Nusa Tenggara/Maluku/Sulawesi almost completely served, Papua and Kalimantan still gap regions
  - BPN (National Land Agency / ATR-BPN) separately operates ~186 CORS stations; integration of BPN stations into InaCORS is in progress
- **Station count (sourcetable)**: only 4 mountpoints appear in the live NTRIP sourcetable (confirmed 2026-05-17) — these are network solution products (`max`, `Nearest`, `imax`, `vrs`), not individual physical stations. The gap between declared (~400+ physical CORS) and exposed (4 network mounts) is by design: BIG runs Leica GNSS Spider in network-RTK mode where physical stations feed the network solution internally and individual single-base RTK mountpoints are not exposed publicly. This means the on-map "station count" derived from the sourcetable will always be 4 — actual physical coverage is much wider.
- **Station map (SRGI visual GNSS)**: The SRGI real-time GNSS monitor at `https://srgi.big.go.id/visual_gnss` exposes a dropdown listing all ~250 real-time InaCORS stations by code and administrative location (e.g. "CRPN - Rancapinang - Pandeglang - Banten"), confirming live station identity. No bulk coordinate download is available without login. The station monitoring page `https://srgi.big.go.id/visual_gnss/detail/[CODE]/nr` provides per-station displacement data (confirming the station exists and is active) but coordinates are not exposed without a registered BIG account.
- **Coverage**: physically denser on Java, Bali, Sumatra, and Sulawesi; Papua, Kalimantan, and eastern islands have documented gaps. BIG's 2022 development planning paper identified Papua, Kalimantan, and parts of Sulawesi/Sumatra as priority expansion areas
- **Registered users**: 16,800+ as of last published report (BIG)
- **Correction format**: RTCM; RINEX post-processing also offered via the same portal
- **Registration portal**: https://nrtk.big.go.id — click "Daftar" (Register); form fields in Indonesian; email verification required
- **Contact**: big.go.id contact page / pjkgg@big.go.id

## Coverage Gap and Volunteer Supplement

The InaCORS sourcetable coverage problem means that outside the Java/Bali core, practical RTK coverage is unreliable. rtk2go carries 7 Indonesian volunteer bases in the data/stations.json fetch 2026-05-17 — distribution: Java (`JavaIoT`, `RTK_BASE-ID_TJ1`, `SI-Indonesia`, `TECHNOGIS`), East Java/Madura (`GSM-Samudera`), Sumbawa (`Dispatch_batuhijau`), South Kalimantan (`SVYKID`). `PSP_Samudera` (East Kalimantan) dropped vs 2026-05-12 snapshot — minor churn. No Centipede-RTK or EarthScope IDN nodes. AUSCORS rebroadcasts `JOG200IDN0` (Yogyakarta) and `igs_ip` carries 2 IDN IGS stations (BAKO, CIBG near Cibinong); `mirai` rebroadcasts `QMKP00IDN` (Makassar). Outer islands (Papua, Maluku, NTT, most of Sulawesi) have no confirmed free RTK coverage outside InaCORS network mounts.

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
- Live caster sourcetable: `curl --http0.9 http://nrtk.big.go.id:2001/` → `SOURCETABLE 200 OK Server: GNSS Spider 7.10.1.168/1.0` (4 STR rows: max-rtcm3, Nearest-rtcm3, imax-rtcm3, vrs-rtcm3; re-verified 2026-05-17)
- SRGI service-check datum quote (WebFetch 2026-05-17): "BIG selaku penyelenggara SRGI2013 telah membangun 397 stasiun CORS terhitung sampai akhir tahun 2022" — operator declaration of SRGI2013 as service frame: https://srgi.big.go.id/page/service-check
- BIG InaCORS product page: https://www.big.go.id/en/content/produk/inacors
- SRGI — InaCORS page: https://srgi.big.go.id/page/nrtk
- SRGI — service check: https://srgi.big.go.id/page/service-check (WebFetch 2026-05-13: "397 stasiun CORS terhitung sampai akhir tahun 2022")
- SRGI — Jaring Kontrol Geodesi: https://srgi.big.go.id/page/jaring-kontrol-geodesi (WebFetch 2026-05-13: "Sampai tahun 2023, BIG mengelola 397 Ina-CORS")
- BIG news 2023-09-04 "PJKGG Terus Lakukan Perawatan Stasiun InaCORS" (WebFetch 2026-05-13: 396 stations Aug 2023, target 435 by end-2023): https://big.go.id/en/news/2023/09/04/pjkgg-terus-lakukan-perawatan-stasiun-inacors
- SRGI visual GNSS station monitor: https://srgi.big.go.id/visual_gnss (250 real-time stations in dropdown; no bulk coord download without login — 2026-05-21)
- SRGI — dataset (InaCORS station distribution): https://data.go.id/dataset/dataset/srgi-inacors-wilayah-indonesia (URL returns 404 as of 2026-05-21; archived reference only)
- ResearchGate — InaCORS distribution figure: https://www.researchgate.net/figure/Distribution-of-InaCORS-source-https-nrtkbiggoid_fig2_355391562
- "The Development Planning of the InaCORS BIG for Disaster Climate Environment and Hazard Mitigation" (2022): https://www.researchgate.net/publication/364394916_The_Development_Planning_of_the_InaCORS_BIG_for_Disaster_Climate_Environment_and_Hazard_Mitigation
- "InaCORS BIG Satu Referensi Pemetaan Indonesia": https://www.researchgate.net/publication/337705971_InaCORS_BIG_Satu_Referensi_Pemetaan_Indonesia
- Indosurta blog — free NTRIP services Indonesia: https://indosurta.co.id/blog/layanan-ntrip-gratis-yang-perlu-dicoba-untuk-pemetaan-topografi/
- ArduSimple — RTK correction services Indonesia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-indonesia/
- ATR/BPN official site: https://www.atrbpn.go.id/
- GeoKKP documentation: https://geokkp-gis.github.io/docs/
- country-survey.md ID stub (2026-04-29)
- rtk_inventory.md `inacors` entry
