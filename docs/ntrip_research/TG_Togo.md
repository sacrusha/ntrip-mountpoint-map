# Togo [TG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (revised from 2026-05-06 — operator identified as IGNTOGO / DGIGC; CORS deployment confirmed as part of multi-year reform validated April 2025 and mandated for all professional work from March 2026; NTRIP endpoint still not publicly discoverable)

## Status: CORS network deployed under the IGNTOGO / DGIGC national geodetic reform; mandatory reference for all professional topographic / cadastral / urbanism / infrastructure work as of 2026-03-09 (3-month compliance window); NTRIP host:port not publicly listed — credentials issued by the operator on request

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (operationally), but **no public host:port has been disclosed** — access via the operator |
| **Operator** | **IGNTOGO** — Institut National de l'Information Géographique du Togo (rebrand, ~February 2026, of the **Direction Générale de l'Information Géographique et de la Cartographie / DGIGC**), under the Ministère de l'Aménagement du Territoire, de l'Urbanisme et de l'Habitat — `urbanisme.gouv.tg` |
| **host:port** | Not publicly listed. `igntogo.tg` was not resolving as of late April 2026 / 2026-05-13; access via `urbanisme.gouv.tg` contact or via direct DGIGC liaison |
| **stream type** | Network of CORS broadcasting RTCM 3 corrections; whether VRS / iMAX / single-base only is not specified in the public communiqués |
| **num_stations** | Not publicly stated. The reform also covers **614 passive geodetic benchmarks** (11 first-order, plus 2nd- and 3rd-order points) distributed nationally — these are pillars, not CORS, but they form the geodetic frame the CORS feed |
| **tariff** | Not published. The March 2026 communiqué frames the network as part of public-service geodetic infrastructure; whether access will be free or fee-based has not been announced |
| **hobbyist_eligibility** | Unclear — no published tier. The compliance mandate addresses professional topographers / cadastral surveyors / urbanists and gives them three months to align equipment to the new reference; nothing on hobbyist access |
| **legal_residency_required** | Unclear — no published rule |
| **last_confirmed_alive** | 2026-05-13 — `urbanisme.gouv.tg` HTTP 200, April 2025 DGIGC workshop report and the March 2026 inter-ministerial communiqué both reachable; `igntogo.tg` not yet a live portal as of 2026-05-13 |

## Project & Operator Timeline

- **Late 2010s** — DGIGC begins continuous-operation GNSS pilots within the national geodetic reform.
- **2025-04-09** — DGIGC validates geodetic observations of reference points in the Central and Kara regions in a Lomé workshop. Network reaches 614 reference points across the country (1st / 2nd / 3rd order). 11 first-order points serve as the national base reference. (Source: `urbanisme.gouv.tg/togo-densification-des-bornes-geodesiques…/`, `lechiquier.info`.)
- **2025–2026** — DGIGC rebranded to **IGNTOGO** (Institut National de l'Information Géographique du Togo) under the territorial-planning ministry.
- **2026-03-09** — Joint inter-ministerial communiqué from the Minister of Finance and Budget (Georges Barcola) and the Minister of Territorial Planning and Development (Kodjo Adedze) makes the new national geodetic reference system **mandatory** for all spatial data in cartography, land management, urban planning, topography, and infrastructure. The communiqué names the CORS network as the real-time backbone alongside the levelling benchmarks. Professional users were granted a **three-month transitional window** (i.e. until ~2026-06-09) to align their equipment and workflows.
- **2026-05-13** — IGNTOGO public NTRIP portal still not surfacing on the open web (`igntogo.tg` not resolving). Access remains via IGNTOGO / `urbanisme.gouv.tg`.

## Most Recent Project Announcements

- **2026-03-09** — Joint Barcola / Adedze inter-ministerial communiqué standardising the national geodetic reference system and mandating CORS-based positioning for all official spatial-data work.
  - Site officiel du Togo: https://www.republiquetogolaise.com/gestion-publique/0903-11681-cartographie-et-urbanisme-de-nouvelles-normes-geospatiales-instaurees
  - Le Nouveau Reporter: https://lenouveaureporter.com/modernisation-fonciere-les-travaux-topographiques-desormais-soumis-au-reseau-geodesique-national/
  - GIS Resources (English): https://gisresources.com/togo-launches-national-cors-network-and-geodetic-reference-system-to-standardise-spatial-data/
- **2025-04-09** — DGIGC densification of Central / Kara region geodetic benchmarks validated, 614 reference points in operation.
  - Ministère de l'Aménagement: https://urbanisme.gouv.tg/togo-densification-des-bornes-geodesiques-dans-les-regions-centrale-et-de-la-kara-le-rapport-des-travaux-valide/
  - Le Chiquier: https://www.lechiquier.info/togo-comprendre-le-fonctionnement-du-reseau-geodesique-national

## Context Notes

- **Scope of the reform**: nationwide CORS for real-time corrections + 614 levelling and reference benchmarks for the passive frame + mandatory transition for professional users. Use cases cited by the ministers: cartography, land management, urban planning (Grand Lomé project), cadastre, precision agriculture, disaster risk reduction.
- **Public web presence is sparse**: The IGNTOGO portal at `igntogo.tg` was not reachable on 2026-05-13. The most authoritative web sources remain `urbanisme.gouv.tg` and the official `republiquetogolaise.com` government newsroom.
- **Regional context**: Neighbouring Benin operates a 7-station national CORS network (RTK-capable since 2022); Ghana operates a national CORS. The Togolese reform aligns with this West African modernisation trend.
- **No volunteer / community option inside Togo**: zero TG-coded rtk2go or Centipede bases (re-cross-checked 2026-05-13 via `py scripts/stations_by_radius.py 8.5 1.0 500` — nearest community base is `fssoyo` in Nigeria at ~333 km, beyond single-base RTK range).
- **Global commercial networks**: No Togo coverage confirmed for GEODNET, ONOCOY, HxGN SmartNet, TopNET Live, or PointOne.
- **Practical workaround for hobbyists, until IGNTOGO publishes a public NTRIP endpoint**:
  1. Email `urbanisme.gouv.tg` requesting CORS credentials (point of contact: the Direction Générale within the ministry).
  2. Deploy a local base station (u-blox F9P / Septentrio Mosaic) for single-base RTK.
  3. PPP: Galileo HAS (free, ~25–40 cm horizontal), Trimble RTX (paid, sub-decimetre).

## Post-Processing (RINEX) Fallback

No publicly accessible Togolese CORS RINEX archive found. The IGNTOGO network is likely to provide one (typical national-CORS practice in the region), but no portal is online. AFREF / IGS coverage in the immediate region is sparse.

## Sources Consulted
- IGN Togo / DGIGC reform (March 2026 inter-ministerial communiqué):
  - Republique Togolaise: https://www.republiquetogolaise.com/gestion-publique/0903-11681-cartographie-et-urbanisme-de-nouvelles-normes-geospatiales-instaurees
  - Le Nouveau Reporter: https://lenouveaureporter.com/modernisation-fonciere-les-travaux-topographiques-desormais-soumis-au-reseau-geodesique-national/
  - Ecofin Agency: https://www.ecofinagency.com/news/1003-53628-togo-standardises-geographic-reference-systems-to-improve-land-and-urban-planning
  - GIS Resources: https://gisresources.com/togo-launches-national-cors-network-and-geodetic-reference-system-to-standardise-spatial-data/
- DGIGC April 2025 workshop / 614-benchmark validation:
  - Ministère de l'Aménagement: https://urbanisme.gouv.tg/togo-densification-des-bornes-geodesiques-dans-les-regions-centrale-et-de-la-kara-le-rapport-des-travaux-valide/
  - Le Chiquier: https://www.lechiquier.info/togo-comprendre-le-fonctionnement-du-reseau-geodesique-national
- Grand Lomé urban GIS database announcement: https://www.republiquetogolaise.com/gestion-publique/0108-10937-amenagement-urbain-le-grand-lome-se-dote-d-une-base-de-donnees-geospatiales
- Africa Top Success — 3-month compliance window: https://www.africatopsuccess.com/topographes-au-togo-3-mois-pour-se-conformer/
- DGIGC new differential-GPS equipment / training (background): https://urbanisme.gouv.tg/la-direction-generale-de-linformation-et-de-la-cartographie-receptionne-du-nouveau-materiel-gps-differentiel-et-forme-son-personnel-sur-la-densification-du-reseau-geodesique/
- RTK2GO / Centipede — no TG entries (re-cross-checked 2026-05-13)
- NTRIP-list.com Africa page — no Togo entries
- ArduSimple country selector — Togo not listed as having a published national caster
- AFREF literature — no operational Togo CORS station recorded
- GEODNET, ONOCOY — no Togo coverage confirmed
