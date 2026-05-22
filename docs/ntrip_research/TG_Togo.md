# Togo [TG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21

## Status

National CORS network deployed under the geodetic reform; **IGNT** (Institut Géographique National du Togo) created by decree 2026-02-19 as an autonomous body, taking over from the former DGIGC. A March 2026 inter-ministerial communiqué makes the new reference system mandatory for all professional topographic / cadastral / urbanism / infrastructure work; professional users were given a 3-month transition window (deadline ~2026-06-09). No public NTRIP host:port has been disclosed; access via direct operator contact. No volunteer / community NTRIP coverage in country.

## Network — IGNT National CORS

| Field | Value |
|---|---|
| **landing_url** | https://urbanisme.gouv.tg/ (Ministère de l'Aménagement du Territoire, de l'Urbanisme et de l'Habitat — tutelle ministry; ministry homepage carries no NTRIP / IGNT portal pointer as of 2026-05-21) |
| **access_url** | not published — credentials issued by IGNT on request via the ministry contact |
| **host:port** | not publicly listed; no `igntogo.tg` / `ignt.tg` portal resolves as of 2026-05-21 |
| **num_stations** | **CORS count not disclosed** in any public communiqué. The 614 figure that appears in 2025 government reporting refers to *passive* geodetic benchmarks (markers/monuments) — 11 first-order + 2nd- and 3rd-order points — not real-time CORS antennas. The CORS layer is mandated in the 2026-03-09 communiqué as the real-time backbone alongside the levelling network, but the active-station count is not published. |
| **vrs** | ? — not specified in public communiqués |
| **tariff** | not published; March 2026 communiqué frames the network as public-service geodetic infrastructure but is silent on fees |
| **hobbyist_eligibility** | ? — compliance mandate addresses professional topographers / cadastral surveyors / urbanists, nothing on hobbyist access |
| **legal_residency_required** | ? — no published rule |
| **last_confirmed_alive** | 2026-05-21 — `urbanisme.gouv.tg` HTTP 200; April 2025 + March 2026 communiqués remain the only authoritative public references; no public caster endpoint to probe |
| **datum_epoch** | omitted — March 2026 communiqué mandates a new "système de référence national" without naming a datum/epoch. Secondary reporting (GIS Resources, Mar 2026) places Togo's reform inside the ITRF/AFREF West African modernisation pattern but does not state which realization or epoch IGNT actually adopted. Per primer rule, only operator declarations are citable — none located. |

## Project & Operator Timeline

- **Late 2010s** — DGIGC (Direction Générale de l'Information Géographique et de la Cartographie) begins continuous-operation GNSS pilots within the national geodetic reform.
- **2025-04-09** — DGIGC validates geodetic observations of reference points in the Central and Kara regions in a Lomé workshop. Network reaches 614 reference points nationally (1st / 2nd / 3rd order); 11 first-order points serve as national base reference.
- **2026-02-19** — Council of Ministers adopts the decree creating **IGNT** (Institut Géographique National du Togo) as an autonomous body with administrative and financial independence, taking over DGIGC's mission and strengthening the production and reliability of national geographic data.
- **2026-03-09** — Joint inter-ministerial communiqué from the Minister of Finance and Budget (Essowè Georges Barcola) and the Minister of Territorial Planning (Sévon-Tépé Kodjo Adedze) makes the new national geodetic reference system **mandatory** for all spatial data in cartography, land management, urban planning, topography and infrastructure. The CORS network is named as the real-time backbone alongside the levelling benchmarks. Professional users were granted a 3-month transitional window (deadline ~2026-06-09).
- **2026-05-21** — Ministry homepage `urbanisme.gouv.tg` still carries no IGNT / CORS / NTRIP pointer; the 3-month professional compliance window is still in effect with no public endpoint disclosure.

## Context

- **Scope**: nationwide CORS for real-time corrections + 614 levelling and reference benchmarks for the passive frame + mandatory transition for professional users. Use cases cited: cartography, land management, urban planning (Grand Lomé project), cadastre, precision agriculture, disaster risk reduction.
- **Naming**: the post-2026 institute is **IGNT** (per Togo First, 2026-02-20). Earlier 2025 communications and some third-party write-ups use "IGNTOGO" informally; the legal entity created by decree is IGNT.
- **Public web presence is sparse**: no `ignt.tg` / `igntogo.tg` portal reachable 2026-05-21. Authoritative sources remain `urbanisme.gouv.tg` and the official `republiquetogolaise.com` newsroom.
- **Regional context**: Neighbouring Bénin operates a 7-station national CORS (RTK-capable since 2022); Ghana operates a partial national CORS. The Togo reform aligns with this West African modernisation trend.

## Probes (2026-05-22)

| Endpoint | Result |
|---|---|
| `https://urbanisme.gouv.tg/` | HTTP 200 — ministry homepage live; no IGNT / CORS / NTRIP portal pointer |
| `http://ignt.tg/` | DNS fails — no A record (`Could not resolve host: ignt.tg`) |
| `http://igntogo.tg/` | DNS fails — no A record (`Could not resolve host: igntogo.tg`) |
| `caster.centipede.fr:2101` | 0 TGO mountpoints |
| `rtk2go.com:2101` | 0 TGO mountpoints |

## Volunteer / Free Coverage

None inside Togo. 0 TG-coded rtk2go or Centipede bases (verified 2026-05-21 via local `data/stations.json` and rtk2go sourcetable probe). Nearest community base is `fssoyo` in Nigeria (Oyo, 7.84 N 3.95 E) at ~333 km from central Togo, beyond useful single-base RTK range. No GEODNET, ONOCOY, HxGN SmartNet, TopNET Live, or PointOne coverage confirmed.

## Practical Workaround Until IGNT Publishes a Public Endpoint

1. Email the ministry (`urbanisme.gouv.tg`) requesting CORS credentials.
2. Deploy a local base station (u-blox F9P / Septentrio Mosaic) for single-base RTK.
3. PPP: Galileo HAS open service (~25–40 cm horizontal, free) or Trimble RTX (paid, sub-decimetre).

## Post-Processing (RINEX) Fallback

No publicly accessible Togolese CORS RINEX archive found. IGNT is likely to provide one (typical national-CORS practice in the region), but no portal is online. AFREF / IGS coverage in the immediate region is sparse.

## Sources

- **2026-03-09 reform** (joint Barcola / Adedze inter-ministerial communiqué):
  - Republique Togolaise: https://www.republiquetogolaise.com/gestion-publique/0903-11681-cartographie-et-urbanisme-de-nouvelles-normes-geospatiales-instaurees
  - Togo First: https://www.togofirst.com/fr/gestion-publique/1003-18420-togo-de-nouvelles-normes-geospatiales-pour-la-cartographie-et-l-urbanisme
  - Le Nouveau Reporter: https://lenouveaureporter.com/modernisation-fonciere-les-travaux-topographiques-desormais-soumis-au-reseau-geodesique-national/
  - Ecofin Agency: https://www.ecofinagency.com/news/1003-53628-togo-standardises-geographic-reference-systems-to-improve-land-and-urban-planning
  - GIS Resources: https://gisresources.com/togo-launches-national-cors-network-and-geodetic-reference-system-to-standardise-spatial-data/
  - Africa Top Success — 3-month compliance window: https://www.africatopsuccess.com/topographes-au-togo-3-mois-pour-se-conformer/
- **2026-02-19 IGNT creation decree** (Council of Ministers):
  - Republique Togolaise: https://www.republiquetogolaise.com/gestion-publique/2002-11624-le-togo-se-dote-dun-institut-geographique
  - Togo First: https://www.togofirst.com/fr/gouvernance-economique/2002-18277-togo-creation-d-un-institut-geographique-national-pour-fiabiliser-les-donnees-territoriales
- **2025-04-09 DGIGC 614-benchmark validation**:
  - Ministère de l'Aménagement: https://urbanisme.gouv.tg/togo-densification-des-bornes-geodesiques-dans-les-regions-centrale-et-de-la-kara-le-rapport-des-travaux-valide/
  - Le Chiquier: https://www.lechiquier.info/togo-comprendre-le-fonctionnement-du-reseau-geodesique-national
- DGIGC differential-GPS equipment / training (background): https://urbanisme.gouv.tg/la-direction-generale-de-linformation-et-de-la-cartographie-receptionne-du-nouveau-materiel-gps-differentiel-et-forme-son-personnel-sur-la-densification-du-reseau-geodesique/
- Local: `py scripts/stations_by_country.py TGO` → no stations; `py scripts/stations_by_radius.py 8.5 1.0 500` → nearest is `fssoyo` (NGA) ~333 km away
