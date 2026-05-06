# Canada [CA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO free national NTRIP; Quebec offers free direct-IP RTK (non-NTRIP); all other provinces are paid or commercial; rtk2go volunteer coverage present

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (no free national NTRIP); Yes (paid provincial/commercial) |
| **Federal operator** | NRCan (Natural Resources Canada) — RINEX archive only (CSRS portal); no NTRIP stream |
| **hobbyist_eligibility — federal** | RINEX only (post-processing); free registration |
| **legal_residency_required** | No for NRCan RINEX; varies per provincial/commercial service |
| **last_confirmed_alive** | rtk2go volunteer Canadian stations confirmed active 2026-05-06; commercial networks assumed live |

---

## Quebec (Ministère des Ressources naturelles et des Forêts — MRNF)

| Field | Value |
|---|---|
| **Service** | Réseau de référence GPS du Québec (RRGQ) — 18 permanent GNSS stations |
| **Protocol** | Direct IP (CMR+ or RTCM 3.2 per station) — **NOT NTRIP** |
| **Tariff** | Free — "accessible to all" |
| **Coverage** | Populated Quebec municipalities; sparse in north |
| **hobbyist_eligibility** | Yes — free access; specific IP/port per station from documentation |
| **VRS** | No — single-base per station; direct TCP connection to each station IP |
| **Source document** | "Stations de captage GNSS" (IP addresses per city) at https://diffusion.mern.gouv.qc.ca/ |

Note: Quebec's free RTK service uses CMR+ or RTCM 3.2 but requires a direct TCP connection to each station's IP rather than standard NTRIP protocol. Standard NTRIP clients cannot access it without custom configuration.

---

## British Columbia (Province of BC)

| Field | Value |
|---|---|
| **Network** | BC Active Control System (BCACS) — 21 GNSS stations |
| **Protocol** | FTP/post-processing primary; real-time RTK via commercial VARs |
| **Tariff — post-processing** | Free (BCeID account required) |
| **Tariff — real-time RTK** | Via commercial Value Added Resellers: Can-Net, SmartNet, BrandtNet, Topnet |
| **Contact** | GeoBCinfo@gov.bc.ca |
| **hobbyist_eligibility** | Post-processing: yes (free). Real-time RTK: paid subscription to commercial VAR |

---

## Commercial Network RTK Providers (Canada-wide)

The following commercial networks provide NTRIP-based VRS RTK corrections in Canada:

| Provider | Coverage | Approx. Price | Notes |
|---|---|---|---|
| **HxGN SmartNet NA** | 8+ Canadian provinces + US | ~USD $2,400/year (state-level); flexible plans | smartnetna.com; port 10000 typical; NTRIP with credentials; VRS (iMAX) |
| **Can-Net (Trimble)** | Coast-to-coast; 300+ stations | Contact vendor (am_corrections@trimble.com) | trimble.com; VRS; NTRIP |
| **BrandtNet** | Prairies, BC | Contact vendor | Tied to Brandt equipment dealers |
| **Topnet (Topcon)** | Major metros | Contact vendor | VRS |
| **MeasurNET** | Canada-wide via GA CORS + own | Contact measur.ca | RTCM 3.2; hobbyist-friendly |
| **Location.io (Rx Networks)** | Canada | Paid | rxnetworks.com |

None of the commercial networks publish pricing publicly; all require account creation or vendor contact.

---

## Nova Scotia

| Field | Value |
|---|---|
| **Network** | Nova Scotia Active Control Stations (NSACS) — 40 GNSS stations |
| **Tariff — real-time RTK** | Fee-based subscription via commercial Network RTK providers (SmartNet, etc.) |
| **Tariff — post-processing** | Free (NRCan web interface) |

## Prince Edward Island

PEI active control stations managed by Leica Geosystems SmartNet; subscriptions via SmartNet NA.

## Other Provinces (AB, MB, SK, ON, NB, NL)

Alberta, Manitoba, Saskatchewan, and Ontario rely primarily on commercial network RTK services (SmartNet NA, Can-Net, Topnet). No free provincial NTRIP tier identified.

---

## Volunteer Coverage (rtk2go)

rtk2go hosts a number of Canadian volunteer NTRIP base stations. Coverage concentrates around:
- BC Lower Mainland / Greater Vancouver
- Alberta (Calgary, Edmonton corridors)
- Ontario (Greater Toronto Area)
- Quebec populated areas

No Centipede equivalent for Canada exists. rtk2go bases are the only free NTRIP option for Canadian hobbyists outside of Quebec's non-NTRIP direct-IP system.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **NRCan CSRS** — RINEX archive + online PPP | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/ | Free (registration) |
| **NRCan OPUS / CSRS-PPP** — precise point positioning | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php | Free |
| **MRNF Québec RINEX** | https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ | Free |

## Sources Consulted
- NRCan RTK networks web application: https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php (observed 2026-05-06)
- CGRSC network RTK services: https://cgrsc.ca/resources/geodetic-control-networks/network-rtk-services/ (observed 2026-05-06)
- CGRSC provincial networks: https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ (observed 2026-05-06)
- MRNF Québec GNSS réseau: https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ (observed 2026-05-06)
- Quebec GNSS open data: https://www.donneesquebec.ca/recherche/dataset/donnees-gnss/resource/8f37e6ba-3025-4e9c-81c9-85b1705b5de3 (observed 2026-05-06)
- BC Active Control System: https://www2.gov.bc.ca/gov/content/data/geographic-data-services/geo-spatial-referencing/bcacs (observed 2026-05-06)
- Can-Net: https://www.can-net.ca/ (observed 2026-05-06)
- SmartNet NA: https://www.smartnetna.com/ (observed 2026-05-06)
- MeasurNET: https://measur.ca/products/measur-net (observed 2026-05-06)
- NTRIP-list North America: https://ntrip-list.com/north-america/ (observed 2026-05-06)
- rtk2go.com mountpoint list (CAN stations, observed 2026-05-06)
