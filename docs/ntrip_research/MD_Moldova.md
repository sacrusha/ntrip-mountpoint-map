# Moldova [MD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior 2026-05-17, 2026-05-06)
**Exchange rate used:** ~17.7 MDL / 1 USD (approximate spot, May 2026)

## Status: YES — MOLDPOS national RTK network active; paid; published tariff schedule found; open to any GPS receiver owner

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — MOLDPOS (Moldova Positioning System), operated by S.E. INGEOCAD under the Agency for Geodesy, Cartography and Cadastre (AGCC / agcc.gov.md) |
| **landing_url** | https://moldpos.md/ — operator-owned MOLDPOS service site (RO/RU); describes the network, mountpoints (VRS/MAX/MSM, FreeZone), test credentials. Alternative: https://agcc.gov.md/content/moldpos (AGCC agency-level MOLDPOS page). |
| **access_url** | http://moldpos.md/index.php?option=com_content&view=featured&Itemid=546&lang=RO — MOLDPOS "Documente importante" page links the tariff PDF, RTK manual, RINEX manual, and SBC registration. Registration form itself at http://moldpos.ingeocad.md/SBC/Account/Register (Leica Spider Business Center). |
| **host:port** | `185.108.183.29:8080` (updated from former IP 188.237.130.50:8080). SBC portal: `moldpos.ingeocad.md`. Source: moldpos.md official pages. |
| **num_stations** | 10+ permanent GNSS stations (network founded 2011 with 10 stations; 2025 INGEOCAD procurement "Bunuri și servicii pentru modernizarea Sistemului Național de Poziționare MOLDPOS (utilaje GNSS)" at 2,000,000 MDL confirmed on e-licitatie.md — adds GNSS equipment; specific Spider licence count and post-expansion CORS total not publicly stated; sourcetable as of 2026-05-21 shows 9+ STR rows) |
| **vrs** | Yes — mountpoints `VRS` (Virtual Reference Station), `MAX` (master-auxiliary), `MSM` (RTCM 3 MSM, GPS+GLO+GAL), `NEAREST` (nearest-station); plus free test mountpoints `FZUTM`, `FZUASM`, `FZMA`, `FZINGEOCAD`, `FZCDEIC` |
| **tariff — RTK 100** | 252.00 MDL/month inclusive of TVA = 210.00 MDL net + 42.00 MDL TVA (20%); 100 minutes/month (over-package 2.10 MDL/min); source: http://moldpos.md/images/publish_docs/MP_Tarife__Cu_TVA_2013.xls.pdf, observed 2026-05-21 |
| **tariff — RTK 400** | 828.00 MDL/month inclusive of TVA = 690.00 MDL net + 138.00 MDL TVA (20%); 400 minutes/month (over-package 2.10 MDL/min); same source |
| **tariff — RTK PRO** | 2,208.00 MDL/month inclusive of TVA = 1,840.00 MDL net + 368.00 MDL TVA (20%); unlimited; same source |
| **tariff — RINEX download** | 36.00 MDL inclusive of TVA = 30.00 MDL net + 6.00 MDL TVA per 1 hour of RINEX data per CORS; same source |
| **tariff — additional decoding (KML, XLSX)** | 30.00 MDL inclusive of TVA = 25.00 MDL net + 5.00 MDL TVA |
| **tariff — free trial mountpoints** | "FreeZone" mountpoints (FZUTM, FZUASM, FZMA, FZINGEOCAD, FZCDEIC) accessible with shared credentials `moldpos` / `moldpos` — no subscription. These cover specific test campuses (university buildings, ministry sites), not the full national coverage. |
| **VAT status** | All MOLDPOS tariffs are denominated **с НДС / cu TVA** (TVA included; 20% standard rate) on the published price list. |
| **tariff context (2024 reduction)** | An October 2024 AGCC order (Order No. 115 of 29.10.2024) is described in public-search result summaries as directing INGEOCAD to reduce MOLDPOS tariffs for economic agents effective 1 December 2024. No direct page fetch of the order has been completed — the moldpos.md news URL returns HTTP 404 and no AGCC/Monitorul Oficial direct link was found in research. The published price-list PDF served as of 2026-05-21 is the same 2013 reference (RTK 100 / 400 / PRO + RINEX). Whether the December 2024 reduction is already reflected in this PDF or applies only to B2B invoicing is unknown. Confirm with `moldpos@ingeocad.md` before relying on the above figures as current invoice prices. |
| **datum_epoch** | omitted — no citable operator declaration. INGEOCAD/AGCC prose mentions ETRS89 alignment (EuroGeographics context) but no operator-side stream/portal cite states the caster output frame. |
| **hobbyist_eligibility** | Yes — INGEOCAD declares "MOLDPOS is an open network; any GPS receiver owner can join" ("MOLDPOS – ОТКРЫТАЯ СЕТЬ: ЛЮБОЙ ОБЛАДАТЕЛЬ GPS ПРИЕМНИКА МОЖЕТ ПРИСОЕДИНИТЬСЯ К НАМ"). Registration via SBC portal appears sufficient; no licensed-surveyor restriction found. Cheapest paid tier RTK 100 (~$14/mo) is well inside hobbyist range. |
| **legal_residency_required** | ? — not stated. Order No. 115 of 29.10.2024 mentions "agenți economici" (economic agents) for the tariff reduction, hinting at a Moldovan-business orientation, but the standard tariff schedule does not impose a residency clause. Contract execution likely needs a Moldovan invoicing identity; ask INGEOCAD before paying from abroad. |
| **last_confirmed_alive** | 2026-05-21 — direct probe of `185.108.183.29:8080` returned `SOURCETABLE 200 OK`, Server `GNSS Spider 7.10.1.168/1.0`, Date `Thu, 21 May 2026`, Content-Length 2,317, 9+ STR rows including `VRS`, `MAX`, `MSM`, `NEAREST`, `FZUTM`, `FZINGEOCAD`, `FZUASM`. moldpos.ingeocad.md SBC portal also alive. |

## Most Recent Project Announcements

- **2024 tariff reduction** — AGCC Order No. 115 of 29 October 2024 is referenced in public-search descriptions as directing INGEOCAD to reduce MOLDPOS tariffs for "agenți economici" starting 1 December 2024. No direct document fetch confirmed (moldpos.md news link HTTP 404; no Monitorul Oficial URL found). The PDF served at moldpos.md as of 2026-05-21 still shows the 2013 four-tier structure. The order is not independently verified; treat this claim as unconfirmed until a direct source is found.
- **2025 modernisation** — INGEOCAD procurement "Bunuri și servicii pentru modernizarea Sistemului Național de Poziționare MOLDPOS (utilaje GNSS)" confirmed on e-licitatie.md (ID on INGEOCAD profile; value 2,000,000 MDL, 2025). Specific equipment breakdown (Leica Spider licences vs. field receivers vs. infrastructure) not stated in the tender listing; post-expansion CORS count not publicly announced.
- **Galileo integration** — MOLDPOS now broadcasts GPS+GLONASS+Galileo on the `MSM` mountpoint; BeiDou added on `NEAREST` (RTCM 3 GPS+GLO+GAL+BDS per sourcetable 2026-05-21).

## Context Notes

- **Caster connection details**:
  - IP: `185.108.183.29` · Port: `8080` (non-standard; Leica Spider NTRIP caster default)
  - Former IP `188.237.130.50:8080` is superseded — use the current IP above
  - SBC web portal: http://moldpos.ingeocad.md/SBC/
  - Registration (new account): http://moldpos.ingeocad.md/SBC/Account/Register (Leica Spider Business Center)
  - Station status map: http://moldpos.ingeocad.md/SBC/User/SiteMap/SiteMapPublic
- **Mountpoints (from 2026-05-21 sourcetable)**:
  - Production: `VRS` (RTCM 3 GPS+GLO+GAL), `MAX` (RTCM 3 GPS+GLO master-auxiliary), `MSM` (RTCM 3 GPS+GLO+GAL), `NEAREST` (RTCM 3 GPS+GLO+GAL+BDS)
  - Free test ("FreeZone" — credentials `moldpos` / `moldpos`): `FZUTM` (Technical University of Moldova), `FZUASM` (State Agrarian University), `FZMA` (Ministry of Defence), `FZINGEOCAD`, `FZCDEIC` (Centre of Excellence in Construction)
- **Tariff lineage**: Service became paid per AGCC Order No. 04 of 06.01.2012. Current published price list at moldpos.md remains the "Tarife cu TVA" PDF with the four-tier structure above; 2024 reduction order text not separately published. Per-package overuse pricing 2.10 MDL/min applies on RTK 100 / RTK 400.
- **Accuracy**: RTK via VRS/MAX/MSM — cm-level precision using RTCM and TCP/IP delivery via NTRIP protocol.
- **Contact**: moldpos@ingeocad.md · info@ingeocad.md · +373 22 881200 · Chișinău, str. Pușkin 47, of. 225 · Tel. 022 881 214 (MOLDPOS desk)
- **AGCC**: info@agcc.gov.md · +373 22 881255
- **Practical workaround**: Register at moldpos.ingeocad.md/SBC/Account/Register; test free zones (FZxxx mountpoints, credentials moldpos/moldpos) before paying. Contact moldpos@ingeocad.md to confirm whether the post-2024 reduction adjusts the listed tariffs.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **MOLDPOS SBC** — RINEX data for registered users; historical observations | http://moldpos.ingeocad.md/SBC/ | Paid; contact INGEOCAD |
| **EarthScope GNSS Data Archive** — IGS/EUREF-affiliated Moldova stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |
| **EUREF Permanent GNSS Network (EPN)** — regional CORS near Moldova | https://epncb.oma.be/ | Free (account required) |

## Sources Consulted
- moldpos.md (official MOLDPOS site) — caster IP 185.108.183.29:8080; mountpoints VRS/MAX/MSM/NEAREST + FreeZone; test credentials moldpos/moldpos; Galileo note; re-checked 2026-05-21
- moldpos.md "Documente importante": http://moldpos.md/index.php?option=com_content&view=featured&Itemid=546&lang=RO (links the tariff PDF, RTK manual, RINEX manual)
- MOLDPOS published tariff PDF: http://moldpos.md/images/publish_docs/MP_Tarife__Cu_TVA_2013.xls.pdf — extracted 2026-05-21 (URL obtained by following link from the moldpos.md "Documente importante" page at http://moldpos.md/index.php?option=com_content&view=featured&Itemid=546&lang=RO, not a guessed URL): RTK 100 = 252 MDL TTC (100 min/mo, overuse 2.10 MDL/min); RTK 400 = 828 MDL TTC (400 min/mo, overuse 2.10 MDL/min); RTK PRO = 2,208 MDL TTC (unlimited); RINEX 36 MDL TTC per 1 h; decoding services 30 MDL TTC; 20% TVA included throughout
- moldpos.ingeocad.md/SBC — Leica Spider Business Center; HTTP 200 confirmed 2026-05-21
- ingeocad.md — "MOLDPOS open network, any GPS receiver owner can join" (Russian text); 2025 modernisation procurement note (5 new Spider licences); contact info@ingeocad.md, +373 22 881200
- agcc.gov.md/content/moldpos — AGCC MOLDPOS page; EU candidate country / EuroGeographics context
- AGCC Order No. 115 of 29.10.2024 (tariff reduction for economic agents, effective 1 December 2024) — referenced in public-search summaries only; moldpos.md news article URL (Itemid=435) returns HTTP 404; no direct document fetch completed; no Monitorul Oficial or AGCC page fetch confirming the order text. Claim unverified by direct source.
- INGEOCAD procurement 2025 — e-licitatie.md INGEOCAD profile (https://e-licitatie.md/organizatii/1951/ingeocad): "Bunuri și servicii pentru modernizarea Sistemului Național de Poziționare MOLDPOS (utilaje GNSS)", value 2,000,000 MDL, 2025; confirms active modernisation but not the specific equipment count
- elicitatie.md tender "Servicii Moldpos RTK 400" (ID 21131053, 14 Dec 2023) — confirms RTK 400 SKU exists as a stand-alone procurable item; estimated 690 MDL net (matches published tariff): https://elicitatie.md/en/public/tender/21131053/
- moldpos.md tariff news (2016 temporary modification): http://moldpos.md/index.php?option=com_content&view=article&id=143%3Anovosti-11ro&catid=83&Itemid=493&lang=RO
- groups.google.com/g/UGGCM — "SERVICII PUBLICE MOLDPOS" thread; Order No. 04 of 06.01.2012 (paid service); old IP 188.237.130.50:8080; Chișinău address str. Pușkin 47
- GPS World — "Moldova's positioning system now uses Galileo" (GPS+GLONASS+Galileo confirmation)
- Scribd — "MOLDPOS – GNSS-Positioning Service of Moldova – CHIRIAC" (2012 paper; network founding, 10-station initial deployment)
- ardusimple.com/rtk-correction-services-and-ntrip-casters-in-moldova/ — confirms paid national service; SBC registration URLs
- EuroGeographics — AGCC member profile (ETRS89 alignment, EU candidate context)
- Direct caster probe (2026-05-21): `curl --http0.9 http://185.108.183.29:8080/` → `SOURCETABLE 200 OK`, Server `GNSS Spider 7.10.1.168/1.0`, Content-Length 2,317, mountpoints VRS / MAX / MSM / NEAREST + FZUTM / FZINGEOCAD / FZUASM (+ further FreeZone rows)
- RTK2go monitor — no Moldova NTRIP streams confirmed
- `py scripts/stations_by_radius.py 47.0 28.5 200` (2026-05-12) — only nearest free RTK stations are POPINCIUC (rtk2go, Romania, 125 km) and VASLUI (Centipede, Romania, 108 km); both outside reliable single-base range (~35 km) from Chișinău
