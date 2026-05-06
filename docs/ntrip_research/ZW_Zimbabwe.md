# Zimbabwe [ZW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: CORS exists — NTRIP endpoint NOT publicly disclosed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown / probably yes (semi-operational; access gated through direct contact) |
| **host:port** | Not publicly published — CORS portal at https://zingsa.ac.zw/django-test/cors does not expose NTRIP host:port |
| **tariff** | Not published. No pricing schedule on ZINGSA website. Contact required. |
| **hobbyist_eligibility** | Unclear — ZINGSA describes users broadly ("surveyors, GIS users, engineers, scientists and other people who collect GNSS data") but no published hobbyist policy |
| **legal_residency_required** | Unclear — no published terms of service |
| **last_confirmed_alive** | 2026-05-06 — ZINGSA website and CORS portal page reachable; no ZW mountpoint found in any public NTRIP sourcetable |

## Operator

**ZINGSA — Zimbabwe National Geospatial and Space Agency**
630 Churchill Avenue, Mount Pleasant, Harare, Zimbabwe
Phone: +263 8677009885 / +263 8677009884
Email: publicrelations@zingsa.ac.zw
Website: https://zingsa.ac.zw/

## Timeline

| Date | Event |
|------|-------|
| 2018 | ZINGSA established by Presidential decree |
| Sep 2020 | Academic paper: Zimbabwe in "planning phase" for CORS; EU/UNDP funding earmarked for initial 5 stations |
| Feb 4, 2024 | Herald Zimbabwe confirms ZINGSA "has embarked on densification of CORS" — network described as operational but expanding |
| Jan 10, 2025 | 2025 national budget allocates ZiG 64.22 million (~USD 1.78M) to ZINGSA space programme including CORS |

## Known Station

- **ZINH** (Harare) — referenced in internal ZINGSA DJI M300 RTK setup document. Connection parameters not publicly disclosed.

## Negative Findings

- RTK2GO: No ZW mountpoints in any public sourcetable
- IGS: No Zimbabwe stations in network. Note: "HARB" is HARB00ZAF in Pretoria, South Africa — not Zimbabwe.
- AFREF (2016 docs): Central-southern Africa including Zimbabwe "devoid of CORS installations"
- HartRAO: No Zimbabwe stations in 28-station African archive
- TrigNet: South Africa only; RTK range does not reach Zimbabwe
- GEODNET, ONOCOY, ArduSimple: Zimbabwe not listed
- ntrip-list.com Africa: Zimbabwe not listed

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **ZINGSA CORS RINEX data service** — portal page exists; access method and cost not publicly disclosed | https://zingsa.ac.zw/django-test/cors | Unknown — contact publicrelations@zingsa.ac.zw |

## Sources
- https://zingsa.ac.zw/ (CORS portal)
- https://www.heraldonline.co.zw/technology-to-enhance-countrys-ability-to-solve-challenges/ (Feb 2024)
- https://doaj.org/article/835a37dd28564728869ad42dcde830d2 (Mlambo & Ali 2020)
- https://spaceinafrica.com/2025/01/10/zimbabwes-2025-space-budget-a-strategic-leap-for-zingsa/
- ntrip-list.com/africa, ArduSimple country directory
