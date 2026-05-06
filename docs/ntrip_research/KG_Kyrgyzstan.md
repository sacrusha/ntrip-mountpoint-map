# Kyrgyzstan [KG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — KyrPOS national CORS/RTK network active; contract registration required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — KyrPOS (Kyrgyz Positioning System), operated by ГАЗРКГК (State Agency for Land Resources, Cadastre, Geodesy and Cartography of the Kyrgyz Republic / gosreg.gov.kg) |
| **host:port — KyrPOS** | `cors.gosreg.gov.kg : 8085` (source: gosreg.gov.kg/ky/?page_id=3029, observed 2026-05-06) |
| **tariff — KyrPOS** | 170 KGS / day per receiver · 3 180 KGS / month per receiver (minimum subscription: 1 month; weekends and public holidays not counted). Source: gosreg.gov.kg/ky/?page_id=3029, observed 2026-05-06. VAT inclusion not confirmed. |
| **hobbyist_eligibility** | Unclear — registration requires a signed contract with the receiver's make, model, and serial number; no individual/hobbyist category is listed. Bureaucratic friction is likely, but non-professionals are not explicitly excluded. |
| **legal_residency_required** | Unclear — workflow implies a Kyrgyz legal address for contract delivery (signed copies mailed back), but no explicit residency bar was found. |
| **last_confirmed_alive** | gosreg.gov.kg/ky/?page_id=3029 returned HTTP 200 on 2026-05-06. WebFetch of `cors.gosreg.gov.kg:8085` returned ECONNREFUSED on 2026-05-06 — port not reachable from outside (firewall or geo-block likely; caster may only accept connections after credential issuance). |

## Most Recent Project Announcement

KyrPOS is the national CORS RTK network managed by ГАЗРКГК (gosreg.gov.kg). The online connection form and detailed service description are active at https://gosreg.gov.kg/ky/?page_id=3029. The network operates 18 permanent CORS stations distributed across five geographic zones:

- 6 stations in Chui oblast (capital region / Bishkek area)
- 8 stations in the Fergana Valley (Osh, Jalal-Abad)
- 1 station in Naryn oblast
- 3 stations in Issyk-Kul oblast

An academic paper (ResearchGate: "GNSS Permanent Networks in Kyrgyzstan") documented an earlier iteration of the same network. The UN RCCAP-20 workshop presentation by Azamat Karypov (2020) confirms the KyrPOS Control Centre of CORS Network provides RTK satellite positioning service.

## Context Notes

- **NTRIP caster endpoint**: `cors.gosreg.gov.kg:8085`. This hostname and port were obtained directly from the official ГАЗРКГК service page (gosreg.gov.kg/ky/?page_id=3029) on 2026-05-06. Port 8085 is non-standard for NTRIP (standard is 2101) but used here. WebFetch probe returned ECONNREFUSED — likely filtered from outside Kyrgyzstan or restricted to credentialed IPs.
- **Access procedure (9 steps as listed on the official page)**:
  1. Download the contract template from gosreg.gov.kg.
  2. Fill in GNSS receiver make, model, serial number, and desired subscription period.
  3. Email the contract to kyrposgnss@gosreg.gov.kg.
  4. Receive login credentials by email.
  5. Receive two printed contract copies by mail.
  6. Sign and register the contracts.
  7. Make bank payment.
  8. Submit signed contract + payment receipt to the agency's physical office.
  9. Call 0312 664937 for questions or follow-up.
  Portal registration with QR-code payment is also available; multiple sub-accounts (per receiver) can be created under one portal account.
- **Tariff currency**: Kyrgyzstani Som (KGS). At May 2026 rates, 3 180 KGS/month ≈ USD 37 at market exchange rates. Whether this is inclusive of VAT (НДС) was not confirmed from the page.
- **Coverage gaps**: 18 stations across a mountainous country of ~200 000 km². The Chui plain and Fergana Valley have best coverage; Naryn, Batken, and parts of Jalal-Abad are underserved. High terrain in mountain corridors will degrade VRS performance.
- **Contact**: kyrposgnss@gosreg.gov.kg · phone 0312 664937 · general agency: gazr@mail.gov.kg · Bishkek, ul. Orozbekova 44, office hours.
- **CAIAG station**: The Central Asian Institute for Applied Geosciences (CAIAG, caiag.kg) operates scientific GNSS station BIK0/BIS2 in Bishkek for geodynamic research — not an RTK corrections stream.
- **Practical workaround**: Apply via gosreg.gov.kg/ky/?page_id=3029; alternatively deploy a local base station or use satellite PPP (Galileo HAS, Trimble RTX).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope / GAGE GNSS Archive** — IGS and regional stations in Kyrgyzstan | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |
| **CAIAG** — Central Asian Institute; scientific GNSS data, Bishkek area | http://www.caiag.kg | Contact required |

## Sources Consulted
- gosreg.gov.kg/ky/?page_id=3029 — KyrPOS official connection form; caster host:port `cors.gosreg.gov.kg:8085`, tariff 170 KGS/day · 3 180 KGS/month, 9-step registration, contact email kyrposgnss@gosreg.gov.kg, phone 0312 664937; observed 2026-05-06
- gosreg.gov.kg — agency home page and navigation structure; observed 2026-05-06
- ResearchGate — "GNSS Permanent Networks in Kyrgyzstan" (academic paper; 18-station breakdown by oblast confirmed)
- UN RCCAP-20 workshop — Azamat Karypov presentation "Department of Cadastre and Registration of Rights on Immovable Property" (2020, unstats.un.org)
- CAIAG Bishkek station page (caiag.kg)
- GitHub mvarga1989 — The-list-of-GNSS-CORS-RTK-networks (lists Kyrgyzstan / gosreg entry)
- RTK2go monitor — no Kyrgyzstan NTRIP streams confirmed
- ArduSimple country selector — no dedicated Kyrgyzstan page found
- WebFetch probe of `cors.gosreg.gov.kg:8085` — ECONNREFUSED 2026-05-06 (port not reachable from external network; caster may filter by IP or geo-block)
- WebFetch probe of `gosreg.gov.kg/ky/?page_id=3029` — HTTP 200 confirmed 2026-05-06
