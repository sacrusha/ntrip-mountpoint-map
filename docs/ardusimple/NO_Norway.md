# Norway

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-norway/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **CPOS** — operator: Kartverket (Norwegian Mapping Authority) — coverage: Norway
  - landing_url: https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos  [reachable: reachable]
  - notes: Paid national service; free for research organizations and students

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

- **CENTIPEDE** — operator: community-based — coverage: Europe (high density)
  - landing_url: https://centipede.fr/index.php/view/map?repository=cent&project=centipede  [reachable: reachable]
  - access_url:  https://centipede.fr/  [reachable: reachable]
  - notes: Free community-based network with high density

- **EUREF** — operator: pan-European — coverage: Europe
  - landing_url: https://epncb.oma.be/_networkdata/data_access/real_time/map.php  [reachable: unverified — curl exit 0 with HTTP 000, likely TLS/connection issue]
  - access_url:  https://epncb.oma.be/_networkdata/data_access/real_time/  [reachable: unverified — curl exit 0 with HTTP 000, likely TLS/connection issue]
  - notes: Free paneuropean low-density high-quality correction service

## Raw extract
### National RTK network in Norway

**CPOS** — Paid national service; free for research organizations and students.
- Guide: https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos
- Coverage map: https://norgeskart.no/?test=1&_ga=2.95277916.1996222763.1597000894-2085064561.1573565451#!?project=Fastmerker&layers=1005,1018,1019&zoom=4&lat=7197864.00&lon=396722.00&panel=searchOptionsPanel

### Free international RTK correction services in Norway

**RTK2GO** — Free global community based correction network without quality of service. It is good enough for pass-to-pass centimeter accuracy, but not good for calibrated surveying applications.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (formerly UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/

**CENTIPEDE** — Free community-based network with high density.
- Coverage map: https://centipede.fr/index.php/view/map?repository=cent&project=centipede
- Registration: https://centipede.fr/

**EUREF** — Free paneuropean low-density high-quality correction service.
- Coverage map: https://epncb.oma.be/_networkdata/data_access/real_time/map.php
- Registration: https://epncb.oma.be/_networkdata/data_access/real_time/

### Paid international correction services in Norway

**u-blox PointPerfect Flex** — 1 cm RTK and 2-4 cm RTK-SSR accuracy. Starting from $5.90/month for up to 100 hours of use. Free 30-day trial available.

**Swift Navigation Skylark** — RTK from $69/month; RTK-SSR from $29/month for unlimited use. Free 6-month trial available.
