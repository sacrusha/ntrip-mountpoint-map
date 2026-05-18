# Guinea [GN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-12 entry; WebSearch 2026-05-17 surfaced no new INC CORS/NTRIP initiative)

## Status: NO national NTRIP caster — single rtk2go volunteer base "Gine-Albrk" present near Conakry

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (no national / institutional caster) |
| **Volunteer fallback (rtk2go)** | 1 GIN-coded base — "Gine-Albrk" at ~9.52, -13.72 (Conakry area); free, anonymous via `rtk2go.com:2101`, hobbyist-grade (local `data/stations.json` 2026-05-12). Sub-decimetre RTK only within ~20–30 km of base. |
| **host:port** | `rtk2go.com:2101` (volunteer caster, not a national service) |
| **tariff** | Free (rtk2go is a community service; donations accepted) |
| **hobbyist_eligibility** | Yes (rtk2go is explicitly hobbyist) |
| **legal_residency_required** | No |
| **last_confirmed_alive** | Gine-Albrk mountpoint listed in local `data/stations.json` rtk2go sourcetable, refreshed 2026-05-12 by project's `update-stations` workflow |

## Most Recent Project Announcement

None found. No CORS programme, NTRIP deployment timeline, or geodetic modernisation announcement for Guinea has been identified in public sources as of 2026-05-06.

**AFREF Workshop 2024** (RCMRD, Nairobi, August 2024): Guinea not listed among the ~22 African countries confirmed to have at least one operational CORS installation.
URL: https://ric2024.rcmrd.org/afref

## Context Notes

- **Political context**: A military coup on 5 September 2021 ousted President Alpha Condé; Colonel Mamadi Doumbouya leads the transitional government (CNRD). ECOWAS suspended Guinea following the coup; diplomatic and technical cooperation with France (IGN FI, AFD) and other bilateral partners has been curtailed since 2021. No US/EU OFAC sanctions target the Guinean state itself. The political situation has not been reported to have directly decommissioned existing geodetic infrastructure, but the pipeline for new GNSS modernisation projects — which typically require bilateral technical cooperation — has been substantially narrowed.
- **INC** (Institut National Cartographique, under the Ministry of Town Planning) is the national geodesy and mapping authority. INC has not published a CORS network, caster host:port, or real-time NTRIP service in any identified public source.
- **AFREF contributions**: Guinea's contributions to AFREF, if any, are raw-archive RINEX at most — no streaming station has been confirmed.
- **Bilateral cooperation freeze**: IGN FI and AFD (Agence Française de Développement), the two main partners historically involved in Francophone West African geodetic modernisation, have reduced or suspended technical cooperation with Guinea since the 2021 coup. This significantly reduces the near-term probability of a CORS or NTRIP rollout.
- **No CORS confirmed**: Guinea does not appear in the IGS network, ITRF2020, SONEL, AFREF confirmed-CORS country list, or any institutional NTRIP listing as of 2026-05-12.
- **RTK2go**: 1 volunteer base "Gine-Albrk" at ~9.52, -13.72 (Conakry/Kaloum area) present in local `data/stations.json` 2026-05-12. Single base, hobbyist-operated — only useful within ~20–30 km of that single station; no monitoring or SLA, may drop without notice.
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
- Local `data/stations.json` 2026-05-12 — rtk2go: 1 GIN-coded mountpoint "Gine-Albrk" (~9.52, -13.72); Centipede / EarthScope: 0
- GitHub mvarga1989 CORS list — no GN entry
- ntrip-list.com/africa/ — no GN entry
- WebSearch 2026-05-12 ("Guinea Conakry INC CORS NTRIP GNSS reference station 2025 2026") — no Guinea-specific geodetic CORS initiative surfaced
