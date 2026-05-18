# Germany [DE] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (deep verification 2026-05-07, URL re-sweep 2026-05-17)

## Status: YES — extensive public NTRIP RTK coverage; primary provider is the 16-state SAPOS network; most Bundesländer now free; some remain paid

---

## Per-Bundesland SAPOS Summary Table

All casters confirmed live (SOURCETABLE 200 OK) on 2026-05-07 via curl probe unless noted; re-spot-check of ZSS national `www.sapos-ntrip.de:2101` + Thüringen `www.sapos-th-ntrip.de:2101` + GeoNord `www.sapos.geonord.de:2101` succeeded 2026-05-12. Port 2101 throughout. VRS product naming follows AdV convention: `VRS_3_Xg_XX` where X = constellation count, g = letter (2G=GPS+GLO, 3G=+GAL, 4G=+BDS), XX = state code.

**Datum anchor (applies to every SAPOS row below):** all 16 state casters + ZSS + GEPOS unified on **ETRS89/DREF91 R2025** (ITRF2020/IGb20-anchored, 2021 GNSS campaign) bundesweit 01.07.2025. Per-state `datum_epoch` declaration deferred to this anchor to avoid 16× duplication. AdV authority page: `https://www.adv-online.de/AdV-Produkte/Integrierter-geodaetischer-Raumbezug/Transformationsparameter/ITRF2020-IGb20-ETRS89-DREF91-R2025/`. Switchover details in Context Notes / Datum section.

| State | Code | Operator | NTRIP host | landing_url | access_url | Tariff | VRS product(s) | num_stations | hobbyist_eligible | residency_req | last_confirmed_alive |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Baden-Württemberg | BW | LGL BW | `www.sapos-bw-ntrip.de:2101` | https://www.lgl-bw.de/unsere-themen/Geoinformation/Geodaetischer-Raumbezug/Satellitenpositionierungsdienst/ | https://www.lgl-bw.de/unsere-themen/Geoinformation/Geodaetischer-Raumbezug/Satellitenpositionierungsdienst/Registrierungsformular/index.html | Data free ("Open SAPOS®, vollständig gebührenfrei"); €150 incl. USt one-time admin/credential fee retained per HEPS Zugangskennung; GPPS data free | VRS_3_2G_BW · VRS_3_3G_BW · VRS_3_4G_BW | unknown (LGL does not publish a station count on the public page) | yes | unclear | 2026-05-07 |
| Bayern | BY | LDBV | `www.sapos-by-ntrip.de:2101` | https://sapos.bayern.de/ | https://sapos.bayern.de/download.php?file=SAPOS-Nachrichten-2024_01.pdf | €20/yr/account (incl. HEPS + GPPS; flat rate since 01.06.2024; no per-use charges; excl. VAT) | VRS_3_2G_BY · VRS_3_3G_BY · VRS_3_4G_BY | ~50 (LDBV publishes "rund 50 Referenzstationen" on sapos.bayern.de) | yes | unclear | 2026-05-07 |
| Berlin | BE | SenStadt Berlin | `www.sapos-be-ntrip.de:2101` | https://www.berlin.de/sen/sbw/stadtdaten/geoportal/landesvermessung/raumbezug/sapos/ | https://www.berlin.de/sen/sbw/stadtdaten/geoportal/landesvermessung/raumbezug/sapos/ | Free | VRS_3_2G_BE · VRS_3_3G_BE · VRS_3_4G_BE | unknown (Berlin uses neighbouring BB+ST stations; no Berlin-only count published) | yes | unclear | 2026-05-07 |
| Brandenburg | BB | LGB (Potsdam) | `www.sapos-bb-ntrip.de:2101` | https://geobasis-bb.de/lgb/de/geodaten/raumbezug-sapos/ | https://geobasis-bb.de/lgb/de/geodaten/raumbezug-sapos/ | Free (since 2020) | VRS_3_2G_BB · VRS_3_3G_BB · VRS_3_4G_BB | unknown (LGB does not publish a count on the public page) | yes | unclear | 2026-05-07 |
| Bremen | HB | LGLN (shared with NI) | `www.openservice-sapos.niedersachsen.de:2101` or `www.sapos-ni-ntrip.de:2101` | https://www.lgln.niedersachsen.de/startseite/online_angebote_amp_services/webdienste/sapos/sapos-r-ab-oktober-2019-gebuhrenfrei-nutzen-179127.html | https://www.lgln.niedersachsen.de/startseite/online_angebote_amp_services/webdienste/sapos/sapos-r-ab-oktober-2019-gebuhrenfrei-nutzen-179127.html | Free | VRS_3_2G_NI · VRS_3_3G_NI · VRS_3_4G_NI | shared with NI (no Bremen-only stations) | yes | unclear | 2026-05-07 |
| Hamburg | HH | LGV Hamburg (SAPOS GeoNord) | `www.sapos.geonord.de:2101` | https://sapos.geonord.de/ | https://sapos.geonord.de/dienste/echtzeit-positionierungs-service-open-data | Free (Hamburg data permanently free; Open Data registration-free service via `sapos.geonord-od.de:2101` user=gast/pass=gast) | VRS_3_2G_HH-SH · VRS_3_4G_HH-SH | shared with SH via GeoNord (no HH-only count) | yes | unclear | 2026-05-07 |
| Hessen | HE | HVBG | `www.sapos-he-ntrip.de:2101` | https://hvbg.hessen.de/landesvermessung/geodaetischer-raumbezug/saposr | https://hvbg.hessen.de/landesvermessung/geodaetischer-raumbezug/saposr | Free (since 01.01.2019) | VRS_3_2G_HE · VRS_3_4G_HE · VRS_3_2G_HE_GK · VRS_3_4G_HE_GK | unknown (HVBG does not publish a count on the public page) | yes | unclear | 2026-05-07 |
| Mecklenburg-Vorpommern | MV | LAiV MV | `www.sapos-mv-ntrip.de:2101` | https://www.laiv-mv.de/Geoinformation/Raumbezug/Satellitenpositionierungsdienste/ | https://www.laiv-mv.de/Geoinformation/Raumbezug/Satellitenpositionierungsdienste/ | Free (since 01.01.2024); one-time €100 admin fee per end-user at registration | openrtk_mv · VRS_3_2G_MV · VRS_3_4G_MV · VRS_3_GE_MV | unknown (LAiV does not publish a count on the public page) | yes ("für Jedermann") | unclear | 2026-05-07 |
| Niedersachsen | NI | LGLN | `www.openservice-sapos.niedersachsen.de:2101` or `www.sapos-ni-ntrip.de:2101` | https://www.lgln.niedersachsen.de/startseite/online_angebote_amp_services/webdienste/sapos/sapos-r-ab-oktober-2019-gebuhrenfrei-nutzen-179127.html | https://www.lgln.niedersachsen.de/startseite/online_angebote_amp_services/webdienste/sapos/sapos-r-ab-oktober-2019-gebuhrenfrei-nutzen-179127.html | Free (permanently, since Oct 2019) | VRS_3_2G_NI · VRS_3_3G_NI · VRS_3_4G_NI | unknown (LGLN does not publish a count on the public page; includes Bremen) | yes | unclear | 2026-05-07 |
| Nordrhein-Westfalen | NW | Geobasis NRW / BezReg Köln | `www.sapos-nw-ntrip.de:2101` | https://www.bezreg-koeln.nrw.de/geobasis-nrw/produkte-und-dienste/raumbezug/satellitenpositionierungsdienst-saposr | https://www.bezreg-koeln.nrw.de/geobasis-nrw/produkte-und-dienste/raumbezug/satellitenpositionierungsdienst-sapos/sapos-heps | Free | VRS_3_2G_NW · VRS_3_3G_NW · VRS_3_4G_NW · FKP_3_2G_NW · MAC_3_2G_NW · EPS_NW-VRS | ~37 (Geobasis NRW publishes "rund 37 Referenzstationen"; figure also visible in sourcetable CAS entries) | yes | unclear | 2026-05-07 |
| Rheinland-Pfalz | RP | LVermGeo RLP | `www.sapos-ntrip.rlp.de:2101` (IP 83.243.48.22) | https://lvermgeo.rlp.de/produktinformationen/vermessungstechnischer-raumbezug/saposr-dienste | https://lvermgeo.rlp.de/produktinformationen/vermessungstechnischer-raumbezug/saposr-dienste/so-gehts-anwendung-faqs | Paid Pauschalgebühr/year: HEPS €120/account · GPPS €120/account · EPS €70/account · R-HEPS €150 per agricultural Betrieb (not per credential); one-time Einrichtungsgebühr €100 on HEPS/GPPS new registrations since 03.06.2024 (EPS + R-HEPS exempt); cancellation only effective 31.12.; VAT not stated on product page | VRS_3_2G_RP · VRS_3_3G_RP · VRS_3_4G_RP · VRS_3_GE_RP · MAC_3_2G_RP · FKP_3_2G_RP | unknown (LVermGeo RLP does not publish a count on the product page) | yes | unclear | 2026-05-07 |
| Saarland | SL | LVGL Saarbrücken | `www.sapos-sl-ntrip.de:2101` | https://www.saarland.de/lvgl/DE/themen-aufgaben/themen/grundlagen/sapos/heps/heps.html | https://www.saarland.de/lvgl/DE/themen-aufgaben/themen/grundlagen/sapos/heps/heps.html | Free (registration required) | LW_HEPS_SL (VRS 4G) | unknown (LVGL Saarland does not publish a count; Saarland is the smallest flächenstaat) | yes | unclear | 2026-05-07 |
| Sachsen | SN | GeoSN | `www.ntrip.sachsen.de:2101` | https://www.landesvermessung.sachsen.de/sapos-sachsen-7213.html | https://www.landesvermessung.sachsen.de/sapos-sachsen-7213.html | Free (since Open Data rollout 2019; costs "fully eliminated") | VRS_3_2G_SN · VRS_3_4G_SN · FKP_3_2G_SN · MAC_3_2G_SN | unknown (GeoSN does not publish a count on the public page) | yes | unclear | 2026-05-07 |
| Sachsen-Anhalt | ST | LVermGeo ST | `www.sapos-lsa-ntrip.de:2101` (primary; backup `www2.sapos-lsa-ntrip.de:2101`); 4G: `4g.sapos-lsa-ntrip.de:2101` | https://www.lvermgeo.sachsen-anhalt.de/de/gdp-sapos-in-sachsen-anhalt.html | https://www.lvermgeo.sachsen-anhalt.de/de/gdp-heps-korrekturdatenabgabe.html | Free (since 01.07.2023); credentials user=user / pass=user for testing | VRS_3_2G_ST · VRS_3_4G_ST (HEPS); VRS_3_1G_ST / VRS_2_1G_ST / FKP / PRS / MAC variants | unknown (LVermGeo ST does not publish a count on the public page) | yes | unclear | 2026-05-07 |
| Schleswig-Holstein | SH | LVermGeo SH (SAPOS GeoNord) | `www.sapos.geonord.de:2101` | https://sapos.geonord.de/ | https://sapos.geonord.de/dienste/heps | SH HEPS: €0.10/min (min. €10/month when used); R-HEPS SH (agri): €150/device/yr; Open Data service (registration-free): `sapos.geonord-od.de:2101` user=gast/pass=gast | VRS_3_2G_HH-SH · VRS_3_4G_HH-SH; R-HEPS SH via `www.sapossh.de:2101` | shared with HH via GeoNord (no SH-only count published) | yes | unclear | 2026-05-07 |
| Thüringen | TH | TLBG | `www.sapos-th-ntrip.de:2101` (IP 195.191.15.131) | https://sapos.thueringen.de/dienste_heps.php | https://sapos.thueringen.de/price.php | Free (since 01.01.2017; "all data and positioning services free"; guest login: Gast/Gast) | VRS_3_2G_TH · VRS_3_4G_TH · VRS_3_2G_TH_PD · VRS_3_4G_TH_PD | unknown (TLBG does not publish a count on the public service page) | yes | unclear | 2026-05-07 |

**`access_url` selection note for BY:** Bayern's `register.php` is a bare registration form (no service description); the `access_url` instead points to the operator-published "SAPOS-Nachrichten 2024_01" newsletter PDF describing the €20 flat-rate model effective 01.06.2024 — the substantive access/tariff doc.

---

## National / Aggregator NTRIP Services

### ZSS — Zentrale Stelle SAPOS (Paid national aggregator)
- **Operator:** Zentrale Stelle SAPOS (ZSS), operated by LGLN Niedersachsen
- **Host:Port:** `www.sapos-ntrip.de:2101`
- **landing_url:** https://zentrale-stelle-sapos.de/en/
- **access_url:** https://zentrale-stelle-sapos.de/en/fees-registration/
- **Sourcetable confirmed:** 2026-05-07 (SOURCETABLE 200 OK, AdVCasterV1.14, Mar 2026 build)
- **Mountpoints:** VRS_3_4G (SAPOS_VRS_3_4G, nationwide) · VRS_3_2G (SAPOS_VRS_3_2G, nationwide); also acts as routing hub to all 16 state casters (CAS entries)
- **num_stations:** ~270 (national aggregator routes to the AdV-wide network; see Context Notes)
- **datum_epoch:** ETRS89/DREF91 R2025 (ITRF2020/IGb20-anchored, bundesweit switchover 01.07.2025); ZSS Produktinformation 2025-01: https://zentrale-stelle-sapos.de/produktinformation-2025-01/ — also see AdV authority page in datum anchor above
- **Tariff:** HEPS €10/month/user-ID (flat); GPPS €10/month/reference station used; one-time admin fee €100; invoiced semi-annually. **Not the cheapest route** — most individual states are now free; ZSS is intended for cross-state or nationwide commercial users.
- **Registration:** Form to sapos-zentrale-stelle@lgln.niedersachsen.de; credentials sent by email
- **hobbyist_eligibility:** yes (no professional license required, but fee deters casual use)
- **last_confirmed_alive:** 2026-05-12 (curl SOURCETABLE 200 OK on `www.sapos-ntrip.de:2101`)
- **Contact:** +49 511 64609-222

### SAPOS GEPOS / BKG (Federal PPP-RTK broadcast — out of scope for standard NTRIP VRS)
- **Operator:** BKG (Bundesamt für Kartographie und Geodäsie) + ZSS dual-instance
- **Host:Port:** `bkg1.positioning-service.net:2101` (NTRIP); also broadcast via DAB+ (Channel 5C, Subchannel 32)
- **Mountpoint:** BKG-SSRZ-BRST-DE (SSR correction, not standard VRS RTCM)
- **Tariff:** Free, no registration (CC-BY 4.0)
- **Note:** Uses SSRZ SSR correction format; requires conversion tool (Geo++ SSR2OBS) for standard receivers. This is a PPP-RTK/SSR service, **not** standard VRS RTCM for a typical RTK rover. Out of scope for hobbyist NTRIP VRS use but documented here for completeness.

---

## Commercial Alternatives

### HxGN SmartNet Germany (Hexagon / Leica Geosystems) — out of scope
- **Status:** B2B / enterprise commercial network — out of scope per project remit (hobbyist + small-shop focus). Documented only as a name a hobbyist might encounter when searching for German RTK options; not pursued for full per-caster fields (`vrs`, `num_stations`, `last_confirmed_alive` deliberately omitted — host not public, no probe possible).
- **Operator:** Hexagon Geosystems (formerly Leica Geosystems SmartNet); nationwide Germany, also CH/AT/EU.
- **hobbyist_eligibility:** no (enterprise contracts; pricing not published; host disclosed only after contract).
- **Portal:** https://hxgnsmartnet.com/ — provided so a researcher can verify the out-of-scope classification; **do not surface in the public map/guide**.

### Geo++ GNSMART (software infrastructure, not a direct-access caster)
- **Operator:** Geo++ GmbH, Garbsen (Germany)
- **Note:** Geo++ supplies the GNSMART network software that runs several state SAPOS casters (confirmed in sourcetables: NW, NI/HB). Geo++ itself does not operate a public end-user NTRIP caster; they are a B2B infrastructure vendor.
- **Portal:** https://www.geopp.de/

---

## Volunteer Networks

### rtk2go (Germany presence)
- **Count:** 31 DE stations active at data pull (stations.json, 2026-05-06)
- **Access:** `rtk2go.com:2101`; free; no registration required for rover use
- **Relevance:** Small presence compared to the 270-station SAPOS network; useful for specific localities or testing without SAPOS registration; distribution across Germany is uneven

### Centipede (Germany presence)
- **Count:** 3 DE stations (country=DEU in stations.json, 2026-05-06)
- **Access:** `caster.centipede.fr:2101`; free
- **Relevance:** Negligible; Centipede is primarily a French network with very limited reach into Germany

---

## Context Notes

### SAPOS Network Overview
SAPOS (Satellitenpositionierungsdienst der deutschen Landesvermessung) is coordinated by the AdV (Arbeitsgemeinschaft der Vermessungsverwaltungen der Länder). It consists of approximately 270 GNSS reference stations distributed across 16 Bundesländer. Each state operates its own caster independently. All casters support RTCM 3.x and VRS positioning; multi-constellation (4G = GPS+GLO+GAL+BDS) is standard on modern mountpoints.

**Open Data wave:** Germany has progressively liberalised SAPOS access:
- **Thüringen:** Free since 01.01.2017 (first mover)
- **Hamburg:** Free since 01.01.2022
- **Niedersachsen + Bremen:** Free since Oct 2019
- **Hessen:** Free since 01.01.2019
- **Berlin, Brandenburg, NRW, Sachsen, Saarland:** Free (exact dates not found in sources; confirmed free as of 2024–2025)
- **Sachsen-Anhalt:** Free since 01.07.2023
- **Mecklenburg-Vorpommern:** Free since 01.01.2024 (one-time €100 admin fee retained)
- **Schleswig-Holstein:** Paid-per-minute (HEPS) + free Open Data tier (registration-free, since April 2023)
- **Baden-Württemberg:** Free (data cost zero; one-time €150 admin fee for credential issuance)
- **Bayern:** €20/yr/account (significantly reduced from previous per-minute billing; new model since 01.06.2024)
- **Rheinland-Pfalz:** Paid (€120/yr/credential for HEPS/GPPS); most restrictive commercial model remaining

**hobbyist eligibility:** No Bundesland found to explicitly require a professional surveying licence or business registration. Registration forms exist but appear open to individuals. The term "Nutzer" (user) is used generically. No legal_residency_required clause in operator T&Cs. ArduSimple SAPOS-access guide (re-verified 2026-05-17): DE-resident applicants get credentials before invoice; **non-DE residents "must pay invoice in advance and only receive access data after receipt of payment"** — operational hurdle but not a residency ban. Marked as "unclear" for residency throughout because (a) no operator decree publishes a ban, and (b) policy varies per Bundesland office handling foreign applications.

**VRS product naming convention:** All states use AdV-standard mountpoint naming except GeoNord (HH+SH shared caster `VRS_3_XG_HH-SH`), Sachsen-Anhalt (uses `VRS_3_XG_ST`, `FKP_3_XG_ST`, `PRS_3_XG_ST`), and Thüringen (appends `_PD` for Pulsdorf datum variant).

**Sachsen-Anhalt curiosity:** The HEPS page prominently lists credentials user=`user` / pass=`user` as "standard NTRIP access" — effectively no-authentication for the primary host.

**Thüringen Open Data:** Guest login `Gast`/`Gast` on sapos-th-ntrip.de:2101 provides anonymous access; geographic restriction to Thüringen borders enforced by server-side NMEA GGA position check.

**SAPOS GeoNord (HH + SH):** Unique joint operation by LGV Hamburg and LVermGeo Schleswig-Holstein. One shared caster serves both states. Hamburg is always free; SH charges per-minute for HEPS (€0.10/min, min €10/month when active) but offers a free Open Data service (`sapos.geonord-od.de:2101`, user=gast/pass=gast, mountpoint RTCM4G, CC-BY 4.0) since April 2023.

**AdV-GR 4.0 (June 2024):** New nationwide fee directive replaced usage-based billing with flat-rate per-credential models, substantially reducing costs for remaining paid states. Rheinland-Pfalz remains the outlier with the highest cost structure.

**Bayern price model (since 01.06.2024):** Confirmed €20/year flat rate per customer account, no VAT, no monthly base fee, annual billing, 1-year contract, 1-month cancellation notice. Includes both HEPS (real-time) and GPPS (post-processing); also extended to the agricultural Landwirtschaftsfahrzeug-Positionierungs-Service (LFPS) on the same date. Source: bayern.de press release "Füracker: vereinfachtes Preismodell für den Satellitenpositionierungsdienst SAPOS — Neuer Flatrate-Tarif für SAPOS-Kunden ab 1. Juni 2024 — Nur 20 Euro jährlich pro Kundenkonto" (re-verified 2026-05-12).

**Rheinland-Pfalz price model (since 03.06.2024):** Confirmed via LVermGeo RLP product page (re-verified 2026-05-12): HEPS €120/yr/credential, GPPS €120/yr/credential, EPS €70/yr/credential, R-HEPS (agriculture) €150/yr; one-time €100 setup fee on NEW HEPS/GPPS registrations from 03.06.2024 onwards (EPS and R-HEPS exempt from setup fee). VAT inclusivity not annotated on the public product page.

**NRW free since 2018:** Bezirksregierung Köln / Geobasis NRW confirms (2026-05-12 search) "Die SAPOS HEPS- und GPPS-Dienste können seit dem 30.03.2018 in Nordrhein-Westfalen kostenfrei genutzt werden" — i.e., free since 30 March 2018. Registration with Geobasis NRW is still required for HEPS; OpenGeoData NRW serves the RINEX archive (15s) anonymously.

**Datum:** All SAPOS services use ETRS89/DREF91 horizontal reference + DHHN2016 height. AdV declared the new realisation **ETRS89/DREF91 R2025** (anchored on ITRF2020/IGb20, derived from 2021 GNSS campaign on stable GGP network points) — bundesweit switchover **01.07.2025** during the window 30.06.2025 17:00 → 01.07.2025 08:00 MESZ per ZSS Produktinformation 2025-01 (states may deviate within that window; GeoNord HH+SH executed it 01.07.2025 01:50–02:10). Coordinate jump vs R2016 ≤1 cm horizontal and ≤a few cm vertical — within service accuracy, no practical impact on hobbyist RTK. AdV publishes an NTv2 grid (R2016 → R2025) for legacy data; transformation cannot recover precision beyond the original observation. Operator-declaration source: AdV transformation-parameter authority page `https://www.adv-online.de/AdV-Produkte/Integrierter-geodaetischer-Raumbezug/Transformationsparameter/ITRF2020-IGb20-ETRS89-DREF91-R2025/`.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SAPOS GPPS** (each Bundesland) | Via state portal (GPPS-PrO online calculation or RINEX download) | Free in most states; RP charges €120/yr |
| **BKG EUREF-IP / CORS-DE** — federal CORS stations | https://igs.bkg.bund.de/ | Free (registration) |
| **GeoSN SAPOS RINEX** (Sachsen) | http://www.landesvermessung.sachsen.de/sapos/ | Free |
| **LVermGeo ST RINEX** (Sachsen-Anhalt) | https://www.lvermgeo.sachsen-anhalt.de/de/gdp-sapos-in-sachsen-anhalt.html | Free |

---

## Sources Consulted
- ZSS Zentrale Stelle SAPOS: https://zentrale-stelle-sapos.de/en/
- ZSS fees & registration: https://zentrale-stelle-sapos.de/en/fees-registration/
- ZSS AdV-GR 4.0 announcement (June 2024): https://zentrale-stelle-sapos.de/info-advgr4/
- ZSS product info 2023-03 (MV free from 01.01.2024): https://zentrale-stelle-sapos.de/produktinformation-2023-03/
- sapos.de national portal: https://sapos.de/
- ArduSimple DE NTRIP guide: https://www.ardusimple.de/rtk-correction-services-and-ntrip-casters-in-germany/
- ArduSimple SAPOS access guide: https://www.ardusimple.de/how-to-get-access-to-sapos-ntrip-service-in-germany/
- SAPOS BW (LGL): https://gpps-web.sapos-bw.de/faq.php · https://www.lgl-bw.de/unsere-themen/Geoinformation/Geodaetischer-Raumbezug/Satellitenpositionierungsdienst/
- SAPOS BY (LDBV): https://sapos.bayern.de/ · https://sapos.bayern.de/register.php · Bayern press release (€20 flat June 2024): https://www.bayern.de/fueracker-vereinfachtes-preismodell-fuer-den-satellitenpositionierungsdienst-sapos-neuer-flatrate-tarif-fuer-sapos-kunden-ab-1-juni-2024-nur-20-euro-jaehrlich-pro-kundenkonto/
- SAPOS BE (Berlin): https://www.berlin.de/sen/sbw/stadtdaten/geoportal/landesvermessung/raumbezug/sapos/
- SAPOS BB (Brandenburg): https://geobasis-bb.de/lgb/de/geodaten/raumbezug-sapos/
- SAPOS HH+SH (GeoNord): https://sapos.geonord.de/ · https://sapos.geonord.de/dienste/echtzeit-positionierungs-service-open-data · https://sapos.geonord.de/dienste/heps · https://sapos.geonord.de/dienste/r-heps-sh · https://sapos.geonord.de/agb
- SAPOS HE (HVBG): https://hvbg.hessen.de/landesvermessung/geodaetischer-raumbezug/saposr
- SAPOS MV (LAiV): https://www.laiv-mv.de/Geoinformation/Raumbezug/Satellitenpositionierungsdienste/
- SAPOS NI+HB (LGLN): https://www.lgln.niedersachsen.de/startseite/online_angebote_amp_services/webdienste/sapos/sapos-r-ab-oktober-2019-gebuhrenfrei-nutzen-179127.html
- SAPOS NW (Geobasis NRW): https://www.bezreg-koeln.nrw.de/geobasis-nrw/produkte-und-dienste/raumbezug/satellitenpositionierungsdienst-saposr · IP change notice: https://www.ili-gis.com/post-3-2/
- SAPOS RP (LVermGeo RLP): https://lvermgeo.rlp.de/produktinformationen/vermessungstechnischer-raumbezug/saposr-dienste · https://lvermgeo.rlp.de/produktinformationen/vermessungstechnischer-raumbezug/saposr-dienste/so-gehts-anwendung-faqs
- SAPOS SL (LVGL Saarland): https://www.saarland.de/lvgl/DE/themen-aufgaben/themen/grundlagen/sapos/heps/heps.html
- SAPOS SN (GeoSN): https://www.landesvermessung.sachsen.de/sapos-sachsen-7213.html · https://www.gis.gmbh/agrar/open-data-in-sachsen.html
- SAPOS ST (LVermGeo ST): https://www.lvermgeo.sachsen-anhalt.de/de/gdp-heps-korrekturdatenabgabe.html · https://www.lvermgeo.sachsen-anhalt.de/de/sapos_faq/kosten-ntrip-nutzung.html
- SAPOS TH (TLBG): https://sapos.thueringen.de/dienste_heps.php · https://sapos.thueringen.de/price.php
- SAPOS GEPOS/BKG: https://gepos.sapos.de/nutzung/ · https://www.bkg.bund.de/DE/Produkte-und-Dienste/Positionierungsdienst/Positionierungsdienst.html
- NTRIP-list.com Europe: https://ntrip-list.com/europe/
- curl probe of `www.sapos-ntrip.de:2101` — SOURCETABLE 200 OK, AdVCasterV1.14 (Mar 2026), confirmed 2026-05-07
- curl probe of `www.sapos-by-ntrip.de:2101` — SOURCETABLE 200 OK, Trimble Ntrip Caster 5.2, confirmed 2026-05-07
- curl probe of `www.sapos-th-ntrip.de:2101` — SOURCETABLE 200 OK, Trimble Ntrip Caster 5.2, confirmed 2026-05-07
- curl probe of `www.sapos-nw-ntrip.de:2101` — SOURCETABLE 200 OK, GNSS Spider 7.11.1.109, confirmed 2026-05-07
- curl probe of `www.sapos-mv-ntrip.de:2101` — SOURCETABLE 200 OK, GNSS Spider 7.11.1.109, confirmed 2026-05-07
- curl probe of `www.sapos-bb-ntrip.de:2101` — SOURCETABLE 200 OK, GNSMART_Caster 2.0, confirmed 2026-05-07
- curl probe of `www.sapos-be-ntrip.de:2101` — SOURCETABLE 200 OK, GNSMART_Caster 2.0, confirmed 2026-05-07
- curl probe of `www.ntrip.sachsen.de:2101` — SOURCETABLE 200 OK, Trimble Ntrip Caster 5.1, confirmed 2026-05-07
- curl probe of `www.sapos-lsa-ntrip.de:2101` — SOURCETABLE 200 OK, GNSMART_Caster, confirmed 2026-05-07
- curl probe of `www.sapos-sl-ntrip.de:2101` — SOURCETABLE 200 OK, GNSMART_Caster 2.0, confirmed 2026-05-07
- curl probe of `www.sapos-ntrip.rlp.de:2101` — SOURCETABLE 200 OK, GNSS Spider 7.10.1.168, confirmed 2026-05-07
- curl probe of `www.sapos-he-ntrip.de:2101` — SOURCETABLE 200 OK, GNSS Spider 7.10.1.168, confirmed 2026-05-07
- curl probe of `www.sapos-bw-ntrip.de:2101` — SOURCETABLE 200 OK, Trimble Ntrip Caster 5.2, confirmed 2026-05-07
- curl probe of `www.sapos-ni-ntrip.de:2101` — SOURCETABLE 200 OK, GNSMART_Caster 2.0, confirmed 2026-05-07
- curl probe of `www.sapos.geonord.de:2101` — SOURCETABLE 200 OK, GNSMART_Caster 2.0, confirmed 2026-05-07
- HxGN SmartNet: https://hxgnsmartnet.com/
- Geo++ GNSMART: https://www.geopp.de/gnsmart/
- stations.json data pull: rtk2go 32 DE stations · centipede 3 DE stations (2026-05 snapshot — `stations_by_country.py DEU`)
- bayern.de Füracker press release (Bayern €20/yr flat-rate): https://www.bayern.de/fueracker-vereinfachtes-preismodell-fuer-den-satellitenpositionierungsdienst-sapos-neuer-flatrate-tarif-fuer-sapos-kunden-ab-1-juni-2024-nur-20-euro-jaehrlich-pro-kundenkonto/ (re-verified 2026-05-12)
- bayern.de SAPOS-Nachrichten 2024_01 (Preismodell-Umstellung): https://sapos.bayern.de/download.php?file=SAPOS-Nachrichten-2024_01.pdf
- LVermGeo RLP SAPOS Preise (re-verified 2026-05-12): HEPS €120/yr · GPPS €120/yr · EPS €70/yr · R-HEPS €150/yr · setup €100 (HEPS/GPPS new registrations from 03.06.2024)
- NRW Geobasis kostenfrei seit 30.03.2018 (re-verified 2026-05-12): https://www.bezreg-koeln.nrw.de/geobasis-nrw/produkte-und-dienste/raumbezug/satellitenpositionierungsdienst-sapos/sapos-heps
- AdV ITRF2020/IGb20 ↔ ETRS89/DREF91 R2025 transformation parameter authority page (re-verified 2026-05-17): https://www.adv-online.de/AdV-Produkte/Integrierter-geodaetischer-Raumbezug/Transformationsparameter/ITRF2020-IGb20-ETRS89-DREF91-R2025/
- ZSS Produktinformation 2025-01 — bundesweiter DREF91 R2025 Umstieg 01.07.2025 (Fenster 30.06. 17:00 → 01.07. 08:00 MESZ): https://zentrale-stelle-sapos.de/produktinformation-2025-01/
- SAPOS GeoNord R2025 switchover notice (HH+SH unavailable 01.07.2025 01:50–02:10): https://sapos.geonord.de/node/27
- LGL BW SAPOS service page — "Open SAPOS®, vollständig gebührenfrei" (data free, admin fee retained, re-verified 2026-05-17): https://www.lgl-bw.de/unsere-themen/Geoinformation/Geodaetischer-Raumbezug/Satellitenpositionierungsdienst/
- SAPOS BW Registrierungsformular — "Verwaltungsentgelt 150 € (inkl. USt) je neue Zugangskennung" (re-verified 2026-05-17): https://www.lgl-bw.de/unsere-themen/Geoinformation/Geodaetischer-Raumbezug/Satellitenpositionierungsdienst/Registrierungsformular/index.html
- ArduSimple SAPOS-access guide — non-DE residents must prepay before access (re-verified 2026-05-17): https://www.ardusimple.com/how-to-get-access-to-sapos-ntrip-service-in-germany/
