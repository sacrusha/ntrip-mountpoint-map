# Mongolia [MN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-17 — pipeline-confirmed alive)

## Status: YES — MonPOS national caster live in pipeline (source id `almgg_mn`); shared public credentials `rover` / `262461`; ETA: cm @ ≤35 km

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — MonPOS (Mongolian Positioning System); pipeline-confirmed `last_ok` 2026-05-15 (data/stations.json source `almgg_mn`) |
| **Operator** | General Office of Land Relations, Geodesy and Cartography (gazar.gov.mn). Formerly ALACGaC / ALMGG. |
| **landing_url** | https://monpos.gazar.gov.mn/ |
| **access_url** | https://monpos.gazar.gov.mn/monpos/3/ — public announcement page that posts the shared rover credentials |
| **host:port** | `rtk.gazar.gov.mn:2101` (primary; curl-confirmed 2026-04-30 by upstream research). Alternate IP `66.181.168.80:2101`. Caster: SubCarrier Systems SNIP R3.14.00. |
| **Mountpoint** | `MGL_network` — physical-coord VRS-style; RTCM 3.x; 2 cm + 1 ppm within ~35 km of nearest station. Plus individual single-base mounts (40+ MNG-tagged stations now in `stations.json`). |
| **Published credentials** | Username `rover` / password `262461` (posted on the government announcement page `monpos.gazar.gov.mn/monpos/3/`, not just community lore). Individual accounts also issued via geodesy.gov.mn portal. |
| **tariff** | Free at protocol via shared rover account; no published fee. Licensed-survey accounts likely require gazar.gov.mn registration. |
| **num_stations** | 40+ physical CORS (Trimble NetR8/NetR9; choke-ring + Zephyr Geodetic antennas). Coverage dense Ulaanbaatar–Darkhan–Erdenet corridor, sparse elsewhere — country ~1.56 M km², mean spacing ~200 km, so RTK practical only in north-central corridor and selected aimag centres. |
| **vrs** | Yes (`MGL_network`) |
| **hobbyist_eligibility** | Yes — shared rover credentials work for any user; no licence check observed. |
| **legal_residency_required** | Not stated. |
| **last_confirmed_alive** | 2026-05-15 (data/stations.json `almgg_mn.last_ok`); MonPOS portal pages live; web portal still serves outdated TLS cert (re-verified 2026-05-17). |
| **datum_epoch** | omitted — no operator-declaration of datum/epoch citable. Gazar.gov.mn pages describe accuracy class but stop short of naming an ITRF/IGS frame for the caster output. |

## Recent activity
- **2026-05-15** — caster `almgg_mn` healthy in data/stations.json (`status: ok`, `last_ok: 2026-05-15`).
- **2026-04-30** — sourcetable curl-confirmed; `pipeline-flags: solution_filter=False` applied (6 physical stations were caster-tagged solution=1 erroneously).
- **2021-onwards** — network grew from 6 stations (delivered 2010 by ILS under US Millennium Challenge Corp / Property Rights Project, Trimble NetR8) to 40+; cadastral GCPs across ~75 k plots in early phase.

## Context
- Pipeline already surfaces MonPOS as `almgg_mn` (color #9e6b00, type `physical-vrs`). Country tag `MN`; stations carry tag `MNG` in sourcetable.
- Web portal `monpos.gazar.gov.mn` and CORS page `cors.gazar.gov.mn/all/` use outdated/self-signed TLS — sandbox WebFetch returns cert error; rovers using a stock NTRIP client over plain HTTP/2101 are unaffected.
- Practical: Within ~35 km of Ulaanbaatar / Darkhan / Erdenet → VRS works; rural / Gobi → falls back to nearest single-base, often >100 km → useless for cm-level fix.
- No rtk2go / Centipede / EarthScope volunteer base within useful range (zero MN stations in those sources as of 2026-05-17).

## Post-processing (RINEX) fallback
| Service | URL | Cost |
|---|---|---|
| gazar.gov.mn — daily RINEX (30 s) from CORS | https://en.gazar.gov.mn/p/613-110 | likely free; registration probable |
| IGS — ULAB (Ulaanbaatar; GFZ/IAG-MAS, 1997-) | https://network.igs.org/ ; https://www.earthscope.org/data/gnss-data/ | free |

## Sources consulted
- gazar.gov.mn — https://en.gazar.gov.mn/ ; MONPOS online processing https://en.gazar.gov.mn/system/10
- monpos.gazar.gov.mn portal + announcement page `/monpos/3/` (shared credentials confirmed, accessed 2026-05-17)
- cors.gazar.gov.mn/all/ — CORS status map (TLS issue from sandbox)
- ardusimple Mongolia page (Mongolia not listed in 2026 ardusimple country catalogue per cache + WebFetch)
- mycoordinates.org — "GNSS-CORS geodetic network development in Mongolia" (2019)
- MundoGEO — "ILS Delivers CORS Infrastructure in Mongolia" (2011-01-03)
- data/stations.json source `almgg_mn` — status ok, last_ok 2026-05-15
- docs/rtk_inventory.md `almgg_mn` block (canonical record, includes pipeline-flags)
