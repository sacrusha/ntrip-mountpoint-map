# DR Congo [CD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (re-verified — no operational change)

## Status: NO — no public NTRIP RTK caster operating; no national CORS network identified

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **landing_url** | null — no operator portal exists |
| **access_url** | null — no service exists |
| **host:port** | null |
| **tariff** | null — no service exists |
| **num_stations** | 0 |
| **vrs** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster endpoint identified |
| **datum_epoch** | OMIT — no national active geodetic datum published |

## Most Recent Project / Announcement

No public announcement of a planned national NTRIP caster or operational CORS network for DR Congo found as of 2026-05-22. The Institut Géographique du Congo (IGC, `igc-rdc.org` — statutory national mapping and geodesy agency, est. 1949, Kinshasa) lists no real-time GNSS correction service on either public site (`igc-rdc.org`, `igcongo.cd`).

**IGC / IGN FI framework**: A collaboration convention was signed on **10 March 2016** in Kinshasa between IGC (DG Albert Mbuyu Numbi) and IGN FI (DG Christophe Dekeyne), covering capacity-building for densification of the national geodetic network, cartographic update, and a national training/research policy for geomatics. **No CORS, NTRIP caster, or operational geodetic station has been confirmed as a deliverable in the 10 years since.** The AFREF "fully-fledged CORS map for Africa" effort (GIM International) and AFREF 2024 workshop materials (RCMRD, Nairobi) continue to list DR Congo among countries that still need a CORS system.

## Probe Outcomes (2026-05-22)

- `https://igc-rdc.org/` — reachable but page body returns empty in sandbox WebFetch (rendered via JS); site exists and IGC institutional info confirmed via WebSearch. No GNSS/NTRIP/CORS/RTK content surfaces in any search snippet.
- rtk2go sourcetable — 0 `COD` mountpoints (live probe 2026-05-22).
- Centipede-RTK sourcetable — 0 `COD` mountpoints (live probe 2026-05-22). `CODAR` matches "CODAR" in Guemps, FRA — false positive.
- IGS Network — 0 `COD` station entries.
- `py scripts/stations_by_country.py COD` → empty; `py scripts/stations_by_radius.py -4.32 15.31 600` → empty.
- GIM International "Fully Fledged CORS Map for Africa" (re-checked 2026-05-22) — DR Congo absent from the 25 mapped-CORS countries.

## Context Notes

- **IGC status**: The IGC website lists "actualités" and "projets" sections but, as of 2026-05-22, contains no public reference to CORS infrastructure, NTRIP streaming, or a real-time correction service. Wikipedia describes IGC as having 12 provincial stations / 11 sub-stations of the **agency** (administrative offices), not GNSS reference stations — terminology that should not be conflated with CORS.
- **IGC / IGN FI 2016 framework**: signed 10 March 2016 (ERAIFT cérémonie de signature, Salle bleue du Gouvernement, Kinshasa). Densification of national geodetic network is named scope; no CORS / NTRIP deliverable confirmed in any subsequent public reporting (IGC site, IGN FI portfolio, francophone surveying press).
- **AFREF participation**: DR Congo is nominally a participant in AFREF (African Reference Frame), but no DRC station appears in the current IGS network or AFREF Operational Data Centre feed. Published AFREF status snapshots (RCMRD 2024, GIM International CORS-Africa overview) consistently exclude DRC from the ~22 African countries with confirmed operational CORS installations.
- **Legacy geodetic work**: A network of geodetic survey points was installed in the southern third of DRC circa 2005 to strengthen the colonial-era triangulation framework; these are passive monuments, not continuously operating GNSS stations.
- **Commercial deployments**: International mining and surveying contractors operating in DRC (cobalt/copper belt around Lubumbashi, Kolwezi) typically deploy private base stations rather than relying on a national caster; none are exposed via a public NTRIP endpoint.
- **rtk2go / Centipede / GEODNET**: Zero CD/COD mountpoints on rtk2go or Centipede (confirmed by direct sourcetable fetch 2026-05-22). GEODNET's public coverage map shows no miners in DRC; the Q3 2025 GEODNET state report concentrates growth in US/EU/South America/India and does not list DRC.
- **Infrastructure barriers**: Outside Kinshasa and a handful of provincial capitals, grid power and IP backhaul are unreliable — structural prerequisites for continuous GNSS streaming are largely absent, and this is the recurring rationale cited by AFREF/RCMRD for the persistent CORS gap.

## Nearest Cross-border Free RTK (within ~50 km of a DRC border)

- **EarthScope NOTA — western Rwanda / Lake Kivu shore** (within ~50 km of the Goma / Bukavu / Rubavu border): `KMBR_RTCM3P3` (-1.83, 29.29), `NYBA_RTCM3P3` (-1.76, 29.35), `RUBO_RTCM3P3` (-1.73, 29.26) on `ntrip.earthscope.org:2101`. Free under EarthScope NULA (non-commercial), no residency requirement, account registration required. Useful for short-baseline RTK or post-processing in the Kivu corridor on the DRC side; documented in `docs/rtk_inventory.md` under `rgn_rw`.
- **UGRF (Uganda) — Kabale / Rukungiri** (within ~40–60 km of the DRC-Uganda border in the Kivu corridor): `Kabale` (-1.27, 29.98) and `Rukungiri` (-0.78, 29.93) are exposed as single-base mountpoints on `ugrf.mlhud.go.ug:2101`. Verified via `stations_by_radius.py -1.83 29.29 200`. UGRF is a free national caster operated by MLHUD; hobbyist registration is open via Spider Business Centre (`https://ugrf.mlhud.go.ug/SBC`) — no professional licence or residency restriction documented (full network detail in `docs/ntrip_research/UG_Uganda.md`). These two stations extend short-baseline RTK options on the eastern DRC side north of the EarthScope NOTA Kivu trio.
- No comparable free cross-border casters identified near the western (Angola, Republic of Congo), northern (CAR, South Sudan), or southern (Zambia, northern Tanzania) borders within ~50 km as of 2026-05-22.

## Post-Processing (RINEX) Fallback

No national RINEX archive identified. The IGS public archive contains no DR Congo stations with regular data contributions.

- **EarthScope NOTA daily RINEX** for the three Kivu-shore Rwanda stations above — the only free PPK source within ~50 km of DRC territory.
- **UGRF RINEX (Uganda)** is downloadable from the SBC portal (free, account required) for the two stations listed above and the wider UGRF network — useful for static post-processing in eastern DRC.
- **IGS NKLG (Libreville, Gabon)** at (0.354, 9.672) — for western DRC users (Kinshasa, Matadi, Bandundu) NKLG is the nearest IGS reference, Kinshasa → NKLG ~814 km (haversine). Useless for RTK but viable as a long-baseline PPP / very-long-static anchor; RINEX hosted by CDDIS / IGN data centres, also rebroadcast live on AUSCORS / IGS-IP / MIRAI.

## Sources Consulted (2026-05-22)
- IGC official site: https://igc-rdc.org/ (no NTRIP/CORS content)
- IGC alternate site: https://www.igcongo.cd/
- DécryptaGéo — IGC / IGN FI 2016 accord: https://decryptageo.fr/linstitut-geographique-du-congo-fait-appel-a-lexpertise-dign-fi-pour-developper-lutilisation-de-linformation-geographique-en-rdc/
- ERAIFT signing ceremony (10 March 2016): https://www.eraift-rdc.org/index.php/activites/evenements/158-participation-de-l-eraift-a-la-ceremonie-de-signature-de-l-accord-de-collaboration-entre-l-igc-et-l-ign-fi
- GIM International — IGC profile: https://www.gim-international.com/content/company/institut-geographique-du-congo-2
- GIM International — "Developing a Fully Fledged CORS Map for Africa" (re-checked 2026-05-22): https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- AFREF background: https://geodesy.science/glossary/afref-african-reference-frame/
- IGS Network: https://network.igs.org/ (no COD entries, 2026-05-22)
- Live probes (2026-05-22): rtk2go, Centipede-RTK (0 COD mountpoints)
- Local pipeline: `scripts/stations_by_country.py COD`, `scripts/stations_by_radius.py -4.32 15.31 600` — empty
