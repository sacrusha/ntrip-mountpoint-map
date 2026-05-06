# Myanmar [MM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster (CORS introduction ceremony documented; stream unconfirmed)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — CORS launched internally; no public endpoint documented |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no public service confirmed |
| **legal_residency_required** | null — no public service confirmed |
| **last_confirmed_alive** | null — no public NTRIP stream confirmed at any date |

## Most Recent Project Announcement

- **Undated (circa 2018–2021):** Myanmar's Department of Survey (surveydepartment.gov.mm) held an "Introduction of GNSS CORS Network Application Ceremony," indicating that CORS infrastructure has been officially launched for internal government use. No date or NTRIP endpoint was published externally.
- No subsequent public announcement of an NTRIP RTK service for external users has been found in English-language or Burmese-language searches as of 2026-05-06.
- Myanmar Survey Department website: http://www.surveydepartment.gov.mm/eng/ (accessibility may be intermittent given the political situation since 2021).

## Context Notes

- Myanmar's Department of Survey (Ministry of Natural Resources and Environmental Conservation) is the mandated agency for geodetic CORS and GPS control stations. The department has documented GPS control station establishment and maintenance as one of its core functions.
- The political crisis beginning in February 2021 has significantly disrupted government services and internet connectivity in Myanmar; any pre-existing NTRIP infrastructure may be inaccessible or non-operational.
- No commercial CORS/RTK network for Myanmar was found in any surveying industry or hobbyist source.
- Global commercial networks (GEODNET, ONOCOY, PointOne, Centipede): no Myanmar coverage confirmed.
- Any regional IGS stations in or near Myanmar for scientific purposes: specific 4-character station IDs not confirmed via web research (2026-05-06); check https://network.igs.org/ filtering by Myanmar.
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS, NRCAN PPP).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope/GAGE archive** — regional IGS-affiliated stations (limited in Myanmar) | https://www.unavco.org/data/gps-gnss/ | Free non-commercial |

## Sources Consulted
- Myanmar Survey Department: http://www.surveydepartment.gov.mm/eng/
- ArduSimple country RTK list (Myanmar not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2go monitor (no Myanmar stations observed)
- mvarga1989 GitHub GNSS CORS networks list (Myanmar not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- GEODNET (no Myanmar coverage)
- EarthScope/GAGE (scientific stations only)
