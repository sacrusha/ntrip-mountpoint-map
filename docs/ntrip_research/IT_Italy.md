# Italy [IT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (refresh of 2026-05-07 entry — all endpoints re-probed)

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
| Friuli-Venezia Giulia | Re.M.FVG "A. Marussi" | `gnsscaster.regione.fvg.it:8080` | Free (form registration) | Yes (VRS_RTCM23/31/32, MAC, IMAC) | Yes (form open to anyone) | SOURCETABLE 200 OK |
| Friuli-Venezia Giulia | FReDNet (OGS/INGV) | `158.110.30.81:2110` | Free (account on frednet.crs.ogs.it) | Yes (VRS) | Yes (research/all welcome) | SOURCETABLE 200 OK |
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
- **Operator:** Regione Autonoma Friuli-Venezia Giulia; software: Leica GNSS Spider.
- **host:port:** `gnsscaster.regione.fvg.it:8080` / `193.43.178.173:8080` (confirmed SOURCETABLE 200 OK, 2026-05-07).
- **Stations:** 10+ stations covering entire FVG region; integrates Austrian EPOSA and Slovenian university stations at borders.
- **Products:** VRS_RTCM23, VRS_RTCM31, VRS_RTCM32 (GPS+GLO+GAL+BDS), VRS_CMR, MAC_RTCM31, IMAC_RTCM3, IMAC_RTCM32, SingleBase, DGPS variants — confirmed in sourcetable.
- **Tariff:** Free; credentials by email: rete.gnss.marussi@regione.fvg.it (form on website).
- **hobbyist_eligibility:** Yes — form is open to anyone who applies.
- **legal_residency_required:** No.
- **VRS:** Yes (multiple VRS formats confirmed in sourcetable).
- **Reference system:** ETRS89 / ETRF2000 (2008.0) — RDN aligned.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK, Leica GNSS Spider/7.11.1.109 confirmed).
- Source: https://rem.regione.fvg.it/rem-fvg/servizi/correzioni-differenziali · https://www.regione.fvg.it/rafvg/cms/RAFVG/ambiente-territorio/conoscere-ambiente-territorio/FOGLIA11/FOGLIA4/

---

### FReDNet — Friuli-Venezia Giulia (OGS/INGV seismological network)
- **Operator:** OGS – Istituto Nazionale di Oceanografia e di Geofisica Sperimentale, Centro di Ricerche Sismologiche (CRS).
- **host:port:** `158.110.30.81:2110` (confirmed SOURCETABLE 200 OK, 2026-05-07; note port 2110). Also: http://frednet.crs.ogs.it/en/servizio-rtk/
- **Stations:** Network of ~40 GNSS stations designed for seismic/geodynamic monitoring; primarily in FVG but extends into adjacent Slovenia and Austria.
- **Products:** VRS (Virtual Reference Station) confirmed on website; RTCM 2 + RTCM 3 single-base and VRS corrections.
- **Tariff:** Free (account via frednet.crs.ogs.it registration form).
- **hobbyist_eligibility:** Yes — "all research and collaboration proposals are welcome." Open registration.
- **legal_residency_required:** No.
- **VRS:** Yes.
- **last_confirmed_alive:** 2026-05-07 (SOURCETABLE 200 OK on 158.110.30.81:2110).
- Note: FReDNet is a scientific/research network operating in parallel to the regional Re.M.FVG network. Both serve FVG; FReDNet stations are distributed for geodynamic coverage, not optimised for RTK density.
- Source: https://frednet.crs.ogs.it/en/servizio-rtk/

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
- FReDNet OGS RTK service: https://frednet.crs.ogs.it/en/servizio-rtk/
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
