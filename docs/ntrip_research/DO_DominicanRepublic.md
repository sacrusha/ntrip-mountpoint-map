# Dominican Republic [DO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (prior: 2026-05-17)

## Status

Four Dominican-Republic CORS / NTRIP layers exist:

1. **FUNDCORSRD** — non-profit nationwide caster, live and probed; access by credential request (not self-service); ~40 unique physical stations on a single SNIP caster.
2. **IGN REGNA-RD** — government network. Two IGN-owned CORS (Moca IGMO, Puerto Plata IGPP) installed 2025-11-12; IGN has also certified third-party CORS as part of the Active Reference Network (see below). Registration portal `ntrip.ign.gob.do` reachable but NTRIP port not externally probable.
3. **TRIMBLERD / CORS RD (Geomedición, Instrumentos y Sistemas, SRL)** — commercial Trimble-based CORS network of 34 stations; not a unified NTRIP sourcetable but per-station Trimble GNSS receivers exposed on the public Internet (each station hosts a Trimble device web UI; NTRIP credentials per receiver via subscription).
4. **CODIA CORS-MET** — gated to licensed CODIA members.

| Field | Value |
|---|---|
| Active public NTRIP RTK caster | Yes — FUNDCORSRD curl-confirmed live 2026-05-21 (~40 stations, credential request); IGN REGNA-RD government portal reachable; TRIMBLERD commercial (per-station, ~34 stations); CODIA licensed-only. |

### FUNDCORSRD — non-profit national caster

| Field | Value |
|---|---|
| landing_url | https://fundcorsrd.com/ |
| access_url | https://fundcorsrd.com/ (credential request via the site's contact form; no self-service signup) |
| host:port | `190.166.228.161:2103` |
| num_stations | ~40 unique physical stations (live sourcetable 2026-05-21: 76 STR rows + 1 `NEAR` routing alias = 77 mountpoints; each station typically exposes paired RTCM 3.0 and RTCM 3.2/3.3 MSM streams, suffix `32` = MSM stream). Station codes observed in the live sourcetable: BARA, FCAC, FCBN, FCBO, FCBR, FCCT, FCCZ, FCDA, FCDN, FCEP, FCHT, FCHY, FCJA, FCLM, FCLR, FCLT, FCMF, FCMI, FCMO, FCNA, FCNB, FCNV, FCOC, FCPE, FCPS, FCPT, FCRS, FCSF, FCSJ, FCSM, FCUP, FCVP, FCVV, HGUY, LVEG, PEVA, SAMN, SJUM, SPED, SROD, STGO. The dual-stream pairing is not perfectly clean — FCJA, FCMI, FCNA appear without the paired `32` MSM mount and FCPE appears only on the legacy stream, while the 76-row total does not divide evenly into clean pairs of 38 + 4 singles. The precise count of physical stations vs. mountpoint aliases is therefore approximate (~40); FUNDCORSRD does not publish a definitive list. |
| vrs | No — single-base station mountpoints only; only routing alias is `NEAR`. |
| tariff | not published — credentials issued by application to fundcorsrd.com / fundcorsrd@gmail.com |
| hobbyist_eligibility | unclear — non-profit founded by surveyors; self-described as serving "society in general" (838+ users as of May 2025 office inauguration article); access decided per request |
| legal_residency_required | unclear |
| last_confirmed_alive | 2026-05-21 — `190.166.228.161:2103` `SOURCETABLE 200 OK` from curl; SNIP `[wPRO] R3.19.00 of:Dec 19 2025`; 76 STR + 1 NEAR rows |
| datum_epoch | omitted — no citable operator declaration on fundcorsrd.com. (Caster software is SNIP, which propagates RTCM 1006 ARP coordinates; receivers ignore DF021 ITRF-year field per primer.) |

### IGN REGNA-RD — government Active Reference Network

| Field | Value |
|---|---|
| operator | Instituto Geográfico Nacional "José Joaquín Hungría Morell" (IGN-JJHM) |
| landing_url | https://ign.gob.do/red-geodesica-nacional-activa/ |
| access_url | https://ntrip.ign.gob.do/ (registration portal — HTTPS 200 from curl 2026-05-21) |
| host:port | `ntrip.ign.gob.do` (registration portal HTTPS reachable; raw NTRIP port not externally probable from sandbox — consistent with WAF/IP filter) |
| num_stations (IGN-owned) | 2 own CORS — IGMO (Moca) + IGPP (Puerto Plata), installed and brought into service 2025-11-12. IGN has additionally certified third-party CORS belonging to the TRIMBLERD network as part of the National Active Geodetic System (11 stations Region Norte, 6 stations Region Suroeste, and 5 stations Registro Inmobiliario). These certified third-party stations are not IGN-operated; they belong to Geomedición SRL / Registro Inmobiliario. |
| vrs | unknown |
| tariff | not published — IGN does not state a price on the REGNA-RD page or the registration portal; nationally funded service so a free tier is plausible but no operator declaration confirms this |
| hobbyist_eligibility | unclear — credentialed via registration portal; no published policy excluding hobbyists |
| legal_residency_required | unclear |
| last_confirmed_alive | 2026-05-21 — `ntrip.ign.gob.do` HTTPS 200; IGN news page for IGMO/IGPP dated 2025-11-12 |
| datum_epoch | omitted — REGNA-RD page is a stub; IGN news article does not state datum/epoch. Underlying CORS-RD stations are certified under "SIRGAS-IGS-NGS-EarthScope standard" (IGN-JJHM news 2023-10-16); not citable as a service-level declaration. |

### TRIMBLERD / CORS RD — commercial (Geomedición SRL)

| Field | Value |
|---|---|
| operator | Geomedición, Instrumentos y Sistemas, SRL (TRIMBLE Caribbean partner; trading as Geomatica.com.do). Founded 1998; first CORS `RDSD` installed 2004. |
| landing_url | https://www.geomatica.com.do/pages/cors-rd |
| access_url | https://www.geomatica.com.do/pages/request-for-quote (commercial quotation request form; per-station subscription) |
| host:port | Not a unified NTRIP caster sourcetable. Each station is reached individually as a Trimble GNSS receiver, examples: `190.80.239.109:81` (ATT3, Santo Domingo), `rdci.ddns.net:8080` (RDCI, La Ciénaga), `ggsrdma.ddns.net:8080` (RDMA, Valverde Mao). Probed 2026-05-21: ATT3 endpoint returns a Trimble web UI ("Copyright(c) 2005-2023 Trimble Inc., GPS, GLONASS, Galileo, BeiDou, QZSS, NavIC, SBAS, GNSS Trimble Geomatics Infrastructure Survey VRS Construction SPS") — credential-gated per-receiver NTRIP, not a sourcetable index. |
| num_stations | 34 (per CORS-RD page list, with codes ATT3, RDCI, RDEH, RDLT, RDM2, RDMA, RDPP, RDSC, RDSF, RDVE, RDSD among others). |
| vrs | No (Pivot Web frontend not observed). Probe of station IPs (e.g. ATT3 at `190.80.239.109:81`) returns per-receiver Trimble web UIs; no Trimble Pivot Web NRTK aggregator at a unified caster address has surfaced, which is evidence against an active VRS service. Each station distributes single-station RTCM. |
| tariff | commercial subscription — not published; quotation by request. |
| hobbyist_eligibility | yes in principle (subscription-based; no licensing requirement on the page), priced commercially. |
| legal_residency_required | no (commercial subscription) |
| last_confirmed_alive | 2026-05-21 — geomatica.com.do CORS-RD page reachable; ATT3 (`190.80.239.109:81`) Trimble receiver UI reachable. |
| datum_epoch | omitted — operator does not publish a service-level datum/epoch. 11 of the Norte stations (and 6 Suroeste) were certified by IGN-JJHM under "estándar de SIRGAS-IGS-NGS-EarthScope" but no datum is stated on the operator site itself. |

### CODIA CORS-MET

Restricted to licensed members of CODIA (Colegio Dominicano de Ingenieros, Arquitectos y Agrimensores). Not accessible to non-licensed individuals or hobbyists. Service-specific page not located on `codia.org.do` as of 2026-05-21.

### TopNETlive (Topcon, global)

Paid commercial global subscription network — `rtk.topnetlive.com:2101`; DR coverage listed on corsstations.com. Open enrolment via Topcon dealers; pricing not on public Topcon page. Treated as international caster; relevant for completeness only.

## Volunteer / Global Coverage (2026-05-21)

- **rtk2go (DOM-coded, 2 nodes per `py scripts/stations_by_country.py DOM`):** `geofis_mbase` (18.46, -69.92) and `geofis_ovni` (18.47, -69.91), both at Santo Domingo. Mountpoint names suggest institutional rebroadcasts (the "geofis" prefix is consistent with UASD's Instituto de Geofísica), but this is name-based inference only — no operator-side acknowledgement of these mountpoints has been located. Both nodes carry `nmea=1` in the rtk2go sourcetable.
- **earthscope (NOTA) DOM-coded, 10 stations:** BARA, CN05, CN06, CN07, CN27, LVEG, RDMA, RDSD, SPED, SROD. Accessible via NULA non-commercial registration.
- **igs_ip:** 1 station `RDSD00DOM0` (18.46, -69.91).
- **Centipede / GEODNET / ONOCOY:** no DOM-coded nodes visible in project sourcetables or public coverage maps.

## Most Recent Project Announcement

- **2025-11-12 — IGN-JJHM**: Installed IGMO (Moca) and IGPP (Puerto Plata), the two first IGN-owned CORS in REGNA-RD ("La incorporación de estas dos nuevas estaciones CORS … refuerza la capacidad técnica nacional"). Border-zone CORS evaluation underway with Ministerio de Defensa for Dajabón, Elías Piña (Comendador, Pedro Santana), Jimaní, Pedernales. https://ign.gob.do/ign-jjhm-fortalece-la-infraestructura-geodesica-nacional-con-la-instalacion-de-dos-nuevas-estaciones-de-dos-cors-en-moca-y-puerto-plata/
- **2023-10-16 — IGN-JJHM**: certified 11 CORS in the Región Norte belonging to TRIMBLERD (Geomedición SRL): ATT3, RDCI, RDEH, RDLT, RDM2, RDMA, RDPP, RDSC, RDSF, RDVE, RDSD. Subsequent IGN-JJHM certifications cover 6 stations in Región Suroeste and 5 stations operated by Registro Inmobiliario.
- **2025-05-21 — FUNDCORSRD**: Office inauguration in Santo Domingo. Inmobiliario.do quotes FUNDCORSRD: "ha instalado 30 estaciones a nivel nacional, brindando cobertura a más de 838 usuarios" (30 stations nationwide, 838+ users). The BARA, LVEG, SPED, SROD codes that appear in the FUNDCORSRD sourcetable are also Registro Inmobiliario (Jurisdicción Inmobiliaria) installations, but no source published in May 2025 combined the two networks into a single station total. Equipment: ComNav SinoGNSS M300 Pro receivers + AT600 antennas (GPS World 2023-10-09). Live sourcetable 2026-05-21 lists ~40 unique stations.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| FUNDCORSRD RINEX | https://fundcorsrd.com/ | Account required (same registration as live caster) |
| EarthScope / SIRGAS-CON DR stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (NULA); USD 1,000/seat/yr commercial |
| IGN REGNA-RD RINEX | https://ign.gob.do/ / https://ntrip.ign.gob.do/ | Likely free with account |

## Sources

- FUNDCORSRD live sourcetable: `190.166.228.161:2103` (curl 2026-05-21; 76 STR + 1 NEAR; SNIP wPRO R3.19.00 of:Dec 19 2025)
- FUNDCORSRD homepage: https://fundcorsrd.com/
- Inmobiliario.do — "Office opens to strengthen technological services for surveyors" (2025-05-21; "30 estaciones a nivel nacional, ... 838 usuarios"): https://inmobiliario.do/en/office-opens-to-strengthen-technological-services-for-surveyors/
- GPS World — "ComNav Technology and Dominican Republic Forge Advanced CORS Network" (2023-10-09): https://www.gpsworld.com/comnav-technology-and-dominican-republic-forge-advanced-cors-network/
- IGN REGNA-RD landing page (HTTPS 200, 2026-05-21): https://ign.gob.do/red-geodesica-nacional-activa/
- IGN-JJHM news, IGMO + IGPP installation (2025-11-12): https://ign.gob.do/ign-jjhm-fortalece-la-infraestructura-geodesica-nacional-con-la-instalacion-de-dos-nuevas-estaciones-de-dos-cors-en-moca-y-puerto-plata/
- IGN-JJHM news, 11 CORS Norte certification to TRIMBLERD (2023-10-16): https://ign.gob.do/el-instituto-geografico-nacional-jose-joaquin-hungria-morel-ign-jjhm-entrega-certificacion-de-11-cors-gnss-de-la-region-norte-de-la-republica-dominicana/
- Dominican Today (2025-11-12) — Moca + Puerto Plata CORS coverage: https://dominicantoday.com/dr/local/2025/11/12/new-cors-stations-strengthen-dominican-republics-geographic-infrastructure/
- Geomatica.com.do CORS-RD product page (34 stations, per-station IPs/ports): https://www.geomatica.com.do/pages/cors-rd
- Geomatica.com.do Red CORS Trimble RD page: https://www.geomatica.com.do/pages/red-cors-trimble-rd
- Trimble receiver web UI on ATT3 station (probed 2026-05-21): `http://190.80.239.109:81/`
- ArduSimple Dominican Republic page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-dominican-rep/
- `py scripts/stations_by_country.py DOM` (2026-05-21): 10 earthscope + 2 rtk2go + 1 igs_ip
