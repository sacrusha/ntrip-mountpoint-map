# Belgium [BE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: YES — three free regional public NTRIP casters covering all Belgium (FLEPOS/Flanders, WALCORS/Wallonia, GPSBru/Brussels); VRS on two of three; plus 17 Centipede volunteer nodes and 2 rtk2go bases providing redundant free coverage

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — three separate regional networks forming complete national coverage |

---

### FLEPOS — Flanders (Agentschap Informatie Vlaanderen)

| Field | Value |
|---|---|
| **Operator** | Agentschap Informatie Vlaanderen (Government of Flanders) |
| **host:port** | `flepos.vlaanderen.be:2101` |
| **IP (as of June 2024)** | 3.64.78.173 (migrated June 17, 2024) |
| **VRS** | Yes |
| **Key mountpoint** | `FLEPOSVRS32GREC` (RTCM 3.2; GPS+GLO+GAL+BDS) |
| **tariff** | Free — account registration required at flepos.vlaanderen.be |
| **hobbyist_eligibility** | Yes — ArduSimple notes "professional organizations" preferred but individual registration confirmed possible; subscription types include Survey, Agriculture, Machine guidance, Maritime, Education, Test |
| **legal_residency_required** | Unclear — Belgian government network; no explicit foreign restriction stated, but primarily designed for Belgian users |
| **last_confirmed_alive** | `flepos.vlaanderen.be:2101` returned `SOURCETABLE 200 OK` on 2026-05-06 (curl confirmed) |

**Registration:** Admin account created via flepos.vlaanderen.be; admin login used to manage device subscriptions; each device gets its own credentials. Support: support.flepos@vlaanderen.be.

---

### WALCORS — Wallonia (Service Public de Wallonie)

| Field | Value |
|---|---|
| **Operator** | Service Public de Wallonie (SPW) — DGO3 (Direction générale opérationnelle Agriculture, Ressources naturelles et Environnement) |
| **host:port** | `gnss.wallonie.be:8081` |
| **IP (as of 2026)** | 157.164.253.36 |
| **VRS** | Yes — VRS, IMAX, and NEAR correction types |
| **Key mountpoints** | `VRS32GREC` (VRS, RTCM 3.2, all constellations) · `IMAX32GREC` (Leica iMAX) · `NEAR32GREC` (nearest physical station) |
| **tariff** | Free — registration required via form at gnss.wallonie.be |
| **hobbyist_eligibility** | Yes — three user categories (SURVEY, GIS, GUIDAGE); individual registration accepted. Access geographically restricted to Belgium territory (software polygon limit) |
| **legal_residency_required** | Unclear — no explicit residency requirement, but geographic software limit (corrections only delivered within Belgium) |
| **last_confirmed_alive** | gnss.wallonie.be website HTTP-reachable 2026-05-06; port 8081 timed out from external IP (firewall likely restricts to Belgian IPs or registered users). Login portal confirmed accessible |

**Registration:** Fill online form at gnss.wallonie.be (French/German); separate user per receiver; 5 MB/hr data volume. Contact: gnss@spw.wallonie.be / +32 81 71 59 22.

Network: 22 stations across Wallonia + 13 exchanged with neighbouring networks (Luxembourg, Netherlands, France, Germany). Coverage area: Wallonie only.

---

### GPSBru / AGN — Brussels Capital Region (NGI / Institut Géographique National)

| Field | Value |
|---|---|
| **Operator** | NGI (Nationaal Geografisch Instituut / Institut Géographique National) |
| **host:port** | Via AGN portal at agn.ngi.be — host/port provided after login request |
| **Station** | UKKE (Uccle/Ukkel — NGI campus) — single physical station |
| **VRS** | No — single-base corrections only |
| **Key mountpoints** | `UKKE_GNSS_3.0` (RTCM 3.0; GPS+GLONASS) · RTCM 2.1/2.3 variants (GPS only) |
| **tariff** | Free — login request required |
| **hobbyist_eligibility** | Yes — registration form on agn.ngi.be; no stated professional restriction |
| **legal_residency_required** | No restriction stated |
| **last_confirmed_alive** | agn.ngi.be confirmed HTTP 200 on 2026-05-06; RTCM 3.0 stream uses GPS+GLONASS dual-constellation for improved urban sky coverage |

**RTK range:** Corrections usable within ~20 km of Ukkel station; DGPS usable throughout Belgium.

---

## Hobbyist Path

All three networks are free and allow individual registration. For full Belgium coverage:
- Flanders → FLEPOS (`flepos.vlaanderen.be:2101`)
- Wallonia → WALCORS (`gnss.wallonie.be:8081`)
- Brussels → GPSBru (`agn.ngi.be`)

Together the three networks provide VRS-based RTK (FLEPOS, WALCORS) and single-base RTK (GPSBru) across all of Belgium at no cost.

## Volunteer / Community Backstop

Belgium has dense volunteer-base coverage even though the government networks are free:

- **Centipede-RTK**: 17 BEL-coded nodes confirmed in `data/stations.json` 2026-05-12 — clustered in Wallonia and the Brussels–Antwerp corridor (mountpoints include `5640`, `AHOA`, `AIDE`, `ALEX`, `BIST`, `COCO`, `CRA1`, `DEBEN`, `DEPO`, `FLEN`, `HAYE`, `JFDE`, `KUBA`, `LEMA`, `LEON`, `NLER`, `STAVE`). Access via `caster.centipede.fr:2101` — no signup required.
- **rtk2go**: 2 BEL-coded volunteer bases — `ROOS1` (50.84°N, 4.86°E, central Belgium) and `Stuer` (51.19°N, 4.25°E, Antwerp area). Access via `rtk2go.com:2101`.

These are useful redundancy if the government caster a user is registered with is down, or as a quick-start option without going through registration.

## EUREF / Scientific Relay

The Royal Observatory of Belgium (ROB) operates a EUREF NTRIP caster at `www.euref-ip.be:2101` with EPN station streams, primarily for scientific post-processing — not for RTK rover use.

## Sources Consulted
- FLEPOS login portal: https://flepos.vlaanderen.be/Login.aspx (observed 2026-05-06)
- FLEPOS NTRIP settings (Vlaanderen Intern): https://overheid.vlaanderen.be/Flepos-NTRIP (observed 2026-05-06, returned 403 — content sourced from CGEOS and Fieldbee references)
- CGEOS Belgium GNSS networks summary: https://cgeosbe.weebly.com/reseaux-gnss.html (observed 2026-05-06)
- WALCORS real-time access page: https://gnss.wallonie.be/walcors/acces-au-reseau/acces-au-reseau-1.html (observed 2026-05-06)
- WALCORS FAQ: https://gnss.wallonie.be/walcors/foire-aux-questions.html (observed 2026-05-06)
- WALCORS products page: https://gnss.wallonie.be/walcors/produits-delivres.html (observed 2026-05-06)
- GPSBru/AGN NTRIP info (NL): https://agn.ngi.be/NL/NL1-2.jsp (observed 2026-05-06)
- GPSBru/AGN overview (NL): https://agn.ngi.be/NL/NL1.jsp (observed 2026-05-06)
- EUREF caster ROB: https://www.euref-ip.be/ (observed 2026-05-06)
- ArduSimple Belgium caster list: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-belgium/ (observed 2026-05-06)
- curl probe of `flepos.vlaanderen.be:2101` — SOURCETABLE 200 OK confirmed 2026-05-06
- curl probe of `gnss.wallonie.be:2101` and `:8081` — port 2101 timed out; port 8081 resolves to same IP 157.164.155.179 (firewall restricted) 2026-05-06
