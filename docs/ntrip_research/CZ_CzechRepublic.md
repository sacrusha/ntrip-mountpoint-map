# Czech Republic [CZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — paid national NTRIP (CZEPOS, ~80 CZK/hr or annual fee); free for public authorities, schools, thesis students; private commercial alternatives available

---

## Service A: CZEPOS (national, operated by Czech State — primary)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | ČÚZK — Český úřad zeměměřický a katastrální (Czech Office for Surveying, Mapping and Cadastre) |
| **host:port — RTK (MSM, RTCM 3.2)** | `czeposr.cuzk.gov.cz:2101` (also: IP 195.245.209.181) |
| **host:port — legacy RTK (RTCM 2.3)** | `czepos.cuzk.gov.cz:2100` |
| **VRS** | Yes — MAX (MAX3C-MSM), iMAX (iMAX3C-MSM), VirtualRS (VirtualRS3C-MSM) |
| **Mountpoints (RTK)** | Per-station: `C[ID]3-MSM`; network nearest: `RTK.NEAREST.SITE-CZEPOS-MSM`; VRS: `MAX3C-MSM`, `iMAX3C-MSM`, `VirtualRS3C-MSM` |
| **Mountpoints (DGPS)** | Per-station on port 2100: e.g., `CPAR1`, `CSVI1`, `CJIH1` (decimeter accuracy only) |
| **tariff — commercial** | **~80 CZK + VAT per hour** for RTK; DGPS at ~20 CZK/hr. Annual flat-rate available (~10,000 CZK/yr, ~€400 at 2026 rates). Pricing governed by Decree No. 31/1995 Sb. as amended by No. 383/2015 Sb. VAT rate: 21% (standard Czech rate). Date observed: 2026-05-06. Source: https://czepos.cuzk.cz/_servicesProducts.aspx; tariff regulation via portal.gov.cz |
| **tariff — exempt categories** | **Free** for: public authorities performing statutory functions; schools, school facilities, and universities for educational purposes; students writing bachelor's, diploma, or other qualifying theses |
| **hobbyist_eligibility** | **Yes** — paid tier available to any registrant; no professional licence check |
| **legal_residency_required** | **Unclear** — no explicit residency requirement; Czech ID number preferred in registration form; foreign applicants may register via email |
| **last_confirmed_alive** | CZEPOS portal (czepos.cuzk.cz) accessible 2026-05-06; new Opava station added 2026-03; new Olomouc station added 2024 |

### CZEPOS Network Details
- **Stations:** ~30 reference stations covering Czech Republic; recent additions in Opava (2026) and Olomouc (2024); network described on czepos.cuzk.cz as continuously expanding
- **Constellations:** GPS, GLONASS, Galileo, BeiDou (BeiDou-3 and Galileo E6 added in recent software version)
- **Services:** DGPS (decimeter), RTK single-station, RTK nearest-site, VRS (MAX, iMAX, VirtualRS), RINEX, Virtual RINEX
- **Registration:** Written request form (registrace.doc) submitted to ČÚZK; see https://czepos.cuzk.gov.cz/_registraceInfo.aspx

---

## Service B: TopNET (private, GB-geodezie)

| Field | Value |
|---|---|
| **Operator** | GB-geodezie, spol. s r.o. |
| **host:port** | `topnet.gb-geodezie.cz:8006` (also IP 77.240.179.190) |
| **VRS** | Yes — RRTK (regional network RTK) and MRTK (multi-station RTK) |
| **tariff** | **~75 CZK + VAT per hour** for usage-based billing (monthly invoicing). Date observed: 2026-05-06. Source: https://geopen.cz/gnss-gps-mereni/622-topnet-rtk-sluzby.html |
| **hobbyist_eligibility** | **Yes** — no licence requirement stated |
| **legal_residency_required** | **Unclear** |
| **last_confirmed_alive** | topnet.gb-geodezie.cz portal accessible 2026-05-06 |

- **Stations:** 32 Czech stations + 3 Austrian (EPOSA) + 4 Polish (TPI NETpro) = ~39 total in network
- **Note:** Only one GNSS receiver can connect per RRTK/MRTK service at a time (per pricing page); additional logins require separate subscriptions

---

## Services Investigated and Excluded

| Service | Finding |
|---|---|
| VRS Now (Trimble/Spectra) | Czech coverage confirmed; operated via TopNET-branded or Topcon Live platform; pricing per-request from distributor |
| HxGN SmartNet | Present in Czech Republic but no dedicated Czech portal found; contact Hexagon Czech distributor |
| rtk2go volunteer bases | ~5–10 Czech-coded bases; sparse, not a reliable free alternative |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **CZEPOS RINEX archive** — per-station RINEX 2.x/3.x download | https://czepos.cuzk.cz/ | Free for exempt categories; paid for commercial users |
| **Virtual RINEX** — network-generated RINEX for any point in CZ | https://czepos.cuzk.cz/ | Same pricing as RTK corrections |
| **EUREF/EPN** — European archive including Czech CORS stations | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- CZEPOS portal: https://czepos.cuzk.cz/ (observed 2026-05-06)
- CZEPOS RTK3 MSM service page: https://czepos.cuzk.cz/_korekceRTCM.aspx
- CZEPOS services and products: https://czepos.cuzk.cz/_servicesProducts.aspx
- CZEPOS registration info: https://czepos.cuzk.gov.cz/_registraceInfo.aspx
- Czech government service portal (pricing/exemptions): https://portal.gov.cz/en/sluzby-vs/poskytnuti-sluzeb-site-permanentnich-stanic-czepos-S47119
- TopNET GB-geodezie: http://topnet.gb-geodezie.cz/topnet/topnet.aspx
- TopNET reseller (geopen.cz) pricing: https://geopen.cz/gnss-gps-mereni/622-topnet-rtk-sluzby.html
- ArduSimple Czech Republic page: https://cs.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-czech-republic/
