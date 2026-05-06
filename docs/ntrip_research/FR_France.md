# France [FR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — Centipede RTK (INRAE-coordinated community network) provides de-facto national free coverage; commercial Orphéon available; no free government caster

---

## Service A: Centipede RTK (FREE — community/open-source — primary for hobbyists)

| Field | Value |
|---|---|
| **Operator** | Centipede-RTK association (non-profit, formed August 2024); historically coordinated by INRAE (Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement). Open-source: https://github.com/CentipedeRTK |
| **host:port** | `crtk.net:2101` **(canonical since 2025-03-18)** |
| **Old host (still redirects)** | `caster.centipede.fr:2101` — was the canonical address until 2025-03-18; still resolves but redirects to new caster |
| **Caster software** | Millipede (open-source, by Pierre Beyssac; https://github.com/pbeyssac/millipede-caster) — migrated from legacy caster on 2025-03-18 at 22:17 Paris time; 50× capacity improvement |
| **VRS** | No — physical base stations only; network density makes single-base RTK viable in most metropolitan France |
| **Mountpoints** | `NEAR` (auto-nearest station, RTCM3 MSM7); `NEAR4` (auto-nearest, MSM4, lower bandwidth for older receivers); individual station names (see https://map-centipede-rtk.org/) |
| **tariff** | **Free — €0.00.** No subscription, no registration required. Anonymous access. Date observed: 2026-05-06. Source: https://www.centipede-rtk.org/fr/the-centipede-rtk-network |
| **Credentials** | Username: `centipede` (or `c`); Password: `centipede` (or `c`); or no credentials (anonymous) |
| **hobbyist_eligibility** | **Yes** — fully open, no registration required |
| **legal_residency_required** | **No** |
| **Simultaneous connection limit** | 1 device per IP address |
| **last_confirmed_alive** | crtk.net:2101 — sourcetable confirms >1,200 STR entries globally as of 2026-05-06; France-coded ~719 stations |

### Centipede Network Scale and Coverage (as of 2025–2026)
- **French metropolitan stations:** ~625 bases installed in mainland France since launch (2019); ~719 France-coded nodes active on crtk.net sourcetable
- **Global network:** ~860+ bases in 30 countries worldwide (primarily France, then overseas territories, Belgium, Germany, Spain, and others)
- **Coverage zone per base:** ~50 km radius; coverage is very dense in grain-belt agricultural regions (Occitanie, Grand Est, Bretagne) and sparser in mountainous areas (Alps, Pyrenees)
- **RENAG integration:** Since June 2023, ~30 RENAG (Réseau National GNSS Permanent) scientific stations are re-distributed through Centipede, particularly strengthening southeastern France coverage

### Caster Migration Details (2025-03-18)
- **Migration date:** 2025-03-18, completed at 22:17 Paris time
- **Old address:** `caster.centipede.fr:2101` (remains active, auto-redirects to `crtk.net`)
- **New address:** `crtk.net:2101`
- **Action required:** Update NTRIP client configurations to use `crtk.net:2101`; the old address redirect is not guaranteed indefinitely
- **Why migrated:** New Millipede caster software is open-source, more performant (50× user capacity), and simpler to operate. Millipede automatically connects rover to nearest base via `NEAR` mountpoint.

---

## Service B: Orphéon (PAID — professional/commercial)

| Field | Value |
|---|---|
| **Operator** | Géodata Diffusion SAS (part of Hexagon Group) |
| **host** | `ntrip.reseau-orpheon.fr` |
| **port — topography** | 8500 |
| **port — agriculture** | 7500 |
| **VRS** | Yes — VRS and i-Max (individualized MAX) mountpoints |
| **Mountpoints (topography)** | `VRS_RTCM-MSM_FULL`, `VRS_RTCM-3.0_GG`, `VRS_CMRx_GG`, `i-Max_RTCM-MSM_FULL`, `i-Max_RTCM-3.0_GG` |
| **Mountpoints (agriculture)** | `VRS_RTCM-MSM_FULL`, `VRS_RTCM-3.0_GG`, `i-Max_RTCM-MSM_FULL`, `i-Max_RTCM-3.0_GG`, `Plus_pres_RTCM3_GG`, `Plus_pres_CMRPlus_GG` |
| **tariff** | **€756 to €3,456 TTC (VAT included)** per subscription depending on coverage area (departmental/regional/national) and service type; commitment periods 1–5 years (5% discount at 36 months, 10% at 60 months). Date observed: 2026-05-06. Source: https://www.flyingeye.fr/product/abonnement-ntrip-corrections-rtk-orpheon/ and https://reseau-orpheon.fr/en/orpheon-services/orpheon-rtk-subscriptions/ |
| **VAT** | Prices quoted TTC (VAT inclusive); French standard VAT 20% |
| **hobbyist_eligibility** | **Yes** — annual subscriptions and hourly packages available for individuals; no licence requirement stated |
| **legal_residency_required** | **Unclear** — French company; international users may subscribe via web shop |
| **last_confirmed_alive** | reseau-orpheon.fr portal accessible 2026-05-06 |

- **Stations:** ~215–220 permanent Full GNSS stations across mainland France and French West Indies; ~60 km average inter-station spacing
- **Constellations:** GPS, GLONASS, Galileo, BeiDou (Full GNSS)
- **Note:** Orphéon also offers "RTK on demand" hourly packages via shop.reseau-orpheon.fr for occasional users

---

## Service C: RENAG (free, low-density, research-grade scientific stations)

| Field | Value |
|---|---|
| **Operator** | RESIF-RENAG (Réseau National GNSS Permanent); hosted at Observatoire de la Côte d'Azur |
| **host** | renag.resif.fr (NTRIP server hosted at OCA) |
| **tariff** | **Free** — authentication required (free registration) |
| **hobbyist_eligibility** | **Unclear** — primarily for research; registration open but intended for scientific use |
| **Stations:** | ~30 French stations redistributed via Centipede since June 2023; RENAG direct caster used mainly by researchers |
| **Coverage:** | Patchy; concentrates in south-east France |
| **last_confirmed_alive** | renag.resif.fr accessible 2026-05-06 |

**Note:** For practical RTK use, RENAG stations accessed via Centipede (`crtk.net:2101`) are a better option than connecting to the RENAG caster directly.

---

## No Free Government NTRIP

- **IGN France** (Institut Géographique National) operates ~100+ permanent GNSS reference stations (RGP — Réseau GNSS Permanent) used for geodetic reference, but does **not** provide a free public RTK NTRIP stream. IGN stations are available for RINEX post-processing download only.
- The Centipede network fills the role of a free public RTK network that governments provide elsewhere.

---

## Overseas Territories Note

Centipede coverage exists in some overseas territories (Martinique, Guadeloupe, Réunion have a handful of bases) but is sparse to absent in many DOM-TOM. For Caribbean territories check dedicated files (HT, GP, MQ, etc.).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGN RGP RINEX archive** — national geodetic stations | https://rgp.ign.fr/ | Free (registration required) |
| **RENAG RINEX archive** | https://renag.epos-france.fr/donnees/ | Free (account required) |
| **EUREF/EPN** — French EPN stations | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- Centipede-RTK documentation: https://docs.centipede.fr/docs/centipede/3_connect_caster.html
- Centipede-RTK network: https://www.centipede-rtk.org/fr/the-centipede-rtk-network
- Geocommuns forum — caster migration announcement: https://forum.geocommuns.fr/t/nouveau-caster-pour-centipede-rtk-ce-sera-le-18-mars-2025-a-21-heures/2182
- Millipede caster (GitHub): https://github.com/pbeyssac/millipede-caster
- Centipede INRAE press: https://www.inrae.fr/en/news/democratising-precision-guided-agriculture-ever-expanding-centipede-rtk-network
- Intrax — Centipede migration guide: https://intrax.farm/blog/autoguidage/migration-serveur-centipede-comment-faire/
- Orphéon network: https://reseau-orpheon.fr/en/the-orpheon-network/
- Orphéon FAQ / setup: https://reseau-orpheon.fr/en/frequently-asked-questions/reception-and-setup-questions/
- Orphéon subscriptions: https://reseau-orpheon.fr/en/orpheon-services/orpheon-rtk-subscriptions/
- Orphéon subscription via Flying Eye (pricing): https://www.flyingeye.fr/product/abonnement-ntrip-corrections-rtk-orpheon/
- RENAG real-time RTK: https://renag.resif.fr/fr/donnees/rtk/
- RENAG via Centipede (June 2023): https://www.epos-france.fr/en/blog/2022/07/12/renag-distributes-its-data-in-real-time/
- ArduSimple France: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-france/
- NTRIP-list.com Europe: https://ntrip-list.com/europe/
