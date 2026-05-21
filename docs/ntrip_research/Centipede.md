# Centipede — NTRIP RTK Research (cross-country volunteer network, not a country)

> **Scope note.** This is not a country entry. Centipede-RTK is a single
> volunteer caster (`crtk.net:2101`) carrying ~1,200 base stations across
> ~40 territory codes, dominated by France. Many country files reference
> Centipede stations; this entry consolidates the caster-wide facts
> (host, port, credentials, license, frame policy, association status,
> country-code quirks) so country files can point to a single source.
> For the non-ISO country code legend (`CHZ`=Switzerland, `ENG`=whole UK,
> `DAN`/`DNK`, `ROM`/`ROU`, `SER`/`SRB`), see `_centipede_country_codes.md`.

## Status: ACTIVE — single global caster, free, no registration, 1,213 STR rows live 2026-05-19; volunteer single-base RTK; non-profit Centipede-RTK association (FR law 1901) since 2024-08-28.

| Field | Value |
|---|---|
| **Network name** | Centipede-RTK (French: *Réseau GNSS Centipède*) |
| **Caster software** | Millipede (C, libevent, multithreaded, TLS, IP-anycast-ready) — open source, by Pierre Beyssac (https://github.com/pbeyssac/millipede-caster). Migrated 2025-03-18 22:17 Paris time from legacy `caster.centipede.fr` to `crtk.net`; ~50× capacity vs previous caster per operator. |
| **landing_url** | https://www.centipede-rtk.org/ |
| **access_url** | https://www.centipede-rtk.org/the-centipede-rtk-network — connection how-to (host, port, credentials, mountpoints). Technical reference: https://docs.centipede-rtk.org/access.html. |
| **host:port (canonical)** | `crtk.net:2101` (plain TCP, NTRIP 1 + 2 both supported) |
| **host:port (TLS)** | `crtk.net:443` (NTRIP 2.0 over TLS only — "only supported by some clients" per operator docs) |
| **host:port (legacy)** | `caster.centipede.fr:2101` still resolves but per operator the redirect is *not guaranteed indefinitely*; clients should be reconfigured. |
| **Tariff** | **Free.** "The service is provided free of charge and doesn't require any subscription." Source: https://www.centipede-rtk.org/the-centipede-rtk-network (observed 2026-05-21). No VAT/currency applicable. |
| **Credentials** | None required (anonymous works). Optional placeholder: username `c` or `centipede`, password `c` or `centipede`. Source: https://docs.centipede-rtk.org/access.html. |
| **hobbyist_eligibility** | Yes — no professional licence filter, anonymous access; DbCL 1.0 license permits commercial use of corrections subject to attribution. |
| **legal_residency_required** | No — association statutes do not restrict by residency; network already serves ~40 territories. |
| **Simultaneous connection limit** | 1 device / NTRIP client per IP. Source: https://docs.centipede.fr/docs/centipede/3_connect_caster.html *"Limite de connexion: 1 matériel/ntrip client par IP"*. |
| **last_confirmed_alive** | 2026-05-19 — pipeline `source_health.json` records `last_ok` for `centipede` source at 2026-05-19T08:33:26Z. Local fetch `data/centipede.sourcetable` carries 1,213 STR rows + 1 CAS + 1 NET record (`CAS;crtk.net;2101;Millipede-caster;Centipede-RTK;...`). |
| **num_stations** | ~1,213 physical bases (one mountpoint per base — Millipede caster does not multiplex multiple streams per station). NEAR + NEAR4 are routing aliases over the same physical set; do not double-count (primer `[stations-vs-mps]`). |
| **vrs** | No — single-base streams only. `NEAR` / `NEAR4` are *routing aliases* that auto-select the closest *physical* base by rover GGA; not a network solution (no MAC, no FKP, no VRS synthesis). |
| **datum_epoch** | **France only:** RGF93 v2b = ETRF2000 ep 2019.0 (current IGN realisation since 2021-01-05; coords from IGN online positioning → fixed in RTKBase). Operator docs note RGF93 coincides with ITRS at its 1989.0 *frame-definition* epoch — that is not the *coordinate* epoch used for base coords. Sources: https://docs.centipede-rtk.org/coordinate-systems.html + https://geodesie.ign.fr/le-reseau-geodesique-francais-1993-rgf93. **Non-France stations: operator does not declare a frame per station.** Primer `[centipede-intl]` documents the recipe (EU=ETRF2000, ROW=ITRF current) as guidance to base operators with no central enforcement — do not cite as the network's declared frame outside France. |

---

## Caster details

### Sourcetable

Live `crtk.net:2101` sourcetable header (verbatim from `data/centipede.sourcetable` 2026-05-19):

```
CAS;crtk.net;2101;Millipede-caster;Centipede-RTK;0;FRA;45.99;-1.02;0.0.0.0;0;https//map.centipede-rtk.org
NET;ASSO;CENTIPEDE-RTK;B;N;https://www.centipede-rtk.org/terms-conditions;https://docs.centipede.fr;contact@centipede-rtk.org;none
STR;...
```

STR row count: **1,213** (single ASSO network). Every STR row is `RTCM3` with messages `1004,1005,1006,1008,1012,1019,1020,1033,1042,1046,1077,1087,1097,1107,1127,1230`, carrier `2`, constellations `GLO+GAL+SBS+BDS+GPS`, network `CentipedeRTK`. Most stations are RTKBase-on-ZED-F9P installations.

NMEA flag in the sourcetable: 1,211 of 1,213 STR rows carry `nmea=0; solution=0`. Only `NEAR` and `NEAR4` carry `nmea=1` (router needs rover GGA to select closest base). The project's `fetch_stations.py` uses the default `nmea_filter=True` for the centipede source; with 99.8 % of bases already `nmea=0`, no override needed.

### NEAR / NEAR4 routing mountpoints

| Mount | Format | Use case |
|---|---|---|
| `NEAR` | RTCM3 MSM7 (full resolution) | Default; rover sends GGA, caster routes to closest declared base. 1 km hysteresis to avoid base-switching while moving. Source: https://docs.centipede-rtk.org/advanced-topics/near.html. |
| `NEAR4` | RTCM3 MSM4 (compact: no carrier-phase/Doppler sub-mm fractions) | For lower-bandwidth links and older receivers (e.g. John Deere RTK guidance). Resolution still below F9P measurement noise. |

NEAR/NEAR4 are aliases — they do **not** add station count.

### Network reach (territory codes)

Centipede assigns a 3-letter territory code in sourcetable field 9. Codes observed 2026-05-19 (42 distinct): ALA, AUS, AUT, BEL, BGD, BGR, CAN, CHZ, CZE, DAN, DEU, DNK, ENG, ESP, FIN, FRA, GRC, HUN, IRL, ISR, ITA, LTU, LVA, MDG, MTQ, NCL, NLD, NOR, PYF, REU, ROM, ROU, SAU, SEN, SER, SJM, SVK, SVN, SRB, SWE, USA, ZAF.

**Non-ISO codes that mean something else** (`CHZ`=Switzerland not Czech; `ENG`=whole UK not just England; `DAN`/`DNK`, `ROM`/`ROU`, `SER`/`SRB` used in parallel for the same country): see `_centipede_country_codes.md` for the authoritative legend and per-country counts.

Top territories by node count (2026-05-19 fetch): France 709 (FRA), Hungary 217 (HUN), United Kingdom ~45 (ENG), Switzerland 30 (CHZ), Netherlands 26 (NLD), Norway 21 (NOR; Svalbard separately as SJM), Canada 19 (CAN), Finland mainland 18 (FIN; Åland separately as ALA), Denmark ~18 (DAN 10 + DNK 8), Belgium 17 (BEL), Serbia ~14 (SER 11 + SRB 3), Romania 9 (ROM 7 + ROU 2), Czech Republic 3 (CZE).

---

## Governance and license

### Association

| Field | Value |
|---|---|
| **Legal form** | Association loi du 1er juillet 1901 (French non-profit) |
| **Name** | Centipede-RTK (CRTK) |
| **SIREN** | 932 561 517 |
| **Registered** | 2024-08-28 (Annuaire des Entreprises) |
| **Headquarters** | 1 Rue du Papineau, 17220 Saint-Médard-d'Aunis, France |
| **Status** | Active; classified under Économie Sociale et Solidaire (ESS); no salaried staff. |
| **Founding board** | President Stéphane Péneau; Secretary/VP Philippe Bourcier; Treasurer/VP Raphaël Boukris. Two-year mandates, unlimited reelection. |
| **Historical origin** | Network started 2019 by INRAE researchers (Charente-Maritime farm); pre-association funded/hosted under INRAE CATI GEDEOP. |
| **Membership / donations** | Via HelloAsso: https://www.helloasso.com/associations/centipede-rtk. |

### Data license

Stream contents licensed under **Open Data Commons Database Contents License (DbCL) 1.0**. Source: https://www.centipede-rtk.org/terms-conditions.

Key license terms:
- Commercial use of the corrections permitted with attribution.
- "*Resale, redistribution, leasing, or offering the data for commercial purposes with the intention of competing*" without written authorisation is prohibited (anti-rebroadcast clause).
- Liability indemnification capped at **€1/calendar year**.
- Use prohibited for "*harmful, dangerous, or illegal activities, including but not limited to offensive military operations*".
- Rover GGA positions stored pseudonymised for ≤6 months (GDPR retention cap).

No residency requirement. No professional certification required.

---

## Reference frame policy

Centipede has **no per-station epoch declaration**; the frame is set by each base operator at install. Operator documentation only commits citably for metropolitan France:

> "RGF93 constitutes the legal geographic reference … three-dimensional and geocentric … linked to the global ITRS reference system … coincides with the global ITRS system at epoch 1989.0." — https://docs.centipede-rtk.org/coordinate-systems.html

For French bases the documented recipe is: ≥24 h RINEX → IGN online positioning → coordinates in RGF93 v2b (= ETRF2000 ep 2019.0 per IGN) → fixed in RTKBase. This recipe is **not enforced centrally**: a base operator could install with autonomous TMODE3 SVIN coordinates and be accepted into the caster anyway. Primer `[centipede-FR]` treats France as the strict case.

For non-French stations the operator docs offer only recipe-level guidance (EU bases → ETRF2000 via local IGS services; rest-of-world → ITRF current via NRCAN/IGN online services). There is no central enforcement and no per-country override of station coordinates. Country files should not cite ETRF2000/ITRF as Centipede's declared frame outside France — primer `[centipede-intl]` is the correct reference.

RTCM 3.1 datum-transformation messages 1021–1027 are not transmitted by Centipede streams (RTKBase/F9P does not generate them).

---

## Institutional stream integrations

Per https://docs.centipede-rtk.org/advanced-topics/institutional-streams.html:

| Integration | Stations | Status |
|---|---|---|
| **RÉNAG** (Réseau National GNSS permanent, scientific) | 35 stations in France | Live since June 2023; RÉNAG also archives Centipede French base RINEX (1 s + 30 s) for post-processing. |
| **IGS / EUREF-IP** | (unspecified subset) | "Ongoing integration" status (no live count published as of 2026-05-21). |

Centipede does *not* relay/peer commercial casters (Orphéon, Teria, SmartNet, etc.) and per terms cannot redistribute private streams.

---

## Post-processing (RINEX) fallback

Per https://docs.centipede-rtk.org/rinex.html:

| Service | Coverage | Sampling | License |
|---|---|---|---|
| `centipede_30s` | Declared bases in metropolitan France | 30 s | CC-BY 4.0 |
| `centipede_1s` | Declared bases in metropolitan France | 1 s | CC-BY 4.0 |

Format RINEX 3 Hatanaka-compressed (`.crx.gz`). RINEX archive is currently France-only and is delivered via the RÉNAG database integration. Operators with RTKBase access can generate/download from the RTKBase "File Service" tab.

---

## Global infrastructure

Per https://www.centipede-rtk.org/ (operator homepage) and https://www.inrae.fr/en/news/democratising-precision-guided-agriculture-ever-expanding-centipede-rtk-network:

- "*First RTK network to deploy a global server presence on all continents*" via IP-anycast (Millipede caster's anycast-ready design).
- Anycast partnership: **PCH (Packet Clearing House)**, the intergovernmental treaty organisation running the world's largest anycast DNS infrastructure. Partnership formalised after association formed (Aug 2024).
- INRAE press release (undated, 2024–2025): 625 bases in mainland France, 860 bases across 30 countries worldwide. (Local sourcetable 2026-05-19 = 1,213 STR — number has grown since the press release was written.)

---

## Cross-reference table (country file pointers)

Country files that depend on Centipede counts should pin to `_centipede_country_codes.md` for the legend and reference this file for caster details. Files known to depend (audited via `_centipede_country_codes.md` 2026-05-13):

- `FR_France.md` — primary host network (709 FRA nodes); largest single deployment.
- `HU_Hungary.md` — 217 HUN nodes; effective national free RTK alongside paid GNSSnet.hu.
- `GB_Great-Britain.md` — 45 ENG nodes (entire UK including Scotland/Wales/NI under `ENG`).
- `CH_Switzerland.md` — 30 CHZ nodes (non-ISO; not Czech).
- `NL_Netherlands.md` — 26 NLD nodes; supplement to AGRS.
- `NO_Norway.md` — 21 NOR nodes; supplement to CPOS.
- `CA_Canada.md` — 19 CAN nodes.
- `FI_Finland.md` — 18 FIN nodes (mainland; Åland separately under ALA, 2 nodes).
- `DK_Denmark.md` — 18 nodes split DAN 10 + DNK 8 (sum both).
- `BE_Belgium.md` — 17 BEL nodes.
- `RS_Serbia.md` — 14 nodes split SER 11 + SRB 3 (sum both).
- `RO_Romania.md` — 9 nodes split ROM 7 + ROU 2 (sum both).
- `IE_Ireland.md` — 8 IRL nodes.
- `CZ_CzechRepublic.md` — 3 CZE nodes (CZE ≠ CHZ).
- `AX_AlandIslands.md`, `SJ_Svalbard.md`, `IS_Iceland.md` — small island/territory subsets.
- `IL_Israel.md`, `ZA_SouthAfrica.md`, `SN_Senegal.md`, `MG_Madagascar.md`, `BD_Bangladesh.md`, `SA_SaudiArabia.md`, `NC_NewCaledonia.md`, `PF_FrenchPolynesia.md`, `RE_Reunion.md`, `MQ_Martinique.md`, `US_USA.md` — small per-country footprints (1–5 nodes each, see `_centipede_country_codes.md`).

---

## Sources Consulted

- Operator homepage: https://www.centipede-rtk.org/
- Network overview / connection how-to: https://www.centipede-rtk.org/the-centipede-rtk-network
- Technical access reference: https://docs.centipede-rtk.org/access.html
- Coordinate systems doc (RGF93 / France frame statement): https://docs.centipede-rtk.org/coordinate-systems.html
- NEAR / NEAR4 mountpoint reference: https://docs.centipede-rtk.org/advanced-topics/near.html
- Institutional stream integrations (RÉNAG, IGS/EUREF-IP): https://docs.centipede-rtk.org/advanced-topics/institutional-streams.html
- RINEX archive (France only, CC-BY 4.0): https://docs.centipede-rtk.org/rinex.html
- Terms (DbCL 1.0, liability cap, anti-rebroadcast, GDPR retention): https://www.centipede-rtk.org/terms-conditions
- Statutes of the association (1901 law, board): https://www.centipede-rtk.org/statutes-of-the-association
- Host-base volunteer guide: https://www.centipede-rtk.org/host-rtk-base
- Projects (Millipede / RTKBase / DIY rover): https://www.centipede-rtk.org/projects
- Connection limit "1 matériel/ntrip client par IP": https://docs.centipede.fr/docs/centipede/3_connect_caster.html
- French business registry: https://annuaire-entreprises.data.gouv.fr/entreprise/centipede-rtk-932561517 (SIREN 932561517, registered 2024-08-28)
- INRAE press release (network scale 625 FR / 860 worldwide / 30 countries; PCH partnership): https://www.inrae.fr/en/news/democratising-precision-guided-agriculture-ever-expanding-centipede-rtk-network
- Millipede caster repo (BSD-3, Pierre Beyssac): https://github.com/pbeyssac/millipede-caster
- Centipede-RTK GitHub org (RTKBase fork, RtkBaseVar): https://github.com/centipedeRTK
- FOSDEM 2026 talk (Millipede architecture): https://fosdem.org/2026/schedule/event/X7FTTA-millipede_and_centipede-rtk_centimeter-level_gnss_positioning_for_the_rest_of_us/
- PCH anycast service: https://www.pch.net/services/anycast
- Country code legend (this repo): `_centipede_country_codes.md`
