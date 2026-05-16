# Burkina Faso [BF] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: BF-CORS NTRIP caster confirmed live — 13 BFA single-base mountpoints + 1 VRS + 1 DGNSS-multi all enumerated 2026-05-15; web Register page returns maintenance error; hobbyist eligibility unconfirmed (gate is registration approval, not network availability)

| Field | Value |
|---|---|
| **landing_url** | https://www.igb.bf/?page_id=47 (IGB GNSS-CORS page, authoritative; instructs users to register at `www.bfcors.net`) |
| **access_url** | http://www.bfcors.net/ (Trimble Pivot Web portal; `RegisterAccount.aspx` returns "service is temporarily not available due to maintenance or technical problems" — 2026-05-15) |
| **host:port** | `www.bfcors.net:2101` — live NTRIP caster, `SOURCETABLE 200 OK`, `Server: NTRIP Trimble Ntrip Caster 4.1`, 2026-05-15. Probe must pass `--http0.9` flag (caster speaks HTTP/0.9); a probe without that flag will appear to fail. |
| **tariff** | Not published. IGB page does not state cost; no tariff page on the Pivot Web portal pre-login. |
| **num_stations** | 13 physical BFA single-base mountpoints in live sourcetable (DORI, DIAP, FADA, BF01, BOBO, DEDG, GAOA, MANG, OHGY, DPGO, IGB0, KBRI, TGDA), plus `MultiStation_RTCM31` (BFA, solution=1, network VRS) and `BurkinaDGNSSMulti` (BFA, DGNSS multi-station, solution=1), plus 1 cross-reference `VRSRTCM32` tagged DEU. Matches IGB-reported 9 (2011) + 4 (2018) = 13 physical CORS. |
| **vrs** | yes — `MultiStation_RTCM31` (BFA, solution=1) and `BurkinaDGNSSMulti` (BFA, DGNSS multi-station, solution=1) present alongside the 13 single-base streams. |
| **hobbyist_eligibility** | ? — IGB's stated audience is "géomètres, cadastreurs, cartographes". No explicit exclusion of hobbyists, but `RegisterAccount.aspx` non-functional today and Login form expects an "organization" field (multi-tenant Pivot). Sourcetable is anonymously enumerable; rover access still requires approved credentials. |
| **legal_residency_required** | ? — not stated; in practice expect IGB to favour locally established professional users. |
| **last_confirmed_alive** | 2026-05-15 — `curl --http0.9 http://www.bfcors.net:2101/` returned `SOURCETABLE 200 OK`, `Server: NTRIP Trimble Ntrip Caster 4.1`, Content-Length 2754, all 13 BFA + 1 VRS + 1 DGNSS-multi STR rows enumerated. Web portal also live: `www.bfcors.net/` HTTP 200, IIS/8.0, footer "© Copyright 2026, Trimble Inc."; `Login.aspx` HTTP 200; `RegisterAccount.aspx` HTTP 302 → DefaultErrorPage with maintenance message. |
| **datum_epoch** | Omitted — no citable official declaration found. IGB references a "système de référence national" without specifying datum/epoch in any public document located. |

## Probes (2026-05-15, from this sandbox)

| Endpoint | Result |
|---|---|
| `http://www.bfcors.net/` | HTTP 200, 10.4 KB, Microsoft-IIS/8.0, Trimble Pivot Web home page, footer "© Copyright 2026, Trimble Inc." |
| `http://www.bfcors.net/Login.aspx` | HTTP 200; form fields: Organization, User Name, Password |
| `http://www.bfcors.net/Map/SensorMap.aspx` | HTTP 200; OpenLayers map shell; server-side `NumSensors=0` (sensors loaded by authenticated JS) |
| `http://www.bfcors.net/RegisterAccount.aspx` | HTTP 302 → `/DefaultErrorPage.aspx` displaying "The requested service is temporarily not available due to maintenance or technical problems. Please try again later." |
| `http://www.bfcors.net:2101/` (with `--http0.9`) | `SOURCETABLE 200 OK`, `Server: NTRIP Trimble Ntrip Caster 4.1`, Content-Length 2754, 15 STR rows (13 BFA single-base + 1 BFA VRS + 1 BFA DGNSS-multi + 1 DEU passthrough). A probe without `--http0.9` returns "Received HTTP/0.9 when not allowed" and looks like a failure — this was the prior-research artefact. |
| `http://www.bfcors.net:2102/`, `:2103/`, `:8080/` | TCP refused |

Implication: the operator's caster is publicly enumerable — sourcetable contents (mountpoint names, formats, lat/lon=0/0 obfuscated by Trimble Pivot) are visible without credentials. New-account self-registration via `RegisterAccount.aspx` is currently broken (maintenance error), but the caster itself is live and a target user with valid credentials can connect a rover from outside Burkina Faso. The bottleneck is the registration approval path, not the network.

## Context Notes

- **Stations (per IGB):** 13 total.
  - 2011 (9, MCA-BF / Trimble contract May 2010, ~700 MFCFA): Gampela, Manga, Fada, Diapaga, Dori, Ouahigouya, Dédougou, Bobo-Dioulasso, Gaoua.
  - 2018 (4, state budget, Ouagadougou metro densification): Ouagadougou (IGB HQ), Koubri, Dapélogo, Tanguen-Dassouri.
- **IGB tutelle:** under the Ministry of Infrastructure; technical management of the network since September 2012.
- **Academic confirmation of historical operation:** Station BF01 (Ouagadougou) raw GNSS-CORS data 2013-01-01 to 2021-12-31 used in 2024 ionospheric VTEC publication (ResearchGate 379545036). Post-2021 continuity unverified.
- **Security/political context:** 2022 military coup; Burkina Faso, Mali, Niger withdrew from ECOWAS and formed the Alliance of Sahel States (AES) January 2025; jihadist insurgency affects a large share of national territory; reduced bilateral technical-cooperation with the West. Station operational continuity and IGB maintenance capacity uncertain — consistent with the observed bfcors.net `RegisterAccount.aspx` maintenance error.
- **Volunteer / free coverage:** zero. Confirmed via `scripts/stations_by_country.py BFA` (no stations) and `scripts/stations_by_radius.py 12.37 -1.52 200` (no stations within 200 km of Ouagadougou) on 2026-05-15. No rtk2go BF mountpoints; no Centipede BFA nodes; no GEODNET/ONOCOY/Emlid coverage; EarthScope/NOTA scope is Americas-only.
- **Cross-border alternatives within ~50 km:** none. Nearest CORS infrastructure of any kind sits well beyond 50 km (RECI in Côte d'Ivoire, IGN Bénin, IGN Niger, IGN Mali — all institutional, none public NTRIP).
- **Practical workaround for a hobbyist in BF today:** deploy a local single base for RTK, or use PPP (Galileo HAS open service, Trimble RTX) for sub-metre positioning without subscription.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| IGB BF-CORS RINEX archive (13 stations; contact IGB directly; portal section gated) | https://www.igb.bf/?page_id=47 | Not published |
| SONEL station OUAG (Ouagadougou, AMMA → IGS contribution since 2011) | https://www.sonel.org/spip.php?page=gps&idStation=2561 | Free |
| IGS / CDDIS data archive (if/when BF stations federate) | https://cddis.nasa.gov/Techniques/GNSS/IGS_Summary.html | Free non-commercial |

## Sources Consulted (2026-05-15)

- IGB GNSS-CORS page — https://www.igb.bf/?page_id=47 (verified live)
- IGB home page — https://www.igb.bf/ (verified live; latest visible news March 2026, GDZHIAO workshop closure)
- BF-CORS Trimble Pivot Web — http://www.bfcors.net/ (verified live, HTTP 200, IIS/8.0, "© Copyright 2026, Trimble Inc.")
- BF-CORS Login — http://www.bfcors.net/Login.aspx (verified live)
- BF-CORS Sensor Map — http://www.bfcors.net/Map/SensorMap.aspx (verified live, no public sensor data)
- BF-CORS Register — http://www.bfcors.net/RegisterAccount.aspx (302 → DefaultErrorPage maintenance message)
- IGB contact email observed on igb.bf: infogeo.bf@gmail.com
- 2024 ionospheric VTEC paper on BF01 — https://www.researchgate.net/publication/379545036
- SONEL OUAG station — https://www.sonel.org/spip.php?page=gps&idStation=2561
- RTK2GO monitor — http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101 (no BF mountpoints)
- Centipede-RTK map — https://map.centipede-rtk.org/ (no BFA nodes)
- Local: `scripts/stations_by_country.py BFA` → no stations; `scripts/stations_by_radius.py 12.37 -1.52 200` → no stations
