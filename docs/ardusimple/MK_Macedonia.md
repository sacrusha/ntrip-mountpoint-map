# Macedonia (North Macedonia)

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-macedonia/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **MAKPOS** — operator: Macedonia national (State Geodetic Authority) — coverage: Macedonia
  - landing_url: http://makpos.katastar.gov.mk/  [reachable: unverified — HTTP 000]
  - access_url:  https://makpos.katastar.gov.mk/SBC/Account/Register  [reachable: unverified — HTTP 000]
  - notes: Paid national service

- **RTK2GO** — operator: community-based — coverage: global
  - landing_url: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101  [reachable: reachable]
  - access_url:  http://rtk2go.com/  [reachable: reachable]
  - host:port: rtk2go.com:2101
  - notes: Free global community based correction network without quality of service. Pass-to-pass accuracy only.

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
### National RTK network in Macedonia

Many countries, including Macedonia, have established their own National RTK Networks. In order to access real-time services, you will need to register on the website or send them an email to get your NTRIP credentials.

**MAKPOS** — Paid national service.
- Coverage map: http://makpos.katastar.gov.mk/
- Registration: https://makpos.katastar.gov.mk/SBC/Account/Register

### Free international RTK correction services in Macedonia

If you only need pass-to-pass accuracy, social-based RTK networks are the cheapest way to go. RTK only works up to 35-50 km.

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

### Paid international correction services in Macedonia

**u-blox PointPerfect Flex** — 1 centimeter RTK and 2-4 centimeter accuracy augmentation service (RTK-SSR) starting from $5.90/month for up to 100 hours. Free 30-day trial available.
