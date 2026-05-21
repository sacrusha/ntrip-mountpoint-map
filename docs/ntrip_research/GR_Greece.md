# Greece [GR] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-12, 2026-05-06)
**status:** YES — national paid NTRIP (HEPOS, KTIMATOLOGIO S.A.) + two private commercial networks (URANUS / TopNET Live Greece, JGC-Net). No free national NTRIP RTK. Modest volunteer footprint (1 rtk2go + 3 Centipede GR bases).

## Caster 1 — HEPOS (Hellenic Positioning System, national paid)

| field | value |
|---|---|
| landing_url | https://www.hepos.gr/en/home/ |
| access_url | https://www.hepos.gr/en/subscriptions-en/ |
| operator | KTIMATOLOGIO S.A. (Ελληνικό Κτηματολόγιο / Hellenic Cadastre) |
| host:port | Issued after registration. Public-facing site `www.hepos.gr`. Earlier documentation cites `ntrip.hepos.gr:2101` but the subdomain does not resolve from the sandbox 2026-05-21 (no public sourcetable reachable anonymously). Akamai CDN on `hepos.gr` returns HTTP 403 to anonymous curl, so the pipeline cannot scrape a sourcetable directly. |
| vrs | yes — Network RTK / VRS corrections; RTCM 3.1 (GPS+GLO) and RTCM 3.2 MSM (full GNSS) |
| num_stations | 98 permanent reference stations across all Greece including islands |
| tariff — 3-month flat-rate RTK | €160,00 excl. VAT (re-confirmed via WebSearch 2026-05-21; hepos.gr product page returns Akamai 403 to anonymous WebFetch — WebSearch result includes the figure) |
| tariff — 1-year flat-rate RTK | €480,00 excl. VAT (same source) |
| tariff — "per minute" RTK product | €90,00 excl. VAT — this is the product named "Real time Services per minute" on the HEPOS webshop (URL: https://www.hepos.gr/en/product/real-time-services-per-minute/); based on the product name it is a pre-paid usage bundle at a per-minute consumption rate, but the specific minute bundle size and per-minute rate are not stated on publicly accessible pages (hepos.gr Akamai 403). Do not confuse with the 3-month flat-rate (€160,00 excl. VAT). |
| VAT | Greek standard VAT 24%; prices above net |
| hobbyist_eligibility | yes — individual registration accepted; no licensed-surveyor requirement stated |
| legal_residency_required | ? — subscription/payment online; no explicit residency restriction; Greek VAT registration may be required for the invoice |
| last_confirmed_alive | 2026-05-21 — hepos.gr en/home page Akamai 403 to anonymous curl (expected); product/subscription pages confirmed via WebSearch result 2026-05-21 with the same €160 / €480 / €90 figures still served |
| datum_epoch | omitted — hepos.gr returns Akamai 403 to anonymous requests; no operator page declaring HTRS07 for HEPOS streams was accessible from this sandbox. HTRS07 (Hellenic Terrestrial Reference System 2007, Greek realization of ETRS89 aligned to ETRF2005 at epoch 2007.5) is confirmed as the national geodetic frame in academic literature and is declared by JGC-Net for its own caster, but the primer's citation rule requires an operator portal URL — none accessible for HEPOS specifically. gov.gr service entry for HEPOS also returned 403. Defer rather than infer. |

## Caster 2 — URANUS / TopNET Live Greece (private commercial)

| field | value |
|---|---|
| landing_url | https://www.uranus.gr/home-page |
| access_url | https://www.uranus.gr/program-details (subscription form + plans; 3-day free trial; commercial subscription) |
| operator | Tree Company Corporation A.E.B.E. (Treecomp) — private Topcon distributor; contact `uranus@treecomp.gr` / +30 210 9473600 |
| host:port | NTRIP caster credentials issued after registration; `ntrip-list.com` lists URANUS publicly via the 3-day free trial workflow |
| vrs | yes — VRS Network RTK; GPS, GLONASS, Galileo, BeiDou |
| num_stations | 117 reference stations spanning Greece + Cyprus combined (operator-stated on `uranus.gr/kalipsi` 2026-05-21: "117 Μόνιμοί Σταθμοί Αναφοράς" with coverage map showing both GR mainland/islands and CY); per-country split not disclosed by operator |
| tariff | Paid; rates not publicly listed. 3-day free trial available. Contact `uranus@treecomp.gr` / +30 210 9473600. |
| hobbyist_eligibility | ? — designed for commercial surveyors; trial workflow at least technically accessible to individuals |
| legal_residency_required | ? — Cyprus office exists for CY users; Greek mainland access logistics not explicitly stated |
| last_confirmed_alive | 2026-05-21 — `uranus.gr/kalipsi` WebFetch 200, confirms "117 Μόνιμοι Σταθμοί Αναφοράς" + Greece+Cyprus coverage; Joomla/Helix-Ultimate landing intact |
| datum_epoch | omitted — not publicly declared |

## Caster 3 — JGC-Net (private commercial)

| field | value |
|---|---|
| landing_url | https://www.jgc.gr/jgc-net/?lang=en |
| access_url | https://www.jgc.gr/jgc-net/?lang=en — same page; no separate self-service signup portal. Contact `cdounias@jgc.gr` / +302108023917 for trial credentials and subscription. |
| operator | JGC Geoinformation Systems S.A. (private Spectra / Nikon / NovAtel / DJI distributor) |
| host:port | `ntrip.jgc.gr:2201` — listed on ntrip-list.com and sourcetable.htm URL confirmed (WebSearch 2026-05-21). TCP probe from sandbox timed out (port 2201 firewalled to sandbox egress; consistent with other geo-restricted Balkan casters). |
| vrs | yes — NRTK corrections; RTCM 3.1 (GPS+GLO) and RTCM 3.2 MSM (full GNSS). ~2 cm accuracy within 50 km of each station per operator page. |
| tariff | Not publicly listed; contact `cdounias@jgc.gr` |
| hobbyist_eligibility | ? — page targets professional surveyors; trial credentials available on request; commercial subscription terms not published |
| legal_residency_required | ? — not stated; CY office exists suggesting cross-country access |
| last_confirmed_alive | 2026-05-21 — jgc.gr/jgc-net page WebFetch 200 (page dateModified 2025-07-14 per schema.org metadata) |
| datum_epoch | HTRS07 operator-declared on jgc.gr/jgc-net: "stations are fixed to the HEPOS Reference System (HTRS07: Hellenic Terrestrial Reference System 2007)." Epoch not stated. |

## Context

- **HEPOS** is operated by Hellenic Cadastre (KTIMATOLOGIO S.A.), a government-linked entity. Launched 2008; continuously upgraded. 98 permanent reference stations covering all of Greece including islands.
- **HEPOS tariff structure**: three distinct products — per-minute (pay-as-you-go bundle), 3-month flat-rate, 1-year flat-rate. Unlimited usage within the flat-rate period. All prices published on the hepos.gr webshop in English.
- **URANUS / TopNET Live Greece**: private commercial network operated by Tree Company Corporation (Treecomp), Topcon's Greek distributor. Despite being free-trial-friendly (3 days), it is not a free service — it is a paid competitor to HEPOS aimed at commercial surveyors. Earlier internal docs in this repo conflated `uranus.gr:2101` with the HEPOS endpoint, which is incorrect: URANUS is its own caster.
- **JGC-Net**: private network run by JGC Geoinformation Systems. Operates its own CORS in northern/central Greece and islands, supplementing HEPOS. Marketed as providing >50 km baseline coverage. Pricing not public.
- **Hobbyist note**: HEPOS allows individual online registration and payment with credit card; no professional-licensing check is documented. The per-minute bundle (€90 + VAT) is the lowest-commitment entry; the 3-month flat (€160 + VAT ≈ €198 incl. VAT, ~$215) covers a single project at unlimited usage.
- **DGNSS** (HEPOS sub-meter tier) is out of scope.

## Volunteer footprint (2026-05-21)

- **rtk2go** (`GRC`, 1 base): `NTAGIAS` (Almyros, 39.19 N 22.68 E, RTCM 3.2 GPS+GLO+GAL+BDS).
- **Centipede** (`GRC`, 3 bases): `ANOCH` (39.312 N 22.305 E, Unicore UM982), `MYRO` (40.978 N 24.932 E, Unicore UM982), `RGEO` (39.341 N 22.608 E, U-blox ZED-F9P).
- **EUREF**: 2 GRC stations. **IGS-IP**: 2 GRC stations. Useful for RINEX, not for commodity RTK.

Thin compared to HU / FR / SRB volunteer meshes. Mainland Thessaly (Volos area) has practical free coverage via NTAGIAS + ANOCH + RGEO triangle; rest of mainland Greece + islands need HEPOS or URANUS.

## Post-processing fallback

| Service | URL | Cost |
|---|---|---|
| HEPOS RINEX download | https://www.hepos.gr/ (login required) | Included with subscription or separate fee |
| EUREF / EPN archive (NOA1 + others) | https://www.epncb.oma.be/ | free |

## Sources

- HEPOS English home: https://www.hepos.gr/en/home/ (Akamai 403 anonymous; WebSearch + product-URL discovery confirms pricing)
- HEPOS 3-month product: https://www.hepos.gr/en/product/real-time-services-flat-rate-3-months-rtk/
- HEPOS 1-year product: https://www.hepos.gr/en/product/real-time-services-flat-rate-1-year-rtk/
- HEPOS per-minute product: https://www.hepos.gr/en/product/real-time-services-per-minute/
- HEPOS subscriptions: https://www.hepos.gr/en/subscriptions-en/
- HEPOS Q&A: https://www.hepos.gr/en/qa/
- HEPOS gov.gr: https://www.gov.gr/en/upourgeia/upourgeio-psephiakes-diakuberneses/elleniko-ktematologio-ae/elleniko-sustema-entopismou-theses-hepos
- URANUS / TopNET Live Greece: https://www.uranus.gr/home-page · coverage page https://uranus.gr/kalipsi (WebFetch 2026-05-21: 117 stations, Greece+Cyprus)
- URANUS on ntrip-list Europe: https://ntrip-list.com/europe/
- JGC-Net: https://www.jgc.gr/jgc-net/?lang=en (WebFetch 2026-05-21 — HTRS07 declared; host ntrip.jgc.gr:2201 per ntrip-list + search result 2026-05-21)
- JGC-Net sourcetable URL: http://ntrip.jgc.gr:2201/sourcetable.htm (ECONNREFUSED from sandbox 2026-05-21)
- ArduSimple GR: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-greece/
- Local: `data/centipede.sourcetable` 2026-05-21 (ANOCH, MYRO, RGEO); `data/rtk2go.sourcetable` 2026-05-21 (NTAGIAS); `py scripts/stations_by_country.py GRC` → 3 centipede + 1 rtk2go + 2 EUREF + 2 IGS
