# Canada [CA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status
No free public NTRIP at any level of Canadian government. NRCan operates CACS as a post-processing / PPP backbone only — no real-time streaming. Provincial real-time tiers (BC, NS, PE, etc.) are delivered exclusively through paid commercial VAR contracts (Can-Net / SmartNet NA / BrandtNet / Topnet). Quebec MRNF is the only province publishing free real-time corrections, but it does so via per-station direct TCP (CMR+ / RTCM 3.2), not aggregated NTRIP. Volunteer rtk2go (64 CAN bases) and Centipede (21 CAN nodes) are the only free NTRIP options reachable by a stock rover firmware.

---

## NRCan / Canadian Geodetic Survey — CACS, CSRS-PPP, RTK compliance registry

| Field | Value |
|---|---|
| **landing_url** | https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/canadian-spatial-reference-system-csrs |
| **access_url** | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php (RTK networks compliance map) · https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php (CSRS-PPP) |
| **Operator** | Natural Resources Canada — Canadian Geodetic Survey |
| **Real-time NTRIP** | None operated by NRCan. CACS is a ~20-site backbone for NAD83(CSRS) integration and CSRS-PPP; the federal service does not stream RTCM publicly. |
| **What is free** | CSRS-PPP web service (post-mission PPP); RINEX archive from CACS sites; the public RTK-networks map listing third-party stations compliant with NAD83(CSRS). |
| **datum_epoch** | NAD83(CSRS) v7 (current realization). Datum reference: https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/canadian-spatial-reference-system-csrs |
| **last_confirmed_alive** | 2026-05-15 — rtk.php HTTP 200 |

---

## Quebec — Réseau géodésique du Québec (MRNF)

| Field | Value |
|---|---|
| **landing_url** | https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ |
| **access_url** | https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ (per-station IP list in `Stations_GNSS.pdf`) |
| **Operator** | Ministère des Ressources naturelles et des Forêts (MRNF) |
| **Protocol** | **NOT NTRIP** — direct per-station TCP (one IP per station; CMR+ or RTCM V3.2). Page text: "the data are not distributed according to the Networked Transport of RTCM via Internet Protocol (NTRIP)". |
| **host:port** | Per-station IP/port published in `https://diffusion.mern.gouv.qc.ca/diffusion/RGQ/Documentation/Geodesie/Stations_GNSS.pdf` (HTTP 200 2026-05-15) |
| **tariff** | Free, open data, no registration mentioned (donneesquebec.ca dataset, MRNF page) |
| **num_stations** | 18 permanent GNSS stations |
| **vrs** | No (single-base per station) |
| **hobbyist_eligibility** | Yes only if rover/software can connect to a raw TCP socket (e.g., RTKLIB `str2str -in tcpcli://`). Most consumer GNSS firmware accepts NTRIP only and cannot use this service without an NTRIP-relay shim. |
| **legal_residency_required** | No (open data) |
| **datum_epoch** | NAD83(CSRS) epoch 1997.0 — declared on the operator page (mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/) |
| **last_confirmed_alive** | 2026-05-15 — mrnf.gouv.qc.ca HTTP 200; diffusion.mern.gouv.qc.ca PDF HTTP 200 |

Pipeline note: tracked in `docs/networks.md` as `qc_mern` and rejected from the map pipeline (`status: other`) because per-station direct-TCP streams are not NTRIP-aggregable.

---

## British Columbia — BC Active Control System (BCACS) / GeoBC

| Field | Value |
|---|---|
| **landing_url** | https://www2.gov.bc.ca/gov/content/data/geographic-data-services/geo-spatial-referencing/bcacs |
| **access_url** | Same; contact GeoBCInfo@gov.bc.ca |
| **Operator** | Province of British Columbia (GeoBC) |
| **num_stations** | 20 permanent BCACS GNSS receivers (operator page, 2026-05-15) |
| **Real-time RTK** | Not delivered free by the province. Page directs to MVRD (Metro Vancouver) and CRD (Capital Regional District) RTN partnerships sold by annual/monthly subscription, and to commercial VARs (Can-Net, HxGN SmartNet NA, BrandtNet, Topnet). NTRIP portal URLs not currently public following a gov.bc.ca reorganisation. |
| **Post-processing** | RINEX FTP, subscription or pay-per-download; requires Basic or Business BCeID. |
| **tariff (RTK via VAR)** | Documented in `docs/networks.md` `bc_rtn` as CAD 1,650/yr (~USD 1,212) per Land Act Subscription Fee Regulation B.C. Reg. 55/98 (vendor-quoted, not on a self-service web page). |
| **vrs** | Yes (Trimble-based RTN where delivered) |
| **hobbyist_eligibility** | Post-processing yes; real-time only via paid VAR contract. |
| **datum_epoch** | NAD83(CSRS) — provincial standard, per BCACS page |
| **last_confirmed_alive** | 2026-05-15 — bcacs page HTTP 200 |

---

## Other provincial / territorial control networks (CGRSC inventory, observed 2026-05-15)

| Province | Network | Stations | Real-time RTK access | Post-processing | Notes |
|---|---|---|---|---|---|
| **AB** | Alberta Survey Control (HPN subset of ~27,500 integrated points) | ~1,120 HPN | None public; via Can-Net / SmartNet / BrandtNet | SPIN System | No free real-time |
| **MB** | MSRN — Manitoba Spatial Reference Network | 244 GNSS / 6,500 SuperNet | None public | KML / GDB free | Real-time gap |
| **NB** | NB-HPN / Service NB | 135 (9 ACS) | None public | Online portal RINEX — free | No NTRIP |
| **NL** | Provincial markers | ~7,000 monuments | None public | Available | No NTRIP |
| **NS** | NSACS | 40 | Paid via HxGN SmartNet NA, Can-Net, BrandtNet only (no direct provincial caster). SmartNet Atlantic plan CAD 3,328/yr (~USD 2,429); national SmartNet CAD 6,084/yr (~USD 4,441), `smartnetna.com` confirmed by `docs/networks.md` 2026-04-30. | Free via NRCan | No free real-time |
| **ON** | HPN | ~10,300 HPN of 125,000+ control points | None public; commercial VARs | COSINE viewer | No free real-time |
| **PE** | Active Control (Leica) | 8 | Paid SmartNet subscription | Web app | No free real-time |
| **QC** | MRNF — Réseau géodésique du Québec | 18 | **Free direct-IP CMR+ / RTCM 3.2** (not NTRIP) | Free download | Pipeline-incompatible |
| **SK** | ISC digital archive | ~9,000 H / 15,000+ V | None public | RINEX download | No real-time |
| **YT / NT / NU** | — | — | None | NRCan / EarthScope-NOTA at a handful of northern sites | No coverage |

Source: https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ (HTTP 200 2026-05-15) and per-province operator pages.

---

## Commercial NTRIP providers (paid; reference only, all out of map scope)

Listed because Canadian hobbyists routinely arrive at these when no free path is reachable. None publish hobbyist-tier pricing on the open web; quotes are reseller-only.

| Provider | Coverage | Indicative pricing | Probe / source |
|---|---|---|---|
| **Can-Net (Trimble VRS Now)** | 300+ stations coast-to-coast | Quote-only via `am_corrections@trimble.com` / +1 832 538 0210 | https://www.can-net.ca/ HTTP 200 2026-05-15; raw `vrs.can-net.ca:2101` not reachable from this sandbox (curl exit 6 / HTTP 000 — DNS/firewall) |
| **HxGN SmartNet NA** | 8+ CA provinces + USA | CAD 3,328/yr Atlantic plan; CAD 6,084/yr national | https://www.smartnetna.com/ HTTP 302 2026-05-15 |
| **BrandtNet** | Prairies + BC; 140+ stations | Quote-only (account login) | https://rtk.brandt.ca/ HTTP 301 2026-05-15 |
| **Topnet (Topcon)** | Major metros | Quote-only | `rtk.topnetlive.com:2101` HTTP 000 from this sandbox |
| **MeasurNET (Measur)** | Canada-wide (+ GA CORS augment) | Quote-only | measur.ca/products/measur-net |
| **Skylark (Swift Navigation)** | Continental | Subscription (USD 29–69/mo per Ardusimple review) | swiftnav.com/skylark |
| **Lewis Instruments** | Regional | Quote-only | Listed by NRCan as a compliance-agreement RTN operator |
| **GEODNET** | Decentralized (Helium-style RTK token incentive) | Free public tier + paid via api | Listed on NRCan rtk.php data catalog (provider key `GEODNET`) |
| **METACON / LATNET / DART** | Regional | Quote-only | Also listed on NRCan rtk.php data catalog; smaller VARs |

---

## Volunteer Coverage (free NTRIP actually usable by hobbyists)

Live counts from `data/stations.json` (updated 2026-05-15T16:22Z; both casters probed HTTP 200 today):

| Source | CAN total | Geographic concentration |
|---|---|---|
| **rtk2go** | 64 | AB ~16 (Calgary/Edmonton/farm corridor), ON ~13 (incl. GTA / Niagara), QC ~10, SK/MB ~7, Maritimes 2, BC 2 (fluffyYAQ ~48.81/-123.59, Nakusp1 ~50.24/-117.80), YT/NT/NU 0 |
| **Centipede** | 21 | QC 16, ON 5 — organic St. Lawrence corridor seeded by the French-speaking Centipede community |
| **EarthScope (NOTA)** | a handful of IGS-grade sites in northern Canada | Non-commercial NULA, primarily US-facing |
| **IGS-IP** | 32 CAN | Operational-research streams; not intended for cm-level RTK |

Practical reading:
- AB / ON / southern QC are the only Canadian regions where free NTRIP is consistently within useful RTK baseline (≤30 km) of a populated area.
- BC has 2 rtk2go bases (fluffyYAQ + Nakusp1). Lower Mainland and Vancouver Island hobbyists outside their reach are effectively forced to a commercial VAR or self-hosted base.
- Maritimes (2 rtk2go), Prairies interior (7 rtk2go in SK/MB combined), and all three territories have no usable free coverage.

Ottawa cross-check (`scripts/stations_by_radius.py 45.42 -75.69 200`, 2026-05-15): 7 rtk2go CAN bases inside 200 km (closest `CanalTerris` 6.8 km) plus 4 Centipede nodes (1 US-tagged `RANG7` at 43.8 km is the nearest of any — cross-border behaviour, no functional impact).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| NRCan CSRS RINEX archive + CSRS-PPP | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/ | Free (registration) |
| CSRS-PPP web tool | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php | Free |
| MRNF Quebec RINEX | https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ | Free |
| Manitoba MSRN | Provincial portal | Free |
| Service NB | RINEX portal | Free |
| Nova Scotia (via NRCan) | RINEX | Free |
| SK ISC digital archive | RINEX | Free |
| ON COSINE | Control coords / archive | Free |

---

## Gaps & Observations

1. **No federal free real-time NTRIP exists.** CACS remains post-processing / PPP only; the 2013 NRCan/NGS shutdown gap has not been filled and no replacement is signalled in 2026 NRCan communications.
2. **Quebec is the only province with a free real-time correction service**, but its choice to use per-station direct TCP (not NTRIP) excludes essentially all consumer rover firmware without a manual TCP-socket or NTRIP-relay configuration. From a "stock rover + free corrections" hobbyist perspective Quebec is functionally a volunteer-network province.
3. **All other provinces have fully outsourced real-time delivery to paid VARs.** Even where the underlying CORS hardware (NSACS 40, BCACS 20, PE 8) is government-funded, streaming is monetised by SmartNet / Can-Net / BrandtNet / Topnet under quote-only contracts.
4. **Volunteer networks are the only free NTRIP path for a typical hobbyist.** rtk2go 64 + Centipede 21 ≈ 85 free CAN bases. Practical baselines exist in AB, southern ON, and southern QC; everywhere else there is effectively no free RTK.
5. **Centipede's Canadian footprint sits 16 QC + 5 ON** — concentrated along the southern St. Lawrence corridor, the densest free-coverage zone in the country when combined with rtk2go QC.

---

## Sources Consulted (literal probe results, 2026-05-15)

- NRCan RTK networks map — https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php — HTTP 200
- NRCan CACS — https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/cacs-scca.php?locale=en — referenced
- NRCan CSRS landing — https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/canadian-spatial-reference-system-csrs — referenced
- CGRSC provincial networks — https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ — HTTP 200
- CGRSC network RTK services — https://cgrsc.ca/resources/geodetic-control-networks/network-rtk-services/ — referenced
- MRNF Québec GNSS — https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ — HTTP 200
- MRNF Stations_GNSS.pdf (per-station IPs) — https://diffusion.mern.gouv.qc.ca/diffusion/RGQ/Documentation/Geodesie/Stations_GNSS.pdf — HTTP 200
- Données Québec GNSS dataset — https://www.donneesquebec.ca/recherche/dataset/donnees-gnss — HTTP 403 (anti-bot; reachable from a normal browser per WebSearch result excerpt)
- BCACS info page — https://www2.gov.bc.ca/gov/content/data/geographic-data-services/geo-spatial-referencing/bcacs — HTTP 200
- Can-Net — https://www.can-net.ca/ — HTTP 200; `vrs.can-net.ca:2101` HTTP 000 (not reachable from this sandbox; access is subscriber-only by design)
- HxGN SmartNet NA — https://www.smartnetna.com/ — HTTP 302
- BrandtNet portal — https://rtk.brandt.ca/ — HTTP 301
- Ardusimple Canada caster review — https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-canada/ — referenced
- rtk2go caster — http://rtk2go.com:2101/ — HTTP 200 (sourcetable 143 KB)
- Centipede caster — http://caster.centipede.fr:2101/ — HTTP 200 (sourcetable 262 KB)
- Local pipeline data: `data/stations.json` updated 2026-05-15T16:22:28Z — rtk2go CAN=64, Centipede CAN=21, IGS-IP CAN=32, EarthScope CAN counted only as a handful of NULA northern sites
