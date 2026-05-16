# Bosnia and Herzegovina

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bosnia-and-herzegovina/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **FBiHPOS** — operator: Bosnia and Herzegovina (national) — coverage: Bosnia and Herzegovina
  - landing_url: http://fbihpos.katastar.ba/SBC/Admin  [reachable: reachable]
  - access_url:  http://fbihpos.katastar.ba/SBC/Account/Register  [reachable: reachable]
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
### National RTK network in Bosnia and Herzegovina

Many countries, including Bosnia and Herzegovina, have established their own National RTK Networks to support various high-precision GNSS applications within their borders. In order to access real-time services, you will need to register on the website or send them an email to get your NTRIP credentials. However, their website may not be very user-friendly, so navigating the registration process might take some effort.

**FBiHPOS** — Paid national service.
- Coverage map: http://fbihpos.katastar.ba/SBC/Admin
- Registration: http://fbihpos.katastar.ba/SBC/Account/Register

### Free international RTK correction services in Bosnia and Herzegovina

If you only need pass-to-pass accuracy, and you don't need to compare your measurements with local maps done by other companies, social-based RTK networks are the cheapest way to go. There are also free global correction services with calibrated base stations which are available in Bosnia and Herzegovina. You can use them to achieve centimeter-level accuracy if you are lucky to have a base station close to you (remember that RTK only works up to 35-50 km).

**RTK2GO** — Free global community based correction network without quality of service. It is good enough for pass-to-pass centimeter accuracy, but not good for calibrated surveying applications.
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

### Paid international correction services in Bosnia and Herzegovina

**u-blox PointPerfect Flex** — 1 centimeter RTK and 2-4 centimeter accuracy augmentation service (RTK-SSR) starting from $5.90/month for up to 100 hours of use. Free 30-day trial available.
