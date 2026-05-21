# Cyprus [CY] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-12)
**status:** YES — paid national CYPOS (DLS). 7 CORS. €142.80/6 mo or €238.00/12 mo per receiver. Runtime caster gated behind DLS portal + Citizen Service Centre profile validation. Only CY RTK service. €238/yr exceeds the $200 hobbyist cutoff; 6-month tier sits just below. URANUS (Tree Company Corporation, Greece) extends from GR with a Cyprus office and includes CY in its 117-station network.

## CYPOS — Cyprus Positioning System

| field | value |
|---|---|
| landing_url | https://portal.dls.moi.gov.cy/en/alles-ypiresies/diktyo-cypos/ |
| access_url | https://helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf (operator-published instructions; HTTP 200, 612 kB) |
| operator | Department of Lands and Surveys (DLS), Ministry of Interior, Republic of Cyprus |
| host:port | Not externally indexed. Leica Spider Business Center on internal `213.7.195.11/SBC/FrontendPage.aspx?mode=register` (geo-restricted; sandbox times out). Runtime NTRIP host issued after activation. |
| vrs | yes — VRS, iMAX, FKP, MAC all advertised per CYPOSNetwork.pdf → Leica GNSS Spider NRTK |
| num_stations | 7 — Nicosia, Limassol, Larnaca, Paphos, Paralimni, Polis (Chrysochous), Evrychou. 24/7/365 since 2010. Northern Cyprus not covered. |
| tariff — 6 mo / receiver | €142,80 |
| tariff — 12 mo / receiver | €238,00 |
| tariff — 2nd / 3rd receiver bundles | same per-receiver rate |
| VAT | CYPOSNetwork.pdf does not state whether the €142,80 / €238,00 figures are VAT-inclusive or exclusive. CY standard VAT 19%. Confirm at checkout. |
| hobbyist_eligibility | yes (CY residents) per CYPOSNetwork.pdf: "Any physical or legal person is entitled to apply for registration at CYPOS." No surveying-licence requirement. No practical path for non-residents — step 2 requires Citizen Service Centre profile validation (see legal_residency_required). |
| legal_residency_required | yes de facto — step 2 requires a "validated profile Id at the Citizen Service Centres" (physical persons) / "Central Post Offices" (legal entities). Assumes CY ID or residence-permit civil registration. Foreign-passport-only path not documented. |
| subscription cycle | 6 or 12 months; activation ≤2 working days post-payment; email + SMS reminder 5 days pre-expiry; no auto-renew |
| last_confirmed_alive | 2026-05-21 — `portal.dls.moi.gov.cy/.../diktyo-cypos/` 200; CYPOSNetwork.pdf 200, content unchanged from 2026-05-12 |
| datum_epoch | omitted — CYPOSNetwork.pdf and DLS Portal pages contain no explicit frame/epoch declaration for CYPOS streams. National geodetic frame is CGRS93 (Cyprus Geodetic Reference System 1993, based on WGS84 ellipsoid, transformation to ETRS89 derived at epoch 1993.1 per EPSG datum 1112; DLS is the stated authority per EPSG). No CYPOS operator page cites CGRS93 or an epoch for the broadcast corrections, so the primer citation rule is not satisfied. |

## Registration (per CYPOSNetwork.pdf)

1. Register at DLS Portal: http://eservices.dls.moi.gov.cy/#/signinscreen
2. Validate profile ID at Citizen Service Centre (physical) or Central Post Office (legal). Practical residency gate.
3. Apply to CYPOS Group via DLS Portal.
4. After Group admission → Dashboard "CYPOS Website" button → SBC registration form on `213.7.195.11/SBC/FrontendPage.aspx?mode=register`. Fill username, password, name, email, company (mandatory), language, mobile (mandatory), rover username (optional), period (6 / 12 mo).
5. Confirm via email link.
6. DLS Portal → Subscriptions → buy slot (€142,80 or €238,00).
7. Activation ≤2 working days.

## Context

- Only CY-internal RTK service identified. Zero CYP-coded rtk2go + Centipede streams (2026-05 archives).
- Local data: `py scripts/stations_by_country.py CYP` 2026-05-21 → 1 AUSCORS + 2 EUREF + 1 IGS (academic / IGS-IP only, including `NICO00CYP0`, `ASGA00CYP0`).
- "CYPOS services are not compatible with GPS mobile phones" per the operator PDF — RTCM-capable rover required (F9P, Trimble, Leica, Septentrio).
- ArduSimple CY page confirms paid national service; no pricing listed (figures here from CYPOSNetwork.pdf Figure 4).
- **URANUS** (Tree Company Corporation, Greece — see `GR_Greece.md`) advertises 117 reference stations across Greece + Cyprus combined (per-country split not disclosed), with a CY office (`info@haldera.com.cy`, +357 22 678897) per `uranus.gr/kalipsi`. Effectively a second commercial option for CY users, gated behind Treecomp commercial registration; 3-day free trial. hobbyist_eligibility: ? (same qualification as in GR entry — designed for commercial surveyors; trial at least technically accessible to individuals; ongoing rate not public).

## Post-processing

- CYPOS RINEX bundled with active subscription via DLS Portal.
- EUREF EPN: `NICO00CYP0` (free): https://epncb.oma.be/

## Sources

- DLS Portal CYPOS: https://portal.dls.moi.gov.cy/en/alles-ypiresies/diktyo-cypos/ (HTTP 200, 2026-05-21)
- CYPOSNetwork.pdf: https://helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf
- DLS Portal Subscriptions help: http://portal.dls.moi.gov.cy/en-us/FrontEndHelp/Pages/Subscriptions.aspx
- gov.cy service entry: https://www.gov.cy/en/service/cypos-cyprus-positioning-system-registration/
- ICA Cyprus National Report 2019-2023: https://icaci.org/files/documents/national_reports/2019-2023/Cyprus-2023.pdf
- ArduSimple CY: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-cyprus/
- URANUS coverage cite (Cyprus inclusion + CY office): https://uranus.gr/kalipsi (WebFetch 2026-05-21)
- SBC probe `http://213.7.195.11/SBC/...` (research env): timeout — geo-restricted

## Gaps

- Runtime NTRIP host:port — issued post-activation only; not publicly advertised.
- VAT inclusivity of €142,80 / €238,00 not annotated in PDF; 19% CY standard rate applies but whether prices are gross or net is unknown.
- Foreign-resident pathway through Citizen Service Centre profile validation undocumented; practically a hard gate for non-residents.
