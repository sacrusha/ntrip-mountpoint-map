# Bahrain [BH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster; CORS infrastructure exists under SLRB; access restricted; territory tiny (~765 km²)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No confirmed public endpoint |
| **host:port** | null — not published |
| **tariff** | null — not applicable (licensed surveyors only) |
| **hobbyist_eligibility** | No — access restricted to licensed surveyors/contractors |
| **legal_residency_required** | Unclear — no individual registration path found |
| **last_confirmed_alive** | null — no public NTRIP stream confirmed at any date |

---

## Service Details

### SLRB Infrastructure

The **Survey and Land Registration Bureau (SLRB)** (`slrb.gov.bh`) is the government body responsible for geodetic infrastructure, cadastral surveying, and property registration in the Kingdom of Bahrain. SLRB manages:

- **BGD2000** — Bahrain Geodetic Datum 2000 (national horizontal datum)
- CORS reference stations (number not publicly disclosed; given Bahrain's ~765 km² total area, a single well-sited station would suffice for national RTK coverage)
- Hydrographic survey services
- Land and property registration

**Access policy:** Corrections are restricted to licensed surveyors and SLRB-contracted entities. No public NTRIP caster host:port has been published. No individual or hobbyist registration path has been identified.

### Territory Context

Bahrain is the smallest country in the Gulf and the Arab world (~765 km² total, ~60 km from north to south). Its small territory means even a single CORS station would theoretically cover the entire kingdom within typical RTK baseline limits (~30 km). Despite this trivial infrastructure requirement, no public NTRIP stream has been opened.

### ArduSimple Bahrain Page

ArduSimple maintains a page (`ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kingdom-of-bahrain/`) but based on search result excerpts it follows the same pattern as other Gulf pages: mentions Bahrain's national RTK network but lists no hobbyist-accessible NTRIP endpoint with credentials. The page recommends Galileo HAS (40 cm, free, global) as the fallback for users who cannot access the national network.

---

## Commercial Alternatives

No independent commercial NTRIP provider with confirmed Bahrain coverage has been identified. Global networks (GEODNET, PointOne, HxGN SmartNet, ONOCOY) do not list Bahrain in coverage maps from public documentation.

**KSA-CORS spill:** KSA-CORS stations near Dammam/Al-Ahsa (Eastern Province, Saudi Arabia) are approximately 25–50 km from Bahrain Island. KSA-CORS VRS *may* provide marginal RTK coverage in Bahrain — especially in the northern Manama/Muharraq area — but this is unconfirmed, and KSA-CORS has reachability issues from non-SA IPs (see SA_SaudiArabia.md).

Global free fallback: **Galileo HAS** (~40 cm accuracy, no connectivity required, globally available including Bahrain).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SLRB** — no public RINEX download portal identified | https://www.slrb.gov.bh/ | Contact required |
| **IGS / EarthScope** — check for any IGS station in Bahrain | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

---

## Negative Findings

- SLRB: no public NTRIP host:port published
- rtk2go: zero BH mountpoints
- Centipede: zero BH nodes
- GEODNET, PointOne, HxGN SmartNet: no Bahrain coverage confirmed in public documentation
- No commercial alternative NTRIP provider for Bahrain identified
- No open-access announcement from SLRB found in 2024–2026 sources

---

## Sources Consulted
- Investigation notes next.txt entry 84 (project internal)
- country-survey.md entry `BH — Bahrain` (project internal, date_added 2026-04-28)
- SLRB official site: https://www.slrb.gov.bh/en/
- Bahrain national portal — SLRB listing: https://www.bahrain.bh/wps/portal/en/BNP/GSX-UI-AllEntities/GSX-UI-EntityDetails?entityID=4
- ArduSimple Bahrain NTRIP page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kingdom-of-bahrain/
- SA_SaudiArabia.md — KSA-CORS context (project internal)
- mvarga1989 GitHub — community CORS/RTK networks list (Bahrain not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
