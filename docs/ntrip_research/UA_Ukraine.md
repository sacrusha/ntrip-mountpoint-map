# Ukraine [UA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — multiple commercial NTRIP casters operational; war conditions affect eastern infrastructure; no free government tier

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (commercial) |
| **Operator 1 — System.NET (gnss.org.ua)** | Commercial (Leica GNSS Spider); `gnss.org.ua:2101` — confirmed alive via SOURCETABLE 2026-05-06 |
| **Operator 2 — Kyivstar mAgri.RTK** | Commercial (Trimble Pivot Platform); `rtk.kyivstar.ua:2101` — confirmed alive via SOURCETABLE 2026-05-06 |
| **Operator 3 — ZAKPOS (zakpos.zakgeo.com.ua)** | Commercial; `zakpos.zakgeo.com.ua:2102` (IP: 185.68.16.164:2102) — timed out 2026-05-06 |
| **VRS** | Yes — both System.NET (vrs mountpoint) and Kyivstar (VRS, Nearest_MSM5/7) offer VRS |
| **tariff — Kyivstar mAgri.RTK GEO 365** | UAH 17,700/year (~USD 430 at 2026 rates) |
| **tariff — Kyivstar mAgri.RTK GEO 30** | UAH 5,550/month |
| **tariff — Kyivstar mAgri.RTK GEO 7** | UAH 1,800/7 days |
| **tariff — Kyivstar mAgri.RTK GEO 1** | UAH 450/day |
| **tariff — Kyivstar mAgri.RTK Try&Buy** | UAH 2 (7 days trial) |
| **tariff — System.NET annual** | ~UAH 47,000–50,000/year (approximately USD 1,150 at 2026 rates) — from rtk-navigation.com article |
| **VAT** | Ukraine VAT is 20%; Kyivstar pricing not confirmed excl./incl. VAT — verify at checkout |
| **hobbyist_eligibility** | Yes — Kyivstar mAgri.RTK is available to any Kyivstar contract subscriber; individual subscriptions available; System.NET requires account registration |
| **legal_residency_required** | Unclear — Kyivstar requires a Kyivstar mobile contract (Ukrainian carrier); foreign payment may be difficult given wartime context |
| **last_confirmed_alive** | `gnss.org.ua:2101` SOURCETABLE 200 OK on 2026-05-06; `rtk.kyivstar.ua:2101` SOURCETABLE 200 OK on 2026-05-06 |

## Sourcetable Observations (2026-05-06)

**gnss.org.ua:2101 (System.NET)** — Leica GNSS Spider 7.11.1.109; 4 mountpoints: `autom`, `nearest`, `imax`, `vrs` (GPS+GLO+GAL+BDS for vrs); coordinates anchored ~51.52°N 30.75°E (near Kyiv). Content-Length 366 bytes — small public sourcetable; production mountpoints behind auth.

**rtk.kyivstar.ua:2101 (Kyivstar)** — Trimble Ntrip Caster 5.2; 14+ mountpoints including: `VRS` (RTCM3Net), `VRS_old` (RTCM 3.1), `Nearest_MSM5`, `Nearest_MSM7`, `Nearest` (RTCM 3.4 MSM4), `UCS2000_5z`, `UCS2000_6z`, `MSK_80`, `MSK_05`, `MSK_07`, `MSK_12`, `MSK_14`, `MSK_18`, `MSK_21` — multi-coordinate system outputs; GPS+GLO+GAL+BDS+QZS. 97 base stations (Trimble equipment; nationwide). 

## Context Notes

- **War conditions (Russia-Ukraine war, since 2022-02-24):** Eastern and southeastern Ukrainian territory is occupied or contested; CORS stations in those regions are non-operational or inaccessible. Western Ukraine (Lviv, Uzhhorod) casters remain operational. Kyivstar (97 stations, Trimble + xFill Premium) claims nationwide monitoring with backup channels.
- **System.NET / gnss.org.ua:** Swiss-Ukrainian joint venture using Leica Geosystems GNSS Spider; 320+ integrated stations; ~3,000 users; 2 cm accuracy; annual pricing ~47,000 UAH.
- **Kyivstar mAgri.RTK:** Operated by Kyivstar (Ukraine's largest mobile operator, now majority Veon-owned); 97 RTK base stations on Trimble equipment with 24/7 monitoring; uses xFill Premium for signal continuity. mAgri.RTK 365 StarLink variant integrates Starlink for connectivity in areas with unstable mobile networks. Service available to Kyivstar business contract subscribers. Targeted at agriculture and geodesy.
- **ZAKPOS** (`zakpos.zakgeo.com.ua:2102`): Operated by Zakgeo in Zakarpattia (western Ukraine). Timed out from external IP on 2026-05-06 — may be temporarily down or IP-restricted.
- No free government GNSS NTRIP service; pre-war State Geodetic Survey of Ukraine (DGSZU) service not confirmed operational.
- UAH/USD exchange rate at time of research: approximately UAH 41–42 per USD (May 2026 estimate; wartime rates volatile).
- No rtk2go or Centipede volunteer bases found for Ukraine.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **System.NET RINEX archive** | https://gnss.org.ua | Via account; pricing unclear |
| **IGS/EPN stations in Ukraine** — limited | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- System.NET / gnss.org.ua: http://gnss.org.ua (SOURCETABLE confirmed 2026-05-06)
- Kyivstar mAgri.RTK product page: https://kyivstar.ua/business/products/geodesiya (observed 2026-05-06)
- Kyivstar mAgri.RTK pricing: https://gpsgeometer.com/en/products/magri.rtk-365-by-kyivstar-high-precision-signal-for-gnss-rtk-equipment-starlink (observed 2026-05-06)
- Ukraine RTK network stability article: https://www.rtk-navigation.com/en/background-information/chi-pratsyuyut-ukrainski-ta-evropejski-rtk-merezhi-stabilno-po-vsij-teritorii-polya-chi-chasto-buvayut-rozrivi (observed 2026-05-06)
- ZAKPOS portal: http://zakpos.zakgeo.com.ua/ (redirect loop 2026-05-06)
- Trimble/Kyivstar RTK partnership: https://www.terradaily.com/reports/Trimble_and_Kyivstar_to_provide_GNSS_correction_services_in_Ukraine_999.html
- ArduSimple Ukraine page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-ukraine/ (observed 2026-05-06; incorrectly states no national network — outdated)
- curl probe of `gnss.org.ua:2101` — SOURCETABLE 200 OK on 2026-05-06
- curl probe of `rtk.kyivstar.ua:2101` — SOURCETABLE 200 OK on 2026-05-06
- curl probe of `zakpos.zakgeo.com.ua:2102` (185.68.16.164:2102) — timed out 2026-05-06
