# DR Congo [CD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (revising 2026-05-12 entry)

## Status: NO — no public NTRIP RTK caster operating; no national CORS network identified

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster endpoint identified |

## Most Recent Project / Announcement

No public announcement of a planned national NTRIP caster or operational CORS network for DR Congo found as of 2026-05-15. The Institut Géographique du Congo (IGC, `igc-rdc.org` — the statutory national mapping and geodesy agency, established 1949, headquartered Kinshasa, Boulevard du 30 Juin) advertises a mandate for establishing and maintaining geodetic networks, leveling grids, gravimetric canevas, topographic mapping and remote sensing, but no real-time GNSS correction service is described on either of its public sites (`igc-rdc.org` or `igcongo.cd`). The AFREF "fully-fledged CORS map for Africa" effort and the AFREF 2024 workshop materials (RCMRD, Nairobi) explicitly list DR Congo among the countries that "still need to be equipped with a CORS system."

## Probe Outcomes (2026-05-15)

- `http://igc-rdc.org/` and `https://igc-rdc.org/` — HTTP 200; no GNSS/NTRIP/CORS/RTK content on landing, "À propos," or contacts pages.
- `http://rtk2go.com:2101/SNIP::STATUS` — zero mountpoints with country `COD` or city tokens (Kinshasa, Lubumbashi, Goma, Bukavu, Kisangani, Matadi).
- `http://caster.centipede.fr:2101/` sourcetable — zero `COD` country entries. (`CODAR` matches the mountpoint name "CODAR" in Guemps, FRA, lat 50.94 — not DR Congo.)
- IGS Network CSV (`files.igs.org/pub/station/general/IGSNetwork.csv`) — zero `COD` / "Congo" / "Kinshasa" station entries.
- `py scripts/stations_by_country.py COD` → `No stations for 'COD'`.
- `py scripts/stations_by_radius.py -4.32 15.31 300` (Kinshasa, 300 km) → `No stations within 300 km`.

## Context Notes

- **IGC status**: The IGC website lists "actualités" and "projets" sections but, as of 2026-05-15, contains no public reference to CORS infrastructure, NTRIP streaming, or a real-time correction service.
- **AFREF participation**: DR Congo is nominally a participant in AFREF (African Reference Frame), but no DRC station appears in the current IGS network or AFREF Operational Data Centre feed. Published AFREF status snapshots (RCMRD 2024, GIM International CORS-Africa overview) consistently exclude DRC from the ~22 African countries with confirmed operational CORS installations.
- **Legacy geodetic work**: A network of geodetic survey points was installed in the southern third of DRC circa 2005 to strengthen the colonial-era triangulation framework; these are passive monuments, not continuously operating GNSS stations.
- **Commercial deployments**: International mining and surveying contractors operating in DRC (cobalt/copper belt around Lubumbashi, Kolwezi) typically deploy private base stations rather than relying on a national caster; none are exposed via a public NTRIP endpoint.
- **rtk2go / Centipede / GEODNET**: Zero CD/COD mountpoints on rtk2go or Centipede (confirmed by direct sourcetable fetch 2026-05-15). GEODNET's public coverage map shows no miners in DRC; the Q3 2025 GEODNET state report concentrates growth in US/EU/South America/India and does not list DRC.
- **Infrastructure barriers**: Outside Kinshasa and a handful of provincial capitals, grid power and IP backhaul are unreliable — structural prerequisites for continuous GNSS streaming are largely absent, and this is the recurring rationale cited by AFREF/RCMRD for the persistent CORS gap.

## Nearest Cross-border Free RTK (within ~50 km of a DRC border)

- **EarthScope NOTA — western Rwanda / Lake Kivu shore** (within ~50 km of the Goma / Bukavu / Rubavu border): `KMBR_RTCM3P3` (-1.83, 29.29), `NYBA_RTCM3P3` (-1.76, 29.35), `RUBO_RTCM3P3` (-1.73, 29.26) on `ntrip.earthscope.org:2101`. Free under EarthScope NULA (non-commercial), no residency requirement, account registration required. Useful for short-baseline RTK or post-processing in the Kivu corridor on the DRC side; documented in `docs/networks.md` under `rgn_rw`.
- No comparable free cross-border casters identified near the western (Angola, Republic of Congo), northern (CAR, South Sudan), eastern (Uganda, Tanzania) or southern (Zambia) borders within ~50 km as of 2026-05-15.

## Post-Processing (RINEX) Fallback

No national RINEX archive identified. The IGS public archive contains no DR Congo stations with regular data contributions. EarthScope NOTA daily RINEX is available for the three Kivu-shore stations above and is the only free PPK source within ~50 km of DRC territory.

## Sources Consulted (2026-05-15)
- IGC official website: https://igc-rdc.org/ (HTTP 200, no NTRIP/CORS content)
- IGC about page: https://igc-rdc.org/a-propos/
- IGC alternate site: https://www.igcongo.cd/
- GIM International — IGC profile: https://www.gim-international.com/content/company/institut-geographique-du-congo-2
- GIM International — "Developing a Fully Fledged CORS Map for Africa": https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- AFREF background (IAG geodesy.science): https://geodesy.science/glossary/afref-african-reference-frame/
- AFREF data portal: http://www.afrefdata.org/welcome.php
- AFREF 2024 Workshop / RCMRD: https://ric2024.rcmrd.org/afref
- RCMRD AFREF service page: https://apps.rcmrd.org/web-service/african-geodetic-reference-frame
- IGS Network: https://network.igs.org/ (534 stations as of 2026-05-15; no COD entries)
- IGS Network CSV: https://files.igs.org/pub/station/general/IGSNetwork.csv (no COD entries, 2026-05-15)
- Wikipedia (FR) — Institut géographique du Congo: https://fr.wikipedia.org/wiki/Institut_g%C3%A9ographique_du_Congo
- rtk2go status page: http://rtk2go.com:2101/SNIP::STATUS (0 COD mountpoints, 2026-05-15)
- Centipede sourcetable: http://caster.centipede.fr:2101/ (0 COD mountpoints, 2026-05-15)
- Local pipeline data: `data/stations.json` via `scripts/stations_by_country.py COD` and `scripts/stations_by_radius.py -4.32 15.31 300` — both empty, 2026-05-15
