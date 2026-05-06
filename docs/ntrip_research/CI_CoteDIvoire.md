# Côte d'Ivoire [CI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: CORS infrastructure exists; no confirmed public NTRIP endpoint

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — CORS network (RECI, 5 stations) is operational; no public host:port has been published |
| **host:port** | unknown — not published; likely requires institutional registration |
| **tariff** | unknown |
| **hobbyist_eligibility** | unclear — CORS access appears to be restricted to government and professional users |
| **legal_residency_required** | unclear |
| **last_confirmed_alive** | RECI network confirmed operational in September 2025 conference presentation; no NTRIP sourcetable probe possible without a disclosed host:port |

## Most Recent Project Announcement

**September 2025 — "Le Réseau Géodésique de la Côte d'Ivoire" (Fernand BALE, Director CIGN)**: A presentation delivered at the Francophone surveyors congress (Fédération des géomètres francophones, Abidjan, 3–5 September 2025) describes Côte d'Ivoire's four-tier geodetic network:

- **RECI** (Réseau CORS Ivoirien): 5 permanent GNSS stations plus 1 IGS station — the active continuous-operation tier
- **RGIR** (Réseau Géodésique de Référence Ivoirien): 43 markers at ~1 point/100 km, established 1998; includes a permanent station at Yamoussoukro
- **RGIO** (Réseau Géodésique Opérationnel Ivoirien): 716 markers
- **RGID** (Réseau Géodésique de Détail Ivoirien): densification tier

The presentation confirms that RECI CORS stations have been deployed and are "significantly reducing time and errors in land demarcation operations." It does not publish a caster host:port or describe public NTRIP access.

Source: https://www.geometres-francophones.org/5e8sef5sdgf/uploads/2025/09/S3-2_BALE.pdf

**Toposat / BNETD-CIGN CORS deployment**: Toposat (a French GNSS/drone survey company) supported BNETD-CIGN (Bureau National d'Études Techniques et de Développement — Centre d'Information Géographique National) in establishing the 5-station RECI CORS network. The project involved "project management and supervision of the improvement and modernization of Ivory Coast's geodetic infrastructure."

Source: https://toposat.com/modernization-of-the-geodetic-infrastructure-of-ivory-coast/?lang=en

**CNTIG** (Comité National de Télédétection et d'Information Géographique) is described as "a central actor in modernising public action" with a GIS/remote sensing mandate linked to national development plans, but is not the operator of the CORS network (that role sits with BNETD-CIGN).

Source: https://cntig.net/ · https://www.linkedin.com/company/cntig

**AFREF Workshop 2024**: Côte d'Ivoire is listed among the ~22 African countries confirmed to have at least one operational CORS installation — consistent with the RECI network.
URL: https://ric2024.rcmrd.org/afref

## Context Notes

- **RECI is operational, but access is opaque**: Five CORS stations are confirmed as deployed and in use for professional survey work. However, no public NTRIP caster URL, port, or registration portal has been found in any public source. Access appears to be provided through institutional channels within BNETD-CIGN and/or government survey agencies.
- **Centipede-RTK**: ~2 volunteer nodes with country code `CIV` appear in the Centipede sourcetable — these are independent of the government RECI network and provide limited geographic coverage.
- **RTK2go**: Zero CI government mountpoints in the sourcetable.
- **IGS station**: One IGS-affiliated station is referenced in the RECI tier description (consistent with the ABID station historically listed for Abidjan in some IGS lists).
- **ArcGIS Open Data**: The RGCI (Réseau Géodésique de Côte d'Ivoire) marker dataset is published on ArcGIS for post-processing reference:
  - https://cotedivoire.africageoportal.com/items/004575bd810f47b39e7e4f0f3d73f885
- **Global commercial networks**: GEODNET, ONOCOY, PointOne — no CI coverage identified as of 2026-05-06.
- **Hobbyist path**: Centipede volunteer nodes (code `CIV`) provide some RTK access; a local base station is the fallback. Contact BNETD-CIGN directly to enquire about institutional RECI access.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **RGCI marker dataset (ArcGIS Open Data)** — static network point coordinates for post-processing reference | https://cotedivoire.africageoportal.com/items/004575bd810f47b39e7e4f0f3d73f885 | Free (open data) |
| **EarthScope GNSS Data Archive** — any IGS-affiliated Abidjan station data | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |
| **Centipede-RTK** — ~2 volunteer nodes (CIV) | https://caster.centipede.fr:2101 | Free / open |

## Sources Consulted
- FGF 2025 congress presentation — "Le Réseau Géodésique de la Côte d'Ivoire" (Fernand BALE): https://www.geometres-francophones.org/5e8sef5sdgf/uploads/2025/09/S3-2_BALE.pdf
- Toposat — Modernisation of geodetic infrastructure of Ivory Coast: https://toposat.com/modernization-of-the-geodetic-infrastructure-of-ivory-coast/?lang=en
- CNTIG official site: https://cntig.net/
- ArcGIS Africa GeoPortal — RGCI dataset: https://cotedivoire.africageoportal.com/items/004575bd810f47b39e7e4f0f3d73f885
- ArcGIS — RGCI map: https://www.arcgis.com/home/item.html?id=3c9985b3d6ae45b0aff6f818109d89ba
- AFREF 2024 Workshop / RCMRD: https://ric2024.rcmrd.org/afref
- IGS network (network.igs.org) — searched for CI/Abidjan
- RTK2go sourcetable — 0 CI government mountpoints
- Centipede-RTK sourcetable — ~2 CIV nodes (volunteer)
- GitHub mvarga1989 CORS list — checked for CI entries
- ntrip-list.com/africa/ — no CI government caster listed
