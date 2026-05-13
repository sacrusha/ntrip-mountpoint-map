# Pakistan [PK] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh; prior pass 2026-05-06)

## Status: NO national public NTRIP caster — single rtk2go community station (Karachi) is the only known free real-time path

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (national)** | No — no publicly documented government NTRIP endpoint |
| **Community real-time stream** | 1 rtk2go mountpoint: `Stingray_tech` (24.89°N, 67.09°E, Karachi area) — confirmed in `data/stations.json` via `scripts/stations_by_country.py PAK` 2026-05-12 |
| **host:port — national** | null |
| **host:port — rtk2go** | `rtk2go.com:2101` (mountpoint `Stingray_tech`) |
| **tariff — national** | null |
| **tariff — rtk2go** | Free (community-hosted; operator-set; rtk2go terms apply — reservation message required) |
| **hobbyist_eligibility** | rtk2go: yes (open community caster). No national service to evaluate. |
| **legal_residency_required** | rtk2go: no. No national service to evaluate. |
| **last_confirmed_alive** | No national caster confirmed at any date. `Stingray_tech` present in the latest rtk2go ingestion in `data/stations.json` (the project pipeline fetches rtk2go and surfaces only currently-broadcasting bases). |

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
- **rtk2go**: 1 active mountpoint `Stingray_tech` in Karachi (24.89°N, 67.09°E). Useful only for users within ~30 km of central Karachi. No other PK rtk2go stations.
- **Centipede / EarthScope**: no PK-tagged mountpoints (`scripts/stations_by_country.py PAK` 2026-05-12).
- Practical workaround for hobbyists outside Karachi: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS, NRCAN PPP, ISRO NavIC-based PPP services for the region).

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
- RTK2go monitor (1 Pakistan mountpoint `Stingray_tech` near Karachi, confirmed via `scripts/stations_by_country.py PAK` 2026-05-12)
- GEODNET (no Pakistan coverage confirmed)
- Local pipeline check `scripts/stations_by_country.py PAK` (2026-05-12): rtk2go = 1 (Stingray_tech), centipede = 0, earthscope = 0
