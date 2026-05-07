# Canada [CA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07 (revising 2026-05-06 entry)

## Status: NO free national NTRIP. Quebec MRNF offers free per-station GNSS streams but on direct-IP (CMR+/RTCM 3.2) — not aggregated NTRIP. All other provinces are commercial-only (paid VAR networks). Volunteer rtk2go (~65 CAN bases) and Centipede (~19 CAN nodes, mostly QC + ON) are the only free NTRIP paths for hobbyists.

| Field | Value |
|---|---|
| **Active free public NTRIP RTK caster (national)** | No |
| **Federal operator (NRCan / NRCan-CSRS)** | RINEX archive + online PPP only (CACS / CSRS-PPP / NRCAN-PPP). No streaming NTRIP. |
| **Provincial free real-time RTK (NTRIP)** | None confirmed. Quebec is closest but uses non-NTRIP per-station TCP streams. |
| **Volunteer NTRIP** | rtk2go ~65 CAN, Centipede ~19 CAN — pulled from `data/stations.json` 2026-05-06T20:16Z |
| **last_confirmed_alive (volunteer)** | 2026-05-06 (latest pipeline fetch) |

---

## Quebec — Réseau géodésique du Québec (RRGQ) [MRNF]

| Field | Value |
|---|---|
| **Operator** | Ministère des Ressources naturelles et des Forêts (MRNF) — formerly MERN/MRN |
| **Service name** | Réseau géodésique du Québec — données GNSS / Stations de captage GNSS |
| **Stations** | 18 permanent GNSS stations across populated Quebec |
| **Protocol** | **NOT NTRIP** — direct cellular IP per station; each emits CMR+ or RTCM V3.2; per-station IP and antenna model published in `Stations_GNSS.pdf` |
| **Tariff** | Free (open data; no registration mentioned on the data portal) |
| **VRS** | No — single-base per station, direct TCP per IP |
| **hobbyist_eligibility** | Yes if your rover/software can take a raw TCP socket (e.g., RTKLIB `str2str` with `tcpcli://`); standard NTRIP clients require manual reconfiguration |
| **legal_residency_required** | No (open data) |
| **last_confirmed_alive** | 2026-05-06 (mrnf.gouv.qc.ca page reachable) |
| **Source documents** | https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ · `https://diffusion.mern.gouv.qc.ca/diffusion/RGQ/Documentation/Geodesie/Stations_GNSS.pdf` (per-station IPs) · https://www.donneesquebec.ca/recherche/dataset/donnees-gnss |

Pipeline note: this network is documented in `docs/networks.md` as `qc_mern` and rejected from the map pipeline because per-station direct-TCP streams are not NTRIP-aggregable.

---

## British Columbia — BC Active Control System (BCACS) / GeoBC

| Field | Value |
|---|---|
| **Operator** | Province of BC (GeoBC) |
| **Stations** | 21 BCACS GNSS stations |
| **Real-time RTK** | Not delivered free. Partnerships with MVRD (Metro Vancouver) and CRD (Capital Regional District) and commercial VARs: Can-Net (Trimble), HxGN SmartNet NA, BrandtNet, Topnet |
| **Tariff — post-processing (BCACS RINEX)** | Free with BCeID account |
| **Tariff — real-time (paid via VAR)** | Country-survey records BC RTN at CAD 1,650/yr (~USD 1,212) — vendor-quoted, not on a public pricing page |
| **hobbyist_eligibility** | Post-processing yes; real-time only via paid VAR contract |
| **Contact** | GeoBCinfo@gov.bc.ca |
| **last_confirmed_alive** | 2026-05-07 (CGRSC + GeoBC pages reachable) |
| **Sources** | https://www2.gov.bc.ca/gov/content/data/geographic-data-services/geo-spatial-referencing/bcacs · https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ |

---

## Other provincial / territorial control networks (CGRSC inventory, 2026-05-07)

| Province | Network | Stations | Real-time RTK access | Post-processing | Notes |
|---|---|---|---|---|---|
| **AB** | GOA HPN (subset of 27,500 total integrated points) | ~1,120 high-precision | No public provincial NTRIP; RTK via commercial VARs (Can-Net, SmartNet, BrandtNet) | SPIN System interactive map | No free real-time tier |
| **MB** | MSRN — Manitoba Survey Reference Network | 244 (MSRN); ~6,500 SuperNet | Not advertised as free real-time | KML / GDB via Manitoba Land Information — **free** | Real-time gap |
| **NB** | NB-HPN / Service New Brunswick | 135 (incl. 9 ACS) | Online portal RINEX only | RINEX via online portal — **free** | No NTRIP |
| **NS** | NSACS — Nova Scotia Active Control Stations | 40 | Fee-based subscription via commercial NRTK providers (HxGN SmartNet, Can-Net, BrandtNet); SmartNet Atlantic plan ~CAD 3,328/yr (~USD 2,429) for NB+NL+NS+PE per country-survey | Post-mission via NRCan — **free** | No free real-time |
| **ON** | HPN | ~10,300 control points | No provincial NTRIP; commercial VARs | COSINE database/viewer | No free real-time |
| **PE** | Active Control (Leica) | 8 active | SmartNet subscription (paid) | Web app available | No free real-time |
| **QC** | RRGQ (MRNF) | 18 | **Free direct-IP CMR+/RTCM 3.2** (not NTRIP) | Free download | Closest to free RTK; pipeline-incompatible |
| **SK** | ISC archive | ~9,000 H / 15,000+ V | Not advertised | Digital archive download | No real-time |
| **YT/NT/NU** | — | — | None confirmed | NRCan archive | EarthScope NOTA covers a few northern stations |

NRCan also lists private RTN operators (Leica SmartNet, Trimble Can-Net, Topcon TopNET, Lewis Instruments, BrandtNet) as compliance-agreement networks integrated into NAD83 (CSRS) but does not operate any public free NTRIP itself. The federal real-time service has been silent since the 2013 NRCan/NGS shutdowns.

---

## Commercial Network RTK providers (Canada-wide, paid; reference only)

The below are listed because Canadian hobbyists usually end up here when no free path is reachable. None publish individual hobbyist tariffs on the open web — all require contact-vendor or reseller quote.

| Provider | Coverage | Indicative pricing | Notes |
|---|---|---|---|
| **Can-Net (Trimble VRS Now)** | Coast-to-coast; 300+ GNSS stations | Quote-only — `am_corrections@trimble.com`, +1 832 538 0210 | VRS via NTRIP; Trimble-acquired; Sensor Map at vrs.can-net.ca |
| **HxGN SmartNet NA** | 8+ Canadian provinces + USA | ~USD 2,400/yr state-level baseline; CAD 3,328/yr Atlantic plan | smartnetna.com; port 10000 typical; iMAX VRS |
| **BrandtNet** | Prairies, BC | Quote-only | Tied to Brandt equipment dealers |
| **Topnet (Topcon)** | Major metros | Quote-only | VRS |
| **MeasurNET** (Measur Drones) | Canada-wide via Measur + GA CORS-augment | Quote-only — measur.ca/products/measur-net | RTCM 3.2; markets itself as "most affordable RTK network in Canada" |
| **Location.io / Rx Networks** | Canada | Paid | rxnetworks.com |
| **CanadaGPS.ca / GeoAstra** | Caster software resellers (free + paid plans) | Free tier 1 base + 1 rover; paid above | canadagps.ca; not a correction network — SaaS caster only |

None of these are free for an individual hobbyist; the commercial Canadian market is structurally reseller-quoted.

---

## Volunteer Coverage (rtk2go + Centipede)

Live counts from `data/stations.json` (fetched 2026-05-06T20:16Z):

| Source | CAN total | Approximate regional split |
|---|---|---|
| **rtk2go** | 65 | AB 21, QC/Maritimes 19, ON 17, Prairies (MB/SK) 7, BC/YT 1 |
| **Centipede** | 19 | QC 15, ON 4 |
| **EarthScope NOTA** | (covers a handful of northern Canada IGS stations under non-commercial NULA; primarily a US service) | — |

Notes:
- The 2026-05-06 entry's claim that *"No Centipede equivalent for Canada exists"* was incorrect. Centipede has a real Canadian footprint (15 in southern Quebec extending the French/Acadian network across the border, plus 4 in southern Ontario).
- rtk2go BC/YT presence is now thin (1 base in the latest fetch); historical "BC Lower Mainland" cluster has receded — Vancouver-area hobbyists are largely on commercial VAR or self-hosted bases.
- AB rtk2go cluster (21) is the strongest Canadian volunteer concentration, mostly Calgary/Edmonton corridors and farm bases.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| NRCan CSRS RINEX archive + CSRS-PPP | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/ | Free (registration) |
| NRCan CSRS-PPP / NRCAN-PPP web tool | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php | Free |
| MRNF Quebec RINEX | https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ | Free |
| Manitoba MSRN / Land Information | KML / GDB downloads via prov. portal | Free |
| Service NB online portal | RINEX | Free |
| SK ISC digital archive | RINEX | Free |
| ON COSINE viewer | Control coords / archive | Free |

---

## Gaps & Observations

1. **No free real-time NTRIP exists at any level of Canadian government.** Quebec's RRGQ is the closest analogue and is free, but the choice not to expose it via NTRIP excludes ~all consumer rover firmware without manual TCP-socket setup.
2. **Provincial real-time tiers have devolved entirely to private VARs.** Even where the underlying CORS hardware (NSACS, BCACS, PE) is government-funded, the streaming layer is monetised by SmartNet/Can-Net/BrandtNet/Topnet under quote-only contracts.
3. **Volunteer networks are the only free NTRIP path.** rtk2go ~65 + Centipede ~19 = ~84 free CAN bases, concentrated in AB (rtk2go), QC (Centipede + rtk2go), ON (both). Practical baselines: Calgary, Edmonton, GTA, southern Quebec are workable; Atlantic, Prairies (interior), BC interior, the territories effectively have no free coverage.
4. **Centipede's Canadian footprint is real and growing southward from Quebec into Ontario** — likely organic spillover from the French Centipede community given the QC linguistic tie. Worth tracking as a potential "free RTK belt" up the St. Lawrence corridor.
5. **No federal replacement for the 2013 NGS/NRCan shutdown is signalled.** Hobbyist policy gap is structural, not pending.

---

## Sources Consulted

- NRCan RTK networks: https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php (observed 2026-05-07)
- CGRSC network RTK services: https://cgrsc.ca/resources/geodetic-control-networks/network-rtk-services/ (observed 2026-05-07)
- CGRSC provincial networks (per-province table): https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ (observed 2026-05-07)
- MRNF Québec GNSS: https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ (observed 2026-05-07)
- MRNF Stations_GNSS.pdf (per-station IPs): `https://diffusion.mern.gouv.qc.ca/diffusion/RGQ/Documentation/Geodesie/Stations_GNSS.pdf` (observed 2026-05-07)
- Quebec GNSS open data: https://www.donneesquebec.ca/recherche/dataset/donnees-gnss (observed 2026-05-07)
- BC Active Control System: https://www2.gov.bc.ca/gov/content/data/geographic-data-services/geo-spatial-referencing/bcacs (observed 2026-05-07)
- Can-Net (Trimble VRS Now): https://www.can-net.ca/ (observed 2026-05-07)
- HxGN SmartNet NA: https://www.smartnetna.com/ ; https://hxgnsmartnet.com/services/smartnet-nrtk (observed 2026-05-07)
- MeasurNET: https://measur.ca/products/measur-net (observed 2026-05-07)
- ArduSimple Canada caster review: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-canada/ (observed 2026-05-07)
- NTRIP-list North America: https://ntrip-list.com/north-america/ (observed 2026-05-07)
- Local pipeline data: `data/stations.json` (rtk2go, centipede source counts; fetched 2026-05-06T20:16Z)
