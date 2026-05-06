# Bosnia and Herzegovina [BA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — dual government NTRIP casters operating (BiHPOS dual-entity network); paid subscription; no free tier

Bosnia and Herzegovina is a dual-entity state. Two separate government CORS networks operate under the EU-funded BiHPOS umbrella: SRPOS (Republika Srpska) and FBiHPOS (Federation of BiH). Both are paid. They are independently operated, have separate endpoints, separate tariffs, and separate registration processes.

---

## SRPOS — Republika Srpska sub-network

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | SRPOS — Mreža Permanentnih GNSS Stanica Republike Srpske |
| **Operator** | RGURS / RUGIPP — Republička uprava za geodetske i imovinsko-pravne poslove, Republika Srpska |
| **Admin contact** | Spomenko Mitrović — Tel: +387 55 220-890 / +387 55 202-643 — Email: srposnet@rgurs.org |
| **Network size** | ~17 CORS stations (RS portion of the ~34-station BiHPOS network) |
| **Launched** | 27 September 2011 |
| **host:port** | `srpos.rgurs.org:2101` (preferred); legacy IP `81.93.74.247:8080` also documented |
| **VRS** | Yes (VRS-AUTO mountpoint, RTCM 3.1, GPS + GLONASS) |
| **tariff — per commenced minute** | 0.20 KM (~€0.10, ~$0.12) |
| **tariff — 10 hours** | 30 KM (~€15.34, ~$17) |
| **tariff — 20 hours** | 50 KM (~€25.57, ~$29) |
| **tariff — 50 hours** | 150 KM (~€76.70, ~$87) |
| **tariff — 1 month (flat)** | 250 KM (~€127.83, ~$145) |
| **tariff — 2 months** | 350 KM (~€178.96, ~$202) |
| **tariff — 3 months** | 450 KM (~€230.10, ~$260) |
| **tariff — 6 months** | 750 KM (~€383.51, ~$433) |
| **tariff — 12 months (annual)** | 1,000 KM (~€511.35, ~$578) |
| **tariff — DGPS 1 month** | 200 KM (~€102.27, ~$116) |
| **tariff — DGPS 12 months** | 1,000 KM (~€511.35, ~$578) |
| **tariff — Post-processing RINEX (RTK)** | 28 KM/hr (~€14.32) |
| **tariff — Post-processing RINEX (DGPS)** | 17 KM/hr (~€8.69) |
| **VAT status** | Not explicitly stated in the tariff document (Odluka Sl. glasnik RS 85/2011); government tariff schedule — rates likely gross (inclusive of all applicable charges) but VAT treatment under RS law for public administration services not confirmed explicitly |
| **Currency** | BAM / KM (Konvertibilna Marka) — pegged to EUR at exactly 1.95583 BAM = 1 EUR; ~$0.578/BAM (April 2026) |
| **hobbyist_eligibility** | Yes — SRPOS registration form imposes no professional surveying licence requirement; individual natural persons can register |
| **legal_residency_required** | Unclear (leans toward no explicit restriction) — foreign nationals not explicitly excluded, but RS giro-account payment route practically favours in-entity users |
| **last_confirmed_alive** | 2026-04-30 (rgurs.org/stranica/srpos loaded normally; most recent RGURS news item dated 2026-04-30; caster portal `http://srpos.rgurs.org/sbc` referenced as live) |

### SRPOS Mountpoints

| Mountpoint | Format | Method | Corrections | Systems |
|---|---|---|---|---|
| MAX-AUTO | RTCM 3.1 | MAX | Network | GPS + GLONASS |
| iMAX-AUTO | RTCM 3.1 | iMAX | Network | GPS + GLONASS |
| VRS-AUTO | RTCM 3.1 | VRS | Network | GPS + GLONASS |
| FKP-AUTO | RTCM 2.3 (msg 18/19) | FKP | Network | GPS only |
| NEAREST | RTCM 3.1 | Nearest station | Single base | GPS + GLONASS |
| iMAX-AUTO-2.3 | RTCM 2.3 | iMAX | Network | GPS + GLONASS |

---

## FBiHPOS — Federation of BiH sub-network

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | FBiHPOS — Mreža Permanentnih GNSS Stanica Federacije Bosne i Hercegovine |
| **Operator** | FGU — Federalna uprava za geodetske i imovinsko-pravne poslove, Federacija BiH |
| **Contact** | fbihpos@fgu.com.ba — Tel: +387 33 586 065 |
| **Network size** | ~17 CORS stations (FBiH portion of the ~34-station BiHPOS network) |
| **host:port** | `fbihpos.katastar.ba:8080` — note port 8080, not conventional 2101; caster runs on a separate cadastre subdomain |
| **VRS** | Yes (VRS-AUTO and VRS-3G mountpoints) |
| **tariff — one-time registration fee** | 100 KM (~€51.14, ~$58) |
| **tariff — RTK-VPSP 7 days** | 150 KM (~€76.70, ~$87) |
| **tariff — RTK-VPSP 1 month** | 250 KM (~€127.83, ~$145) |
| **tariff — RTK-VPSP 2 months** | 350 KM (~€178.96, ~$203) |
| **tariff — RTK-VPSP 3 months** | 450 KM (~€230.10, ~$261) |
| **tariff — RTK-VPSP 6 months** | 750 KM (~€383.51, ~$435) |
| **tariff — RTK-VPSP 12 months** | 1,000 KM (~€511.35, ~$580) |
| **tariff — All FBiHPOS services 12 months** | 1,400 KM (~€715.89, ~$812) |
| **tariff — Post-processing only 12 months** | 700 KM (~€357.94, ~$406) |
| **Multi-rover discounts** | −10% on 2nd rover, −20% on 3rd; capped at −50% |
| **VAT status** | Not mentioned in tariff document; government statutory fees (naknada) paid to Federal Treasury account (Jedinstveni račun trezora FBiH, acc. 1020500000106698, vrsta prihoda 722516); rates stated gross |
| **Currency** | BAM / KM — pegged to EUR at exactly 1.95583 BAM = 1 EUR; ~$0.578/BAM (April 2026) |
| **Tariff authority** | FBiH Government Decision V. broj: 605/2022, dated 14.04.2022 |
| **hobbyist_eligibility** | Yes — registration form has a "FIZIČKA LICA" (natural persons / individuals) section with no requirement for a surveying company, professional licence, or trade registration; fields are: name, surname, address, city, email, phone, username |
| **legal_residency_required** | Unclear — no citizenship or residency restriction mentioned in any public document; foreign-applicant eligibility not explicitly stated — contact FBiHPOS directly to confirm |
| **last_confirmed_alive** | 2026-04-30 (fgu.com.ba/bs/servisi.html and all FBiHPOS pages fully reachable; site footer shows "FGU © 2026"; 2024-dated FBiHPOS documents in active maintenance folder) |

### FBiHPOS Mountpoints

| Mountpoint | Service |
|---|---|
| MAX-AUTO | MAX network RTK |
| iMAX-3G | iMAX network RTK |
| VRS-AUTO | VRS network RTK |
| VRS-3G | VRS network RTK (3G variant) |
| NEAREST | Nearest single-base RTK |
| FBiH_H+V | Combined horizontal + vertical component stream |

---

## Context Notes

- **BiHPOS dual-entity structure**: BiHPOS is the overall project name for the national CORS network, funded under an EU/EC project. Bosnia and Herzegovina's constitutional structure (two entities: Republika Srpska and Federation of BiH) means the network is split into two independently operated sub-networks. Each entity manages its own stations, caster, tariff, and registration process. There is no unified single endpoint or registration for all of BiH.
- **Domain correction**: The correct FGU domain is `fgu.com.ba` (not `fgu.gov.ba`). Within FBiH, "federal" bodies may use `.com.ba` or `.gov.ba` depending on the institution; FGU uses `.com.ba`. The NTRIP caster itself runs on `fbihpos.katastar.ba` (katastar = cadastre), separate from the FGU web domain.
- **Port 8080**: FBiHPOS uses port 8080, not the conventional NTRIP port 2101. Firewall rules may need adjustment. SRPOS is accessible on both port 2101 (preferred) and legacy port 8080.
- **Tariff parity**: The 1-month and annual RTK rates are essentially identical across both sub-networks (SRPOS: 250 KM/month, 1,000 KM/year; FBiHPOS: 250 KM/month, 1,000 KM/year). The key differences are: FBiHPOS adds a 100 KM one-time registration fee and has no short hourly/per-minute blocks; SRPOS has per-minute and hourly blocks making it cheaper for short-term or occasional use.
- **No free tier on either network**: Neither SRPOS nor FBiHPOS offers any free or open-access NTRIP stream.
- **Volunteer/community bases**: Approximately 1 BiH base on RTK2go; zero on Centipede. These are the only free alternatives and coverage is negligible.
- **SRPOS tariff history**: The SRPOS tariff was established by Decision published in Sl. glasnik RS 85/2011 at launch in September 2011. A 20% discount applied before 1 January 2013; current full rates apply post-2013.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| SRPOS post-processing (RTK, <30 sec interval) | rgurs.org/stranica/srpos | 22 KM/hr (~€11.25) |
| SRPOS RINEX generation & delivery (RTK) | rgurs.org/stranica/srpos | 28 KM/hr (~€14.32) |
| SRPOS RINEX generation & delivery (DGPS) | rgurs.org/stranica/srpos | 17 KM/hr (~€8.69) |
| FBiHPOS post-processing 12-month flat | fgu.com.ba/bs/servisi.html | 700 KM (~$406) |

## Sources Consulted

- RGURS SRPOS page: https://www.rgurs.org/stranica/srpos (observed 2026-04-30)
- RGURS SRPOS English page: https://www.rgurs.org/en/stranica/srpos
- SRPOS user-access guide: https://www.rgurs.org/uploads/pages/SRPOS_Korisnicki_pristup.pdf
- SRPOS tariff document (Sl. glasnik RS 85/2011): https://www.rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf (observed 2026-04-30)
- FGU servisi page: https://www.fgu.com.ba/bs/servisi.html (observed 2026-04-30)
- FBiHPOS access guide (2024): https://www.fgu.com.ba/files/Novosti/2024/PDF/FBiHPOS%20-%20novo/Pristup%20FBiHPOS%20servisima.pdf
- FBiHPOS tariff document (V. broj 605/2022): https://www.fgu.com.ba/files/Novosti/2022/PDF/tarife/b/TARIFA%20NAKNADA%20ZA%20VRSENJE%20USLUGA%20IZ%20OBLASTI%20PREMJERA%20I%20KATASTRA.pdf
- FBiHPOS registration form: https://www.fgu.com.ba/files/Novosti/2022/PDF/FBIHPOS%20zahtjev/b/Zahtjev%20za%20koristenje%20usluga%20FBHIPOS%20mreze%20permanentnih%20stanica.pdf
- EuroGeographics / third-party references to fbihpos.fgu.com.ba (older hostname, superseded by fbihpos.katastar.ba per 2024 access guide)
