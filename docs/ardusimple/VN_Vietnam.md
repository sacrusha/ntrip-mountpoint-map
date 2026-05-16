# Vietnam

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-vietnam/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **VNGEONET** — operator: Vietnamese national authority — coverage: Vietnam
  - landing_url: https://gddt.vngeonet.vn/huong-dan-cung-cap/pham-vi-thu-phi-rtk  [reachable: unverified — HTTP 000 / DNS fail]
  - access_url:  https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-tao-tai-khoan-sbc?culture=en-US  [reachable: unverified — HTTP 000 / DNS fail]
  - notes: Paid national service; registration may be difficult

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

## Raw extract
### National RTK network in Vietnam

**VNGEONET** — Paid national service. Registration may be difficult.
- Coverage map: https://gddt.vngeonet.vn/huong-dan-cung-cap/pham-vi-thu-phi-rtk
- Registration: https://gddt.vngeonet.vn/huong-dan-cung-cap/huong-dan-tao-tai-khoan-sbc?culture=en-US

### Free international RTK correction services in Vietnam

If you only need pass-to-pass accuracy, social-based RTK networks are the cheapest way to go. There are also free global correction services available in Vietnam. RTK only works up to 35-50 km.

**RTK2GO** — Free global community based correction network without quality of service. Good enough for pass-to-pass centimeter accuracy, not for calibrated surveying.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/
