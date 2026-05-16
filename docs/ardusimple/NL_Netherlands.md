# Netherlands

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-netherlands/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **NETPOS** — operator: NSGI (Netherlands Geographical and Cadastral Service) — coverage: Netherlands
  - landing_url: https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/stationsinformatie  [reachable: reachable]
  - access_url:  https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams  [reachable: reachable]
  - notes: Free national service

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

- **CENTIPEDE** — operator: INRAE/community — coverage: Europe
  - landing_url: https://centipede.fr/index.php/view/map?repository=cent&project=centipede  [reachable: reachable]
  - access_url:  https://centipede.fr/  [reachable: reachable]
  - host:port: caster.centipede.fr:2101
  - notes: Free community RTK network; mostly France with European coverage

- **EUREF** — operator: EUREF/BKG — coverage: Europe
  - landing_url: https://epncb.oma.be/_networkdata/data_access/real_time/map.php  [reachable: unverified — HTTP 000]
  - access_url:  https://igs.bkg.bund.de/ntrip/register  [reachable: reachable]
  - notes: Free European reference network; academic/geodetic use

## Raw extract
### National RTK network in Netherlands

**NETPOS** — Free national service operated by NSGI.
- Coverage map: https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/stationsinformatie
- Registration: https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams

### Free international RTK correction services in Netherlands

**RTK2GO** — Free global community based correction network without quality of service.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/

**CENTIPEDE** — Free community RTK network.
- Coverage map: https://centipede.fr/index.php/view/map?repository=cent&project=centipede
- Registration: https://centipede.fr/

**EUREF** — Free European reference network.
- Status: https://epncb.oma.be/_networkdata/data_access/real_time/map.php
- Registration: https://igs.bkg.bund.de/ntrip/register

### Paid international correction services in Netherlands

**u-blox PointPerfect Flex** — 1 centimeter RTK and 2-4 centimeter RTK-SSR. Starting from $5.90/month for up to 100 hours. Free 30-day trial available.

**Swift Navigation Skylark** — Centimeter-level RTK correction service. $69/month for RTK, $29/month for RTK-SSR. Free 6-month trial available.
