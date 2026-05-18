# USA National Park Service CORS [US-NPS] — NTRIP RTK Caster Research

## Status: YES — operational, free, manual account provisioning; hobbyist eligibility unlikely (federal-internal scope per latest documented policy)

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | Yes |
| Operator | US DOI / National Park Service (NPS) |
| landing_url | https://ntrip.nps.gov/ — operator portal; declares rover endpoint `rtk.nps.gov:2101` |
| access_url | Skip — portal describes manual provisioning + RINEX downloads; no separate signup page. Contact `neil_winn@ios.doi.gov` for accounts (portal page text 2026-05-18) |
| host:port | `rtk.nps.gov:2101` (rover NTRIP). Portal/management on `ntrip.nps.gov` HTTPS |
| software | NTRIP Trimble Caster 5.2; Trimble Pivot Platform; Trimble NetR9 receivers in field |
| tariff | Free — no fee schedule; federal service, manual/discretionary provisioning |
| account_provisioning | Manual — contact `neil_winn@ios.doi.gov` (portal text 2026-05-18); no self-service form |
| vrs | No — all 142 mountpoints single-base (nmea=0). No NRTK mountpoint advertised |
| num_stations | 142 active mountpoints (live ST 2026-05-18). 1:1 with physical stations; no NEAR/AUTO/VRS routing aliases |
| hobbyist_eligibility | Likely no — only documented external-access policy (2022 NPS-AKRO Cusick slide deck) scopes access to "DOI partners" / federal-state collaborators (ACORN tie-in). No subsequent broader policy located. Login = email + password but accounts are staff-provisioned (not self-service) and no public access tier published. Confirm via portal contact `neil_winn@ios.doi.gov` |
| legal_residency_required | Unclear — no residency/citizenship requirement stated; access at NPS staff discretion |
| last_confirmed_alive | 2026-05-18 — `SOURCETABLE 200 OK`, 142 STR; portal HTTP 200 |
| datum_epoch | NAD83(2011) Epoch 2010.0 — **only-positive citation is single 2022 slide deck** (Cusick, NPS Alaska Regional Office, "Centimeter Precision Mapping via GNSS Base Stations", DGGS-hosted): "DATUM NAD83 (2011) 2010.0". Slide-deck format from a regional office, not operator spec or current network policy; ~4 years stale. `ntrip.nps.gov` portal landing pages checked 2026-05-18 (home + Login.aspx + Map/SensorMap.aspx — Trimble Pivot defaults; no inline datum text); contact `neil_winn@ios.doi.gov` provided as pointer for binding current statement. MYCS2→MYCS3 transition status (post-NGS June 2025 model release) unresolved for NPS — could have changed epoch since 2022 slide. **Treat citation as weak; re-confirm with operator before survey-grade use** |

## Stream characteristics

| Parameter | Value |
|---|---|
| Solution | Single-base RTK (no VRS/MAC/FKP/iMAX in ST) |
| Update rate | 1 second |
| Format | RTCM 3.2 (most stations); RTCM 3.4 (newer, e.g. `DESO_RTCM3`). Declared message set `1004(1),1005/1007(5),PBS(10)` |
| Constellations | Live ST 2026-05-18 advertises RTCM 3.2 / 3.4 with MSM-family message sets capable of multi-GNSS; per-stream constellation declaration (sourcetable field 6) is multi-const on current streams across the 142 mountpoints sampled. Historical Cusick 2022 slide deck explicitly "GPS only — old school"; current ST advertises multi-const network-wide. **Inference vs verified**: confirmed from sourcetable field 6 read across STR rows, not inferred from format alone |
| Coverage | CONUS, Alaska, Caribbean (Puerto Rico via `SAJU_RTCM3`), Pacific (Hawaii, American Samoa), Marianas |
| Sourcetable structure | Per-stream `NET` = `NPSNet` on most rows (some blank, e.g. `YOSE_RTCM3`); no `CAS;`/`NET;` summary line (normal for this Trimble Pivot deployment) |

## Coverage spot-check (live ST 2026-05-18)

- Pacific: `HALE_RTCM3` (Haleakala, Maui), `HAVO_RTCM3` (Hawaii Volcanoes), `KAHO`, `KEF1`, `PUHE`
- Alaska: `DENA_RTCM3` (Denali), `GAA2_RTCM3`/`GAA3_RTCM3` (Gates of Arctic), `GLAC_RTCM3` (Glacier Bay), `KNAI_RTCM3`, `LACL_RTCM3`
- CONUS/Caribbean: `DESO_RTCM3` (De Soto, FL — RTCM 3.4), `PAAL_RTCM3`, `SAJU_RTCM3` (San Juan, PR)

## Hostname

Portal: "NTRIP Address: **rtk.nps.gov** Port: **2101**". `ntrip.nps.gov` = portal/management; `rtk.nps.gov:2101` = rover NTRIP. Earlier 2022 DGGS slide deck cited `ntrip.nps.gov:2101`; live portal now explicitly directs to `rtk.nps.gov:2101`.

## Notes

- Federal-government survey infrastructure, not public community service. Primary purpose: NPS internal GIS and field survey.
- 2022 Cusick slide deck (Alaska Regional Office) explicit external-access language: "DOI partners preferred" for planned site expansion; "Using our stations is good practice for tying into ACORN" (CT–AK collaborative framing); contact for credentials shown as `joel_cusick@nps.gov` (AK regional) in 2022, now `neil_winn@ios.doi.gov` network-wide. **External access precedent in 2022 slide: scoped to DOI / federal partners and ACORN-style collaboration — NOT a broad hobbyist/public invitation.** No subsequent public-access policy document identified.
- No published external-access policy, pricing, or subscription tier.
- Pipeline ingestion: 142 physical CORS = 142 mountpoints (1:1, nmea=0). Sourcetable publicly listable (no auth); credentials required only for stream subscription.

## Sources

- NPS GNSS portal: https://ntrip.nps.gov/ (HTTP 200; contact `neil_winn@ios.doi.gov` shown)
- Live ST: `curl --http0.9 -A 'NTRIP/1.0' http://rtk.nps.gov:2101/` → 142 STR
- NGS MYCS3 release page (context only, NOT citable for datum_epoch): https://geodesy.noaa.gov/CORS/news/mycs3/mycs3.shtml
- 2022 DGGS slide deck (Cusick, historical context): https://dggs.alaska.gov/webpubs/dggs/ago/documents/2022AGC_GISDay/Day_1-4_Joel_Cusick_Hi_Precision_BaseStations.pdf
- NPS ArcGIS layer: https://www.arcgis.com/home/item.html?id=c7490365d71a4cdb8da245b11c28c99f
