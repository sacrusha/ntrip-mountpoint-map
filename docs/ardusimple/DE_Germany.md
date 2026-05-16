# Germany

source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-germany/
fetched: 2026-05-16
fetch_passes: 1

## Networks (as listed by ardusimple)
- **SAPOS** — operator: AdV / state surveying authorities — coverage: Germany (16 state networks, most free)
  - notes: Decentralized national network; each German state runs its own SAPOS endpoint. Most states offer free service; some (Bavaria, Baden-Württemberg, Rhineland-Palatinate, Mecklenburg-Western Pomerania) charge. See per-state details below.

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

- **EUREF** — operator: EUREF/BKG — coverage: Europe
  - landing_url: https://epncb.oma.be/_networkdata/data_access/real_time/map.php  [reachable: unverified — HTTP 000]
  - access_url:  https://igs.bkg.bund.de/ntrip/register  [reachable: reachable]
  - notes: Free European reference network; academic/geodetic use

## Raw extract
### National RTK network in Germany

**SAPOS** — Germany's national CORS network, operated per-state by state surveying authorities (AdV coordination). Most states free; some paid.

State endpoints:
- Baden-Württemberg (LGL): map https://gpps-web.sapos-bw.de/karte.php — reg https://www.lgl-bw.de/Produkte/Satellitenpositionierungsdienst/ — paid
- Bavaria (LDBV): map https://sapos.bayern.de/refmap.php — reg https://sapos.bayern.de/register.php — paid
- Berlin (SenSBW): reg https://www.berlin.de/sen/sbw/.../sapos/ — free
- Brandenburg (LGB): map https://www.geobasis-bb.de/.../sapos-referenzstationen/ — reg https://www.geobasis-bb.de/.../sapos-anmeldeformular/ — free
- Hamburg (LGV): map https://sapos.geonord.de/stationskarte — reg https://sapos.geonord.de/registrierung/Formular.html — free
- Hesse (HVBG): map https://sapos.hvbg.hessen.de/refmap.php — reg https://sapos.hvbg.hessen.de/service.php — free
- Mecklenburg-Western Pomerania (LAIV-MV): reg https://www.laiv-mv.de/Geoinformation/Raumbezug/ — paid
- Lower Saxony & Bremen (LGLN): reg https://lgln-geodaten.niedersachsen.de/sapos/ — free
- North Rhine-Westphalia (NRW): map https://gppspro.saposnrw.de/refmap.php — reg https://registrierung.saposnrw.de/ — free
- Rhineland-Palatinate (LVermGeo): reg https://lvermgeo.rlp.de/.../heps-anmeldung — paid
- Saarland (LVGL): reg https://www.saarland.de/lvgl/.../sapos.html — free
- Saxony (GeoSN): map https://landesvermessung.sachsen.de/.../refmap_sn.php — reg https://landesvermessung.sachsen.de/.../anmeldung.php — free
- Saxony-Anhalt (LVermGeo ST): reg https://lvermgeo.sachsen-anhalt.de/.../heps-korrekturdatenabgabe.html — free
- Schleswig-Holstein (LVermGeoSH): map https://sapos.geonord.de/stationskarte — reg https://sapos.geonord.de/registrierung/Formular.html — free
- Thuringia (TLBG): map https://sapos.thueringen.de/karte.php — reg https://sapos.thueringen.de/anmeldung.php — free

### Free international RTK correction services in Germany

**RTK2GO** — Free global community based correction network without quality of service.
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

### Paid international correction services in Germany

**u-blox PointPerfect Flex** — 1 centimeter RTK and 2-4 centimeter RTK-SSR. Starting from $5.90/month for up to 100 hours. Free 30-day trial available.

**Swift Navigation Skylark** — Centimeter-level RTK correction service. $69/month for RTK, $29/month for RTK-SSR. Free 6-month trial available.
