# Liberia [LR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-verified; no 2025-2026 LR caster launch found. New finding: LibRef21 = Liberia Reference Frame 2021 is registered with EPSG as an active datum, EPSG revision date 2025-02-19; data source = Liberia Land Authority. Operator portal still does not publish CORS endpoints.)

## Status: NO — no public NTRIP RTK caster operating. National geodetic reference frame LibRef21 (LGR) is realised on paper; one private CORS announcement (Derks Surveying Solutions, June 2024) remains in planning.

| Field | Value |
|---|---|
| **landing_url** | https://lla.gov.lr (Liberia Land Authority; no NTRIP section) |
| **access_url** | n/a — no operational service |
| **Active public NTRIP RTK caster** | No |
| **host:port** | None found |
| **tariff** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster identified 2026-05-21 |
| **datum_epoch** | LibRef21 (Liberia Reference Frame 2021), GRS 1980 ellipsoid, EPSG:10799 — registered by Liberia Land Authority (LLA); no operator-published station coordinates or NTRIP caster yet (declaration is for the national frame; no live CORS broadcasting it). Source: https://epsg.io/10799 |

## Most Recent Project Announcement

- **14 June 2024 — Derks Surveying Solutions (DSS) CORS plan (announcement only)**: DSS (a Liberian-owned surveying firm established 2018, led by civil engineer / retired Air Force officer Solomon Vincent) announced via FrontPage Africa that it has purchased over USD 500,000 of optical + GNSS surveying equipment and "intends to work closely with local governmental agencies to establish Continuous Operating Reference Stations (CORS) as mandated by the United Nations Economic Commission for Africa (UNECA)" to contribute to the African Geodetic Reference Frame (AFREF). The project is in **announcement / planning phase**: no operational caster, no station list, no NTRIP endpoint as of 2026-05-12. DSS also describes a planned apprenticeship programme for Liberians aged 18–30 with emphasis on women, and is seeking collaboration with government ministries, the Liberia Land Authority, civil society and private sector.
  - Source: https://frontpageafricaonline.com/community-news/liberia-derks-surveying-solutions-seeks-collaborations-to-enhance-accuracy-in-surveying-purchases-over-500k-survey-equipment/ (14 June 2024)
- **February 2026 — LLA strategic planning retreat in Ganta**: brought together commissioners, directors and technical staff to plan strengthening of land governance; no specific CORS / GNSS deliverables announced in the public summary.

The **Liberia Land Authority** (LLA, `lla.gov.lr`), established under the Land Rights Act of 2018, is the national land administration body responsible for public surveying, cadastral mapping, and the national geodetic reference network. The LLA's Land Administration Department explicitly aims to ensure that all land parcels in Liberia reference the **Liberia Geodetic Reference frame (LGR)** for security of tenure, but no CORS station list, NTRIP service page, or public endpoint has been found on the LLA website or in any third-party geodetic resource.

The LLA concluded a training programme on drone technology for land surveying capability under the **Inclusive Land Administration and Management Project (ILAMP)** (World Bank-funded), but ILAMP deliverables identified in search results focus on land registration, not CORS/NTRIP infrastructure.

## Context Notes

- **National authority:** Liberia Land Authority (LLA) — `lla.gov.lr` / info@lla.gov.lr. Website is live and operational as of 2026-05-06. No geodetic data download or NTRIP service section found.
- **Liberia Geodetic Reference Frame (LGR / LibRef21):** Registered with EPSG as **LibRef21 = EPSG:10799** (active, ellipsoidal 3D, GRS 1980 ellipsoid, Greenwich prime meridian; area of use Liberia onshore + offshore). Source attribution: Liberia Land Authority (LLA). EPSG entry does not publish epoch year or explicit ITRS alignment. An older Liberian Geodetic Datum 2005 (LGD2005) is referenced in MLME concept papers as ITRS / GRS80 based. No operational CORS network is yet known to broadcast in LibRef21. Source: https://epsg.io/10799
- **AFREF participation:** Liberia is within the AFREF geographic scope for West Africa. Liberia does not appear in the published lists of countries with at least one AFREF-contributing CORS (approximately 22 countries as of the 2024 AFREF workshop). No GNSS station with country code LR has been found in HartRAO, EarthScope/IGS, or RCMRD archives.
- **Historical CORS procurement (pre-LLA):** A Ministry of Lands, Mines and Energy concept paper (Department of Lands, Surveys and Cartography) describes earlier work under the MCC Liberia Threshold Program: "some monuments have been planted and a set of CORS station[s] procured" toward re-establishing the National Geodetic Control Network. No public sourcetable or NTRIP endpoint emerged from that procurement; the hardware appears never to have come online as a public real-time service. Source: https://www.studocu.com/row/document/university-of-liberia/geomatics-engineering/concept-paper/5446378 (secondary; original LLA / MLME concept paper).
- **ILAMP project:** The World Bank-funded Inclusive Land Administration and Management Project is supporting LLA capacity; project documentation focuses on parcel registration and land governance, not geodetic CORS infrastructure.
- **No entries on rtk2go, Centipede or EarthScope:** Zero LR mountpoints in project pipelines (`py scripts/stations_by_country.py LBR` → empty 2026-05-21). Wider radius `py scripts/stations_by_radius.py 6.3 -10.8 800` returns 2 hits: Centipede `INP02` (Côte d'Ivoire, 6.873/-5.238) at 617.7 km and rtk2go `Gine-Albrk` (Guinea/Conakry) at 481.2 km — both far beyond RTK range (~30–40 km practical limit).
- **No entry on ntrip-list.com:** Liberia absent from ntrip-list.com Africa listing.
- **No commercial NTRIP providers found:** GEODNET, ONOCOY, PointOne, HxGN SmartNet — none list Liberia coverage.
- **Regional context:** Neighbouring Sierra Leone and Guinea also have no confirmed public caster. Côte d'Ivoire (to the east) and Senegal (further north-west) have isolated IGS sites but no public RTK service usable in LR. No cross-border RTK coverage applicable.
- **Practical hobbyist guidance:** Deploy a local GNSS base station for single-base RTK; use Galileo HAS / PPP for sub-metre work without connectivity. Galileo HAS (free, ~40 cm) is the realistic zero-cost option until either DSS or the LLA bring a national CORS online.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope / IGS RINEX archive** — no Liberia station identified; nearest qualifying stations are in Ghana or Senegal | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |

## Negative Findings

- AFREF station count (~22 contributing countries as of 2024): Liberia not included
- HartRAO GNSS archive: no LR station
- IGS network: no station with country code LR
- rtk2go monitor: zero LR mountpoints
- Centipede: zero LR nodes
- ntrip-list.com/africa: no Liberia entry
- GEODNET, ONOCOY, PointOne: no Liberia coverage
- LLA website (lla.gov.lr): no GNSS service, CORS station, or NTRIP endpoint documented

## Sources Consulted
- Liberia Land Authority — home: https://lla.gov.lr
- LLA Land Administration Department: https://lla.gov.lr/index.php/about-us/organizational-arrangements/land-administration-department
- LLA services overview: https://lla.gov.lr/index.php/services
- LLA Overview: https://www.lla.gov.lr/index.php/about-us/overview
- Derks Surveying Solutions CORS announcement (14 Jun 2024): https://frontpageafricaonline.com/community-news/liberia-derks-surveying-solutions-seeks-collaborations-to-enhance-accuracy-in-surveying-purchases-over-500k-survey-equipment/
- Devex — LLA profile (ILAMP context): https://www.devex.com/organizations/liberia-land-authority-liberia-128200
- Land Portal — LLA: https://landportal.org/organization/liberia-land-authority
- AFREF workshop 2024 (RCMRD): https://ric2024.rcmrd.org/afref
- AFREF background (UN-SPIDER): https://un-spider.org/space-application/space-application-matrix/african-geodetic-reference-frame-afref
- ntrip-list.com Africa: https://ntrip-list.com/africa/
- rtk2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
- Local pipeline check (2026-05-21): `py scripts/stations_by_radius.py 6.3 -10.8 800` → 2 stations (Centipede INP02 CIV 617.7 km; rtk2go Gine-Albrk GIN 481.2 km, status stale)
- EPSG LibRef21 entry: https://epsg.io/10799 (source: Liberia Land Authority)
