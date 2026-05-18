# Algeria [DZ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; original 2026-05-06) | USD/DZD rate: 1 USD ≈ 132.23 DZD

## Status: RESTRICTED — AL-CORS-Net operational but no public access (re-verified 2026-05-17: no new public endpoint, tariff, or registration portal has been announced; INCT remains the sole point of contact; inct.mdn.dz still SSL-broken / ECONNREFUSED; asjp.cerist.dz article URL returns TLS cert-verification failure)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — likely exists internally; not publicly accessible |
| **landing_url** | http://inct.mdn.dz (INCT institutional portal; SSL broken / ECONNREFUSED 2026-05-17 — no other operator-owned NTRIP-service page located) |
| **access_url** | null — no public signup/conditions page exists; access is granted only via direct contact (contact@inct.dz / inct@mdn.dz / +213 23 79 50 26) |
| **host:port** | null — no published endpoint |
| **tariff** | null — no pricing found |
| **num_stations** | 189 (AL-CORS-Net; North + South subdivisions; cited in INCT documentation and Takka et al. 2023 performance paper) |
| **hobbyist_eligibility** | no |
| **legal_residency_required** | ? |
| **last_confirmed_alive** | VRS sessions confirmed Oct 2021 – Jan 2022 (research paper published 2023); no newer public liveness signal |
| **datum_epoch** | omitted — no citable operator declaration available (INCT portal unreachable; AL-CORS-Net documentation not published outside the asjp.cerist.dz paper, which is not the operator's portal/spec) |

## AL-CORS-Net

**Operator:** INCT (Institut National de Cartographie et de Télédétection), Ministry of National Defense
**Also known as:** SAAP — Système Algérien d'Aide au Positionnement
**Portal:** http://inct.mdn.dz (SSL issues; ECONNREFUSED as of 2026-05-06)
**Contact:** contact@inct.dz / inct@mdn.dz / +213 23 79 50 26
**Backend:** Geo++ GNSMART — delivers Network RTK via VRS over NTRIP
**Stations:** 189 permanent GNSS stations across Algeria (North and South subdivisions); original published network cited 6 anchor stations (Algiers DZAL, Oran DZOR, Constantine DZCO, Ouargla OGLA, Bechar BECH, Tindouf TIND)
**Performance:** ~1.3 cm horizontal, ~2.2 cm vertical (1σ); 97.25% VRS availability; 98.8% horizontal integrity; 94.9% vertical integrity

No public endpoint, registration portal, or tariff is advertised. Direct contact with INCT is required; no confirmed civilian or non-governmental access on record.

**Hobbyist context:** the `no` in the field above is de-facto, not a published prohibition. INCT operates under the Ministry of National Defense; the network is reserved for institutional and professional users, and no hobbyist tier or civilian onboarding path is published.

## REGAT (secondary network — not RTK)

53 stations operated by CRAAG (Centre de Recherche en Astronomie, Astrophysique et Géophysique) — seismotectonic monitoring only; no real-time RTK dispensed.

## Commercial Providers

No commercial RTK provider (SmartNet, Trimble VRS Now, GEODNET, onocoy, Polaris) has confirmed Algeria coverage.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS / CDDIS** — sparse scientific stations; nearest dense coverage is Tunisia/Morocco | https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/ | Free (NASA Earthdata account required) |

## Sources Consulted
- INCT/SAAP: http://www.inct.mdn.dz/source/act-saap.php
- Research paper (VRS performance assessment): https://asjp.cerist.dz/en/article/216928 — Takka Elhadi, Touabet Touabet, Boudrassene Abdennour (survey Oct 2021 – Jan 2022; published 2023)
- GIM International CORS Africa map: https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- RTK2GO, ntrip-list.com/africa/, corsstations.com — no DZ entries
- GEODNET, onocoy, Trimble VRS Now, SmartNet — no DZ coverage confirmed
