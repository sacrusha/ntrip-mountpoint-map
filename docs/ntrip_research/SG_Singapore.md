# Singapore [SG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid national NTRIP (SiReNT); SingPass/CorpPass required; residency-gated in practice; no free tier

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | SLA (Singapore Land Authority) |
| **Service name** | SiReNT (Singapore Integrated Reference Station Network) |
| **host:port** | `199.184.151.36:2101` (older published IP: `203.127.20.71:2101`) |
| **VRS** | Yes — Trimble Pivot Platform; mountpoints DGNSS_SLYG, RTK_SLYG_31/32/GPS/X etc. |
| **Constellations** | GPS+GLONASS (RTCM 2.3/3.1); GPS+GLO+GAL+BDS+QZS (RTCM 3.2, CMRx) |
| **Number of reference stations** | 8+ (SLYG, SNPT, SNUS, SNYU, SRPT shown in sourcetable) |
| **tariff — single account (1–9)** | SGD 107.00/month per account |
| **tariff — bulk (10–50 accounts)** | SGD 64.20/month per account |
| **tariff — bulk (51+ accounts)** | SGD 32.10/month per account |
| **tariff — post-processing on-demand** | SGD 10.70/month + SGD 0.32/min |
| **tariff — post-processing archive** | SGD 53.50/month |
| **admin fee (one-time)** | SGD 32.10 |
| **tariff — 3-day trial** | Available (one trial per month) |
| **VAT** | Not confirmed in reviewed sources; Singapore GST is 9% (2024 rate) |
| **hobbyist_eligibility** | Unclear — individual SingPass accounts exist for foreigners (SFA) but SiReNT registration flow requires SingPass or CorpPass; no explicit hobbyist block, but foreign individuals would need SFA first |
| **legal_residency_required** | Yes in practice — SingPass is Singapore national digital identity; CorpPass is for Singapore-registered entities; foreign individuals need Singpass Foreign Account (SFA) which is NRIC/FIN-gated |
| **last_confirmed_alive** | `199.184.151.36:2101` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl probe); Trimble Ntrip Caster 4.7 |

## Context Notes

- SiReNT covers Singapore's entire territory (733 km²) with VRS corrections. Multiple mountpoints per physical station in RTCM 2.3, 3.1, 3.2 and CMRx formats.
- Physical stations identified in sourcetable: SLYG (~1.37°N 103.87°E), SNPT (~1.38°N 103.85°E), SNUS (~1.29°N 103.78°E), SNYU (~1.35°N 103.68°E), SRPT (~1.44°N 103.78°E) — at minimum 5 reference stations.
- SingPass Foreign User Account (SFA): Foreigners with a valid FIN (Foreign Identification Number) issued by Singapore can register for SFA. Tourists without a FIN cannot. This effectively restricts hobbyist access for visitors.
- No rtk2go or Centipede volunteer bases found for Singapore.
- No free government tier exists.
- Tariff prices observed on `app.sla.gov.sg/sirent/Page/Services` on 2026-05-06 (prices inclusive of GST unclear — confirm at registration).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SiReNT post-processing on-demand** | https://app.sla.gov.sg/sirent/ | SGD 10.70/month + SGD 0.32/min |
| **SiReNT archive** | https://app.sla.gov.sg/sirent/ | SGD 53.50/month |

## Sources Consulted
- SiReNT Services page: https://app.sla.gov.sg/sirent/Page/Services (observed 2026-05-06)
- SiReNT FAQ: https://app.sla.gov.sg/sirent/Page/FAQ (confirmed IP 199.184.151.36:2101)
- ArduSimple Singapore RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-singapore/
- Singpass SFA for foreign individuals: https://www.iras.gov.sg/digital-services/others/singpass-foreign-user-account-(sfa)-for-foreign-individuals
- curl probe of `199.184.151.36:2101` — SOURCETABLE 200 OK confirmed 2026-05-06; Trimble Ntrip Caster 4.7; sourcetable shows RTK and DGNSS mountpoints for SiReNT
