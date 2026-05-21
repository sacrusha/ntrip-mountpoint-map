# rtk2go — NTRIP RTK Research (cross-country community caster, not a country)

> **Scope note.** This is not a country entry. rtk2go is a single open
> community NTRIP caster (`rtk2go.com:2101`) carrying ~880 volunteer base
> stations from "nearly every country" (operator claim). Per-country files
> often cite small rtk2go footprints as fallback when no national free
> network exists; this file consolidates caster-wide facts (operator,
> ports, credentials, terms, ban policy, frame caveats) so country files
> can point to a single source.

## Status: ACTIVE — single global caster, free, no rover registration, 888 STR rows live 2026-05-19; volunteer single-base RTK; operated by SubCarrier Systems Corp. (SCSC) since the early SNIP era.

| Field | Value |
|---|---|
| **Network name** | rtk2go (registered trademark; the public-facing instance of SCSC's SNIP NTRIP caster software) |
| **Caster software** | SNIP Pro (commercial NTRIP caster, sold separately by SCSC) — same code that operators run on their own servers, run by SCSC themselves on AWS for the community caster. |
| **landing_url** | http://rtk2go.com/ — operator-owned. HTTP only; no HTTPS variant of the marketing site. |
| **access_url** | http://rtk2go.com/how-to-connect/ (rover connection guide). For base-station operators: http://rtk2go.com/sample-page/new-reservation/ (reservation form), and email `support@use-snip.com` to confirm mountpoint name and password. |
| **host:port (plain)** | `rtk2go.com:2101` |
| **host:port (TLS)** | `rtk2go.com:2102` — secure SNIP caster on TLS; requires SNIP "Rev2"-aware client. Source: http://rtk2go.com/on-secure-caster-connections/. |
| **host:port (regional filter — Poland)** | `rtk2go.com:2103` — filtered view of POL-coded mountpoints; *same physical caster*, distinct sourcetable. Source: http://rtk2go.com/regionalcastertables/. |
| **host:port (regional filter — Japan)** | `rtk2go.com:2104` — filtered view of JPN-coded mountpoints; same caster. |
| **Tariff** | **Free.** "*There is no cost for this service.*" — `use-snip.com` KB. Voluntary donations accepted at http://rtk2go.com/donations-and-support/ to offset SCSC's hosting costs (AWS Windows VM). No subscription tier; no paid tier. Date observed: 2026-05-21 (via search mirror; HTTP site directly behind ECONNREFUSED to this fetcher). |
| **Rover credentials** | Username: *any email address* (used only as identifier in caster logs); Password: `none`. No registration required to consume streams. Source: SNIP KB "Question: What is RTK2go". |
| **Base operator credentials** | Email `support@use-snip.com` with desired mountpoint name, parsing preference, public/private visibility, city name, password, and optional fixed-IP restriction. Processed "typically within one day", no charge. Source: https://www.use-snip.com/kb/knowledge-base/sending-data-rtk2go-reservations/. |
| **hobbyist_eligibility** | Yes — explicitly the target audience ("*support users that do not have access to a static IP of their own, or who do not care to operate their own NTRIP Caster*"). Commercial use also permitted under same terms. |
| **legal_residency_required** | No — operator claims "*250,000+ users from nearly every country*". No geographic restriction in terms. SCSC is US-based (Glendora, California) but does not restrict by user residency or export status. |
| **Simultaneous connections** | ? — operator publishes no explicit per-rover concurrent-connection cap; abusive patterns (rapid bad-credential connects, idle TCP holds) trigger automated IP bans (`how-to-get-your-ip-banned/`). |
| **last_confirmed_alive** | 2026-05-19 — pipeline `source_health.json` records `last_ok` for `rtk2go` at 2026-05-19T08:33:27Z. Local fetch `data/rtk2go.sourcetable` carries 888 STR rows + 1 NET record (`NET;SNIP;RTK2go;N;N;rtk2go.com;rtk2go.com:2101;support@use-snip.com;;`). Operator homepage advertises "800+ free base stations online at any time" plus "11,000+ Registered Base Stations" total. |
| **num_stations** | ~888 active at any moment (sourcetable 2026-05-19); ~11,000 ever-registered cumulative. Operator notes "*only approximately 10% of them active at any given time*", consistent with the 888/11,000 ratio. |
| **vrs** | No — predominantly single-base RTK. Caster carries an unspecified number of routing-alias mountpoints named `NEAR-xxx` / `NEAR_xxx` (e.g. `NEAR-AUT`, `NEAR-AUS`, `NEAR_DEU`, `NEAR-JPNn`); these are tagged `solution=1` and dropped by the project's default `solution_filter=True` — absent from the cached sourcetable. Count not published by SNIP. No MAC / FKP / iMAX product offered. |
| **datum_epoch** | **Not declared.** rtk2go does no per-base PPP/vetting; many bases run TMODE3 survey-in mode (autonomous fix, ~1–3 m absolute coords frozen at survey-in instant, drifting at plate speed); some operators do voluntary PPP. The sourcetable carries no frame field, and the operator makes no frame statement. Treat individual bases case-by-case (primer `[rtk2go]`). |

---

## Operator and infrastructure

| | |
|---|---|
| **Operator** | SubCarrier Systems Corp. (SCSC) — US Inc., DBA "SNIP" |
| **Location** | 1833 E Foothill Blvd, Glendora, California 91741, USA |
| **Jurisdiction** | United States (California) |
| **Founding focus** | RTCM SC-104 / ION standards body members; high-accuracy automotive DGPS, DSRC ITS. |
| **Hosting** | AWS 2-core Windows VM (per SNIP KB) running SNIP Pro edition. |
| **Trademarks** | SNIP® and RTK2go® are registered trademarks of SCSC. |
| **Software model** | SNIP is paid software (Pro tier sold via use-snip.com/pricing); rtk2go is the free public instance SCSC runs themselves. |

---

## Sourcetable details

Live `rtk2go.com:2101` sourcetable header (verbatim from `data/rtk2go.sourcetable` 2026-05-19):

```
STR;aamakinen;Evijarvi;RTCM 3.2;1005(1), 1077(1), 1084(1), 1097(1), 1127(1), 1230(1);;;SNIP;FIN;63.36;23.36;1;0;SNIP;none;B;N;6840;
...
NET;SNIP;RTK2go;N;N;rtk2go.com;rtk2go.com:2101;support@use-snip.com;;
```

STR row count: **888** (single SNIP network). Operator-claimed live count "800+" matches. Cumulative registered: 11,000+.

### Sourcetable misconfiguration quirks (relevant to pipeline filtering)

- **NMEA=1 on physical bases.** The SNIP caster software tags every uploaded mountpoint as NMEA-required even when the base is a fixed-coordinate single-base RTK that does *not* consume rover GGA. The project's `fetch_stations.py` uses `nmea_filter=False` for the rtk2go source to retain all entries (all 888 cached STR rows have `nmea=1`).
- **Carrier field blank.** Format starts with `RTCM 3` (`RTCM 3.2`, `RTCM 3.3`). Parser infers `carrier=2` from format when field is blank.
- **`carrier=0` legacy rows.** Some rows carry `carrier=0` (e.g. `Bacsbokod`, `Drumads_Farms`, `CURRSTHCMR`, `quinbase1`) — typically CMR/CMR+ legacy uploads lacking the carrier-phase tag. Per primer `[sourcetable]` these are dropped as DGNSS (code-only).
- **`NEAR-xxx` / `NEAR_xxx` aliases.** Regional nearest-station VRS-style routes (e.g. `NEAR-AUT`, `NEAR-AUS`, `NEAR_DEU`, `NEAR-JPNn`); the caster marks these `solution=1`. The project keeps `solution_filter=True` (default) which drops them — they would otherwise inflate `num_stations` with duplicate-locked aliases. These are the only VRS-flavored mountpoints on rtk2go; everything else is single-base.

---

## Access model

### Rovers (data consumers)

No registration. Username field accepts any email address (logged by caster for support / ban purposes only), password field literally `none`. Documented in http://rtk2go.com/how-to-connect/ and SNIP KB.

### Base operators (data uploaders)

1. Register at http://rtk2go.com/sample-page/new-reservation/ (or send the equivalent details by email to `support@use-snip.com`):
   - Mountpoint name (correct capitalisation, no offensive or commercial-promotional names)
   - Parsing preference (whether caster should parse the RTCM)
   - Public or private visibility (whether the mountpoint appears in the public sourcetable)
   - City name (free-text)
   - Password (do not share with others)
   - Optional fixed IP (connection restriction)
2. Processed typically within one business day, no charge.
3. By submitting data the operator affirms: "*a) you have the right to do so, b) you consent to allow others to freely use your data, c) the Caster owner/operator shall be held harmless for any faults or loss.*"

Source: https://www.use-snip.com/kb/knowledge-base/sending-data-rtk2go-reservations/.

### Banned activities (will get IP/operator banned)

Per http://rtk2go.com/how-to-get-your-ip-banned/ and SNIP KB:

- Naming a mountpoint with offensive content, or using the mountpoint name as commercial/product promotion (even if GNSS-related).
- Opening TCP/IP sockets and never sending any data (e.g. third-party-software validation tests).
- Subscribing to a *private* upstream service and redistributing that data on rtk2go.
- Rover devices sending large amounts of non-GGA NMEA-0183 data (caster keeps only the GGA fragment relevant to routing).
- Repeated failed connection attempts (hundreds of bad-credential connects) — auto-banned.

**Ban duration:** Typical ~3 hours for automated abuse; "minutes to days" for moderate cases; weeks-to-permanent for repeat or extreme abuse (rare). Live ban list is exposed at `http://new.rtk2go.com:2101/SNIP::BANS`.

---

## Reference frame — operational caveat

rtk2go does **not** vet or correct base coordinates; the caster relays whatever the upstream RTKBase / SimpleRTK / proprietary setup emits in RTCM 1005/1006. Many hobbyist bases run u-blox ZED-F9P in TMODE3 SVIN (autonomous survey-in), producing a fixed coordinate good to ~1–3 m absolute that drifts at plate-tectonic speed (a few cm/yr). Some operators do PPP and recompute base coordinates; the sourcetable carries no marker to distinguish.

**Implication for users:** rtk2go gives you cm-relative accuracy between rover and base (RTK works regardless), but absolute coordinates inherit whatever frame and absolute error the base operator chose. RTCM 1021–1027 datum-transformation messages are not transmitted (F9P does not generate them). Treat as recipe-only, not as a declared network frame — primer `[rtk2go]`.

---

## Pipeline notes (project-internal)

- SOURCES id: `rtk2go`
- Endpoint: `http://rtk2go.com:2101/`
- Flags: `nmea_filter=False`, `solution_filter=True` (default), carrier inference from `RTCM 3*` format.
- Regional filtered views (`:2103` PL, `:2104` JP) are *not* separate SOURCES entries — same caster, same stations.

---

## Cross-references

Country research files commonly cite rtk2go as the volunteer/fallback option when no free national caster exists. See `docs/rtk_inventory.md` for the curated catalogue line. For country-level counts and station IDs, grep `rtk2go` across `docs/ntrip_research/`. Example dependencies:

- `BG_Bulgaria.md`, `BA_BosniaHerzegovina.md`, `GE_Georgia.md`, `AZ_Azerbaijan.md`, `TH_Thailand.md`, `MM_Myanmar.md` etc. — single-base rtk2go fallback noted alongside paid or restricted national caster.
- `BR_Brazil.md`, `AR_Argentina.md` — rtk2go supplements free national networks (RBMC-IP, RAMSAC) in metro areas.
- `DK_Denmark.md`, `SE_Sweden.md`, `NL_Netherlands.md`, `BE_Belgium.md`, `IE_Ireland.md`, `GB_Great-Britain.md` — rtk2go as backup to paid commercial European networks.

---

## Sources Consulted

- rtk2go homepage (statistics, software banner): http://rtk2go.com/ (HTTP only; ECONNREFUSED to WebFetch HTTPS-upgrade; content read via search-engine mirror)
- Cost page: http://rtk2go.com/cost/
- Donations / support: http://rtk2go.com/donations-and-support/
- Rover connection guide: http://rtk2go.com/how-to-connect/
- Base reservation form: http://rtk2go.com/sample-page/new-reservation/
- Reservation procedure & terms-of-submission: https://www.use-snip.com/kb/knowledge-base/sending-data-rtk2go-reservations/
- "What is rtk2go": https://www.use-snip.com/kb/knowledge-base/question-what-is-rtk2go/
- "An open NTRIP caster": https://www.use-snip.com/kb/knowledge-base/an-open-ntrip-caster/
- Secure (TLS) port 2102: http://rtk2go.com/on-secure-caster-connections/
- Regional ports 2103 (PL) / 2104 (JP): http://rtk2go.com/regionalcastertables/
- Abuse / ban policy: http://rtk2go.com/how-to-get-your-ip-banned/
- Live ban list: http://new.rtk2go.com:2101/SNIP::BANS
- SNIP::STATUS live endpoint: http://rtk2go.com:2101/SNIP::STATUS
- About SNIP / SCSC (Glendora, CA; standards involvement): https://www.use-snip.com/about-snip/
- Product / pricing for SNIP software: https://www.use-snip.com/pricing/
- SNIP rtk2go service page: https://www.use-snip.com/rtk2go/
