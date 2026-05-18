# Slovenia [SI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-13)

## Status: YES — paid national NTRIP (SIGNAL); free for public bodies; individuals can subscribe; port 8080

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | GURS via Geodetski inštitut Slovenije (Surveying and Mapping Authority of the Republic of Slovenia) |
| **Service name** | Omrežje SIGNAL |
| **host:port** | `178.172.26.131:8080` |
| **VRS** | Yes — VRSSLO(2_3), VRSSLO(3_1), VRSMSM5, VRSCMRx, VRSCMRp |
| **Network type** | VRS, MAC/MAX (MacSLO), individual station streams |
| **Constellations** | GPS+GLO (RTCM 2.3/3.1); GPS+GLO+GAL+BDS (CMRx, MSM5) |
| **Number of reference stations** | 16 stations across Slovenia (Bovec, Brežice, Celje, Črnomelj, Idrija, Ilirska Bistrica, Koper, Lendava, Ljubljana, Maribor, Nova Gorica, Ptuj, Radovljica, Slovenj Gradec, Trebnje + foreign-adjacent stations) |
| **tariff — flat rate (annual)** | €829.44/year excl. VAT (billing year 2025-04-01 to 2026-03-31; new 2026-04-01 to 2027-03-31 billing year is now active — page is not yet refreshed with the new headline figure at 2026-05-13 but the structure is unchanged); €622.08 with 25% early-bird discount if contracted before 2025-07-31 and paid in one installment (this specific discount window has closed; equivalent discounts may be offered for the current billing year — confirm with gps@gis.si) |
| **tariff — pay-per-use (RTCM)** | €0.12/connected minute excl. VAT; quarterly billing (monthly if invoice > €25) |
| **tariff — RINEX commercial** | €0.26/second server-processing time (~€4.21 per hour of RINEX data) |
| **tariff — TOP commercial (static/rapid-static post-processing)** | €0.26/second server-processing time |
| **tariff — public bodies / RTCM Non-Commercial** | Free (requires documentation to gps@gis.si within 1 week of registration) |
| **tariff — students/civil society** | Free with institutional verification (educational certification / public-interest documentation) |
| **VAT** | Slovenian standard rate 22%; prices above are excl. VAT |
| **hobbyist_eligibility** | Yes — individuals (fizična oseba) can register; no professional licence required |
| **legal_residency_required** | Unclear — no explicit restriction for non-Slovenian EU users; registration requires postal mail of signed contract (4 copies) to Geodetski inštitut Slovenije, Jamova cesta 2, 1000 Ljubljana |
| **last_confirmed_alive** | `178.172.26.131:8080` `SOURCETABLE 200 OK` on 2026-05-13 (TCP probe, Trimble Ntrip Caster 5.2, 113 STR). Pricing page `gu-signal.si/postopek-registracije/` re-fetched 2026-05-17: same headline €829.44/yr excl. VAT, billing 2025-04-01 → 2026-03-31 (page not yet refreshed for 2026-04 → 2027-03 billing year — confirm with gps@gis.si) |
| **datum / epoch** | D96/TM (national projection over ETRS89) is Slovenia's official survey CRS; SIGNAL operator portal does not republish a frame/epoch declaration in the registration or services pages reachable from this sandbox — `omitted -- no citable operator declaration`. Cross-border products tie to ETRS89 via Slovenian state survey (GURS), but no SIGNAL operator page states epoch. |

## Context Notes

- Sourcetable confirmed 113 STR records (2026-05-13 probe): includes network products (VRSSLO 2.3 / 3.1 / MSM5, VRSCMRp, VRSCMRx, MULTI 2_3, MULTI 3_1, MULTI_CMRx, MAC/MAX) plus individual SI station streams (e.g. SLOG_APOS, MRBR_APOS) and cross-border streams (KOPR_fvg, etc. — Austria/Croatia/Italy/Hungary stations).
- RTCM formats: 2.3 (GPS), 3.1 (GPS+GLONASS), 3.2 MSM5/MSM7 (multi-constellation), CMR+, CMRx.
- Registration requires: completing online form → receiving contract by email → signing 4 copies → posting to Geodetski inštitut Slovenije → receiving credentials by email. Allow ~2 business days.
- Non-commercial eligibility (public administration, students, civil societies) requires supporting documentation submitted to gps@gis.si within one week of application.
- The SIGNAL portal (gu-signal.si) is in Slovenian; English support available via phone 01 200 29 29 or email gps@gis.si.
- **Volunteer supplement (verified 2026-05-13)**: `py scripts/stations_by_country.py SVN` → rtk2go 4 SI volunteer bases (FRELIH, Kmetija-Budic, Lukez, MarkovciRTK), Centipede 4 SI nodes (MAKO, OUCE, PRIME, SIPOS). Useful coverage but SIGNAL is the primary RTK source.
- Tariff re-verified on gu-signal.si/postopek-registracije/ on 2026-05-17: "Cena takega paketa znaša 829,44 € brez DDV, z možnostjo dodatnega 25% popusta…" — wording unchanged from 2025-04 schedule; new 2026-04 → 2027-03 billing schedule had not propagated to public page at fetch time.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SIGNAL RINEX/post-processing** | https://gu-signal.si/ | €0.26/s server processing time (€4.21/hr of data); free for public bodies |
| **SIGNAL open data (OPSI)** | https://podatki.gov.si/dataset/podatki-omrezja-signal | Free (historic GNSS observations) |

## Sources Consulted
- GURS SIGNAL portal: https://gu-signal.si/ (observed 2026-05-06)
- SIGNAL NTRIP access page: https://gu-signal.si/dostop-do-ntrip-streznika/ (IP 178.172.26.131, port 8080)
- SIGNAL RTK mountpoints: https://gu-signal.si/rtk-dostopne-tocke-in-stevilke/
- SIGNAL registration & pricing: https://gu-signal.si/postopek-registracije/
- TCP probe of `178.172.26.131:8080` — SOURCETABLE 200 OK confirmed 2026-05-13; Trimble Ntrip Caster 5.2; 113 mountpoints visible (network + single-station + cross-border)
