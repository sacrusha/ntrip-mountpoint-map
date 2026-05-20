# Canada [CA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17

## Status
No free public NTRIP at any level of Canadian government. NRCan operates CACS as a post-processing / PPP backbone only — no real-time streaming. Federal NATRF2022 cutover (geocentric, plate-fixed, ITRF2020-aligned) begins early 2027; provinces follow ~2030. Provincial real-time tiers (NS, PE, BC, etc.) reach the user exclusively through paid commercial VAR contracts (Can-Net / HxGN SmartNet NA / BrandtNet / TopNET Live / Rx Networks TruePoint FOCUS / Lewis Instruments / RTKdata.com). Quebec MRNF is the only province publishing free real-time corrections, but via per-station direct TCP (CMR+ / RTCM 3.2), not NTRIP. Volunteer rtk2go (68 CAN bases) and Centipede (21 CAN nodes) are the only free NTRIP options reachable by stock rover firmware.

Pattern below: one block per provincial agency + one block per commercial operator. Federal NRCan policy + NATRF2022 cutover timeline kept as Context. Quebec stays as one inline provincial block (per-station direct TCP, not aggregable NTRIP).

---

## Context — NRCan / Canadian Geodetic Survey

CACS = federal post-processing backbone (~20 sites), CSRS-PPP web service, RTK compliance registry of third-party stations integrated to NAD83(CSRS). NRCan does **not** stream RTCM publicly. NATRF2022 federal cutover: early 2027 per CSRS modernization page (https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/canadian-spatial-reference-system-csrs-modernization). Provincial follow-on ~2030. Expect 1–2 m horizontal coordinate shift at adoption. Most provincial CORS hardware is shared with Can-Net / SmartNet / BrandtNet — datum migration is a vendor problem on subscribed services, end-user problem only for self-hosted bases. Anchor registry: https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php?locale=en (interactive map; static content empty without JS, list discovered via CGRSC + per-operator portals).

| Field | Value |
|---|---|
| **landing_url** | https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/canadian-spatial-reference-system-csrs |
| **access_url** | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php (RTK compliance map) · https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php (CSRS-PPP) |
| **host:port** | None operated by NRCan. |
| **num_stations** | ~20 CACS backbone sites |
| **vrs** | No |
| **tariff** | Free CSRS-PPP + RINEX archive; no real-time tier |
| **hobbyist_eligibility** | Yes (post-processing only) |
| **legal_residency_required** | No |
| **datum_epoch** | NAD83(CSRS); federal NATRF2022 cutover begins early 2027 — operator declaration https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/canadian-spatial-reference-system-csrs (epoch not separately published on NRCan CSRS landing) |
| **last_confirmed_alive** | 2026-05-17 (rtk.php + modernization pages reachable) |

---

## Provincial blocks

### British Columbia — BCACS / GeoBC

| Field | Value |
|---|---|
| **landing_url** | https://www2.gov.bc.ca/gov/content/data/geographic-data-services/geo-spatial-referencing/bcacs |
| **access_url** | Same; contact GeoBCInfo@gov.bc.ca for RINEX (Basic / Business BCeID required). Real-time only via MVRD / CRD municipal partnerships + commercial VARs. |
| **host:port** | None published. NTRIP URL absent following gov.bc.ca reorganisation; municipal RTNs (Metro Vancouver, Capital Regional District) referenced on BCACS page but no public caster URL surfaced 2026-05-17. |
| **num_stations** | 20 permanent BCACS receivers (operator page 2026-05-17; CGRSC table says 21 — operator-page count preferred). |
| **vrs** | Yes (Trimble-based RTN where municipal partnerships deliver). |
| **tariff** | CAD 1,650/yr statutory fee per Land Act Subscription Fee Regulation B.C. Reg. 55/98 (vendor-quoted; not on self-service page). Post-processing: pay-per-download or subscription via GeoBCInfo. |
| **hobbyist_eligibility** | Post-processing yes; real-time only via paid VAR contract (Can-Net / SmartNet / BrandtNet / TopNET). |
| **legal_residency_required** | No formal residency req. BCeID for RINEX FTP. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (no public caster). |
| **last_confirmed_alive** | 2026-05-17 (BCACS info page WebFetch 200; no public caster to probe) |

Pipeline: tracked in `rtk_inventory.md` as `bc_rtn` (status: paid).

---

### Alberta — Alberta Survey Control / SPIN System

| Field | Value |
|---|---|
| **landing_url** | https://alta.registries.gov.ab.ca/spinii/logon.aspx (SPIN — Spatial Information System; ASC viewer) |
| **access_url** | SPIN portal (KML / GDB download); no real-time provincial caster |
| **host:port** | None — Alberta does not operate a public CORS NTRIP stream (CGRSC + Ardusimple 2026-05-17: AB maintains passive HPN monuments only). |
| **num_stations** | ~1,120 HPN of ~27,500 ASC integrated monuments (passive control). Zero active CORS run by province. |
| **vrs** | n/a |
| **tariff** | Free passive-monument access via SPIN; real-time only via Can-Net / SmartNet / BrandtNet / TopNET. |
| **hobbyist_eligibility** | Passive-data yes; real-time no free path. |
| **legal_residency_required** | No (SPIN public). |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (no active caster). |
| **last_confirmed_alive** | 2026-05-17 (SPIN page referenced via CGRSC; no caster) |

---

### Saskatchewan — ISC Geomatics Dataset

| Field | Value |
|---|---|
| **landing_url** | https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ (operator page is ISC Geomatics; canonical link surfaced via CGRSC inventory) |
| **access_url** | ISC online digital archive (RINEX + control coords; no real-time NTRIP) |
| **host:port** | None — SK runs no provincial CORS NTRIP stream. |
| **num_stations** | ~9,000 horizontal + 15,000+ vertical passive monuments. |
| **vrs** | n/a |
| **tariff** | Free passive download; real-time only via commercial VARs (BrandtNet dominant on Prairies). |
| **hobbyist_eligibility** | Passive-data yes; real-time no free path. |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (no active caster). |
| **last_confirmed_alive** | 2026-05-17 (CGRSC inventory page) |

---

### Manitoba — MSRN / Manitoba Land Information

| Field | Value |
|---|---|
| **landing_url** | https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ (canonical operator page via CGRSC; Manitoba Land Information portal links from there) |
| **access_url** | MSRN KML / GDB free download; SuperNet GIS infrastructure separately. No real-time NTRIP. |
| **host:port** | None — MB runs no provincial CORS NTRIP stream. |
| **num_stations** | 244 GNSS monuments + 6,500 SuperNet markers (passive). |
| **vrs** | n/a |
| **tariff** | Free passive download; real-time only via commercial VARs (BrandtNet, Can-Net). |
| **hobbyist_eligibility** | Passive-data yes; real-time no free path. |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (no active caster). |
| **last_confirmed_alive** | 2026-05-17 (CGRSC inventory) |

---

### Ontario — COSINE / Ontario Geographic Reference Framework

| Field | Value |
|---|---|
| **landing_url** | https://www.ontario.ca/page/ontario-specification-global-navigation-satellite-systems-gnss-geodetic-control-surveys |
| **access_url** | COSINE viewer (Control Survey Information Exchange) — passive control coords; no real-time NTRIP. |
| **host:port** | None — ON runs no provincial CORS NTRIP stream. Province publishes GNSS-network specifications for third-party CORS to integrate into COSINE; no operator caster. |
| **num_stations** | ~10,300 HPN within 125,000+ control points (passive). |
| **vrs** | n/a |
| **tariff** | Free passive access via COSINE; real-time only via commercial VARs. |
| **hobbyist_eligibility** | Passive-data yes; real-time no free path. |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (no active caster). |
| **last_confirmed_alive** | 2026-05-17 (Ontario specification page; CGRSC) |

---

### Quebec — Réseau géodésique du Québec (MRNF)

| Field | Value |
|---|---|
| **landing_url** | https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ |
| **access_url** | Same; per-station IP list at https://diffusion.mern.gouv.qc.ca/diffusion/RGQ/Documentation/Geodesie/Stations_GNSS.pdf |
| **host:port** | **NOT NTRIP** — direct per-station TCP (one IP per station, CMR+ or RTCM v3.2). Operator wording: "the data are not distributed according to the Networked Transport of RTCM via Internet Protocol (NTRIP)." |
| **num_stations** | 18 permanent stations. |
| **vrs** | No (single-base per station). |
| **tariff** | Free, open data (donneesquebec.ca dataset), no registration. |
| **hobbyist_eligibility** | Yes IFF rover/software can connect to raw TCP socket (e.g. RTKLIB `str2str -in tcpcli://`). Most consumer firmware NTRIP-only → needs NTRIP-relay shim. |
| **legal_residency_required** | No. |
| **datum_epoch** | NAD83(CSRS) epoch 1997.0 — operator declaration https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ ("NAD 83 (SCRS) (époque 1997,0)"). |
| **last_confirmed_alive** | 2026-05-17 (MRNF page reachable; Stations_GNSS.pdf HEAD 200, 264 KB, Last-Modified 2026-01-15 via DNS 142.41.245.97). |

Pipeline note: tracked in `rtk_inventory.md` as `qc_mern` (status: other) — direct-TCP not NTRIP-aggregable. Block kept inline; not split to CA-QC file (under split-threshold; one block; flagged under unresolved).

---

### New Brunswick — NB-HPN / Service NB

| Field | Value |
|---|---|
| **landing_url** | https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ |
| **access_url** | SNB online portal — RINEX download, no real-time NTRIP. |
| **host:port** | None — SNB licenses RINEX redistribution only; no provincial caster. |
| **num_stations** | 135 monuments incl. 9 Active Control Stations (continuously operating GNSS receivers, RINEX-only). |
| **vrs** | n/a |
| **tariff** | Free RINEX via SNB portal; real-time only via commercial VARs (HxGN SmartNet Atlantic). |
| **hobbyist_eligibility** | Passive-data yes; real-time no free path. |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (no active caster). |
| **last_confirmed_alive** | 2026-05-17 (CGRSC inventory) |

---

### Nova Scotia — NSACS / GeoNova

| Field | Value |
|---|---|
| **landing_url** | https://geonova.novascotia.ca/coordinate-referencing |
| **access_url** | Same. RINEX free via NRCan archive; real-time only via NSACS-licensed NRTK resellers (HxGN SmartNet NA, Can-Net, BrandtNet). |
| **host:port** | None operated by province. SmartNet caster `it.nrtk.eu`-equivalent NA endpoint via smartnetna.com; not provincial. |
| **num_stations** | 40 NSACS Active Control Stations (provincially-owned hardware; commercial-stream delivery). |
| **vrs** | Yes (via commercial resellers; province does not stream). |
| **tariff** | CAD 3,328/yr Atlantic plan (NB/NL/NS/PE) HxGN SmartNet; CAD 6,084/yr national; Can-Net + BrandtNet quote-only. Free RINEX via NRCan. |
| **hobbyist_eligibility** | Passive-data yes; real-time via paid VAR only. |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (province does not stream; commercial-reseller stream not provincial). |
| **last_confirmed_alive** | 2026-05-17 (geonova page + NSACS reseller doc) |

Pipeline: tracked in `rtk_inventory.md` as `nsacs` (status: paid).

---

### Prince Edward Island — PEI Active Control

| Field | Value |
|---|---|
| **landing_url** | https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ |
| **access_url** | Provincial web app (control-coord viewer); real-time only via SmartNet Atlantic. |
| **host:port** | None operated by province. |
| **num_stations** | 8 Active Control Stations (Leica) + 4,746 passive. |
| **vrs** | Via reseller only. |
| **tariff** | Real-time: paid HxGN SmartNet Atlantic (CAD 3,328/yr). Passive: free. |
| **hobbyist_eligibility** | Passive yes; real-time no free path. |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (province does not stream). |
| **last_confirmed_alive** | 2026-05-17 (CGRSC inventory) |

---

### Newfoundland & Labrador — Provincial passive markers

| Field | Value |
|---|---|
| **landing_url** | https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/ |
| **access_url** | Provincial monument archive; no real-time NTRIP. |
| **host:port** | None. |
| **num_stations** | ~7,000 passive monuments; zero active CORS run by province. |
| **vrs** | n/a |
| **tariff** | Passive free; real-time only via HxGN SmartNet Atlantic / Can-Net (where coverage extends). |
| **hobbyist_eligibility** | Passive yes; real-time no free path. |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (no active caster). |
| **last_confirmed_alive** | 2026-05-17 (CGRSC inventory) |

---

### Territories — Yukon / Northwest Territories / Nunavut

| Field | Value |
|---|---|
| **landing_url** | NRCan CACS + EarthScope NOTA portal (https://www.earthscope.org/data/gnss-realtime/) |
| **access_url** | Same. No territorial operator. |
| **host:port** | None operated. Handful of NRCan CACS + EarthScope-NOTA sites in northern Canada; non-commercial scientific use. |
| **num_stations** | Combined territorial real-time: effectively 0 usable for surveying RTK. |
| **vrs** | No. |
| **tariff** | Free (where any stream exists; EarthScope non-commercial NULA). |
| **hobbyist_eligibility** | YT/NT/NU: no practical free RTK coverage; long-baseline PPP only. |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — national standard, no per-network operator declaration (no provincial/territorial caster). |
| **last_confirmed_alive** | 2026-05-17 (no caster) |

---

## Commercial blocks (paid; all out of map scope but listed for hobbyist arrival path)

### Can-Net — Trimble VRS Now Canada

| Field | Value |
|---|---|
| **landing_url** | https://www.can-net.ca/ |
| **access_url** | Same; subscription via am_corrections@trimble.com / +1 832 538 0210 |
| **host:port** | `vrs.can-net.ca:2101` (subscriber-only; sourcetable not public) |
| **num_stations** | 300+ stations coast-to-coast (operator-stated 2026-05-17). |
| **vrs** | Yes (Trimble VRS). |
| **tariff** | Quote-only; no public price list. Subscription + post-processed services both quote-only. |
| **hobbyist_eligibility** | Unclear; not stated as restricted. No public hobbyist tier. |
| **legal_residency_required** | No. |
| **datum_epoch** | NAD83(CSRS) — NRCan compliance registry citation https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php?locale=en (epoch not declared by operator or NRCan registry). |
| **last_confirmed_alive** | 2026-05-17 (can-net.ca operator page WebFetch 200; raw caster not probed) |

---

### HxGN SmartNet NA — Leica Geosystems / Hexagon

| Field | Value |
|---|---|
| **landing_url** | https://hxgnsmartnet.com/en-US (redirected from smartnetna.com 2026-05-17) |
| **access_url** | https://www.smartnetna.com/store_product_selector.cfm (subscription store) |
| **host:port** | Subscriber-only NA caster (URL not on landing); historical `smartnet-na.com` endpoints. |
| **num_stations** | NA-wide (8+ CA provinces + USA); per-country station count not published. |
| **vrs** | Yes. |
| **tariff** | CAD 3,328/yr Atlantic plan (NB/NL/NS/PE); CAD 6,084/yr national; smartnetna.com store. GST/HST not stated → confirm at checkout. |
| **hobbyist_eligibility** | Unclear; no explicit residency / VAT-ID gate. Professional-surveying positioning. |
| **legal_residency_required** | No. |
| **datum_epoch** | NAD83(CSRS) — NRCan compliance registry citation https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php?locale=en (epoch not declared by operator or NRCan registry). |
| **last_confirmed_alive** | 2026-05-17 (smartnetna.com redirect → hxgnsmartnet.com 200; pricing page 2026-04-30) |

---

### BrandtNet — Brandt Tractor / John Deere dealer network

| Field | Value |
|---|---|
| **landing_url** | https://rtk.brandt.ca/ |
| **access_url** | Account request via rtk.brandt.ca/login.php; +1 877 291 7503 |
| **host:port** | Subscriber-only (account login wall) |
| **num_stations** | 140+ stations Prairies + BC (operator-stated; per-province breakdown not public). |
| **vrs** | Yes. |
| **tariff** | Monthly + yearly rates available; not on public page. Quote-only via account portal. |
| **hobbyist_eligibility** | Unclear. John Deere ag dealer channel; small-farm subscriptions common. |
| **legal_residency_required** | No. |
| **datum_epoch** | NAD83(CSRS) — NRCan compliance registry citation https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php?locale=en (epoch not declared by operator or NRCan registry). |
| **last_confirmed_alive** | 2026-05-17 (rtk.brandt.ca page 200) |

---

### TopNET Live Canada — Topcon

| Field | Value |
|---|---|
| **landing_url** | https://www.topnetlive.com/ (CA cert expired 2026-05-17 — operator site unreachable today; landing reachable via cache; NRCan registry confirms Canadian CORS contribution.) |
| **access_url** | Subscription via Topcon Positioning dealer network. |
| **host:port** | `rtk.topnetlive.com:2101` (NA region; not probed 2026-05-17). |
| **num_stations** | Major-metro coverage; Canadian station count not public. |
| **vrs** | Yes. |
| **tariff** | Quote-only via dealer. |
| **hobbyist_eligibility** | No public self-serve tier; Topcon dealer-channel subscription required. CGRSC commercial-RTN list (2026-05-17) confirms operator alive but provides no hobbyist-tier info; per primer convention this is treated as "no" (no published hobbyist path) rather than "unclear". |
| **legal_residency_required** | No. |
| **datum_epoch** | NAD83(CSRS) — NRCan compliance registry citation https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php?locale=en (epoch not declared by operator or NRCan registry). |
| **last_confirmed_alive** | 2026-05-17 (operator site `topnetlive.com` cert expired; CGRSC commercial-RTN list https://cgrsc.ca/resources/geodetic-control-networks/network-rtk-services/ still lists Topcon TopNET as alive Canadian RTN operator) |

---

### Lewis Instruments — Atlantic Canada regional RTN

| Field | Value |
|---|---|
| **landing_url** | http://www.lewisinstruments.com (HTTP 403 to WebFetch 2026-05-17 from sandbox; CGRSC commercial-RTN list 2026-09-09 confirms operator) |
| **access_url** | (800) 883-9984 / info@lewisinstruments.com |
| **host:port** | Not publicly listed. |
| **num_stations** | Regional (Atlantic-focused); count not published. |
| **vrs** | Yes (NRCan compliance-agreement RTN operator). |
| **tariff** | Quote-only. |
| **hobbyist_eligibility** | Unclear; surveying-equipment dealer. |
| **legal_residency_required** | No. |
| **datum_epoch** | NAD83(CSRS) — NRCan compliance registry citation https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php?locale=en (epoch not declared by operator or NRCan registry). |
| **last_confirmed_alive** | 2026-05-17 (CGRSC operator-list reference; operator site 403 from sandbox) |

---

### RTKdata.com Canada — Kansi Solutions GmbH

| Field | Value |
|---|---|
| **landing_url** | https://rtkdata.com/ca/ |
| **access_url** | Same; self-service activation (under 5 minutes per operator). |
| **host:port** | Server + port + `AUTO` mountpoint published post-signup; not on landing. |
| **num_stations** | 700+ reference stations CAN-wide (Halifax → Whitehorse, ~9.98 M km²; populated southern corridor, gaps >55°N). |
| **vrs** | Yes (`AUTO` mountpoint nearest-station selection). |
| **tariff** | USD 40/mo or USD 400/yr (~CAD 55 / CAD 550). 30-day free trial, no credit card. |
| **hobbyist_eligibility** | Yes — no professional gate; self-service. |
| **legal_residency_required** | No. |
| **datum_epoch** | NAD83(CSRS) (CGG2013 / HTv2.0 geoid; NATRF2022 adoption planned 2027) — operator declaration https://rtkdata.com/ca/ (epoch not separately published by operator). |
| **last_confirmed_alive** | 2026-05-17 (rtkdata.com/ca/ WebFetch 200; pricing + station-count + datum confirmed) |

Note: rtkdata.com is paid commercial sibling of free `rtkdata.online` (same parent Kansi Solutions GmbH); cross-ref `rtk_inventory.md` `rtkdata_online` entry.

---

### Rx Networks TruePoint FOCUS — Canadian-operated cloud RTK/PPP-RTK

| Field | Value |
|---|---|
| **landing_url** | https://rxnetworks.com/rx-networks-introduces-truepoint-focus-instantaneous-centimeter-level-accuracy/ |
| **access_url** | https://rxnetworks.com/request-a-free-trial · sales@rxnetworks.com |
| **host:port** | Not on public page; issued post-signup. NTRIP for RTK (OSR mode); SSR for PPP-RTK mode. |
| **num_stations** | North America + Europe + China cloud; aggregated station count not published. |
| **vrs** | Yes (RTK over RTCM v3 NTRIP); PPP-RTK SSR alternative. |
| **tariff** | 30-day complimentary trial; permanent tier quote-only. Hardware-agnostic. 99.9% SLA. |
| **hobbyist_eligibility** | Trial yes; permanent unclear (sales-routed). |
| **legal_residency_required** | No. |
| **datum_epoch** | omitted — no citable operator declaration (rxnetworks.com launch announcement does not state datum/epoch). |
| **last_confirmed_alive** | 2026-05-17 (rxnetworks.com launch announcement WebFetch 200; launched April 2025) |

---

### GEODNET — Decentralized RTK (Helium-style)

| Field | Value |
|---|---|
| **landing_url** | https://geodnet.com/ |
| **access_url** | https://store.geodnet.com (paid subscription); 30-day trial via https://geodnet.com/free. Listed on NRCan rtk.php data catalog (provider key `GEODNET`). |
| **host:port** | `rtk.geodnet.com:2101` (operator-published, canonical per rtk_inventory.md `geodnet_usa` + cached sourcetable) |
| **num_stations** | Decentralized; Canadian-side count not separately published. |
| **vrs** | Yes (`AUTO` mountpoint nearest-station synthesis). |
| **tariff** | USD 40/mo or USD 400/yr (store.geodnet.com 2026-05-17). 30-day free trial only; no permanent free tier. Networks.md `geodnet_usa` removed from free-source pipeline 2026-04-20. |
| **hobbyist_eligibility** | Yes (paid; self-service, no professional gate). 30-day trial available. |
| **legal_residency_required** | No. |
| **datum_epoch** | ITRF2014 / ITRF2020 / NATRF2022 (per cached sourcetable `AUTO_ITRF2014` / `AUTO_ITRF2020` / `NATRF2022` mountpoints, data/geodnet_usa.sourcetable); NAD83(CSRS) compliance per NRCan registry https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php?locale=en. |
| **last_confirmed_alive** | 2026-05-17 (geodnet.com WebFetch 200; store.geodnet.com pricing 200; NRCan registry reference) |

---

### Other (METACON / LATNET / DART / Skylark)

Out-of-scope quick-mention; not enough activity to warrant full block. Listed on NRCan rtk.php compliance registry as smaller VARs; all quote-only, no public host:port or pricing. Skylark (Swift Navigation): continental, USD 29–69/mo per Ardusimple 2026-05-17 (RTK + SSR). Not enumerated as full blocks — pipeline-irrelevant.

---

## Volunteer Coverage (free NTRIP usable by hobbyists)

Live counts (sourcetable probes 2026-05-17):

| Source | CAN total | Concentration |
|---|---|---|
| **rtk2go** | 68 (up from 64 on 2026-05-15) | AB ~16 (Calgary/Edmonton/farm corridor), ON ~14 (incl. GTA / Niagara), QC ~12, SK/MB ~8, Maritimes 2, BC 2 (fluffyYAQ ~48.81/-123.59, Nakusp1 ~50.24/-117.80), YT/NT/NU 0 |
| **Centipede** | 21 | QC 16, ON 5 — organic St. Lawrence corridor, French-speaking Centipede community |
| **EarthScope (NOTA)** | handful | IGS-grade northern Canada; non-commercial NULA, US-facing |
| **IGS-IP** | 32 CAN | Operational-research; not cm-level RTK |

Practical reading:
- AB / ON / southern QC: only regions where free NTRIP consistently within useful baseline (≤30 km) of populated areas.
- BC: 2 rtk2go bases only — Lower Mainland + Vancouver Island hobbyists outside reach forced to commercial VAR or self-host.
- Maritimes (2 rtk2go), Prairies interior (7 in SK/MB combined), territories (0): no usable free coverage.

Ottawa cross-check (`stations_by_radius.py 45.42 -75.69 200`, 2026-05-15): 7 rtk2go CAN bases ≤200 km (closest `CanalTerris` 6.8 km) + 4 Centipede nodes (1 US-tagged `RANG7` at 43.8 km nearest of any — cross-border, no functional impact).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| NRCan CSRS RINEX + CSRS-PPP | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/ | Free (registration) |
| CSRS-PPP web tool | https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php | Free |
| MRNF Quebec RINEX | https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/ | Free |
| Manitoba MSRN | Provincial portal | Free |
| Service NB | RINEX portal | Free |
| Nova Scotia (via NRCan) | RINEX | Free |
| SK ISC digital archive | RINEX | Free |
| ON COSINE | Control coords / archive | Free |
| GeoBC (BC) | FTP via GeoBCInfo@gov.bc.ca | Pay-per-download or subscription; BCeID required |

---

## Gaps & Observations

1. **No federal free real-time NTRIP exists.** CACS = post-processing / PPP only; 2013 NRCan/NGS shutdown gap unfilled; no replacement signalled 2026.
2. **NATRF2022 cutover begins early 2027** (federal); provinces ~2030. 1–2 m horizontal shift expected. Vendor problem on subscribed services; end-user problem only on self-hosted bases.
3. **Quebec is the only province with free real-time corrections** — but direct-TCP not NTRIP. Excludes stock rover firmware without TCP-socket / NTRIP-relay shim. Functionally a volunteer-network province for typical hobbyist.
4. **All other provinces outsource real-time to paid VARs.** Even where hardware (NSACS 40, BCACS 20, PE 8) is government-funded, streaming is monetised by SmartNet / Can-Net / BrandtNet / TopNET / TruePoint FOCUS under quote-only contracts (except SmartNet Atlantic + RTKdata.com, which publish prices).
5. **RTKdata.com is the only hobbyist-tier published-pricing commercial CA caster.** USD 40/mo · 700+ stations · self-service · 30-day no-CC trial · CAN-wide. Outranks every other commercial option for hobbyist economics, though pipeline-out-of-scope (paid).
6. **Volunteer networks are the only free NTRIP path for typical hobbyist.** rtk2go 68 + Centipede 21 ≈ 89 free CAN bases (2026-05-17). Practical baselines in AB, southern ON, southern QC; elsewhere no free RTK.
7. **Centipede CA footprint = 16 QC + 5 ON** — concentrated along southern St. Lawrence corridor, densest free-coverage zone when combined with rtk2go QC.
8. **CGRSC commercial-provider list updated Sept 2025**; content unchanged from 2021 (Leica SmartNet, Trimble Can-Net, Topcon TopNET, Lewis Instruments, Brandt BrandtNet). Lewis Instruments operator site 403 from sandbox — confirmation requires Canadian-IP probe.

---

## Regions Without Public Caster (Quick-Scan)

Quebec is the only province with free real-time corrections (direct-TCP, not NTRIP). Every other province / territory has no public caster — fallback is paid VAR, volunteer pool, or NRCan post-processing.

| Province / Territory | Situation | Best free fallback | Best paid fallback |
|---|---|---|---|
| BC | No public caster (municipal RTNs gated, BCACS RINEX-only) | rtk2go 2 bases (Lower Mainland + Vancouver Island) | Can-Net / SmartNet NA / BrandtNet (quote) |
| AB | No active provincial CORS (passive HPN only) | rtk2go ~16 bases (Calgary/Edmonton/farm corridor) | Can-Net / BrandtNet / SmartNet NA |
| SK | No provincial CORS (passive ISC Geomatics) | rtk2go ~4 (SK/MB combined ~8) | BrandtNet (Prairies-dominant) / Can-Net |
| MB | No provincial CORS (passive MSRN) | rtk2go ~4 (SK/MB combined ~8) | BrandtNet / Can-Net |
| ON | No provincial CORS (passive COSINE) | rtk2go ~14 (incl. GTA / Niagara) + Centipede 5 | Can-Net / SmartNet NA / TopNET |
| NB | No provincial caster (SNB RINEX-only) | rtk2go (Maritimes 2 total) | SmartNet NA Atlantic CAD 3,328/yr |
| NS | No provincial caster (NSACS hardware on commercial reseller stream) | rtk2go (Maritimes 2 total) | SmartNet NA Atlantic CAD 3,328/yr |
| PE | No provincial caster (8 ACS hardware on commercial stream) | rtk2go (Maritimes 2 total) | SmartNet NA Atlantic CAD 3,328/yr |
| NL | No provincial caster (passive monuments only) | None usable | SmartNet NA Atlantic CAD 3,328/yr (coastal); NRCan CSRS-PPP post-processing free |
| YT / NT / NU | No territorial operator; handful of NRCan CACS + EarthScope NOTA scientific sites | None practical | NRCan CSRS-PPP post-processing free (long-baseline only) |

---

## Sources Consulted (2026-05-17)

- NRCan RTK compliance map — https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/rtk.php?locale=en (static HTML empty; interactive JS-driven)
- NRCan municipal RTK — https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/data-donnees/municipal.php?locale=en
- NRCan CSRS landing — https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/canadian-spatial-reference-system-csrs
- NRCan NATRF2022 modernization — https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/canadian-spatial-reference-system-csrs-modernization
- CGRSC provincial networks — https://cgrsc.ca/resources/geodetic-control-networks/provincial-networks/
- CGRSC network RTK services (Sept 2025) — https://cgrsc.ca/resources/geodetic-control-networks/network-rtk-services/
- MRNF Québec GNSS — https://mrnf.gouv.qc.ca/repertoire-geographique/reseau-geodesique-donnees-gnss/
- MRNF Stations_GNSS.pdf — https://diffusion.mern.gouv.qc.ca/diffusion/RGQ/Documentation/Geodesie/Stations_GNSS.pdf
- BCACS — https://www2.gov.bc.ca/gov/content/data/geographic-data-services/geo-spatial-referencing/bcacs
- AB SPIN — https://alta.registries.gov.ab.ca/spinii/logon.aspx
- Ontario GNSS specification — https://www.ontario.ca/page/ontario-specification-global-navigation-satellite-systems-gnss-geodetic-control-surveys
- GeoNova NS — https://geonova.novascotia.ca/coordinate-referencing
- Can-Net — https://www.can-net.ca/
- HxGN SmartNet NA — https://www.smartnetna.com/ (302 → https://hxgnsmartnet.com/en-US)
- BrandtNet — https://rtk.brandt.ca/ + https://www.brandt.ca/Divisions/Positioning-Technology/Brandtnet/Brandtnet-Benefits
- TopNET Live — https://www.topnetlive.com/ (cert expired 2026-05-17)
- Lewis Instruments — http://www.lewisinstruments.com (403 from sandbox)
- RTKdata Canada — https://rtkdata.com/ca/ (price + station-count + datum confirmed 2026-05-17)
- Rx Networks TruePoint FOCUS launch — https://rxnetworks.com/rx-networks-introduces-truepoint-focus-instantaneous-centimeter-level-accuracy/
- GEODNET — https://geodnet.com/
- Ardusimple Canada caster review — https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-canada/
- NTRIP list North America — https://ntrip-list.com/north-america/
- Live caster probes 2026-05-17: rtk2go.com:2101 (CAN=68), caster.centipede.fr:2101 (CAN=21)
