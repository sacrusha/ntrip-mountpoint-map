# Agent intended Edit
- batch: batch1
- target: D:\Projects\ntrip-mountpoint-map\docs\ntrip_research\BY_Belarus.md
- transcript line: 101

## OLD_STRING

```markdown
# Belarus [BY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid national GNSS RTK network (ССТП РБ / Belgeodeziya); contract required; no free or self-service hobbyist tier; NTRIP protocol confirmed; host not published

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid; contract-gated) |
| **Operator** | GP "Belgeodeziya" (State Enterprise Белгеодезия / Государственное предприятие «Белгеодезия») |
| **Service name** | ССТП РБ (Система Спутниковых Технологий Позиционирования Республики Беларусь — Satellite Precision Positioning System of the Republic of Belarus) |
| **host:port** | Not publicly listed — provided to users after contract signing with Belgeodeziya |
| **VRS** | Likely yes — documentation describes network corrections delivered via GNSS Spider software (GeoMax); corrections type not confirmed VRS vs. MAC |
| **Stations** | 98 reference stations nationwide (full territory coverage) |
| **RTCM format** | RTCM 3.x (confirmed in documentation); CMR+ also referenced |
| **tariff** | Paid — "unified tariffs of GP 'Belgeodeziya' agreed with the State Committee on Property of the Republic of Belarus" (Госкомитет по имуществу); no public rate schedule found as of 2026-05-06 |
| **hobbyist_eligibility** | No — institutional/commercial contract required; no individual self-service registration path identified |
| **legal_residency_required** | Unclear — state enterprise contract implies Belarusian legal entity; no confirmed mechanism for foreign individual access; Western sanctions (EU/US, post-2022) create practical barriers |
| **last_confirmed_alive** | geo.by website HTTP 200 on 2026-05-06; ССТП service page confirmed active at geo.by/services/sstp; no public NTRIP endpoint to probe |
```

## NEW_STRING

```markdown
# Belarus [BY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07 (initial 2026-05-06)

## Status: YES — paid national GNSS RTK network (ССТП РБ / Belgeodeziya); public contract sign-up restricted to Belarusian residents; no free hobbyist tier

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid; public contract; residency-gated) |
| **Operator** | РУП «Белгеодезия» (Republican Unitary Enterprise Belgeodesiya, under the State Committee for Property — Госкомимущество) |
| **Service name** | ССТП РБ (Система Спутниковых Технологий Позиционирования Республики Беларусь — Satellite System of Precise Positioning of the Republic of Belarus) |
| **host:port** | `sstp.geo.by:8080` (IP fallback `93.125.21.51:8080`) — sourced from companion research in `docs/country-survey.md` (BY entry, date_added 2026-04-30); not advertised on the geo.by service page itself |
| **VRS** | Likely yes — documentation describes network corrections delivered via GNSS Spider software (Leica/GeoMax); corrections type not confirmed VRS vs. MAC |
| **Stations** | 98 reference stations nationwide (full territory coverage) |
| **RTCM format** | RTCM 3.x (confirmed in documentation); CMR+ also referenced |
| **tariff — RTK metered** | 0.24 BYN/min RTK (~$0.085/min, "Общий" plan) on the residents-of-Belarus tariff schedule. Source: `docs/country-survey.md` BY entry 2026-04-30. No annual flat RTK rate published. |
| **tariff — monthly fixed** | "Точная навигация" (Precise Navigation) plan: 150.78 BYN/month (~$53/month, ~$641/yr if rolled monthly); Source: same as above |
| **VAT** | Unknown if BYN figures include НДС (Belarusian VAT, currently 20%); Belgeodeziya tariff PDF not extractable as text (PDF binary) |
| **hobbyist_eligibility** | No for self-service path. Public contract (Публичный договор) is in principle open to individuals (физическое лицо) and legal entities, but the specific tariff schedule sighted is "для резидентов Республики Беларусь" — residency-gated |
| **legal_residency_required** | Yes — tariff explicitly addressed to Belarusian residents; no confirmed mechanism for foreign individual access; EU/US/UK sanctions packages post-2022 add practical barriers (see Sanctions context below) |
| **last_confirmed_alive** | geo.by website HTTP 200 on 2026-05-07; ССТП service page confirmed active at https://geo.by/services/sstp; tariff PDF link present at `geo.by/images/tariffs.pdf` (binary, not text-extractable) |
```
