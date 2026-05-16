# Greece

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-greece/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **HEPOS** — operator: Greek national service (Hellenic Cadastre) — coverage: Greece
  - landing_url: https://www.ktimatologio.gr/pliroforiako-yliko/geoxorika/43  [reachable: auth-required]
  - access_url:  https://www.ktimatologio.gr/pliroforiako-yliko/geoxorika/43  [reachable: auth-required]
  - notes: Paid national service; registration required via website or email

- **RTK2GO** — operator: community-based — coverage: global
  - landing_url: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101  [reachable: reachable]
  - access_url:  http://rtk2go.com/  [reachable: reachable]
  - host:port: rtk2go.com:2101
  - notes: Free global community based correction network without quality of service. Pass-to-pass centimeter accuracy, not for calibrated surveying.

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
### National RTK network in Greece

**HEPOS** — Paid national service. Registration required via website or email.
- Landing/Registration: https://www.ktimatologio.gr/pliroforiako-yliko/geoxorika/43

### Free international RTK correction services in Greece

**RTK2GO** — Free global community based correction network without quality of service. Pass-to-pass centimeter accuracy, but not good for calibrated surveying.
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

### Paid international correction services in Greece

**u-blox PointPerfect Flex** — 1 cm RTK and 2-4 cm RTK-SSR accuracy. Starting from $5.90/month for up to 100 hours. Free 30-day trial available.
