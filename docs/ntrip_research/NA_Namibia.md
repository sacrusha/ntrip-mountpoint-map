# Namibia [NA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; single physical CORS WIND00NAM0 is now confirmed live on BKG IGS-IP and AUSCORS as a real-time NTRIP stream — previous "RINEX-only" framing corrected)

## Status: NO Namibia-operated public NTRIP caster, BUT the IGS station WIND (Windhoek) is republished live on the BKG IGS-IP global caster and mirrored on AUSCORS — usable for free single-base RTK within ~30 km of Windhoek with a BKG NTRIP account (or AUSCORS registration).

| Field | Value |
|---|---|
| **Namibia-operated public NTRIP caster** | No — no NA-government host:port found in any directory, sourcetable, or academic reference |
| **Foreign-operated NTRIP streams covering NA** | Yes — `WIND00NAM0` (-22.57, 17.09, Windhoek IGS site; HartRAO contributes data) republished on `www.igs-ip.net:2101` (BKG IGS-IP) and `ntrip.data.gnss.ga.gov.au:2101` (AUSCORS rebroadcast). Single-base raw 1 Hz RTCM 3; full RTK effective ~30 km of Windhoek |
| **landing_url — BKG IGS-IP** | https://igs.bkg.bund.de/ntrip/ (BKG NTRIP service description) |
| **access_url — BKG IGS-IP** | https://igs.bkg.bund.de/ntrip/register (BKG NTRIP account registration) |
| **landing_url — AUSCORS** | https://gnss.ga.gov.au/stream (Geoscience Australia AUSCORS landing) |
| **access_url — AUSCORS** | https://gnss.ga.gov.au/registration (GA self-service registration, CC BY 4.0) |
| **num_stations** | 1 physical CORS visible to NA users (WIND00NAM0 in Windhoek) on both IGS-IP and AUSCORS; same physical station — count once. Snapshot 2026-05-17 via `py scripts/stations_by_country.py NAM`. |
| **datum_epoch** | omitted — IGS-IP / AUSCORS rebroadcast carries no Namibia-operator-side datum declaration; the Namibian Surveyor-General publishes no NTRIP caster and no citable real-time-stream datum/epoch statement. Per primer, do NOT infer ITRF/IGS from caster identity. |
| **Operator (national)** | Surveyor General's Department (SGDN), Ministry of Agriculture, Water and Land Reform, Windhoek |
| **Operator (data feed)** | HartRAO (Hartebeesthoek Radio Astronomy Observatory, ZAF) hosts WIND00NAM site; IGS rebroadcasts via BKG |
| **host:port — IGS-IP** | `www.igs-ip.net:2101` (mountpoint `WIND00NAM0`) |
| **host:port — AUSCORS mirror** | `ntrip.data.gnss.ga.gov.au:2101` (mountpoint `WIND00NAM0`) |
| **tariff (IGS-IP)** | Free; requires BKG NTRIP account (`igs.bkg.bund.de/ntrip/register`) |
| **tariff (AUSCORS)** | Free; CC BY 4.0; Geoscience Australia self-service registration (`gnss.ga.gov.au/registration`) |
| **hobbyist_eligibility** | Yes for both IGS-IP and AUSCORS (no surveyor licence required) |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-17 — WIND00NAM0 present in local data/igs_ip.sourcetable and data/auscors.sourcetable snapshots (see source_health.json). Radius probe `py scripts/stations_by_radius.py -22.5 17.1 1500` returns 55 stations across 6 sources, with WIND00NAM0 the only one inside Namibia |

## Operator

**Surveyor General's Department (SGDN)**
Ministry of Agriculture, Water and Land Reform
Windhoek, Namibia

**African Geomatics** (private Windhoek firm) — carries out first-order geodetic densification under SGDN contract since ~2008; no known NTRIP service.

## Geodetic Infrastructure Context

- **First-order network:** Namibia divided into 15 project zones; first-order control stations in zones 1–10 constructed by 2010–2020 (zones 1–8 by 2012; zones 9–10 by 2020). African Geomatics (Windhoek) has been primary contractor.
- **IGS station WIND00NAM:** Windhoek IGS site, hosted/maintained by HartRAO. **Confirmed real-time NTRIP stream** on both BKG IGS-IP (`www.igs-ip.net:2101`) and AUSCORS rebroadcast (`ntrip.data.gnss.ga.gov.au:2101`) as of 2026-05-17. This corrects prior "RINEX archive only" framing — the station has both archive RINEX and live RTCM 3 streaming.
- **SGDN GNSS RTK capability:** SGDN and private firms (e.g., African Geomatics with 4 RTK GNSS receivers) use base-and-rover setups for fieldwork; no Namibia-operated networked VRS or CORS caster service found.
- **CORS Map / GIM International:** Namibia appears as unmapped on GIM International's Africa CORS map — no Namibia-operated public CORS caster.
- **AFREF:** WIND00NAM is the sole AFREF-affiliated station for Namibia; real-time stream available via IGS-IP/AUSCORS.
- **Country size:** ~824,000 km², sparse population — WIND covers only Windhoek metro (~30 km); full national CORS coverage remains a long-term infrastructure project.

## Negative Findings

- RTK2GO / Centipede: Zero NA mountpoints in any public sourcetable (2026-05-17)
- NTRIP-list.com Africa: Namibia not listed as a national network
- ArduSimple country directory: Namibia not listed with any national NTRIP service
- mvarga1989 GNSS CORS list (GitHub): No Namibia-operated NTRIP endpoint
- No SGDN/Surveyor-General-operated public caster address found in any indexed source as of 2026-05-17

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
- HartRAO geodesy pages — WIND00NAM site information
- IGS network page: https://network.igs.org/WIND00NAM
- Local data: `py scripts/stations_by_country.py NAM` — WIND00NAM0 on igs_ip and auscors (2026-05-17 snapshot); `py scripts/stations_by_radius.py -22.5 17.1 1500` — 55 stations within 1500 km across 6 sources, WIND00NAM0 the only NA station
