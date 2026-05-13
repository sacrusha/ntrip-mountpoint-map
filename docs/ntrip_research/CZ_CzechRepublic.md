# Czech Republic [CZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06; deep verification 2026-05-07)
**Exchange rate used:** ~22.5 CZK / 1 USD; ~25.0 CZK / 1 EUR (approximate spot rates, 2026-05-07)

## Status: YES — paid national NTRIP (CZEPOS); commercial alternative Trimble VRS Now Czech via Geotronics; private TopNET via GB-geodezie; Centipede + rtk2go volunteer trickle. CZEPOS annual ~10,000 CZK (~€400) above the project's $200/yr hobbyist cutoff; cheapest hourly rate is ~50 CZK/hr (~€2/hr) for casual-use individuals.

---

## Service A: CZEPOS (national, ČÚZK — primary)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | ČÚZK — Český úřad zeměměřický a katastrální (Czech Office for Surveying, Mapping and Cadastre); CORS network operationally managed by Zeměměřický úřad (ZÚ — Land Survey Office), Odbor geodetických základů |
| **Mandate basis** | Vyhláška ČÚZK č. 31/1995 Sb., kterou se provádí zákon č. 200/1994 Sb. o zeměměřictví (decree implementing the Surveying Act); pricing in items 26–32 of section 11.1 of the Annex; most recently amended by vyhláška 156/2023 Sb. and earlier by 383/2015 Sb. |
| **host:port — primary RTK3 MSM (RTCM 3.2)** | `czepos.cuzk.gov.cz:2101` (caster also alive on legacy `czepos.cuzk.cz:2101`; IPv4 195.245.209.183, IPv6 `2001:67c:28b8:ffff::1:32`); confirmed HTTPS 200 on web portal 2026-05-07; direct port-2101 NTRIP probe timed out from research environment (likely geo-restricted or sandbox firewall) |
| **host:port — legacy RTCM 2.3** | `czepos.cuzk.gov.cz:2100` (`_korekceRTCMpuv.aspx`) for older single-frequency receivers |
| **host:port — legacy Leica Spider proxy** | `czepos.cuzk.gov.cz:2111` (legacy compatibility port) |
| **VRS** | Yes — three network-solution variants on port 2101: VRS3-MAX (mountpoint `MAX3C-MSM`, identifier `VRS.MAX-CZEPOS-MSM`), VRS3-iMAX (`iMAX3C-MSM`, `VRS.iMAX-CZEPOS-MSM`), VRS3-VirtualRS (`VirtualRS3C-MSM`, `VRS.VirtualRS-CZEPOS-MSM`) |
| **Mountpoints — RTK single-station** | Per-station `C[XXX]3-MSM` format (e.g., `CPAR3-MSM` Pardubice, `CSVI3-MSM` Svitavy, `CJIH3-MSM` Jihlava); ~30 CZ stations + ~27 foreign-network stations cross-fed for border-zone solutions |
| **Mountpoints — RTK nearest-site** | `RTK.NEAREST.SITE-CZEPOS-MSM` (port 2101) |
| **Mountpoints — DGPS** | Per-station on port 2100, e.g., `CPAR1`, `CSVI1`, `CJIH1` (decimeter accuracy only, single-frequency RTCM 2.3) |
| **tariff — DGPS hourly (item 26)** | 60 CZK/hr (~€2.40) per receiver |
| **tariff — RTK and VRS hourly (item 27)** | 50 CZK/hr (~€2.00) per receiver |
| **tariff — RINEX 1-second interval (item 28)** | 10 CZK/hr per file |
| **tariff — RINEX 5-second interval (item 29)** | 5 CZK/hr per file |
| **tariff — RINEX 10-second interval (item 30)** | (table layout in cenik.pdf is mis-aligned — reference vyhláška 31/1995 Sb. items 26–32 directly for authoritative reading; per published transcript, item 30 covers 10-second RINEX with a per-hour rate consistent with sampling-interval discount) |
| **tariff — RTK/DGPS/VRS annual flat (item 31)** | 10,000 CZK / 12 calendar months / 1 GPS (~€400/yr; ~$444/yr per receiver) |
| **tariff — RTK/DGPS/VRS monthly flat (item 32)** | 1,000 CZK / 1 calendar month / 1 GPS (~€40/month) |
| **VAT status** | Prices in vyhláška are net of 21% Czech standard VAT (DPH); commercial users add 21% on invoice |
| **tariff — exempt categories** | **Free of charge** for: státní orgány a orgány územních samosprávných celků (state authorities, local-government bodies) for statutory functions; školy, školská zařízení a vysoké školy (schools, school facilities, universities) for educational purposes; students writing bachelor's, diploma, or other qualifying theses |
| **hobbyist_eligibility** | Yes — paid tier accepts physical persons (`fyzická osoba`), self-employed persons (`podnikající fyzická osoba` — živnostník/OSVČ), and legal entities; registration form (`registrace.doc`) explicitly accepts physical-person applicants for "personal needs"; no professional surveying licence required |
| **legal_residency_required** | Unclear — registration form requests Czech identification number (rodné číslo / IČO) and a Czech bank account; foreign applicants can register via email (scanned application) but practical onboarding may require Czech tax presence; foreign applicants should expect to negotiate; no explicit residency exclusion stated in vyhláška |
| **last_confirmed_alive** | 2026-05-12 — `czepos.cuzk.gov.cz` HTTPS 200; portal continues to serve the stations overview and cenik documentation. Port-2101 NTRIP fetch from research env still times out (sandbox/geo-restriction). Recent service announcements: Opava station live 2026-03-22 (Ostrava RTK/DGPS retired but kept in VRS network solution), Olomouc RTK/DGPS launched 2024-10-21, BeiDou-3/Galileo E6 firmware upgrade 2025-02-01 |

### Account types and registration

The CZEPOS registration form (`czepos.cuzk.gov.cz/registrace.doc`) offers three subscription account types:

- **Type A**: Unlimited account billed by usage (hourly rate per items 26–30 of the price list)
- **Type B**: Fixed annual fee per item 31 (10,000 CZK/yr per GPS receiver)
- **Type C**: Fixed monthly fee per item 32 (1,000 CZK/month per GPS receiver)

Applicants commit to using CZEPOS "only for personal needs of a physical person, own internal needs of a legal entity or self-employed person" — explicitly excluding commercial resale of the corrections.

Submission methods: postal mail to Zeměměřický úřad, Odbor geodetických základů, Pod sídlištěm 9, 182 11 Praha 8; email scanned application; or data box ID `6yvadsa`. Invoice payment within 30 days; statutory interest on late payment.

### Network details

- **Stations**: ~30 CZ permanent stations + ~27 foreign-network stations integrated for border-zone solutions (German DVRS/SAPOS, Austrian APOS, Polish ASG-EUPOS, Slovak SKPOS cross-feeds); recent CZ additions: Opava 2026-03, Olomouc 2024-12; Ostrava decommissioned for RTK/DGPS 2026-03 (retained in VRS)
- **Constellations**: GPS, GLONASS, Galileo (incl. E6), BeiDou-3 — software upgrade 2025-02-01 added BeiDou-3 and Galileo E6 ahead of solar maximum
- **Hardware**: Leica GNSS Spider on the caster side (RTK3-MSM service)
- **Coverage**: National; centimeter-level accuracy expected anywhere in CZ via VRS; real-estate cadastre-approved (no verification measurements required)

---

## Service B: Trimble VRS Now Czech (commercial — Geotronics Praha)

| Field | Value |
|---|---|
| **Operator** | Geotronics Praha s.r.o. (authorized Trimble distributor for CZ); reseller via Geoshop.cz |
| **Network name** | Trimble VRS Now Czech |
| **host:port** | `vrsnow.cz` (web portal); NTRIP caster credentials issued at subscription, host not advertised on public marketing pages |
| **VRS** | Yes — Trimble VRS network on Trimble Pivot Platform |
| **Stations** | 37 reference stations across Czech Republic, Moravia, Silesia plus border German cells; Trimble Alloy receivers with Maxwell 7 dual chips |
| **Constellations** | GPS+GLO+GAL+BDS (40-satellite track); CMRx/CMR+/RTCM correction formats |
| **tariff — RTK Czech 100 (100 hours / 24 months)** | 11,000 CZK net (13,310 CZK incl. 21% VAT; ~€440 / ~$489 net) — for surveying-grade <2 cm |
| **tariff — RTK Czech Unlimited (unlimited / 12 months)** | 25,800 CZK net (~31,218 CZK incl. VAT; ~€1,032 / ~$1,147 net) — for surveying-grade <2 cm |
| **tariff — H-Star 100 (100 hours / 24 months)** | 8,950 CZK net (10,829 CZK incl. VAT) — 10 cm GIS/agriculture |
| **tariff — H-Star Unlimited (unlimited / 12 months)** | 18,000 CZK net (21,780 CZK incl. VAT) — 10 cm GIS/agriculture |
| **tariff — DGNSS Unlimited (unlimited / 12 months)** | 6,000 CZK net (7,260 CZK incl. VAT; ~€240 / ~$267 net) — sub-meter |
| **VAT status** | All prices listed net of 21% Czech VAT; gross-of-VAT price listed alongside on Geoshop.cz product pages |
| **hobbyist_eligibility** | Yes — Geoshop.cz e-commerce checkout accepts physical persons; demo accounts available on request via `korekce@geotronics.cz`; service activated within 2 business days |
| **legal_residency_required** | Unclear — Czech-language web shop, Czech bank account preferred for invoicing; foreign customers possible via direct contact |
| **last_confirmed_alive** | 2026-05-07 — geotronics.cz, geoshop.cz, vrsnow.cz all served pages normally; product page lists current pricing |

Cheapest entry tier (DGNSS Unlimited at 6,000 CZK net / ~$267) is barely under $300/yr but the surveying-grade tier is well above $200/yr. Cadastre-approval same as CZEPOS (registered in VÚGTK monitoring campaign).

---

## Service C: TopNET (commercial — GB-geodezie)

| Field | Value |
|---|---|
| **Operator** | GB-geodezie, spol. s r.o. |
| **host:port** | `topnet.gb-geodezie.cz:8006` (also IP 77.240.179.190 in older references); not curl-verified in this research session |
| **VRS** | Yes — RRTK (regional network RTK), MRTK (multi-station RTK) |
| **Stations** | 32 Czech stations + 3 Austrian (EPOSA cross-feed) + 4 Polish (TPI NETpro cross-feed) = ~39 total |
| **tariff** | ~75 CZK + VAT per hour (usage-based, monthly invoicing); annual flat rates exist per direct quote — not publicly listed on a single price page |
| **hobbyist_eligibility** | Yes — physical persons accepted |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | 2026-05-06 (per prior research; not re-verified 2026-05-07) |

Only one GNSS receiver per RRTK/MRTK service can connect at a time — additional logins require separate subscriptions.

---

## Volunteer / Free Alternatives

- **rtk2go**: ~4 CZE-coded bases (verified against `data/rtk2go.sourcetable` 2026 archives via project pipeline). Sparse, no national coverage.
- **Centipede**: ~3 CZE nodes. Sparse.
- **EUREF EPN**: GOPE (Ondřejov) and other Czech CORS contribute to EPN — academic post-processing only.

These provide enough corrections for occasional hobbyist use within ~30 km of a base, but density is too thin for general-purpose national coverage. A self-operated base or a Centipede node is the cheapest free path for serious hobbyist use outside CZEPOS-funded categories.

---

## Most Recent Public Announcement (date + URL)

- **2026-03-22** — Opava station operational; Ostrava RTK/DGPS retired (still in VRS network solution). Source: czepos.cuzk.cz news section.
- **2025-02-01** — Software upgrade adding BeiDou-3 and Galileo E6 frequencies ahead of solar maximum. Source: czepos.cuzk.cz.
- **2024-12-01** — Olomouc station activated (installed 2024-09-12). Source: czepos.cuzk.cz.
- **2024-04-01** — CZEPOS web portal migrated to `gov.cz` state domain (czepos.cuzk.gov.cz; legacy czepos.cuzk.cz still resolves and serves the same content as of 2026-05-07).
- **2024-06-23** — Coordinate readjustment for Liberec, Prachatice, Trutnov, Znojmo (millimeter-level shifts).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost | Notes |
|---|---|---|---|
| **CZEPOS RINEX archive** — per-station RINEX 2.x/3.x download (1-sec, 5-sec, 10-sec intervals) | https://czepos.cuzk.gov.cz/ | Free for exempt categories; otherwise vyhláška items 28–30 (10/5/lower CZK per hour) | Items 28–30 of vyhláška 31/1995 Sb. |
| **Virtual RINEX** — network-generated RINEX for any point in CZ | https://czepos.cuzk.gov.cz/ | Same pricing as RTK corrections | |
| **EUREF EPN** — European archive includes Czech CORS | https://www.epncb.oma.be/ | Free | Daily 30-second RINEX |

---

## Sources Consulted
- CZEPOS portal (current, gov.cz domain): https://czepos.cuzk.gov.cz/ (observed 2026-05-07; HTTPS 200)
- CZEPOS legacy portal: https://czepos.cuzk.cz/ (still serving same content 2026-05-07)
- CZEPOS RTK3-MSM service description: https://czepos.cuzk.gov.cz/_korekceRTCM.aspx (mountpoint list, network-solution mappings)
- CZEPOS legacy RTK service: https://czepos.cuzk.gov.cz/_korekceRTCMpuv.aspx (port 2100, RTCM 2.3)
- CZEPOS services and products: https://czepos.cuzk.gov.cz/_servicesProducts.aspx
- CZEPOS registration info: https://czepos.cuzk.gov.cz/_registraceInfo.aspx
- CZEPOS application form (DOC): https://czepos.cuzk.cz/registrace.doc (text-extracted 2026-05-07)
- CZEPOS news / network status: https://czepos.cuzk.gov.cz/ (Opava/Olomouc/Ostrava notices observed)
- ČÚZK Geoportál CZEPOS metadata: https://geoportal.cuzk.gov.cz/ (text metadata; pricing reference to vyhláška)
- ČÚZK price list (cenik.pdf): https://geoportal.cuzk.cz/dokumenty/cenik.pdf — items 26–32 list CZEPOS services and prices in CZK
- Vyhláška 31/1995 Sb. (legal source): https://www.zakonyprolidi.cz/cs/1995-31 (403 from research env, but pricing structure verified via cenik.pdf and search transcripts)
- Czech government services portal (eligibility): https://portal.gov.cz/sluzby-vs/poskytnuti-sluzeb-site-permanentnich-stanic-czepos-S47119
- Geotronics VRS Now Czech: https://geotronics.cz/produkty/gnss-korekce/o-siti/ (network description, 37 stations)
- Geoshop VRS Now Czech 100 product page: https://www.geoshop.cz/vsechny-produkty/korekcni-sluzby/trimble-vrs-now-czech-tarif-czech-100-... (CZK 11,000 net / 13,310 incl. VAT)
- Geoshop VRS Now Czech full product list: https://www.geoshop.cz/vsechny-produkty/korekcni-sluzby/korekce-trimble-vrs-now-pro-cr/
- Geotronics VRS Now overview: https://geotronics.cz/trimble-vrs-now-czech/
- Geotronics promotional pricing page: https://geotronics.cz/korekce-trimble-vrs-now-vyhodneji/
- TopNET (GB-geodezie) reseller pricing: https://geopen.cz/gnss-gps-mereni/622-topnet-rtk-sluzby.html
- ArduSimple Czech Republic: https://cs.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-czech-republic/
- Contact (CZEPOS): czepos@cuzk.gov.cz / +420 284 041 530 / +420 2 8404 1536

## Known Data Gaps
- **Direct sourcetable verification**: Port 2101 NTRIP fetch from research environment timed out (sandbox/network limitation) — mountpoint list was reconstructed from `_korekceRTCM.aspx` web page, not direct fetch. Czech operators in-country should be able to verify directly.
- **TopNET re-verification**: TopNET data from 2026-05-06 prior research; not re-fetched. Annual flat-rate pricing not on a public web page — by-quote only.
- **Foreign individual practical onboarding**: Vyhláška does not require Czech residency, but foreign applicants without a Czech bank account or IČO are not explicitly addressed in registration form. Real outcome unknown — direct contact recommended.
- **Item 30 (10-second RINEX) numerical extraction**: cenik.pdf table layout misalignment makes exact CZK figure for 10-second-interval RINEX ambiguous in mechanical text extraction; vyhláška 31/1995 Sb. items 26–32 are the authoritative source. Item 31 = 10,000 CZK/12-mo/GPS and item 32 = 1,000 CZK/mo/GPS are confirmed and consistent across all sources.
