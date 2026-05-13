# Cyprus [CY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: YES — paid national CYPOS service operated by DLS; 7 permanent GNSS stations; subscription **€142.80 / 6 months** or **€238.00 / 12 months** per receiver, additional 2nd/3rd-receiver bundles at the same per-receiver rate; software stack is Leica Spider Business Center on internal IP 213.7.195.11; NTRIP host:port not externally indexed (gated behind DLS Portal + Citizen Service Centre profile validation)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Service name** | CYPOS — Cyprus Positioning System |
| **Operator** | Department of Lands and Surveys (DLS), Ministry of Interior — `dls.moi.gov.cy` / `portal.dls.moi.gov.cy` |
| **Stations** | 7 permanent GNSS stations on the south coast and central plateau: Nicosia, Limassol, Larnaca, Paphos, Paralimni, Polis (Chrysochous), Evrychou. In continuous 24/7/365 operation since 2010. |
| **host:port** | Not externally indexed. CYPOS's Leica Spider Business Center registration page is on internal IP `213.7.195.11/SBC/FrontendPage.aspx?mode=register` (per the official `helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf` instructions, Figure 3) — this IP is geo-restricted / DLS-tenant-only and times out from outside-Cyprus IPs (confirmed unreachable 2026-05-12 from research env). The runtime NTRIP caster host:port is issued to users after subscription activation and not advertised publicly. |
| **Network solutions** | VRS (Virtual Reference Station), iMAX, FKP (Flächen-Korrektur-Parameter), MAC (Master-Auxiliary Concept) — per the official CYPOSNetwork.pdf. Implies Leica GNSS Spider network-RTK on the caster side. |
| **tariff — 6 months / 1st receiver** | **€142.80** per credential (CYPOS 6 months) — figure observed on the official DLS Portal Subscriptions page screenshot in `helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf` Figure 4, dated 2026-05-12 |
| **tariff — 12 months / 1st receiver** | **€238.00** per credential (CYPOS 12 months) |
| **tariff — 6 months / 2nd or 3rd receiver bundle** | **€142.80** each (same UserName, separate credentials per receiver) |
| **tariff — 12 months / 2nd or 3rd receiver bundle** | **€238.00** each |
| **VAT status** | The price-list screenshot does not annotate VAT/no-VAT explicitly; Cyprus standard VAT is 19% and government cadastral services are generally invoiced inclusive of VAT — to be confirmed at checkout |
| **hobbyist_eligibility** | **Yes — explicitly open to physical persons**: per CYPOSNetwork.pdf, "Any physical or legal person is entitled to apply for registration at CYPOS." No professional licence requirement stated. |
| **legal_residency_required** | **Likely yes (de facto)** — registration requires "validated profile Id at the Citizen Service Centres (for physical entities) or Central Post Offices (for legal entities)" which assumes Cypriot ID or a residence-permit-backed civil registration. Foreign-passport-only signup is not addressed in CYPOSNetwork.pdf; foreign hobbyists would need a Cypriot identity number or a local legal-entity sponsor. |
| **Subscription cycle (1st-receiver)** | "Subscribtion refers to 6 or 12 months period" (per CYPOSNetwork.pdf, Figure 3 form note). Activation takes up to **2 working days** after payment. Auto-renewal not enabled; system sends email + SMS 5 days before expiry. |
| **last_confirmed_alive** | 2026-05-12 — `portal.dls.moi.gov.cy/en/alles-ypiresies/diktyo-cypos/` HTTPS 200; `helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf` HTTP 200, 612 kB PDF. Active operation confirmed by ongoing publication of CYPOS Subscription product on DLS Portal; previous DLS maintenance notice posted for 28 April 2026. Caster live status cannot be confirmed without credentials. |

## Registration Process

Per the official CYPOSNetwork.pdf (`helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf`, 4 pages, observed 2026-05-12):

1. Register at the DLS Portal: `http://eservices.dls.moi.gov.cy/#/signinscreen`
2. **Validate your profile ID at a Citizen Service Centre (Κέντρα Εξυπηρέτησης του Πολίτη) for physical persons, or at a Central Post Office for legal entities** — this is the practical residency gate.
3. Submit application to join the CYPOS Group via the DLS Portal (`portal.dls.moi.gov.cy/en-us/FrontEndHelp/Pages/GroupsAndMembeships.aspx`).
4. Once admitted to the CYPOS Group, a "CYPOS Website" button appears on the Dashboard; click it to be redirected to the Leica Spider Business Center registration form on internal IP `213.7.195.11/SBC/FrontendPage.aspx?mode=register`. Fill: username, password, first/last name, e-mail, company (mandatory), language (multi-language including English), mobile phone (mandatory), rover username (optional), subscription period in months (6 or 12).
5. Confirm registration via email link.
6. Return to DLS Portal → Subscriptions → select CYPOS product (6 mo / 12 mo / 2nd / 3rd receiver) and pay (€142.80 or €238.00 per slot).
7. Activation within 2 working days after payment.
8. **Subscription renewal**: SMS + email reminder 5 days before expiry; renew via DLS Portal Subscriptions.

## Network Details

- **Operator:** Department of Lands and Surveys, Ministry of Interior of the Republic of Cyprus (`dls.moi.gov.cy`)
- **Network coverage:** 7 stations distributed across the government-controlled areas of Cyprus (Nicosia central, Limassol, Larnaca, Paphos, Paralimni, Polis, Evrychou). North-Cyprus areas are not covered.
- **Software stack:** Leica GNSS Spider + Spider Business Center (SBC) for user/account management, hosted on internal IP `213.7.195.11`
- **Reference frame:** ETRS89 / CGRS93 (Cyprus Geodetic Reference System 1993, ITRF-aligned)
- **Note on GPS phones:** "CYPOS services are not compatible with GPS mobile phones" — i.e., the corrections require an RTCM-capable surveying-grade or RTK-grade GNSS receiver (e.g., u-blox ZED-F9P based rovers, Trimble, Leica, Septentrio).

## Context Notes

- CYPOS is the **only** RTK correction service identified for Cyprus. There is no significant volunteer presence: zero CYP-coded rtk2go bases and zero Centipede nodes (verified against 2026-05 archives), and `stations_by_radius.py 35.0 33.0 100` returns no project-tracked stations within 100 km.
- The annual cost (€238) is **above** the project's $200/yr hobbyist guidance and would qualify CYPOS for "paid, above threshold" classification in `docs/networks.md`. The 6-month tier (€142.80) splits the year and stays just under the equivalent $200 at current EUR/USD rates — usable for short-term hobbyist projects.
- The **residency gate via Citizen Service Centre profile validation** is the practical barrier: a foreign visitor without a Cypriot civil-registration number ("Αριθμός Δελτίου Ταυτότητας") or residence permit will struggle to complete step 2 even if able to pay.
- ArduSimple's Cyprus NTRIP services guide (`ardusimple.com/rtk-correction-services-and-ntrip-casters-in-cyprus/`, observed 2026-04-30) confirms the service exists and is paid but does not list pricing — the figures here come from the official CYPOSNetwork.pdf Figure 4 screenshot.

## Contact for Access
- DLS Geodesy Department: `portal.dls.moi.gov.cy` (registration portal)
- General DLS contact: `dls.moi.gov.cy`
- No dedicated public phone or email for CYPOS specifically is listed

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **CYPOS data for post processing** — RINEX from same 7 stations, requested via DLS Portal | https://portal.dls.moi.gov.cy/ | Bundled with active CYPOS subscription |
| **EUREF EPN** — Cyprus stations contributed to European archive | https://epncb.oma.be/ | Free |

## Sources Consulted
- DLS main site: https://dls.moi.gov.cy (2026-04-30)
- DLS Portal CYPOS Network page: https://portal.dls.moi.gov.cy/en/alles-ypiresies/diktyo-cypos/ (HTTPS 200; 2026-05-12)
- DLS Portal CYPOS Network help page (en-us): https://portal.dls.moi.gov.cy/en-us/FrontEndHelp/Pages/CYPOS%20Network.aspx
- DLS Portal CYPOS registration form (Greek/EL): https://portal.dls.moi.gov.cy/en/application_forms/engrafi-cypos/
- DLS Portal Subscriptions help: http://portal.dls.moi.gov.cy/en-us/FrontEndHelp/Pages/Subscriptions.aspx
- **CYPOSNetwork.pdf (authoritative — official DLS help PDF, 4 pages)**: https://helpfiles.dls.moi.gov.cy/en-us/CYPOSNetwork.pdf (HTTP 200; 612 kB; downloaded and parsed 2026-05-12)
  - Figure 3 (SBC user registration form on `213.7.195.11/SBC/FrontendPage.aspx?mode=register`)
  - Figure 4 (Subscriptions: CYPOS 6 months €142.80, CYPOS 12 months €238.00, plus 2nd/3rd-receiver bundles at same per-receiver rate)
- ICA Cyprus National Report 2019–2023: https://icaci.org/files/documents/national_reports/2019-2023/Cyprus-2023.pdf (DLS / CYPOS context)
- ResearchGate CYPOS station map (7 stations): https://www.researchgate.net/figure/The-permanent-GNSS-network-of-Cyprus-CYPOS-red-circles-indicate-the-seven-stations_fig1_332131388
- gov.cy CYPOS registration service: https://www.gov.cy/en/service/cypos-cyprus-positioning-system-registration/ (HTTP 403 from research env; service entry confirmed via search index)
- ArduSimple Cyprus NTRIP guide: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-cyprus/ (2026-04-30)
- Direct probe `http://213.7.195.11/SBC/...` (research env 2026-05-12): connection timed out — caster network is geo-restricted to Cyprus IPs / DLS tenants

## Known Data Gaps
- **NTRIP caster host:port** for runtime correction stream — not advertised externally; only issued to subscribers after activation
- **VAT inclusivity** of the €142.80 / €238.00 figures — Cyprus standard VAT is 19%; whether the displayed price includes or excludes VAT is not annotated on the screenshot
- **Foreign-resident pathway**: no documented procedure for a non-resident hobbyist with a foreign passport to complete the Citizen Service Centre profile validation
