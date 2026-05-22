# Angola [AO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22 (prior: 2026-05-17, 2026-05-15, 2026-05-12, 2026-05-06)

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
| **last_confirmed_alive** | 2026-05-22 — IGCA portal https://www.igca.gov.ao/ live (latest news 2025-09-18); REPANGOL site http://www.repangol.net/ ECONNREFUSED |
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
| Network portal | http://www.repangol.net/ — ECONNREFUSED 2026-05-22 (re-probed; same result on 2026-05-06, 2026-05-12, 2026-05-17). Site is indexed by Google with the title "MGN: Rede de Estacoes Permanentes GNSS de Angola", but TCP connections from this sandbox have been refused continuously over multiple weeks |
| Operator portal | https://www.igca.gov.ao/ — live 2026-05-22, no mention of NTRIP, RTK, REPANGOL real-time access, or sourcetable; services listed are "Levantamento Topográficos", "Coordenadas", "Venda de Mapas" |

Earlier research (now removed) cited the OICRF paper "Rigorous estimation
of the coordinates of two new national permanent GNSS networks in Africa
— NIGNET (Nigeria) and REPANGOL (Angola)" as a datum/frame source. URL
returns HTTP 404 (re-checked 2026-05-22); the operator portal does not
declare the frame, so per the primer's citation rule the datum_epoch
field is omitted.

Secondary technical sources (IOGP "Coordinate Reference Systems and
transformations for offshore Angola" 2023 via ANPG;
[IOGP doc](https://anpg.co.ao/wp-content/uploads/2023/07/IOGP_Angola-Coordinate-Reference-Systems_373-27_June2023.pdf))
describe REPANGOL's 18-station 2010–2011 campaign as connecting Angola
to ITRF2008, with the resulting national realisation named **RSA013**
(Reference System para Angola 2013). RSA013 is the Angolan national
realisation name; it is **not** an EPSG-registered code (no `RSA013`
identifier in epsg.io). RSA013 is mandatory for offshore exploration
blocks assigned after 2015 per Angolan petroleum regulation. The
operator (IGCA) site does not declare the frame in any page accessible
from the sandbox, so the field stays omitted per spec.

## Recent project activity (no NTRIP outcome)

- **Decreto Presidencial n.º 115/21 (2021):** IGCA statute; assigns REPANGOL management. No RTK service mandate.
- **DGT Portugal / IGCA cooperation:** geodesy/cadastre knowledge exchange. No public NTRIP output.
- **ESRI 2025 case study** (Angola land administration with cadastre/GIS): documents IGCA modernisation; no public RTK service described.
- **ANGOSAT-2 connectivity hub launch (Dec 2025):** satcomms / broadband, not GNSS corrections — unrelated despite surface similarity.

## Local data verification (2026-05-22)

- `py scripts/stations_by_country.py AGO` → no entries (rtk2go / Centipede / EarthScope all empty for AGO).
- `py scripts/stations_by_radius.py -8.84 13.23 600` → no stations within 600 km of Luanda.
- Direct rtk2go live sourcetable probe — 0 Angola-tagged mountpoints.
- Direct Centipede live sourcetable probe — 0 Angola-tagged mountpoints.
- Corsmap / GIM International (re-checked 2026-05-22) lists Angola among the 25 African countries with at least some CORS hardware sourced by Corsmap founders, but flagged "unverified" (no local-custodian contact made); no NTRIP host:port published in any aggregator.

Nearest cross-border alternatives are well over 50 km from any Angolan
border (no usable Namibia, DRC, Zambia or Congo public NTRIP within
practical RTK baseline). RTK from a neighbouring country is not viable.

## Post-processing fallback

| Service | URL | Cost |
|---------|-----|------|
| REPANGOL (RINEX, via IGCA) | http://www.repangol.net/ (offline 2026-05-17); contact via https://www.igca.gov.ao/ | Unknown — contact IGCA |
| AFREF Operational Data Centre | http://www.afrefdata.org/ (ECONNREFUSED from sandbox 2026-05-17; reported reachable for users by AFREF/GIM International) | Free for participating stations |

## Sandbox probes (2026-05-22)

- WebFetch http://www.repangol.net/ → ECONNREFUSED (TCP refused; same result over 2026-05-06, 2026-05-12, 2026-05-17; this matches the public report that the portal has been long-term down).
- WebFetch https://www.igca.gov.ao/ → 200 OK, content rendered, latest news still dated 2025-09-18.
- WebFetch https://ntrip-list.com/africa/ → 200 OK; no AO row.
- WebFetch https://www.oicrf.org/.../nignet-nigeria-and-repangol-angola- → HTTP 404 (previously cited; long-term dead, removed from sources).
- WebFetch http://www.afrefdata.org/welcome.php → ECONNREFUSED from sandbox.
- WebFetch https://map.centipede-rtk.org/ → page loads but station list not in fetched HTML; relied on `stations_by_country.py AGO` (empty) and live Centipede sourcetable probe (empty) for ground truth.

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
