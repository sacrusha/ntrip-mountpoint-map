# Singapore

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-singapore/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **SiReNT** — operator: Singapore Land Authority (SLA) — coverage: Singapore
  - landing_url: https://app.sla.gov.sg/sirent/Page/ReferenceStations  [reachable: server-error]
  - access_url:  https://app.sla.gov.sg/sirent/Page/Services  [reachable: server-error]
  - notes: Paid national service

- **RTK2GO** — operator: community-based — coverage: global
  - landing_url: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101  [reachable: reachable]
  - access_url:  http://rtk2go.com/  [reachable: reachable]
  - host:port: rtk2go.com:2101
  - notes: Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, not for calibrated surveying.

- **IGS** — operator: International GNSS Service — coverage: global
  - landing_url: https://network.igs.org/  [reachable: reachable]
  - access_url:  https://register.rtcm-ntrip.org/cgi-bin/registration.cgi  [reachable: reachable]
  - notes: Free global low density high quality correction service

- **Earthscope (previously UNAVCO)** — operator: Earthscope/UNAVCO — coverage: global
  - landing_url: https://www.unavco.org/instrumentation/networks/status/nota  [reachable: reachable]
  - access_url:  https://www.earthscope.org/data/gnss-realtime/  [reachable: reachable]
  - notes: Free (for non-commercial use) global low-density high-quality correction service

## Raw extract
### National RTK network in Singapore

**SiReNT** (Singapore Satellite Positioning Reference Network) — Paid national service.
- Coverage map: https://app.sla.gov.sg/sirent/Page/ReferenceStations
- Registration: https://app.sla.gov.sg/sirent/Page/Services

### Free international RTK correction services in Singapore

**RTK2GO** — Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy; not good for calibrated surveying.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/
