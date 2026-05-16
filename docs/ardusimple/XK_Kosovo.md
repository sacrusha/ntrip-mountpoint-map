# Kosovo

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kosovo/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **KOPOS** — operator: Kosovo government — coverage: Kosovo
  - landing_url: https://kopos.rks-gov.net/  [reachable: reachable]
  - access_url:  https://kopos.rks-gov.net/SBC/Account/Register  [reachable: reachable]
  - notes: Paid national service; registration required via website or email

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

- **EUREF** — operator: pan-European — coverage: Europe
  - landing_url: https://epncb.oma.be/_networkdata/data_access/real_time/map.php  [reachable: unverified — HTTP 000]
  - access_url:  https://epncb.oma.be/_networkdata/data_access/real_time/  [reachable: unverified — HTTP 000]
  - notes: Free paneuropean low-density high-quality correction service

## Raw extract
### National RTK network in Kosovo

Many countries, including Kosovo, have established their own National RTK Networks. In order to access real-time services, you will need to register on the website or send them an email to get your NTRIP credentials. Their website may not be very user-friendly.

**KOPOS** — Paid national service.
- Landing: https://kopos.rks-gov.net/
- Registration: https://kopos.rks-gov.net/SBC/Account/Register

### Free international RTK correction services in Kosovo

**RTK2GO** — Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, but not good for calibrated surveying.
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

### Paid international correction services in Kosovo

**u-blox PointPerfect Flex** — 1 cm RTK and 2-4 cm RTK-SSR accuracy. Starting from $5.90/month for up to 100 hours. Free 30-day trial available.
