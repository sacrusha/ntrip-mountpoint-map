# Burundi [BI] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06
**Note:** "BI — IG" refers to IGEBU (Institut Géographique du Burundi), the national geographic institute.

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no caster has ever been confirmed alive |

## Most Recent Project Announcement

None found. **RCMRD AFREF capacity-building workshop** (August 12–15, 2024) included Burundi but announced no operational caster.
URL: https://ric2024.rcmrd.org/afref

## National Mapping Agency

**IGEBU** (Institut Géographique du Burundi) — https://www.igebu.bi/
Established 1980 (Decree 100/146). Departments: Cartography & Topography, Hydrometeorology & Hydrogeology, Administrative & Financial.
- JICA partnership since 2009: updating cartography of Bujumbura and Gitega using GPS, remote sensing, GIS — no CORS/NTRIP deployment announced.
- No GNSS network or RTK services listed on website.

## Context Notes

- **No known GNSS CORS station** in Burundi in any registry: IGS network (0 results for BI), SONEL, AFREF, EarthScope/GAGE, community lists.
- **Geodetic status**: Active datum still Arc 1960 (Clarke 1880 ellipsoid) — not yet modernised to a GNSS-based national reference frame. Ground control marks largely no longer visible in field (per 2016 academic paper).
- **RCMRD**: Burundi is one of 20 RCMRD member states; RCMRD CORS portal (corsdata.rcmrd.org) is behind Leica SBC login — no Burundi-specific content accessible.
- **Rwanda** (neighbour): Has 8-station Rwanda GeoNet CORS network. Burundi has nothing equivalent.
- Global commercial networks (GEODNET, ONOCOY, Centipede-RTK, RTKdata): No Burundi coverage.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **RCMRD CORS data portal** — Burundi is an RCMRD member state; if a station is connected, RINEX may be accessible via the login-gated Leica SBC portal | https://corsdata.rcmrd.org/sbc | Unknown — login required; contact rcmrd@rcmrd.org |

## Contact for Status Enquiries
- IGEBU Cartography & Topography Dept: igebu.bi
- RCMRD (AFREF/CORS programme): rcmrd@rcmrd.org

## Sources Consulted
- IGS network.igs.org — 0 results for BI
- RTK2GO, SONEL, AFREF (UN-SPIDER)
- RCMRD (corsdata.rcmrd.org, rcmrd.org)
- IGEBU website (igebu.bi)
- GitHub mvarga1989 CORS list
- GIM International CORS Africa map
- SCIRP 2016 geodetic datum transformation paper for Burundi
