# Mexico [MX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-01

## Status: NO — national CORS network (INEGI RGNA) is post-processing only; no public NTRIP RTK caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — INEGI RGNA provides RINEX/PPK only, no real-time RTK stream |
| **host:port** | null |
| **tariff** | Free (RINEX/PPK only — RTK stream not offered) |
| **VRS** | N/A |
| **hobbyist_eligibility** | Yes (RINEX service is free, no registration required) |
| **legal_residency_required** | No |
| **last_confirmed_alive** | SFTP/FTP server confirmed reachable per INEGI documentation (2024-10); INEGI RGNA page observed 2026-05-01 |

## Context Notes

- **INEGI RGNA** (Red Geodésica Nacional Activa): Mexico's national CORS network operated by the Instituto Nacional de Estadística y Geografía. The network provides **post-processing only** via:
  - FTP: `ftp://geodesia.inegi.org.mx` (credentials: user `rgnaftp` / password `rgnaftp`)
  - SFTP: migration to SFTP was effective October 2024
  - Data: RINEX files at 15-second intervals, freely available for PPK use.
- INEGI's own English-language page confirms **no real-time RTK/NTRIP service** — corrections are RINEX files for post-processing only.
- A 2013 SIRGAS bulletin discussed aspirations for an INTRIP NTRIP caster for INEGI, but no live caster has been publicly documented.
- No commercial national NTRIP RTK service for Mexico was found as of 2026-05-01.
- Global commercial services (GEODNET, Trimble RTX, PointOne) may provide sparse coverage in urban Mexico but are not Mexico-specific networks.

## Most Recent Project / Announcement

No announced project to deploy a national NTRIP RTK caster in Mexico was found as of 2026-05-01. The 2024 SFTP migration is an infrastructure maintenance update, not a real-time service launch.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **INEGI RGNA** — RINEX download via FTP/SFTP | ftp://geodesia.inegi.org.mx (user: rgnaftp / pass: rgnaftp) | Free, no registration |
| **INEGI RGNA** — information page | https://en.www.inegi.org.mx/temas/geodesia_activa/ | Free |

## Sources Consulted
- INEGI RGNA English page: https://en.www.inegi.org.mx/temas/geodesia_activa/ (observed 2026-05-01)
- INEGI RGNA Spanish: https://geodesia.inegi.org.mx
- SIRGAS 2013 bulletin on INEGI NTRIP aspirations: sirgas.ipgh.org
