# Agent intended Edit
- batch: batch5
- target: D:\Projects\ntrip-mountpoint-map\docs\ntrip_research\SX_SintMaarten.md
- transcript line: 230

## OLD_STRING

```markdown
# Sint Maarten [SX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no territory-operated NTRIP; nearest free option is EarthScope CN59 on Anguilla (~20 km); Kadaster NL AGRS does NOT cover SX

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Operator** | — |
| **Nearest free option** | EarthScope NOTA station CN59 on Anguilla (~20 km) via `ntrip.earthscope.org:2101`; free noncommercial (account + NULA required) |
| **VRS** | No — single-base stream only |
| **tariff — EarthScope noncommercial** | Free |
| **tariff — EarthScope commercial** | USD $1,000/seat/year |
| **hobbyist_eligibility** | Yes (EarthScope noncommercial account) |
| **legal_residency_required** | No |
| **last_confirmed_alive** | EarthScope portal alive 2026-05-06 |
```

## NEW_STRING

```markdown
# Sint Maarten [SX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07

## Status: YES — Kadaster St. Maarten now offers a paid CORS reference-station subscription (priced in XCG); host:port not yet publicly listed; nearest free fallback is EarthScope CN59 on Anguilla (~20 km); Kadaster NL AGRS does NOT cover SX

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — Kadaster St. Maarten CORS subscription (host:port not on public web; obtained at subscription); **previous status (no caster) revised 2026-05-07** based on `kadaster.sx/services` price list discovery |
| **Operator (primary)** | Stichting Kadaster- en Hypotheekwezen Sint Maarten — `kadaster.sx`. Foundation established 1999 as official property registrar; in-house GIS platform deployed 2025-07 with GIS4C B.V. (ArcGIS Enterprise + ArcGIS Pro + Drone2Map) |
| **Service name (SX domestic)** | "Use of CORS station" (subscription product on `kadaster.sx/services`) |
| **host:port — SX Kadaster CORS** | Not published on public web (typical Caribbean cadaster pattern: credentials and host issued on subscription; sourcetable not exposed) |
| **VRS — SX Kadaster CORS** | Unclear — number of reference stations and product type (single-base vs. VRS) not on public service catalogue; SX is 34 km² so a single Kadaster reference station likely covers the whole Dutch side |
| **tariff — SX Kadaster CORS, monthly** | XCG 360.00 / month (~USD 202.30 at 2026-05 transition rate; XCG = Caribbean guilder, the new 2025 currency replacing the Antillean guilder ANG, pegged 1.79 to USD) |
| **tariff — SX Kadaster CORS, annual** | XCG 3,600.00 / year (~USD 2,022.50; equivalent to 10 months — 16.7 % annual discount) |
| **VAT — SX Kadaster CORS** | TOT (Turnover Tax / "Belasting op Bedrijfsomzetten" / BBO) is 5 % on services in Sint Maarten; pricing-page wording "XCG 360.00 / 3,600.00" does not flag whether TOT is included; verify on invoicing |
| **hobbyist_eligibility — SX Kadaster CORS** | Unclear — Kadaster St. Maarten product catalogue does not list registration restrictions; client base is conventionally licensed surveyors and land-related professionals. No price tier for individuals |
| **legal_residency_required — SX Kadaster CORS** | Unclear — typical Kadaster customer flow accepts non-resident professionals through invoiced billing; nothing on the service page restricts to SX residents |
| **Nearest free fallback** | EarthScope NOTA station CN59 on Anguilla (~20 km north) via `ntrip.earthscope.org:2101`; free noncommercial (NULA license + account required); single-base RTCM 3 stream |
| **tariff — EarthScope noncommercial** | Free (NULA) |
| **tariff — EarthScope commercial** | USD $1,000 / seat / year (2024 commercial license tier) |
| **hobbyist_eligibility — EarthScope** | Yes (noncommercial account) |
| **legal_residency_required — EarthScope** | No |
| **last_confirmed_alive — Kadaster SX** | `kadaster.sx/services` HTTP 200 with CORS-station price line confirmed 2026-05-07 |
| **last_confirmed_alive — EarthScope** | 2026-05-07 (`ntrip.earthscope.org` portal reachable; CN59 in NOTA station list) |
```
