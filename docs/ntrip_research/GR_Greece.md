# Greece [GR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (updated 2026-05-07: separated URANUS from HEPOS — URANUS is a private commercial network, not a HEPOS alias; re-verified 2026-05-12: HEPOS pricing unchanged on hepos.gr product pages, URANUS portal loads HTTP 200 with Greek content) (refresh 2026-05-17: hepos.gr product/about pages return HTTP 403 to anonymous WebFetch via Akamai — pricing assumed unchanged since 2026-05-12 reseller/search confirmations; no operator-citable HTRS07/ETRS89 datum declaration retrievable from this sandbox)

## Status: YES — national NTRIP RTK caster operating (HEPOS, paid); two private commercial networks (URANUS / TopNET, JGC-Net) also available; no free national NTRIP RTK in Greece

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid only) |
| **Network name — primary** | HEPOS (Hellenic POsitioning System) |
| **Operator — HEPOS** | KTIMATOLOGIO S.A. (Ελληνικό Κτηματολόγιο / Hellenic Cadastre) |
| **host:port — HEPOS** | Issued after registration. Public-facing site `www.hepos.gr`; the actual caster hostname is delivered with credentials. Earlier documentation cites `ntrip.hepos.gr:2101` but no public sourcetable is reachable anonymously. Akamai CDN on hepos.gr returns HTTP 403 to anonymous curl, so the pipeline cannot scrape a sourcetable directly. |
| **access_url — HEPOS** | https://www.hepos.gr/en/subscriptions-en/ (operator signup / subscriptions landing) |
| **VRS — HEPOS** | Yes — Network RTK / VRS corrections; RTCM 3.1 (GPS+GLONASS) and RTCM 3.2 MSM (full GNSS); 98 permanent reference stations covering all Greece including islands |
| **datum_epoch — HEPOS** | omitted — no citable declaration retrievable from this sandbox (hepos.gr Akamai 403 to anonymous WebFetch). HTRS07 (Hellenic Terrestrial Reference System 2007, Greek realization of ETRS89) is named in context but the operator URL declaring it is not directly fetchable this pass; defer rather than infer. |
| **tariff — 3 months flat-rate RTK** | €160.00 excl. VAT (source: hepos.gr/en/product/real-time-services-flat-rate-3-months-rtk/, observed 2026-05-06; carried forward, unverified at 2026-05-17 refresh — hepos.gr returns Akamai HTTP 403 to anonymous WebFetch) |
| **tariff — 1 year flat-rate RTK** | €480.00 excl. VAT (source: hepos.gr/en/product/real-time-services-flat-rate-1-year-rtk/, observed 2026-05-06; carried forward, unverified at 2026-05-17 refresh — Akamai 403) |
| **tariff — per-minute RTK bundle** | €90.00 excl. VAT one-time bundle (per-minute rate not separately published; source: hepos.gr/en/product/real-time-services-per-minute/, observed 2026-05-06; carried forward, unverified at 2026-05-17 refresh — Akamai 403) |
| **VAT** | Greek standard VAT is 24%; prices listed above are net |
| **hobbyist_eligibility — HEPOS** | Yes — individual registration accepted; no licensed-surveyor requirement stated |
| **legal_residency_required — HEPOS** | Unclear — subscription/payment is online; no explicit residency restriction; Greek VAT registration may be required to receive an invoice |
| **last_confirmed_alive — HEPOS** | 2026-05-12 (hepos.gr en/home page Akamai-protected, returns 403 to anonymous curl; product/subscription pages confirmed via WebSearch results 2026-05-12 — €160 / €480 / €90 product pages all still served) |
| **Network name — secondary 1** | URANUS — TopNET Live Greece |
| **Operator — URANUS** | Tree Company Corporation A.E.B.E. (Treecomp) — private commercial Topcon distributor |
| **host:port — URANUS** | `www.uranus.gr` / NTRIP caster credentials issued after registration. ntrip-list.com lists URANUS as the public free-trial face (3-day trial), commercial subscription thereafter |
| **VRS — URANUS** | Yes — VRS Network RTK; 117 reference stations across Greece + Cyprus; advertised 99% coverage; GPS, GLONASS, Galileo, BeiDou |
| **tariff — URANUS** | Paid (rates not publicly listed; 3-day free trial available; contact uranus@treecomp.gr / +30 210 9473600) |
| **last_confirmed_alive — URANUS** | 2026-05-12 (uranus.gr loaded HTTP 200 with full Joomla/Helix-Ultimate page in Greek; service marketed as the largest private CORS network in Greece, certified by NTUA) |
| **Network name — secondary 2** | JGC-Net |
| **Operator — JGC-Net** | JGC Geoinformation Systems S.A. (private Spectra/Nikon/NovAtel distributor) |
| **host:port — JGC-Net** | Not publicly listed; credentials issued after commercial registration with JGC |
| **tariff — JGC-Net** | Not publicly listed; contact jgc.gr |
| **VRS — JGC-Net** | Yes — fixed to HTRS07 reference system; ~2 cm accuracy within 50 km of each station |
| **last_confirmed_alive — JGC-Net** | 2026-05-12 (jgc.gr/jgc-net page reachable; no anonymous host:port or sourcetable advertised — endpoint gated behind commercial registration) |

## Context Notes

- **HEPOS** is operated by Hellenic Cadastre (KTIMATOLOGIO S.A.), a government-linked entity. The network comprises 98 permanent reference stations covering all of Greece including islands, supporting GPS, GLONASS, Galileo, and BeiDou. Launched 2008; continuously upgraded.
- **Reference system**: HTRS07 (Hellenic Terrestrial Reference System 2007), the Greek realization of ETRS89.
- **HEPOS tariff structure**: Three distinct products — per-minute (pay-as-you-go bundle), 3-month flat-rate, 1-year flat-rate. Unlimited usage within the flat-rate period. All prices published on the hepos.gr webshop in English.
- **URANUS / TopNET Live Greece**: A private commercial network operated by Tree Company Corporation (Treecomp), Topcon's distributor in Greece. Despite being free-trial-friendly (3-day trial), it is not a free service — it is a competitor to HEPOS aimed at commercial surveyors. Earlier internal documentation in this repository conflated `uranus.gr:2101` with the HEPOS endpoint, which is incorrect: URANUS is its own caster.
- **JGC-Net**: A private network run by JGC Geoinformation Systems (distributor for Spectra, Nikon, NovAtel, DJI in Greece). Operates its own CORS in northern/central Greece and islands, supplementing HEPOS. Marketed as providing >50 km baseline coverage. Pricing not publicly listed; oriented towards professional surveying customers.
- **Hobbyist note**: HEPOS allows individual online registration and payment with credit card. No professional-licensing check is documented. The per-minute bundle (€90 + VAT) is the lowest-commitment entry point; the 3-month flat-rate (€160 + VAT ≈ €198 incl. VAT, ~$215) covers a single project at unlimited usage.
- **DGNSS**: HEPOS also provides a DGPS/DGNSS service (sub-meter) at lower cost; out of scope for this research.
- **Volunteer footprint (separately noted in country-survey, out of scope here)**: a small number of rtk2go and Centipede-RTK Greek bases are documented in the repository's pipeline data — 1 rtk2go (`NTAGIAS`, 39.19 N 22.68 E, Thessaly) and 3 Centipede-RTK (`ANOCH`, `MYRO`, `RGEO`) in the data/stations.json 2026-05-12 fetch. Thin compared to HU/FR.

## Post-Processing (RINEX) Fallback

HEPOS offers post-processing RINEX download from registered reference stations. Access requires a HEPOS account; post-processing is available through the HEPOS web portal.

| Service | URL | Cost |
|---|---|---|
| **HEPOS RINEX download** | https://www.hepos.gr/ (login required) | Included with subscription or separate fee |
| **EUREF / EPN archive (NOA1, etc.)** | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- HEPOS English home: https://www.hepos.gr/en/home/
- HEPOS 3-month flat-rate product: https://www.hepos.gr/en/product/real-time-services-flat-rate-3-months-rtk/
- HEPOS 1-year flat-rate product: https://www.hepos.gr/en/product/real-time-services-flat-rate-1-year-rtk/
- HEPOS per-minute product: https://www.hepos.gr/en/product/real-time-services-per-minute/
- HEPOS subscriptions page: https://www.hepos.gr/en/subscriptions-en/
- HEPOS Q&A: https://www.hepos.gr/en/qa/
- HEPOS gov.gr listing: https://www.gov.gr/en/upourgeia/upourgeio-psephiakes-diakuberneses/elleniko-ktematologio-ae/elleniko-sustema-entopismou-theses-hepos
- URANUS / TopNET Live Greece: https://www.uranus.gr/home-page (operator: Tree Company Corporation, contact uranus@treecomp.gr)
- URANUS as listed on ntrip-list Europe: https://ntrip-list.com/europe/
- JGC-Net: https://www.jgc.gr/jgc-net/?lang=en
- ArduSimple Greece overview: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-greece/
