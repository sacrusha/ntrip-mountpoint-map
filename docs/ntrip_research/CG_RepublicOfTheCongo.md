# Republic of the Congo [CG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15 (full refactor — prior entry mis-dated the CERGEC / IGN FI announcement as 2024; the underlying news wire is from June 2019. Re-verified against IGS, SONEL, rtk2go, Centipede sourcetables and the local stations.json.)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **landing_url** | null |
| **access_url** | null |
| **host:port** | null |
| **tariff** | null |
| **num_stations** | 0 |
| **vrs** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no CG caster has ever been confirmed alive |
| **datum_epoch** | OMIT — no national declaration cited |

## Most Recent Project Announcements

**CERGEC / IGN FI geomatics cooperation (June 2019, resumption of prior agreement)**: On 27 June 2019 in Brazzaville, IGN FI regional director Aude Areste announced support for CERGEC (Centre de Recherche Géographique et de Production Cartographique) in geomatics projects, after meeting Minister Martin Parfait Aimé Coussoud-Mavoungou. Scope: cartographic document digitisation, satellite imagery / remote sensing, GIS training, 1:50 000 map renewal. **No CORS network, NTRIP caster, or permanent GNSS station is named, dated, or budgeted.** A protocol covered geodetic infrastructure support broadly but no deployment has been confirmed in any later reporting.

Source: https://www.adiac-congo.com/content/recherche-scientifique-le-cergec-et-lign-fi-ameliorent-la-qualite-des-donnees-geographiques (27 June 2019)
Mirror (FAAPA, same wire): https://www.faapa.info/blog/congo-linstitut-geographique-francais-entend-accompagner-le-cergec-pour-des-projets-geomatiques/ — probe returns HTTP 403 from this sandbox; reachable normally in a browser.

**CFCO / BeiDou modernisation announcement (Feb-Mar 2026)**: On 28 February 2026 in Brazzaville, Minister of Posts, Telecommunications and Digital Economy Léon Juste Ibombo received a Chinese delegation for the launch of the US$595 M Congo-Ocean Railway rehabilitation. Discussions reference integrating BeiDou navigation for train tracking, signalling and cargo traceability along the 502 km Pointe-Noire–Brazzaville corridor. **This is rolling-stock receiver integration, not a CORS / NTRIP caster deployment.** No reference station is named.

Source: https://techafricanews.com/2026/03/04/congo-modernizes-cfco-with-satellite-technology-in-partnership-with-china/

**CERGEC institutional capacity**: Adiac-Congo reporting (Feb 2017) documents that CERGEC suffers from chronic shortages of qualified personnel, modern equipment, and funding ("Nous lançons un SOS aux autorités"). No subsequent reporting reverses this picture.
Source: https://www.adiac-congo.com/content/recherche-scientifique-le-cergec-manque-de-moyens-pour-sa-politique-61373

## Verification Probes (2026-05-15)

- **IGS network** (https://network.igs.org/) — API query `country=CG` returns 0 of 814 stations. Confirmed zero IGS monuments in CG.
- **SONEL** (https://www.sonel.org/) — 0 GNSS stations in CG; nearest Atlantic-coast African stations are BJCO (Benin, ~2 100 km NW) and the South Africa cluster.
- **rtk2go sourcetable** (http://rtk2go.com:2101/SOURCETABLE, probed 2026-05-15) — 0 CG mountpoints. Substring matches like `CogRTK` are bases located in Atlanta, Georgia, USA — false positives.
- **Centipede-RTK sourcetable** (http://caster.centipede.fr:2101/SOURCETABLE, probed 2026-05-15) — 0 CG mountpoints.
- **Local data/stations.json** — `py scripts/stations_by_country.py COG` → "No stations for 'COG'". `py scripts/stations_by_radius.py -4.27 15.28 800` (Brazzaville, 800 km radius) → "No stations within 800 km".
- **GEODNET, Onocoy, RTKdata.online** — no published coverage in CG.

## Nearest Cross-Border Alternative

Nothing within ~50 km of any Congolese population centre. The nearest IGS permanent station is **NKLG (Libreville, Gabon)**, ~480 km NW of Brazzaville — IGS data archive only, not an NTRIP RTK product, and well outside any useful single-baseline range.

## Post-Processing (RINEX) Fallback

| Service | URL | Notes |
|---------|-----|-------|
| **EarthScope GNSS Data Archive** | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA). No CG monument in current archive (verified via IGS country filter, 2026-05-15). |
| **CDDIS / IGN data centres** | https://cddis.nasa.gov/ | IGS RINEX hosting for NKLG (Gabon, ~480 km NW) — useful only for very-long-baseline post-processing of static sessions. |

## Hobbyist Reality Check

For a target user (drone mapping, surveying, hobby RTK) sitting in CG:
- No public CG NTRIP caster — free, paid, or restricted — has ever been confirmed.
- No cross-border caster is within useful single-baseline distance.
- Practical options reduce to **PPP** (CSRS-PPP, Trimble RTX post-process trial, IGS final products) for static occupations, or running a private F9P / Mosaic-X5 / UM980 base on your own job site and serving rovers over your own NTRIP (self-hosted RTK2go publish or LAN caster). The georezo.net 2017 thread on CG permanent stations reaches the same conclusion.

## Sources Consulted

- IGS network (https://network.igs.org/) — API `country=CG` filter, 2026-05-15
- SONEL GNSS database (https://www.sonel.org/-GPS-.html?lang=en)
- rtk2go SOURCETABLE — http://rtk2go.com:2101/SOURCETABLE
- Centipede SOURCETABLE — http://caster.centipede.fr:2101/SOURCETABLE
- Local data/stations.json — via scripts/stations_by_country.py & stations_by_radius.py
- Adiac-Congo — CERGEC / IGN FI 2019 cooperation (https://www.adiac-congo.com/content/recherche-scientifique-le-cergec-et-lign-fi-ameliorent-la-qualite-des-donnees-geographiques)
- Adiac-Congo — CERGEC 2017 resource-shortage report (https://www.adiac-congo.com/content/recherche-scientifique-le-cergec-manque-de-moyens-pour-sa-politique-61373)
- FAAPA mirror — IGN FI / CERGEC (https://www.faapa.info/blog/congo-linstitut-geographique-francais-entend-accompagner-le-cergec-pour-des-projets-geomatiques/) — sandbox probe HTTP 403
- TechAfrica News — CFCO / BeiDou launch, 4 March 2026 (https://techafricanews.com/2026/03/04/congo-modernizes-cfco-with-satellite-technology-in-partnership-with-china/)
- GeoRezo Forum 2017 thread on CG permanent stations (https://georezo.net/forum/viewtopic.php?id=107681)
- AFREF 2024 / RCMRD workshop landing (https://ric2024.rcmrd.org/afref) — prior research cited this; URL now returns HTTP 404 (post-event takedown), removed as a load-bearing citation
- Ministère de la Recherche Scientifique (recherchescientifique.gouv.cg) — DNS no longer resolves from this sandbox; removed as a citation

## Removed / Corrected Since Prior Entry

- **Date correction**: prior entry attributed the Aude Areste / IGN FI Brazzaville announcement to "26 June 2024". The underlying news wire (adiac-congo) is dated **27 June 2019**; the FAAPA copy is the same wire. No 2024 announcement exists.
- **Dead sources removed**: `recherchescientifique.gouv.cg` host no longer resolves; `ric2024.rcmrd.org/afref` returns 404; `ignfi.fr/.../aide-delimitation-frontiere-congo/` no longer lists a Congo portfolio item. Demoted from primary citations.
- **Added**: 2026 CFCO/BeiDou announcement, clarifying it is rolling-stock GNSS, not CORS.
