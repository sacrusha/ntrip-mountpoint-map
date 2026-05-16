# Kenya

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kenya/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **Muya CORS** — operator: not specified — coverage: Kenya
  - landing_url: https://muya-cors.com/map  [reachable: reachable]
  - access_url:  https://muya-cors.com/services?group=rtk_corrections  [reachable: reachable]
  - notes: Paid private service

- **RTK2GO** — operator: community-based — coverage: global
  - landing_url: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101  [reachable: reachable]
  - access_url:  http://rtk2go.com/  [reachable: reachable]
  - host:port: rtk2go.com:2101
  - notes: Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, but not good for calibrated surveying applications.

- **IGS** — operator: International GNSS Service — coverage: global
  - landing_url: https://network.igs.org/  [reachable: reachable]
  - access_url:  https://register.rtcm-ntrip.org/cgi-bin/registration.cgi  [reachable: reachable]
  - notes: Free global low density high quality correction service

- **Earthscope (previously UNAVCO)** — operator: Earthscope/UNAVCO — coverage: global
  - landing_url: https://www.unavco.org/instrumentation/networks/status/nota  [reachable: reachable]
  - access_url:  https://www.earthscope.org/data/gnss-realtime/  [reachable: reachable]
  - notes: Free (for non-commercial use) global low-density high-quality correction service

## Raw extract
### National RTK network in Kenya

Many countries, including Kenya, have established their own National RTK Networks to support various high-precision GNSS applications within their borders. In order to access real-time services, you will need to register on the website or send them an email to get your NTRIP credentials. However, their website may not be very user-friendly, so navigating the registration process might take some effort.

**Muya CORS** — Paid private service
- Coverage map: https://muya-cors.com/map
- Registration: https://muya-cors.com/services?group=rtk_corrections

### Free international RTK correction services in Kenya

If you only need pass-to-pass accuracy, and you don't need to compare your measurements with local maps done by other companies, social-based RTK networks are the cheapest way to go. There are also free global correction services with calibrated base stations which are available in Kenya. You can use them to achieve centimeter-level accuracy if you are lucky to have a base station close to you (remember that RTK only works up to 35-50 km).

**RTK2GO** — Free global community based correction network without quality of service. It is good enough for pass-to-pass centimeter accuracy, but not good for calibrated surveying applications. To view the RTK2GO coverage map, open the page and click 'View all' on the top right.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/
