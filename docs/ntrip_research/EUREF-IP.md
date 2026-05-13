# EUREF-IP — NTRIP Federation Research (cross-country, not a country)
**Date researched:** 2026-05-13 (live probes of all three federated broadcasters + IGS-IP + products.igs-ip.net)

> **Scope note.** This is not a country entry. EUREF-IP is the federated NTRIP
> broadcaster network that disseminates real-time GNSS streams from the EUREF
> Permanent Network (EPN). It is operated by three institutions across three
> countries (BKG/DE, ROB/BE, ASI/IT). Several country files reference EUREF-IP
> stations; this entry consolidates the per-broadcaster facts (host, port,
> registration, station counts, station verifications) so those files can
> point to a single source.

## Status: ACTIVE — three federated broadcasters live and reachable 2026-05-13; ~229 unique EPN stations streaming real-time; free with per-broadcaster registration. Raw single-base RTCM 3.x observations only (no VRS / FKP / MAC).

| Field | Value |
|---|---|
| **Federation name** | EUREF-IP — EUREF NTRIP broadcaster federation |
| **What is streamed** | Raw 1 Hz RTCM 3.x GNSS observations from EPN reference stations + a few SSR/BRDC mountpoints for PPP/research |
| **Broadcasters (live)** | 3 — BKG (DE), ROB (BE), ASI (IT). All three returned `SOURCETABLE 200 OK` on 2026-05-13. |
| **Sister federation** | IGS-IP (`www.igs-ip.net:2101`, operated by BKG) — global IGS stations; raw observation streams; same registration system as BKG EUREF-IP |
| **PPP product caster** | `products.igs-ip.net:2101` (operated by BKG) — IGS-RTS SSR corrections, **not** RTCM observation streams; enables PPP for PPP-capable receivers |
| **Tariff** | Free of charge across all three broadcasters |
| **Registration model** | **Per-broadcaster account** — there is **no federated single-sign-on**. BKG-issued credentials do not work on ROB; ROB-issued credentials do not work on BKG; ASI separate again. |
| **hobbyist_eligibility** | Yes — no professional/licensing filter on any of the three registration forms |
| **legal_residency_required** | No — registration is open globally; both ROB and BKG forms accept any country code |
| **last_confirmed_alive** | 2026-05-13 — all three sourcetables retrieved successfully (BKG 218 STR, ROB 214 STR, ASI 201 STR; counts below) |
| **Operator statements on RTK use** | ROB registration page: *"The provided raw GNSS data streams are unsuitable for operational real-time kinematic positioning."* BKG and ASI make no equivalent statement. None of the three publishes a VRS / network RTK product. |

---

## Federation members (live probes 2026-05-13)

All three are NTRIP 2.0 BKG-derived caster software (`NTRIP BKG Caster 2.0.x/2.0`) except ASI which also exposes a slightly older NTRIP/2.0.21 instance via IP.

### BKG — Bundesamt für Kartographie und Geodäsie (Germany)

| Field | Value |
|---|---|
| **Operator** | BKG, Frankfurt am Main |
| **Host:Port** | `euref-ip.net:2101` (plain HTTP) and `:80` |
| **TLS** | `euref-ip.net:443` (HTTPS, confirmed live with `-k`) — same sourcetable contents |
| **Caster banner** | `NTRIP BKG Caster 2.0.48/2.0` |
| **STR rows** | 218 (218 distinct mountpoints) |
| **NET groups** | EUREF (144), IGS (66), MISC (7), GREF (1) |
| **Format** | RTCM 3.3 (173), RTCM 3.2 (38), RTCM 3.1 (7) |
| **Constellations** | 163 of 218 are GPS+GLO+GAL+BDS; rest mix in QZS/SBAS/IRS |
| **Solution column** | 206 physical (`0`) + 12 derived/network (`1` — SSR feeds, EUREF01/02 BRDC mountpoints, GFZ-relayed IGS streams) |
| **Authentication** | 217 require Basic auth; 1 (DELF00NLD0, TU Delft) is open (`N`) |
| **Fee column** | 215 free (`N`); 3 marked `Y` — Austrian APOS/BEV streams (PFA300AUT0, SBG200AUT0, TRF200AUT0). The `Y` flag indicates an upstream paywall on the source side; on the BKG caster they are still gated behind the same BKG account but may not stream to anonymous BKG users without separate APOS authorisation. |
| **NMEA flag** | All 218 rows have NMEA=0 (no GGA upload required) |
| **Registration URL** | `http://register.rtcm-ntrip.org/cgi-bin/registration.cgi` — single form serves BKG EUREF-IP, BKG IGS-IP, and BKG products.igs-ip.net |
| **Required fields** | Family Name, First Name, Organization, Organization Type, Country, E-Mail, User-Name, Password, Application (free-text); BKG privacy policy consent |
| **Approval timing** | Manual approval during BKG working hours; no published SLA |
| **Contact** | `euref-ip@bkg.bund.de` ; `igs-ip@bkg.bund.de` (registration support) |
| **Terms language** | "Best effort", no SLA, no commercial/non-commercial split, citation requested in publications |
| **Relayed-caster count (CAS rows in sourcetable)** | 5 — itself, ROB, ASI (two entries), and rtcm-ntrip.org info-only caster |

### ROB — Royal Observatory of Belgium

| Field | Value |
|---|---|
| **Operator** | Royal Observatory of Belgium (ROB), Brussels (also `gnss.be`) |
| **Host:Port** | `www.euref-ip.be:2101` (plain HTTP). Also `euref-ip.be:2101` (same caster) |
| **TLS** | `www.euref-ip.be:2102` (HTTPS, confirmed live) |
| **Caster banner** | `NTRIP BKG Caster 2.0.48/2.0` (ROB uses BKG caster software) |
| **STR rows** | 214 (214 distinct mountpoints) |
| **NET groups** | EUREF (205), PROPOSED (4), IGS (1), MISC (4) |
| **Format** | RTCM 3.2 (161), RTCM 3.3 (34), RTCM 3.1 (17), RTCM 3.0 (2) — ROB skews toward RTCM 3.2; BKG skews toward RTCM 3.3 |
| **Constellations** | 141 of 214 GPS+GLO+GAL+BDS; rest GPS+GLO/GAL only or +QZS/+SBAS |
| **Authentication** | 207 require Basic auth; 7 are open (`N`) |
| **Fee column** | 212 free (`N`); 2 marked `Y` (same Austrian APOS streams) |
| **NMEA flag** | All 214 rows have NMEA=0 |
| **Registration URL** | `https://www.euref-ip.be/user-registration/user-registration-main-page.php` |
| **Required fields** | First name, last name, email, affiliation, address, city, country code, username, password, "Purpose" free-text; CAPTCHA required |
| **Approval timing** | Manual approval "during normal working hours" — holiday delays possible |
| **Explicit RTK disclaimer** | *"The provided raw GNSS data streams are unsuitable for operational real-time kinematic positioning."* (ROB registration page) |
| **Cannot upload streams** | ROB credential cannot be used to push streams to the broadcaster (read-only consumer account) |
| **Relayed-caster count (CAS rows in sourcetable)** | 23 — ROB itself, BKG, ASI, plus 20 external upstream casters (ergnss-ip.ign.es, rgp-ip.ign.fr, ntrip1.os.co.uk, cpos.kartverket.no, ntripdist-swepos.lm.se, skpos.gku.sk, ntrip1.gnssnet.hu, tpp.swipos.ch, sulp.polynet.lviv.ua, agh.edu.pl Poland, ntrip.pecny.cz, ICV Valencia, IGEO Portugal, two Italian university casters, mgex.igs-ip.net, www.igs-ip.net, rtcm-ntrip.org) |

### ASI — Agenzia Spaziale Italiana / e-GEOS (Italy)

| Field | Value |
|---|---|
| **Operator** | Agenzia Spaziale Italiana (ASI) / e-GEOS, Matera Space Geodesy Centre |
| **Host:Port** | `euref-ip.asi.it:2101` (plain HTTP) — also resolvable as `192.106.234.17:2101` |
| **TLS** | None — port 443 on `euref-ip.asi.it` refused TCP connect on 2026-05-13 |
| **Caster banner** | `NTRIP BKG Caster 2.0.37/2.0` (slightly older BKG software than BKG/ROB run) |
| **STR rows** | 201 (201 distinct mountpoints) |
| **NET groups** | EUREF, IGS, MISC (same as BKG) |
| **Registration URL** | Not exposed via the EPNCB broadcaster page directly; ASI registrations are administered by BKG's `register.rtcm-ntrip.org` form (per EPNCB documentation) but ASI-specific accounts may differ — verify with ASI before relying on BKG credentials for ASI |
| **Stations carried** | Largely the same EPN set as BKG/ROB (overlap with BKG = 199 stations; ASI unique: `BORR00ESP0`, `METG00FIN0` are NOT on ASI but BKG has neither — ASI has 0 stations BKG lacks; BKG has 19 stations ASI lacks including all `NABG`, `NYA2`, `WUTH` Norway/Svalbard stations) |
| **Relayed-caster count (CAS rows in sourcetable)** | 1 — itself |

---

## What's actually in the sourcetables (consolidated)

### Mountpoint naming convention

EPN stations follow the **IGS station 9-character + monument-number convention**: `XXXXMMCCCS` where:
- `XXXX` = 4-char station code (e.g. `PCAR`, `REYK`, `NICO`, `AGRN`)
- `MM` = monument number (`00` is the default for most)
- `CCC` = ISO-3 country code (`AND`, `ISL`, `CYP`, `ITA`, `ESP`, `DEU`, ...)
- `S` = solution / antenna identifier digit (almost always `0`)

Example mountpoints: `PCAR00AND0` (Andorra), `REYK00ISL0` (Iceland), `NICO00CYP0` (Cyprus), `AGRN00ITA0` (Agrigento Italy), `ALAC00ESP0` (Alicante Spain).

A handful of legacy 4-char-only mountpoints exist on adjacent broadcasters (`MARI` for Mariehamn was historically a 4-char name) but these are not currently present in any of the three EUREF-IP sourcetables.

A small number of non-station mountpoints carry SSR/BRDC products on BKG only:
`EUREF01`, `EUREF02`, `SSRA02IGS0_EUREF`, `SSRA02IGS1_EUREF`, `SSRA03IGS0_EUREF`, `SSRA03IGS1_EUREF`, `BCEP00BKG0` — all RTCM 3.1 with SSR (1057–1268, 4076_xxx) messages; for PPP, not RTK.

### Real-time station count (EPNCB authoritative)

The EPNCB real-time map (`https://epncb.oma.be/_networkdata/data_access/real_time/map.php`, fetched 2026-05-13) lists **229 EPN stations with active real-time streams**. Each broadcaster carries a subset:

- BKG: 218 STR rows (216 distinct EPN-network + 6 IGS-classed cross-listings + SSR products)
- ROB: 214 STR rows (highest EPN-only coverage in the federation; carries 1 station BKG lacks — `METG00FIN0`/Metsahovi, Finland — relayed from `rgp-ip.ign.fr`)
- ASI: 201 STR rows (subset of BKG; mostly Italian and southern European stations)

The remaining ~10–15 stations that appear on the EPNCB map but not on the EUREF-IP federation sourcetables are stations whose streams are listed but inactive at probe time, or stations carried by relayed upstream casters (e.g. `rgp-ip.ign.fr`, `ergnss-ip.ign.es`, `cpos.kartverket.no`) that are reachable directly but not relayed into EUREF-IP.

### RTCM versions and constellations

Format spread across all three broadcasters: **majority RTCM 3.2 or 3.3** with full multi-constellation MSM messages (1075–1127). A small minority remain on RTCM 3.0/3.1 with legacy 1004/1012 GPS+GLO observations. Constellation breakdown is dominated by **GPS+GLO+GAL+BDS** (~75 % of streams); rest include QZS or SBAS depending on receiver type.

### Important quirks

- **NMEA=0 throughout**: All EUREF-IP STR rows have `NMEA=0` — no GGA upload required from the rover. This makes it pipeline-friendly (the project's default `nmea_filter=True` does NOT drop EUREF-IP streams).
- **Solution=1 rows** (12 on BKG, fewer on ROB): SSR product mountpoints and a small set of IGS-relayed stations that carry processed/derived streams rather than raw observations. These are still individual-station-tagged but should not be confused with VRS.
- **Authentication=N (open) rows are rare**: 1 on BKG (TU Delft), 7 on ROB. They can be accessed anonymously but are still EPN-controlled and may be restricted by the upstream owner.
- **Fee=Y rows** (3 Austrian APOS streams on BKG, 2 on ROB): These are relayed from BEV/APOS Austria. The EUREF-IP account may not be sufficient — Austrian APOS gating likely applies upstream. Do not assume Austrian state-level access via a BKG/ROB credential.

---

## Registration, access, and use restrictions

### How registration works

**There is no federated single-sign-on.** A user must register separately with each broadcaster they want to consume:

1. **BKG (`register.rtcm-ntrip.org`)** — single form covers EUREF-IP, IGS-IP, products.igs-ip.net. Manual approval by BKG staff; credentials emailed back. Required: name, organisation, organisation type, country, email, chosen username/password, application description, privacy-policy consent.
2. **ROB (`www.euref-ip.be/user-registration/`)** — separate form, CAPTCHA, manual approval by ROB staff. Required: name, email, affiliation, address, city, country code, chosen username/password, "Purpose" free-text. Page explicitly states streams are unsuitable for operational RTK.
3. **ASI** — administered via BKG's registration system per EPNCB documentation; in practice some Italian-network streams on ASI may require separate vetting. The ASI broadcaster does not expose its own public registration portal as of 2026-05-13.

### Access model

- All three are **free of charge**.
- Approval is **manual**, typically within a few business days; holiday delays expected.
- Accounts are **per-broadcaster**, not federated across BKG/ROB/ASI.
- Both BKG and ROB casters accept **Basic auth over HTTP/HTTPS**. ROB's HTTPS lives on port 2102 (non-standard); BKG offers HTTPS on standard 443. ASI is HTTP-only.

### Use restrictions

- **No explicit non-commercial or residency clause** on any of the three. Both BKG and ROB registration forms are open to any country and any application type.
- **ROB statement**: registration page states streams are "unsuitable for operational real-time kinematic positioning." BKG and ASI make no equivalent statement.
- **No throttling published** on any of the three; BKG documentation notes that "NTRIP relay operators" can request expanded simultaneous-stream quotas (5–50) by emailing BKG. Default per-account quota is not published.
- **Citation request**: BKG asks that users include a citation in publications. No legal enforcement.
- **No commercial-use prohibition** found on any of the three registration pages or terms.

---

## Cross-references from country files (verified 2026-05-13)

Each row below verifies whether the station the country file claims streams via EUREF-IP actually appears in any of the three federated sourcetables today.

| Country file | Cited EPN station | In BKG? | In ROB? | In ASI? | Notes |
|---|---|:-:|:-:|:-:|---|
| `AD_Andorra.md` | `PCAR00AND0` (Pic de Carroi) | ✅ RTCM 3.3 GPS+GLO+GAL+BDS | ✅ RTCM 3.2 (PROPOSED) | ✅ RTCM 3.2 | Upstream is `185.194.59.113:2101/PCAR3M` (Leica GR50 receiver, direct public IP). All three broadcasters relay from the same upstream. |
| `AD_Andorra.md` | `RULL` (second ERGAND station) | ❌ | ❌ | ❌ | No RULL or `RULL*` row in any of the three sourcetables 2026-05-13. Not streaming real-time via EUREF-IP. |
| `CY_Cyprus.md` | `NICO00CYP0` via AUSCORS | ✅ RTCM 3.3 (IGS network class) | ✅ RTCM 3.0 GPS+GLO + RTCM 3.2 GPS+GLO+GAL+BDS | ✅ | Cited via AUSCORS in the CY file; EUREF-IP also carries NICO00CYP0 directly on all three broadcasters. Baseline ~20 km from Nicosia city centre. |
| `AX_AlandIslands.md` | `MARI` (Mariehamn EPN station) | ❌ | ❌ | ❌ | No MARI or `MAR*` 9-char mountpoint in any EUREF-IP sourcetable as of 2026-05-13. AX file's note that EPN MARI "may stream real-time RTCM via euref-ip.net" is not currently true. |
| `IS_Iceland.md` | `REYK00ISL0` (Reykjavik IGS station) | ✅ RTCM 3.3 | ✅ RTCM 3.0 + RTCM 3.2 | ✅ | EUREF-IP carries REYK on all three broadcasters; baseline ~15 km from Reykjavik centre. Also carried by IGS-IP (`www.igs-ip.net:2101/REYK00ISL0`). |
| `SJ_Svalbard.md` | `NYA2` / `NABG` Ny-Ålesund | ✅ NABG00NOR0 + NYA200NOR0 (both RTCM 3.3) | ✅ both | ❌ ASI does not carry them | NABG and NYA2 reachable via BKG and ROB EUREF-IP. NYA2 on BKG is `solution=1` (derived/processed at GFZ-Potsdam) rather than raw observation. Also carried by IGS-IP. |
| `GI_Gibraltar` (no file) | `BIGF`/`GIBR` station mention | ❌ | ❌ | ❌ | No GIBR* or BIGF* mountpoint in any EUREF-IP sourcetable 2026-05-13. BIGF (British Isles Continuous GNSS Facility) data flows are separate and not pushed to EUREF-IP. Closest live EPN stations are in southern Spain (`MALA00ESP0` Malaga; `ALGE00ESP0` Algeciras — presence to verify on demand). |

### Other EPN stations verified live 2026-05-13

EPN stations on the EUREF-IP federation as of 2026-05-13 that are not currently cross-referenced in country files:

- **`ASGA00CYP0`** (Asgata, southern Cyprus, RTCM 3.2 MSM, BKG+ROB)
- **`MIKL00UKR0`** / **`SULP00UKR0`** (Ukraine western stations on BKG/ROB via `sulp.polynet.lviv.ua` relay)
- **`LROC00FRA0`** / **`TLSE00FRA0`** etc. (French stations, mostly relayed from `rgp-ip.ign.fr`)
- **`LEIJ00DEU0`** (Leipzig, BKG only — not on ROB)

---

## Confusion resolution: EUREF-IP vs IGS-IP vs products.igs-ip.net

These three are operationally distinct despite all being BKG-operated.

| | EUREF-IP (`euref-ip.net:2101` + ROB + ASI) | IGS-IP (`www.igs-ip.net:2101`) | products.igs-ip.net (`:2101`) |
|---|---|---|---|
| **Operator** | BKG + ROB + ASI federation | BKG (single caster) | BKG (single caster) |
| **Scope** | Regional — EPN reference stations across Europe | Global — IGS reference stations worldwide | Global — IGS Real-Time Service SSR products |
| **What's on it** | ~214–218 raw GNSS observation streams (RTCM 3.x); few SSR mountpoints on BKG | 386 raw observation streams from the global IGS network | 87 SSR product streams (orbits/clocks/biases) for PPP |
| **Stream type** | Single-base raw observations (RTCM 3.x). Not a network RTK product. | Single-base raw observations (RTCM 3.x). Same character as EUREF-IP. | SSR product streams (orbits/clocks/biases). PPP only — requires PPP-capable receiver (e.g. BNC, RTKLIB with SSR support). |
| **Registration** | BKG: `register.rtcm-ntrip.org` (single form covers all 3 BKG casters); ROB: separate; ASI: via BKG | Same BKG form | Same BKG form |
| **Overlap with EUREF-IP** | Several stations appear on both (e.g. REYK, NICO, NABG, NYA2) | | |
| **TLS** | BKG :443, ROB :2102, ASI none | BKG :443 | BKG :443 |

---

## Recent and planned changes (2024–2026)

### EPN → EPOS integration (formalised at 2025 EUREF Symposium, Covilhã)

Per the December 2025 EUREF newsletter (Issue 6) and Resolution No. 1 of the 2025 EUREF Symposium:

- All EPN stations will, by default, be included in the GNSS network of EPOS (European Plate Observing System).
- EPN metadata (M3G) and RINEX archive data will gradually become discoverable within EPOS starting **2026**.
- **No published change to real-time NTRIP access or terms** as of 2026-05-13. The three EUREF-IP broadcasters continue to operate under existing registration models.
- The EPOS integration affects historical/archive data discoverability, not the live RTCM streams or their authentication.

### Next EUREF Symposium

23–25 June 2026, ENSA Paris-Val de Seine, France. No public agenda items signalling changes to EUREF-IP access policy.

### Broadcaster software refresh

BKG and ROB casters were running `NTRIP BKG Caster 2.0.48/2.0` on 2026-05-13; ASI runs an older 2.0.37 build. ROB additionally relays from 20+ external upstream casters in its sourcetable (CAS rows). No operator changes announced for 2026.

### What 2024–2026 did NOT change

- All three broadcasters remain free with registration.
- Per-broadcaster account model (no federation SSO) is unchanged.
- No VRS / network RTK product added on any of the three; streams remain raw single-base observations.
- No new TLS port additions beyond what's documented above.

---

## Sourcetable parsing characteristics

All rows have `NMEA=0`. `solution=0` for ~95 % of rows; the 12 BKG SSR/derived rows carry `solution=1`. RTCM 3.x throughout, mostly MSM with full GPS+GLO+GAL+BDS.

---

## Post-Processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| **EPN Central Bureau RINEX archive** (all 280+ EPN stations, daily/hourly/15-min RINEX) | https://epncb.oma.be/ftp/ | Free (EPN data policy) |
| **BKG GNSS data archive** | https://igs.bkg.bund.de/ | Free with registration |
| **IGS data archive (global IGS stations)** | https://igs.org/network and various IGS data centres | Free |

---

## Sources Consulted

- EPN Central Bureau: https://epncb.oma.be/
- EPN Real-Time map (2026-05-13, fetched directly with Mozilla UA — returns full HTML with embedded GeoJSON of 229 active stations): https://epncb.oma.be/_networkdata/data_access/real_time/map.php
- EPN NTRIP broadcaster list: https://www.epncb.oma.be/_networkdata/data_access/real_time/broadcasters.php
- EUREF-IP BKG (`euref-ip.net`): https://euref-ip.net/home (HTTP 200; states `:80, :2101, :443`; contact `euref-ip@bkg.bund.de`)
- EUREF-IP ROB (`www.euref-ip.be`): https://www.euref-ip.be/ (states explicit "unsuitable for operational real-time kinematic positioning")
- ROB user registration: https://www.euref-ip.be/user-registration/user-registration-main-page.php (CAPTCHA-gated form)
- BKG user registration (single form for EUREF-IP + IGS-IP + products.igs-ip.net): http://register.rtcm-ntrip.org/cgi-bin/registration.cgi
- IGS-IP caster home: https://www.igs-ip.net/home
- products.igs-ip.net caster home: https://products.igs-ip.net/home
- EPN data access overview: https://www.epncb.oma.be/_networkdata/data_access/real_time/
- EUREF Newsletter Issue 6 (2025-12-22, EPN→EPOS integration starting 2026): http://www.epncb.oma.be/_documentation/newsletters/EUREF_Newsletter_2025_01.pdf
- BKG NTRIP infrastructure: https://igs.bkg.bund.de/ntrip/
- IGS RTS user access: https://igs.org/rts/user-access/
- EPN Wikipedia: https://en.wikipedia.org/wiki/EUREF_Permanent_Network
- GNSS.be EUREF page: https://gnss.be/activities-EUREF.php

### Live probes (2026-05-13)

- `curl --http0.9 http://euref-ip.net:2101/` — `SOURCETABLE 200 OK`, `NTRIP BKG Caster 2.0.48/2.0`, 218 STR rows, 3 NET, 5 CAS
- `curl --http0.9 http://www.euref-ip.be:2101/` — `SOURCETABLE 200 OK`, `NTRIP BKG Caster 2.0.48/2.0`, 214 STR rows, 2 NET, 23 CAS
- `curl --http0.9 http://euref-ip.asi.it:2101/` — `SOURCETABLE 200 OK`, `NTRIP BKG Caster 2.0.37/2.0`, 201 STR rows, 3 NET, 1 CAS
- `curl --http0.9 -k https://euref-ip.net:443/` — same 218 STR rows; TLS confirmed live
- `curl --http0.9 -k https://www.euref-ip.be:2102/` — same 214 STR rows (minus 2 rows fluctuation); TLS confirmed live on non-standard port
- `curl https://euref-ip.asi.it:443/` — connection refused; ASI is HTTP-only on `:2101`
- `curl --http0.9 http://www.igs-ip.net:2101/` — 386 STR rows global
- `curl --http0.9 http://products.igs-ip.net:2101/` — 87 STR rows (SSR products, RTCM 3.1 with 4076_xxx messages)
- `curl --http0.9 http://185.194.59.113:2101/` — upstream PCAR receiver (LEICA GR50 4.80.109/1.0; STR rows `PCAR3` and `PCAR3M`)

### Cross-references inspected in `docs/ntrip_research/`

- `AD_Andorra.md`, `CY_Cyprus.md`, `AX_AlandIslands.md`, `IS_Iceland.md`, `SJ_Svalbard.md`, `BE_Belgium.md`, `DE_Germany.md` (for SAPOS BKG/GEPOS interplay), `IT_Italy.md`, `HT_Haiti.md`, `CW_Dutch_Caribbean.md`.
