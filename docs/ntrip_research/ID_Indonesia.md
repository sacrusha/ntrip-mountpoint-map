# Indonesia [ID] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — InaCORS (BIG) free national NTRIP caster operational; coverage outside Java/Bali sparse

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **host:port — InaCORS** | `nrtk.big.go.id:2001` (non-standard port; not 2101) |
| **network type** | physical-coord-vrs — up to 5 nearest bases used per session; VRS computed corrections |
| **tariff** | Free — mandated by Law No. 4/2011 (Geospatial Information Law) |
| **hobbyist_eligibility** | Yes — registration open to government, academic, and private sector; no surveying licence required |
| **legal_residency_required** | Unclear — registration at nrtk.big.go.id; no documented residency or citizenship requirement, though the registration form is in Indonesian |
| **last_confirmed_alive** | nrtk.big.go.id and srgi.big.go.id both returned HTTP 200 on 2026-05-06; service referenced in active Indonesian surveying community guides |

## InaCORS Network Details

- **Operator**: BIG — Badan Informasi Geospasial (Geospatial Information Agency), the Indonesian national mapping authority
- **Legal basis**: Law No. 4/2011 on Geospatial Information mandates free public access to the national spatial reference infrastructure
- **Station count (declared)**: BIG reported 397 physical CORS stations by end of 2022, targeting 435 by end of 2023; BPN (National Land Agency / ATR-BPN) separately operates ~186 CORS stations; integration of BPN stations into InaCORS is in progress
- **Station count (sourcetable)**: only ~4 unique physical coordinates appear in the live NTRIP sourcetable — the pipeline noted this discrepancy. The gap between declared (~400+) and sourced (~4) stations suggests the caster exposes only a subset of the network, or that most stations connect via internal VRS computation and do not appear as individual mountpoints
- **Coverage**: physically denser on Java, Bali, Sumatra, and Sulawesi; Papua, Kalimantan, and eastern islands have documented gaps. BIG's 2022 development planning paper identified Papua, Kalimantan, and parts of Sulawesi/Sumatra as priority expansion areas
- **Registered users**: 16,800+ as of last published report (BIG)
- **Correction format**: RTCM; RINEX post-processing also offered via the same portal
- **Registration portal**: https://nrtk.big.go.id — click "Daftar" (Register); form fields in Indonesian; email verification required
- **Contact**: big.go.id contact page / pjkgg@big.go.id

## Coverage Gap and Volunteer Supplement

The InaCORS sourcetable coverage problem means that outside the Java/Bali core, practical RTK coverage is unreliable. rtk2go carries approximately 8 Indonesian volunteer bases (mostly Java/Bali), which partially fills the gap in the densest population centres. Outer islands (Papua, Maluku, Nusa Tenggara Timur, most of Kalimantan) have no confirmed free RTK coverage.

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
