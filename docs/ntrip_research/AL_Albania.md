# Albania [AL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (originally 2026-05-06)

## Status: YES — two GNSS RTK networks active (ALBCORS / ASIG state network + SATNET LIVE / Land&Co commercial)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — ALBCORS (state, ASIG) and SATNET LIVE (commercial, Land&Co / Topcon) |
| **host:port** | ALBCORS: krgjsh.asig.gov.al (port not confirmed publicly; contact info.albcors@asig.gov.al). SATNET LIVE: provided after registration via landcoal.com or SATNET app. |
| **tariff** | ALBCORS: unknown — state service, likely subsidized or low-cost for licensed surveyors. SATNET LIVE: commercial; 3 free days for new users; free for 1 year with Land&Co GPS equipment purchase. Ongoing rate not published. |
| **hobbyist_eligibility** | ALBCORS: Unclear — application form (ASIG_Formulari-i-aplikimit-ALBCORS) required; professional context implied. SATNET LIVE: Unclear — open registration via mobile app suggests broader access. |
| **legal_residency_required** | Unclear for both |
| **last_confirmed_alive** | krgjsh.asig.gov.al confirmed live (2026-05-06); landcoal.com confirmed live (2026-05-06) |

## Most Recent Project Announcement

**ALBCORS** is the state GNSS CORS network operated by the State Authority for Geospatial Information (ASIG — Autoriteti Shtetëror për Informacionin Gjeohapësinor). It comprises 27 CORS stations (21 ground-mounted concrete blocks + 6 roof-type stations integrated from the former ALBPOS system) with a control center at ASIG premises in Tirana. A 2023 EUREF Gothenburg symposium presentation (EUREF, 2023-Gothenburg) confirmed Albania's geodetic reference frame and ALBCORS operational status.

The predecessor ALBPOS system was found non-compliant with national CORS standards in 2015; ALBCORS was built as a replacement. Contact: info.albcors@asig.gov.al.

**SATNET LIVE ALBANIA** is a commercial RTK CORS network service offered by Land&Co (Topcon Albania distributor, landcoal.com, Tirana). It is also accessible via the "SATNET live" mobile application (available on App Store).

## Context Notes

- **ALBCORS host**: The GNSS network subdomain is krgjsh.asig.gov.al (KRGJSH = Kontrolli i Rrjetit Gjeodezik dhe Shërbimeve Hartografike). The precise NTRIP caster hostname and port are not published openly; the application form (PDF linked from krgjsh.asig.gov.al) must be submitted to ASIG.
- **ALBCORS ETRS89**: The network is aligned to ETRS89 European reference frame, supporting future EU-compatible surveying standards (Albania is an EU candidate country).
- **SATNET LIVE**: Land&Co is the Topcon distributor in Albania and uses the Topnet Live / SATNET platform. Customers who purchase GPS/GNSS equipment from Land&Co get 1 year free RTK access. New registrations get 3 free days. Ongoing subscription pricing is not published on the website; contact Land&Co directly.
- **Topnet Live network**: It is possible that SATNET LIVE Albania feeds into or partners with Topnet Live's European coverage — exact relationship not confirmed.
- **Coverage**: ALBCORS 27 stations for a country of ~29 000 km² — reasonable density. SATNET LIVE coverage area not precisely documented.
- **Practical workaround**: Apply for ALBCORS at krgjsh.asig.gov.al, or register for SATNET LIVE via landcoal.com / SATNET app.
- **Volunteer / community**: zero AL mountpoints on rtk2go; zero AL nodes on Centipede; zero EarthScope. Confirmed via `scripts/stations_by_country.py ALB` (no entries) and `scripts/stations_by_radius.py 41.15 20.17 50` (no stations within 50 km of Tirana area) on 2026-05-12.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **ASIG / ALBCORS** — RINEX data for registered users | https://krgjsh.asig.gov.al | Contact ASIG |
| **EUREF Permanent GNSS Network** — regional stations near Albania | https://epncb.oma.be/ | Free (account required) |
| **ASIG Geoportal** — national spatial data | https://geoportal.asig.gov.al | Free (account required) |

## Sources Consulted
- ASIG GNSS network (ALBCORS) page and application form: https://krgjsh.asig.gov.al/?page_id=1218&lang=en
- ASIG State Authority for Geospatial Information home: https://asig.gov.al/en/home/
- Land&Co SATNET LIVE service page: https://landcoal.com/satnet_live_rtk_cors_network
- EUREF Symposium 2023 Gothenburg — Albania presentation (ASIG / Lasku): http://www.euref.eu/sites/default/files/symposia/2023Gothenburg/04-01-Albania.pdf
- Wikipedia — State Authority for Geospatial Information (Albania): https://en.wikipedia.org/wiki/State_Authority_for_Geospatial_Information
- SpringerLink — "Development of Classical and Modern Geodetic Reference Systems of Albania" (2023): https://link.springer.com/book/10.1007/978-3-031-25366-9
- LinkedIn — "The Role and Contribution of Geodetic Reference Frame to the NSDI in Albania" (Arian Lasku)
- ResearchGate — "Coordinate Reference Systems Used in Albania to Date"
- ResearchGate — "Albanian National GNSS map" figure
- ArduSimple country selector — no dedicated Albania page found
- RTK2go monitor (monitor.use-snip.com) — no Albania NTRIP streams confirmed
