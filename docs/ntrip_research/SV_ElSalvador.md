# El Salvador [SV] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — active private NTRIP caster (Survey3G); no government caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (private commercial, subscription-based) |
| **Operator** | Survey3G (private company, San Miguel, El Salvador) |
| **Network name** | NTRIP SURVEY — El Salvador |
| **host:port — Survey3G** | not published; IP, port, username, password disclosed by email after subscription payment |
| **tariff — Survey3G** | USD 15 / 7 days · USD 30 / 15 days · USD 45 / 30 days · USD 135 / 3 months · USD 450 / 12 months (source: survey3g.com/servicios-de-ntrip/, observed 2026-05-06); El Salvador uses USD as official currency; no VAT stated |
| **hobbyist_eligibility** | Yes — subscription open to individuals; no professional licence required |
| **legal_residency_required** | No explicit requirement stated; appears to target El Salvador-based users but no residency gate on sign-up |
| **last_confirmed_alive** | survey3g.com/servicios-de-ntrip/ HTTP 200 on 2026-05-06; curl probe of survey3g.com:2101 not executable in this session (shell tools unavailable) |

## Most Recent Project Announcement

No formal government announcement. Survey3G describes itself as "pioneer in El Salvador" for NTRIP, operating continuously since launch. Tariffs are refreshed every 6 months at survey3g.com/ntrip/ (the /ntrip/ slug returned HTTP 404 on 2026-05-06; current pricing is at survey3g.com/servicios-de-ntrip/).

## Context Notes

- **Survey3G** (survey3g.com): A private geomatics company based in Residencial Obrajuelo, San Miguel, El Salvador. Distributes South, CHCNav, Topcon, and DWSitePro equipment and operates the only known national NTRIP correction network. The company brands itself as "el primer proveedor de NTRIP en El Salvador."
- **CORS stations (6):** SAN MIGUEL, PERKIN, LA UNION, SAN SALVADOR (UES, for research/education only — labeled temporary), SANTA ANA, COJUTE. Each station covers approximately 50 km radius; combined coverage claims ~90% of the national territory. Constellations: GPS + GLONASS + BeiDou + Galileo L1/L2/L5 at all stations.
- **Activation lead time:** New subscribers require 48 hours advance notice for configuration and testing; existing subscribers need 32 hours. Credentials are unique per subscription period (start/end dates). No automatic renewal.
- **Internet requirement:** Standard data connection required (promotional or capped packages may cause issues per operator policy).
- **Service interruptions:** Lost days from outages beyond operator control are added proportionally to the subscription at no cost.
- **Host:port:** Not disclosed publicly. Provided via email after subscription confirmation. Users configure IP, port, username, and password in their NTRIP client.
- **Connectivity test:** Available on request before purchase ("Si quieres realizar una prueba de conectividad, escríbenos").
- **No national government NTRIP caster found.** Centro Nacional de Registros (CNR) manages geodetic infrastructure but no publicly documented NTRIP stream was found.
- **SIRGAS-RT:** El Salvador appears in historical SIRGAS RT cooperation documents for Central America but no active SIRGAS-RT caster node for El Salvador was found in public registries.
- **Global commercial fallbacks:** Galileo HAS (~40 cm, no internet); GEODNET or Onocoy (coverage in El Salvador not confirmed); own base-station setup.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SIRGAS station data** (stations shared with SIRGAS) | https://sirgas.ipgh.org/en/gnss-network/stations/station-list/ | Free |
| **NOAA NGS CORS** (any shared El Salvador stations in NCN) | https://geodesy.noaa.gov/CORS/ | Free |

## Sources Consulted
- Survey3G services page: https://survey3g.com/servicios-de-ntrip/ — HTTP 200, tariff table confirmed 2026-05-06
- Survey3G homepage: https://survey3g.com/ — company address, contact info, equipment brands confirmed 2026-05-06
- Survey3G NTRIP policy: https://survey3g.com/politicas-de-servicios-ntrip/ — activation rules, coverage, service interruption policy confirmed 2026-05-06
- Survey3G NTRIP page: https://survey3g.com/ntrip/ — HTTP 404 on 2026-05-06 (pricing no longer at this URL)
- curl probe of `survey3g.com:2101` — not executable: shell tools unavailable in this session
- SIRGAS-RT bulletins (sirgas.ipgh.org)
- rtcm-ntrip.org (no El Salvador entries found)
- ArduSimple El Salvador page (no dedicated page found)
