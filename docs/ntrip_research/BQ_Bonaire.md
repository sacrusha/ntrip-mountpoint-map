# Bonaire, Sint Eustatius, Saba [BQ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: YES — free public NTRIP via AGRS.BES (Kadaster NL / NSGI); 7 mountpoints across the three BES islands; fully anonymous access

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | NSGI (partnership of Kadaster, Rijkswaterstaat, Hydrographic Service of the Royal Netherlands Navy) — caster run by Kadaster Nederland |
| **landing_url** | https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams |
| **access_url** | https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams |
| **host:port** | `ntrip.kadaster.nl:2101` (plain TCP) · `ntrip.kadaster.nl:443` (TLS) |
| **Network identifier** | AGRS.BES (sub-network on the shared Kadaster caster) |
| **num_stations** | 4 physical CORS (Bonaire ×2, Saba ×1, Sint Eustatius ×1) feeding 7 streams |
| **vrs** | No — single-base only; one stream per physical receiver, no network solution for BES |
| **tariff** | €0.00, no VAT applicable. NSGI page (Dutch): *"De real-time data van onderstaande GNSS-stations is gratis: GNSS-stations van het AGRS.NL, de GNSS-stations op de Noordzee, de GNSS-stations op de BES-eilanden"* (observed 2026-05-15). Legal basis: Tarievenregeling Kadaster BWBR0037196 art. 19 lid 4 (effective 2026-01-01) — *"De ruwe data van stations die deel uitmaken van het AGRS.NL, evenals de ruwe GNSS-data met een waarnemingsinterval van één seconde, zijn kosteloos beschikbaar."* The 2026 Tarieven-Kadaster-BES PDF does not separately price NTRIP — confirms it stays under the free tier. |
| **hobbyist_eligibility** | Yes — fully anonymous, no account required |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-15 — `curl --http0.9 http://ntrip.kadaster.nl:2101/sourcetable.txt` returned all 7 BES streams under network `AGRS.BES`; caster identifier "Netherlands GNSS Network", operator NSGI |
| **datum_epoch** | ITRF2000 @ epoch 2001.00 (local realisation "Bonaire 2004", within 0.1 m); transformations to other frames published in NSGI BESTRANS2020 v230405 (https://www.nsgi.nl/documents/1888506/69577825/BESTRANS2020_v230405.pdf). Saba/Sint Eustatius stations are also distributed in the same ITRF realisation; consult BESTRANS2020 for per-island transform parameters. |

## Mountpoints — AGRS.BES (7 streams, sourcetable verified 2026-05-15)

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
- Free anonymous tier: username/password not required. NSGI recommends entering an email address in the username field (only) so they can notify operators of outages and changes — entirely optional.
- Modern multi-constellation receivers should connect to the `…00BES0` (RTCM 3.3 MSM) streams. The legacy `0` streams (`SABY0`, `SEUS0`, `SABY00BES1` raw SBF) exist for backward compatibility with older equipment or research applications.
- Single-base only — there is no VRS / network-RTK product over BES. Island footprints are small (Bonaire ~294 km², Saba 13 km², Sint Eustatius 21 km²); one physical base per island delivers full-island coverage at short baselines.
- Reference frame: NSGI uses the local realisation "Bonaire 2004" (≡ ITRF2000 @ 2001.00 within 0.1 m) for cadastral output on Bonaire; the same station-coordinate epoch is used for the AGRS.BES corrections. BESTRANS2020 (v230405) publishes the 3D similarity parameters for transforming to/from DPnet Bonaire.
- **Aruba (AW)**, **Curaçao (CW)**, and **Sint Maarten (SX)** are separate constituent countries within the Kingdom of the Netherlands — NOT covered by AGRS.BES. See `AW_Aruba.md`, `CW_Dutch_Caribbean.md`, and `SX_Sint_Maarten.md` (the latter two have their own Kadaster casters).

## Local Data Cross-References

- `py scripts/stations_by_country.py BES` → no matches (rtk2go/Centipede/EarthScope do not use a "BES" country tag; AGRS.BES is fed directly into stations.json via the `bq_cors` SOURCES entry — not through any of those aggregators).
- `py scripts/stations_by_radius.py 12.16 -68.27 200` → 0 rtk2go/Centipede/EarthScope stations physically on Bonaire; nearest are CUW (Curaçao, 70–77 km) and ABW (Aruba, ~190 km). None within Bonaire itself.
- `py scripts/stations_by_radius.py 17.65 -63.22 200` → 11 EarthScope COCONet stations within 200 km of Saba — AIA (Anguilla, 65 km), ATG (Antigua, 122 km), MSR (Montserrat, 145 km), VGB (BVI, 156 km). None are on Saba/Sint Eustatius themselves.
- Cross-border alternative within ~50 km: none. The closest non-BES public stream is ~65 km away (EarthScope CN59 on Anguilla) — outside the 50 km threshold for a viable single-base alternative.

## Access

Connection using any NTRIP client:
- Host: `ntrip.kadaster.nl`
- Port: `2101` (unencrypted) or `443` (TLS)
- Username: blank, any string, or email (email recommended by NSGI for outage notices, not validated)
- Password: blank or any string
- Mountpoint examples: `BONK00BES0` (Bonaire), `SABY00BES0` (Saba), `SEUS00BES0` (Sint Eustatius)

## Sources Consulted (probes 2026-05-15)

- NSGI real-time streams page (Dutch, content verified 2026-05-15): https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams
- NSGI station information map (verified 2026-05-15): https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/stationsinformatie
- Kadaster NTRIP caster sourcetable, RAW format with `--http0.9` (curl probe 2026-05-15, all 7 BES streams present): http://ntrip.kadaster.nl:2101/sourcetable.txt — note: the HTML variant `/sourcetable.htm` returns HTTP/0.9 and is rejected by default curl without `--http0.9`
- Caster root (returns sourcetable index over HTTPS, 2026-05-15): https://ntrip.kadaster.nl/
- NSGI BESTRANS2020 v230405 (datum / epoch authoritative source): https://www.nsgi.nl/documents/1888506/69577825/BESTRANS2020_v230405.pdf
- Tarievenregeling Kadaster BWBR0037196 art. 19 lid 4 (effective 2026-01-01, free raw AGRS data clause): https://wetten.overheid.nl/BWBR0037196/2026-01-01
- Tarieven Kadaster BES 2026 (PDF, no separate NTRIP line — remains free anonymous tier): https://kadorbonaire.com/wp-content/uploads/2025/12/Tarieven-Kadaster-BES-2026.pdf
- Kadaster BES portal (cadastral, no GNSS content but confirms organisational structure): https://bes.kadaster.nl/kadaster-bonaire
- Related dev research file: `NL_Netherlands.md` (full mainland AGRS.NL + NETPOS context)

## Self-Review

(a) Status reflects fresh probe — yes, 7 streams live 2026-05-15.
(b) All fields filled from spec — landing_url, access_url, host:port, tariff, num_stations, vrs, hobbyist, residency, last_confirmed_alive, datum_epoch all present and citable.
(c) No guesses substituted for unknowns — datum_epoch only cited with BESTRANS2020 URL; tariff cited with both NSGI quote and legal article.
(d) Local data cross-references run — `stations_by_country.py BES` (no matches), `stations_by_radius.py` at Bonaire / Saba / Sint Eustatius coordinates; no rtk2go/Centipede/EarthScope station physically on BES.
(e) Scope: only `BQ_Bonaire.md` modified.
(f) Cross-border alternative within 50 km — none (CUW nearest ~70 km, AIA ~65 km from Saba).

SELF-REVIEW: PASS
