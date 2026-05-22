# Bonaire, Sint Eustatius, Saba [BQ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-probed; prior: 2026-05-15)

## Status: YES — free public NTRIP via AGRS.BES (Kadaster NL / NSGI); 7 mountpoints across the three BES islands; fully anonymous access

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | NSGI (partnership of Kadaster, Rijkswaterstaat, Hydrographic Service of the Royal Netherlands Navy) — caster run by Kadaster Nederland |
| **landing_url** | https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams |
| **access_url** | https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams |
| **host:port** | `ntrip.kadaster.nl:2101` (plain TCP) · `ntrip.kadaster.nl:443` (TLS) |
| **Network identifier** | AGRS.BES (sub-network on the shared Kadaster caster) |
| **num_stations** | 4 physical CORS (Bonaire ×2 collocated independent receivers at one monument, Saba ×1, Sint Eustatius ×1) feeding 7 streams |
| **vrs** | No — single-base only; one stream per physical receiver, no network solution for BES |
| **tariff** | €0.00, no VAT applicable. NSGI page (Dutch, observed 2026-05-21): *"De real-time data van onderstaande GNSS-stations is gratis: GNSS-stations van het AGRS.NL de GNSS-stations op de Noordzee de GNSS-stations op de BES-eilanden"*. Legal basis: Tarievenregeling Kadaster BWBR0037196 art. 19 lid 4 (effective 2026-01-01) — *"De ruwe data van stations die deel uitmaken van het AGRS.NL, evenals de ruwe GNSS-data met een waarnemingsinterval van één seconde, zijn kosteloos beschikbaar."* The 2026 Tarieven-Kadaster-BES PDF lists no NTRIP line — service remains under the free tier. |
| **hobbyist_eligibility** | Yes — fully anonymous, no account required |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-21 — `curl --http0.9 http://ntrip.kadaster.nl:2101/` returned all 7 BES streams under network `AGRS.BES`, country `BES` |
| **datum_epoch** | Per-island, per NSGI BESTRANS2020 v230405: Bonaire on **"Bonaire 2004" = ITRF2000 @ epoch 2001.00** (within 0.1 m); Saba and Sint Eustatius on **ITRF2014** (dynamic; document recommends epoch 2020.00 for static GIS use, aligning with the planned CATRF2022 frame). Source: https://www.nsgi.nl/documents/1888506/69577825/BESTRANS2020_v230405.pdf |

## Mountpoints — AGRS.BES (7 streams, sourcetable verified 2026-05-21)

| Mountpoint | Island | Format | Message types (interval s) | Constellations | Receiver | Lat / Lon |
|---|---|---|---|---|---|---|
| `BON200BES0` | Bonaire | RTCM 3.3 | 1006(15), 1008(15), 1019, 1020, 1033(15), 1042, 1046, 1077(1), 1087(1), 1097(1), 1127(1) | GPS+GLO+GAL+BDS | STONEX SC2200 | 12.15, -68.27 |
| `BONK00BES0` | Bonaire | RTCM 3.3 | 1006(15), 1008(15), 1013, 1019, 1020, 1033(15), 1042, 1045, 1046, 1077(1), 1087(1), 1097(1), 1127(1), 1230(15) | GPS+GLO+GAL+BDS | LEICA GR30 | 12.15, -68.27 |
| `SABY0` | Saba | RTCM 3.1 | 1004(1), 1006(1), 1008(1), 1012(1), 1019(1), 1020(1), 1033(1), 1230(1) | GPS+GLO | SEPT POLARX5E (legacy stream) | 17.65, -63.22 |
| `SABY00BES0` | Saba | RTCM 3.3 | 1006(1), 1008(1), 1019(1), 1020(1), 1033(1), 1042(1), 1045(1), 1046(1), 1077(1), 1087(1), 1097(1), 1127(1), 1230(1) | GPS+GLO+GAL+BDS | SEPT POLARX5E | 17.65, -63.22 |
| `SABY00BES1` | Saba | RAW (Septentrio SBF) | SBF(1) | GPS+GLO+GAL+BDS | SEPT POLARX5E | 17.65, -63.22 |
| `SEUS0` | Sint Eustatius | RTCM 3.1 | 1004(1), 1006(15), 1007(15), 1012(1), 1013(60), 1033(15), 1230(5) | GPS+GLO | SEPT POLARX5 (legacy stream) | 17.50, -62.98 |
| `SEUS00BES0` | Sint Eustatius | RTCM 3.3 | 1006(1), 1008(1), 1019(1), 1020(1), 1033(1), 1042(1), 1045(1), 1046(1), 1075(1), 1085(1), 1095(1), 1125(1), 1230(1) | GPS+GLO+GAL+BDS | SEPT POLARX5 | 17.50, -62.98 |

All streams: NMEA=0, Solution=0 (physical base, not VRS), Auth=N (none), Fee=N. Carrier = L1+L2 (Carrier field "2" in sourcetable).

## Context Notes

- The BES islands (Bonaire, Sint Eustatius, Saba) are special municipalities of the Netherlands since 10 October 2010 ("10-10-10"). Since 1 January 2021 their cadastral organisations have been part of Kadaster Nederland. NSGI is the umbrella partnership that operates the GNSS reference infrastructure (Kadaster + Rijkswaterstaat + Dienst der Hydrografie of the Royal Netherlands Navy).
- Bonaire collocation note: `BON200BES0` (STONEX SC2200) and `BONK00BES0` (LEICA GR30) share identical sourcetable coordinates (12.15, -68.27). Two different receiver brands at one site is most consistent with two independent receivers (each on its own antenna) installed for redundancy / cross-checking. NSGI station-information page does not enumerate per-station antenna sharing, so independence is inferred from receiver-brand difference, not operator-confirmed.
- Free anonymous tier: username/password not required. NSGI recommends entering an email address in the username field (only) so they can notify operators of outages and changes — entirely optional.
- Modern multi-constellation receivers should connect to the `…00BES0` (RTCM 3.3 MSM) streams. The legacy `0` streams (`SABY0`, `SEUS0`) are RTCM 3.1 for backward compatibility with older clients. `SABY00BES1` is different — a raw Septentrio SBF (binary) stream intended for Septentrio post-processing tools and research use, not a legacy RTCM stream.
- Single-base only — there is no VRS / network-RTK product over BES. Island footprints are small (Bonaire ~294 km², Saba 13 km², Sint Eustatius 21 km²); one physical base per island delivers full-island coverage at short baselines.
- Reference frame: NSGI uses "Bonaire 2004" (≡ ITRF2000 @ 2001.00 within 0.1 m) as the cadastral / station reference for Bonaire. Saba and Sint Eustatius stations are referenced to ITRF2014 (dynamic; BESTRANS2020 recommends epoch 2020.00 for static GIS use). BESTRANS2020 (v230405) publishes the 3D similarity parameters for transforming each island's frame to/from its local DPnet projection + EGM2008-derived height system.
- **Aruba (AW)**, **Curaçao (CW)**, and **Sint Maarten (SX)** are separate constituent countries within the Kingdom of the Netherlands — NOT covered by AGRS.BES. See `AW_Aruba.md`, `CW_Dutch_Caribbean.md`, and `SX_SintMaarten.md` (SX has its own paid Kadaster caster; CW has no national caster).

## Local Data Cross-References

- `py scripts/stations_by_country.py BES` (2026-05-21) → 8 hits (6 agrs_nl + 2 igs_ip). The two igs_ip rows (SABY00BES0, SEUS00BES0) are BKG IGS-IP relays of `ntrip.kadaster.nl/SABY00BES0` and `/SEUS00BES0` — same physical antennas, not additional stations.
- Cross-border alternatives within ~50 km: none. Nearest non-BES public stream is EarthScope CN59 on Anguilla (~65 km from Saba) — beyond the 50 km threshold for a viable single-base alternative. Bonaire is even more isolated: nearest is CUW JAJO cluster on Curaçao at ~70 km.

## Access

Connection using any NTRIP client:
- Host: `ntrip.kadaster.nl`
- Port: `2101` (unencrypted) or `443` (TLS)
- Username: blank, any string, or email (email recommended by NSGI for outage notices, not validated)
- Password: blank or any string
- Mountpoint examples: `BONK00BES0` (Bonaire), `SABY00BES0` (Saba), `SEUS00BES0` (Sint Eustatius)

## Sources Consulted

- NSGI real-time streams page (Dutch, HTTP 200, "gratis BES-eilanden" line verified 2026-05-21): https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams
- NSGI station information map: https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/stationsinformatie
- Kadaster NTRIP caster sourcetable (curl `--http0.9` probe 2026-05-21, all 7 BES streams present): http://ntrip.kadaster.nl:2101/
- NSGI BESTRANS2020 v230405 (datum + epoch authoritative source; Bonaire = ITRF2000@2001.00, Saba/Sint Eustatius = ITRF2014, recommended static epoch 2020.00): https://www.nsgi.nl/documents/1888506/69577825/BESTRANS2020_v230405.pdf
- Tarievenregeling Kadaster BWBR0037196 art. 19 lid 4 (free raw AGRS data clause, effective 2026-01-01): https://wetten.overheid.nl/BWBR0037196/2026-01-01
- Tarieven Kadaster BES 2026 (PDF, no separate NTRIP line item): https://kadorbonaire.com/wp-content/uploads/2025/12/Tarieven-Kadaster-BES-2026.pdf
- Kadaster BES portal: https://bes.kadaster.nl/kadaster-bonaire
- Related dev research file: `NL_Netherlands.md` (mainland AGRS.NL + NETPOS context)
