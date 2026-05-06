# Pakistan [PK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO confirmed public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — no publicly documented NTRIP endpoint found |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service confirmed |
| **legal_residency_required** | null — no service confirmed |
| **last_confirmed_alive** | null — no public caster confirmed at any date |

## Most Recent Project Announcement

- **2024–2025 (SUPARCO):** Pakistan's national space agency SUPARCO is developing the Pak-SBAS (Satellite-Based Augmentation System) for sub-metre accuracy, with an indigenous receiver unveiled at the 2025 Cholistan Rally field trials. Production scaling and government agency delivery expected before end of 2026. Note: SBAS provides sub-metre accuracy only — not RTK-grade centimetre corrections, and out of scope for this project.
- **2024:** Pakistan's National Space Policy approved, mandating SUPARCO as the national space agency for all space-related activities, including GNSS infrastructure. No public CORS/NTRIP RTK service announced under this policy.
- **Survey of Pakistan (SoP):** The national mapping agency (surveyofpakistan.gov.pk) has listed procurements for GNSS RTK equipment but no public NTRIP caster service has been published.
- No named national CORS network (e.g., Pak-CORS, PCORS, PAKOR) found in any geodetic or surveying press source.

## Context Notes

- Pakistan has no confirmed national public NTRIP RTK network as of 2026-05-06. ArduSimple does not list Pakistan in its country-by-country RTK correction services directory.
- The Survey of Pakistan is the principal government agency for geodetic surveying. Its website (surveyofpakistan.gov.pk) lists procurement activities but no GNSS correction streaming service.
- SUPARCO operates scientific GNSS reference stations for space weather and positioning research, not a public RTK corrections service.
- IGS station KARR (Karachi) provides long-running geodetic data for post-processing, not real-time RTK.
- No commercial CORS/RTK network has been identified for Pakistan in any surveying industry or hobbyist source.
- Global commercial networks (GEODNET, ONOCOY, PointOne): no Pakistan coverage confirmed as of research date.
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS, NRCAN PPP, ISRO NavIC-based PPP services for the region).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS / EarthScope archive** — KARR station (Karachi); archival RINEX | https://www.unavco.org/data/gps-gnss/ | Free non-commercial |
| **IGS data centre (BKG)** — global reference frames including Pakistani stations | https://igs.bkg.bund.de/ | Free |

## Sources Consulted
- Survey of Pakistan: http://www.surveyofpakistan.gov.pk/
- SUPARCO: https://en.wikipedia.org/wiki/SUPARCO
- corsstations.com — "Pakistan Debuts Indigenous Pak SBAS Receiver" (2025): https://corsstations.com/news/pakistan-debuts-indigenous-pak-sbas-receiver-with-sub-meter-gnss-accuracy-during-cholistan-rally-field-trials/
- ArduSimple country RTK list (Pakistan not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- mvarga1989 GitHub GNSS CORS networks list (Pakistan not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- RTK2go monitor (no Pakistan stations observed)
- GEODNET (no Pakistan coverage confirmed)
