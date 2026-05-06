# Bangladesh [BD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — Survey of Bangladesh national NTRIP RTK caster (paid subscription); website accessible

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (government-operated; registration + subscription required) |
| **Operator** | Survey of Bangladesh (SoB), Ministry of Defence |
| **Network name** | Bangladesh National RTK Network |
| **host:port** | `202.40.181.3:8021` (registration portal; note non-standard port 8021) |
| **tariff** | Paid subscription; fee amount not publicly listed. Register via http://202.40.181.3:8021 |
| **hobbyist_eligibility** | Unclear — "not very user-friendly" per ArduSimple; registration open; no professional restriction stated |
| **legal_residency_required** | Unknown — no explicit restriction stated |
| **last_confirmed_alive** | SoB caster portal referenced as active (ArduSimple, Aug 2025); direct HTTP probe not executed |

## Most Recent Project Announcement

**Survey of Bangladesh NTRIP caster** — ArduSimple's Bangladesh page (Aug 2025) identifies the Survey of Bangladesh as operator and lists registration at `http://202.40.181.3:8021`. The page notes the "website may not be very user-friendly." This is a paid service; fee amount not published publicly. Coverage map and registration at the IP portal.

Source: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bangladesh/

## Context Notes

- **Survey of Bangladesh** (SoB) is the national mapping agency under the Ministry of Defence; it operates the national RTK NTRIP caster at `202.40.181.3:8021` (non-standard port). Registration and subscription required at http://202.40.181.3:8021. Fee undisclosed publicly.
- **SPARRSO** (Bangladesh Space Research and Remote Sensing Organization) has GNSS receivers for Earth observation but no NTRIP caster found.
- **BUET** (Bangladesh University of Engineering and Technology) has conducted GNSS accuracy research in Bangladesh; no public NTRIP caster operated by BUET was found.
- Bangladesh's flat, deltaic terrain makes high-precision surveying critical for flood management, land registration, and infrastructure — creating demand for RTK, but institutional capacity to operate a national NTRIP caster remains unconfirmed.
- The ArduSimple page's description ("register on the website or send an email") is consistent with a small-scale or pilot caster, possibly operated by an academic or professional institution, rather than a national publicly accessible service.
- RTK2go: no Bangladesh base stations confirmed.
- Practical alternative for hobbyists: GEODNET or Onocoy (coverage in BD not confirmed); Galileo HAS (~40 cm, no internet); own base-station setup.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **Survey of Bangladesh RTK caster** — registration portal (paid); coverage map on site | http://202.40.181.3:8021 | Paid subscription (fee unlisted) |
| **Survey of Bangladesh main site** | https://sob.gov.bd | — |
| **IGS/EarthScope archive** (any IGS stations in Bangladesh) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial |
| **SIRGAS / BKG** (not applicable; Bangladesh outside SIRGAS) | — | — |

## Sources Consulted
- ArduSimple Bangladesh page (operator, host:port confirmed): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-bangladesh/
- Survey of Bangladesh NTRIP portal: http://202.40.181.3:8021 (not directly probed 2026-05-06)
- Survey of Bangladesh official site: https://sob.gov.bd
- SPARRSO job circulars (referenced in search results; no GNSS caster content)
- BUET published research (referenced generically; no NTRIP caster paper found)
- rtcm-ntrip.org (no Bangladesh entries found)
- RTK2go monitor (monitor.use-snip.com — no BD stations visible)
- Generic NTRIP/RTK resources (emlid, swiftnav, pointonenav)
