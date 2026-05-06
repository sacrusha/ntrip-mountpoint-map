# South Korea [KR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free national NTRIP RTK caster operating (NGII Network RTK); registration required; also Seoul city network

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — free of charge |
| **Network name** | NGII Network RTK (위성기준점 네트워크 RTK 서비스) |
| **Operator** | NGII (National Geographic Information Institute / 국토지리정보원), Ministry of Land, Infrastructure and Transport |
| **host:port — VRS service** | `vrs3.ngii.go.kr:2101` |
| **host:port — FKP service** | `fkp.ngii.go.kr:2201` |
| **Password (shared)** | `ngii` (documented in user guides and academic papers) |
| **VRS** | Yes — VRS (Virtual Reference Station) and FKP (Flächenkorrekturparameter) corrections; both based on GNSMART (Geo++) and Trimble PIVOT software |
| **tariff** | Free — open to registered users |
| **hobbyist_eligibility** | Yes — individual registration accepted; unified member registration at ngii.go.kr |
| **legal_residency_required** | Unclear — registration portal is at ngii.go.kr (Korean-language forms); foreign individuals may face practical barriers (Korean phone number or ID may be required) |
| **last_confirmed_alive** | 2026-05-06 (ngii.go.kr loaded; map.ngii.go.kr VRS service page accessible; service address change notice from May 2022 (vrs3.ngii.go.kr) found active) |

## Service Details

### NGII CORS Network
NGII operates approximately 60 GNSS reference stations at ~40 km intervals covering all ~100,000 km² of South Korea. The network has been operational since 1995 and has been progressively upgraded. As of 2024, it supports GPS, GLONASS, Galileo, and BeiDou.

### VRS Service (vrs3.ngii.go.kr:2101)
Network RTK corrections using the VRS method; centimeter-level accuracy nationwide. Password for all mountpoints: `ngii`. Users must first register as unified NGII members at ngii.go.kr and then subscribe to the Network RTK service separately through the geospatial platform (map.ngii.go.kr).

### FKP Service (fkp.ngii.go.kr:2201)
Area correction parameter (FKP) method; same free service under the same account. Port is 2201 (not standard 2101).

### Address change (2022)
NGII changed the Network RTK service connection addresses effective 2 May 2022 (notice: ngii.go.kr, board_code=notice_ko, sq=77502). The current addresses are as listed above. The legacy `vrs.ngii.go.kr` and `fkp.ngii.go.kr` (port 2101) addresses were decommissioned.

## Context Notes

- **Scale**: By 2016 NGII reported ~15,000 registered users and over 1 million service sessions. The network is heavily used by Korea's construction and civil engineering sector. Hobbyist/individual use is less common but not restricted.
- **Seoul metropolitan network**: Seoul City operates a separate supplementary network RTK system with additional stations in the Seoul metropolitan area (gnss.eseoul.go.kr). Likely requires a separate Seoul-city registration; details not fully researched.
- **Commercial alternatives**: Several private RTK network operators exist in South Korea (equipment distributors, survey companies) but these are not the primary focus here given the free NGII service.
- **Hobbyist note**: NGII service is free and widely used. The registration process is in Korean, and a Korean government portal account (using PASS/mobile identity verification) is typically required, which may be difficult for non-residents. In practice the `ngii` shared password documented in academic papers may enable connection without individual account for the FKP service, but this is not the official registration path.
- **RINEX**: NGII also provides post-processing RINEX data from its reference stations, free of charge, via the same portal.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **NGII CORS RINEX download** | http://map.ngii.go.kr/ms/mesrInfo/gnss/vrsUserView.do | Free (registration required) |

## Sources Consulted
- NGII VRS user service page: http://map.ngii.go.kr/ms/mesrInfo/gnss/vrsUserView.do
- NGII notice — service address change (May 2022): https://www.ngii.go.kr/kor/board/view.do?sq=77502&board_code=notice_ko
- NGII unified member login/registration: https://www.ngii.go.kr/member/login.do
- NGII VRS registration guide (koseco.co.kr): http://koseco.co.kr/ngii_rtk/
- Seoul city GNSS RTK system: https://gnss.eseoul.go.kr/system_sub2_03
- ASCEN Korea GNSS centre notice: http://ascenkorea.net/?page_id=126&uid=16&mod=document
- IGS Workshop 2017 paper — GNSS CORS and Network-RTK in Korea: https://files.igs.org/pub/resource/pubs/workshop/2017/W2017-PS06-06%20-%20Kim.pdf
- Network RTK smartphone app paper (PMC): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3758627/
- ArduSimple South Korea: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-south-korea/
