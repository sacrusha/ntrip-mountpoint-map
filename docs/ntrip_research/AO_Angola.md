# Angola [AO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-15, 2026-05-12, 2026-05-06)

## Status: No public NTRIP RTK caster

A national geodetic CORS network exists (REPANGOL, 18 stations, operated
by IGCA) but its purpose is reference frame densification and
post-processing. No public real-time NTRIP/RTK service is documented,
advertised, or community-reported. Zero AO mountpoints on rtk2go,
Centipede, GEODNET, ONOCOY, NTRIP-list Africa, or corsstations.com.

| Field | Value |
|---|---|
| **landing_url** | https://www.igca.gov.ao/ (IGCA, operator) |
| **access_url** | null — no public access path is published |
| **host:port** | null — no NTRIP endpoint publicly documented |
| **tariff** | null — no service |
| **num_stations** | 18 physical CORS (REPANGOL), not exposed as NTRIP |
| **vrs** | null — no service |
| **hobbyist_eligibility** | null — no service |
| **legal_residency_required** | null — no service |
| **last_confirmed_alive** | 2026-05-17 — IGCA portal https://www.igca.gov.ao/ live (latest news 2025-09-18); REPANGOL site http://www.repangol.net/ ECONNREFUSED |
| **datum_epoch** | omitted — no citable official declaration accessible |

## REPANGOL — physical CORS network (no public RTK output)

| Detail | Value |
|--------|-------|
| Network name | REPANGOL (Rede de Estações Permanentes GNSS de Angola) |
| Operator | IGCA (Instituto Geográfico e Cadastral de Angola) |
| Stations | 18 permanent CORS |
| Installed | 2010 (initial geodetic campaign 2010–2011) |
| Past maintenance | TeroMovigo (works completed 2020) |
| Stated purpose | Geodetic reference frame densification, post-processing support |
| Network portal | http://www.repangol.net/ — ECONNREFUSED 2026-05-17 (re-probed; same result 2026-05-06 and 2026-05-12) |
| Operator portal | https://www.igca.gov.ao/ — live 2026-05-17, no mention of NTRIP, RTK, REPANGOL real-time access, or sourcetable |

Earlier research (now removed) cited the OICRF paper "Rigorous estimation
of the coordinates of two new national permanent GNSS networks in Africa
— NIGNET (Nigeria) and REPANGOL (Angola)" as a datum/frame source. URL
returns HTTP 404 (2026-05-17); claim of ITRF2008 cannot be verified from
a live primary source, so the datum_epoch field is omitted per spec.

## Recent project activity (no NTRIP outcome)

- **Decreto Presidencial n.º 115/21 (2021):** IGCA statute; assigns REPANGOL management. No RTK service mandate.
- **DGT Portugal / IGCA cooperation:** geodesy/cadastre knowledge exchange. No public NTRIP output.
- **ESRI 2025 case study** (Angola land administration with cadastre/GIS): documents IGCA modernisation; no public RTK service described.
- **ANGOSAT-2 connectivity hub launch (Dec 2025):** satcomms / broadband, not GNSS corrections — unrelated despite surface similarity.

## Local data verification (2026-05-17)

- `py scripts/stations_by_country.py AGO` → no entries (rtk2go / Centipede / EarthScope all empty for AGO).
- `py scripts/stations_by_radius.py -8.84 13.23 300` → no stations within 300 km of Luanda.
- `py scripts/stations_by_radius.py -12.5 13.5 300` (Benguela / Lobito) → no stations.
- `py scripts/stations_by_radius.py -12.6 23.4 300` (eastern Angola, Lunda) → no stations.

Nearest cross-border alternatives are well over 50 km from any Angolan
border (no usable Namibia, DRC, Zambia or Congo public NTRIP within
practical RTK baseline). RTK from a neighbouring country is not viable.

## Post-processing fallback

| Service | URL | Cost |
|---------|-----|------|
| REPANGOL (RINEX, via IGCA) | http://www.repangol.net/ (offline 2026-05-17); contact via https://www.igca.gov.ao/ | Unknown — contact IGCA |
| AFREF Operational Data Centre | http://www.afrefdata.org/ (ECONNREFUSED from sandbox 2026-05-17; reported reachable for users by AFREF/GIM International) | Free for participating stations |

## Sandbox probes (2026-05-17)

- WebFetch http://www.repangol.net/ → ECONNREFUSED (TCP refused; same result on 2026-05-06 and 2026-05-12; this matches the public report that the portal has been long-term down).
- WebFetch https://www.igca.gov.ao/ → 200 OK, content rendered, latest news 2025-09-18.
- WebFetch https://ntrip-list.com/africa/ → 200 OK; no AO row.
- WebFetch https://www.oicrf.org/.../nignet-nigeria-and-repangol-angola- → HTTP 404 (previously cited; now dead, removed from sources).
- WebFetch http://www.afrefdata.org/welcome.php → ECONNREFUSED from sandbox.
- WebFetch https://map.centipede-rtk.org/ → page loads but station list not in fetched HTML; relied on `stations_by_country.py AGO` (empty) for ground truth.

## Sources consulted

- https://www.igca.gov.ao/ (operator portal — live)
- http://www.repangol.net/ (network portal — offline)
- https://angolex.com/paginas/decreto-presidencial/estatuto-organico-do-instituto-geografico-e-cadastral-de-angola-115a-21a.html (Decreto 115/21 text)
- https://teromovigo.com/project/maintenance-of-repangol-network/ (2020 maintenance record)
- https://www.esri.com/en-us/lg/industry/government/stories/angola-modernizes-land-administration-gis-cadastre-management (ESRI 2025 case study)
- https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa (Corsmap Africa — confirms AO has CORS hardware but no verified custodian contact)
- https://ntrip-list.com/africa/ (no AO entry)
- http://www.afrefdata.org/welcome.php (AFREF; unreachable from sandbox)
- Local verification: `scripts/stations_by_country.py AGO`, `scripts/stations_by_radius.py` Luanda/Benguela/Lunda (all empty)
