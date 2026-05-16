# Åland Islands [AX] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: YES (limited) — 2 Centipede volunteer nodes on Fasta Åland (free, open). No dedicated Åland CORS programme. FINPOS (NLS Finland) RTK is restricted to research/test use only. SWEPOS (Sweden) covers Åland only via a paid Inter-Nordic add-on; baseline geometry is marginal.

## Hobbyist-ready option

| Field | Value |
|---|---|
| **landing_url** | https://www.centipede-rtk.org/ |
| **access_url** | https://docs.centipede-rtk.org/ (registration not required for sourcetable; rovers connect with any username/password) |
| **host:port** | `caster.centipede.fr:2101` |
| **num_stations** | 2 physical CORS in AX: `MAR1` (Mariehamn, 60.126, 19.951) and `FOG2` (60.014, 20.409, ~28 km ESE of Mariehamn). Confirmed in live sourcetable 2026-05-15: both rows present with country code `ALA`, RTCM3 MSM5/legacy, GPS+GLO+GAL+BDS. |
| **vrs** | no — single-base stations only |
| **tariff** | Free of charge, no tier list, no VAT applicable (associative project funded by INRAE / French research institutions) |
| **hobbyist_eligibility** | yes — open to anyone; users are also encouraged to host their own base |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-15 — `HTTP/1.1 200 OK` from `http://caster.centipede.fr:2101/`; STR rows for MAR1 and FOG2 both present with ALA country code |
| **datum_epoch** | not citably declared on Centipede pages — stations stream RTCM3 with broadcast antenna position; rover obtains coordinates in whatever frame the base was set up in (typically ITRF/IGS) |

## Cross-border alternatives

### SWEPOS (Sweden, Lantmäteriet) — paid Inter-Nordic add-on required
| Field | Value |
|---|---|
| **landing_url** | https://www.lantmateriet.se/en/geodata/gps-geodesy-and-swepos/swepos/ |
| **access_url** | https://swepos.lantmateriet.se/services/order.aspx |
| **host:port** | `swepos.lantmateriet.se:2101` (port did not respond to TCP probe from this sandbox 2026-05-15 — confirmed reachable for paid subscribers per Lantmäteriet) |
| **num_stations** | ~450 stations in Sweden; nearest to Åland are on the Stockholm archipelago east coast (≥150 km from Mariehamn). No SWEPOS station on Åland. |
| **vrs** | yes (Network-RTK / MAC) |
| **tariff** | Base Network-RTK in Sweden: 12,000 SEK/yr unlimited (1–3 subscriptions tier; bulk pricing drops to 2,500 SEK/yr at 300+); 90-day 5,000 SEK; 30-day 2,000 SEK; 10-day trial free. Statutory taxes (Swedish moms 25%) added separately — prices are ex-VAT. (Source: `swepos.lantmateriet.se/services/order.aspx`, observed 2026-05-15.) |
| | Domestic page explicitly limits use to "Sveriges gränser" (Sweden's borders). |
| | **Inter-Nordic Finland add-on**: +7,000 SEK/yr per connection (Norway: +5,000 SEK/yr). The Lantmäteriet SWEPOS overview cites these as effective from 2010-01-01 — figures may be stale, must order separately. Åland is not explicitly named but is Finnish territory and therefore falls under the Finland add-on. |
| **hobbyist_eligibility** | not restricted to professionals, but pricing is professional-tier; SWEPOS markets to surveying / construction / agriculture. |
| **legal_residency_required** | no — billing address only |
| **last_confirmed_alive** | 2026-05-15 (web portal reachable; caster TCP probe timed out from this sandbox — public confirmation is via the order portal, not the live caster) |
| **datum_epoch** | SWEREF 99 (Swedish ETRS89 realisation), epoch 1999.5. Declared on Lantmäteriet Referenssystem page: https://www.lantmateriet.se/en/geodata/gps-geodesy-and-swepos/Referenssystem/ |

### FINPOS / FinnRef (Finland, NLS Maanmittauslaitos) — RTK is research/test only, not for hobbyists
| Field | Value |
|---|---|
| **landing_url** | https://www.maanmittauslaitos.fi/en/finpos |
| **access_url** | https://www.maanmittauslaitos.fi/en/finpos/register |
| **host:port** | `opencaster.nls.fi:2101` (unencrypted) / `opencaster.nls.fi:2105` (TLS). Live 2026-05-15: HTTP 200 OK, `Server: GNSMART_Caster/2.0`. Sourcetable advertises 3 mountpoints: `SINGLE` (nearest-station RTCM 3.2 MSM4), `VRS-FKP` (network solution from SSR-FKP), `VRS-FKP-OLD` (RTCM 3.1 legacy). Fee=Y(B), Auth=Y. |
| **num_stations** | ~90 FinnRef/FINPOS stations across Finland; coverage area includes Åland geographically (no station on Åland but network-RTK interpolation reaches it). |
| **vrs** | yes (`VRS-FKP` mountpoint) |
| **tariff** | Free of charge when granted, but **RTK access is granted only for fixed-term research and testing, 3-month renewable, application must justify the research/test purpose** — explicitly *not* for production or routine survey/drone use. DGNSS and RINEX are unrestricted free with registration. |
| **hobbyist_eligibility** | no — RTK service explicitly excludes production use. A hobbyist may qualify only by framing usage as bona-fide R&D and submitting feedback. DGNSS sub-metre is fully open. |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-15 — `opencaster.nls.fi:2101` HTTP 200, streamtable reachable |
| **datum_epoch** | EUREF-FIN (Finnish ETRS89 realisation), anchor epoch 1997.0. Official declaration: JHS196 recommendation http://docs.jhs-suositukset.fi/jhs-suositukset/JHS196/JHS196.html ; also registered in EPSG (e.g. EPSG:10690 / EPSG:3067). |

## No Åland-specific government CORS programme

The autonomous Government of Åland (Ålands landskapsregering) maintains GIS / cadastral mapping services (`regeringen.ax/kartor`) but has not announced any geodetic correction service. Geodetic infrastructure for Åland is administered by Finland's National Land Survey (Maanmittauslaitos / NLS); no Åland-specific RTK programme is documented as of 2026-05-15.

## Coverage geometry note

- **Centipede MAR1 + FOG2** cover the main island (Fasta Åland) including Mariehamn and the southern/central archipelago well (typical single-base reliable radius 20–35 km with U-blox ZED-F9P). The outer archipelago (Kökar, Brändö, far northwest) is beyond reliable baseline.
- **SWEPOS** nearest stations are on the Swedish east coast (≥150 km baseline to Mariehamn) — Network-RTK accuracy degrades significantly at these distances; SWEPOS does not advertise guaranteed coverage over Åland.
- **FINPOS** has no station on Åland but interpolates from mainland Finland; coverage exists on paper, but the eligibility wall (R&D only) is the practical blocker.

## Other networks checked, none present in AX

- **rtk2go** — 0 stations in AX (verified via `scripts/stations_by_country.py`)
- **GEODNET** — 0 confirmed nodes in Åland as of 2026-05-15
- **EarthScope / UNAVCO** — no Northern Europe coverage
- **EUREF EPN** — no Åland station confirmed in EPN station list searches (`MAR2`/`MARI` not present in EPN station list as of 2026-05-15). The prior claim of an EPN station "MARI" in Mariehamn was not verifiable and has been removed.

## Post-processing (RINEX) options

| Service | URL | Cost |
|---|---|---|
| FINPOS RINEX / Raw data | https://finpos.nls.fi/ | Free of charge with FINPOS account; raw data service nominally charged but DGNSS+RINEX are open |
| EUREF EPN daily/hourly RINEX | https://epncb.oma.be/_networkdata/data_access/ | Free; nearest Finnish/Swedish EPN stations only — no Åland EPN station |

## Sources

- Centipede-RTK landing: https://www.centipede-rtk.org/ — live 2026-05-15
- Centipede docs: https://docs.centipede-rtk.org/
- Centipede caster sourcetable: `http://caster.centipede.fr:2101/` — HTTP 200 OK on 2026-05-15, MAR1 + FOG2 STR rows confirmed with ALA country code
- FINPOS service overview: https://www.maanmittauslaitos.fi/en/finpos
- FINPOS RTK service: https://www.maanmittauslaitos.fi/en/finpos/rtk
- FINPOS register: https://www.maanmittauslaitos.fi/en/finpos/register
- FINPOS Terms of Use: https://www.maanmittauslaitos.fi/en/finpos/kayttoehdot
- FINPOS portal: https://finpos.nls.fi/
- FINPOS opencaster probe: `http://opencaster.nls.fi:2101/` — HTTP 200 OK on 2026-05-15
- JHS196 EUREF-FIN declaration: http://docs.jhs-suositukset.fi/jhs-suositukset/JHS196/JHS196.html
- SWEPOS landing: https://www.lantmateriet.se/en/geodata/gps-geodesy-and-swepos/swepos/
- SWEPOS Network-RTK product page: https://www.lantmateriet.se/en/geodata/our-products/product-list/swepos-network-rtk/
- SWEPOS order portal (pricing observed 2026-05-15): https://swepos.lantmateriet.se/services/order.aspx
- SWEPOS Inter-Nordic policy (Finland +7,000 SEK/yr, Norway +5,000 SEK/yr; rates dated 2010-01-01): cited on the Lantmäteriet SWEPOS overview page above
- SWEREF 99 reference system: https://www.lantmateriet.se/en/geodata/gps-geodesy-and-swepos/Referenssystem/
- Åland regional government GIS portal (no RTK service): https://www.regeringen.ax/kartor
- EUREF EPN: https://epncb.oma.be/

## Sandbox reachability notes

- `caster.centipede.fr:2101` and `opencaster.nls.fi:2101` — both reachable via HTTP from this sandbox 2026-05-15.
- `swepos.lantmateriet.se:2101` — TCP probe timed out from this sandbox. Service is publicly reachable for paid subscribers; the sandbox blocks NTRIP/authenticated-caster ports broadly. SWEPOS being live is evidenced by the publicly reachable order portal (`swepos.lantmateriet.se/services/order.aspx`, HTTPS 200) actively serving subscriptions; Lantmäteriet has not announced any caster outage in 2026.
- `https://docs.centipede-rtk.org/docs/3.tutoriels/connect_caster` — returned 404 (page path likely changed). Root site `centipede-rtk.org` and `docs.centipede-rtk.org` reachable.
- EPN per-station info pages (`epncb.oma.be/_networkdata/siteinfo4onestation.php`) — 403 from this sandbox; the station-list itself is reachable.
