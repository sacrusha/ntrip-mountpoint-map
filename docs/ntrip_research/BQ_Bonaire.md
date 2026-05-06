# Bonaire, Sint Eustatius, Saba [BQ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free public NTRIP via AGRS.BES (Kadaster NL / NSGI); 7 mountpoints across BES islands; no registration required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | NSGI (Nationaal Samenwerkingsverband voor de Geo-informatie-infrastructuur) / Kadaster |
| **host:port** | `ntrip.kadaster.nl:2101` (plain TCP) · `ntrip.kadaster.nl:443` (TLS) |
| **Network identifier** | AGRS.BES (sub-network of the main Kadaster caster) |
| **VRS** | No — individual physical station streams (single-base) |
| **tariff** | €0.00 — no registration required; fully anonymous access. Email as username is recommended (for outage notices) but not mandatory |
| **hobbyist_eligibility** | Yes — fully anonymous, no account required |
| **legal_residency_required** | No |
| **last_confirmed_alive** | `ntrip.kadaster.nl:2101` returned all 7 BES mountpoints in SOURCETABLE on 2026-05-06 (curl verified) |

## Mountpoints — AGRS.BES (7 streams)

| Mountpoint | Island | Format | Message types | Constellations | Receiver |
|---|---|---|---|---|---|
| `BON200BES0` | Bonaire | RTCM 3.3 | 1006(15), 1008(15), 1019, 1020, 1033(15), 1042, 1046, 1077(1), 1087(1), 1097(1), 1127(1) | GPS+GLO+GAL+BDS | STONEX SC2200 |
| `BONK00BES0` | Bonaire | RTCM 3.3 | 1006(15), 1008(15), 1013, 1019, 1020, 1033(15), 1042, 1045, 1046, 1077(1), 1087(1), 1097(1), 1127(1), 1230(15) | GPS+GLO+GAL+BDS | LEICA GR30 |
| `SABY0` | Saba | RTCM 3.1 | 1004(1), 1006(1), 1008(1), 1012(1), 1019(1), 1020(1), 1033(1), 1230(1) | GPS+GLO | SEPT POLARX5E (legacy stream) |
| `SABY00BES0` | Saba | RTCM 3.3 | 1006(1), 1008(1), 1019(1), 1020(1), 1033(1), 1042(1), 1045(1), 1046(1), 1077(1), 1087(1), 1097(1), 1127(1), 1230(1) | GPS+GLO+GAL+BDS | SEPT POLARX5E |
| `SABY00BES1` | Saba | RAW | SBF(1) | GPS+GLO+GAL+BDS | SEPT POLARX5E (Septentrio raw binary) |
| `SEUS0` | Sint Eustatius | RTCM 3.1 | 1004(1), 1006(15), 1007(15), 1012(1), 1013(60), 1033(15), 1230(5) | GPS+GLO | Legacy stream |
| `SEUS00BES0` | Sint Eustatius | RTCM 3.3 | 1006(1), 1008(1), 1019(1), 1020(1), 1033(1), 1042(1), 1045(1), 1046(1), 1075(1), 1085(1), 1095(1), 1125(1), 1230(1) | GPS+GLO+GAL+BDS | — |

**Coordinates:**
- Bonaire (BON200BES0 / BONK00BES0): 12.15°N 68.27°W
- Saba (SABY*): 17.65°N 63.22°W
- Sint Eustatius (SEUS*): 17.50°N 62.98°W

## Context Notes

- The BES islands (Bonaire, Sint Eustatius, Saba) are special municipalities of the Netherlands since 10 October 2010 ("10-10-10"). Since 1 January 2021 their cadastral organisations are part of Kadaster Netherlands. GNSS reference stations are operated by NSGI (partnership of Kadaster, Rijkswaterstaat, and Hydrographic Service of the Royal Netherlands Navy).
- All AGRS.BES streams are in the free anonymous tier alongside AGRS.NL mainland streams; the legal basis is the Tarievenregeling Kadaster BWBR0037196 art. 19 lid 4 (same as mainland).
- The two modern `00BES0` format mountpoints per island (RTCM 3.3 MSM) are the recommended streams for modern multi-constellation receivers. The legacy `0` suffix streams (SEUS0, SABY0) are maintained for backward compatibility.
- Single-base corrections only — no VRS product exists for BES islands. Given the small island areas (Bonaire ~294 km², Saba 13 km², Sint Eustatius 21 km²) a single station per island provides full coverage with short baselines.
- The Bonaire coordinate frame reference: an older local realisation "Bonaire 2004" (ITRF2000 at epoch 2001.00, within 0.1 m) is used for cadastral purposes; NSGI has published transformation parameters (BESTRANS2020) to convert between frames.
- **Aruba (AW)**, **Curaçao (CW)**, and **Sint Maarten (SX)** are separate countries/entities of the Kingdom of the Netherlands and are NOT covered by AGRS.BES. See `AW_Aruba.md` and `CW_Dutch_Caribbean.md`.

## Access

Connection using any NTRIP client:
- Host: `ntrip.kadaster.nl`
- Port: `2101` (unencrypted) or `443` (TLS)
- Username: any string or email address (no validation)
- Password: any string or blank
- Select mountpoint: e.g. `BONK00BES0` for Bonaire, `SABY00BES0` for Saba, `SEUS00BES0` for Sint Eustatius

## Sources Consulted
- NSGI real-time streams page: https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams (observed 2026-05-06)
- Kadaster NTRIP caster sourcetable (html): http://ntrip.kadaster.nl:2101/sourcetable.htm (curl verified 2026-05-06)
- Kadaster Bonaire cadastral office: https://kadorbonaire.com/ (observed 2026-05-06)
- Kadaster BES overview: https://bes.kadaster.nl/kadaster-bonaire (observed 2026-05-06)
- NSGI BESTRANS2020 coordinate transformation document: https://www.nsgi.nl/documents/1888506/69577825/BESTRANS2020_v230405.pdf (observed 2026-05-06)
- Tarievenregeling Kadaster BWBR0037196/2026-01-01: https://wetten.overheid.nl/BWBR0037196/2026-01-01
- NL_Netherlands.md (existing research — full Netherlands context)
- curl live probe of all 7 AGRS.BES mountpoints — confirmed present in sourcetable 2026-05-06
