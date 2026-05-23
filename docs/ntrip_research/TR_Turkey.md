# Turkey [TR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-23 (refresh of 2026-05-17 entry; live curl probe of 212.156.70.42:2101 returned SOURCETABLE 200 OK, 1142-byte sourcetable, 9 MPs identical; tariff re-fetched from tusaga-aktif.gov.tr — 2026 schedule unchanged)
last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-17
last_caster_search_date: 2026-05-17
agent_version: 0.1

## Status: YES — national government NTRIP RTK caster operating (TUSAGA-Aktif / CORS-TR)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — national government service |
| **host:port** | `212.156.70.42:2101` (also `tusaga-aktif.gov.tr:2101`) |
| **tariff** | Published on tusaga-aktif.gov.tr; all prices **KDV dahil** (VAT inclusive), 2026 tariff set by BHİKPK |
| **VRS** | Yes (Ağ-RTK / Network RTK corrections) |
| **hobbyist_eligibility** | Yes — individual ("bireysel") registration accepted; same-day activation |
| **legal_residency_required** | Yes (effectively) — online registration requires TC Kimlik No (Turkish national ID); foreign nationals without a Turkish ID cannot self-register online |
| **num_stations** | ~146 permanent CORS stations across Turkey + Northern Cyprus (ISPRS-Annals IV-4-W4/2017 + multiple peer-reviewed sources; consistent figure across academic literature) |
| **last_confirmed_alive** | 2026-05-23 — `212.156.70.42:2101` SOURCETABLE 200 OK; Trimble Pivot Caster 5.2; 9 mountpoints; 1142 bytes (2-byte delta from 2026-05-17 1140-byte snapshot, content identical) |
| **datum_epoch** | TUREF (Turkish national frame) = ITRF96 epoch 2005.0. Cited inline by the three TG20 broadcast streams in sourcetable field 19 as `{"REF":{"NAME":"ITRF96","EPOCH":2005.0}}` (`212.156.70.42:2101`, 2026-05-23). The VRS / FKP / DGPS streams do not carry an inline datum field; their frame is implied by the network-wide TUREF declaration but no separate operator URL confirming the VRS/FKP/DGPS streams output TUREF was located (checked: tkgm.gov.tr/sss 2026-05-23; tusaga-aktif.gov.tr homepage 2026-05-23). |

## Tariff (2026, KDV / VAT dahil / inclusive)

USD column uses ~45.74 TRY/USD (TCMB / Trading Economics indicative rate, 2026-05-22). TRY has depreciated rapidly through 2024–2026; USD equivalents age quickly — always re-check rate before quoting.

| Product | TRY (gross incl. KDV) | USD equiv. (~45.74 TRY/USD) |
|---|---|---|
| Cihaz Abonelik (device subscription, required first) | ₺550.00 | ~$12.0 |
| RTK 1 Month | ₺1,000.00 | ~$21.9 |
| RTK 2 Months | ₺2,000.00 | ~$43.7 |
| RTK 3 Months | ₺3,000.00 | ~$65.6 |
| RTK 4 Months | ₺4,000.00 | ~$87.5 |
| RTK 5 Months | ₺5,000.00 | ~$109.3 |
| RTK 6 Months | ₺6,000.00 | ~$131.2 |
| RTK 1 Year | ₺8,135.00 | ~$177.9 |
| DGPS 1 Month | ₺405.00 | ~$8.9 |
| DGPS 2 Months | ₺810.00 | ~$17.7 |
| DGPS 3 Months | ₺1,215.00 | ~$26.6 |
| DGPS 4 Months | ₺1,620.00 | ~$35.4 |
| DGPS 5 Months | ₺2,025.00 | ~$44.3 |
| DGPS 6 Months | ₺2,430.00 | ~$53.1 |
| DGPS 1 Year | ₺2,985.00 | ~$65.3 |
| 30 sec RINEX | ₺0.00 | Free |
| 1 sec RINEX | ₺4.00 / file | ~$0.09 |

Source: https://tusaga-aktif.gov.tr/ (homepage, re-fetched 2026-05-23, tariff identical to 2026-05-13 snapshot). All prices set annually by BHİKPK (Interministerial Coordination and Planning Commission for Mapping).

**Note on discounts:** Public institutions and universities receive a **75% discount** on 1-sec RINEX. Universities and vocational schools may apply for **free use** within their campus areas.

## Context Notes

- **TUSAGA-Aktif** (Türkiye Ulusal Sabit GNSS İstasyonları Ağı — Aktif): Turkey's national continuously operating reference station network, operated by TKGM (Tapu ve Kadastro Genel Müdürlüğü — General Directorate of Land Registry and Cadastre). Also referred to as CORS-TR.
- The host IP `212.156.70.42` and port `2101` are explicitly documented in TKGM FAQ and academic publications: *"TUSAGA-Aktif Sistemi Ağ-RTK Düzeltme Verileri 212.156.70.42 IP adresi ve 2101 Port Numarası üzerinden yayınlanmaktadır."*
- Corrections are streamed as Ağ-RTK (Network RTK), which is VRS-based. Single-base RTK is not the primary product.
- Registration is individual ("bireysel") or corporate. The site states users can register and **start using the same day**: *"Henüz bir hesabınız yoksa aşağıdaki kayıt ol düğmesini tıklayarak hesap oluşturabilir ve kullanmaya aynı gün başlayabilirsiniz."*
- **TC Kimlik No** (Turkish national identity number) is mandatory on the online registration form. This number is issued only to Turkish citizens and registered foreign residents (foreigners with residence permit). Foreign nationals without a Turkish ID cannot self-register online; direct contact with TKGM/TUSAGA-Aktif would be required.
- A device subscription (Cihaz Abonelik, ₺550) must be purchased first before any RTK or DGPS time subscription.
- The VAT rate in Turkey is currently 20% (standard rate as of 2026); all published prices are already KDV inclusive so no addition is required.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **TUSAGA-Aktif 30-sec RINEX** | https://tusaga-aktif.gov.tr/ | Free (account required) |
| **TUSAGA-Aktif 1-sec RINEX** | https://tusaga-aktif.gov.tr/ | ₺4.00 per session (~$0.12); 75% discount for institutions |

## Sourcetable Mountpoints (curl probe 2026-05-23; 2-byte delta from 2026-05-17, content identical)

- `VRSCMRP` — VRS, CMR+, GPS+GLO
- `VRSRTCM31` — VRS, RTCM 3.1, GPS+GLO
- `VRSRTCM34` — VRS, RTCM 3.4 MSM, GPS+GLO+GAL+BDS+QZS (modern multi-constellation stream — preferred for current rovers)
- `RTCM3Net` — Network RTK
- `FKP_RTCM31` — FKP, RTCM SAPOS, GPS+GLO
- `DGPSNet` — DGPS, RTCM 2.3 (TNC1)
- `TG20-BATI-BRDCST-RTCM` — single-direction broadcast stream for 25°–32° longitude band ("West"), RTCM 3.1, GPS+GLO, ITRF96 epoch 2005.0
- `TG20-ORTA-BRDCST-RTCM` — 32°–38° longitude band ("Centre"), RTCM 3.1, GPS+GLONASS, ITRF96 epoch 2005.0
- `TG20-DOGU-BRDCST-RTCM` — 38°–45° longitude band ("East"), RTCM 3.1, GPS+GLONASS, ITRF96 epoch 2005.0

The three TG20 broadcast streams are one-way (no NMEA upload required), which makes them usable on rovers that cannot send GGA — useful for fielded hardware with limited bandwidth. They are pinned to ITRF96 epoch 2005.0 (TUREF, Turkish national datum).

## Sources Consulted
- TUSAGA-Aktif homepage with 2026 price list: https://tusaga-aktif.gov.tr/
- TUSAGA-Aktif user agreement (PDF): https://www.tusaga-aktif.gov.tr/Content/Files/tusaga-aktif-kullanici-sozlesmesi.pdf
- TKGM FAQ (TC Kimlik No requirement, pricing): https://www.tkgm.gov.tr/sss/tusaga-aktif-sistemi-kullanici-islemleri
- TKGM FAQ (technical, IP/port): https://www.tkgm.gov.tr/sss/tusaga-aktif-sistemi-teknik-konulari
- TKGM pricing FAQ node: https://www.tkgm.gov.tr/node/3364
- curl probe of `212.156.70.42:2101` — SOURCETABLE 200 OK 2026-05-23 (Trimble Pivot Caster 5.2; 9 mountpoints; 1142-byte sourcetable; 2-byte whitespace delta from prior 1140-byte snapshot, content identical)
