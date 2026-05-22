# IGS-IP — Global IGS Real-Time Broadcaster (BKG)

**Date researched:** 2026-05-21 (live probes of `www.igs-ip.net:2101` and `products.igs-ip.net:2101`; BKG/IGS portal pages).

> **Scope note.** Not a country entry. IGS-IP is BKG's global counterpart to
> EUREF-IP: a single NTRIP broadcaster (`www.igs-ip.net:2101`) operated by the
> Bundesamt für Kartographie und Geodäsie (BKG, Germany) that disseminates
> raw real-time RTCM 3.x observation streams from the worldwide IGS reference
> station network. Several country files reference IGS-IP for a single IGS
> station in or near them — this file is the consolidated source.
>
> Sister caster `products.igs-ip.net:2101` carries SSR product streams
> (IGS Real-Time Service: orbits, clocks, biases) for PPP. Documented here
> for completeness; it is **not** an RTK observation stream and is out of
> scope for the project's standard-RTK pipeline.

## Status: ACTIVE — caster reachable 2026-05-21; 386 STR mountpoints (raw RTCM 3.x global IGS observations); free with BKG account.

| Field | Value |
|---|---|
| **Caster name** | IGS-IP — IGS NTRIP broadcaster |
| **Operator** | Bundesamt für Kartographie und Geodäsie (BKG), Frankfurt am Main, in support of the IGS Real-Time Working Group (RTIGS) |
| **landing_url** | https://igs.bkg.bund.de/ntrip/ (BKG NTRIP hub — describes the three BKG broadcasters and their purpose) |
| **access_url** | http://register.rtcm-ntrip.org/cgi-bin/registration.cgi (single BKG registration form covers IGS-IP, EUREF-IP and products.igs-ip.net) |
| **host:port** | `www.igs-ip.net:2101` (HTTP); also reachable on `:80` and `:443` (HTTPS). Probed 2026-05-21. Sister product caster: `products.igs-ip.net:2101`. |
| **tariff** | Free of charge. BKG registration form (http://register.rtcm-ntrip.org/cgi-bin/registration.cgi) explicitly states "apply for free real-time access to GNSS data streams" (observed 2026-05-21). VAT n/a (no charge). No commercial tier. |
| **num_stations** | ~370 physical IGS reference stations streaming via this caster, based on 386 STR rows minus a few SSR/derived/MGEX mountpoints (`solution=1` rows: 36 of 386). The IGS global network itself comprised **534 stations** as of 2026-05-21 (network.igs.org tracker) — IGS-IP carries the real-time-enabled subset. |
| **vrs** | No. All streams are single-base raw observations (`NMEA=0` on all 386 rows; no GGA upload). No NRTK/VRS product. |
| **hobbyist_eligibility** | Yes. BKG registration form's "Organization Type" dropdown includes non-institutional categories; form is approved manually but no profession filter. |
| **legal_residency_required** | No. BKG country dropdown is global; no geographic restriction. |
| **last_confirmed_alive** | 2026-05-21 — `curl --http0.9 http://www.igs-ip.net:2101/` returned `SOURCETABLE 200 OK`, server banner `NTRIP ntrips 2.0.69274/1.0`, 386 STR rows, 2 CAS rows, 4 NET groups (EUREF/IGS/MGEX/MISC). HTTPS on `:443` confirmed live with same payload. |
| **datum_epoch** | **IGS20** (= ITRF2020-derived global frame; epoch 2015.0 per ITRF2020 definition), effective for all IGS operational products from GPS week 2238 (2022-11-27). Source: IGS announcement `https://igs.org/news/igs20/`. Individual IGS station RTCM observation streams carry only positions, not a frame declaration — IGS20 is the operator-declared frame of the underlying station network. |

---

## What's in the sourcetable (live 2026-05-21)

### NET group breakdown

| NET group | STR count |
|---|---|
| IGS | 364 |
| MGEX | 4 |
| MISC | 18 |
| **Total** | 386 |

MGEX (Multi-GNSS Experiment) stations and MISC mountpoints share the same caster. EUREF NET group is exposed in the sourcetable header (NET row) for cross-reference but no STR rows currently carry the EUREF tag — those live on the EUREF-IP federation, not on IGS-IP.

### Country distribution (top 25, of 105 countries represented)

| ISO-3 | STR rows | ISO-3 | STR rows |
|---|---|---|---|
| USA | 49 | DEU | 14 |
| CAN | 32 | JPN | 12 |
| AUS | 24 | ITA | 10 |
| BRA | 23 | ATA (Antarctica) | 10 |
| ESP | 14 | SWE | 9 |
| ZAF | 8 | NZL | 8 |
| ARG | 8 | FRA | 7 |
| CHL | 6 | PRT | 5 |
| POL | 5 | GBR | 5 |
| PYF | 4 | NOR | 4 |
| CHN | 4 | UZB | 3 |
| SGP | 3 | NLD | 3 |
| NCL | 3 | | |

Long tail: 80+ additional countries each with 1–2 streams. Notable: 10 in Antarctica, full coverage of Pacific island stations (PYF, NCL, MHL, FSM, TUV, KIR, WSM, etc.).

### Stream characteristics

| Field | Value | Count |
|---|---|---|
| Format | RTCM 3.3 | 256 |
| | RTCM 3.2 | 102 |
| | RTCM 3.1 | 11 |
| | RTCM 3.0 | 1 |
| | RAW (binary) | 11 |
| | RTCM 2.3 | 2 |
| | Other | 3 |
| `nmea` (col 12) | 0 (no GGA upload required) | 386/386 |
| `solution` (col 13) | 0 (raw observation) | 350 |
| | 1 (derived/processed) | 36 |
| `authentication` (col 16) | B (Basic auth) | 377 |
| | D (Digest auth, per NTRIP STR spec — https://software.rtcm-ntrip.org/wiki/STR) | 9 |
| `fee` (col 17) | N (free) | 386/386 |

### Receiver mix

Sourcetable column 14 (manufacturer) is dominated by the Septentrio POLARX5 family (134 streams = POLARX5 101 + POLARX5TR 26 + POLARX5S 5 + POLARX5E 2), Trimble NETR9 / Alloy (~97: NETR9 45 + Alloy 43 + Alloy-upper 7 + NETR8 2), Javad TRE_3xx / TRE_G3xx variants (~55: TRE_G3TH 33, TRE_3 6, TRE_G3T 5, TRE_3S 4 etc.), Leica GR series (46: GR50 30, GR30 7, GR10 5, GR25 4). The relay aggregator "euronet" appears on 21 streams; "NRCanRTCM" on 13. All multi-constellation capable.

### Pipeline relevance

NMEA=0 throughout (no GGA upload required) → fetch_stations.py default `nmea_filter=True` keeps all IGS-IP rows. Solution=1 rows (36) are processed/relayed feeds (euronet aggregator, NRCanRTCM-derived streams, a few SSR-tagged rows); default `solution_filter=True` drops them. For accurate per-station tagging in the project's pipeline, IGS-IP should be treated like EUREF-IP — single-base raw observations, regional country tag in column 9 = ISO-3 of the underlying station.

**Carrier=0 quirk:** 12 STR rows publish `carrier=0` despite carrying real RTCM 3.2/3.3 observation streams (CEBR00ESP0, FAA100PYF0, KIRU00SWE0, KIT300UZB0, KOUR00GUF0, LPGS00ARG0, MAL200KEN0, MAS100ESP0, MGUE00ARG0, NNOR00AUS0, REDU00BEL0, VILL00ESP0). The project pipeline drops `carrier ∉ {1,2,3}` (DGNSS filter), so these 12 IGS stations are silently dropped from the map even though they stream phase observations. Operator-side mislabel; resolving requires a per-station override (`carrier=2` based on RTCM 3 format).

---

## Sister caster: `products.igs-ip.net:2101`

| Field | Value |
|---|---|
| **landing_url** | https://products.igs-ip.net/home (operator-owned info page) |
| **host:port** | `products.igs-ip.net:2101` (HTTP), `:80`, `:443` (HTTPS, confirmed) |
| **Caster banner** | `NTRIP BKG Caster 2.0.48/2.0` (same software as EUREF-IP BKG; different from IGS-IP's `ntrips 2.0.69274`) |
| **STR rows** | 91 (probed 2026-05-21): 11 with `solution=0`, 80 with `solution=1` (SSR products) |
| **NET groups** | IGS (21), MISC (70) |
| **Format** | RTCM 3.1 (70), RTCM 3.3 (8), RTCM 3.2 (2), other (11) — predominantly RTCM 3.1 carrying SSR messages (1057–1268, 4076_xxx) |
| **Stream type** | IGS Real-Time Service (RTS) **SSR product streams**: precise orbits, clocks, code/phase biases. Plus a few BCEP-prefixed Broadcast-Ephemeris carriers. Not OSR observations. |
| **What it enables** | PPP (Precise Point Positioning) in real time using a PPP-capable client (e.g. BNC, RTKLIB-SSR). Cm-level convergence in tens of minutes globally, no base needed. |
| **Registration** | Same BKG form as IGS-IP / EUREF-IP |
| **Out of scope** | This project is RTK-focused. PPP via SSR is documented for awareness only; not surfaced on the RTK map. |

---

## Registration, access, and use restrictions

### How to register

BKG operates a single web form for all three of its broadcasters (EUREF-IP, IGS-IP, products.igs-ip.net):

- URL: `http://register.rtcm-ntrip.org/cgi-bin/registration.cgi`
- Required fields: Family Name, First Name, Organization/Agency, Organization Type (dropdown, 14 options including non-institutional categories), Country (global dropdown), E-Mail, User-Name, Password, Application (free-text purpose), terms-of-service consent.
- Manual approval by BKG staff; credentials emailed back. No published SLA; "few business days" typical.
- Contact: `igs-ip@bkg.bund.de` (per `products.igs-ip.net/home` page).

### Terms

The registration form states:

- Service is "best effort"; BKG "makes no assurances, implied or otherwise, for the accuracy or availability of the Service".
- User indemnifies BKG against third-party claims.
- Per-account default quota: up to ~5 simultaneous streams. Users needing 5–50 simultaneous streams may request expanded access by emailing BKG.
- No explicit prohibition on commercial use; no residency requirement; no professional-licensing filter.
- Account is for "personal use" (per ASI form wording; BKG form does not state this) — user-side credential confidentiality expected.

### Relationship to other RTS broadcasters

The IGS Real-Time Service is hosted by multiple casters per the IGS RTS user-access page (`https://igs.org/rts/user-access/`):

1. **BKG** (`www.igs-ip.net:2101`, `products.igs-ip.net:2101`, `euref-ip.net:2101`) — this file.
2. **CAS** — IGS Regional Data Center Asia; separate caster.
3. **CDDIS** (NASA) — separate caster with two-step registration.
4. **Geoscience Australia** — `auscors.ga.gov.au:2101` (covered separately in `AU_Australia.md`).
5. **UCAR** — former IGS Central Bureau caster.

Each caster requires its own registration. They are not federated.

---

## Cross-references to country files

Country files that cite an IGS station as their only/primary EUREF-IP- or IGS-IP-served stream should point to this file for the global IGS-IP caster facts.

Live spot-checks 2026-05-21 (from the 386-row sourcetable):

- `IS_Iceland.md` — `REYK00ISL0` Reykjavik IGS station: streams via IGS-IP (RTCM 3.3, SEPT POLARX5).
- `SJ_Svalbard.md` — `NABG00NOR0`, `NYA200NOR0` Ny-Ålesund: also via IGS-IP (relay).
- `CY_Cyprus.md` — `NICO00CYP0` Nicosia IGS station: present on IGS-IP (RTCM 3.3, IGS network class).
- `GL_Greenland.md` / `IS_Iceland.md` references — IGS-IP carries `KELY00GRL0` (Kellyville), `THU200GRL0` (Thule), `REYK00ISL0` and several others.
- Non-EU stations (USA, BRA, AUS, JPN, etc.) → IGS-IP is the relevant federation when no national caster is documented for the hobbyist.

For European stations specifically, **EUREF-IP is more comprehensive** (218 STR on BKG, vs ~5 EU IGS sites on IGS-IP) — IGS-IP is the right entry point only outside Europe or for the global IGS subset (e.g. MGEX experimental streams).

---

## Recent and planned changes (2024–2026)

### IGS20 reference frame (effective 2022-11-27)

All IGS operational products switched from IGb14/igs14.atx to **IGS20/igs20.atx** at GPS week 2238 (27 November 2022). IGS20 is an extract of ITRF2020 coordinates for selected IGS stations with stable position time series. IGS station coordinates served by IGS-IP receivers are therefore in the IGS20 frame, although the RTCM stream itself does not declare a frame (DF021 ITRF year field rarely populated; receivers default to using the position encoded by the operator). Source: https://igs.org/news/igs20/.

### Network growth

IGS network station count: **534 as of 2026-05-21** (network.igs.org tracker). 386 of those stream real-time observations via IGS-IP. The remaining ~150 are post-process / RINEX-archive only.

### No registration policy changes

BKG registration form unchanged in 2026; same free-with-account model that has been in place since 2002.

---

## Post-processing / RINEX fallback

| Service | URL | Cost |
|---|---|---|
| IGS data archives (multiple) | https://igs.org/data-access/ | Free |
| BKG GNSS data archive | https://igs.bkg.bund.de/ | Free with registration |
| NASA CDDIS | https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/ | Free with registration |

---

## Confusion resolution: IGS-IP vs EUREF-IP vs products.igs-ip.net

These three BKG-operated casters are operationally distinct:

| | IGS-IP (`www.igs-ip.net:2101`) | EUREF-IP (`euref-ip.net:2101` + ROB + ASI) | products.igs-ip.net (`:2101`) |
|---|---|---|---|
| **Operator** | BKG (single caster) | BKG + ROB + ASI federation | BKG (single caster) |
| **Scope** | Global — IGS reference stations worldwide | Regional — EPN reference stations across Europe | Global — IGS Real-Time Service SSR products |
| **What's on it** | 386 raw observation streams (RTCM 3.x) | ~214–219 raw observation streams (RTCM 3.x) | 91 SSR product streams (orbits/clocks/biases) for PPP |
| **Caster software** | `NTRIP ntrips 2.0.69274/1.0` | `NTRIP BKG Caster 2.0.48/2.0` (BKG, ROB), `2.0.37` (ASI) | `NTRIP BKG Caster 2.0.48/2.0` |
| **Registration** | BKG form `register.rtcm-ntrip.org` | BKG, ROB, ASI separate forms | BKG form (same as IGS-IP) |
| **Overlap with EUREF-IP** | A few EPN stations are mirrored on IGS-IP (e.g. REYK, NICO, NABG, NYA2). EUREF-IP is the more comprehensive European source. | | |
| **TLS** | `:443` confirmed | BKG `:443`, ROB `:2102`, ASI none | `:443` confirmed |

See `EUREF-IP.md` for the federated European broadcaster details.

---

## Sources consulted

- BKG NTRIP infrastructure hub: https://igs.bkg.bund.de/ntrip/
- BKG broadcaster about page: https://igs.bkg.bund.de/ntrip/about
- BKG NTRIP caster software description: https://igs.bkg.bund.de/ntrip/bkgcaster
- IGS-IP caster home (HTTP only — TLS cert presents as `igs.bkg.bund.de`): http://igs-ip.net (returned 404 on direct hit; canonical info lives on `igs.bkg.bund.de/ntrip/` and `products.igs-ip.net/home`)
- products.igs-ip.net caster home: https://products.igs-ip.net/home
- BKG user registration (single form): http://register.rtcm-ntrip.org/cgi-bin/registration.cgi
- IGS Real-Time Service overview: https://igs.org/rts/
- IGS RTS user access: https://igs.org/rts/user-access/
- IGS Real-Time Working Group: https://igs.org/wg/real-time/
- IGS network tracker (534 stations live count): https://network.igs.org/
- IGS20 reference frame announcement (2022): https://igs.org/news/igs20/
- EPNCB broadcaster overview (mentions IGS-IP as sister caster): https://epncb.oma.be/_networkdata/data_access/real_time/broadcasters.php

### Live probes (2026-05-21)

- `curl --http0.9 http://www.igs-ip.net:2101/` → `SOURCETABLE 200 OK`, server `NTRIP ntrips 2.0.69274/1.0`, **386 STR rows**, 2 CAS, 4 NET (EUREF/IGS/MGEX/MISC). Content-Length 86621.
- `curl --http0.9 -k https://www.igs-ip.net:443/` → identical 386-row payload; HTTPS confirmed live.
- `curl --http0.9 http://products.igs-ip.net:2101/` → `SOURCETABLE 200 OK`, server `NTRIP BKG Caster 2.0.48/2.0`, **91 STR rows** (11 obs + 80 SSR), 2 CAS, 2 NET (IGS/MISC).
- `curl --http0.9 -k https://products.igs-ip.net:443/` → identical 91-row payload; HTTPS confirmed live.
- `curl --http0.9 http://mgex.igs-ip.net:2101/` → no response (TCP connect succeeded but empty body); HTTPS `:443` also empty. The `mgex.igs-ip.net/home` info page is offline (ECONNREFUSED) as of 2026-05-21 — MGEX streams now live on the main `www.igs-ip.net:2101` caster (4 STR rows tagged NET=MGEX).
