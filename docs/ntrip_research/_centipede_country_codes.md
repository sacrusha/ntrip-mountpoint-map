# Centipede-RTK country-code legend (sourcetable field 9)

**Date compiled:** 2026-05-13 (initial); refreshed 2026-05-21 (live re-probe of `crtk.net:2101`).
**Sources:** live `crtk.net:2101` (Centipede-RTK Millipede caster) sourcetables 2026-05-13 and 2026-05-21; cross-checked against `data/stations.json` Centipede facet via `py scripts/stations_by_country.py`; coordinate spot-checks per code.

## Why this file exists

Centipede's sourcetable populates field 9 ("country") with codes that **do not consistently follow ISO 3166-1 alpha-3**. Several codes look like ISO codes but mean something else (`CHZ` is Switzerland, *not* Czech Republic; `ENG` covers all of the UK including Scotland/Wales/Northern Ireland — *not* just England). Other codes are valid alpha-3 but Centipede also uses alternative non-ISO codes for the same country in parallel (`DAN` *and* `DNK` for Denmark; `ROM` *and* `ROU` for Romania; `SER` *and* `SRB` for Serbia). This has caused multiple distillation errors when per-country research files reported Centipede counts.

This file is the authoritative table for resolving any Centipede country attribution. Per-country research files in `docs/ntrip_research/` should reference this file (`see _centipede_country_codes.md`) when discussing Centipede counts.

## Legend (full Centipede country-code → real-territory map, refreshed 2026-05-21)

Live Centipede codes observed in sourcetable on 2026-05-21 (1213 STR rows total):
`ALA, AUS, AUT, BEL, BEN, BGD, BGR, CAN, CHZ, CIV, CZE, DAN, DEU, DNK, ENG, ESP, FIN, FRA, GRC, HUN, IRL, ISR, ITA, LTU, LVA, MDG, MTQ, NCL, NLD, NOR, PYF, REU, ROM, ROU, SEN, SER, SJM, SRB, SVK, SVN, SWE, USA, ZAF`.

Difference vs 2026-05-13 probe:
- **Added**: `BEN` (Benin, 1 node at 9.69°N/1.66°E), `CIV` (Côte d'Ivoire, 1 node at 6.87°N/-5.24°E).
- **Removed**: `SAU` (Saudi Arabia) — no longer in sourcetable.
- Per-code count shifts: FRA 709 → 715, HUN 217 → 218, FIN 18 → 19, ENG 44 → 42, ROM dropped from 7 to 7 (unchanged), and minor ±1 across other codes. The legend below uses 2026-05-21 counts.

| Code | Real territory | ISO 3166-1 alpha-3? | 2026-05-21 nodes | Notes |
|---|---|---|---|---|
| ALA | Åland Islands (Finland) | yes (ISO) | 2 | Mariehamn area. ISO 3166-1 alpha-3 for Åland is genuinely `ALA`. |
| AUS | Australia | yes (ISO) | 2 | Standard. |
| AUT | Austria | yes (ISO) | 1 | Standard. |
| BEL | Belgium | yes (ISO) | 17 | Standard. |
| **BEN** | **Benin** | yes (ISO) | 1 | New 2026-05-21. Node `BJDJ` at 9.69°N/1.66°E = Djougou, northwestern Benin (largest city of the Donga department; ~70 km east of the Togo border, well inside Benin). |
| BGD | Bangladesh | yes (ISO) | 2 | Standard. |
| BGR | Bulgaria | yes (ISO) | 2 | Standard. |
| CAN | Canada | yes (ISO) | 21 | Standard. Quebec/Ontario/east. |
| **CHZ** | **Switzerland** | **no — non-ISO** | 31 | **Most-confused code.** ISO `CHE` = Switzerland; ISO `CZE` = Czech Republic. Centipede chose `CHZ` for Switzerland; does *not* mean Czech. Czech stations carry `CZE` separately. |
| **CIV** | **Côte d'Ivoire** | yes (ISO) | 1 | New 2026-05-21. Node `INP02` at 6.87°N/-5.24°E in central Côte d'Ivoire. |
| CZE | Czech Republic | yes (ISO) | 3 | Standard. Distinct from `CHZ`. |
| **DAN** | **Denmark** | **no — non-ISO** | 11 | Centipede uses **both** `DAN` (mostly `AG*` agricultural cluster in Jutland) and `DNK` (also Jutland) — appears to be the same network with a label inconsistency. Total Denmark Centipede footprint ~19 nodes (DAN ∪ DNK). |
| DEU | Germany | yes (ISO) | 3 | Standard. |
| DNK | Denmark | yes (ISO) | 8 | See `DAN` above — used in parallel. |
| **ENG** | **United Kingdom (all of GB + Northern Ireland)** | **no — non-ISO** | 42 | ISO `GBR` = UK. Centipede uses `ENG` even for stations clearly outside England: Scotland (BALL 57.5°N, BRACO, CRAG, DRUM, FRAS, HRVA, LARL, MLLC, TYRI, WOCF, CHAP, FHL1), Northern Ireland (DJAM, DYFM, GWMD, OATS), Wales (PEMBS). 42 `ENG` nodes cover the whole UK, not just England. **Per-country files should treat `ENG` as "UK" for Centipede counts**, not as "England only", and *especially not* attempt to split Centipede ENG counts across separate UK constituent countries. |
| ESP | Spain | yes (ISO) | 1 | Standard. |
| FIN | Finland | yes (ISO) | 19 | Standard. (Åland uses `ALA` separately.) |
| FRA | France | yes (ISO) | 715 | Standard. Largest single-country footprint. |
| GRC | Greece | yes (ISO) | 2 | Standard. |
| HUN | Hungary | yes (ISO) | 218 | Standard. Second-largest. |
| IRL | Ireland | yes (ISO) | 6 | Standard. East coast. |
| ISR | Israel | yes (ISO) | 1 | Standard. |
| ITA | Italy | yes (ISO) | 3 | Standard. |
| LTU | Lithuania | yes (ISO) | 1 | Standard. |
| LVA | Latvia | yes (ISO) | 1 | Standard. |
| MDG | Madagascar | yes (ISO) | 2 | Standard. |
| MTQ | Martinique | yes (ISO) | 1 | Standard. |
| NCL | New Caledonia | yes (ISO) | 2 | Standard. |
| NLD | Netherlands | yes (ISO) | 26 | Standard. |
| NOR | Norway | yes (ISO) | 23 | Standard. (Svalbard uses `SJM`.) |
| PYF | French Polynesia | yes (ISO) | 2 | Standard. |
| REU | Réunion | yes (ISO) | 4 | Standard. |
| **ROM** | **Romania** | **no — non-ISO** | 7 | ISO `ROU` = Romania. Centipede uses **both** `ROM` (7 nodes) and `ROU` (2 nodes) in parallel. Anyone counting "Centipede Romania" must sum both codes — total 9 nodes 2026-05-21. |
| ROU | Romania | yes (ISO) | 2 | See `ROM` above — used in parallel. |
| SEN | Senegal | yes (ISO) | 2 | Standard. |
| **SER** | **Serbia** | **no — non-ISO** | 12 | ISO `SRB` = Serbia. Centipede uses **both** `SER` (12 nodes, Vojvodina) and `SRB` (3 nodes also in Serbia) in parallel. Anyone counting "Centipede Serbia" must sum both — total ~15 nodes 2026-05-21. |
| SJM | Svalbard and Jan Mayen | yes (ISO) | 1 | NYAWIPEV at Ny-Ålesund. |
| SRB | Serbia | yes (ISO) | 3 | See `SER` above — used in parallel. |
| SVK | Slovakia | yes (ISO) | 2 | Standard. |
| SVN | Slovenia | yes (ISO) | 4 | Standard. |
| SWE | Sweden | yes (ISO) | 1 | Standard. |
| USA | United States | yes (ISO) | 4 | Standard. |
| ZAF | South Africa | yes (ISO) | 1 | Standard. |

### Code that left the sourcetable

- **`SAU`** — Saudi Arabia. Present 2026-05-13, absent 2026-05-21. `SA_SaudiArabia.md` exists and already records the dropout ("0 SA nodes in local archive 2026-05-17 (KHAY dropped since 2026-05-12)") — no further correction needed there. No other per-country file depends on a Centipede SAU count.

## Summary of non-standard codes (the "watch list")

| Centipede code | Real meaning | Confusion risk |
|---|---|---|
| `CHZ` | Switzerland | **HIGH** — looks like CZ (Czech) but is CH (Switzerland). Czech stations are under `CZE`. |
| `ENG` | All of UK (England + Scotland + Wales + Northern Ireland) | **HIGH** — looks like just England, but covers the whole UK. Distillation must not split ENG across constituent countries. |
| `DAN` | Denmark (parallel to `DNK`) | **MEDIUM** — counting Denmark requires summing DAN + DNK. |
| `ROM` | Romania (parallel to `ROU`) | **MEDIUM** — counting Romania requires summing ROM + ROU. |
| `SER` | Serbia (parallel to `SRB`) | **MEDIUM** — counting Serbia requires summing SER + SRB. |

## Codes the docstring of `scripts/stations_by_country.py` mentions but were NOT observed in 2026-05-21 sourcetable

The docstring on `scripts/stations_by_country.py` reads: *"Centipede quirks: CHZ=CZ ENG=GB SER=RS BIH=BA NLD/BEL separate."*

- **`BIH`** — claimed in docstring as "BIH=BA" (Bosnia). **Not observed in the Centipede sourcetable** on either 2026-05-13 or 2026-05-21. Other local NTRIP sources do use `BIH`: `rtk2go` carries 1 node (AGROORSOLIC), and `euref_ip` carries SRJV00BIH0 (Sarajevo EPN station, NET=EUREF, country=BIH). The docstring's `BIH=BA` aside therefore refers to a code Centipede has shed (or never used); the code remains valid ISO-3 for Bosnia-Herzegovina in other casters. No per-country file currently relies on a Centipede `BIH` code, so no correction needed.

## Implications for per-country research files

Files that quote a Centipede count must use the right code(s). Files known to reference Centipede counts (audited 2026-05-13, re-checked 2026-05-21):

| File | Centipede code(s) used | Verdict |
|---|---|---|
| `CH_Switzerland.md` | `CHZ` (31 nodes 2026-05-21) | OK (post-revision 2026-05-13). Explicitly notes CHZ ≠ Czech. |
| `CZ_CzechRepublic.md` | `CZE` (3 nodes) | OK. Does not confuse with CHZ. |
| `GB_Great-Britain.md` | `ENG` (42 nodes 2026-05-21) | needs clarification — file should make clear that `ENG` covers all of UK (incl. Scotland/Wales/NI), not just England. The count (42 today) is the correct UK-wide footprint. |
| `IE_Ireland.md` | `IRL` (6 nodes 2026-05-21) | OK. |
| `DK_Denmark.md` | `DNK` (8 nodes) | undercount — does not include the parallel `DAN` code (11 more nodes). True Centipede Denmark footprint is ~19 nodes (DAN ∪ DNK), not 8. |
| `RO_Romania.md` | `ROM` (7 nodes) | undercount — does not include the parallel `ROU` code (2 nodes 2026-05-21). True Centipede Romania total is 9 nodes (ROM ∪ ROU). |
| `RS_Serbia.md` | `SER` (12) + `SRB` (3) | OK — already sums both codes. |
| `AX_AlandIslands.md` | `ALA` (2 nodes) | OK. |
| `SJ_Svalbard.md` | `SJM` (1 node, NYAWIPEV) | OK. |
| `FI_Finland.md` | `FIN` (19 nodes 2026-05-21) | OK. (Note that Åland is separately under `ALA` — Finland mainland count is unaffected.) |
| `NO_Norway.md` | `NOR` (23 nodes 2026-05-21) | OK. (Svalbard separately under `SJM`.) |
| `FR_France.md` | `FRA` (715 nodes 2026-05-21) and notes top counts including `CHZ (Switzerland — *not* Czech)` | OK on CHZ. Could optionally note the ENG/DAN/ROM/SER quirks as well, but FR file does not depend on those. |
| `BJ_Benin.md` | (new code `BEN`, 1 node 2026-05-21) | needs check — BJ file may not have known about Centipede's `BEN` code yet. ISO `BEN` is genuinely Benin so the code is standard. |
| `CI_CoteDIvoire.md` (if exists) | (new code `CIV`, 1 node 2026-05-21) | needs check — file may not have known about Centipede's `CIV` code yet. ISO `CIV` is genuinely Côte d'Ivoire so the code is standard. |

**Action items from this audit:**
1. `GB_Great-Britain.md` — clarify in the Volunteer fallback row that `ENG` covers the whole UK, not just England, and that the 42 nodes include Scotland/Wales/NI base stations.
2. `DK_Denmark.md` — re-count Denmark Centipede footprint as `DAN ∪ DNK` (~19 nodes total), not just the 8 `DNK` nodes.
3. `RO_Romania.md` — Centipede Romania is `ROM ∪ ROU` = 9 nodes today; previous 7-node figure undercounted by 2.
4. `BJ_Benin.md` and any `CI_*` file — add note that a Centipede node now exists in their country (1 node each as of 2026-05-21).
5. If a Saudi Arabia file references `SAU` Centipede nodes — note that Centipede no longer carries them as of 2026-05-21.

## Reproducibility

To re-derive this legend on any future date:

```
# 1. List all distinct Centipede country codes from the live sourcetable:
curl -s http://crtk.net:2101/ | awk -F';' '/^STR;/ {print $9}' | sort -u

# 2. Per-code count:
curl -s http://crtk.net:2101/ | awk -F';' '/^STR;/ {print $9}' | sort | uniq -c | sort -rn

# 3. For each suspect code, dump stations to verify by coordinate:
py scripts/stations_by_country.py <CODE>
# (if a code only appears in Centipede and the lat/lon clearly fall in country X but the alpha-3 doesn't match, it's a non-ISO Centipede convention)
```

If a future Centipede sourcetable introduces new non-ISO codes (e.g. a `SCO` for Scotland would split out from ENG; a `WLS` for Wales; a `GBR` replacing `ENG`), update this file and re-audit per-country counts.
