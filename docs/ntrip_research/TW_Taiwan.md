# Taiwan [TW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid national NTRIP (e-GNSS / MOI NLSC); likely IP-restricted from outside Taiwan; day-rate pricing in TWD

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | NLSC (National Land Surveying and Mapping Center), Ministry of the Interior (MOI), R.O.C. (Taiwan) |
| **Service name** | e-GNSS Real-time Positioning System |
| **host:port** | `210.241.63.193:81` (primary published IP; timed out from external IP on 2026-05-06) |
| **VRS** | Yes — VBS-RTK (Virtual Base Station Real-Time Kinematic) |
| **Constellations** | GPS+GLONASS; selected stations also BeiDou+Galileo |
| **Number of reference stations** | 78 online real-time service base stations nationwide |
| **tariff — permit** | TWD 2,000 per 5-year application permit (~USD 62 at 2026 rates) |
| **tariff — daily use fee** | TWD 300/day (~USD 9.30/day at 2026 rates) |
| **VAT** | Taiwan does not apply VAT (business tax) to government GNSS service fees; confirm at registration |
| **hobbyist_eligibility** | Unclear — registration requires government permit application process; foreign individuals not explicitly excluded but practical access path unclear |
| **legal_residency_required** | Unclear — caster timed out from external IP during research, suggesting possible IP restriction or geoblocking |
| **last_confirmed_alive** | Portal egnss.nlsc.gov.tw reachable but returned ECONNREFUSED on direct caster probe 2026-05-06; NLSC website confirms service operational |

## Context Notes

- Taiwan's e-GNSS system is operated by NLSC under the Ministry of the Interior. 78 reference stations cover the entire main island of Taiwan and outlying islands.
- The NTRIP caster IP `210.241.63.193:81` (and port 2101 on same host) both timed out from an external (non-Taiwan) IP during research on 2026-05-06. This is consistent with IP-based access restriction or firewall for authenticated users only.
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
- curl probe of `210.241.63.193:81` and `210.241.63.200:2101` — both timed out 2026-05-06
