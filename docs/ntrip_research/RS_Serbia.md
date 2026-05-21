# Serbia [RS] — NTRIP RTK Research

**researched:** 2026-05-21 (prior: 2026-05-17, 2026-05-12)
**status:** YES — paid government NTRIP (AGROS, RGZ); affordable annual rate (~€74/yr). Strong volunteer supplement: 26 rtk2go + 14 Centipede single-base streams, mostly clustered in Vojvodina.

## AGROS — Active Geodetic Reference Frame of Serbia

| field | value |
|---|---|
| landing_url | https://www.rgz.gov.rs/agros |
| access_url | https://www.rgz.gov.rs/agros (Serbian-language; subscription via RGZ; English mini-portal `agros.rgz.gov.rs/navigation.php?Lang=ENG` ECONNREFUSED 2026-05-12) |
| operator | Republički geodetski zavod (RGZ) — Republic Geodetic Authority of Serbia; Bulevar vojvode Mišića 39, Beograd; `info.centar@rgz.gov.rs` |
| host:port | `agros.rgz.gov.rs:2101` (IP 93.87.56.181) — DNS resolves but TCP connection timed out from sandbox 2026-05-21 (egress firewall suspected; documented in rtk_inventory.md as the canonical endpoint). |
| vrs | yes — Trimble VRS Now (network RTK / VRS) |
| num_stations | ~30 physical CORS; denser in Vojvodina, sparser in southern Serbia |
| tariff — RTK flat-rate | 1,125 RSD/month or 8,688 RSD/year (~€10/mo, ~€74/yr at 117 RSD/EUR) per RGZ Uredba o izmenama i dopunama Uredbe o visini naknade (2010-03-11, Sl. glasnik RS 45/02 base + amendments), source: https://otvorenavlada.rs/uredba-republicki-geodetski-zavod0230-lat-doc/ (observed 2026-05-21). |
| tariff — DGPS flat-rate | 703 RSD/mo · 5,379 RSD/yr — out of scope (DGNSS, carrier 0). Listed for completeness only. |
| hobbyist_eligibility | yes — registration open via rgz.gov.rs; no professional-licence wall stated; annual rate well below project cutoff |
| legal_residency_required | ? — registration portal Serbian-language only; payment methods not fully documented in English |
| last_confirmed_alive | service assumed operational — TCP 93.87.56.181:2101 timed out from sandbox after 15 s (suspected egress firewall geo-block; no sourcetable reachable). RGZ AGROS portal `www.rgz.gov.rs/agros` returns redirect loop on WebFetch (2026-05-21). No shutdown announcement found. Sandbox-reachable confirmation of a sourcetable or login portal could not be obtained this pass. |
| datum_epoch | omitted — no citable declaration on rgz.gov.rs / agros.rgz.gov.rs. SREF98 / ETRS89 is the national frame (geodetic literature) but no operator-portal URL declares broadcast epoch. |

## Context

- **AGROS** established 2002-2005; economic use since December 2005. Trimble Pivot Platform backbone with VRS Now.
- **Pricing**: RGZ Uredba (regulation) in RSD; ~€74/yr is well within project hobbyist cutoff. AGROS is affordable as a national service even before considering the volunteer mesh.
- **Volunteer footprint** (verified against `data/centipede.sourcetable` + `data/rtk2go.sourcetable` 2026-05-21):
  - **rtk2go** (`SRB` country code): 26 base stations including `BOBASL`, `BPACA`, `DJUKA`, `DJURIC55`, `DUCA14`, `Drim`, `FARMASAK`, `FFHV`, `ISKRAML`, `JANKO93`, `JOVAID`, `KARMXT`, `LUKASU`, `MAJKIC`, `MARKMB`, `MIKIDOL`, `MRJNSI`, `OBRVESA`, `PEJIC`, `PERO`, `ROBIBNS` (Calma/Stara Pazova despite "Thorsby, Alberta" label), `SILODANIK`, `SOKACBB`, `ZIKARU`, `livibns`, `prahovo`, `viktor`. All RTCM 3.2-3.3 with GPS+GLO+GAL+BDS, lat 44.3-45.5 N (Vojvodina + central Serbia cluster).
  - **Centipede** uses both non-ISO `SER` (12) and ISO `SRB` (2: `KDCS`, `LEMI`) in parallel — **14 total Serbian Centipede bases**. Stations: `ADAM`, `BRTK`, `DADO`, `DANE`, `DETK`, `KAMA`, `KDCS`, `LEMI`, `MIRO`, `OSZA` (new since prior pass), `RTKM`, `SURD`, `TOMA`, `VRTK`. Unicore UM982 and Ublox ZED-F9P units.
  - Plus 1 Centipede station with country code `SVN` but coordinates 45.563 N 20.704 E (Vojvodina): `SIPOS` — operator-tagged SVN, geographically within Serbia. This station is counted under the SI entry per its operator tag and is **not** included in the ~40 volunteer Serbia total.
- **Total volunteer Serbia** ~40 stations (26 rtk2go SRB + 14 Centipede SER/SRB; SIPOS excluded as operator-tagged SVN), dominantly Vojvodina, with thinner coverage in central/southern Serbia. With AGROS at €74/yr the paid option still offers VRS coverage where volunteer single-base baselines exceed ~30 km.

## Post-processing fallback

RINEX data is available from AGROS reference stations via the RGZ portal at `agros.rgz.gov.rs`; exact pricing not confirmed in English-language documentation. EUREF EPN Serbian stations are free at https://epncb.oma.be/ .

## Sources

- RGZ AGROS page: https://www.rgz.gov.rs/agros (HTTP redirect loop on WebFetch 2026-05-21; page exists)
- AGROS English portal: http://agros.rgz.gov.rs/navigation.php?Lang=ENG (ECONNREFUSED 2026-05-06 + 2026-05-12; sub-portal not responding)
- AGROS NTRIP probe: `curl --http0.9 http://93.87.56.181:2101/` — TCP timeout after 15 s 2026-05-21 (sandbox egress)
- ArduSimple Serbia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-serbia/
- Pricing source: RGZ Uredba amendment (2010-03-11, Sl. glasnik RS 45/02 series): https://otvorenavlada.rs/uredba-republicki-geodetski-zavod0230-lat-doc/ (WebFetch 2026-05-21)
- Local: `data/centipede.sourcetable` 2026-05-21 (14 SER+SRB rows); `data/rtk2go.sourcetable` 2026-05-21 (26 SRB rows); `py scripts/stations_by_country.py SRB` → centipede 14 + rtk2go 26 = 40
