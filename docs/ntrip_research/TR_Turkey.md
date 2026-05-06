# Turkey [TR] — NTRIP RTK Caster Research
**Date researched:** 2026-04-30

## Status: YES — national government NTRIP RTK caster operating (TUSAGA-Aktif / CORS-TR)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — national government service |
| **host:port** | `212.156.70.42:2101` (also `tusaga-aktif.gov.tr:2101`) |
| **tariff** | Published on tusaga-aktif.gov.tr; all prices **KDV dahil** (VAT inclusive), 2026 tariff set by BHİKPK |
| **VRS** | Yes (Ağ-RTK / Network RTK corrections) |
| **hobbyist_eligibility** | Yes — individual ("bireysel") registration accepted; same-day activation |
| **legal_residency_required** | Yes (effectively) — online registration requires TC Kimlik No (Turkish national ID); foreign nationals without a Turkish ID cannot self-register online |
| **last_confirmed_alive** | 2026-04-30 (portal homepage loaded with current 2026 price list) |

## Tariff (2026, KDV / VAT dahil / inclusive)

| Product | TRY (gross incl. KDV) | USD equiv. (~32.9 TRY/USD) |
|---|---|---|
| Cihaz Abonelik (device subscription, required first) | ₺550.00 | ~$16.7 |
| RTK 1 Month | ₺1,000.00 | ~$30.4 |
| RTK 2 Months | ₺2,000.00 | ~$60.8 |
| RTK 3 Months | ₺3,000.00 | ~$91.2 |
| RTK 4 Months | ₺4,000.00 | ~$121.6 |
| RTK 5 Months | ₺5,000.00 | ~$152.0 |
| RTK 6 Months | ₺6,000.00 | ~$182.4 |
| RTK 1 Year | ₺8,135.00 | ~$247.3 |
| DGPS 1 Month | ₺405.00 | ~$12.3 |
| DGPS 1 Year | ₺2,985.00 | ~$90.7 |
| 30 sec RINEX | ₺0.00 | Free |
| 1 sec RINEX | ₺4.00 / session | ~$0.12 |

Source: https://tusaga-aktif.gov.tr/ (homepage, observed 2026-04-30).

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

## Sources Consulted
- TUSAGA-Aktif homepage with 2026 price list: https://tusaga-aktif.gov.tr/
- TKGM FAQ (TC Kimlik No requirement): https://www.tkgm.gov.tr/
- Academic paper citing IP and port: sirgas.ipgh.org / various GNSS conference proceedings
