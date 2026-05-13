# France [FR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-07 entry)

## Status: YES — Centipede RTK (community) provides de-facto national free coverage; three commercial competitors (Orphéon, Teria, HxGN SmartNet); no free government caster

There is no free government NTRIP RTK service in France. IGN's RGP (Réseau GNSS Permanent) operates ~470 reference stations but redistributes them only as RINEX for post-processing. Real-time public RTK in France is split between:

- **Centipede RTK** — community/open-source, free, dense (709 FRA-coded mountpoints on `crtk.net:2101` sourcetable 2026-05-12; the largest free RTK footprint in continental Europe)
- **Three competing commercial casters** — Orphéon (Geodata Diffusion / Hexagon), Teria (Exagone / Ordre des Géomètres-Experts), HxGN SmartNet (Hexagon / Leica Geosystems) — annual subscription pricing, mostly aimed at surveyors and large-equipment agriculture

---

## Service A: Centipede RTK (FREE — community/open-source — primary for hobbyists)

| Field | Value |
|---|---|
| **Operator** | Centipede-RTK association (non-profit, formed August 2024); historically coordinated by INRAE (Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement). Open-source: https://github.com/CentipedeRTK |
| **host:port** | `crtk.net:2101` **(canonical since 2025-03-18)** |
| **Old host (still resolves)** | `caster.centipede.fr:2101` — was the canonical address until 2025-03-18; redirect not guaranteed indefinitely |
| **Caster software** | Millipede (open-source, by Pierre Beyssac; https://github.com/pbeyssac/millipede-caster) — migrated from legacy caster on 2025-03-18 at 22:17 Paris time; ~50× capacity improvement |
| **VRS** | No — physical base stations only; network density makes single-base RTK viable in most metropolitan France |
| **Mountpoints** | `NEAR` (auto-nearest station, RTCM3 MSM7); `NEAR4` (auto-nearest, MSM4, lower bandwidth for older receivers); individual station names (browse https://map.centipede-rtk.org/) |
| **tariff** | **Free — €0.00.** No subscription, no registration required. Anonymous access. Date observed: 2026-05-12. Source: https://www.centipede-rtk.org/the-centipede-rtk-network |
| **Credentials** | Username: `centipede` (or `c`); Password: `centipede` (or `c`); or no credentials (anonymous) |
| **hobbyist_eligibility** | **Yes** — fully open, no registration required |
| **legal_residency_required** | **No** |
| **Simultaneous connection limit** | 1 device per IP address |
| **last_confirmed_alive** | crtk.net:2101 — SOURCETABLE 200 OK on 2026-05-12 (curl probe). 1,205 STR entries globally; 709 FRA-coded. |

### Centipede Network Scale and Coverage (2025–2026)
- **French metropolitan stations:** 709 FRA-coded mountpoints on the live sourcetable (2026-05-12); ~625 bases installed in mainland France since launch (2019), with ongoing growth.
- **Global network:** ~860+ bases in 30 countries; France is dominant, then Hungary (217 `HUN`-coded on 2026-05-12 sourcetable), United Kingdom (45 `ENG`-coded — Centipede's `ENG` covers the whole UK including Scotland/Wales/Northern Ireland, *not* just England), Switzerland (30 `CHZ`-coded — Centipede's `CHZ` is Switzerland, *not* Czech Republic; Czech stations carry `CZE` separately, 3 nodes), with Belgium, Netherlands, Norway and others contributing 17–30 each. See `_centipede_country_codes.md` for the full Centipede non-ISO country-code legend.
- **Coverage zone per base:** ~50 km radius; very dense in grain-belt agricultural regions (Occitanie, Grand Est, Bretagne) and sparser in mountainous areas (Alps, Pyrenees).
- **RENAG integration:** Since June 2023, ~30 RENAG (Réseau National GNSS Permanent) scientific stations are re-distributed through Centipede, particularly strengthening southeastern France coverage.

### Caster Migration Details (2025-03-18)
- **Migration date:** 2025-03-18, completed at 22:17 Paris time
- **Old address:** `caster.centipede.fr:2101` (auto-redirect to `crtk.net`)
- **New address:** `crtk.net:2101`
- **Action required:** Update NTRIP client configurations to use `crtk.net:2101`; the old address redirect is not guaranteed indefinitely
- **Why migrated:** New Millipede caster software is open-source, more performant (~50× user capacity), and simpler to operate. Millipede automatically connects rover to nearest base via `NEAR` mountpoint.

---

## Service B: Orphéon (PAID — professional/commercial)

| Field | Value |
|---|---|
| **Operator** | Géodata Diffusion SAS (part of Hexagon Group) |
| **host** | `ntrip.reseau-orpheon.fr` |
| **port — topography** | 8500 (SOURCETABLE 200 OK on 2026-05-12; curl probe; Leica GNSS Spider 7.11.1.105/1.0; ~22 mountpoints) |
| **port — agriculture** | 7500 |
| **VRS** | Yes — VRS and i-Max (individualized MAX) mountpoints |
| **Mountpoints (topography)** | `VRS_RTCM-MSM_FULL`, `VRS_RTCM-3.0_GG`, `VRS_CMRx_GG`, `i-Max_RTCM-MSM_FULL`, `i-Max_RTCM-3.0_GG`, `Plus_pres_RTCM-3.0[_GG]`, `Max_RTCM-3.0_GG`, plus single-constellation/legacy variants |
| **Mountpoints (agriculture)** | `VRS_RTCM-MSM_FULL`, `VRS_RTCM-3.0_GG`, `i-Max_RTCM-MSM_FULL`, `i-Max_RTCM-3.0_GG`, `Plus_pres_RTCM3_GG`, `Plus_pres_CMRPlus_GG` |
| **tariff** | **€756 to €3,456 TTC (VAT included)** per subscription depending on coverage area (departmental/regional/national) and service type and hourly bracket (60h/100h/120h/200h/240h/300h packages also offered); 1–5 year commitment (5% discount at 36 months, 10% at 60 months). Antilles-Guyane sold at the same scale (from €895 HT/yr). Date observed: 2026-05-12. Source: https://www.flyingeye.fr/product/abonnement-ntrip-corrections-rtk-orpheon/ and https://reseau-orpheon.fr/en/orpheon-services/orpheon-rtk-subscriptions/ |
| **VAT** | Prices quoted TTC (VAT inclusive); French standard VAT 20% |
| **hobbyist_eligibility** | **Yes** — annual subscriptions and hourly packages available for individuals; no licence requirement stated |
| **legal_residency_required** | **Unclear** — French company; international users may subscribe via web shop |
| **last_confirmed_alive** | reseau-orpheon.fr portal accessible 2026-05-12; `ntrip.reseau-orpheon.fr:8500` SOURCETABLE 200 OK 2026-05-12 (curl) |

- **Stations:** **220 permanent Full GNSS stations** across mainland France and French West Indies/Guadeloupe (operator's own homepage 2026-05-12); ~60 km average inter-station spacing; described as "the first 100% Full GNSS network in France"
- **Constellations:** GPS, GLONASS, Galileo, BeiDou (Full GNSS)
- **Notes:** Orphéon also offers "RTK on demand" hourly packages via shop.reseau-orpheon.fr for occasional users; included add-ons in annual subs are 50 hours of post-processing/year, RINEX file access, smartphone app.

---

## Service C: Teria (PAID — professional/commercial; surveyor-cooperative)

| Field | Value |
|---|---|
| **Operator** | Exagone SAS, on behalf of the Ordre des Géomètres-Experts (OGE; chartered land-surveyor order). Network created 2005. |
| **host:port** | `teriartk.eu:2101` (also reachable at IP `78.24.131.136:2101`) |
| **Caster software** | GNSMART_Caster 2.0 (Geo++) — confirmed 2026-05-12 SOURCETABLE 200 OK (curl), 30+ mountpoints |
| **VRS** | Yes — VRS, i-Max, MAC, FKP, PRS variants in RTCM 2.3 / 3.0 / 3.1 / 3.2 (MSM4/MSM5) |
| **Stations** | ~187 GPS/GNSS bases (per i3map reseller listing) covering metropolitan France; coverage extends to neighbouring border zones (mountpoints labelled `TERIAEU…`) |
| **Mountpoints (selection)** | `VRS32` (VRS RTCM 3.2 MSM4), `VRS30`, `VRS30GPS`, `IMAC32`, `IMAC30`, `RTKMSM`, `RTKMSM_F9P`, `RTKMSM_LEI`, `MAC30`, `FKP30`, `PRS32`, `PRS32_F9P`, `NETMSM`, `UAV1`, `UAV2`, plus DGPS/legacy entries |
| **tariff** | **From €895 HT/yr (excl. 20% VAT)** for unlimited national RTK; reseller listings (i3map, D3E, Tech4Maps, Sttl-Topographie) sell weekly/monthly packs and Teriasat (L-band) variants. Prices marked HT (hors taxes); add 20% French VAT for TTC. Date observed: 2026-05-12. Source: https://www.reseau-teria.com/en/subscriptions-2/, https://www.tech4maps.com/abonnements-rtk (the operator's own subscriptions page now redirects pricing to a quote-request form; reseller pages remain the canonical published prices) |
| **VAT** | French standard VAT 20% (typical reseller listings quote HT) |
| **hobbyist_eligibility** | **Yes** — annual and short-period subscriptions available; no licence requirement; sold via several public web shops |
| **legal_residency_required** | **Unclear** — French entity; resellers ship internationally |
| **last_confirmed_alive** | `teriartk.eu:2101` SOURCETABLE 200 OK 2026-05-12 (curl probe) |

- **Variants:** TERIA (NTRIP RTK), TERIAsat (L-band PPP-style augmentation, no internet required), TERIArinex (post-processing).

---

## Service D: HxGN SmartNet France (PAID — Hexagon/Leica)

| Field | Value |
|---|---|
| **Operator** | Hexagon Geosystems (Leica Geosystems) |
| **Coverage** | Nationwide France integrated into pan-European HxGN SmartNet footprint |
| **NTRIP host** | Not publicly listed; provided after contract signing |
| **tariff** | Not published; enterprise contracts typical (cf. UK at £2,160/yr ex VAT for unlimited NRTK via SCCS Survey) |
| **hobbyist_eligibility** | Unclear; primarily marketed to professional surveyors and construction |
| **Portal** | https://hxgnsmartnet.com/fr |

---

## Service E: RENAG (free, low-density, research-grade scientific stations)

| Field | Value |
|---|---|
| **Operator** | RESIF-RENAG (Réseau National GNSS Permanent); hosted at Observatoire de la Côte d'Azur |
| **host** | renag.resif.fr (NTRIP server hosted at OCA) |
| **tariff** | Free — authentication required (free registration) |
| **hobbyist_eligibility** | **Unclear** — primarily for research; registration open but intended for scientific use |
| **Stations** | ~30 French stations redistributed via Centipede since June 2023; RENAG direct caster used mainly by researchers |
| **Coverage** | Patchy; concentrates in south-east France |
| **last_confirmed_alive** | renag.resif.fr accessible 2026-05-12 |

**Practical note:** For RTK use, RENAG stations accessed via Centipede (`crtk.net:2101`) are preferable to connecting to the RENAG caster directly.

---

## No Free Government NTRIP

- **IGN France** (Institut Géographique National) operates the RGP (Réseau GNSS Permanent), ~470 permanent reference stations used for geodetic reference, but does **not** provide a free public RTK NTRIP stream. RGP stations are available for RINEX post-processing download only.
- The Centipede network fills the role of a free public RTK network that governments provide elsewhere (e.g. Germany SAPOS, Poland ASG-EUPOS, Switzerland swipos).

---

## Volunteer / Other (rtk2go etc.)

- **rtk2go**: ~7 FR bases — negligible alongside Centipede's 720; only useful as a fallback for very specific localities.
- **Centipede vs rtk2go**: Centipede is the answer in France; do not default to rtk2go.

---

## Overseas Territories Note

Centipede has handfuls of bases in Martinique, Guadeloupe, Réunion, French Guiana, Saint-Martin, French Polynesia and others, but coverage is sparse to absent across most DOM-TOM. For Caribbean territories check dedicated files (HT, GP, MQ, etc.). TERIA and Orphéon also sell Antilles-Guyane subscriptions.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGN RGP RINEX archive** — national geodetic stations | https://rgp.ign.fr/ | Free (registration required) |
| **RENAG RINEX archive** | https://renag.epos-france.fr/donnees/ | Free (account required) |
| **EUREF/EPN** — French EPN stations | https://www.epncb.oma.be/ | Free |
| **Teria RINEX (TERIArinex)** | via Teria subscription | Bundled in Teria sub |

---

## Summary Table

| Service | host:port | Free? | VRS? | Hobbyist | Last alive |
|---|---|---|---|---|---|
| Centipede | `crtk.net:2101` | Yes | No (single-base + NEAR auto-nearest) | Yes | 2026-05-12 ✓ |
| Orphéon | `ntrip.reseau-orpheon.fr:8500/7500` | No (€756–3,456 TTC/yr) | Yes | Yes | 2026-05-12 ✓ |
| Teria | `teriartk.eu:2101` | No (from €895 HT/yr) | Yes | Yes | 2026-05-12 ✓ |
| HxGN SmartNet | not public | No (not published) | Yes | Unclear | n/a |
| RENAG | renag.resif.fr | Free + registration | No | Unclear | 2026-05-12 (portal) |

---

## Sources Consulted
- Centipede-RTK documentation: https://docs.centipede.fr/
- Centipede-RTK network homepage: https://www.centipede-rtk.org/
- Centipede public map: https://map.centipede-rtk.org/
- Geocommuns forum — caster migration announcement: https://forum.geocommuns.fr/t/nouveau-caster-pour-centipede-rtk-ce-sera-le-18-mars-2025-a-21-heures/2182
- Millipede caster (GitHub): https://github.com/pbeyssac/millipede-caster
- Centipede INRAE press: https://www.inrae.fr/en/news/democratising-precision-guided-agriculture-ever-expanding-centipede-rtk-network
- Centipede-RTK association formation (Aug 2024): https://gedeop-cati.hub.inrae.fr/projets/centipede
- Helicomicro 2025 update — Centipede status: https://www.helicomicro.com/2025/04/01/centipede-rtk/
- Réussir Machinisme — Millipede performance: https://www.reussir.fr/machinisme/autoguidage-le-reseau-centipede-rtk-nettement-plus-performant-avec-millipede
- Intrax — Centipede migration guide: https://intrax.farm/blog/autoguidage/migration-serveur-centipede-comment-faire/
- Orphéon network: https://reseau-orpheon.fr/en/the-orpheon-network/
- Orphéon FAQ / setup: https://reseau-orpheon.fr/en/frequently-asked-questions/reception-and-setup-questions/
- Orphéon subscriptions: https://reseau-orpheon.fr/en/orpheon-services/orpheon-rtk-subscriptions/
- Orphéon subscription via Flying Eye (pricing): https://www.flyingeye.fr/product/abonnement-ntrip-corrections-rtk-orpheon/
- Teria homepage: https://www.reseau-teria.com/en/home/
- Teria subscriptions: https://www.reseau-teria.com/en/subscriptions-2/
- Teria reseller (i3map): https://www.i3map.fr/fr/abonnements-corrections-gnss-differentielles-rtk/102-teria-abonnement-rtk-france-national-1-semaine.html
- Teria reseller (Tech4Maps): https://www.tech4maps.com/abonnements-rtk
- Teria reseller (D3E Geospatial): https://geospatial.d3e.fr/Abonnements-gnss-rtk/1722-teria.html
- HxGN SmartNet France: https://hxgnsmartnet.com/fr
- RENAG real-time RTK: https://renag.resif.fr/fr/donnees/rtk/
- RENAG via Centipede (June 2023): https://www.epos-france.fr/en/blog/2022/07/12/renag-distributes-its-data-in-real-time/
- ArduSimple France: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-france/
- NTRIP-list.com Europe: https://ntrip-list.com/europe/
- curl probe of `crtk.net:2101` — SOURCETABLE 200 OK 2026-05-12 (1,205 STR records; 709 FRA, 217 HUN, 45 ENG [= entire UK, not just England], 30 CHZ [= Switzerland, not Czech], 26 NLD, 21 NOR, 19 CAN, 18 FIN, 17 BEL — top countries by field-9 country code). For the full Centipede non-ISO country-code legend (including the `DAN`/`DNK`, `ROM`/`ROU`, `SER`/`SRB` parallel-code quirks) see `_centipede_country_codes.md`.
- curl probe of `teriartk.eu:2101` — SOURCETABLE 200 OK 2026-05-12 (Geo++ GNSMART, 30+ mountpoints)
- curl probe of `ntrip.reseau-orpheon.fr:8500` — SOURCETABLE 200 OK 2026-05-12 (Leica GNSS Spider 7.11.1.105/1.0, ~22 mountpoints)
- Orphéon homepage station count 2026-05-12: 220 Full GNSS stations (mainland + Antilles)
