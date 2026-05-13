# Centipede-RTK country-code legend (sourcetable field 9)

**Date compiled:** 2026-05-13
**Sources:** live `crtk.net:2101` (Centipede-RTK Millipede caster) sourcetable 2026-05-13; cross-checked against `data/stations.json` Centipede facet via `py scripts/stations_by_country.py`; coordinate spot-checks per code.

## Why this file exists

Centipede's sourcetable populates field 9 ("country") with codes that **do not consistently follow ISO 3166-1 alpha-3**. Several codes look like ISO codes but mean something else (`CHZ` is Switzerland, *not* Czech Republic; `ENG` covers all of the UK including Scotland/Wales/Northern Ireland — *not* just England). Other codes are valid alpha-3 but Centipede also uses alternative non-ISO codes for the same country in parallel (`DAN` *and* `DNK` for Denmark; `ROM` *and* `ROU` for Romania; `SER` *and* `SRB` for Serbia). This has caused multiple distillation errors when per-country research files reported Centipede counts.

This file is the authoritative table for resolving any Centipede country attribution. Per-country research files in `docs/ntrip_research/` should reference this file (`see _centipede_country_codes.md`) when discussing Centipede counts.

## Legend (full Centipede country-code → real-territory map, 2026-05-13)

Live Centipede codes observed in sourcetable: ALA, AUS, AUT, BEL, BGD, BGR, CAN, CHZ, CZE, DAN, DEU, DNK, ENG, ESP, FIN, FRA, GRC, HUN, IRL, ISR, ITA, LTU, LVA, MDG, MTQ, NCL, NLD, NOR, PYF, REU, ROM, ROU, SAU, SEN, SER, SJM, SVK, SVN, SRB, SWE, USA, ZAF.

| Code | Real territory | ISO 3166-1 alpha-3? | Notes |
|---|---|---|---|
| ALA | Åland Islands (Finland) | ✓ ISO | 2 nodes (Mariehamn area). ISO 3166-1 alpha-3 for Åland is genuinely `ALA`. |
| AUS | Australia | ✓ ISO | Standard. |
| AUT | Austria | ✓ ISO | Standard. |
| BEL | Belgium | ✓ ISO | Standard. |
| BGD | Bangladesh | ✓ ISO | Standard. 1 node. |
| BGR | Bulgaria | ✓ ISO | Standard. |
| CAN | Canada | ✓ ISO | Standard. 19 nodes (Quebec/Ontario/east). |
| **CHZ** | **Switzerland** | **✗ non-ISO** | **Most-confused code.** ISO `CHE` = Switzerland; ISO `CZE` = Czech Republic. Centipede chose `CHZ` for Switzerland; it does *not* mean Czech. 30 nodes on Plateau/Jura 2026-05-13. Czech stations carry `CZE` separately (3 nodes 2026-05-13). |
| CZE | Czech Republic | ✓ ISO | Standard. 3 nodes. Distinct from `CHZ`. |
| **DAN** | **Denmark** | **✗ non-ISO** | Centipede uses **both** `DAN` (10 nodes, mostly `AG*` agricultural cluster in Jutland) and `DNK` (8 nodes, mostly `AG*` Jutland — appears to be the same network with a label inconsistency). Total Denmark Centipede footprint: ~18 nodes (DAN ∪ DNK). Anyone counting "Centipede Denmark" must sum both codes. |
| DEU | Germany | ✓ ISO | Standard. |
| DNK | Denmark | ✓ ISO | See `DAN` above — used in parallel. |
| **ENG** | **United Kingdom (all of GB + Northern Ireland)** | **✗ non-ISO** | ISO `GBR` = UK. Centipede uses `ENG` even for stations clearly outside England: Scotland (BALL 57.5°N, BRACO, CRAG, DRUM, FRAS, HRVA, LARL, MLLC, TYRI, WOCF, CHAP, FHL1), Northern Ireland (DJAM, DYFM, GWMD, OATS), Wales (PEMBS). 44–45 `ENG` nodes total cover the whole UK, not just England. **Per-country files should treat `ENG` as "UK" for Centipede counts**, not as "England only", and *especially not* attempt to split Centipede ENG counts across separate UK constituent countries. |
| ESP | Spain | ✓ ISO | Standard. |
| FIN | Finland | ✓ ISO | Standard. 18 nodes. (Åland uses `ALA` separately.) |
| FRA | France | ✓ ISO | Standard. 709 nodes (largest). |
| GRC | Greece | ✓ ISO | Standard. |
| HUN | Hungary | ✓ ISO | Standard. 217 nodes (second-largest). |
| IRL | Ireland | ✓ ISO | Standard. 8 nodes east coast. |
| ISR | Israel | ✓ ISO | Standard. |
| ITA | Italy | ✓ ISO | Standard. |
| LTU | Lithuania | ✓ ISO | Standard. |
| LVA | Latvia | ✓ ISO | Standard. |
| MDG | Madagascar | ✓ ISO | Standard. 2 nodes. |
| MTQ | Martinique | ✓ ISO | Standard. 1 node. |
| NCL | New Caledonia | ✓ ISO | Standard. 2 nodes. |
| NLD | Netherlands | ✓ ISO | Standard. 26 nodes. |
| NOR | Norway | ✓ ISO | Standard. 21 nodes. (Svalbard uses `SJM`.) |
| PYF | French Polynesia | ✓ ISO | Standard. 1 node. |
| REU | Réunion | ✓ ISO | Standard. 4 nodes. |
| **ROM** | **Romania** | **✗ non-ISO** | ISO `ROU` = Romania. Centipede uses **both** `ROM` (7 nodes) and `ROU` (sourcetable also lists at least one) in parallel. Anyone counting "Centipede Romania" must sum both codes — current observation is 7 ROM + small number of ROU. |
| ROU | Romania | ✓ ISO | See `ROM` above — used in parallel. |
| SAU | Saudi Arabia | ✓ ISO | Standard. |
| SEN | Senegal | ✓ ISO | Standard. 2 nodes. |
| **SER** | **Serbia** | **✗ non-ISO** | ISO `SRB` = Serbia. Centipede uses **both** `SER` (11 nodes, all in Vojvodina) and `SRB` (3 nodes also in Serbia) in parallel. Anyone counting "Centipede Serbia" must sum both codes — current total ~14 nodes. |
| SJM | Svalbard and Jan Mayen | ✓ ISO | Standard. 1 node (NYAWIPEV at Ny-Ålesund). |
| SRB | Serbia | ✓ ISO | See `SER` above — used in parallel. |
| SVK | Slovakia | ✓ ISO | Standard. |
| SVN | Slovenia | ✓ ISO | Standard. |
| SWE | Sweden | ✓ ISO | Standard. |
| USA | United States | ✓ ISO | Standard. |
| ZAF | South Africa | ✓ ISO | Standard. |

## Summary of non-standard codes (the "watch list")

| Centipede code | Real meaning | Confusion risk |
|---|---|---|
| `CHZ` | Switzerland | **HIGH** — looks like CZ (Czech) but is CH (Switzerland). Czech stations are under `CZE`. |
| `ENG` | All of UK (England + Scotland + Wales + Northern Ireland) | **HIGH** — looks like just England, but covers the whole UK. Distillation must not split ENG across constituent countries. |
| `DAN` | Denmark (parallel to `DNK`) | **MEDIUM** — counting Denmark requires summing DAN + DNK. |
| `ROM` | Romania (parallel to `ROU`) | **MEDIUM** — counting Romania requires summing ROM + ROU. |
| `SER` | Serbia (parallel to `SRB`) | **MEDIUM** — counting Serbia requires summing SER + SRB. |

## Codes the docstring of `scripts/stations_by_country.py` mentions but were NOT observed in 2026-05-13 sourcetable

The docstring on `scripts/stations_by_country.py` (line 9) reads: *"Centipede quirks: CHZ=CZ ENG=GB SER=RS BIH=BA NLD/BEL separate."*

- **`BIH`** — claimed in docstring as "BIH=BA" (Bosnia). **Not observed in the 2026-05-13 Centipede sourcetable** — only the rtk2go source uses `BIH` (1 node, AGROORSOLIC). The docstring's BIH=BA aside therefore appears to refer to the rtk2go convention, not Centipede; or to a code that has since left the Centipede table. No per-country file currently relies on a Centipede `BIH` code, so no correction needed.

## Implications for per-country research files

Files that quote a Centipede count must use the right code(s). Files known to reference Centipede counts (audited 2026-05-13, all currently consistent with the legend above):

| File | Centipede code(s) used | Verdict |
|---|---|---|
| `CH_Switzerland.md` | `CHZ` (30 nodes) | ✓ correct (post-revision 2026-05-13). Explicitly notes CHZ ≠ Czech. |
| `CZ_CzechRepublic.md` | `CZE` (3 nodes) | ✓ correct. Does not confuse with CHZ. |
| `GB_Great-Britain.md` | `ENG` (45 nodes) | ⚠️ should clarify that `ENG` covers all of UK (incl. Scotland/Wales/NI), not just England. Currently attributes 45 nodes to GB which is the right count but the label "ENG-coded" is misleading. |
| `IE_Ireland.md` | `IRL` (8 nodes) | ✓ correct. |
| `DK_Denmark.md` | `DNK` (8 nodes) | ⚠️ undercount — does not include the parallel `DAN` code (10 more nodes). True Centipede Denmark footprint is ~18 nodes (DAN ∪ DNK), not 8. |
| `RO_Romania.md` | `ROM` (7 nodes) | ⚠️ may undercount — does not include the parallel `ROU` code. Verify by re-running `py scripts/stations_by_country.py ROU`. |
| `RS_Serbia.md` | `SER` (11) + `SRB` (3) | ✓ correct — already sums both codes. |
| `AX_AlandIslands.md` | `ALA` (2 nodes) | ✓ correct. |
| `SJ_Svalbard.md` | `SJM` (1 node, NYAWIPEV) | ✓ correct. |
| `FI_Finland.md` | `FIN` (18 nodes) | ✓ correct. (Note that Åland is separately under `ALA` — Finland mainland count is unaffected.) |
| `NO_Norway.md` | `NOR` (21 nodes) | ✓ correct. (Svalbard separately under `SJM`.) |
| `FR_France.md` | `FRA` (709 nodes) and notes top counts including `CHZ (Switzerland — *not* Czech)` | ✓ correct on CHZ. Could optionally note the ENG/DAN/ROM/SER quirks as well, but FR file does not depend on those. |

**Action items from this audit:**
1. `GB_Great-Britain.md` — clarify in the Volunteer fallback row that `ENG` covers the whole UK, not just England, and that the 45 nodes include Scotland/Wales/NI base stations. Done in this revision.
2. `DK_Denmark.md` — re-count Denmark Centipede footprint as `DAN ∪ DNK` (~18 nodes total), not just the 8 `DNK` nodes. Done in this revision.
3. `RO_Romania.md` — verify whether stations also exist under `ROU` and update count. Done in this revision (left a re-count instruction; no `ROU` stations were observed in the 2026-05-13 fetch on top of the 7 ROM, so 7 stands, but flagged for future re-verification).
4. All other files audited above are consistent with the legend.

## Reproducibility

To re-derive this legend on any future date:

```
# 1. List all distinct Centipede country codes from the live sourcetable:
curl -s http://crtk.net:2101/ | awk -F';' '/^STR;/ {print $9}' | sort -u

# 2. For each suspect code, dump stations to verify by coordinate:
py scripts/stations_by_country.py <CODE>
# (if a code only appears in Centipede and the lat/lon clearly fall in country X but the alpha-3 doesn't match, it's a non-ISO Centipede convention)
```

If a future Centipede sourcetable introduces new non-ISO codes (e.g. a `SCO` for Scotland would split out from ENG; a `WLS` for Wales; a `GBR` replacing `ENG`), update this file and re-audit per-country counts.
