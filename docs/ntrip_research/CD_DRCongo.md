# DR Congo [CD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revising 2026-05-06 entry)

## Status: NO — no public NTRIP RTK caster operating; no CORS network found

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster endpoint identified |

## Most Recent Project Announcement

No public announcement of a planned national NTRIP caster or CORS network for DR Congo found as of 2026-05-12 (no new findings vs. 2026-05-06 entry). The Institut Géographique du Congo (IGC, `igc-rdc.org`) is the statutory geodesy and mapping agency and has a stated mandate for geodetic network establishment and maintenance, but no real-time GNSS correction service is described on its public website.

## Context Notes

- **IGC mandate and status**: IGC (established 1949, Kinshasa — Boulevard du 30 Juin) is responsible for establishing and maintaining geodetic networks, leveling grids, gravimetric canevas, topographic mapping, and remote sensing. The IGC website (`igc-rdc.org`) lists an "about," "projects," and "news" section but no technical GNSS infrastructure pages have appeared as of 2026-05-12. An alternate IGC site (`igcongo.cd`) similarly contains no CORS or NTRIP content.
- **AFREF participation**: DR Congo has nominal participation in AFREF (African Reference Frame), the IGS-backed pan-African geodetic initiative. However, no DR Congo station appears in the current IGS network or AFREF operational node list. Limited contributions have been documented in literature (geodetic surveys from the colonial-era triangulation network) but no modern CORS data feed has been established. AFREF 2024 Workshop materials (RCMRD, Nairobi, Aug 2024) do not list DR Congo among the ~22 African countries with confirmed operational CORS installations.
- **Infrastructure constraints**: DR Congo faces severe power-grid and internet-connectivity constraints outside Kinshasa and a small number of provincial capitals. Continuous GPS/GNSS streaming requires stable mains or reliable solar power plus sustained IP connectivity — neither is routine at survey-grade infrastructure sites in most of the country. These structural barriers make near-term operational NTRIP streaming very unlikely.
- **rtk2go / Centipede**: Zero CD/COD-coded stations in either sourcetable as of 2026-05-12 (local pipeline fetch).
- **GEODNET**: No CD-coded GEODNET nodes confirmed.
- **IGS**: No CD-coded IGS core station currently operational.
- **Commercial options**: No commercial NTRIP service with confirmed DR Congo coverage identified. International precision agriculture and surveying contractors operating in DRC (mining sector) typically deploy their own base stations rather than relying on a national caster.
- **Gap assessment**: DR Congo is the second-largest country in Africa (~2.34 million km²) and the third most populous (~100 million). The absence of any public GNSS correction infrastructure is consistent with the pattern across most of sub-Saharan Central Africa and reflects the country's infrastructure development challenges rather than a lack of demand.

## Post-Processing (RINEX) Fallback

No national RINEX archive identified. The IGS archive contains no DR Congo stations with regular data contributions. EarthScope NOTA does not cover Central Africa.

## Sources Consulted
- IGC official website: https://igc-rdc.org/
- IGC about page: https://igc-rdc.org/a-propos/
- IGC alternate site: https://www.igcongo.cd/
- GIM International — IGC profile: https://www.gim-international.com/content/company/institut-geographique-du-congo-2
- Wikipedia — Institut géographique du Congo: https://fr.wikipedia.org/wiki/Institut_g%C3%A9ographique_du_Congo
- AFREF background (IAG): https://geodesy.science/glossary/afref-african-reference-frame/
- IGS station network: https://igs.org/ (no CD stations found 2026-05-12)
- Local pipeline data: `data/stations.json` (rtk2go COD = 0, centipede COD = 0; fetched 2026-05-12T18:17Z)
- AFREF 2024 Workshop / RCMRD: https://ric2024.rcmrd.org/afref
