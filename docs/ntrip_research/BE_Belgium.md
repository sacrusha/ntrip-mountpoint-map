# Belgium [BE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: MIXED — three regional government NTRIP RTK casters covering all Belgium (FLEPOS / Flanders, WALCORS / Wallonia, GPSBru / Brussels). FLEPOS is **professional-organization-only — hobbyists CANNOT register.** WALCORS allows individuals via SURVEY/GIS categories. GPSBru registration accepts individuals. Geographic / IP restrictions apply on WALCORS. Volunteer Centipede (17 BEL nodes) and rtk2go (3 BEL bases) provide hobbyist fallback.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — three separate regional networks forming complete national coverage; only two are open to hobbyists |

---

### FLEPOS — Flanders (Agentschap Digitaal Vlaanderen)

| Field | Value |
|---|---|
| **Operator** | Agentschap Digitaal Vlaanderen (Government of Flanders) |
| **landing_url** | `https://www.vlaanderen.be/digitaal-vlaanderen/onze-diensten-en-platformen/flepos-centimeternauwkeurige-positiebepaling` — Digitaal Vlaanderen FLEPOS product page. Verified 2026-05-15 (200 OK); describes service, audience (professional users only), free-of-charge model, links to registration. Replaces former `overheid.vlaanderen.be/en/producten-diensten/centimetre-accurate-positioning-flepos` which now 302-redirects to `vlaanderen.be/intern` (internal staff portal, broken for visitors). |
| **access_url** | `https://www.vlaanderen.be/digitaal-vlaanderen/onze-diensten-en-platformen/flepos-centimeternauwkeurige-positiebepaling/registratie` — registration page; states the two-step process and explicitly excludes individuals. Verified 2026-05-15 (200 OK). |
| **host:port** | `flepos.vlaanderen.be:2101` (IP 3.64.78.173 since 2024-06-17) |
| **VRS** | Yes |
| **num_stations** | 45 declared GNSS reference stations; 33 operated directly by Informatie Vlaanderen, remainder cross-border partners |
| **Key mountpoints** | `FLEPOSVRS32GREC` (RTCM 3.2; GPS+GLO+GAL+BDS) · `FLEPOSVRS31GR` (RTCM 3.1; GPS+GLO) — both observed in live sourcetable 2026-05-15 |
| **tariff** | Free; user pays only mobile-data costs. No VAT mentioned (gratis service). Observed 2026-05-15 on `vlaanderen.be/digitaal-vlaanderen` product page. |
| **hobbyist_eligibility** | **No.** Operator product page `vlaanderen.be/.../flepos-.../registratie` states the policy directly: *"Enkel professionele organisaties kunnen zich registreren en een abonnement aanvragen (niet voor particulieren)"* — only professional organisations can register and request a subscription (not for private individuals). The dynamic form repeats this scoped to itself: *"Dit online registratieformulier is uitsluitend bedoeld voor professionele organisaties. Particulieren kunnen hiermee geen FLEPOS-abonnement aanvragen"* (note: `hiermee` = "with this form", so taken alone the form quote is form-scoped — the policy-level statement is on the parent product page). Belgian organisations must supply a KBO enterprise number; foreign organisations supply an equivalent government identifier. ArduSimple page (probed 2026-05-15, displayed update date 2026-05-15) corroborates: "available only to professional organizations." **Conflict with prior research** (2026-05-06 / 2026-05-12, which read ArduSimple as "professional preferred but individuals possible"): either ArduSimple's wording changed recently or the prior agent over-read "preferred" as "non-exclusive". The operator's own product page now closes the question. |
| **legal_residency_required** | No — foreign professional organisations may register (form has explicit "buitenlands" / foreign-org branch supplying alternate identifier in lieu of KBO). |
| **last_confirmed_alive** | `flepos.vlaanderen.be:2101` returned SOURCETABLE 200 OK from this sandbox on 2026-05-15 (`curl` with `Ntrip-Version: Ntrip/2.0`); first STR rows for `FLEPOSVRS31GR` and `FLEPOSVRS32GREC` retrieved. |
| **datum_epoch** | Omitted — no citable per-network declaration found on operator pages. (Belgium uses ETRS89; the national realisation BEREF2002 / EPSG:3812 is widely referenced but no FLEPOS-operator page pins an explicit epoch.) |

Subscription categories: Survey, Agriculture, Machine Control (Machinebesturing), Maritime, Education, Test (durations 1–3 years; auto-renew except Test). Admin login then creates per-device subscriptions. Support: `support.flepos@vlaanderen.be`. Old domain `ntrip.flepos.be` is NXDOMAIN.

---

### WALCORS — Wallonia (Service Public de Wallonie)

| Field | Value |
|---|---|
| **Operator** | Service Public de Wallonie (SPW) — Direction de la Géométrologie (DGEO). Operations subcontracted to Leica Geosystems (helpdesk e-mail `walcors@leica-geosystems.com`). |
| **landing_url** | `https://gnss.wallonie.be/walcors.html` — operator-owned WALCORS landing on the SPW GNSS portal. Verified 2026-05-15. |
| **access_url** | `https://www.wallonie.be/fr/demarches/acceder-au-reseau-permanent-de-stations-gnss-de-reference-walcors` — official SPW démarche page describing how to request access. Backup: `https://gnss.wallonie.be/walcors/acces-au-reseau/acces-au-reseau-1.html` (technical access description). Both observed 2026-05-15. |
| **host:port** | `gnss.wallonie.be:8081` (IP 157.164.253.36) |
| **VRS** | Yes — three correction types: VRS (virtual reference station), IMAX (Leica MAX-cell), NEAR (single nearest physical). |
| **num_stations** | **23** stations across Wallonia (operator confirms 2026-05-15) + 13 exchanged with neighbouring networks (LU/NL/FR/DE) for edge-effect mitigation. Modernisation in progress will progressively reduce to 14 receivers (new GPS+GLONASS+GALILEO+BEIDOU hardware, same quality of service). |
| **Key mountpoints** | `VRS32GREC` (VRS, RTCM 3.2, GPS+GLO+GAL+BDS) · `IMAX32GREC` (iMAX) · `NEAR32GREC` (nearest). Naming suffix: G=GPS, GR=+GLO, GRE=+GAL, GREC=+BDS. |
| **tariff** | Free for positioning (SURVEY, GIS); user pays only mobile-data. Auto-guidage (machine-guidance) tier paid since 2013-01-01, billed via commercial resellers (no public WALCORS price list; routed through Leica reseller channel). VAT not stated. Observed 2026-05-15 on `gnss.wallonie.be/walcors/acces-au-reseau/acces-au-reseau-4.html`. |
| **hobbyist_eligibility** | Yes — registration form has three user categories (SURVEY, GIS, GUIDAGE); SURVEY/GIS are free and accept individuals. 5 MB/hr per-user data cap. |
| **legal_residency_required** | Unclear / **geographic restriction in effect**: software polygon limits delivery of corrections to Belgian territory ("L'accès n'est pas autorisé en dehors du territoire belge" — *not authorised outside Belgian territory* — except SURVEY-category surveyors who may connect from anywhere in Belgium since 2017-09). No explicit residency requirement, but corrections will not be served outside Belgium. |
| **last_confirmed_alive** | `gnss.wallonie.be:8081` timed out (15s) from this sandbox 2026-05-15 — expected due to geographic firewall. Web portal `gnss.wallonie.be` is reachable and active (operator status page updated 2026-05-14 announcing 2026-05-13 WERB outage and 2026-05-18..2026-06-04 maintenance windows for GHIS/ONHA/FLOR/OSTI/CHAR/MAFA/TILM). Live service-monitoring activity from operator is the strongest evidence of an active caster despite external-IP block. |
| **datum_epoch** | Omitted — no citable per-network declaration. (See FLEPOS note re: BEREF2002.) |

Contact: `gnss@spw.wallonie.be` · administration +32 81 71 59 22 · technical helpdesk +32 2 209 07 08 · 24/7 emergency +32 81 71 59 30. Coordinates for stations VITH (2025-07-11), MARI and OLLN (2025-11-09) were adjusted as part of the modernisation programme; users with stored base coordinates must refresh.

---

### GPSBru / AGN — Brussels Capital Region (NGI / IGN)

| Field | Value |
|---|---|
| **Operator** | Nationaal Geografisch Instituut / Institut Géographique National (NGI/IGN) — Belgian federal mapping agency |
| **landing_url** | `https://agn.ngi.be/NL/NL1.jsp` (NL) · `https://agn.ngi.be/FR/FR1.jsp` (FR) — operator-owned AGN service page describing GPSBru/UKKE. |
| **access_url** | `https://agn.ngi.be/NL/NL1-2.jsp` — NTRIP datastreams + registration request page; describes the five streams and the "log in must be requested after registration" path. |
| **host:port** | Issued only after AGN login is approved; not published on the public AGN site. Public published port is 2101 (IANA NTRIP default) on `agn.ngi.be` but not reachable from external IP without credentials. |
| **VRS** | No — single-base corrections from station UKKE (Uccle/Ukkel — NGI Observatory campus). |
| **num_stations** | 1 (UKKE). Equipment: Septentrio PolarX5 receiver + Sepchoke_MC SPKE antenna (installed 2019-01-11; coordinates valid from 2019-01-03). |
| **Key mountpoints** | `UKKE_GNSS_30` (RTCM 3.0, GPS+GLONASS) — the modern dual-constellation stream · `UKKEL_21` (RTCM 2.1, GPS-only) · `UKKEL_23` (RTCM 2.3, GPS-only) · `DGPS_GPS_RTCM2.0` (DGPS) · `DGPS_GPS+GLONASS_RTCM3.0` (DGNSS) |
| **tariff** | Free; user bears only communication costs. No VAT mentioned (no fee charged). Observed 2026-05-15 on `agn.ngi.be/NL/NL1-2.jsp`. |
| **hobbyist_eligibility** | Yes — registration form on `agn.ngi.be` requires personal contact details + GNSS receiver brand/model + GSM number; no stated professional restriction. NGI describes audience as "landmeters en topografen" (surveyors and cartographers) but does not exclude private requesters. |
| **legal_residency_required** | No restriction stated. |
| **last_confirmed_alive** | `agn.ngi.be:2101` timed out (15s) from this sandbox 2026-05-15 (probable IP/firewall restriction — port is closed to unauthenticated external probes). Web portal `agn.ngi.be` reachable; service description and registration entry both observed live 2026-05-15. ROB EUREF caster (see below) is operated by NGI's sister institution and demonstrates Belgian federal-government NTRIP infrastructure is active. |
| **datum_epoch** | Omitted at network level. (UKKE station coordinates published in ETRS89 geographic / geocentric, Lambert72 and Lambert08 on `agn.ngi.be/NL/NL1-1.jsp`, but no NTRIP-stream-level epoch declaration.) |

**RTK range:** Corrections usable within ~20 km of UKKE (Brussels metro area). DGPS streams cover all of Belgium. Modern `UKKE_GNSS_30` stream is dual-constellation (GPS+GLO) for improved urban sky coverage.

**investigate:** the actual public NTRIP host:port issued post-registration — not visible on the public AGN pages.

---

## Hobbyist Path

- **Flanders:** FLEPOS is **off-limits to private individuals** (registration form rejects "particulieren"; KBO/foreign-org-equivalent required). Hobbyists in Flanders should fall back to Centipede / rtk2go bases (see below) or a personal base.
- **Wallonia:** WALCORS SURVEY or GIS category, free, individual registration accepted. Corrections only delivered within Belgian territory.
- **Brussels:** GPSBru/AGN — free, single-base RTK within ~20 km of Ukkel; individual registration accepted.

---

## Volunteer / Community Backstop

Belgium has dense volunteer-base coverage that complements (and partially substitutes for) the government networks — important for hobbyists locked out of FLEPOS.

- **Centipede-RTK (17 BEL nodes confirmed in `data/stations.json` 2026-05-15):** `5640`, `AHOA`, `AIDE`, `ALEX`, `BIST`, `COCO`, `CRA1`, `DEBEN`, `DEPO`, `FLEN`, `HAYE`, `JFDE`, `KUBA`, `LEMA`, `LEON`, `NLER`, `STAVE`. Clustered in Wallonia and the Brussels–Antwerp corridor. Access: `caster.centipede.fr:2101`, no signup.
- **rtk2go (3 BEL volunteer bases):** `ROOS1` (50.84°N, 4.86°E, central Belgium), `Stuer` (51.19°N, 4.25°E, Antwerp area), `BELHAS01` (50.92°N, 5.35°E, eastern Belgium / Limburg). Access: `rtk2go.com:2101`, no signup.

For a Brussels-centred user (50.85°N, 4.35°E), within 100 km there are 4 rtk2go bases, 33 Centipede nodes (incl. 18 in BE, plus FR/NL cross-border) — ample redundancy.

---

## EUREF / Scientific Relay

The Royal Observatory of Belgium (ROB) operates the EUREF NTRIP caster at `www.euref-ip.be:2101` (RTK2GO `ROBcaster`). Sourcetable returned 200 OK from this sandbox 2026-05-15 (`CAS;www.euref-ip.be;2101;ROBcaster;ROB;0;BEL;50.48;4.21;...`). Carries EPN station streams primarily for scientific post-processing; not intended as a rover RTK service. Mirror with BKG (Germany) and ASI (Italy).

---

## Pipeline notes

- `docs/networks.md` FLEPOS entry presently states `**hobbyist_eligibility**: yes` ("ArduSimple notes 'professional organizations' preferred but individual registration confirmed possible"). This is **wrong**. Operator-side evidence (Digitaal Vlaanderen registration form + product page) and ArduSimple's actual wording both confirm hobbyists CANNOT register. PIPELINE NOTE: networks.md `flepos` should be updated to `hobbyist_eligibility: no` and `pipeline-access: registration` may want a stronger flag (e.g. `professional-only`).
- WALCORS station count in `networks.md` reads "0 (22 Wallonia + 13 cross-border …)" — current operator confirms 23 active, decreasing to 14 under modernisation. PIPELINE NOTE: refresh after next station decommissioning batch.
- FLEPOS `landing_url` in `networks.md` (`https://overheid.vlaanderen.be/en/producten-diensten/centimetre-accurate-positioning-flepos`) now 302-redirects to `vlaanderen.be/intern`. PIPELINE NOTE: update to `https://www.vlaanderen.be/digitaal-vlaanderen/onze-diensten-en-platformen/flepos-centimeternauwkeurige-positiebepaling`.
- `country_markers.json` FLEPOS marker description should clarify hobbyists are not eligible (currently silent on this).

---

## Sources Consulted (probes 2026-05-15)

**FLEPOS:**
- `https://www.vlaanderen.be/digitaal-vlaanderen/onze-diensten-en-platformen/flepos-centimeternauwkeurige-positiebepaling` — 200 OK; operator service description (NEW landing).
- `https://www.vlaanderen.be/digitaal-vlaanderen/onze-diensten-en-platformen/flepos-centimeternauwkeurige-positiebepaling/registratie` — 200 OK; registration walk-through.
- `https://dynamicforms.crmiv.vlaanderen.be/dynamicforms/flepos-registratie` — 200 OK; registration form; states *"Dit online registratieformulier is uitsluitend bedoeld voor professionele organisaties."*
- `https://metadata.vlaanderen.be/srv/api/records/c52869d5-446b-468c-8e73-73d53732105e` — 200 OK; metadata record confirms free-of-charge + professional-only + KBO requirement.
- `https://flepos.vlaanderen.be/` — 200 OK; login gateway (no service description).
- `https://overheid.vlaanderen.be/en/producten-diensten/centimetre-accurate-positioning-flepos` — 302 redirect to `vlaanderen.be/intern` (broken for visitors); was previously the landing.
- `https://overheid.vlaanderen.be/Flepos-NTRIP` — 302 redirect to `vlaanderen.be/intern`.
- Live sourcetable: `curl http://flepos.vlaanderen.be:2101/` — SOURCETABLE 200 OK; STR rows captured.

**WALCORS:**
- `https://gnss.wallonie.be/walcors.html` — 200 OK; operator landing.
- `https://gnss.wallonie.be/walcors/reseau-walcors.html` — 200 OK; older static text lists "22 stations + 13 cross-border" (page predates modernisation). Current count (23, transitioning to 14) is sourced from actualite.html and foire-aux-questions.html below.
- `https://gnss.wallonie.be/walcors/actualite.html` — 200 OK; modernisation news, station count 23→14, latest update 2025-11-09 (MARI/OLLN coordinate change).
- `https://gnss.wallonie.be/walcors/etat-du-reseau-walcors.html` — 200 OK; operator status page, last update 2026-05-14 (confirms active operations).
- `https://gnss.wallonie.be/walcors/foire-aux-questions.html` — 200 OK; FAQ ("Les 23 antennes du réseau Walcors sont situées exclusivement en Wallonie").
- `https://gnss.wallonie.be/walcors/acces-au-reseau/acces-au-reseau-1.html` — 200 OK; access description.
- `https://gnss.wallonie.be/walcors/acces-au-reseau/acces-au-reseau-4.html` — 200 OK; cost page (free for positioning; auto-guidance paid since 2013-01-01).
- `https://gnss.wallonie.be/walcors/produits-delivres/survey.html` — 200 OK; product taxonomy (G/GR/GRE/GREC suffixes).
- `https://www.wallonie.be/fr/demarches/acceder-au-reseau-permanent-de-stations-gnss-de-reference-walcors` — 200 OK; SPW démarche access page.
- Live port probe: `curl http://gnss.wallonie.be:8081/` — timeout 15s from external IP (expected; firewall to Belgian territory). Operator-side status page proves caster is live (active maintenance window announcements through 2026-06-04).

**GPSBru / AGN:**
- `https://agn.ngi.be/NL/NL1.jsp` — 200 OK; operator landing (NL).
- `https://agn.ngi.be/FR/FR1.jsp` — 200 OK; operator landing (FR).
- `https://agn.ngi.be/NL/NL1-1.jsp` — 200 OK; UKKE station coordinates (ETRS89 geographic, geocentric, Lambert72/Lambert08).
- `https://agn.ngi.be/NL/NL1-2.jsp` — 200 OK; NTRIP streams + registration request.
- Live port probe: `curl http://agn.ngi.be:2101/` — timeout 15s from external IP (port not open to unauthenticated probes; access by request only).

**EUREF / cross-check:**
- `curl http://www.euref-ip.be:2101/` — SOURCETABLE 200 OK; ROBcaster (Royal Observatory of Belgium) live 2026-05-15.

**Third-party / corroboration:**
- `https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-belgium/` — 200 OK; corroborates FLEPOS "available only to professional organizations".

**Local data probes:**
- `py scripts/stations_by_country.py BEL` — 3 rtk2go + 17 Centipede BEL stations enumerated 2026-05-15.
- `py scripts/stations_by_radius.py 50.85 4.35 100` — 4 rtk2go + 33 Centipede stations within 100 km of Brussels.
