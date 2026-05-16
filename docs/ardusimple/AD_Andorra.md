# Andorra

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-andorra/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **ERGAND** — operator: Andorran national service — coverage: Andorra
  - landing_url: https://www.cartografia.ad/descripcio-dels-serveis  [reachable: reachable]
  - access_url:  https://www.cartografia.ad/serveis-a-temps-real  [reachable: reachable]
  - notes: Free national service

- **RTK2GO** — operator: community-based — coverage: global
  - landing_url: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101  [reachable: reachable]
  - access_url:  http://rtk2go.com/  [reachable: reachable]
  - host:port: rtk2go.com:2101
  - notes: Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, but not good for calibrated surveying.

- **IGS** — operator: International GNSS Service — coverage: global
  - landing_url: https://network.igs.org/  [reachable: reachable]
  - access_url:  https://register.rtcm-ntrip.org/cgi-bin/registration.cgi  [reachable: reachable]
  - notes: Free global low density high quality correction service

- **Earthscope (previously UNAVCO)** — operator: Earthscope/UNAVCO — coverage: global
  - landing_url: https://www.unavco.org/instrumentation/networks/status/nota  [reachable: reachable]
  - access_url:  https://www.earthscope.org/data/gnss-realtime/  [reachable: reachable]
  - notes: Free (for non-commercial use) global low-density high-quality correction service

## Raw extract
### National RTK network in Andorra

**ERGAND** — Free national service.
- Description: https://www.cartografia.ad/descripcio-dels-serveis
- Registration: https://www.cartografia.ad/serveis-a-temps-real

### Free international RTK correction services in Andorra

**RTK2GO** — Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, but not good for calibrated surveying applications.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/

### Paid international correction services in Andorra

**u-blox PointPerfect Flex** — 1 centimeter RTK and 2-4 centimeter accuracy augmentation service (RTK-SSR). Starting from $5.90/month for up to 100 hours. Free 30-day trial available.

**Swift Navigation Skylark** — RTK from $69/month; RTK-SSR from $29/month for unlimited use. Free 6-month trial available.
