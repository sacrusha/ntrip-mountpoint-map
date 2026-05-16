# New Zealand

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-new-zealand/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **PositioNZ** — operator: LINZ (Land Information New Zealand) — coverage: New Zealand
  - landing_url: https://www.geodesy.linz.govt.nz/positionzrt/  [reachable: reachable]
  - access_url:  https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-real-time-service/connect-positionz-real-time-service  [reachable: auth-required — HTTP 403]
  - notes: Free national service

- **AUSCORS** — operator: Geoscience Australia — coverage: Australia/Pacific (available in New Zealand)
  - landing_url: https://gnss.ga.gov.au/network  [reachable: reachable]
  - access_url:  https://data.gnss.ga.gov.au/docs/home/auth.html  [reachable: reachable]
  - notes: Free regional service; registration required

- **RTK2GO** — operator: community-based — coverage: global
  - landing_url: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101  [reachable: reachable]
  - access_url:  http://rtk2go.com/  [reachable: reachable]
  - host:port: rtk2go.com:2101
  - notes: Free global community based correction network without quality of service.

- **IGS** — operator: International GNSS Service — coverage: global
  - landing_url: https://network.igs.org/  [reachable: reachable]
  - access_url:  https://register.rtcm-ntrip.org/cgi-bin/registration.cgi  [reachable: reachable]
  - notes: Free global low density high quality correction service

- **Earthscope (previously UNAVCO)** — operator: Earthscope/UNAVCO — coverage: global
  - landing_url: https://www.unavco.org/instrumentation/networks/status/nota  [reachable: reachable]
  - access_url:  https://www.earthscope.org/data/gnss-realtime/  [reachable: reachable]
  - notes: Free (for non-commercial use) global low-density high-quality correction service

## Raw extract
### National RTK network in New Zealand

**PositioNZ** — Free national service operated by LINZ.
- Coverage map: https://www.geodesy.linz.govt.nz/positionzrt/
- Registration: https://www.linz.govt.nz/products-services/geodetic/positionz/positionz-real-time-service/connect-positionz-real-time-service

**AUSCORS** — Free service from Geoscience Australia; also covers New Zealand.
- Coverage map: https://gnss.ga.gov.au/network
- Registration: https://data.gnss.ga.gov.au/docs/home/auth.html

### Free international RTK correction services in New Zealand

**RTK2GO** — Free global community based correction network without quality of service.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/
