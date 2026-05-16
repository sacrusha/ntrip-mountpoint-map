# Bosnia and Herzegovina [BA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: YES — two government NTRIP RTK casters operating (BiHPOS dual-entity structure: SRPOS in Republika Srpska, FBiHPOS in Federation of BiH). Both paid; no free tier. Single rtk2go volunteer base in the northern Posavina (AGROORSOLIC).

Bosnia and Herzegovina is a dual-entity state. Two separate government CORS networks operate under the EU-funded BiHPOS umbrella: SRPOS (Republika Srpska) and FBiHPOS (Federation of BiH). They are independently operated with separate endpoints, separate tariffs, and separate registration processes. Both sourcetables fetched live 2026-05-15.

---

## SRPOS — Republika Srpska sub-network

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | SRPOS — Mreža Permanentnih GNSS Stanica Republike Srpske |
| **Operator** | RGURS / RUGIPP — Republička uprava za geodetske i imovinsko-pravne poslove, Republika Srpska |
| **landing_url** | https://www.rgurs.org/stranica/srpos (Serbian Cyrillic) — operator-owned overview page; English mirror at https://www.rgurs.org/en/stranica/srpos |
| **access_url** | https://srpos.rgurs.org/sbc/Account/Register — Leica Spider Business Center self-registration; natural persons (физичка лица) register with placeholder "007" in tax-ID fields per form labels |
| **Admin contact** | Spomenko Mitrović — Tel: +387 55 220-890 / +387 55 202-643 — Email: srposnet@rgurs.org |
| **num_stations** | ~17 CORS stations (RS portion of the ~34-station BiHPOS network) |
| **Launched** | 27 September 2011 |
| **host:port** | `srpos.rgurs.org:2101` (sourcetable probed live 2026-05-15 17:36 UTC, GNSS Spider 7.11.0.96 — 18 mountpoints returned, ENDSOURCETABLE present); port 8080 also supported per user-access guide; legacy IP `81.93.74.247:8080` still documented |
| **vrs** | yes (VRS.GK6, iVRS.GK6 mountpoints in live sourcetable) |
| **tariff** | BAM (KM, pegged 1 EUR = 1.95583 KM). Source: Odluka, Sl. glasnik RS 85/2011, full schedule at https://www.rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf (PDF re-fetched 2026-05-15). VAT status not explicitly stated on the tariff — schedule is "висине накнада" (fee amounts) set by government decision, rates published gross. RTK rates: 0.20 KM/min · 10 h 30 KM · 20 h 50 KM · 50 h 150 KM · 1 mo 250 KM · 2 mo 350 KM · 3 mo 450 KM · 4 mo 550 KM · 5 mo 650 KM · 6 mo 750 KM · 12 mo 1,000 KM. DGPS rates: 0.15 KM/min · 10 h 20 KM · 20 h 40 KM · 50 h 100 KM · 1 mo 200 KM … 12 mo 1,000 KM. Post-processing: RTK <30 s 22 KM/hr; DGPS ≥30 s 13 KM/hr. RINEX delivery: RTK 28 KM/hr; DGPS archived 19 KM/hr. Coordinate transformation 13 KM/point. The 20% pre-2013 discount has expired; full rates apply. |
| **hobbyist_eligibility** | yes — registration form imposes no surveying-licence requirement; the SBC form explicitly accepts "007" placeholder in the company-registration field for natural persons (физичка лица) |
| **legal_residency_required** | ? — no citizenship/residency clause in form or tariff document; RS giro-account payment route practically favours in-entity users but foreign payment is not explicitly excluded |
| **last_confirmed_alive** | 2026-05-15 — sourcetable returned 200 OK on `srpos.rgurs.org:2101` at 17:36 UTC; rgurs.org/stranica/srpos rendered HTTP 200; SBC register page reachable |
| **datum_epoch** | BH_ETRS89 (EPSG:10328); GRS 1980 ellipsoid. Authoritative source cited by EPSG: FGU "Rulebook for Basic Geodetic Works", Feb 2019 — https://epsg.io/10328. Project realisation epoch widely cited in academic literature as ETRF2000 epoch 2011.307 but not on an official decree URL — citable BH_ETRS89 declaration only |

### SRPOS Mountpoints (live sourcetable 2026-05-15)

| Mountpoint | Format | Method | Systems | Solution |
|---|---|---|---|---|
| VRS.GK6 | RTCM 3 | VRS | GPS+GLO+GAL | Network |
| iVRS.GK6 | RTCM 3 | VRS | GPS+GLO+GAL+BDS | Network |
| MAX.GK6_3s | RTCM 3 | MAX | GPS+GLO+GAL+BDS | Network |
| MAXGK6_3s / MAXGK6_3sR | RTCM 3 | MAX | GPS+GLO / GPS+GLO+GAL+BDS | Network |
| iMAX.GK6_3s / iMAX.GK6_3sR | RTCM 3 | iMAX | GPS+GLO+GAL+BDS | Network |
| iMAXGK6_3s / iMAXGK6_3sR | RTCM 3 | iMAX | GPS+GLO+GAL+BDS | Network |
| iMAX-AUTO_Galileo | RTCM 3 | iMAX | GPS+GLO+GAL+BDS | Network |
| VRS-AUTO-1819 | RTCM 2 | VRS | GPS+GLO | Network |
| NearestGK6_3s / _3sR / GK5 / GK7 | RTCM 3 | Nearest | GPS+GLO (some +GAL+BDS) | Single base |
| iNearestGK5/6/7_3s | RTCM 3 | Nearest | GPS+GLO+GAL+BDS | Single base |

(Live sourcetable is richer than the 6-mountpoint table in older docs; the RGURS user-access guide PDF still lists the legacy MAX-AUTO / iMAX-AUTO / VRS-AUTO / FKP-AUTO / NEAREST / iMAX-AUTO_2.3 / VRS-AUTO_2.3 names which are no longer published on the caster.)

---

## FBiHPOS — Federation of BiH sub-network

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | FBIHPOS — Mreža Permanentnih GNSS Stanica Federacije Bosne i Hercegovine |
| **Operator** | FGU — Federalna uprava za geodetske i imovinsko-pravne poslove, Federacija BiH (Hamdije Kreševljakovića 96, 71000 Sarajevo) |
| **landing_url** | https://www.fgu.com.ba/bs/servisi.html — operator services page listing DSP / VPSP / GPSP services and access parameters |
| **access_url** | https://www.fgu.com.ba/files/Novosti/2022/PDF/FBIHPOS%20zahtjev/b/Zahtjev%20za%20koristenje%20usluga%20FBHIPOS%20mreze%20permanentnih%20stanica.pdf — official FBIHPOS application form (FIZIČKA LICA section + tariff selection grid) |
| **Contact** | fbihpos@fgu.com.ba, uprava@fgu.com.ba — Tel: +387 33 20 17 84 — Fax: +387 33 58 60 56 |
| **num_stations** | ~17 CORS stations (FBiH portion of the ~34-station BiHPOS network) |
| **host:port** | `fbihpos.katastar.ba:8080` — confirmed by FGU 2024 access guide and live sourcetable probe 2026-05-15 17:36 UTC (GNSS Spider 7.9.0.386, 15 mountpoints, ENDSOURCETABLE present). Older third-party `fbihpos.fgu.com.ba` hostname is superseded. Web portal: `http://fbihpos.katastar.ba/SBC` (redirect 302). |
| **vrs** | yes (VRS-AUTO, VRS-3G in live sourcetable) |
| **tariff** | BAM (KM, pegged 1 EUR = 1.95583 KM). Authority: FBiH Government Decision V. broj 605/2022 dated 14.04.2022; full schedule re-fetched 2026-05-15 from https://www.fgu.com.ba/files/Novosti/2022/PDF/tarife/b/TARIFA%20NAKNADA%20ZA%20VRSENJE%20USLUGA%20IZ%20OBLASTI%20PREMJERA%20I%20KATASTRA.pdf (Tariff group 4 = FBIHPOS). VAT not separately itemised — statutory fees paid to Federal Treasury (Jedinstveni račun trezora FBiH). **4.1.1** one-time registration 100 KM. **4.2 VPSP / RTK**: 7 d 150 · 1 mo 250 · 2 mo 350 · 3 mo 450 · 4 mo 550 · 5 mo 650 · 6 mo 750 · 12 mo 1,000 KM. **4.3 DSP / DGPS**: 1 mo 80 · 2 mo 120 · 3 mo 160 · 4 mo 200 · 5 mo 250 · 6 mo 300 · 12 mo 500 KM. **4.4 GPSP post-processing**: RINEX 15 min 3 KM / 1 h 10 KM; VRINEX 15 min 5 KM / 1 h 15 KM; online LGO obrada 10 KM per 30 min; flat 12 mo all services 1,400 KM; flat 12 mo post-processing only 700 KM. Multi-rover discount −10% on 2nd, −20% on 3rd, cap −50%. |
| **hobbyist_eligibility** | yes — application PDF has dedicated **FIZIČKA LICA** (natural-persons) section requiring only name, surname, address, city, email, phone, and chosen username; no surveying-licence, company-registration, or ID-number requirement; one-time 100 KM registration fee applies equally to individuals |
| **legal_residency_required** | ? — neither the application form nor the tariff document references citizenship or residency; foreign-applicant handling not stated. Contact `fbihpos@fgu.com.ba` to confirm before purchase. |
| **last_confirmed_alive** | 2026-05-15 — `fbihpos.katastar.ba:8080` sourcetable returned 200 OK at 17:36 UTC with 15 STR rows; `www.fgu.com.ba/bs/servisi.html` and `www.fgu.com.ba/bs/pocetna.html` returned 200 OK |
| **datum_epoch** | BH_ETRS89 (EPSG:10328) projected as ETRS89-BIH / TM (EPSG:10329, central meridian 18°E, scale 0.9999, false easting 500000). Authority cited by EPSG: FGU "Rulebook for Basic Geodetic Works", Feb 2019 — https://epsg.io/10329 and https://epsg.io/10328. Academic densification epoch ETRF2000 2011.307 lacks a citable official URL. |

### FBiHPOS Mountpoints (live sourcetable 2026-05-15)

| Mountpoint | Format | Method | Systems | Solution |
|---|---|---|---|---|
| MAX-AUTO | RTCM 3 | MAX | GPS+GLO | Network |
| MAX-AUTO_CSCS | RTCM 3 | MAX | GPS+GLO | Network |
| MAX-AUTO_SRJV1000 | RTCM 3 | MAX | GPS+GLO+GAL+BDS | Network |
| iMAX-AUTO | RTCM 3 | iMAX | GPS+GLO | Network |
| iMAX-3G | RTCM 3 | iMAX | GPS+GLO+GAL | Network |
| VRS-AUTO | RTCM 3 | VRS | GPS+GLO | Network |
| VRS-3G | RTCM 3 | VRS | GPS+GLO+GAL | Network |
| NEAREST | RTCM 3 | Nearest | GPS+GLO | Single base |
| NEAREST-3G | RTCM 3 | Nearest | GPS+GLO+GAL | Single base |
| FBiH_H+V | RTCM 3 | Combined H+V | GPS+GLO+GAL+BDS | Network |
| SRJV1000_H+V | RTCM 3 | H+V | GPS+GLO+GAL+BDS | Network |
| DKS_H+V | RTCM 3 | H+V | GPS+GLO+GAL+BDS | Network |
| FKP-AUTO-1819 | RTCM 2 | FKP | GPS+GLO | Network |
| FBIHPOS_DGNSS | RTCM 2 | DGNSS | GPS+GLO | Single base |
| diplomski | RTCM 3 | — | GPS+GLO+GAL+BDS | Test stream (inactive flag) |

---

## Context Notes

- **BiHPOS dual-entity structure**: BiHPOS is the project name for the unified national CORS network funded under an EU/EC project. The constitutional division (two entities) means the network is split into two independently operated sub-networks. No unified single endpoint or single registration for all of BiH.
- **FBiHPOS hostname**: The current authoritative host is `fbihpos.katastar.ba` (per FGU 2024 access guide and live probe). The older third-party-cited `fbihpos.fgu.com.ba` is no longer the canonical entry point. FGU's web domain itself is `.com.ba`, not `.gov.ba`.
- **Ports**: FBiHPOS uses 8080 (not the conventional NTRIP 2101). SRPOS publishes on 2101 (preferred) and 8080 (legacy IP route).
- **Tariff parity**: RTK 1-month and 12-month rates are essentially identical across both sub-networks (250 KM / 1,000 KM). FBiHPOS adds a 100 KM one-time registration. SRPOS has per-minute and short hourly blocks (10 h / 20 h / 50 h) making it cheaper for occasional use. Both annualised tiers exceed this project's ~$200/yr free/cheap-RTK cutoff.
- **No free tier**: Neither SRPOS nor FBiHPOS offers an open or free NTRIP stream.
- **Volunteer / community bases**: 1 rtk2go base — `AGROORSOLIC` at 45.01°N, 18.60°E (Posavina, near Orašje), confirmed in `data/stations.json` 2026-05-15 with country code `BIH`. Zero Centipede or EarthScope BA nodes. Coverage of central/southern Bosnia is negligible from free sources.
- **Cross-border free alternatives**: Within ~200 km of Sarajevo (43.85, 18.36), the only free options are a cluster of ~15 rtk2go bases on the Serbian side (Vojvodina / north Serbia, ~138–200 km out — see `RS_Serbia.md`). Croatian, Montenegrin, and Albanian sides offer no free rtk2go cover within practical RTK baseline distance.

## Post-Processing (RINEX) Options

| Service | Cost | Source |
|---|---|---|
| SRPOS post-processing RTK <30 s/hr | 22 KM/hr | rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf |
| SRPOS RINEX delivery (RTK) | 28 KM/hr | same |
| SRPOS RINEX delivery (DGPS archived) | 19 KM/hr | same |
| FBiHPOS RINEX download 1 h | 10 KM | FGU tariff §4.4.2 |
| FBiHPOS VRINEX 1 h | 15 KM | FGU tariff §4.4.4 |
| FBiHPOS online LGO obrada 30 min | 10 KM | FGU tariff §4.4.5 |
| FBiHPOS post-processing-only 12 mo flat | 700 KM | FGU tariff §4.4.7 |

## Sources Consulted (probe results, 2026-05-15)

- RGURS SRPOS page (SR-Cyrillic): https://www.rgurs.org/stranica/srpos — HTTP 200 OK
- RGURS SRPOS page (EN): https://www.rgurs.org/en/stranica/srpos — confirmed via WebSearch result snippet
- SRPOS SBC registration: https://srpos.rgurs.org/sbc/Account/Register — reachable; natural-person registration confirmed
- SRPOS user-access guide PDF: https://www.rgurs.org/uploads/pages/SRPOS_Korisnicki_pristup.pdf — HTTP 200 (736 KB, 2 pages)
- SRPOS tariff PDF (Sl. glasnik RS 85/2011): https://www.rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf — HTTP 200 (619 KB, 1 page)
- SRPOS NTRIP probe: `srpos.rgurs.org:2101` HTTP/0.9 SOURCETABLE 200, GNSS Spider 7.11.0.96, 18 STR rows (curl 2026-05-15 17:36 UTC)
- FGU services page: https://www.fgu.com.ba/bs/servisi.html — HTTP 200 (Apache, cookie set, last-modified 2026-05-15)
- FBiHPOS access guide (2024 PDF): https://www.fgu.com.ba/files/Novosti/2024/PDF/FBiHPOS%20-%20novo/Pristup%20FBiHPOS%20servisima.pdf — HTTP 200 (141 KB)
- FBiHPOS tariff PDF (V. broj 605/2022): https://www.fgu.com.ba/files/Novosti/2022/PDF/tarife/b/TARIFA%20NAKNADA%20ZA%20VRSENJE%20USLUGA%20IZ%20OBLASTI%20PREMJERA%20I%20KATASTRA.pdf — HTTP 200 (518 KB, 8 pages)
- FBiHPOS application form PDF: https://www.fgu.com.ba/files/Novosti/2022/PDF/FBIHPOS%20zahtjev/b/Zahtjev%20za%20koristenje%20usluga%20FBHIPOS%20mreze%20permanentnih%20stanica.pdf — HTTP 200 (93 KB, 2 pages)
- FBiHPOS NTRIP probe: `fbihpos.katastar.ba:8080` HTTP/0.9 SOURCETABLE 200, GNSS Spider 7.9.0.386, 15 STR rows (curl 2026-05-15 17:36 UTC)
- FBiHPOS SBC portal: `http://fbihpos.katastar.ba/SBC` HTTP 302 redirect (live)
- Datum / EPSG: https://epsg.io/10328 (BH_ETRS89), https://epsg.io/10329 (ETRS89-BIH / TM), https://epsg.io/10326 — source cited as FGU "Rulebook for Basic Geodetic Works", Feb 2019
- Architecture article (34 stations, EU-funded, 2011 launch): https://www.gim-international.com/content/news/gnss-reference-station-network-for-bosnia-and-herzegovina — WebFetch 200
- Local data: `py scripts/stations_by_country.py BIH` → 1 station (AGROORSOLIC, rtk2go, 45.01, 18.60); `py scripts/stations_by_radius.py 43.85 18.36 200` → 1 BIH (AGROORSOLIC at 130 km) plus 17 SRB rtk2go bases at 138–200 km
