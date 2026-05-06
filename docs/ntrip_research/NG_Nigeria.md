# Nigeria [NG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: CORS network exists (NIGNET / OSGOF); public NTRIP RTK service status UNCERTAIN

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unclear — NIGNET has had NTRIP implemented (BKG caster, documented in academic thesis); but public access reliability and current operational status are not confirmed |
| **Network name** | NIGNET (Nigerian Permanent GNSS Network) |
| **Operator** | Office of the Surveyor-General of the Federation (OSGOF) — osgof.gov.ng |
| **host:port** | Not publicly documented; test mountpoint CLBR used in academic testing; current public endpoint unknown |
| **tariff** | Not publicly documented; PayPal-integrated billing described in 2017 thesis |
| **hobbyist_eligibility** | Unclear — billing mechanism exists; open registration not confirmed |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | osgof.gov.ng confirmed reachable 2026-05-06; NTRIP sourcetable not independently probed |

## Most Recent Project Announcement

**2008:** NIGNET established by OSGOF as part of AFREF initiative, initially 15 stations.
**~2017:** University of Beira Interior (Portugal) thesis documented implementation of a BKG Standard NTRIP Caster on Linux for NIGNET, with a PHP/MySQL management system and PayPal payment integration. Test RTK surveys performed with Trimble R8 via mountpoint CLBR.

No more recent public announcement of expanded NTRIP services found as of 2026-05-06.

- OSGOF: https://osgof.gov.ng/
- NIGNET NTRIP thesis (UBI): https://ubibliorum.ubi.pt/handle/10400.6/5840
- NIGNET stability evaluation (DOAJ): https://doaj.org/article/5d416470808f4841bc1d945385f7b1b9
- Academia.edu paper on NIGNET RTK services: https://www.academia.edu/8484226/LEVERAGING_ON_GNSS_CONTINUOUSLY_OPERATING_REFERENCE_STATIONS_CORS_INFRASTRUCTURE_FOR_NETWORK_REAL_TIME_KINEMATIC_SERVICES_IN_NIGERIA_Ojigi_L_M

## Context Notes

- **Network size:** ~15 CORS stations across Nigeria (Abuja, Lagos, Kano, Port Harcourt, Enugu, Calabar, and others), established 2008–2015.
- **Infrastructure issues:** Academic evaluations note that NIGNET's adequacy "has been compromised by infrastructural failures and lack of continuity in data transmission." Station uptime and data quality are inconsistent.
- **NTRIP implementation:** A formal NTRIP system with user management and billing was built (~2017) as part of a thesis project. Whether this was deployed in production and whether it remains operational today is unclear; no public caster address has been published.
- **OSGOF website:** osgof.gov.ng is the official authority; no NTRIP service page or mount-point list is visible on the public site.
- **ArduSimple Nigeria page:** Notes Nigeria lacks a confirmed national RTK network visible to hobbyists; mentions Galileo HAS as alternative (https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-nigeria/).
- **Global commercial networks:** No Nigeria coverage confirmed for GEODNET, ONOCOY, Centipede-RTK, or PointOne as of research date.
- Practical workaround: Contact OSGOF directly (osgof.gov.ng) to enquire about NIGNET NTRIP access; deploy a local base for single-base RTK; use Galileo HAS / PPP for sub-metre work.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **NIGNET RINEX archive via OSGOF** — historical RINEX; availability and access procedure unclear; contact OSGOF | https://osgof.gov.ng/ | Unknown |
| **IGS / EarthScope archive** — ABUZ (Zaria) or other Nigerian IGS stations for post-processing | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account required) |

## Sources Consulted
- OSGOF official site (https://osgof.gov.ng/)
- UBI thesis on NIGNET NTRIP implementation (https://ubibliorum.ubi.pt/handle/10400.6/5840)
- UBI thesis PDF (https://ubibliorum.ubi.pt/server/api/core/bitstreams/ce626ddf-999d-4856-b4e0-fe03d329fffb/content)
- Academia.edu NIGNET RTK services paper (https://www.academia.edu/8484226)
- DOAJ NIGNET stability paper (https://doaj.org/article/5d416470808f4841bc1d945385f7b1b9)
- ResearchGate NIGNET map (https://www.researchgate.net/figure/The-Nigerian-Permanent-GNSS-Reference-Network-NIGNET_fig2_343040286)
- ArduSimple Nigeria (https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-nigeria/)
- RTK2GO monitor (monitor.use-snip.com) — no Nigeria mount points visible
- NTRIP-list.com — no Nigeria entries found
- GitHub mvarga1989 GNSS CORS list (https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks)
