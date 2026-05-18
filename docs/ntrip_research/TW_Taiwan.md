# Taiwan [TW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-13 entry; no change — caster still externally unreachable, IP geo-block persists)

## Status: YES — paid national NTRIP (e-GNSS / MOI NLSC); likely IP-restricted from outside Taiwan; day-rate pricing in TWD

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | NLSC (National Land Surveying and Mapping Center), Ministry of the Interior (MOI), R.O.C. (Taiwan) |
| **Service name** | e-GNSS Real-time Positioning System |
| **landing_url** | `https://www.nlsc.gov.tw/en/cp.aspx?n=2128` — NLSC English service page; describes e-GNSS, 78-station footprint, and points to the registration portal. |
| **access_url** | `https://egnss.nlsc.gov.tw` — operator registration / fee portal (Chinese-primary, English-language pages available); creates the account and 5-year permit needed to obtain NTRIP credentials. |
| **host:port** | `210.241.63.193:81` (primary published IP; timed out from external IP on 2026-05-06) |
| **num_stations** | 78 physical CORS nationwide (NLSC English service page, 2026-05-17). 4 of the 78 are also IGS stations. Sourcetable not externally probable from sandbox (geo-block) so per-MP enumeration unavailable; rely on operator-declared figure. |
| **VRS** | Yes — VBS-RTK (Virtual Base Station Real-Time Kinematic) |
| **Constellations** | GPS+GLONASS; selected stations also BeiDou+Galileo |
| **Number of reference stations** | 78 online real-time service base stations nationwide |
| **tariff — permit** | TWD 2,000 per 5-year application permit (~USD 62 at 2026 rates) |
| **tariff — daily use fee** | TWD 300/day (~USD 9.30/day at 2026 rates) |
| **VAT** | Taiwan does not apply VAT (business tax) to government GNSS service fees; confirm at registration |
| **hobbyist_eligibility** | Unclear — registration requires government permit application process; foreign individuals not explicitly excluded but practical access path unclear |
| **legal_residency_required** | Unclear — caster timed out from external IP during research, suggesting possible IP restriction or geoblocking |
| **last_confirmed_alive** | Direct caster probes of `210.241.63.193:81` + `:2101` timed out from non-Taiwan sandbox on 2026-05-06, 2026-05-13, 2026-05-17 (10-day persistent timeout consistent with IP geo-block or firewalled-to-authenticated-users behaviour). NLSC English landing page (www.nlsc.gov.tw/en/cp.aspx?n=2128) confirms the service is operational with 78 stations as of 2026-05-17 fetch. |
| **datum_epoch** | omitted -- no citable operator declaration. The NLSC English service page and sandbox-reachable portal content do not state a network frame/epoch. (TWD97 / ITRF94 epoch 1997.0 is the conventional national framework but the primer [datum-epoch] rule restricts citation to operator portal/spec/decree — non-operator sources are not citable.) |

## Context Notes

- Taiwan's e-GNSS system is operated by NLSC under the Ministry of the Interior. 78 reference stations cover the entire main island of Taiwan and outlying islands.
- The NTRIP caster IP `210.241.63.193:81` (and port 2101 on same host) both timed out from external (non-Taiwan) IP on 2026-05-06, 2026-05-13, 2026-05-17. Consistent with IP-based access restriction or firewall for authenticated users only. ArduSimple's Taiwan page (the only neutral third-party documentation) notes "their website may not be very user-friendly, so navigating the registration process might take some effort" — and offers paid registration assistance for clients who cannot complete it themselves. Strong signal that overseas individuals face a non-trivial registration path.
- Tariff structure: a TWD 2,000 application permit (valid 5 years) plus TWD 300/day usage fee. Day passes can be bought on-demand — suitable for hobbyist occasional use if registration is accessible.
- 4 NLSC e-GNSS CORS stations joined the International GNSS Service (IGS) as official IGS stations, indicating high-quality infrastructure.
- Registration: via egnss.nlsc.gov.tw portal; English-language portal available but contact for foreign registrant process not confirmed.
- NLSC contact: 4F., No. 497, Liming Rd., Sec.2, Taichung City 408281; Tel: +886-4-22522966.
- No rtk2go or Centipede volunteer bases found for Taiwan.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **NLSC e-GNSS CORS RINEX** — historical observations | https://egnss.nlsc.gov.tw | Via portal account; free or nominal fee |
| **IGS / CDDIS** — 4 Taiwan IGS stations | https://cddis.nasa.gov/ | Free |

## Sources Consulted
- NLSC e-GNSS service page: https://www.nlsc.gov.tw/en/cp.aspx?n=2128 (observed 2026-05-06)
- NLSC e-GNSS portal: https://egnss.nlsc.gov.tw (ECONNREFUSED on direct probe 2026-05-06)
- NLSC IGS membership: https://www.nlsc.gov.tw/en/NLSC_Content.aspx?n=2110&s=124088
- ArduSimple Taiwan page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-taiwan/
- Radiodetection Asia NTRIP guide (Asia region): https://support.radiodetection.com/hc/en-gb/articles/16203507810333-Asia
- curl probe of `210.241.63.193:81` + `:2101` — timed out 2026-05-06, 2026-05-13, 2026-05-17 (consistent geo-block / firewall)
- WebFetch of NLSC English landing https://www.nlsc.gov.tw/en/cp.aspx?n=2128 — 200 OK 2026-05-17 (service still operational; no datum statement found)
- NLSC fee-schedule page (egnss.nlsc.gov.tw/content.aspx?i=20150625102159760) — referenced as the official 收費標準 (Fee Standards) page; not retrievable from outside Taiwan; per NLSC FAQ source the fee structure follows the National Land Surveying and Mapping Data Fee Standard with membership renewals every 5 years
