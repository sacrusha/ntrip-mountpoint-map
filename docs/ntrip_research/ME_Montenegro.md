# Montenegro [ME] — NTRIP RTK Research

**researched:** 2026-05-21 (refresh of 2026-05-17, 2026-05-06)
**status:** YES — single national NTRIP caster (MontePos, Uprava za nekretnine); endpoint not published; paid subscription. No volunteer base within practical RTK range.

## MontePos — Mreža Stalnih GNSS Stanica Crne Gore

| field | value |
|---|---|
| landing_url | https://www.gov.me/clanak/montepos — operator info + application + payment instructions; endpoint disclosed only after sign-up |
| access_url | https://www.gov.me/clanak/montepos (same page — application form download + giro instructions; no self-service web form) |
| operator | Uprava za nekretnine (Real Estate Administration), Vlada Crne Gore |
| admin contact | Goran Popović, Načelnik odsjeka za geodetske radove i državnu granicu — +382 67 641 119 — `uznmontepos@gmail.com` |
| num_stations | 9 |
| host:port | Null — not published on any public-facing page. NTRIP endpoint disclosed only after signed application + payment. |
| vrs | ? — published technical materials gated behind the `wapi.gov.me` PDF; no public sourcetable to probe. 9 CORS over Montenegro (~14,000 km², mountainous interior) at mean ~40-50 km spacing suggests single-base/nearest-station delivery is most likely; full VRS requiring rover GGA round-trip is possible but unconfirmed without the technical PDF. |
| tariff | Null — figures live in https://wapi.gov.me/download/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0?version=1.0 ("MontePos- tehnički detalji", 382 KB, published 2024-04-11). Domain `wapi.gov.me` not accessible from research environment; PDF was the same edition at 2026-05-21 refresh. No EUR figures found on the gov.me landing page (WebFetch 2026-05-21 confirms subscription periods only: `24h, 48h, 1 mjesec, 3 mjeseca, 6 mjeseci, 1 godinu i 2 godine`). Secondary search (Montenegrin surveying forums, community sites) returned no secondary pricing source. Currency EUR (Montenegro uses EUR; no Montenegrin national currency). VAT treatment unstated. |
| payment process | Giro account 832-1081-58, purpose "Montepos - RTK"; signed application form to `uznmontepos@gmail.com` or to UZN counter offices |
| application form | https://wapi.gov.me/download/3647961e-34ab-41e7-9bf6-282a116f72ff?version=1.0 (394 KB, 2024-04-11) |
| service modules | MontePos-RTK and MontePos-PPK (post-processed kinematic). Established 2005; published 2-3 cm RTK accuracy. |
| hobbyist_eligibility | yes (likely) — public page mentions no professional-licence requirement; application appears open to natural persons |
| legal_residency_required | ? — giro-account payment + in-person counter handling imply resident workflow; no explicit exclusion of non-residents |
| last_confirmed_alive | 2026-05-21 — gov.me/clanak/montepos still publication-dated 2024-04-11; page renders with subscription periods unchanged. NTRIP caster endpoint unknown for independent verification. |
| datum_epoch | omitted — no operator-citable declaration on the public page. Montenegro uses MNE_ETRS89 / ETRF2000 (epoch widely cited as 2008.x in EUREF densification literature) but Uprava za nekretnine does not publish epoch on `gov.me/clanak/montepos`. |

## Context

- **Endpoint not public**. Users must submit a signed application form (PDF) and make payment to a giro account, after which the NTRIP hostname/IP and credentials are disclosed. Common pattern for Balkan government CORS networks.
- **Technical details**. The "MontePos- tehnički detalji" PDF (382 KB, 2024-04-11) is described as containing both full technical parameters and the price list ("zahtjev sa cjenovnikom"). This is the authoritative tariff source but was inaccessible from the research environment.
- **No free tier**. No free or open-access NTRIP stream documented for Montenegro.
- **Volunteer / cross-border coverage**: `py scripts/stations_by_radius.py 42.5 19.3 250` returned zero rtk2go / Centipede / EarthScope volunteer stations within 250 km of Podgorica on 2026-05-12. No free cross-border alternative is in practical RTK baseline range.

## Sources

- MontePos public page (Montenegrin): https://www.gov.me/clanak/montepos (WebFetch 2026-05-21 — periods confirmed; no EUR figures inline; contact details unchanged)
- Real Estate Administration: https://www.uzn.me/ (TLS/connection errors from sandbox; cited in third-party material as the canonical MontePos pricing host)
- Tariff PDF (inaccessible from sandbox but operator-authoritative): https://wapi.gov.me/download/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0?version=1.0 · mirror https://www.gov.me/dokumenta/8f6d09ed-f1d2-4650-9e87-d8d91d2526b0
- Application form: https://wapi.gov.me/download/3647961e-34ab-41e7-9bf6-282a116f72ff?version=1.0
- ArduSimple Montenegro: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-montenegro/ — "as far as we know Montenegro is not among them" (out of date: MontePos exists since 2005).
- Local: `py scripts/stations_by_country.py MNE` → "No stations" 2026-05-21.
