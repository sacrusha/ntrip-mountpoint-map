# Latvia [LV] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free government NTRIP caster (LatPos) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (LatPos — free since 2018) |
| **host:port — LatPos** | `latpos.lgia.gov.lv:5001` (IP: 91.216.2.20) |
| **VRS** | Yes — network RTK corrections; 27 Latvian + 5 Estonian + 4 Lithuanian base stations enable network-level solution |
| **tariff** | Free — explicit free-access policy in force since 2018 |
| **hobbyist_eligibility** | yes — any user may register; no professional licensing stated |
| **legal_residency_required** | unclear — not explicitly required; free public service with registration |
| **last_confirmed_alive** | `latpos.lgia.gov.lv:5001` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl verified) |

## Context Notes

- **LatPos**: Permanent GNSS reference station network operated by the Latvian Geospatial Information Agency (LGIA / Latvijas Ģeotelpiskās informācijas aģentūra). Made free to all registered users in 2018.
- **Infrastructure**: 27 base stations in Latvia, 5 in Estonia, 4 in Lithuania operating continuously. Distributes corrections via mobile internet (GPRS/UMTS/4G). Signals from GPS, GLONASS, Galileo, BeiDou.
- **Real-time accuracy**: ~2 cm horizontal in real-time; ~5 mm in post-processing.
- **Access**: Registration required via the LatPos SBC (Spider Business Center) portal. Users must accept LatPos terms of use before account activation. Portal navigation reportedly not user-friendly.
- **Note from country-survey.md**: In CI, latpos.lgia.gov.lv port 5001 had been timing out (suspected egress firewall on non-standard port from some external networks); the caster responded on 2026-05-06 from this research environment.
- **Operator contact**: LGIA, Rīga; https://www.lgia.gov.lv/en

## Post-Processing (RINEX) Fallback

RINEX data available via LatPos portal at no cost after registration.

## Sources Consulted
- LatPos page (LGIA): https://www.lgia.gov.lv/en/latpos
- Alberding caster map (LatPos): https://www.alberding.eu/cgi-bin/map.cgi?caster=latpos.lgia.gov.lv&port=5001&lang=en&gencgi=1
- ArduSimple Latvia RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-latvia/
- Inside GNSS article on LatPos free access: https://insidegnss.com/latvias-latpos-network-consolidates-free-access-and-operational-resilience/
- curl probe of `latpos.lgia.gov.lv:5001` — SOURCETABLE 200 OK confirmed 2026-05-06
