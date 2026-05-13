# Italy [IT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-13 (FVG refresh — FReDNet and Re.M.FVG/Marussi re-verified against operator portals; earlier 2026-05-12 pass refreshed the other regions)

## Status: YES — extensive public free NTRIP RTK infrastructure; no single national free caster; coverage is regional

Italy has no unified national free RTK caster. Instead, 10+ regional/autonomous networks operated at the Regione or Provincia Autonoma level provide free (registration-required) RTK corrections. Several regions (Emilia-Romagna, Marche, Sardegna, Toscana, Basilicata, Calabria, Molise) lack a public regional caster; users there rely on adjacent networks or commercial services. Two commercial nationwide networks (HxGN SmartNet / ItalPOS and NetGEO / TopNET Live) fill gaps.

---

## Per-Region Summary Table

| Region | Network | host:port | Tariff | VRS | Hobbyist | curl result 2026-05-12 |
|--------|---------|-----------|--------|-----|----------|------------------------|
| Valle d'Aosta, Piemonte, Lombardia | SPIN3 GNSS | `158.102.7.10:2101` | Free (registration) | Yes (VRS, iMAX, MAC, NRT) | Yes (no restriction stated) | SOURCETABLE 200 OK |
| Liguria | Rete GNSS Liguria | `81.23.86.70:2101` | Free (registration) | Yes (VRS 2/3, MAC, NEAR, DGPS) | unclear (form-based registration) | SOURCETABLE 200 OK (GNCASTER) |
| Trentino (PA Trento) | TPOS | `194.105.50.232:2101` | Free (registration) | Yes (IMAX, MAX, NRT/VRS) | unclear | SOURCETABLE 200 OK |
| Alto Adige / Südtirol (PA Bolzano) | STPOS | `62.101.0.40:2109` | Free (registration) | Yes (Netz-rete, MAX, NRT) | unclear | SOURCETABLE 200 OK |
| Veneto | Rete GPS Veneto | `147.162.229.53:2101` | Free (email registration) | Yes (MAX3, IMAX, NRT) | unclear (email-only signup) | SOURCETABLE 200 OK |
| Friuli-Venezia Giulia | Re.M.FVG "A. Marussi" | `gnsscaster.regione.fvg.it:8080` | Free (form registration) | Yes (VRS_RTCM23/31/32, MAC, IMAC) | Yes (form open to anyone) | SOURCETABLE 200 OK 2026-05-12 |
| Friuli-Venezia Giulia | FReDNet (OGS) | `158.110.30.81:2110` | Free (account on frednet.crs.ogs.it) | Yes (VRS, NEAREST, FKP) | Yes (public, private, scientific) | SOURCETABLE 200 OK 2026-05-12 |
| Umbria | GPS-UMBRIA | `gpsumbria.regione.umbria.it:2101` | Free (online form) | Yes (MAC, VRS, Nearest) | unclear | SOURCETABLE 200 OK (GNCASTER) |
| Campania | Rete GNSS Campania | `gps.sit.regione.campania.it:2101` | Free (open credentials) | Yes (1_VRS30, 9_NEAR) | Yes (public credentials) | SOURCETABLE 200 OK (GNCASTER) |
| Puglia | Rete GNSS Puglia | `gps.sit.puglia.it:2101` | Free (registration) | Yes (IMAX3, MAX3) | unclear | SOURCETABLE 200 OK |
| Abruzzo + Lazio | Rete GNSS Abruzzo-Lazio | `gnss-rtk.regione.abruzzo.it:2101` | Free (registration) | Yes (0_RTCM_MSM/VRS, VRS23/30) | Yes (form open to anyone) | timeout from sandbox 2026-05-12 (third successive probe failure; portal HTTP 200 — see note) |
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
- **Operator:** Regione Piemonte + Regione Lombardia + Regione Valle d'Aosta (joint, since ~2004); data centre at CSI Piemonte.
- **host:port:** `158.102.7.10:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07)
- **Stations:** 39 permanent multi-constellation (GPS+GLONASS+Galileo+BeiDou); ~30 km inter-station spacing.
- **Products:** VRS (RTCM 3 MSM5), iMAX, MAC/MAX, NRT; confirmed in sourcetable.
- **Tariff:** Free for all professional users; free for registration. No pricing.
- **Registration:** Web form at spingnss.it → email confirmation → username/password (max 16 chars). Confirmed Feb 2026 application update.
- **hobbyist_eligibility:** unclear — described as open to "professional operators, public and private" but no explicit hobbyist exclusion.
- **legal_residency_required:** No.
- **VRS:** Yes.
- **Border experiments:** Active data exchange experiments at Liguria and Trentino borders; Liguria and Toscana are NOT part of SPIN3 service area.
- **Contact:** info.gnss@csi.it · +39 011 316 8724.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK, SPIN3 GNSS label confirmed in stream headers).
- Source: https://www.spingnss.it/

---

### Rete GNSS Liguria — Liguria
- **Operator:** Regione Liguria, Geoportale; uses GNSMART (Geo++) software.
- **host:port:** `81.23.86.70:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07)
- **Stations:** 10 stations (7 regional + 3 shared with SPIN3); Ventimiglia to La Spezia.
- **Products:** VRS 2, VRS 3, MAC, NEAR 2, NEAR 3, DGPS (per Liguria RTK portal page).
- **Tariff:** Free; registration via Sportello Cartografico online: https://sportellonline.regione.liguria.it/servizio/PE_0012
- **hobbyist_eligibility:** unclear — form-based; no stated professional requirement found, but the process is a formal regional service request.
- **legal_residency_required:** unclear.
- **VRS:** Yes.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK by IP).
- Source: https://geoportal.regione.liguria.it/servizi/rete-gnss-liguria/correzioni-in-tempo-reale.html

---

### TPOS — Trentino / Provincia Autonoma di Trento
- **Operator:** Servizio Catasto – Ufficio Geodetico, Provincia Autonoma di Trento.
- **host:port:** `194.105.50.232:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07); domain: `tpos.provincia.tn.it` (parameters post-login).
- **Stations:** 11 stations covering Trentino; integrates with STPOS (Bolzano), APOS (Austria), SWIPOS (Switzerland) at borders.
- **Products:** IMAX2, MAX3, NRT2, VRS (from sourcetable: Vicina_NRT2, Area_IMAX2, Area_MAX3).
- **Tariff:** Free; registration at https://www.tpos.provincia.tn.it/SBC/Account/Register
- **hobbyist_eligibility:** unclear — form-based; no stated professional requirement.
- **legal_residency_required:** unclear.
- **VRS:** Yes.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK, TPOS label in stream headers confirmed).
- Source: https://www.provincia.tn.it/en/Services/TPOS-Trentino-POsitioning-Service

---

### STPOS — Alto Adige / Südtirol / Provincia Autonoma di Bolzano
- **Operator:** Ufficio Catasto, Provincia Autonoma di Bolzano; Leica Spider Business Center.
- **host:port:** `62.101.0.40:2109` (confirmed SOURCETABLE 200 OK, 2026-05-07; note non-standard port 2109). Port 2101 on same IP refused.
- **Stations:** 10 stations (Bozen, Bruneck, Corvara, Feldthurns, Helm-M.Elmo, Latsch, Mals, Merano2000, Prettau, Vipiteno).
- **Products:** Nearest3.1, Netz-rete3.1 (RTCM 3), Netz-rete18-19 (RTCM 2), Netz-ReteMAX, Netz-ReteMSM4 (quad-constellation), NRT4 (from sourcetable). VRS/network correction confirmed.
- **Tariff:** Free; registration at http://www.stpos.it/sbc/Account/Register
- **hobbyist_eligibility:** unclear.
- **legal_residency_required:** unclear.
- **VRS:** Yes (network correction mode confirmed in sourcetable).
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK on port 2109, STPOS label confirmed).
- Source: https://www.provincia.bz.it/costruire-abitare/catasto-librofondiario/catasto/stpos-reti-appoggio-geodetico.asp

---

### Rete GPS Veneto — Veneto
- **Operator:** Regione Veneto + Università di Padova (CISAS); software: TopNET (Topcon).
- **host:port:** `147.162.229.53:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07); RINEX portal: retegnssveneto.cisas.unipd.it (that hostname timed out on NTRIP port, but NTRIP IP is live).
- **Stations:** 20+ permanent stations across Veneto.
- **Products:** MAX3, IMAX, NRT; confirmed via ProTRACK guide.
- **Tariff:** Free; registration by email to retegpsveneto@gmail.com (include name, org, phone, email).
- **hobbyist_eligibility:** unclear — email-only signup, no professional credential check stated, but targeted at professionals.
- **legal_residency_required:** No explicit requirement.
- **VRS:** Yes (network correction confirmed).
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK on 147.162.229.53:2101).
- Note: Infrastructure update in progress as of 2026 (device replacements at multiple sites); service online.
- Source: https://www.regione.veneto.it/web/ambiente-e-territorio/stazioni-gps

---

### Re.M.FVG "Antonio Marussi" — Friuli-Venezia Giulia (regional network)
- **Operator:** Regione Autonoma Friuli-Venezia Giulia; software: Leica GNSS Spider (7.11.1.109 banner observed).
- **host:port:** `gnsscaster.regione.fvg.it:8080` / `193.43.178.173:8080` (SOURCETABLE 200 OK 2026-05-12).
- **Network history (operator-stated, 2026-05-13):** Founded 1999 (Palmanova, Ampezzo, Moggio Udinese). Open to private users since 2005. VRS since 2007. GPS+GLONASS+Galileo since 2012/2019. BEIDOU added 2024–2025 in receiver-refresh; Sappada and Paularo added 2024–2025; Slovenian SIGNAL stations integrated at the border. All consistent with the SOURCETABLE on disk.
- **Stations:** 14 own physical stations as of 2026-05-13 (Ampezzo, Barcis, Bevazzana, Bovec*, Cervignano, Codroipo, Gorizia, Idrija*, Koper*, MoggioUdinese, Paularo, Pordenone, Sappada, Tarvisio, Trieste, Udine — `*`=Slovenian SIGNAL partner station accessible via the caster). The caster's published sourcetable also exposes 11 OGS/FReDNet mountpoints (`OGS_ACOM`, `OGS_AFAL`, `OGS_MDEA`, `OGS_MPRA`, `OGS_CODR`, `OGS_FUSE`, `OGS_JOAN`, `OGS_NOVE`, `OGS_PAZO`, `OGS_TRIE`, `OGS_UDI1`, `OGS_ZOUF`) — cross-relay of FReDNet, not new physical infrastructure. Border integration also stated with Austrian EPOSA.
- **Products:** VRS_RTCM23, VRS_RTCM31, VRS_RTCM32 (GPS+GLO+GAL+BDS quad-constellation), VRS_CMR, MAC_RTCM31, IMAC_RTCM3, IMAC_RTCM32, SingleBase_RTCM23/31/32, plus DGPS variants per station — confirmed in sourcetable on disk.
- **Tariff:** Free; credentials by online registration form on the Re.M.FVG portal. Per operator: "Access to the real-time service is free, but is regulated through access credentials."
- **hobbyist_eligibility:** Yes — form is open to anyone who applies; no professional, institutional, or commercial-use restriction stated.
- **legal_residency_required:** No.
- **VRS:** Yes (multiple VRS formats including quad-constellation RTCM 3.2).
- **Reference system:** ETRS89 / ETRF2000 (epoch 2008.0) — RDN aligned.
- **last_confirmed_alive:** 2026-05-12 (SOURCETABLE 200 OK, Leica GNSS Spider/7.11.1.109 confirmed).
- Sources:
  - https://rem.regione.fvg.it/rem-fvg/servizi/correzioni-differenziali (service description, host:port — 2026-05-13)
  - https://rem.regione.fvg.it/rem-fvg/info/cenni-storici (history, station roster, BEIDOU refresh — 2026-05-13)
  - https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/conoscere-ambiente-territorio/FOGLIA11/FOGLIA4/ (regional portal entry)

---

### FReDNet — Friuli-Venezia Giulia (OGS geodynamic network)
- **Full name:** FReDNet = Friuli Regional Deformation Network.
- **Operator:** OGS – Istituto Nazionale di Oceanografia e di Geofisica Sperimentale, Centro di Ricerche Sismologiche (CRS), Udine. Operating since June 2002. (Not INGV — the two institutes are distinct; the 2026-05-07 entry's "OGS/INGV" attribution was incorrect.)
- **Partner:** ISPRA contributes a small number of stations; per the operator's `lista-stazioni` page all 24 currently listed stations are OGS-managed. Part of OGS's SMINO (North-East Italy monitoring system) and a node in the EPOS / GLASS CEGNxEPOS gateway.
- **host:port:** `158.110.30.81:2110` (note non-standard port 2110). Listed verbatim on https://frednet.crs.ogs.it/en/servizio-rtk/ as of 2026-05-13.
- **Stations:** 24 listed; 22 active with RTK enabled (LODI and UDIN have RTK off). Distributed across Friuli-Venezia Giulia plus Veneto (CANV, SUSE, NOVE, MGBU, AFAL) and one outlier in Lombardia (LODI). Coverage area stated as "the entire Friuli Venezia Giulia area." Inter-station spacing ~30–50 km; designed for crustal-deformation monitoring along the Adria microplate boundary, not optimised for RTK density.
- **Active OGS station codes (RTK on, 2026-05-13):** ACOM, AFAL, CANV, CODR, FUSE, GRDO, JOAN, LOGA, MDEA, MGBU, MPRA, NOVE, PAZO, PMNT, SUSE, TOLS, TRIE, UDI1, UDI2, VALS, VARM, ZOUF. Receiver type GNSS (GPS+GLONASS+Galileo); RTK streams advertised as GPS+GLONASS RTCM 3.x.
- **Products:** Single-station (e.g. `OGS_JOAN`), NEAREST (`OGS_NEA`), VRS (`OGS_VRS`), FKP network solution (`OGS_FKP`), DGPS (code). The caster also re-broadcasts a subset of Re.M.FVG/Marussi physical stations under the `RAFVG_*` prefix (e.g. `RAFVG_BARC`) — cross-relay of the two FVG networks.
- **Reference system:** ETRF2000 (epoch 2008.0). RDN-aligned.
- **Tariff:** Free for all users — operator describes the service as "freely accessible to public, private and scientific users." No charge for registration, account, or stream.
- **Registration:** Online form at https://frednet.crs.ogs.it/en/servizio-rtk/ (RTK account management).
- **hobbyist_eligibility:** Yes — no professional, institutional, or research-affiliation gate stated; "public, private and scientific users" is the operator's own wording.
- **legal_residency_required:** No (not stated; no national-ID or VAT-ID requirement).
- **VRS:** Yes.
- **Contact:** gnss@ogs.it · Via Treviso 55, 33100 Udine.
- **last_confirmed_alive:** 2026-05-12 (SOURCETABLE 200 OK on 158.110.30.81:2110 during the 2026-05-12 IT refresh pass; portal `frednet.crs.ogs.it/en/servizio-rtk/` returned current RTK details on 2026-05-13 via WebFetch).
- **Recent activity:** New stations in 2021 (TOLS, VALS), 2022 (LOGA, MGBU), 2017 (UDI2). Continued expansion under the PNRR MEET project (part of EPOS). No service-discontinuation signal as of 2026-05-13.
- **Coexistence with Re.M.FVG (Marussi):** FReDNet and Re.M.FVG are two distinct, parallel free networks both serving FVG. FReDNet (OGS, scientific origin) emphasises geodynamic spatial coverage; Re.M.FVG (Regione, surveying/cadastral origin) emphasises VRS density. They cross-relay each other's stations through their respective casters (FReDNet caster carries `RAFVG_*` mounts; Marussi caster carries `OGS_*` mounts). For a hobbyist anywhere in FVG either network is usable; Re.M.FVG's denser VRS solution is typically the better default, FReDNet is the alternative when registering with the Regione is inconvenient or as a cross-check.
- Sources:
  - https://frednet.crs.ogs.it/en/servizio-rtk/ (operator RTK service page, mountpoint examples, contact, host:port — 2026-05-13)
  - https://frednet.crs.ogs.it/en/lista-stazioni/ (full station list with install dates and RTK flags — 2026-05-13)
  - https://www.ogs.it/en/northeast-italy-monitoring-system-smino (SMINO context, 22 active stations — 2026-05-13)
  - https://gnss-metadata.eu/MOID/projnet.6425394325cd38eb370a0aa4 (M3G project/network registry — 2026-05-13)

#### Pipeline status (FVG, 2026-05-13)

Resolved: SOURCES id `frednet` renamed to `rem_fvg` and re-pointed at the
Marussi caster it always served; `data/frednet.sourcetable` → `data/rem_fvg.sourcetable`;
`networks.md` split into a `rem_fvg` block (in pipeline, Marussi) and a
`frednet` block (OGS, not in pipeline — cross-relayed via the Marussi caster).
Country marker, country-survey bullet, README, and global-survey updated.

---

### GPS-UMBRIA — Umbria
- **Operator:** Regione Umbria + Università di Perugia; 13 stations (7 regional, 6 university).
- **host:port:** `gpsumbria.regione.umbria.it:2101` / `46.254.154.14:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07).
- **Stations:** 13 multi-constellation stations (GPS+GLONASS+Galileo+BeiDou); ~40 km spacing.
- **Products:** MAC, VRS, Nearest (from Umbriageo portal). Virtual RINEX also available.
- **Tariff:** Free; online form at umbriageo.regione.umbria.it → credentials emailed.
- **hobbyist_eligibility:** unclear — originally targeted at surveying/cadastral, now also agriculture and drones; no explicit exclusion.
- **legal_residency_required:** No explicit requirement found.
- **VRS:** Yes.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK, HTTP/0.9 NTRIP/1.0 caster format confirmed).
- Source: https://umbriageo.regione.umbria.it/pagine/accesso-rapido-ai-servizi-gpsumbria

---

### Rete GNSS Campania — Campania
- **Operator:** Regione Campania – SIT (Sistema Informativo Territoriale); Leica Spider.
- **host:port:** `gps.sit.regione.campania.it:2101` / `109.115.186.34:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07).
- **Public credentials:** username `Campania` · password `GNSS` (30-second VRS access without login; 1-second requires SPID account).
- **Stations:** Multiple stations covering Campania provinces (Naples, Salerno, Avellino, and others).
- **Products:** `1_VRS30` (Virtual Reference Station 30-sec), `9_NEAR` (nearest station). Confirmed.
- **Tariff:** Free; basic access open without registration using shared credentials.
- **hobbyist_eligibility:** Yes — public shared credentials, no registration required for basic RTK.
- **legal_residency_required:** No.
- **VRS:** Yes.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK confirmed).
- Source: https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-campania/

---

### Rete GNSS Puglia — Puglia
- **Operator:** Regione Puglia – SIT Puglia; Leica Spider (SpiderWeb).
- **host:port:** `gps.sit.puglia.it:2101` / `138.66.34.59:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07).
- **Stations:** 10+ stations distributed across Puglia.
- **Products:** IMAX3, MAX3, RTCM 3.x and 2.x; credentials are personalised per number of rovers indicated during registration.
- **Tariff:** Free; registration via info@gps.sit.puglia.it.
- **hobbyist_eligibility:** unclear — registration is required; process appears open to anyone.
- **legal_residency_required:** No explicit requirement found.
- **VRS:** Yes (network correction mode IMAX/MAX confirmed).
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK confirmed on 138.66.34.59:2101).
- Source: https://pugliacon.regione.puglia.it/web/sit-puglia-sit/global-positioning-system

---

### Rete GNSS Abruzzo + Lazio — Abruzzo and Lazio (shared infrastructure)
- **Operator:** Regione Abruzzo (hosts and operates); Lazio region fully integrated into same system. 16 Abruzzo + 13 Lazio stations.
- **host:port:** `gnss-rtk.regione.abruzzo.it:2101` / `93.57.92.145:2101`
  - NOTE: Both hostnames/IPs timed out from test location on 2026-05-07. The protrack guide (updated Nov 2025) and the regional portal both document this endpoint. The service has a history of brief outages. Treated as likely alive but unconfirmed at probe time.
  - Alternate (older): `gnssnet.regione.abruzzo.it:2101` — also timed out.
  - Registration portal online: https://gnssnet.regione.abruzzo.it/accesso.php (HTTP 200, 2026-05-07)
- **Products:** `near_MSM` (nearest multiconst.), `0_RTCM_MSM` (VRS multiconst.), `VRS23`, `VRS30` (GPS+GLONASS), `NRT30`, `DGPS`, `CMR` variants.
- **Tariff:** Free; register at gnssnet.regione.abruzzo.it/accesso.php.
- **hobbyist_eligibility:** Yes — form is open to anyone; no professional credential required.
- **legal_residency_required:** No.
- **VRS:** Yes.
- **last_confirmed_alive:** portal HTTP 200 historically; NTRIP endpoint timed out again from sandbox 2026-05-12 (third successive failure across 2026-05-07 and earlier probes). The agendadigitale.regione.abruzzo.it and trasparenza.regione.abruzzo.it pages continue to describe the service as "24/7 active" and the analistgroup / protrack guides re-confirm the IP/host as the documented production endpoint. **Likely alive but blocked / unreachable from external test locations — confirmation requires a probe from within Italy.**
- Source: https://gnssnet.regione.abruzzo.it · https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-abruzzo-e-lazio/

---

### Sicili@NET — Sicilia + Southern Calabria
- **Operator:** INGV – Istituto Nazionale di Geofisica e Vulcanologia, Osservatorio Etneo di Catania; scientific network with RTK access.
- **host:port:** `193.206.223.39:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07; Leica GNSS Spider/7.11.1.109).
- **Stations:** ~80 permanent GPS stations across Sicily and southern Calabria. Network used for seismic and civil protection monitoring.
- **Products confirmed in sourcetable:** RTK2, RTK3, IMAX2, IMAX3, MAX3, VRS2, VRS3, FKP2, DGPS (RTCM 2/3); full network correction suite available.
- **Tariff:** Free; request access via email to the INGV referent (contact: francesco.pandolfo@ingv.it).
- **hobbyist_eligibility:** Yes — stated as available to "all users who request it." No professional requirement cited.
- **legal_residency_required:** No.
- **VRS:** Yes (VRS2 and VRS3 confirmed in sourcetable).
- **Coverage note:** Southern Calabria is also covered by Sicili@NET; no separate Calabria regional network exists.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK, full mountpoint list confirmed).
- Source: https://www.ct.ingv.it/index.php/risorse-e-servizi/sicil-net

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
- **host:port:** `it.nrtk.eu:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07; Leica GNSS Spider/7.11.0.96).
- **Products confirmed:** RTK2, RTK3, IMAX2, IMAX3, MAX3, VRS2, VRS3, FKP2, DGPS, RTK3-A (full network correction suite).
- **Coverage:** National coverage (mainland + islands); coverage map at hxgnsmartnet.com/coverage-map.
- **Tariff:** Observed 2026-05-07 via third-party reseller geomatica.it:
  - 12-month subscription: **€385 +IVA** (IVA Italy 22%; total ~€469.70/yr)
  - 60-month subscription: **€1,670 +IVA** (~€2,037.40 total)
  - Activation within 48 hours; device-agnostic (not restricted to Leica hardware for network access; SmartNet+ global product also available).
- **hobbyist_eligibility:** unclear — no explicit restriction found; product positioned for professional surveying/construction/agriculture; no VAT-ID requirement stated (unlike NetGEO).
- **legal_residency_required:** No explicit requirement.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK confirmed).
- Source: https://hxgnsmartnet.com/it-it · https://www.geomatica.it/cat.pag/abbonamento-al-servizio-hxgn-smartnet-czk1345kzpsxzk615.html

---

### NetGEO / TopNET Live — Topcon Positioning Italy S.r.l.
- **host:port:** `rtk.topnetlive.com:2101` / `88.86.116.1:2101` (confirmed SOURCETABLE 200 OK, 2026-05-07; IQProxy/1.2 caster).
- **Operator:** TOPCON POSITIONING ITALY S.r.l., Via Brecce Bianche 152, 60131 Ancona.
- **Stations:** 200 permanent stations (GPS+GLONASS), national coverage.
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
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK confirmed).
- Source: https://shop.netgeo.it · http://www.netgeo.it/page.php?Id=61

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
- FReDNet OGS overview page: https://frednet.crs.ogs.it/en/frednet/ (22 active stations, PNRR MEET / EPOS context — 2026-05-13)
- OGS SMINO: https://www.ogs.it/en/northeast-italy-monitoring-system-smino (network context, 22 active GNSS receivers — 2026-05-13)
- M3G GNSS network metadata: https://gnss-metadata.eu/MOID/projnet.6425394325cd38eb370a0aa4 (operator attribution, station codes — 2026-05-13)
- Re.M.FVG history page: https://rem.regione.fvg.it/rem-fvg/info/cenni-storici (founding 1999, 2024-25 BEIDOU + Sappada/Paularo addition, FReDNet cooperation — 2026-05-13)
- GPS-UMBRIA (Umbriageo): https://umbriageo.regione.umbria.it/pagine/accesso-rapido-ai-servizi-gpsumbria
- Regione Campania GNSS (via blog.analistgroup.com): https://blog.analistgroup.com/come-connettersi-alla-rete-gnss-in-campania/
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
- curl probes of all endpoints — 2026-05-07 and 2026-05-12 (Abruzzo-Lazio endpoint timed out both dates; all other regional endpoints confirmed alive 2026-05-12)
- rtk2go IT volunteer bases (12 stations, 2026-05-12): B506Fields (Lecce), Basertk-fogli (Veneto), Carpi_farm, FM01 (Sicily), GESAMP (Liguria), Garabello_RTK (Piedmont), MASCHERINA, MRCATW2020 (Lombardy), SACCO, SIMMN2024, STAP21, TOMPV22 — patchy distribution
- Centipede IT volunteer bases (3 stations, 2026-05-12): FALA (Emilia), FM01 (Sicily), PGDV (Emilia)
- ProTRACK Emilia-Romagna guide (no public regional network; TopNET LIVE recommended): https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-emilia-romagna/
- ProTRACK Marche guide (no public regional network): https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-nelle-marche/
- ProTRACK Toscana guide (LaMMA pilot remains in testing; no operational public caster): https://protrack.studio/blog/it/come-connettersi-alla-rete-gnss-in-toscana/
- LaMMA (Toscana pilot, in testing): https://www.lamma.toscana.it/territorio/mobilita/rete-gps
