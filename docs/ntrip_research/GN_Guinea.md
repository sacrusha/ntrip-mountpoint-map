# Guinea [GN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (re-verified; no new IGN-Guinée / ITCG CORS/NTRIP initiative surfaced. `py scripts/stations_by_country.py GIN` → 1 rtk2go station Gine-Albrk; rtk2go caster status `ok` in `data/source_health.json` 2026-05-21.)

## Status: NO national NTRIP caster — single rtk2go volunteer base "Gine-Albrk" near Conakry

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (no national / institutional caster) |
| **Volunteer fallback (rtk2go)** | 1 GIN-coded base — "Gine-Albrk" at 9.52°N -13.72°E (Conakry area). Free, anonymous via `rtk2go.com:2101`. Sub-decimetre RTK only within ~20–30 km. |
| **host:port** | `rtk2go.com:2101` (volunteer caster, not a national service) |
| **num_stations** | 1 (Gine-Albrk single volunteer base) |
| **vrs** | no (single base, no VRS/NRTK) |
| **tariff** | Free (rtk2go is a community service; donations accepted) |
| **hobbyist_eligibility** | Yes (rtk2go is explicitly hobbyist) |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-21 — Gine-Albrk present in local `data/stations.json` rtk2go sourcetable; rtk2go caster status `ok` per `data/source_health.json` (re-fetched 2026-05-21T17:26:57Z) |

## Most Recent Project Announcement

None found. No CORS programme, NTRIP deployment timeline, or geodetic modernisation announcement for Guinea has been identified in public sources as of 2026-05-06.

**AFREF Workshop 2024** (RCMRD, Nairobi, August 2024): Guinea not listed among the ~22 African countries confirmed to have at least one operational CORS installation.
URL: https://ric2024.rcmrd.org/afref

## Context Notes

- **Political context**: A military coup on 5 September 2021 ousted President Alpha Condé; Colonel Mamadi Doumbouya leads the transitional government (CNRD). ECOWAS suspended Guinea following the coup. No US/EU OFAC sanctions target the Guinean state itself. The political situation has not been reported to have directly decommissioned existing geodetic infrastructure; no new bilateral GNSS modernisation programme for Guinea has surfaced in identified sources 2022–2026.
- **National authority**: Institut Géographique National de Guinée (IGN-Guinée) — formerly Institut de Topographie et de Cartographie de Guinée (ITCG), established 1980; mandate covers basic cartography, geodetic / leveling networks, and technical standards. No web presence located via search 2026-05-21 (no `ign.gov.gn` or `itcg.gov.gn` resolvable; a Facebook page "Institut Géographique National - IGN Guinée" exists but publishes no CORS / NTRIP service). No public CORS network, caster host:port, or real-time NTRIP service has been published by IGN-Guinée in any identified source. Decree fixing IGN attributions referenced in guineenews.org (decree-les-attributions-de-linstitut-geographique-national-fixees).
- **AFREF contributions**: Guinea's contributions to AFREF, if any, are raw-archive RINEX at most — no streaming station has been confirmed.
- **Bilateral cooperation status**: AFD's Guinea country page (afd.fr/en/page-region-pays/guinea, fetched 2026-05-21) lists Guinea as an active partner country but does not announce new geodetic-modernisation projects in the post-coup period. No specific IGN FI / AFD CORS programme for Guinea has been announced in identified sources 2022–2026.
- **No CORS confirmed**: Guinea does not appear in the IGS network, ITRF2020, SONEL, AFREF confirmed-CORS country list, or any institutional NTRIP listing as of 2026-05-21.
- **RTK2go**: 1 volunteer base "Gine-Albrk" at 9.52°N -13.72°E (broad Conakry area; exact locality not published on the rtk2go monitor page — name suggests Albreda/Kaloum operator label but rtk2go does not document station siting). Present in local `data/stations.json` 2026-05-21; rtk2go caster status `ok` in `data/source_health.json` (last_ok 2026-05-21T17:26:57Z). Single base, hobbyist-operated — only useful within ~20–30 km; no monitoring or SLA, may drop without notice.
- **Centipede / EarthScope**: Zero GN stations.
- **Global commercial networks** (GEODNET, ONOCOY, RTKdata): No GN coverage identified.
- **Hobbyist access**: The rtk2go "Gine-Albrk" base is currently the only public RTK option in Guinea; deploying a local base station (e.g. Emlid RS2+) remains the recommended fallback outside its coverage radius.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — no confirmed continuously-operated GN station in current archive | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) — GN data availability unconfirmed |

## Sources Consulted
- Country-survey.md stub for GN (existing project notes, date_added 2026-04-29)
- AFREF 2024 Workshop / RCMRD confirmed-CORS country list: https://ric2024.rcmrd.org/afref
- IGS network (network.igs.org) — 0 GN results
- SONEL GNSS database — 0 GN results
- Local `data/stations.json` 2026-05-21 — rtk2go: 1 GIN-coded mountpoint "Gine-Albrk" (9.52, -13.72); Centipede / EarthScope: 0. rtk2go caster `data/source_health.json` status `ok` (last_ok 2026-05-21T17:26:57Z).
- GitHub mvarga1989 CORS list — no GN entry
- ntrip-list.com/africa/ — no GN entry
- WebSearch 2026-05-21 ("Guinea Conakry INC CORS NTRIP GNSS reference station 2025 2026") — no Guinea-specific geodetic CORS initiative surfaced
