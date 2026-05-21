# Bosnia and Herzegovina [BA] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-15)
**status:** YES — two government NTRIP RTK casters under the EU-funded BiHPOS umbrella, one per entity (SRPOS in Republika Srpska, FBiHPOS in Federation of BiH). Both paid, both live by direct sourcetable fetch 2026-05-21. No free state tier. Volunteer single base in northern Posavina.

BiH is a dual-entity state. BiHPOS is the project name for the unified national CORS network; the constitutional division splits it into two independently operated sub-networks with separate endpoints, tariffs, and registration. No single unified BiH endpoint exists.

---

## SRPOS — Republika Srpska

| field | value |
|---|---|
| landing_url | https://www.rgurs.org/stranica/srpos (English mirror: https://www.rgurs.org/en/stranica/srpos) |
| access_url | https://srpos.rgurs.org/sbc/Account/Register — Leica Spider Business Center self-registration; natural persons (физичка лица) place `"007"` in the company-registration field per form labels |
| operator | RGURS / RUGIPP — Republička uprava za geodetske i imovinsko-pravne poslove |
| admin contact | Spomenko Mitrović — +387 55 220-890 / 202-643 — `srposnet@rgurs.org` |
| host:port | `srpos.rgurs.org:2101` — live `SOURCETABLE 200 OK` from `GNSS Spider 7.11.0.96/1.0`, 18 STR rows, 1951 bytes, 2026-05-21. Port 8080 also documented; legacy IP `81.93.74.247:8080`. |
| num_stations | ~17 CORS (RS portion of the ~34-station BiHPOS network) |
| launched | 27 September 2011 |
| vrs | yes — `VRS.GK6`, `iVRS.GK6` plus MAX/iMAX/iMAXGK6_3s and Nearest variants in live sourcetable |
| tariff | BAM (KM, pegged 1 EUR = 1.95583 KM) per Odluka, Sl. glasnik RS 85/2011. RTK: 0.20 KM/min · 10 h 30 · 20 h 50 · 50 h 150 · 1 mo 250 · 2 mo 350 · 3 mo 450 · 4 mo 550 · 5 mo 650 · 6 mo 750 · 12 mo 1,000 KM. DGPS: 0.15 KM/min · 10 h 20 · 20 h 40 · 50 h 100 · 1 mo 200 · … · 12 mo 1,000 KM. Post-processing RTK ≤30 s 22 KM/hr; DGPS archived 19 KM/hr. RINEX delivery 28/19 KM/hr. Coordinate transformation 13 KM/point. A 20%-discount clause appeared in the 2013 amendment; whether it is still operative or superseded could not be verified — the RS Official Gazette electronic register was not accessible from the research environment. VAT not separately stated — published as statutory fee amounts. Observed 2026-05-21 on https://www.rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf |
| hobbyist_eligibility | yes — Leica SBC form imposes no surveying-licence requirement; explicitly accepts `"007"` placeholder for natural persons |
| legal_residency_required | ? — no citizenship/residency clause in the form or tariff PDF (formal gate: unknown). Practical barrier: payment requires an RS giro-account transfer, which in practice favours users with in-entity banking access. |
| last_confirmed_alive | 2026-05-21 — `srpos.rgurs.org:2101` SOURCETABLE 200 OK, 18 STR rows; same set as 2026-05-15 |
| datum_epoch | BH_ETRS89, GRS80 ellipsoid (Pravilnik o osnovnim geodetskim radovima, Feb 2019). Operator-hosted at https://www.fgu.com.ba/bs/pravilnici.html ; mirror https://epsg.io/10328 . Project realisation epoch ETRF2000 2011.307 widely cited in academic lit, no official URL pins it — BH_ETRS89 declaration is the only operator-citable piece. |

### SRPOS sourcetable (2026-05-21)

| Mount | Format | Method | Systems | Solution |
|---|---|---|---|---|
| VRS.GK6 | RTCM 3 | VRS | GPS+GLO+GAL | Network |
| iVRS.GK6 | RTCM 3 | VRS | GPS+GLO+GAL+BDS | Network |
| MAX.GK6_3s | RTCM 3 | MAX | GPS+GLO+GAL+BDS | Network |
| MAXGK6_3s / MAXGK6_3sR | RTCM 3 | MAX | GPS+GLO / GPS+GLO+GAL+BDS | Network |
| iMAX.GK6_3s / iMAX.GK6_3sR | RTCM 3 | iMAX | GPS+GLO+GAL+BDS | Network |
| iMAXGK6_3s / iMAXGK6_3sR | RTCM 3 | iMAX | GPS+GLO+GAL+BDS | Network |
| iMAX-AUTO_Galileo | RTCM 3 | iMAX | GPS+GLO+GAL+BDS | Network |
| VRS-AUTO-1819 | RTCM 2 | VRS | GPS+GLO | Network |
| NearestGK5/6/7_3s and `_3sR` | RTCM 3 | Nearest | GPS+GLO (+GAL+BDS on some) | Single base |
| iNearestGK5/6/7_3s | RTCM 3 | Nearest | GPS+GLO+GAL+BDS | Single base |

---

## FBiHPOS — Federation of BiH

| field | value |
|---|---|
| landing_url | https://www.fgu.com.ba/bs/servisi.html — FGU services page listing DSP / VPSP / GPSP |
| access_url | https://www.fgu.com.ba/files/Novosti/2022/PDF/FBIHPOS%20zahtjev/b/Zahtjev%20za%20koristenje%20usluga%20FBHIPOS%20mreze%20permanentnih%20stanica.pdf — application form, includes FIZIČKA LICA (natural persons) section |
| operator | FGU — Federalna uprava za geodetske i imovinsko-pravne poslove, Sarajevo |
| contact | `fbihpos@fgu.com.ba`, `uprava@fgu.com.ba` — +387 33 20 17 84 |
| host:port | `fbihpos.katastar.ba:8080` (port 8080, not the conventional 2101). Live `SOURCETABLE 200 OK` from `GNSS Spider 7.9.0.386/1.0`, 14 STR rows, 1522 bytes, 2026-05-21. Web SBC at `http://fbihpos.katastar.ba/SBC` (302 redirect). Older third-party-cited `fbihpos.fgu.com.ba` is no longer canonical. |
| num_stations | ~17 CORS (FBiH portion of the ~34-station BiHPOS network) |
| vrs | yes — `VRS-AUTO`, `VRS-3G` plus MAX/iMAX/FKP variants |
| tariff | BAM (KM, pegged 1 EUR = 1.95583 KM). FBiH Government Decision V. broj 605/2022 (2022-04-14), tariff group 4. **4.1.1** one-time registration 100 KM. **4.2 VPSP / RTK**: 7 d 150 · 1 mo 250 · 2 mo 350 · 3 mo 450 · 4 mo 550 · 5 mo 650 · 6 mo 750 · 12 mo 1,000 KM. **4.3 DSP / DGPS**: 1 mo 80 · 2 mo 120 · 3 mo 160 · 4 mo 200 · 5 mo 250 · 6 mo 300 · 12 mo 500 KM. **4.4 GPSP**: RINEX 15 min 3 / 1 h 10 KM; VRINEX 15 min 5 / 1 h 15 KM; LGO online 10 KM per 30 min; flat 12 mo all services 1,400 KM; flat 12 mo post-processing only 700 KM. Multi-rover discount −10% / −20% / cap −50%. VAT not separately itemised — paid to Federal Treasury single account. |
| hobbyist_eligibility | yes — application PDF has dedicated FIZIČKA LICA block, only name + address + contact required; 100 KM registration applies equally |
| legal_residency_required | ? — neither form nor tariff PDF mentions citizenship/residency; foreign-applicant pathway undocumented |
| last_confirmed_alive | 2026-05-21 — `fbihpos.katastar.ba:8080` SOURCETABLE 200 OK, 14 STR rows; same set as 2026-05-15 |
| datum_epoch | BH_ETRS89 projected as ETRS89-BIH / TM (CM 18°E, scale 0.9999, FE 500000). Pravilnik o osnovnim geodetskim radovima Feb 2019 (operator-hosted at https://www.fgu.com.ba/bs/pravilnici.html). Mirrors https://epsg.io/10329 + 10328. Academic densification epoch ETRF2000 2011.307 lacks citable official URL. |

### FBiHPOS sourcetable (2026-05-21)

| Mount | Format | Method | Systems | Solution |
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
| FBiH_H+V | RTCM 3 | Combined H+V | GPS+GLO+GAL | Network |
| SRJV1000_H+V | RTCM 3 | H+V | GPS+GLO+GAL+BDS | Network |
| FKP-AUTO-1819 | RTCM 2 | FKP | GPS+GLO | Network |
| FBIHPOS_DGNSS | RTCM 2 | DGNSS | GPS+GLO | Single base (out of scope) |
| diplomski | RTCM 3 | — | GPS+GLO+GAL+BDS | Test stream (inactive flag) |

(Older `DKS_H+V` mountpoint no longer present in 2026-05-21 sourcetable.)

---

## Context

- **Tariff parity / no free tier**: RTK 1-month / 12-month rates are essentially identical across both entities (250 KM / 1,000 KM). FBiHPOS adds a 100 KM one-time registration. SRPOS offers per-minute and short hourly blocks (10 h / 20 h / 50 h), so it is cheaper for occasional use. Both annualised tiers exceed the project's ~$200/yr free/cheap-RTK cutoff. Neither entity offers an open or free NTRIP stream.
- **Volunteer / community bases**: 1 rtk2go base — `AGROORSOLIC` (Ostra Luka, 45.01 N 18.60 E, RTCM 3.3 GPS+GLO+GAL+BDS), live in `data/rtk2go.sourcetable` 2026-05-21. Zero Centipede or EarthScope BA nodes. Coverage of central/southern Bosnia from free sources is negligible.
- **Cross-border free alternatives**: Within ~200 km of Sarajevo (43.85, 18.36) the only free options are a cluster of ~15 rtk2go bases on the Serbian side (Vojvodina / north Serbia, 138-200 km out — see `RS_Serbia.md`). These are beyond any usable single-base RTK baseline (practical limit ~30 km); they are geographically neighbouring but not RTK-usable supplements for central BiH. Croatian, Montenegrin, and Albanian sides offer no free rtk2go cover within practical RTK baseline distance.

## Post-processing options

| Service | Cost | Source |
|---|---|---|
| SRPOS RTK ≤30 s/hr | 22 KM/hr | rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf |
| SRPOS RINEX delivery (RTK / DGPS) | 28 / 19 KM/hr | same |
| FBiHPOS RINEX 1 h | 10 KM | FGU tariff §4.4.2 |
| FBiHPOS VRINEX 1 h | 15 KM | §4.4.4 |
| FBiHPOS LGO online 30 min | 10 KM | §4.4.5 |
| FBiHPOS post-processing-only 12 mo | 700 KM | §4.4.7 |

## Sources

- RGURS SRPOS page (Cyrillic): https://www.rgurs.org/stranica/srpos
- SRPOS SBC registration: https://srpos.rgurs.org/sbc/Account/Register
- SRPOS user-access guide PDF: https://www.rgurs.org/uploads/pages/SRPOS_Korisnicki_pristup.pdf
- SRPOS tariff PDF (Sl. glasnik RS 85/2011): https://www.rgurs.org/uploads/pages/SRPOS_Visine_naknada_za_koristenje_servisa_SRPOS.pdf
- SRPOS live caster: `curl --http0.9 http://srpos.rgurs.org:2101/` SOURCETABLE 200 OK, GNSS Spider 7.11.0.96, 18 STR (2026-05-21)
- FGU services page: https://www.fgu.com.ba/bs/servisi.html
- FBiHPOS access guide (2024): https://www.fgu.com.ba/files/Novosti/2024/PDF/FBiHPOS%20-%20novo/Pristup%20FBiHPOS%20servisima.pdf
- FBiHPOS tariff PDF (V. broj 605/2022): https://www.fgu.com.ba/files/Novosti/2022/PDF/tarife/b/TARIFA%20NAKNADA%20ZA%20VRSENJE%20USLUGA%20IZ%20OBLASTI%20PREMJERA%20I%20KATASTRA.pdf
- FBiHPOS application PDF: https://www.fgu.com.ba/files/Novosti/2022/PDF/FBIHPOS%20zahtjev/b/Zahtjev%20za%20koristenje%20usluga%20FBHIPOS%20mreze%20permanentnih%20stanica.pdf
- FBiHPOS live caster: `curl --http0.9 http://fbihpos.katastar.ba:8080/` SOURCETABLE 200 OK, GNSS Spider 7.9.0.386, 14 STR (2026-05-21)
- Datum / authority: Pravilnik o osnovnim geodetskim radovima (Feb 2019) at https://www.fgu.com.ba/bs/pravilnici.html ; EPSG mirrors https://epsg.io/10328 and https://epsg.io/10329
- Architecture article (34 stations, EU-funded, 2011 launch): https://www.gim-international.com/content/news/gnss-reference-station-network-for-bosnia-and-herzegovina
- Local data: `data/rtk2go.sourcetable` 2026-05-21 (AGROORSOLIC); `py scripts/stations_by_country.py BIH` → 1 rtk2go + 1 EUREF
