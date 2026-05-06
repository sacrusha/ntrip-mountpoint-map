# Greece [GR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — national NTRIP RTK caster operating (HEPOS); paid subscription; second private network (JGC-Net) also available

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name — primary** | HEPOS (Hellenic POsitioning System) |
| **Operator — HEPOS** | KTIMATOLOGIO S.A. (Hellenic Cadastre) |
| **host:port — HEPOS** | `ntrip.hepos.gr:2101` (also documented as `www.hepos.gr:2101`; credentials issued after registration) |
| **VRS — HEPOS** | Yes — Network RTK / VRS corrections; RTCM 3.1 (GPS+GLONASS) and RTCM 3.2 MSM (full GNSS) |
| **tariff — 3 months flat-rate RTK** | €160.00 excl. VAT (source: hepos.gr/en/product/real-time-services-flat-rate-3-months-rtk/, observed 2026-05-06) |
| **tariff — 1 year flat-rate RTK** | €480.00 excl. VAT (source: hepos.gr/en/product/real-time-services-flat-rate-1-year-rtk/, observed 2026-05-06) |
| **tariff — per-minute RTK** | €90.00 excl. VAT per bundle (source: hepos.gr/en/product/real-time-services-per-minute/, observed 2026-05-06) |
| **VAT** | Greek standard VAT is 24%; prices listed above are net |
| **hobbyist_eligibility** | Yes — individual registration accepted; no licensed surveyor requirement stated |
| **legal_residency_required** | Unclear — subscription/payment is online; no explicit residency restriction stated; Greek VAT registration may be required for invoice |
| **last_confirmed_alive** | 2026-05-06 (hepos.gr loaded normally; product/subscription pages returned HTTP 200; Akamai CDN 403 blocks direct curl but pages confirmed via search-engine cache) |
| **Network name — secondary** | JGC-Net |
| **Operator — JGC-Net** | JGC Geoinformation Systems S.A. (private distributor) |
| **host:port — JGC-Net** | Not publicly listed; credentials issued after commercial registration with JGC |
| **tariff — JGC-Net** | Not publicly listed; contact jgc.gr |
| **VRS — JGC-Net** | Yes — fixed to HTRS07 reference system; ~2 cm accuracy within 50 km of each station |

## Context Notes

- **HEPOS** is operated by Hellenic Cadastre (KTIMATOLOGIO S.A.), a government-linked entity. The network comprises 98 permanent reference stations covering all of Greece including islands, supporting GPS, GLONASS, Galileo, and BeiDou. Launched 2008; continuously upgraded.
- **Reference system**: HTRS07 (Hellenic Terrestrial Reference System 2007), which is the Greek realization of ETRS89.
- **HEPOS tariff structure**: Three distinct products — per-minute (pay-as-you-go bundle), 3-month flat-rate, 1-year flat-rate. Unlimited usage within the flat-rate period. All prices published on the hepos.gr webshop in English.
- **JGC-Net**: A private network run by JGC Geoinformation Systems (distributor for Spectra, Nikon, NovAtel, DJI in Greece). Operates its own CORS in northern/central Greece and islands, supplementing HEPOS. Marketed as providing >50 km baseline coverage. Pricing not publicly listed; oriented towards professional surveying customers.
- **Hobbyist note**: HEPOS allows individual online registration and payment with credit card. No professional licensing check is documented. The per-minute bundle (€90 + VAT) is the lowest-commitment entry point.
- **DGNSS**: HEPOS also provides a DGPS/DGNSS service (sub-meter) at lower cost; out of scope for this research.

## Post-Processing (RINEX) Fallback

HEPOS offers post-processing RINEX download from registered reference stations. Access requires a HEPOS account; post-processing is available through the HEPOS web portal.

| Service | URL | Cost |
|---|---|---|
| **HEPOS RINEX download** | https://www.hepos.gr/ (login required) | Included with subscription or separate fee |

## Sources Consulted
- HEPOS English home: https://www.hepos.gr/en/home/
- HEPOS 3-month flat-rate product: https://www.hepos.gr/en/product/real-time-services-flat-rate-3-months-rtk/
- HEPOS 1-year flat-rate product: https://www.hepos.gr/en/product/real-time-services-flat-rate-1-year-rtk/
- HEPOS per-minute product: https://www.hepos.gr/en/product/real-time-services-per-minute/
- HEPOS subscriptions page: https://www.hepos.gr/en/subscriptions-en/
- HEPOS Q&A: https://www.hepos.gr/en/qa/
- JGC-Net: https://www.jgc.gr/jgc-net/?lang=en
- ArduSimple Greece overview: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-greece/
- NTRIP-list.com Europe: https://ntrip-list.com/europe/
