# Czech Republic [CZ] — NTRIP RTK Research

**researched:** 2026-05-17 (prior: 2026-05-12; verification 2026-05-07)
**status:** YES — paid national CZEPOS (ČÚZK); commercial Trimble VRS Now Czech (Geotronics); private TopNET (GB-geodezie); volunteer trickle on rtk2go + Centipede. CZEPOS annual 10,000 CZK (~€400) > $200/yr hobbyist cutoff; cheapest hourly = 50 CZK/hr (~€2/hr) for casual use.

## Service A — CZEPOS (national, paid, ČÚZK)

| field | value |
|---|---|
| landing_url | https://czepos.cuzk.gov.cz/ |
| access_url | https://czepos.cuzk.gov.cz/_registraceInfo.aspx |
| operator | ČÚZK — Český úřad zeměměřický a katastrální. CORS run by Zeměměřický úřad (ZÚ), Odbor geodetických základů. |
| legal basis | vyhláška 31/1995 Sb. (impl. zákon 200/1994 Sb. o zeměměřictví); pricing items 26–32 of section 11.1 of Annex; amended by 156/2023 Sb. (latest) + 383/2015 Sb. |
| host:port — RTK3 MSM (RTCM 3.2) | `czepos.cuzk.gov.cz:2101` (legacy `czepos.cuzk.cz:2101` mirror live; IPv4 195.245.209.183, IPv6 `2001:67c:28b8:ffff::1:32`). Port 2101 NTRIP probe times out from sandbox (geo/firewall); HTTPS portal 200 |
| host:port — RTCM 2.3 legacy | `czepos.cuzk.gov.cz:2100` |
| host:port — Leica Spider proxy | `czepos.cuzk.gov.cz:2111` |
| vrs | yes — VRS3-MAX (`MAX3C-MSM`), VRS3-iMAX (`iMAX3C-MSM`), VRS3-VirtualRS (`VirtualRS3C-MSM`) |
| mountpoints — single-station | `C[XXX]3-MSM` per station (e.g., `CPAR3-MSM` Pardubice, `CSVI3-MSM` Svitavy, `CJIH3-MSM` Jihlava) |
| nearest-site | `RTK.NEAREST.SITE-CZEPOS-MSM` |
| DGPS legacy | per-station port 2100 (`CPAR1` etc), RTCM 2.3, dm only |
| num_stations | ~30 CZ + ~27 cross-fed foreign (SAPOS DE, APOS AT, ASG-EUPOS PL, SKPOS SK) for border zones. Recent: Opava live 2026-03-22; Olomouc activated 2024-10-21; Ostrava RTK/DGPS retired 2026-03-31 (retained in VRS) |
| tariff — DGPS hourly (item 26) | 60 CZK/hr per receiver |
| tariff — RTK + VRS hourly (item 27) | 50 CZK/hr per receiver |
| tariff — RINEX 1-sec (item 28) | 10 CZK/hr per file |
| tariff — RINEX 5-sec (item 29) | 5 CZK/hr per file |
| tariff — RINEX 10-sec (item 30) | (cenik.pdf layout misaligned; vyhláška 31/1995 Sb. items 26–32 authoritative) |
| tariff — annual flat (item 31) | 10,000 CZK / 12 mo / 1 receiver (~€400, ~$444) |
| tariff — monthly flat (item 32) | 1,000 CZK / 1 mo / 1 receiver (~€40) |
| VAT | prices net of 21% DPH; commercial users invoiced +21% |
| exempt categories | free for: státní orgány + ÚSC (state + local-govt bodies) for statutory functions; schools + universities for educational use; students writing thesis |
| hobbyist_eligibility | yes — paid tier accepts fyzická osoba (physical), OSVČ (self-empl), legal entity. Form `czepos.cuzk.cz/registrace.doc` confirms "personal needs" use. No surveying licence required. |
| legal_residency_required | unclear — form asks rodné číslo / IČO + CZ bank account. Foreign applicants via email scan possible; practical onboarding may need CZ tax presence. No explicit exclusion in vyhláška. |
| last_confirmed_alive | 2026-05-17 — portal HTTPS 200; news section unchanged from 2026-03-22 Opava notice. Port 2101 sandbox timeout. |
| datum_epoch | omitted — no citable declaration on operator portal or `_servicesProducts.aspx` (national survey practice is ETRS89 / S-JTSK; ČÚZK does not declare per-stream datum on CZEPOS pages) |

### Account types
- **A** — usage-billed per items 26–30
- **B** — annual flat per item 31 (10,000 CZK/yr)
- **C** — monthly flat per item 32 (1,000 CZK/mo)

User signs commitment to "personal needs of physical person, own internal needs of legal entity or OSVČ" — explicit no commercial resale. Submission: postal to Zeměměřický úřad, OGZ, Pod sídlištěm 9, 182 11 Praha 8; email scan; data box `6yvadsa`. Invoice 30-day terms.

### Network
- ~30 CZ permanent + ~27 cross-fed foreign; recent: Opava 2026-03, Olomouc 2024-10; Ostrava RTK/DGPS decommissioned 2026-03 (retained in VRS)
- GNSS: GPS + GLO + GAL (incl E6) + BDS-3 — firmware upgrade 2025-02-01 added BDS-3 + E6 ahead of solar max
- Hardware: Leica GNSS Spider; RTK3-MSM
- Cadastre-approved (no verification measurements required)

---

## Service B — Trimble VRS Now Czech (commercial, Geotronics)

| field | value |
|---|---|
| landing_url | https://geotronics.cz/trimble-vrs-now-czech/ |
| access_url | https://www.geoshop.cz/vsechny-produkty/korekcni-sluzby/korekce-trimble-vrs-now-pro-cr/ |
| operator | Geotronics Praha s.r.o. (Trimble distributor CZ); reseller Geoshop.cz |
| host:port | `vrsnow.cz` web portal; NTRIP host issued post-subscription |
| vrs | yes — Trimble Pivot Platform |
| num_stations | 37 (CZ + Moravia + Silesia + border DE cells); Trimble Alloy / Maxwell 7 |
| format | CMRx/CMR+/RTCM; tracks GPS+GLO+GAL+BDS (40 sats) |
| tariff — RTK Czech 100 (100 h / 24 mo) | 11,000 CZK net (~€440) — <2 cm |
| tariff — RTK Czech Unlimited (12 mo) | 25,800 CZK net (~€1,032) — <2 cm |
| tariff — H-Star 100 (100 h / 24 mo) | 8,950 CZK net (~10 cm GIS/agri) |
| tariff — H-Star Unlimited (12 mo) | 18,000 CZK net (~10 cm GIS/agri) |
| tariff — DGNSS Unlimited (12 mo) | 6,000 CZK net (~€240, ~$267 — sub-m) |
| VAT | all net of 21% DPH; gross shown alongside on Geoshop product pages (observed 2026-05-17) |
| hobbyist_eligibility | yes — Geoshop accepts fyzická osoba; demo via `korekce@geotronics.cz`; activation ≤2 business days |
| legal_residency_required | unclear — CZ-language shop, CZ bank account preferred for invoicing |
| last_confirmed_alive | 2026-05-17 — Geoshop pricing page live, pricing unchanged |

Cheapest DGNSS Unlimited 6,000 CZK ≈ $267 — barely under $300; surveying tier well above $200/yr.

---

## Service C — TopNET (commercial, GB-geodezie)

| field | value |
|---|---|
| landing_url | http://topnet.gb-geodezie.cz/topnet/services.aspx |
| access_url | http://topnet.gb-geodezie.cz/topnet/pricelist.aspx (ECONNREFUSED 2026-05-17 from sandbox; reseller pricing via geopen.cz) |
| operator | GB-geodezie spol. s r.o. |
| host:port | `topnet.gb-geodezie.cz:8006` (IP 77.240.179.190; not curl-verified) |
| vrs | yes — RRTK (regional NRTK) + MRTK (multi-station RTK) |
| num_stations | 32 CZ + 3 AT (EPOSA) + 4 PL (TPI NETpro) = ~39 |
| tariff | ~75 CZK + VAT / hr; annual flat by quote (not on public page) |
| hobbyist_eligibility | yes — physical persons |
| legal_residency_required | unclear |
| last_confirmed_alive | 2026-05-06 (prior research; sandbox cannot re-fetch 2026-05-17) |

Single concurrent rover per RRTK/MRTK subscription — extra logins = extra subscriptions.

---

## Volunteer / Free
- **rtk2go** — 5 CZE STR (`Krizanov`, `KLAZ`, `LAZANY_UM980`, `MSTAS`, `RaabComputer`) per `data/rtk2go.sourcetable` 2026-05
- **Centipede** — 3 CZE STR (`KLAZ`, `SPUTNIK`, `TREMOS`) per `data/centipede.sourcetable` 2026-05 — `KLAZ` cross-listed both
- **EUREF EPN** — GOPE (Ondřejov) + other CZ CORS; academic / post-processing only

Density too thin for national coverage; useful only within ~30 km of a base. Self-op base or Centipede contribution = cheapest free path outside CZEPOS-exempt categories.

---

## Most recent announcements
- 2026-03-22 — Opava live; Ostrava RTK/DGPS retired (VRS retained)
- 2025-02-01 — Firmware: BDS-3 + Galileo E6 added
- 2024-10-21 — Olomouc activated (installed 2024-09-12)
- 2024-04-01 — Portal migrated to gov.cz
- 2024-06-23 — Coordinate readjustment Liberec / Prachatice / Trutnov / Znojmo (mm-level)

## Post-processing
| Service | URL | Cost |
|---|---|---|
| CZEPOS RINEX archive (1/5/10-sec) | https://czepos.cuzk.gov.cz/ | exempt categories free; else items 28–30 |
| Virtual RINEX | https://czepos.cuzk.gov.cz/ | same as RTK |
| EUREF EPN | https://www.epncb.oma.be/ | free (daily 30-sec) |

## Sources
- CZEPOS portal: https://czepos.cuzk.gov.cz/ (HTTPS 200, 2026-05-17)
- Legacy portal: https://czepos.cuzk.cz/
- RTK3-MSM service: https://czepos.cuzk.gov.cz/_korekceRTCM.aspx
- RTCM 2.3 legacy: https://czepos.cuzk.gov.cz/_korekceRTCMpuv.aspx
- Services + products: https://czepos.cuzk.gov.cz/_servicesProducts.aspx
- Registration info: https://czepos.cuzk.gov.cz/_registraceInfo.aspx
- Application form: https://czepos.cuzk.cz/registrace.doc
- ČÚZK price list: https://geoportal.cuzk.cz/dokumenty/cenik.pdf
- Vyhláška 31/1995 Sb.: https://www.zakonyprolidi.cz/cs/1995-31 (HTTP 403 from sandbox; pricing cross-verified via cenik.pdf)
- Service registry: https://portal.gov.cz/sluzby-vs/poskytnuti-sluzeb-site-permanentnich-stanic-czepos-S47119
- Geotronics VRS Now: https://geotronics.cz/produkty/gnss-korekce/o-siti/
- Geoshop VRS Now product list: https://www.geoshop.cz/vsechny-produkty/korekcni-sluzby/korekce-trimble-vrs-now-pro-cr/ (pricing observed 2026-05-17)
- Geotronics promo: https://geotronics.cz/korekce-trimble-vrs-now-vyhodneji/
- TopNET reseller pricing: https://geopen.cz/gnss-gps-mereni/622-topnet-rtk-sluzby.html
- ArduSimple CZ: https://cs.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-czech-republic/
- Contact CZEPOS: czepos@cuzk.gov.cz / +420 284 041 530 / +420 2 8404 1536

## Gaps
- Port 2101 NTRIP sourcetable not directly fetchable from sandbox — mountpoint list from `_korekceRTCM.aspx` web page. In-CZ operators should verify directly.
- TopNET pricelist URL ECONNREFUSED 2026-05-17; not re-verified since 2026-05-06.
- Foreign-resident practical onboarding outcome unknown (no CZ bank / IČO).
- Item 30 (10-sec RINEX) exact CZK unclear from cenik.pdf layout; vyhláška 31/1995 Sb. items 26–32 authoritative.
- No operator-cited datum/epoch declaration on CZEPOS pages.
