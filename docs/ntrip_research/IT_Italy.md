# Italy [IT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-21 (station coordinate tables added for Campania, Puglia, GPS-UMBRIA, Abruzzo+Lazio; pipeline obstruction notes added per-network). Prior versions: 2026-05-17, 2026-05-13, 2026-05-12.

## Status: YES — extensive public free NTRIP RTK infrastructure; no single national free caster; coverage is regional

Italy has no unified national free RTK caster. Instead, 10+ regional/autonomous networks operated at the Regione or Provincia Autonoma level provide free (registration-required) RTK corrections. Several regions (Emilia-Romagna, Marche, Sardegna, Toscana, Basilicata, Calabria, Molise) lack a public regional caster; users there rely on adjacent networks or commercial services. Two commercial nationwide networks (HxGN SmartNet / ItalPOS and NetGEO / TopNET Live) fill gaps.

---

## Per-Region Summary Table

| Region | Network | host:port | Tariff | VRS | Hobbyist | curl result |
|--------|---------|-----------|--------|-----|----------|-------------|
| Valle d'Aosta, Piemonte, Lombardia | SPIN3 GNSS | `158.102.7.10:2101` | Free (registration) | Yes (VRS, iMAX, MAC, NRT) | Yes (no restriction stated) | SOURCETABLE 200 OK (portal reconfirmed 2026-05-17; 39 deployed / 35 operative) |
| Liguria | Rete GNSS Liguria | `81.23.86.70:2101` | Free (registration) | Yes (VRS 2/3, MAC, NEAR, DGPS) | unclear (form-based registration) | SOURCETABLE 200 OK (GNCASTER) |
| Trentino (PA Trento) | TPOS | `194.105.50.232:2101` | Free (registration) | Yes (IMAX, MAX, NRT/VRS) | unclear | SOURCETABLE 200 OK |
| Alto Adige / Südtirol (PA Bolzano) | STPOS | `62.101.0.40:2109` | Free (registration) | Yes (Netz-rete, MAX, NRT) | unclear | SOURCETABLE 200 OK |
| Veneto | Rete GPS Veneto | `147.162.229.53:2101` | Free (email registration) | Yes (MAX3, IMAX, NRT) | unclear (email-only signup) | SOURCETABLE 200 OK (35 stations per operator station-map page) |
| Friuli-Venezia Giulia | Re.M.FVG "A. Marussi" | `gnsscaster.regione.fvg.it:8080` | Free (form registration) | Yes (VRS_RTCM23/31/32, MAC, IMAC) | Yes (form open to anyone) | SOURCETABLE 200 OK 2026-05-12 |
| Friuli-Venezia Giulia | FReDNet (OGS) | `158.110.30.81:2110` | Free (account on frednet.crs.ogs.it) | Yes (VRS, NEAREST, FKP) | Yes (public, private, scientific) | SOURCETABLE 200 OK 2026-05-12 |
| Umbria | GPS-UMBRIA | `gpsumbria.regione.umbria.it:2101` | Free (online form) | Yes (MAC, VRS, Nearest) | unclear | SOURCETABLE 200 OK (GNCASTER) |
| Campania | Rete GNSS Campania | `gps.sit.regione.campania.it:2101` | Free (open credentials) | Yes (1_VRS30, 9_NEAR) | Yes (public credentials) | SOURCETABLE 200 OK (GNCASTER) |
| Puglia | Rete GNSS Puglia | `gps.sit.puglia.it:2101` | Free (registration) | Yes (IMAX3, MAX3) | unclear | SOURCETABLE 200 OK (station count unverified on operator portal) |
| Abruzzo + Lazio | Rete GNSS Abruzzo-Lazio | `gnss-rtk.regione.abruzzo.it:2101` | Free (registration) | Yes (0_RTCM_MSM/VRS, VRS23/30) | Yes (form open to anyone) | timeout from sandbox — 5 consecutive failures (2026-05-07 through 2026-05-21); registration portal HTTP 200; likely IP-restricted |
| Sicilia + S. Calabria | Sicili@NET (INGV Catania) | `193.206.223.39:2101` | Free (email request) | Yes (VRS2/3, RTK, IMAX, MAX, FKP) | Yes ("all users who request it") | SOURCETABLE 200 OK |
| Emilia-Romagna | No public regional network | — | — | — | — | no caster |
| Toscana | No public RTK caster | — | — | — | — | no caster |
| Marche | No public regional network | — | — | — | — | no caster |
| Sardegna | No public regional network | — | — | — | — | no caster |
| Basilicata | No public regional network | — | — | — | — | no caster |
| Calabria (north) | No dedicated public caster | — | — | — | — | partial: Sicili@NET covers southern tip |
| Molise | No public regional network | — | partial via Abruzzo border | — | — | see Abruzzo note |
| **NATIONAL — commercial** | HxGN SmartNet Italy (ItalPOS) | `it.nrtk.eu:2101` | ~€385/yr +IVA (12 mo); ~€1670/yr (60 mo) | Yes (VRS, IMAX, RTK, FKP, MAX) | unclear (professional focus; no explicit ban) | SOURCETABLE 200 OK |
| **NATIONAL — commercial** | NetGEO / TopNET Live (Topcon) | `rtk.topnetlive.com:2101` | €90/mo · €360/yr · €630/2yr · €850/3yr · €1300/5yr +IVA; VAT-ID required | Yes (NET_MSM5, NET_RTCM3, DGNSS) | No (partita IVA required) | SOURCETABLE 200 OK (IQProxy/1.2) |

---

## Detailed Network Notes

### SPIN3 GNSS — Piemonte, Lombardia, Valle d'Aosta
- **landing_url:** https://www.spingnss.it/
- **access_url:** https://www.spingnss.it/i-servizi/ (service catalogue + registration entry; auxiliary 2026-04-01 frame-refresh notice: https://www.spingnss.it/nuovo-inquadramento-rete-spin3-aggiornamento-coordinate-6/)
- **Operator:** Regione Piemonte + Regione Lombardia + Regione Valle d'Aosta (joint, since ~2004); data centre at CSI Piemonte.
- **host:port:** `158.102.7.10:2101` (confirmed SOURCETABLE 200 OK 2026-05-07; portal alive + service-status board green 2026-05-17).
- **num_stations:** 39 deployed (35 operative on 2026-05-17 portal status board; 4 offline); ~30 km inter-station spacing. Roster change: CREO commissioned at Cremona replacing CREM (2026-05-12); CARZ restored 2025-11-27.
- **Products:** VRS (RTCM 3 MSM5), iMAX, MAC/MAX, NRT; confirmed in sourcetable.
- **Tariff:** Free for all professional users; free for registration. No pricing.
- **Registration:** Web form at spingnss.it → email confirmation → username/password (max 16 chars). Confirmed Feb 2026 application update.
- **hobbyist_eligibility:** unclear — described as open to "professional operators, public and private" but no explicit hobbyist exclusion.
- **legal_residency_required:** No.
- **VRS:** Yes.
- **datum_epoch:** ETRF2000-RDN epoch 2008.0 (also published in IGS20). Operator cite: https://www.spingnss.it/nuovo-inquadramento-rete-spin3-aggiornamento-coordinate-6/ — 2026-04-01 announcement "Nuovo inquadramento Rete SPIN3 – Aggiornamento coordinate" documents semestral coordinate recompute within the same frame/epoch, no datum change.
- **Border experiments:** Active data exchange experiments at Liguria and Trentino borders; Liguria and Toscana are NOT part of SPIN3 service area.
- **Contact:** info.gnss@csi.it · +39 011 316 8724.
- **last_confirmed_alive:** 2026-05-17 (operator portal at spingnss.it served live news feed + station-status board; sandbox NTRIP-TCP blocked today, so curl-on-2101 not re-run; 2026-05-07 sourcetable probe remains last successful direct NTRIP fetch).

---

### Rete GNSS Liguria — Liguria
- **landing_url:** https://geoportal.regione.liguria.it/servizi/rete-gnss-liguria/correzioni-in-tempo-reale.html
- **access_url:** https://sportellonline.regione.liguria.it/servizio/PE_0012 (Sportello Cartografico registration form)
- **Operator:** Regione Liguria, Geoportale; uses GNSMART (Geo++) software.
- **host:port:** `81.23.86.70:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07)
- **num_stations:** 10 (7 regional + 3 shared with SPIN3); Ventimiglia to La Spezia.
- **Products:** VRS 2, VRS 3, MAC, NEAR 2, NEAR 3, DGPS (per Liguria RTK portal page).
- **Tariff:** Free; registration via Sportello Cartografico.
- **hobbyist_eligibility:** unclear — form-based; no stated professional requirement found, but the process is a formal regional service request.
- **legal_residency_required:** unclear.
- **VRS:** Yes.
- **datum_epoch:** omitted — no citable per-operator declaration. (Network is RDN-aligned by national framework, but operator portal does not publish a per-network datum/epoch statement.)
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK by IP).

---

### TPOS — Trentino / Provincia Autonoma di Trento
- **landing_url:** https://www.provincia.tn.it/en/Services/TPOS-Trentino-POsitioning-Service
- **access_url:** https://www.tpos.provincia.tn.it/SBC/Account/Register (registration form)
- **Operator:** Servizio Catasto – Ufficio Geodetico, Provincia Autonoma di Trento.
- **host:port:** `194.105.50.232:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07); domain: `tpos.provincia.tn.it` (parameters post-login).
- **num_stations:** 11 covering Trentino; integrates with STPOS (Bolzano), APOS (Austria), SWIPOS (Switzerland) at borders.
- **Products:** IMAX2, MAX3, NRT2, VRS (from sourcetable: Vicina_NRT2, Area_IMAX2, Area_MAX3).
- **Tariff:** Free; registration via access_url.
- **hobbyist_eligibility:** unclear — form-based; no stated professional requirement.
- **legal_residency_required:** unclear.
- **VRS:** Yes.
- **datum_epoch:** omitted — no citable per-operator declaration on TPOS portal.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK, TPOS label in stream headers confirmed).

---

### STPOS — Alto Adige / Südtirol / Provincia Autonoma di Bolzano
- **landing_url:** https://www.provincia.bz.it/costruire-abitare/catasto-librofondiario/catasto/stpos-reti-appoggio-geodetico.asp
- **access_url:** http://www.stpos.it/sbc/Account/Register (registration form)
- **Operator:** Ufficio Catasto, Provincia Autonoma di Bolzano; Leica Spider Business Center.
- **host:port:** `62.101.0.40:2109` (confirmed SOURCETABLE 200 OK, 2026-05-07; note non-standard port 2109). Port 2101 on same IP refused.
- **num_stations:** 10 (Bozen, Bruneck, Corvara, Feldthurns, Helm-M.Elmo, Latsch, Mals, Merano2000, Prettau, Vipiteno).
- **Products:** Nearest3.1, Netz-rete3.1 (RTCM 3), Netz-rete18-19 (RTCM 2), Netz-ReteMAX, Netz-ReteMSM4 (quad-constellation), NRT4 (from sourcetable). VRS/network correction confirmed.
- **Tariff:** Free; registration via access_url.
- **hobbyist_eligibility:** unclear.
- **legal_residency_required:** unclear.
- **VRS:** Yes (network correction mode confirmed in sourcetable).
- **datum_epoch:** omitted — no citable per-operator declaration on STPOS portal.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK on port 2109, STPOS label confirmed).

---

### Rete GPS Veneto — Veneto
- **landing_url:** https://www.regione.veneto.it/web/ambiente-e-territorio/stazioni-gps
- **access_url:** https://retegnssveneto.cisas.unipd.it/Web/index.php (operator portal at CISAS-UniPD; station map at https://retegnssveneto.cisas.unipd.it/Web/page.php?pid=gmap&link=Stazioni_GNSS&chain=6)
- **Operator:** Regione Veneto + Università di Padova (CISAS); software: TopNET (Topcon).
- **host:port:** `147.162.229.53:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07); RINEX portal: retegnssveneto.cisas.unipd.it (that hostname timed out on NTRIP port, but NTRIP IP is live).
- **num_stations:** 35 (operator station-map page at retegnssveneto.cisas.unipd.it lists 35 site codes including AFAL, ASIA, BL01, BOCN, BORC, BTAC, CGIA, CITT, GRDO, LEG1, LEG2, MAVE, MBEL, PAD1, PADO, PIEV, PRTG, PSAL, ROVI, SAPP, SCHI, SDNA, TAMB, TEOL, TGPO, TRVS, VELO, VENI, VICE, VR02 +5 — confirmed 2026-05-17). Some are cross-relayed from neighbouring networks (e.g. AFAL, GRDO also appear on FReDNet/OGS); operator does not separate own-vs-relayed counts on the public page.
- **Products:** MAX3, IMAX, NRT; confirmed via ProTRACK guide.
- **Tariff:** Free; registration by email to retegpsveneto@gmail.com (include name, org, phone, email).
- **hobbyist_eligibility:** unclear — email-only signup, no professional credential check stated, but targeted at professionals.
- **legal_residency_required:** No explicit requirement.
- **VRS:** Yes (network correction confirmed).
- **datum_epoch:** omitted — no citable per-operator declaration on Regione Veneto / CISAS portal.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK on 147.162.229.53:2101).
- Note: Infrastructure update in progress as of 2026 (device replacements at multiple sites); service online.

---

### Re.M.FVG "Antonio Marussi" — Friuli-Venezia Giulia (regional network)
- **landing_url:** https://rem.regione.fvg.it/rem-fvg/servizi/correzioni-differenziali
- **access_url:** https://rem.regione.fvg.it/rem-fvg/info/cenni-storici (network history + station roster; main regional portal entry: https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/conoscere-ambiente-territorio/FOGLIA11/FOGLIA4/)
- **Operator:** Regione Autonoma Friuli-Venezia Giulia; software: Leica GNSS Spider (7.11.1.109 banner observed).
- **host:port:** `gnsscaster.regione.fvg.it:8080` / `193.43.178.173:8080` (SOURCETABLE 200 OK 2026-05-12).
- **Network history (operator-stated, 2026-05-13):** Founded 1999 (Palmanova, Ampezzo, Moggio Udinese). Open to private users since 2005. VRS since 2007. GPS+GLONASS+Galileo since 2012/2019. BEIDOU added 2024–2025 in receiver-refresh; Sappada and Paularo added 2024–2025; Slovenian SIGNAL stations integrated at the border. All consistent with the SOURCETABLE on disk.
- **num_stations:** 14 own physical stations as of 2026-05-13 (Ampezzo, Barcis, Bevazzana, Bovec*, Cervignano, Codroipo, Gorizia, Idrija*, Koper*, MoggioUdinese, Paularo, Pordenone, Sappada, Tarvisio, Trieste, Udine — `*`=Slovenian SIGNAL partner station accessible via the caster). The caster's published sourcetable also exposes 11 OGS/FReDNet mountpoints (`OGS_ACOM`, `OGS_AFAL`, `OGS_MDEA`, `OGS_MPRA`, `OGS_CODR`, `OGS_FUSE`, `OGS_JOAN`, `OGS_NOVE`, `OGS_PAZO`, `OGS_TRIE`, `OGS_UDI1`, `OGS_ZOUF`) — cross-relay of FReDNet, not new physical infrastructure. Border integration also stated with Austrian EPOSA.
- **Products:** VRS_RTCM23, VRS_RTCM31, VRS_RTCM32 (GPS+GLO+GAL+BDS quad-constellation), VRS_CMR, MAC_RTCM31, IMAC_RTCM3, IMAC_RTCM32, SingleBase_RTCM23/31/32, plus DGPS variants per station — confirmed in sourcetable on disk.
- **Tariff:** Free; credentials by online registration form on the Re.M.FVG portal. Per operator: "Access to the real-time service is free, but is regulated through access credentials."
- **hobbyist_eligibility:** Yes — form is open to anyone who applies; no professional, institutional, or commercial-use restriction stated.
- **legal_residency_required:** No.
- **VRS:** Yes (multiple VRS formats including quad-constellation RTCM 3.2).
- **datum_epoch:** ETRS89 / ETRF2000 epoch 2008.0 (RDN aligned). Operator cite: https://rem.regione.fvg.it/rem-fvg/servizi/correzioni-differenziali (service-description page states ETRF2000-RDN alignment).
- **last_confirmed_alive:** 2026-05-12 (SOURCETABLE 200 OK, Leica GNSS Spider/7.11.1.109 confirmed).

---

### FReDNet — Friuli-Venezia Giulia (OGS geodynamic network)
- **landing_url:** https://frednet.crs.ogs.it/en/servizio-rtk/
- **access_url:** https://frednet.crs.ogs.it/en/lista-stazioni/ (full station list + RTK flags; operator overview at https://frednet.crs.ogs.it/en/frednet/)
- **Full name:** FReDNet = Friuli Regional Deformation Network.
- **Operator:** OGS – Istituto Nazionale di Oceanografia e di Geofisica Sperimentale, Centro di Ricerche Sismologiche (CRS), Udine. Operating since June 2002. (Not INGV — the two institutes are distinct; the 2026-05-07 entry's "OGS/INGV" attribution was incorrect.)
- **Partner:** ISPRA contributes a small number of stations; per the operator's `lista-stazioni` page all currently listed stations are OGS-managed. Part of OGS's SMINO (North-East Italy monitoring system) and a node in the EPOS / GLASS CEGNxEPOS gateway.
- **host:port:** `158.110.30.81:2110` (note non-standard port 2110). Listed verbatim on https://frednet.crs.ogs.it/en/servizio-rtk/ as of 2026-05-13.
- **num_stations:** 25 listed; 23 RTK-active per operator station-list page (2026-05-17 re-fetch — one station added since 2026-05-13's 24/22 reading). Active codes 2026-05-17: ACOM, AFAL, CANV, CODR, FUSE, GRDO, JOAN, LOGA, MDEA, MGBU, MPRA, NOVE, PAZO, PMNT, SUSE, TOLS, TRIE, UDI1, UDI2, VALS, VARM, ZOUF (+1 new). LODI and UDIN remain RTK-off. Distributed across Friuli-Venezia Giulia plus Veneto (CANV, SUSE, NOVE, MGBU, AFAL) and one outlier in Lombardia (LODI). Inter-station spacing ~30–50 km; designed for crustal-deformation monitoring along the Adria microplate boundary, not optimised for RTK density.
  - **Dual-source operator mismatch (flag):** the `lista-stazioni` page shows 25 listed / 23 RTK-active, but the overview page `frednet.crs.ogs.it/en/frednet/` still states "currently … counts 22 active permanent GNSS stations". The two operator pages disagree. Station-list page is the more authoritative + recently-updated count; overview-page text appears stale (also matches SMINO page's 22-active figure). Tracked here so downstream pipeline (rtk_inventory.md, markers) stays consistent with the lista-stazioni count.
- **Products:** Single-station (e.g. `OGS_JOAN`), NEAREST (`OGS_NEA`), VRS (`OGS_VRS`), FKP network solution (`OGS_FKP`), DGPS (code). The caster also re-broadcasts a subset of Re.M.FVG/Marussi physical stations under the `RAFVG_*` prefix (e.g. `RAFVG_BARC`) — cross-relay of the two FVG networks.
- **datum_epoch:** ETRF2000 epoch 2008.0 (RDN-aligned). Operator cite: https://frednet.crs.ogs.it/en/servizio-rtk/ (RTK-service page declares ETRF2000 framing).
- **Tariff:** Free for all users — operator describes the service as "freely accessible to public, private and scientific users." No charge for registration, account, or stream.
- **Registration:** Online form at https://frednet.crs.ogs.it/en/servizio-rtk/ (RTK account management).
- **hobbyist_eligibility:** Yes — no professional, institutional, or research-affiliation gate stated; "public, private and scientific users" is the operator's own wording.
- **legal_residency_required:** No (not stated; no national-ID or VAT-ID requirement).
- **VRS:** Yes.
- **Contact:** gnss@ogs.it · Via Treviso 55, 33100 Udine.
- **last_confirmed_alive:** 2026-05-17 (operator station-list page re-fetched, host:port `158.110.30.81:2110` still published, free-for-all attestation still present, station roster shows 25/23 — net +1 listed and +1 RTK-active since 2026-05-13; 2026-05-12 sourcetable probe remains last successful direct NTRIP fetch — sandbox NTRIP-TCP blocked today).
- **Recent activity:** New stations in 2021 (TOLS, VALS), 2022 (LOGA, MGBU), 2017 (UDI2). One additional station listed 2026-05-13→2026-05-17 (specific code to be confirmed against next sourcetable refresh). Continued expansion under the PNRR MEET project (part of EPOS). No service-discontinuation signal as of 2026-05-17.
- **Coexistence with Re.M.FVG (Marussi):** FReDNet and Re.M.FVG are two distinct, parallel free networks both serving FVG. FReDNet (OGS, scientific origin) emphasises geodynamic spatial coverage; Re.M.FVG (Regione, surveying/cadastral origin) emphasises VRS density. They cross-relay each other's stations through their respective casters (FReDNet caster carries `RAFVG_*` mounts; Marussi caster carries `OGS_*` mounts). For a hobbyist anywhere in FVG either network is usable; Re.M.FVG's denser VRS solution is typically the better default, FReDNet is the alternative when registering with the Regione is inconvenient or as a cross-check.

#### Pipeline status (FVG, 2026-05-13)

Resolved: SOURCES id `frednet` renamed to `rem_fvg` and re-pointed at the
Marussi caster it always served; `data/frednet.sourcetable` → `data/rem_fvg.sourcetable`;
`rtk_inventory.md` split into a `rem_fvg` block (in pipeline, Marussi) and a
`frednet` block (OGS, not in pipeline — cross-relayed via the Marussi caster).
Country marker, country-survey bullet, README, and global-survey updated.

---

### GPS-UMBRIA — Umbria
- **landing_url:** https://umbriageo.regione.umbria.it/pagine/accesso-rapido-ai-servizi-gpsumbria
- **access_url:** Skip — landing_url is the single operator entry-point for registration + service info; no distinct access page. Station monographs: http://www.umbriageo.regione.umbria.it/CatalogoStazioni/StazioniMonografie.aspx (SSL cert error from sandbox; content not fetched 2026-05-21).
- **Operator:** Regione Umbria + Università di Perugia; 13 stations (7 regional, 6 university).
- **host:port:** `gpsumbria.regione.umbria.it:2101` / `46.254.154.14:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07 and 2026-05-21).
- **num_stations:** 13 multi-constellation (GPS+GLONASS+Galileo+BeiDou); ~40 km spacing. 12 of 13 stations have been sourced with coords (see table below); 1 unidentified.
- **Products:** MAC, VRS, Nearest (from Umbriageo portal). Virtual RINEX also available.
- **Tariff:** Free; online form at umbriageo.regione.umbria.it → credentials emailed.
- **hobbyist_eligibility:** unclear — originally targeted at surveying/cadastral, now also agriculture and drones; no explicit exclusion.
- **legal_residency_required:** No explicit requirement found.
- **VRS:** Yes.
- **datum_epoch:** omitted — no citable per-operator declaration on Umbriageo portal.
- **last_confirmed_alive:** 2026-05-21 (SOURCETABLE 200 OK, GNSMART_Caster 2.0/1.0 confirmed; 4 STR rows all at 43.00, 12.50 placeholder — no per-station mounts in public sourcetable).

#### Station Coordinate Table (GPS-UMBRIA, 12 of 13 stations)
Source: https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-umbria/ (2026-05-21). Network ownership: RE* = Regione Umbria (7); UN*/ITGT = Università di Perugia (5 confirmed, 6 stated). Coordinates in ETRF2000. 13th station not identified in any public source consulted.

| Code | Name | Owner | Lat (N) | Lon (E) |
|------|------|-------|---------|---------|
| REAM | Amelia | RE | 42.5587° | 12.4118° |
| REPI | Città della Pieve | RE | 42.9521° | 12.0024° |
| REFO | Foligno | RE | 42.9557° | 12.7035° |
| ITGT | Gualdo Tadino | UniPG | 43.2337° | 12.7820° |
| REGU | Gubbio | RE | 43.3520° | 12.5780° |
| RENO | Norcia | RE | 42.7964° | 13.0948° |
| UNOV | Orvieto | UniPG | 42.7217° | 12.1165° |
| UNPG | Perugia | UniPG | 43.1194° | 12.3557° |
| UNSG | San Giustino | UniPG | 43.5484° | 12.1765° |
| UNTR | Terni | UniPG | 42.5587° | 12.6738° |
| RETO | Todi | RE | 42.7823° | 12.4069° |
| RETU | Tuoro sul Trasimeno | RE | 43.2088° | 12.0724° |

Note: The operator page https://umbriageo.regione.umbria.it/pagine/gpsumbria-001 explicitly states 7 regional + 6 university = 13 stations. The blog lists 12; one station (likely a 6th university station, possibly Città di Castello or Spoleto) is not found in any source consulted. The ITGT code prefix deviates from the expected "RE" or "UN" convention.

#### Pipeline note (GPS-UMBRIA, 2026-05-21)
The public sourcetable exposes only 4 network-solution mounts (CODE at carrier=0, MAC, NRT30, VRS30) all at placeholder `43.00, 12.50`. No individual physical station mounts are exposed. coord_overrides cannot help without per-station mountpoints. Physical station streams may be available post-login via GNSMART portal. The `physical-coord-vrs` type in rtk_inventory.md is aspirational.

---

### Rete GNSS Campania — Campania
- **landing_url:** http://gps.sit.regione.campania.it/indexmain.php (operator portal "Stazione Permanente GNSS Regione Campania"; 2025-08-20 operator notice redirects new account creation to https://gps-sit.regione.campania.it/ with SPID; existing credentials at gps.sit.regione.campania.it remain valid)
- **access_url:** https://gps-sit.regione.campania.it/ (new SPID-gated registration portal); legacy shared-credentials guide remains at https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-campania/ as secondary reference for the public `Campania` / `GNSS` workflow.
- **Operator:** Regione Campania – SIT (Sistema Informativo Territoriale); Leica Spider; technical operation Topcon Positioning Italy (per 2025-08 operator notice).
- **host:port:** `gps.sit.regione.campania.it:2101` / `109.115.186.34:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07; operator portal text confirms port 2101 unchanged).
- **Public credentials:** username `Campania` · password `GNSS` (30-second VRS access; 1-second VRS now requires SPID-gated account via gps-sit.regione.campania.it).
- **num_stations:** 16 permanent stations (operator-stated on http://gps.sit.regione.campania.it/indexmain.php: "Il numero necessario di Stazioni Permanenti è risultato essere 16"; spacing ≤70 km across Campania provinces including Naples, Salerno, Avellino).
- **Products:** `1_VRS30` (Virtual Reference Station 30-sec), `9_NEAR` (nearest station). Confirmed.
- **Tariff:** Free; basic access open without registration using shared credentials. SPID-gated 1-second VRS still free.
- **hobbyist_eligibility:** Yes — public shared credentials, no registration required for basic RTK (1-sec VRS now requires SPID, which is restricted to Italian-residency digital ID).
- **legal_residency_required:** No for basic 30-sec VRS (shared credentials). Yes effectively for 1-sec VRS (SPID is Italian-resident digital ID).
- **VRS:** Yes.
- **datum_epoch:** omitted — no citable per-operator declaration on the Regione Campania GNSS portal.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK confirmed); operator portal text re-verified 2026-05-17 via WebFetch on http://gps.sit.regione.campania.it/indexmain.php (HTTPS variant ECONNREFUSED; HTTP serves the portal).

#### Station Coordinate Table (Campania, all 16 stations)
Source: https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-campania/ (2026-05-21); coordinates in ETRF2000.

| Code | Name | Lat (N) | Lon (E) |
|------|------|---------|---------|
| AGRO | Agropoli | 40.3464° | 14.9968° |
| ALIF | Alife | 41.3270° | 14.3346° |
| AVEL | Avellino | 40.9119° | 14.7833° |
| ISCH | Barano (Ischia) | 40.7120° | 13.9246° |
| BENE | Benevento | 41.1215° | 14.7780° |
| CARI | Carinola | 41.1947° | 13.9742° |
| EBOL | Eboli | 40.5466° | 14.9870° |
| NAPO | Napoli | 40.8700° | 14.2760° |
| CITR | Oliveto Citra | 40.6886° | 15.2307° |
| SALA | Sala Consilina | 40.4172° | 15.5566° |
| ANGE | S. Angelo dei Lombardi | 40.9309° | 15.1839° |
| BAR2 | S. Bartolomeo in Galdo | 41.4099° | 15.0151° |
| NICO | S. Nicola La Strada | 41.0469° | 14.3274° |
| SAPR | Sapri | 40.0737° | 15.6301° |
| TRGR | Torre del Greco | 40.7790° | 14.4100° |
| VALL | Vallo della Lucania | 40.2352° | 15.2799° |

#### Pipeline note (Campania, 2026-05-21)
The live sourcetable exposes 6 individual station mounts (`11_NAPO_4C`, `12_CARI_4C`, `13_BENE_4C`, `14_TRGR_4C`, `15_AGRO_4C`, `16_NICO_4C`) all at placeholder `40.00, 14.00` with `solution=1`. The pipeline drops `solution=1` entries unless `solution_filter: false` is set on the endpoint. The VRS mounts (`1_VRS30`, `9_NEAR3`) are also all at `40.00, 14.00`. No per-station physical coords are exposed in the sourcetable; all 16 stations need coord_overrides if the 6 mounts are to be surfaced. The 10 stations not exposed as individual mounts (ALIF, AVEL, ISCH, EBOL, CITR, SALA, ANGE, BAR2, SAPR, VALL) would require the operator to expose them in the sourcetable. Operator software: GNSMART (Geo++ version 2.0).

---

### Rete GNSS Puglia — Puglia
- **landing_url:** https://pugliacon.regione.puglia.it/web/sit-puglia-sit/global-positioning-system
- **access_url:** Skip — registration is by email to info@gps.sit.puglia.it; no distinct online access form page. SpiderWeb portal: http://gps.sit.puglia.it/SpiderWeb/frmIndex.aspx (ECONNREFUSED from sandbox; registered-user content).
- **Operator:** Regione Puglia – SIT Puglia; Leica Spider (SpiderWeb 4.3.0.4633 per sourcetable banner).
- **host:port:** `gps.sit.puglia.it:2101` / `138.66.34.59:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07 and 2026-05-21).
- **num_stations:** 12 (confirmed 2026-05-21 via multiple sources: analistgroup blog + geodati.gov.it metadata + INSPIRE geoportal; ETRF2000-RDN frame declared).
- **Products:** IMAX3, MAX3, IMAX2, CMR, CMR+, NRT2; credentials are personalised per number of rovers indicated during registration. No per-station mounts in the public sourcetable.
- **Tariff:** Free; registration via info@gps.sit.puglia.it.
- **hobbyist_eligibility:** unclear — registration is required; process appears open to anyone.
- **legal_residency_required:** No explicit requirement found.
- **VRS:** Yes (network correction mode IMAX/MAX confirmed).
- **datum_epoch:** ETRF2000-RDN — operator-declared on geodati.gov.it metadata record (https://geodati.gov.it/resource/id/r_puglia:3f7f19dd-cb9d-44fc-a07a-9e0d04fe42d4). No epoch stated.
- **last_confirmed_alive:** 2026-05-21 (SOURCETABLE 200 OK confirmed: `GNSS Spider 4.3.0.4633/1.0`, 6 STR rows, date header `gio, 21 mag 2026`).

#### Station Coordinate Table (Puglia, all 12 stations)
Source: https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-puglia/ (2026-05-21); coordinates in ETRF2000-RDN. Note: MARGH longitude shown as 116°08'56" in that source is a transcription error — correct value is 16°08'56" (consistent with city of Margherita di Savoia at ~41.37°N, 16.15°E).

| Code | Name | Lat (N) | Lon (E) |
|------|------|---------|---------|
| ACCA | Accadia | 41.1586° | 15.3312° |
| FASA | Fasano | 40.8348° | 17.3590° |
| FOGG | Foggia | 41.4522° | 15.5321° |
| GINO | Ginosa | 40.5780° | 16.7578° |
| GIUR | Giurdignano | 40.1244° | 18.4300° |
| ISCH | Ischitella | 41.9043° | 15.8965° |
| MARGH | Margherita di Savoia | 41.3733° | 16.1489° |
| POGG | Poggiorsini | 40.9166° | 16.2538° |
| SASA | Salice Salentino | 40.3852° | 17.9646° |
| SPCI | S. Paolo di Civitate | 41.7404° | 15.2595° |
| UGEN | Ugento | 39.9277° | 18.1620° |
| VALE | Valenzano | 41.0164° | 16.9045° |

#### Pipeline note (Puglia, 2026-05-21)
The public sourcetable exposes only network-solution mounts (IMAX3, MAX3, IMAX2, CMR, CMR+) at `41.02, 16.90` with `solution=1`, plus NRT2 at `0.00, 0.00` with `solution=0`. No per-station individual mounts are exposed. Physical station coords cannot be surfaced via coord_overrides without per-station mountpoints in the sourcetable. Accessing individual station streams requires authentication via the SpiderWeb portal (registered users only). The network type in rtk_inventory.md (`physical-coord-vrs`) is aspirational; the actual pipeline output is VRS-only until individual station streams are exposed or a separate physical-coord endpoint is added.

---

### Rete GNSS Abruzzo + Lazio — Abruzzo and Lazio (shared infrastructure)
- **landing_url:** https://gnssnet.regione.abruzzo.it (operator portal)
- **access_url:** https://gnssnet.regione.abruzzo.it/accesso.php (registration form; HTTP 200 + active form 2026-05-17)
- **Operator:** Regione Abruzzo (hosts and operates); Lazio region fully integrated into same system.
- **host:port:** `gnss-rtk.regione.abruzzo.it:2101` / `93.57.92.145:2101`
  - NOTE: Both hostnames/IPs timed out from test location on 2026-05-07, -12, -17, and -21. The protrack guide (updated Nov 2025) and the regional portal both document this endpoint. The service has a history of brief outages. Treated as likely alive but unreachable from external test locations.
  - Alternate (older): `gnssnet.regione.abruzzo.it:2101` — also timed out.
- **num_stations:** Abruzzo: 20 per analistgroup station list (2026-05-21; 20 codes with Abruzzo-geography coords). Note: older sources cite 16 (original deployment) and 18 (geoportale.regione.abruzzo.it). The network has expanded over time; 20 likely reflects the current state. Lazio: 18 total / 13 currently active (per Regione Lazio portal 2026-05-21). Combined total: up to 33 active stations.
- **Products:** `near_MSM` (nearest multiconst.), `0_RTCM_MSM` (VRS multiconst.), `VRS23`, `VRS30` (GPS+GLONASS), `NRT30`, `DGPS`, `CMR` variants. Products confirmed from portal description and analistgroup guide; direct sourcetable unverifiable due to persistent timeout.
- **Tariff:** Free; register via access_url.
- **hobbyist_eligibility:** Yes — form is open to anyone; no professional credential required.
- **legal_residency_required:** No.
- **VRS:** Yes.
- **datum_epoch:** ETRF2000, epoch 2022.6 — confirmed from station monographs served at gnssnet.regione.abruzzo.it/[CODE]mono.php (e.g. VTRA monograph: "ETRF2000 (2022.6)", ROUN monograph: "ETRF2000 (2022.6)"; accessed 2026-05-21).
- **last_confirmed_alive:** registration portal `gnssnet.regione.abruzzo.it/accesso.php` re-fetched 2026-05-17, registration form active, "RTK correction and data download services are free" still stated. Individual station monographs (e.g. `gnssnet.regione.abruzzo.it/VTRAmono.php?nome=VTRA`) confirmed serving live coordinate data 2026-05-21. NTRIP TCP endpoint `93.57.92.145:2101` timed out on 2026-05-21 (consistent with prior failures); agendadigitale.regione.abruzzo.it + analistgroup / protrack guides still call the service "24/7 active". **Likely alive but IP-restricted from external test locations.**
- Auxiliary refs: https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-abruzzo-e-lazio/ · https://www.regione.lazio.it/cittadini/urbanistica/sistema-informativo-territoriale-regionale/rete-posizionamento-gnss

#### Station Coordinate Table — Abruzzo (20 stations)
Source: https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-abruzzo/ (2026-05-21); coordinates in ETRF2000. Cross-verified against monograph at gnssnet.regione.abruzzo.it (VTRA matches to arc-second precision).

| Code | Name | Lat (N) | Lon (E) |
|------|------|---------|---------|
| ALRA | Alfedena | 41.7339° | 14.0344° |
| ATRA | Atri | 42.5760° | 13.9910° |
| AZRA | Avezzano | 42.0431° | 13.4238° |
| BLRA | Balsorano | 41.8095° | 13.5617° |
| CDRA | Castel Del Monte | 42.3675° | 13.7201° |
| FRRA | Francavilla | 42.4177° | 14.2922° |
| AQRA | L'Aquila | 42.3659° | 13.3744° |
| MRRA | Martinsicuro | 42.8853° | 13.9159° |
| MZRA | Montazzoli | 41.9466° | 14.4284° |
| MTRA | Montereale | 42.5278° | 13.2400° |
| OCRA | Oricola | 42.0495° | 13.0390° |
| OTRA | Ortucchio | 41.9549° | 13.6459° |
| PBRA | Palombaro | 42.1242° | 14.2285° |
| RMRA | Rocca di Mezzo | 42.2035° | 13.5202° |
| MIRA | Santa Maria Imbaro | 42.2204° | 14.4453° |
| SCRA | Scafa | 42.2681° | 14.0021° |
| SMRA | Sulmona | 42.0499° | 13.9314° |
| TERA | Teramo | 42.6621° | 13.7004° |
| VCRA | Valle Castellana | 42.7354° | 13.4975° |
| VTRA | Vasto | 42.1104° | 14.7079° |

#### Station Coordinate Table — Lazio (18 total, 13 currently active)
Source: https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-nel-lazio/ (station names/codes, 2026-05-21); ROUN and MOCA coordinates confirmed from monograph at gnssnet.regione.abruzzo.it (ETRF2000, epoch 2022.6). Remaining Lazio coordinates NOT independently verified — coordinates not yet sourced. Lazio has 18 total stations; as of 2026-05-21 only 13 are active per Regione Lazio portal (https://www.regione.lazio.it/cittadini/urbanistica/sistema-informativo-territoriale-regionale/rete-posizionamento-gnss). Station LTNA (Latina) was permanently decommissioned after 2024-03-21 communication failure.

Active stations: ACQU (Acquapendente), AMAP (Amatrice), ARDE (Ardea), CASS (Cassino), FIUM (Fiumicino), FOND (Fondi), FROS (Frosinone), MOCA (Montalto di Castro), RITI (Rieti), RIFL (Rignano Flaminio), ROUN (Roma), VALM (Valmontone), VIRB (Viterbo).

Inactive / decommissioned: CVTV (Civitavecchia), LTNA (Latina — permanently offline), PONZ (Ponza), VTEN (Ventotene), VIVA (Vicovaro).

Coordinates confirmed for:
- MOCA (Montalto di Castro): 42.3536°N, 11.6039°E (ETRF2000 ep. 2022.6)
- ROUN (Roma): 41.8932°N, 12.4937°E (ETRF2000 ep. 2022.6)

Monograph URL pattern: `https://gnssnet.regione.abruzzo.it/[CODE]mono.php?nome=[CODE]&type=2L` (Lazio) or `&type=2` (Abruzzo).

#### Pipeline note (Abruzzo+Lazio, 2026-05-21)
The NTRIP endpoint `gnss-rtk.regione.abruzzo.it:2101` / `93.57.92.145:2101` has timed out on every probe from external IPs (2026-05-07, -12, -17, -21). The rtk_map.json entry should be retained; the portal and monograph pages are live. Sourcetable structure is unknown (never fetched from sandbox); likely includes individual station mounts given the station-specific monograph architecture. If/when reachable, coord_overrides or nmea_filter override may be needed depending on how GNSMART exposes stations. The ETRF2000 ep. 2022.6 datum declaration from monographs is citable and should be noted in rtk_inventory.md.

---

### Sicili@NET — Sicilia + Southern Calabria
- **landing_url:** https://www.ct.ingv.it/index.php/risorse-e-servizi/sicil-net
- **access_url:** Skip — access is by direct email to the INGV referent (francesco.pandolfo@ingv.it); no online registration page distinct from landing.
- **Operator:** INGV – Istituto Nazionale di Geofisica e Vulcanologia, Osservatorio Etneo di Catania; scientific network with RTK access.
- **host:port:** `193.206.223.39:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07; Leica GNSS Spider/7.11.1.109).
- **num_stations:** ~80 permanent GPS stations across Sicily and southern Calabria (operator-stated on Sicili@NET landing; primarily for seismic + civil-protection monitoring).
- **Products confirmed in sourcetable:** RTK2, RTK3, IMAX2, IMAX3, MAX3, VRS2, VRS3, FKP2, DGPS (RTCM 2/3); full network correction suite available.
- **Tariff:** Free; request access via email.
- **hobbyist_eligibility:** Yes — stated as available to "all users who request it." No professional requirement cited.
- **legal_residency_required:** No.
- **VRS:** Yes (VRS2 and VRS3 confirmed in sourcetable).
- **datum_epoch:** omitted — no citable per-operator declaration on the Sicili@NET service page.
- **Coverage note:** Southern Calabria is also covered by Sicili@NET; no separate Calabria regional network exists.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK, full mountpoint list confirmed).

---

## Regions Without a Public Caster

| Region | Situation | Best free fallback |
|--------|-----------|-------------------|
| Emilia-Romagna | No public regional GNSS caster | Partial border coverage from Veneto (north-east), SPIN3 (north-west); commercial (NetGEO, HxGN SmartNet) |
| Toscana | No public RTK caster; 8-station University of Siena network is scientific/seismic, no NTRIP | Adjacent GPS-UMBRIA (east/Valtiberina), Liguria GNSS (NW/Lunigiana border) |
| Marche | No public regional GNSS network | Adjacent GPS-UMBRIA (west/south) and Abruzzo-Lazio (south) |
| Sardegna | SARNET project proposed, never activated | Commercial (HxGN SmartNet, NetGEO) |
| Basilicata | No public regional network | Adjacent Campania (west) or Puglia (east) border coverage; commercial |
| Calabria (north/central) | No dedicated caster for most of region | Sicili@NET covers only the southern tip; commercial elsewhere |
| Molise | No public regional network | Partial: Abruzzo Rete GNSS covers northern Molise border zones |

---

## National Reference Network: RDN / IGM

The Rete Dinamica Nazionale (RDN) is a 99-station geodetic framework operated by the Istituto Geografico Militare (IGM), anchoring all regional networks to ETRF2000 (epoch 2008.0). The RDN itself does not operate a public real-time NTRIP caster — it is a geodetic reference network for RINEX download and reference coordinate framing. All regional networks above are tied to RDN. The INGV also operates RING (Rete Integrata Nazionale GPS, ~207 stations for scientific monitoring) which similarly does not offer a public RTK caster; data is free for download.

- IGM RDN: https://www.igmi.org/en/direzione-geodetica/progetto-rdn-rete-dinamica-nazionale

---

## GeoDAF / ASI Caster (EUREF-IP node)
The Agenzia Spaziale Italiana (ASI) operates a EUREF-IP NTRIP broadcaster at `euref-ip.asi.it:2101`. This is a geodetic reference/scientific stream distribution point (RINEX and raw streams for EPN/IGS), not a surveying RTK service. Max 5 simultaneous connections; registration required. Not a hobbyist RTK service.

---

## Commercial Nationwide Networks

### HxGN SmartNet Italy (ItalPOS) — Leica Geosystems / Hexagon
- **landing_url:** https://hxgnsmartnet.com/it-it
- **access_url:** https://hxgnsmartnet.com/it-it/services (service catalogue + subscription routing); reseller-pricing reference https://www.geomatica.it/cat.pag/abbonamento-al-servizio-hxgn-smartnet-czk1345kzpsxzk615.html
- **host:port:** `it.nrtk.eu:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07; Leica GNSS Spider/7.11.0.96).
- **num_stations:** unknown — Hexagon does not publish a per-country physical-CORS count for HxGN SmartNet Italy on the operator portal; coverage stated as nationwide (mainland + islands) at hxgnsmartnet.com/coverage-map.
- **Products confirmed:** RTK2, RTK3, IMAX2, IMAX3, MAX3, VRS2, VRS3, FKP2, DGPS, RTK3-A (full network correction suite).
- **Coverage:** National (mainland + islands); coverage map at hxgnsmartnet.com/coverage-map.
- **Tariff:** Observed 2026-05-07 via third-party reseller geomatica.it:
  - 12-month subscription: **€385 +IVA** (IVA Italy 22%; total ~€469.70/yr)
  - 60-month subscription: **€1,670 +IVA** (~€2,037.40 total)
  - Activation within 48 hours; device-agnostic (not restricted to Leica hardware for network access; SmartNet+ global product also available).
- **hobbyist_eligibility:** unclear — no explicit restriction found; product positioned for professional surveying/construction/agriculture; no VAT-ID requirement stated (unlike NetGEO).
- **legal_residency_required:** No explicit requirement.
- **VRS:** Yes.
- **datum_epoch:** omitted — no citable per-operator declaration on hxgnsmartnet.com IT pages.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK confirmed).

---

### NetGEO / TopNET Live — Topcon Positioning Italy S.r.l.
- **landing_url:** http://www.netgeo.it/page.php?Id=61 (operator service-overview page)
- **access_url:** https://shop.netgeo.it (subscription shop; partita-IVA gated)
- **Operator:** TOPCON POSITIONING ITALY S.r.l., Via Brecce Bianche 152, 60131 Ancona.
- **host:port:** `rtk.topnetlive.com:2101` / `88.86.116.1:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07; IQProxy/1.2 caster).
- **num_stations:** 200 permanent stations (operator-stated, GPS+GLONASS, national coverage).
- **Products:** NET_MSM5, NET_RTCM3, NET_RTCM23 (network/VRS); RTK_MSM5, RTK_RTCM3, RTK_RTCM23 (single station); DGNSS. VRS approach: virtual station generated ~4.5 km from rover.
- **Tariff (observed 2026-05-07 at shop.netgeo.it, VAT excluded):**
  - GEONRTK Mensile: **€90/month +IVA**
  - GeoNRTK Annuale: **€360/year +IVA**
  - GeoNRTK2 Biennale: **€630/2yr +IVA**
  - GEONRTK Triennale: **€850/3yr +IVA**
  - TopNET live-RTK+ EU (5yr): **€1,300 +IVA**
- **hobbyist_eligibility:** **No** — shop explicitly states "La vendita è attiva solo per i clienti con partita IVA" (sales only to VAT-registered entities). Private individuals cannot subscribe without a partita IVA.
- **legal_residency_required:** De facto yes (Italian VAT ID required).
- **VRS:** Yes.
- **datum_epoch:** omitted — no citable per-operator declaration on netgeo.it / topnetlive.com IT pages.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK confirmed).

---

## San Marino (SM) Coverage

San Marino (61 km², enclave within Emilia-Romagna) has no GNSS RTK network of its own. The territory is geographically surrounded by Emilia-Romagna which also lacks a public caster. Coverage available to San Marino users:

- **NetGEO (TopNET Live)** at `rtk.topnetlive.com:2101`: national coverage including San Marino territory; paid/partita IVA required.
- **HxGN SmartNet (ItalPOS)** at `it.nrtk.eu:2101`: national coverage including San Marino; paid (€385/yr +IVA).
- **GPS-UMBRIA** (`gpsumbria.regione.umbria.it:2101`): Umbria stations are ~30–60 km to the west/south-west of San Marino; partial coverage possible near border areas (Pesaro-Urbino direction), but San Marino sits at the edge of Umbria's network geometry. No explicit San Marino coverage claim found.
- **Rete GNSS Abruzzo-Lazio** stations are south of San Marino; marginal coverage at best.
- **Conclusion:** San Marino is practically covered only by the two paid national commercial networks; no free public caster reliably covers SM territory.

---

## Post-Processing (RINEX) Fallbacks

| Service | URL | Cost |
|---------|-----|------|
| RDN – IGM geodetic stations | https://www.igmi.org/en/direzione-geodetica | Free; RINEX download, no real-time |
| RING – INGV national monitoring network | http://ring.gm.ingv.it/ | Free for scientific community |
| Regional portals (FVG, Veneto, Umbria, etc.) | see individual network portals above | Free after registration |
| ASI GeoDAF / EUREF-IP | http://geodaf.mt.asi.it/gps_caster_access.php | Free; registration required; 5-connection limit |

---

## Sources Consulted
- SPIN3 GNSS portal: https://www.spingnss.it/ + https://www.spingnss.it/faq/ + https://www.spingnss.it/i-servizi/
- Regione Liguria geoportal RTK page: https://geoportal.regione.liguria.it/servizi/rete-gnss-liguria/correzioni-in-tempo-reale.html
- TPOS (Provincia Autonoma Trento): https://www.provincia.tn.it/en/Services/TPOS-Trentino-POsitioning-Service
- STPOS (Provincia Autonoma Bolzano): https://www.provincia.bz.it/costruire-abitare/catasto-librofondiario/catasto/stpos-reti-appoggio-geodetico.asp
- Regione Veneto stazioni GPS: https://www.regione.veneto.it/web/ambiente-e-territorio/stazioni-gps
- Re.M.FVG A. Marussi corrections: https://rem.regione.fvg.it/rem-fvg/servizi/correzioni-differenziali
- Regione FVG GNSS (EN): https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/conoscere-ambiente-territorio/FOGLIA11/FOGLIA4/
- FReDNet OGS RTK service: https://frednet.crs.ogs.it/en/servizio-rtk/ (host:port, mountpoints, contact, free-for-all attestation — 2026-05-13)
- FReDNet OGS station list: https://frednet.crs.ogs.it/en/lista-stazioni/ (24 stations, install dates, RTK flags — 2026-05-13)
- FReDNet OGS overview page: https://frednet.crs.ogs.it/en/frednet/ ("22 active stations" — STALE relative to station-list page's 23 RTK-active as of 2026-05-17; operator internal dual-source mismatch flagged in network notes)
- OGS SMINO: https://www.ogs.it/en/northeast-italy-monitoring-system-smino (network context, 22 active GNSS receivers — 2026-05-13)
- M3G GNSS network metadata: https://gnss-metadata.eu/MOID/projnet.6425394325cd38eb370a0aa4 (operator attribution, station codes — 2026-05-13)
- Re.M.FVG history page: https://rem.regione.fvg.it/rem-fvg/info/cenni-storici (founding 1999, 2024-25 BEIDOU + Sappada/Paularo addition, FReDNet cooperation — 2026-05-13)
- GPS-UMBRIA (Umbriageo): https://umbriageo.regione.umbria.it/pagine/accesso-rapido-ai-servizi-gpsumbria
- Rete GNSS Campania operator portal: http://gps.sit.regione.campania.it/indexmain.php (16 permanent stations, port 2101, shared `Campania`/`GNSS` credentials, SPID gate for 1-sec VRS — 2026-05-17)
- Rete GNSS Campania new SPID portal: https://gps-sit.regione.campania.it/ (2025-08-20 operator notice, Topcon Positioning Italy support)
- Regione Campania GNSS (secondary, credentials/usage walkthrough): https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-campania/
- Rete GPS Veneto operator station map: https://retegnssveneto.cisas.unipd.it/Web/page.php?pid=gmap&link=Stazioni_GNSS&chain=6 (35 station codes — 2026-05-17)
- Puglia SIT GPS: https://pugliacon.regione.puglia.it/web/sit-puglia-sit/global-positioning-system
- Abruzzo GNSS portal: https://gnssnet.regione.abruzzo.it/servizi.php
- Regione Lazio GNSS: https://www.regione.lazio.it/cittadini/urbanistica/sistema-informativo-territoriale-regionale/rete-posizionamento-gnss
- ProTRACK Abruzzo+Lazio guide: https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-abruzzo-e-lazio/
- Sicili@NET (INGV Catania): https://www.ct.ingv.it/index.php/risorse-e-servizi/sicil-net
- ProTRACK Sicilia guide: https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-sicilia/
- ArduSimple Italy NTRIP list: https://it.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-italy/
- geoglobex.it Italian regional RTK table: https://www.geoglobex.it/rete-gnss/
- topografo.it Italian GNSS network table: https://topografo.it/rtk-gps-gnss
- HxGN SmartNet Italy: https://hxgnsmartnet.com/it-it/services
- HxGN SmartNet reseller pricing: https://www.geomatica.it/cat.pag/abbonamento-al-servizio-hxgn-smartnet-czk1345kzpsxzk615.html
- NetGEO / TopNET Live shop: https://shop.netgeo.it/
- NetGEO configuration: https://shop.netgeo.it/la-configurazione/
- IGM RDN: https://www.igmi.org/en/direzione-geodetica/progetto-rdn-rete-dinamica-nazionale
- ArduSimple San Marino: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-san-marino/
- ProTRACK Trentino-Alto Adige guide: https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-trentino-alto-adige/
- curl probes of all endpoints — 2026-05-07 and 2026-05-12 (Abruzzo-Lazio endpoint timed out both dates; all other regional endpoints confirmed alive 2026-05-12). 2026-05-17 sandbox NTRIP-TCP egress blocked across the board (all 13 endpoints returned curl exit 28 / HTTP 000), so operator-portal WebFetch was substituted for SPIN3 + FReDNet + Abruzzo to re-attest service status. 2026-05-21: Campania + Puglia + Umbria sourcetables re-confirmed live; Abruzzo endpoint timed out (5th successive failure from external sandbox).
- Puglia station list (12 stations with codes + coords): https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-puglia/ (2026-05-21)
- Puglia GNSS metadata (ETRF2000-RDN frame, INSPIRE): https://geodati.gov.it/resource/id/r_puglia:3f7f19dd-cb9d-44fc-a07a-9e0d04fe42d4 (2026-05-21)
- Campania station list (16 stations with codes + coords): https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-campania/ (2026-05-21)
- Campania permanent stations page: https://gps-sit.regione.campania.it/permanenti.php (2026-05-21 — page exists but does not expose coords directly)
- GPS-UMBRIA station list (12 of 13 stations): https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-umbria/ (2026-05-21)
- GPS-UMBRIA operator station count: https://umbriageo.regione.umbria.it/pagine/gpsumbria-001 (7 regional + 6 university = 13)
- Abruzzo station list (20 stations with codes + coords): https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-abruzzo/ (2026-05-21)
- Lazio station list (18 names/codes): https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-nel-lazio/ (2026-05-21)
- Lazio active station status (13/18 active): https://www.regione.lazio.it/cittadini/urbanistica/sistema-informativo-territoriale-regionale/rete-posizionamento-gnss (2026-05-21)
- Abruzzo+Lazio station monographs (ETRF2000 ep. 2022.6 datum, individual station coords): https://gnssnet.regione.abruzzo.it/VTRAmono.php?nome=VTRA · https://gnssnet.regione.abruzzo.it/ROUNmono.php?nome=ROUN&type=2L · https://gnssnet.regione.abruzzo.it/MOCAmono.php?nome=MOCA&type=2L (2026-05-21)
- SPIN3 GNSS news page (CREO replacing CREM at Cremona 2026-05-12; semestral coordinate refresh 2026-04-01 retaining ETRF2000 epoch 2008.0): https://www.spingnss.it/ + https://www.spingnss.it/nuovo-inquadramento-rete-spin3-aggiornamento-coordinate-6/ — 2026-05-17
- rtk2go IT volunteer bases (12 stations, 2026-05-12): B506Fields (Lecce), Basertk-fogli (Veneto), Carpi_farm, FM01 (Sicily), GESAMP (Liguria), Garabello_RTK (Piedmont), MASCHERINA, MRCATW2020 (Lombardy), SACCO, SIMMN2024, STAP21, TOMPV22 — patchy distribution
- Centipede IT volunteer bases (3 stations, 2026-05-12): FALA (Emilia), FM01 (Sicily), PGDV (Emilia)
- ProTRACK Emilia-Romagna guide (no public regional network; TopNET LIVE recommended): https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-emilia-romagna/
- ProTRACK Marche guide (no public regional network): https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-nelle-marche/
- ProTRACK Toscana guide (LaMMA pilot remains in testing; no operational public caster): https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-toscana/
- LaMMA (Toscana pilot, in testing): https://www.lamma.toscana.it/territorio/mobilita/rete-gps
