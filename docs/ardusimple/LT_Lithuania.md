# Lithuania

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-lithuania/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **LSB (LitPOS)** — operator: Lithuanian national service — coverage: Lithuania
  - landing_url: https://www.geoportal.lt/geoportal/web/litpos-paslauga  [reachable: reachable]
  - access_url:  https://www.geoportal.lt/geoportal/web/litpos-paslauga/registracija  [reachable: reachable]
  - notes: Free national service; registration required

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

- **EUREF** — operator: EUREF/BKG — coverage: Europe
  - landing_url: https://epncb.oma.be/_networkdata/data_access/real_time/map.php  [reachable: unverified — HTTP 000]
  - access_url:  https://igs.bkg.bund.de/ntrip/register  [reachable: reachable]
  - notes: Free European reference network; academic/geodetic use

## Raw extract
### National RTK network in Lithuania

**LSB (LitPOS)** — Free national service.
- Coverage map: https://www.geoportal.lt/geoportal/web/litpos-paslauga
- Registration: https://www.geoportal.lt/geoportal/web/litpos-paslauga/registracija

### Free international RTK correction services in Lithuania

**RTK2GO** — Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, not good for calibrated surveying applications.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/

**EUREF** — Free European reference network.
- Status: https://epncb.oma.be/_networkdata/data_access/real_time/map.php
- Registration: https://igs.bkg.bund.de/ntrip/register

### Paid international correction services in Lithuania

**u-blox PointPerfect Flex** — 1 centimeter RTK and 2-4 centimeter RTK-SSR. Starting from $5.90/month for up to 100 hours. Free 30-day trial available.
