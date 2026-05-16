# Bahrain

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kingdom-of-bahrain/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **PRN (Positioning Reference Network)** — operator: SLRB (Survey and Land Registration Bureau) — coverage: Bahrain
  - landing_url: https://www.slrb.gov.bh/InformationCenter/GeneralInfoDetail/?PageId=942&ChnlId=63&ChnlId2=62  [reachable: reachable]
  - access_url:  https://www.slrb.gov.bh/InformationCenter/GeneralInfoDetail/?PageId=942&ChnlId=63&ChnlId2=62  [reachable: reachable]
  - notes: Free national service; real-time high-precision positioning

- **RTK2GO** — operator: community-based — coverage: global
  - landing_url: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101  [reachable: reachable]
  - access_url:  http://rtk2go.com/  [reachable: reachable]
  - host:port: rtk2go.com:2101
  - notes: Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy.

- **IGS** — operator: International GNSS Service — coverage: global
  - landing_url: https://network.igs.org/  [reachable: reachable]
  - access_url:  https://register.rtcm-ntrip.org/cgi-bin/registration.cgi  [reachable: reachable]
  - notes: Free global low density high quality correction service

- **Earthscope (previously UNAVCO)** — operator: Earthscope/UNAVCO — coverage: global
  - landing_url: https://www.unavco.org/instrumentation/networks/status/nota  [reachable: reachable]
  - access_url:  https://www.earthscope.org/data/gnss-realtime/  [reachable: reachable]
  - notes: Free (for non-commercial use) global low-density high-quality correction service

## Raw extract
### National RTK network in Bahrain

**PRN (Positioning Reference Network)** — Free national service operated by SLRB.
- Info / Registration: https://www.slrb.gov.bh/InformationCenter/GeneralInfoDetail/?PageId=942&ChnlId=63&ChnlId2=62

### Free international RTK correction services in Bahrain

**RTK2GO** — Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/
