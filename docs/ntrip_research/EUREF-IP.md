# EUREF-IP — NTRIP Federation Research (cross-country, not a country)

**Date researched:** 2026-05-21 (live probes of all three federated broadcasters + ASI's separate registration form. Earlier baseline 2026-05-13 retained where unchanged).

> **Scope note.** Not a country entry. EUREF-IP is the federated NTRIP
> broadcaster network that disseminates real-time GNSS streams from the EUREF
> Permanent Network (EPN). It is operated by three institutions across three
> countries (BKG/DE, ROB/BE, ASI/IT). Several country files reference EUREF-IP
> stations; this entry consolidates per-broadcaster facts (host, port,
> registration, station counts, station verifications) so country files can
> point to a single source.
>
> Global counterpart: **IGS-IP** (`www.igs-ip.net:2101`, BKG) — see
> `IGS-IP.md` for that caster's details.

## Status: ACTIVE — three federated broadcasters live and reachable 2026-05-21; ~215 unique stations across the three federated casters (229 per EPNCB authoritative total); free with per-broadcaster registration. Raw single-base RTCM 3.x observations only (no VRS / FKP / MAC).

| Field | Value |
|---|---|
| **Federation name** | EUREF-IP — EUREF NTRIP broadcaster federation |
| **What is streamed** | Raw 1 Hz RTCM 3.x GNSS observations from EPN reference stations + a few SSR/BRDC mountpoints for PPP/research on the BKG broadcaster |
| **Broadcasters (live)** | 3 — BKG (DE), ROB (BE), ASI (IT). All three returned `SOURCETABLE 200 OK` on 2026-05-21. |
| **Sister federation** | IGS-IP (`www.igs-ip.net:2101`, operated by BKG) — global IGS stations; raw observation streams; same registration form on BKG side. See `IGS-IP.md`. |
| **PPP product caster** | `products.igs-ip.net:2101` (operated by BKG) — IGS-RTS SSR corrections, **not** RTCM observation streams; enables PPP for PPP-capable receivers. Documented in `IGS-IP.md`. |
| **Tariff** | Free of charge across all three broadcasters; observed 2026-05-21. VAT n/a (no charge). Sources: BKG form http://register.rtcm-ntrip.org/cgi-bin/registration.cgi; ROB page https://www.euref-ip.be/user-registration/user-registration-main-page.php; ASI page http://geodaf.mt.asi.it/gps_caster_access.php. |
| **num_stations** | ~215 unique physical CORS across the three federated broadcasters (union of mountpoints minus 7 SSR/BRDC non-physical mounts = 215 on 2026-05-21). EPN Central Bureau (https://epncb.oma.be/_networkdata/data_access/real_time/map.php) lists 229 EPN stations as actively streaming real-time; the ~14-station gap is stations reachable only via upstream relay casters not aggregated into the three federated broadcasters. Per-broadcaster STR counts: BKG 221, ROB 215, ASI 202 (2026-05-21). |
| **Registration model** | **Per-broadcaster account** — no federated single-sign-on. BKG-issued credentials do not work on ROB; ROB-issued credentials do not work on BKG; ASI separate again. |
| **hobbyist_eligibility** | Yes — no professional/licensing filter on any of the three registration forms. **Caveat:** ROB's registration page explicitly states the streams are "unsuitable for operational real-time kinematic positioning". Read: federation is intended for monitoring/research, not field RTK; hobbyist account approval is unaffected, but operator does not warrant RTK-grade performance. |
| **legal_residency_required** | No — registration is open globally on all three forms. |
| **last_confirmed_alive** | 2026-05-21 — all three sourcetables retrieved successfully (BKG 221 STR, ROB 215 STR, ASI 202 STR). |
| **datum_epoch** | **ETRS89**, realised in EPN coordinates products as four parallel frames: **ITRF2020(IGc20) / ETRF2000 / ETRF2014 / ETRF2020**. Per EPN Central Bureau positions & velocities page (https://epncb.oma.be/_productsservices/coordinates/): the cumulative multi-year solution is aligned to IGc20 (the ITRF2020 reference solution); the EPN-repro3 preliminary solution labels its global frame as "IGS20"; both are ITRF2020 realisations. The RTCM stream does not encode the frame; the operator-declared frame is the EPN frame above. |
| **Operator statements on RTK use** | ROB registration page: *"The provided raw GNSS data streams are unsuitable for operational real-time kinematic positioning."* BKG and ASI make no equivalent statement. None of the three publishes a VRS / network RTK product. |

---

## Federation members (live probes 2026-05-21)

### BKG — Bundesamt für Kartographie und Geodäsie (Germany)

| Field | Value |
|---|---|
| **Operator** | BKG, Frankfurt am Main |
| **landing_url** | https://igs.bkg.bund.de/ntrip/ (BKG NTRIP infrastructure hub) — alternative: `https://euref-ip.net/home` (caster home page) |
| **access_url** | http://register.rtcm-ntrip.org/cgi-bin/registration.cgi (single form covers BKG EUREF-IP, BKG IGS-IP, BKG products.igs-ip.net) |
| **host:port** | `euref-ip.net:2101` (HTTP), also `:80`. **HTTPS** confirmed live on `:443` (same sourcetable contents). |
| **Caster banner** | `NTRIP BKG Caster 2.0.48/2.0` |
| **STR rows** | 221 (probe 2026-05-21; 218 on 2026-05-13 — minor day-to-day fluctuation) |
| **NET groups** | EUREF (146), IGS (66), MISC (8), GREF (1) |
| **Format** | RTCM 3.3 (176), RTCM 3.2 (36), RTCM 3.1 (7) |
| **Constellations** | ~75 % carry GPS+GLO+GAL+BDS; remainder add QZS/SBAS/IRS or drop one or two systems |
| **Solution column (13)** | 209 raw observations (`0`) + 12 derived/network (`1` — SSR feeds, EUREF01/02 BRDC mountpoints, GFZ-relayed IGS streams) |
| **Authentication (col 16)** | 220 require Basic auth (`B`); 1 open (`N`) — `DELF00NLD0` (TU Delft) is open access |
| **Fee column (17)** | 218 free (`N`); 3 marked `Y` — Austrian APOS/BEV streams (PFA300AUT0, SBG200AUT0, TRF200AUT0). `Y` indicates upstream paywall on the source side; on BKG caster they remain gated behind the BKG account, and Austrian APOS upstream authorisation may also apply. |
| **NMEA flag (col 12)** | All 221 rows are `0` (no GGA upload required) |
| **Required form fields** | Family Name, First Name, Organization/Agency, Organization Type (14-option dropdown), Country, E-Mail, User-Name, Password, Application (free-text); BKG privacy-policy consent |
| **Approval timing** | Manual approval during BKG working hours; no published SLA |
| **Contact** | `euref-ip@bkg.bund.de` ; `igs-ip@bkg.bund.de` (registration support) |
| **Terms language** | "Best effort", no SLA, no commercial/non-commercial split, citation requested in publications |
| **Relayed-caster count (CAS rows)** | 5 — itself, ROB, ASI (two entries), and `rtcm-ntrip.org` info caster |

### ROB — Royal Observatory of Belgium

| Field | Value |
|---|---|
| **Operator** | Royal Observatory of Belgium (ROB), Brussels (also `gnss.be`) |
| **landing_url** | https://www.euref-ip.be/ |
| **access_url** | https://www.euref-ip.be/user-registration/user-registration-main-page.php (CAPTCHA-gated signup) |
| **host:port** | `www.euref-ip.be:2101` (HTTP). Also `euref-ip.be:2101` (same caster) |
| **TLS** | `www.euref-ip.be:2102` (HTTPS, non-standard port, confirmed live 2026-05-21) |
| **Caster banner** | `NTRIP BKG Caster 2.0.48/2.0` (ROB uses BKG caster software) |
| **STR rows** | 215 (probe 2026-05-21; 214 on 2026-05-13) |
| **NET groups** | EUREF (206), PROPOSED (4), IGS (1), MISC (4) |
| **Format** | RTCM 3.2 (161), RTCM 3.3 (34), RTCM 3.1 (17), RTCM 3.0 (2) — ROB skews toward RTCM 3.2; BKG skews toward RTCM 3.3 |
| **Constellations** | ~66 % carry GPS+GLO+GAL+BDS; rest GPS+GLO/GAL only or +QZS/+SBAS |
| **Authentication** | 208 require Basic auth; 7 are open (`N`) |
| **Fee column** | 213 free (`N`); 2 marked `Y` (Austrian APOS streams) |
| **NMEA flag** | All 215 rows have NMEA=0 |
| **Required form fields** | First name, last name, email, affiliation, address, city, country code, username, password, "Purpose" free-text; CAPTCHA required |
| **Approval timing** | Manual approval "during normal working hours" — holiday delays possible |
| **Explicit RTK disclaimer** | *"The provided raw GNSS data streams are unsuitable for operational real-time kinematic positioning."* (ROB registration page) |
| **Stream upload** | ROB consumer credentials cannot be used to push streams to the broadcaster (read-only) |
| **Relayed-caster count (CAS rows)** | 23 — ROB itself, BKG, ASI, plus 20 external upstream casters (ergnss-ip.ign.es, rgp-ip.ign.fr, ntrip1.os.co.uk, cpos.kartverket.no, ntripdist-swepos.lm.se, skpos.gku.sk, ntrip1.gnssnet.hu, tpp.swipos.ch, sulp.polynet.lviv.ua, agh.edu.pl Poland, ntrip.pecny.cz, ICV Valencia, IGEO Portugal, two Italian university casters, mgex.igs-ip.net, www.igs-ip.net, rtcm-ntrip.org) |

### ASI — Agenzia Spaziale Italiana / e-GEOS (Italy)

| Field | Value |
|---|---|
| **Operator** | Agenzia Spaziale Italiana (ASI) / e-GEOS, Matera Space Geodesy Centre |
| **landing_url** | http://geodaf.mt.asi.it/gps_caster_access.php (ASI Broadcaster access info page) |
| **access_url** | http://geodaf.mt.asi.it/gps_caster_access.php (CAPTCHA-gated signup form on same page — **ASI has its own separate registration; the BKG form does not cover ASI**) |
| **host:port** | `euref-ip.asi.it:2101` (HTTP) — also `192.106.234.17:2101` |
| **TLS** | None — `:443` on `euref-ip.asi.it` refused TCP connect (2026-05-13 + 2026-05-21). ASI is HTTP-only on `:2101`. |
| **Caster banner** | `NTRIP BKG Caster 2.0.37/2.0` (slightly older BKG software than BKG/ROB) |
| **STR rows** | 202 (probe 2026-05-21; 201 on 2026-05-13) |
| **NET groups** | EUREF (174), ASI (22), IGS (4), GREF (1), REGINA (1) — ASI also exposes its own NET group |
| **Format** | RTCM 3.0 (48), RTCM 3.1 (68), RTCM 3.2 (39+1), RTCM 3.3 (40), RTCM 3 (3) — markedly older mix than BKG/ROB |
| **Required form fields** (ASI form, observed 2026-05-21) | Family Name, First Name, Organization/Agency, E-Mail, username (max 15 chars), password (max 15 chars), Application (keywords); checkbox consent to inclusion in public online users list; CAPTCHA |
| **Form notes** | "The user ID and password you will receive by email in response to your request is only valid for personal use. Keep it confidential." Manual processing, "give us few days to process your request." Free of charge. |
| **Relayed-caster count (CAS rows)** | 1 — itself |

---

## What's actually in the sourcetables (consolidated)

### Mountpoint naming convention

EPN stations follow the **IGS station 9-character + monument-number convention**: `XXXXMMCCCS` where:
- `XXXX` = 4-char station code (e.g. `PCAR`, `REYK`, `NICO`, `AGRN`)
- `MM` = monument number (`00` is the default for most)
- `CCC` = ISO-3 country code (`AND`, `ISL`, `CYP`, `ITA`, `ESP`, `DEU`, ...)
- `S` = solution / antenna identifier digit (almost always `0`)

Example mountpoints: `PCAR00AND0` (Andorra), `REYK00ISL0` (Iceland), `NICO00CYP0` (Cyprus), `AGRN00ITA0` (Agrigento Italy), `ALAC00ESP0` (Alicante Spain).

A small number of non-station mountpoints carry SSR/BRDC products on BKG only:
`EUREF01`, `EUREF02`, `SSRA02IGS0_EUREF`, `SSRA02IGS1_EUREF`, `SSRA03IGS0_EUREF`, `SSRA03IGS1_EUREF`, `BCEP00BKG0` — all RTCM 3.1 with SSR (1057–1268, 4076_xxx) messages; for PPP, not RTK.

### NET group glossary

The federation sourcetables tag each STR with one NET group. Meanings:

- **EUREF** — EPN reference stations formally accepted into the EUREF Permanent Network. Authoritative network list: https://epncb.oma.be/.
- **IGS** — IGS reference stations that are also mirrored on EUREF-IP (mostly European IGS sites). Same stations also stream on IGS-IP.
- **PROPOSED** — Candidate EPN stations under evaluation, not yet formally accepted. On ROB 2026-05-21: ASGA00CYP0 (Cyprus), ECH200LUX0 (Luxembourg), PCAR00AND0 (Andorra), TROS00LUX0 (Luxembourg). Source: https://epncb.oma.be/_networkdata/proposed.php — "Proposed Stations" list maintained by the EPN Central Bureau.
- **MISC** — Non-EPN mountpoints, including the BKG SSR products (`EUREF01`, `EUREF02`, `SSRA*`), plus a few legacy or experimental streams.
- **GREF** — BKG's German national reference network (Integrated Geodetic Reference Network, ~30 stations across Germany). One mountpoint `WT2100DEU0` (Wettzell) tagged GREF appears on both BKG and ASI. Operator page: https://gref.bkg.bund.de/.
- **REGINA** — REseau GNSS pour l'IGS et la Navigation, a global ~40-station network operated by CNES (France) + IGN (France), not by ASI. One station `GVDG00GRC0` (Greece) tagged REGINA appears on ASI. Project page: https://regina.cnes.fr/.
- **ASI** — ASI's own Italian national GNSS frame network (46 stations across Italy, completed 2021). 22 streams on the ASI broadcaster. Source: https://www.asi.it/en/2021/11/the-italian-space-agency-completes-the-new-national-gnss-frame-network/.

### Real-time station count (EPNCB authoritative)

The EPNCB real-time map (`https://epncb.oma.be/_networkdata/data_access/real_time/map.php`) listed **229 EPN stations with active real-time streams** on 2026-05-13. Each broadcaster carries a subset; per live set-diff 2026-05-21:

- **BKG**: 221 STR rows (largest; carries IGS-cross-listings and the SSR products). 7 mountpoints only on BKG: `CNNE00FRA0`, `ENIS00GBR0`, `EUREF01`, `EUREF02`, `FOYL00GBR0`, `IGNE00ESP0`, `TEOS00ITA0`.
- **ROB**: 215 STR rows (highest EPN-only coverage). 1 mountpoint only on ROB: `BORR00ESP0` (Borredà, Spain — relayed from `ergnss-ip.ign.es`).
- **ASI**: 202 STR rows (subset of BKG; mostly Italian and southern European stations; also exposes its own ASI-tagged 22 streams).
- **Union across all three**: 222 mountpoints. Minus 7 non-physical SSR/BRDC mounts (EUREF01, EUREF02, BCEP00BKG0 [if present], 4 SSRA…IGS… products on BKG) = **215 unique physical CORS**.
- `METG00FIN0` (Metsähovi, Finland) is present on all three broadcasters (not unique to ROB; the earlier version of this file inverted the diff).

The ~14-station gap between the federation union (215) and the EPNCB authoritative count (229) is EPN stations streamed via upstream casters not aggregated into the three federated broadcasters, or temporarily inactive at probe time.

### RTCM versions and constellations

Format spread across the three broadcasters:
- **BKG**: majority RTCM 3.3, all with full multi-constellation MSM messages.
- **ROB**: majority RTCM 3.2.
- **ASI**: mixed including older RTCM 3.0 (48 streams) and RTCM 3.1 (68 streams) — ASI carries the most legacy-format streams in the federation.

Constellation breakdown is dominated by **GPS+GLO+GAL+BDS**; some streams add QZS or SBAS depending on receiver type.

### Important quirks

- **NMEA=0 throughout** all three: no GGA upload required. Pipeline-friendly (default `nmea_filter=True` keeps EUREF-IP rows).
- **Solution=1 rows** (12 on BKG, fewer on ROB): SSR product mountpoints and a small set of IGS-relayed processed streams. Project's default `solution_filter=True` drops these (they are not raw single-station observations).
- **Authentication=N (open) rows are rare**: 1 on BKG (TU Delft `DELF00NLD0`), 7 on ROB. Accessible anonymously but still EPN-controlled.
- **Fee=Y rows** (3 Austrian APOS streams on BKG, 2 on ROB): These are relayed from BEV/APOS Austria. The EUREF-IP account may not be sufficient — Austrian APOS gating likely applies upstream.

---

## Registration, access, and use restrictions

### How registration works

**There is no federated single-sign-on.** A user must register separately with each broadcaster they want to consume:

1. **BKG (`register.rtcm-ntrip.org`)** — single form covers BKG-EUREF-IP, IGS-IP, products.igs-ip.net. Manual approval by BKG staff; credentials emailed back. Required: name, organisation, organisation type, country, email, chosen username/password, application description, privacy-policy consent.
2. **ROB (`www.euref-ip.be/user-registration/`)** — separate form, CAPTCHA, manual approval by ROB staff. Required: name, email, affiliation, address, city, country code, chosen username/password, "Purpose" free-text. Page explicitly states streams are unsuitable for operational RTK.
3. **ASI (`geodaf.mt.asi.it/gps_caster_access.php`)** — separate form, CAPTCHA, manual approval by ASI staff. Required: name, organisation, email, username (≤15 chars), password (≤15 chars), application keywords; consent to include account on public users list. Personal-use only.

### Access model

- All three are **free of charge**. No VAT.
- Approval is **manual**, typically within a few business days; holiday delays expected.
- Accounts are **per-broadcaster**, not federated.
- BKG and ROB casters accept **Basic auth over HTTP or HTTPS**. ROB's HTTPS lives on port 2102 (non-standard); BKG offers HTTPS on standard 443. ASI is HTTP-only.

### Use restrictions

- **No explicit non-commercial or residency clause** on any of the three. All three forms accept any country.
- **ROB statement**: registration page states streams are "unsuitable for operational real-time kinematic positioning." BKG and ASI make no equivalent statement.
- **ASI**: credentials are stated to be valid only for personal use; account holder is asked to keep credentials confidential and ASI publishes account-holders on a public users list.
- **No throttling published** on any of the three; BKG documentation notes that NTRIP relay operators can request expanded simultaneous-stream quotas (5–50) by emailing BKG.
- **Citation request**: BKG asks that users include a citation in publications. No legal enforcement.

---

## Cross-references from country files (verified 2026-05-13, re-checked 2026-05-21)

Each row below verifies whether the station the country file claims streams via EUREF-IP actually appears in any of the three federated sourcetables today.

| Country file | Cited EPN station | In BKG? | In ROB? | In ASI? | Notes |
|---|---|:-:|:-:|:-:|---|
| `AD_Andorra.md` | `PCAR00AND0` (Pic de Carroi) | yes (RTCM 3.3 GPS+GLO+GAL+BDS) | yes (RTCM 3.2 PROPOSED) | yes (RTCM 3.2) | Upstream is `185.194.59.113:2101/PCAR3M` (Leica GR50 receiver, direct public IP). All three broadcasters relay from the same upstream. |
| `AD_Andorra.md` | `RULL` (second ERGAND station) | no | no | no | No RULL or `RULL*` row in any of the three sourcetables. Not streaming real-time via EUREF-IP. |
| `CY_Cyprus.md` | `NICO00CYP0` | yes (RTCM 3.3, IGS network class) | yes (RTCM 3.0 + RTCM 3.2) | yes | EUREF-IP carries NICO00CYP0 on all three broadcasters. Also on IGS-IP. Baseline ~20 km from Nicosia city centre. |
| `AX_AlandIslands.md` | `MARI` (Mariehamn EPN station) | no | no | no | No MARI or `MAR*` 9-char mountpoint in any EUREF-IP sourcetable 2026-05-21. AX file's note that EPN MARI "may stream real-time RTCM via euref-ip.net" is not currently true. |
| `IS_Iceland.md` | `REYK00ISL0` (Reykjavik IGS station) | yes (RTCM 3.3) | yes (RTCM 3.0 + RTCM 3.2) | yes | Baseline ~15 km from Reykjavik centre. Also carried by IGS-IP (`www.igs-ip.net:2101/REYK00ISL0`). |
| `SJ_Svalbard.md` | `NYA2` / `NABG` Ny-Ålesund | yes (NABG00NOR0 + NYA200NOR0, both RTCM 3.3) | yes (both) | no (ASI does not carry them) | NABG and NYA2 reachable via BKG and ROB EUREF-IP. NYA2 on BKG is `solution=1` (derived/processed at GFZ-Potsdam) rather than raw observation. Also on IGS-IP. |
| (no `GI_Gibraltar` file) | `BIGF`/`GIBR` station mention | no | no | no | No GIBR* or BIGF* mountpoint in any EUREF-IP sourcetable. BIGF (British Isles Continuous GNSS Facility) data flows are separate. Closest live EPN: `MALA00ESP0` Malaga, `ALGE00ESP0` Algeciras. |

### Other EPN stations verified live 2026-05-21

EPN stations on the EUREF-IP federation as of 2026-05-21 not currently cross-referenced in country files:

- **`ASGA00CYP0`** (Asgata, southern Cyprus, RTCM 3.2 MSM, BKG+ROB)
- **`MIKL00UKR0`** / **`SULP00UKR0`** (Ukraine western stations via `sulp.polynet.lviv.ua` relay)
- **`LROC00FRA0`** / **`TLSE00FRA0`** etc. (French stations, mostly relayed from `rgp-ip.ign.fr`)
- **`LEIJ00DEU0`** (Leipzig, BKG only — not on ROB)

---

## Confusion resolution: EUREF-IP vs IGS-IP vs products.igs-ip.net

| | EUREF-IP (`euref-ip.net:2101` + ROB + ASI) | IGS-IP (`www.igs-ip.net:2101`) | products.igs-ip.net (`:2101`) |
|---|---|---|---|
| **Operator** | BKG + ROB + ASI federation | BKG (single caster) | BKG (single caster) |
| **Scope** | Regional — EPN reference stations across Europe | Global — IGS reference stations worldwide | Global — IGS Real-Time Service SSR products |
| **What's on it** | ~202–221 raw observation streams (RTCM 3.x); few SSR mountpoints on BKG | 386 raw observation streams from the global IGS network | 91 SSR product streams (orbits/clocks/biases) for PPP |
| **Stream type** | Single-base raw observations (RTCM 3.x). No NRTK. | Single-base raw observations (RTCM 3.x). | SSR product streams. PPP only — requires PPP-capable receiver (e.g. BNC, RTKLIB-SSR). |
| **Registration** | BKG: `register.rtcm-ntrip.org` covers BKG-EUREF-IP + BKG IGS-IP + BKG products.igs-ip.net. **ROB and ASI: separate forms.** | Same BKG form | Same BKG form |
| **TLS** | BKG `:443`, ROB `:2102`, ASI none | BKG `:443` | BKG `:443` |
| **Frame/epoch** | ETRS89 (ETRF2000/2014/2020); also ITRF2020(IGc20) | IGS20 (= ITRF2020-derived) | IGS20 |

See `IGS-IP.md` for IGS-IP and products.igs-ip.net details.

---

## Recent and planned changes (2024–2026)

### EPN → EPOS integration (formalised at 2025 EUREF Symposium, Covilhã)

Per the December 2025 EUREF newsletter (Issue 6) and Resolution No. 1 of the 2025 EUREF Symposium:

- All EPN stations will, by default, be included in the GNSS network of EPOS (European Plate Observing System).
- EPN metadata (M3G) and RINEX archive data will gradually become discoverable within EPOS starting **2026**.
- **No published change to real-time NTRIP access or terms** as of 2026-05-21. The three EUREF-IP broadcasters continue to operate under existing registration models.
- The EPOS integration affects historical/archive data discoverability, not the live RTCM streams or their authentication.

### Reference-frame realisation

EPN coordinates are now published in four parallel reference frames per EPN Central Bureau: ITRF2020(IGc20) for the cumulative multi-year solution (or "IGS20" for the EPN-repro3 preliminary solution — both are ITRF2020 realisations), ETRF2000, ETRF2014, and ETRF2020. The 2022 IGS switch to **IGS20/igs20.atx** (effective GPS week 2238, 2022-11-27) cascaded to the EPN solutions; ETRF2020 is the latest ETRS89 realisation aligned to ITRF2020. Operational tip: ETRF2014 may be preferred for high-precision applications with better consistency to ITRF2014, whereas ETRF2000 retains agreement with neighbour-country realisations.

### Next EUREF Symposium

23–25 June 2026, ENSA Paris-Val de Seine, France. No public agenda items signalling changes to EUREF-IP access policy.

### Broadcaster software refresh

BKG and ROB casters were running `NTRIP BKG Caster 2.0.48/2.0` on 2026-05-21; ASI runs older 2.0.37 build. ROB additionally relays from 20+ external upstream casters in its sourcetable. No operator changes announced for 2026.

### What 2024–2026 did NOT change

- All three broadcasters remain free with registration.
- Per-broadcaster account model (no federation SSO) is unchanged.
- No VRS / network RTK product added on any of the three; streams remain raw single-base observations.
- No new TLS port additions beyond what's documented above.

---

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| **EPN Central Bureau RINEX archive** (all 280+ EPN stations, daily/hourly/15-min RINEX) | https://epncb.oma.be/ftp/ | Free (EPN data policy) |
| **BKG GNSS data archive** | https://igs.bkg.bund.de/ | Free with registration |
| **IGS data archive (global IGS stations)** | https://igs.org/data-access/ and various IGS data centres | Free |

---

## Sources Consulted

- EPN Central Bureau: https://epncb.oma.be/
- EPN Real-Time map: https://epncb.oma.be/_networkdata/data_access/real_time/map.php
- EPN NTRIP broadcaster list: https://epncb.oma.be/_networkdata/data_access/real_time/broadcasters.php
- EPN positions & velocities (frame/realisation): https://epncb.oma.be/_productsservices/coordinates/
- EUREF-IP BKG (`euref-ip.net`): https://euref-ip.net/home
- EUREF-IP ROB (`www.euref-ip.be`): https://www.euref-ip.be/
- ROB user registration: https://www.euref-ip.be/user-registration/user-registration-main-page.php
- BKG user registration (single form for BKG EUREF-IP + IGS-IP + products.igs-ip.net): http://register.rtcm-ntrip.org/cgi-bin/registration.cgi
- ASI EUREF-IP registration: http://geodaf.mt.asi.it/gps_caster_access.php
- IGS-IP caster home (background): https://igs.bkg.bund.de/ntrip/
- products.igs-ip.net caster home: https://products.igs-ip.net/home
- IGS20 reference-frame announcement (2022): https://igs.org/news/igs20/
- BKG NTRIP infrastructure: https://igs.bkg.bund.de/ntrip/
- EUREF Newsletter Issue 6 (2025-12-22, EPN→EPOS integration starting 2026): http://www.epncb.oma.be/_documentation/newsletters/EUREF_Newsletter_2025_01.pdf
- EPN Wikipedia: https://en.wikipedia.org/wiki/EUREF_Permanent_Network
- GNSS.be EUREF page: https://gnss.be/activities-EUREF.php

### Live probes (2026-05-21)

- `curl --http0.9 http://euref-ip.net:2101/` → `SOURCETABLE 200 OK`, `NTRIP BKG Caster 2.0.48/2.0`, **221 STR**, 4 NET, 5 CAS
- `curl --http0.9 http://www.euref-ip.be:2101/` → `SOURCETABLE 200 OK`, `NTRIP BKG Caster 2.0.48/2.0`, **215 STR**, 4 NET, 23 CAS
- `curl --http0.9 http://euref-ip.asi.it:2101/` → `SOURCETABLE 200 OK`, `NTRIP BKG Caster 2.0.37/2.0`, **202 STR**, 5 NET, 1 CAS
- `curl --http0.9 -k https://euref-ip.net:443/` → 221 STR; TLS confirmed live
- `curl --http0.9 -k https://www.euref-ip.be:2102/` → 215 STR; TLS confirmed live on non-standard port
- `curl https://euref-ip.asi.it:443/` → connection refused; ASI is HTTP-only on `:2101`
- Earlier probes (2026-05-13) recorded BKG 218 / ROB 214 / ASI 201 — same federation members and behaviours; intra-week count fluctuation of ±1 is normal as individual stations come and go.

### Cross-references inspected in `docs/ntrip_research/`

- `AD_Andorra.md`, `CY_Cyprus.md`, `AX_AlandIslands.md`, `IS_Iceland.md`, `SJ_Svalbard.md`, `BE_Belgium.md`, `DE_Germany.md`, `IT_Italy.md`, `HT_Haiti.md`, `CW_Dutch_Caribbean.md`.
