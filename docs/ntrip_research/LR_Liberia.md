# Liberia [LR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no public NTRIP RTK caster found; national geodetic reference frame (LGR) under development

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | None found |
| **tariff** | N/A |
| **hobbyist_eligibility** | N/A |
| **legal_residency_required** | N/A |
| **last_confirmed_alive** | N/A — no caster identified |

## Most Recent Project Announcement

No CORS or NTRIP project announcement found for Liberia as of 2026-05-06.

The Liberia Land Authority (LLA, `lla.gov.lr`), established under the Land Rights Act of 2018, is the national land administration body responsible for public surveying, cadastral mapping, and the national geodetic reference network. The LLA's Land Administration Department explicitly aims to ensure that all land parcels in Liberia reference the **Liberia Geodetic Reference frame (LGR)** for security of tenure, but no CORS station list, NTRIP service page, or public endpoint has been found on the LLA website or in any third-party geodetic resource.

The LLA concluded a training programme on drone technology for land surveying capability under the **Inclusive Land Administration and Management Project (ILAMP)** (World Bank-funded), but ILAMP deliverables identified in search results focus on land registration, not CORS/NTRIP infrastructure.

## Context Notes

- **National authority:** Liberia Land Authority (LLA) — `lla.gov.lr` / info@lla.gov.lr. Website is live and operational as of 2026-05-06. No geodetic data download or NTRIP service section found.
- **Liberia Geodetic Reference Frame (LGR):** The LGR is the stated national datum target; its realisation through CORS is implied but no station coordinates, baselines, or operational CORS installations have been published externally.
- **AFREF participation:** Liberia is within the AFREF geographic scope for West Africa. Liberia does not appear in the published lists of countries with at least one AFREF-contributing CORS (approximately 22 countries as of the 2024 AFREF workshop). No GNSS station with country code LR has been found in HartRAO, EarthScope/IGS, or RCMRD archives.
- **ILAMP project:** The World Bank-funded Inclusive Land Administration and Management Project is supporting LLA capacity; project documentation focuses on parcel registration and land governance, not geodetic CORS infrastructure.
- **No entries on rtk2go or Centipede:** Zero LR mountpoints in either public sourcetable.
- **No entry on ntrip-list.com:** Liberia absent from ntrip-list.com Africa listing.
- **No commercial NTRIP providers found:** GEODNET, ONOCOY, PointOne, HxGN SmartNet — none list Liberia coverage.
- **Regional context:** Neighbouring Sierra Leone and Guinea also have no confirmed public caster. No cross-border RTK coverage applicable.
- **Practical hobbyist guidance:** Deploy a local GNSS base station for single-base RTK; use Galileo HAS / PPP for sub-metre work without connectivity.

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
- Devex — LLA profile (ILAMP context): https://www.devex.com/organizations/liberia-land-authority-liberia-128200
- Land Portal — LLA: https://landportal.org/organization/liberia-land-authority
- AFREF workshop 2024 (RCMRD): https://ric2024.rcmrd.org/afref
- AFREF background (UN-SPIDER): https://un-spider.org/space-application/space-application-matrix/african-geodetic-reference-frame-afref
- ntrip-list.com Africa: https://ntrip-list.com/africa/
- rtk2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101
