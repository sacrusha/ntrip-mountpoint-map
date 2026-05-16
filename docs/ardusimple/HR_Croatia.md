# Croatia

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-croatia/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **CROPOS** — operator: Croatian national authority — coverage: Croatia
  - landing_url: https://gnss.cropos.hr/Map/SensorMap.aspx  [reachable: reachable]
  - access_url:  https://www.cropos.hr/o-sustavu/120-cesta-pitanja  [reachable: reachable]
  - notes: Paid national service

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

- **EUREF** — operator: pan-European — coverage: Europe
  - landing_url: https://epncb.oma.be/_networkdata/data_access/real_time/map.php  [reachable: unverified — HTTP 000]
  - access_url:  https://epncb.oma.be/_networkdata/data_access/real_time/  [reachable: unverified — HTTP 000]
  - notes: Free paneuropean low-density high-quality correction service

## Raw extract
### National RTK network in Croatia

Many countries, including Croatia, have established their own National RTK Networks to support various high-precision GNSS applications within their borders.

**CROPOS** — Paid national service.
- Coverage map: https://gnss.cropos.hr/Map/SensorMap.aspx
- Registration: https://www.cropos.hr/o-sustavu/120-cesta-pitanja

### Free international RTK correction services in Croatia

**RTK2GO** — Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, but not good for calibrated surveying applications.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/

**EUREF** — Free paneuropean low-density high-quality correction service.
- Coverage map: https://epncb.oma.be/_networkdata/data_access/real_time/map.php
- Registration: https://epncb.oma.be/_networkdata/data_access/real_time/

### Paid international correction services in Croatia

**u-blox PointPerfect Flex** — 1 centimeter RTK and 2-4 centimeter RTK-SSR accuracy. Starting from $5.90/month for up to 100 hours of use. Free 30-day trial available.

**Swift Navigation Skylark** — RTK from $69/month; RTK-SSR from $29/month for unlimited use. Free 6-month trial available.
