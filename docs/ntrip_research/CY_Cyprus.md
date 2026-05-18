# Cyprus [CY] — NTRIP RTK Research

**researched:** 2026-05-17 (prior: 2026-05-12)
**status:** YES — paid national CYPOS (DLS); 7 CORS; €142.80/6mo or €238.00/12mo per receiver; runtime caster gated behind DLS portal + Citizen Service Centre profile validation. Only CY service. €238/yr > $200 hobbyist cutoff; 6-month tier just under.

## Service — CYPOS (Cyprus Positioning System)

| field | value |
|---|---|
| landing_url | https://portal.dls.moi.gov.cy/en/alles-ypiresies/diktyo-cypos/ |
| access_url | https://helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf (operator instructions; HTTP 200, 612 kB, 2026-05-12) |
| operator | Department of Lands and Surveys (DLS), Ministry of Interior, Republic of Cyprus |
| host:port | not externally indexed. Leica Spider Business Center on internal `213.7.195.11/SBC/FrontendPage.aspx?mode=register` (geo-restricted to CY / DLS tenants; sandbox times out). Runtime NTRIP host issued after activation. |
| vrs | yes — VRS, iMAX, FKP, MAC all advertised (CYPOSNetwork.pdf) → Leica GNSS Spider NRTK |
| num_stations | 7 — Nicosia, Limassol, Larnaca, Paphos, Paralimni, Polis (Chrysochous), Evrychou. 24/7/365 since 2010. Northern Cyprus not covered. |
| tariff — 6 mo / receiver | €142.80 |
| tariff — 12 mo / receiver | €238.00 |
| tariff — 2nd/3rd receiver bundles | same per-receiver rate |
| VAT | not annotated on price screenshot; CY standard 19%; confirm at checkout |
| hobbyist_eligibility | yes per CYPOSNetwork.pdf: "Any physical or legal person is entitled to apply for registration at CYPOS." No surveying-licence requirement. |
| legal_residency_required | yes de facto — step 2 requires "validated profile Id at the Citizen Service Centres" (physical persons) / "Central Post Offices" (legal entities). Assumes CY ID or residence-permit civil registration. Foreign-passport-only path not documented. |
| subscription cycle | 6 or 12 mo; activation ≤2 working days post-payment; email + SMS 5 days pre-expiry; no auto-renew |
| last_confirmed_alive | 2026-05-17 — `portal.dls.moi.gov.cy/.../diktyo-cypos/` 200; CYPOSNetwork.pdf 200, content unchanged from 2026-05-12 |
| datum_epoch | omitted — no citable declaration on operator portal or CYPOSNetwork.pdf |

## Registration (per CYPOSNetwork.pdf)
1. Register at DLS Portal: http://eservices.dls.moi.gov.cy/#/signinscreen
2. Validate profile ID at Citizen Service Centre (physical) or Central Post Office (legal). Practical residency gate.
3. Apply to CYPOS Group via DLS Portal.
4. After Group admission → Dashboard "CYPOS Website" button → SBC registration form on `213.7.195.11/SBC/FrontendPage.aspx?mode=register`. Fill: username, password, name, email, company (mandatory), language, mobile (mandatory), rover username (optional), period (6/12 mo).
5. Confirm via email link.
6. DLS Portal → Subscriptions → buy slot (€142.80 or €238.00).
7. Activation ≤2 working days.

## Notes
- Only CY RTK service identified. Zero CYP-coded rtk2go + Centipede streams (2026-05 archives). EUREF EPN station `NICO00CYP0` + IGS `ASGA00CYP0` present in local mirrors but academic / IGS-IP only.
- "CYPOS services are not compatible with GPS mobile phones" — needs RTCM-capable rover (F9P, Trimble, Leica, Septentrio).
- ArduSimple CY page confirms paid national service; no pricing listed (figures here from CYPOSNetwork.pdf Figure 4).

## Post-processing
- CYPOS RINEX bundled w/ active subscription via DLS Portal.
- EUREF EPN (free): https://epncb.oma.be/

## Sources
- DLS Portal CYPOS: https://portal.dls.moi.gov.cy/en/alles-ypiresies/diktyo-cypos/ (HTTPS 200, 2026-05-17)
- CYPOSNetwork.pdf: https://helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf
- DLS Portal Subscriptions help: http://portal.dls.moi.gov.cy/en-us/FrontEndHelp/Pages/Subscriptions.aspx
- gov.cy service entry: https://www.gov.cy/en/service/cypos-cyprus-positioning-system-registration/
- ICA Cyprus National Report 2019–2023: https://icaci.org/files/documents/national_reports/2019-2023/Cyprus-2023.pdf
- ArduSimple CY: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-cyprus/
- SBC probe `http://213.7.195.11/SBC/...` (research env 2026-05-12): timeout — geo-restricted

## Gaps
- Runtime NTRIP host:port — issued post-activation only.
- VAT inclusivity of €142.80 / €238.00 not annotated.
- Foreign-resident pathway through Citizen Service Centre profile validation undocumented.
