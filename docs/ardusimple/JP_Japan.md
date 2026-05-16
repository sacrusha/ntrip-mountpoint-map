# Japan

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-japan/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **QZSS/CLAS** — operator: JAXA/Cabinet Office — coverage: Japan
  - notes: Free satellite-based centimeter-level correction via QZSS L6 band. No NTRIP; receiver must have L6 band capability. CLAS = centimeter-level, MADOCA = decimeter-level.

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
### National RTK network in Japan

No publicly accessible NTRIP-based national network identified. Ardusimple notes Japan has the QZSS (Michibiki) system with CLAS (centimeter-level) and MADOCA (decimeter-level) corrections delivered via L6 satellite band — free, but requires L6-capable receiver; not NTRIP.

### Free international RTK correction services in Japan

**RTK2GO** — Free global community based correction network without quality of service.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/

### Paid international correction services in Japan

**Swift Navigation Skylark** — Centimeter-level RTK correction service. $69/month for RTK, $29/month for RTK-SSR. Free 6-month trial available.
