# Namibia [NA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster; geodetic first-order network expanding; IGS archive only

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — no public host:port found in any directory, sourcetable, or academic reference |
| **Operator** | Surveyor General's Department (SGDN), Ministry of Agriculture, Water and Land Reform, Windhoek |
| **host:port** | Not publicly listed |
| **tariff** | n/a (no public service) |
| **hobbyist_eligibility** | n/a |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | n/a — no NTRIP service confirmed |

## Operator

**Surveyor General's Department (SGDN)**
Ministry of Agriculture, Water and Land Reform
Windhoek, Namibia

**African Geomatics** (private Windhoek firm) — carries out first-order geodetic densification under SGDN contract since ~2008; no known NTRIP service.

## Geodetic Infrastructure Context

- **First-order network:** Namibia divided into 15 project zones; first-order control stations in zones 1–10 constructed by 2010–2020 (zones 1–8 by 2012; zones 9–10 by 2020). African Geomatics (Windhoek) has been primary contractor.
- **IGS station:** WIND00NAM (Windhoek) — scientific archive station, data held at HartRAO data centre; not an RTK streaming caster.
- **SGDN GNSS RTK capability:** SGDN and private firms (e.g., African Geomatics with 4 RTK GNSS receivers) use base-and-rover setups for fieldwork; no networked VRS or CORS streaming service found.
- **CORS Map / GIM International:** Namibia appears as unmapped on GIM International's Africa CORS map — no catalogued public CORS caster.
- **AFREF:** WIND00NAM is the sole AFREF-affiliated station for Namibia; RINEX archive only, no real-time stream.
- **Country size:** ~824,000 km², sparse population — full national CORS coverage is a long-term infrastructure project.

## Negative Findings

- RTK2GO / Centipede: Zero NA mountpoints in any public sourcetable
- NTRIP-list.com Africa: Namibia not listed
- ArduSimple country directory: Namibia not listed with any NTRIP service
- mvarga1989 GNSS CORS list (GitHub): No Namibia NTRIP endpoint
- HartRAO data centre: WIND00NAM is archiving only; no NTRIP stream
- No public caster address found in any indexed source as of 2026-05-06

## Most Recent Project Reference

No public NTRIP launch announcement found. The most recent traceable public-domain reference is African Geomatics' ongoing first-order densification work (zones 9–10 completed ~2020). No SGDN press release or tender for a public NTRIP caster has been found.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **HartRAO / IGS** — WIND00NAM RINEX archive | https://www.hartrao.ac.za/geodesy/gnss.html | Free non-commercial (account may be required) |
| **IGS / EarthScope** — WIND station archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |

## Sources Consulted
- African Geomatics — geodetic surveys Namibia: https://www.africangeomatics.com/geodetic
- African Geomatics — projects page: https://www.africangeomatics.com/projects
- GIM International — AFREF 2000–2015: https://www.gim-international.com/content/article/development-between-2000-and-2015
- GIM International — CORS Map Africa: https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- GNSS Africa: https://www.gnss-africa.org/
- RTK2GO monitor (monitor.use-snip.com) — no NA mountpoints visible
- NTRIP-list.com/africa — Namibia not listed
- ArduSimple RTK correction services directory — Namibia not listed
- HartRAO geodesy pages — WIND00NAM archive confirmed, no NTRIP stream
