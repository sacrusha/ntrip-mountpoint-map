# Canada

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-canada/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **Quebec Geodetic Network** — operator: MRNF (Ministère des Ressources naturelles et des Forêts) — coverage: Quebec (Canada, regional)
  - landing_url: https://vgo.portailcartographique.gouv.qc.ca/mobile.aspx  [reachable: reachable]
  - access_url:  https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/  [reachable: reachable]
  - notes: Free regional service; GNSS station data for post-processing (no real-time NTRIP stream)

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

## Raw extract
### National RTK network in Canada

**Quebec Geodetic Network** — Free GNSS station network for post-processing operated by MRNF. No real-time NTRIP service.
- Coverage map: https://vgo.portailcartographique.gouv.qc.ca/mobile.aspx
- Registration: https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/

### Free international RTK correction services in Canada

**RTK2GO** — Free global community based correction network without quality of service.
- Coverage map: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Registration: http://rtk2go.com/

**IGS** — Free global low density high quality correction service.
- Coverage map: https://network.igs.org/
- Registration: https://register.rtcm-ntrip.org/cgi-bin/registration.cgi

**Earthscope (previously UNAVCO)** — Free (for non-commercial use) global low-density high-quality correction service.
- Coverage map: https://www.unavco.org/instrumentation/networks/status/nota
- Registration: https://www.earthscope.org/data/gnss-realtime/

### Paid international correction services in Canada

**Swift Navigation Skylark** — Centimeter-level RTK correction service. $69/month for RTK, $29/month for RTK-SSR. Free 6-month trial available.
