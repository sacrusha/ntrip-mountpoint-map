# Switzerland

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-switzerland/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **SWIPOS** — operator: Swisstopo — coverage: Switzerland
  - landing_url: https://www.swisstopo.admin.ch/de/swipos-gisgeo-fuer-rtk-und-postprocessing-anwendungen  [reachable: reachable]
  - access_url:  https://www.swisstopo.admin.ch/en/swipos-order-form  [reachable: reachable]
  - notes: Paid national service; registration may not be user-friendly
  - landing_url: https://shop.swipos.ch/Map/SensorMap.aspx  [reachable: reachable]

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
  - landing_url: https://epncb.oma.be/_networkdata/data_access/real_time/map.php  [reachable: unverified — HTTP 000]
  - access_url:  https://epncb.oma.be/_networkdata/data_access/real_time/  [reachable: unverified — HTTP 000]
  - notes: Free paneuropean low-density high-quality correction service

## Raw extract
### National RTK network in Switzerland

**SWIPOS** — Paid national service. Operated by Swisstopo.
- Landing: https://www.swisstopo.admin.ch/de/swipos-gisgeo-fuer-rtk-und-postprocessing-anwendungen
- Coverage map: https://shop.swipos.ch/Map/SensorMap.aspx
- Registration: https://www.swisstopo.admin.ch/en/swipos-order-form

### Free international RTK correction services in Switzerland

**RTK2GO** — Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, not for calibrated surveying.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/

**CENTIPEDE** — Free community-based network with high density.
- Coverage map: https://centipede.fr/index.php/view/map?repository=cent&project=centipede
- Registration: https://centipede.fr/

**EUREF** — Free paneuropean low-density high-quality correction service.
- Coverage map: https://epncb.oma.be/_networkdata/data_access/real_time/map.php
- Registration: https://epncb.oma.be/_networkdata/data_access/real_time/

### Paid international correction services in Switzerland

**u-blox PointPerfect Flex** — 1 centimeter RTK and 2-4 centimeter accuracy augmentation service (RTK-SSR). Starting from $5.90/month for up to 100 hours. Free 30-day trial available.

**Swift Navigation Skylark** — 1 cm RTK from $69/month; sub-decimeter RTK-SSR from $29/month for unlimited use. Free 6-month trial available.
