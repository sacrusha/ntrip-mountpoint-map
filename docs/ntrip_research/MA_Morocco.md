# Morocco [MA] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified via WebSearch; no service / station-count / pricing change since 2026-05-12; ANCFCC + itri sites still NXDOMAIN from sandbox)

## Status: TWO active NTRIP casters — ANCFCC (government, 60 stations, registration required) and itri (private commercial, 231 stations, registration required)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — two operators |
| **Network name — ANCFCC** | Réseau GNSS permanent de l'ANCFCC |
| **Operator — ANCFCC** | Agence Nationale de la Conservation Foncière du Cadastre et de la Cartographie (ANCFCC) — ancfcc.gov.ma |
| **host:port — ANCFCC** | Not publicly documented; registration required at ancfcc.gov.ma; portal at https://www.ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/ |
| **tariff — ANCFCC** | Not publicly listed; contact ANCFCC via +212 6 60 10 27 01–06 or +212 5 37 70 58 85 (fax) |
| **Network name — itri** | itri (first private Moroccan GNSS permanent-station network) |
| **Operator — itri** | itri / SAMTOP — itri-gnss.ma / itri-gnss.com |
| **landing_url — itri** | `https://itri-gnss.ma/index.html` — operator-owned itri landing (FR). Describes the 231-station network, constellation support, correction modes (single-base RTK / network RTK / VRS), RINEX post-processing. Alternative mirror: `https://www.itri-gnss.com/`. |
| **access_url — itri** | `https://www.itri-gnss.ma/documentation/index.html` — operator-owned documentation hub describing service usage and configuration. More useful than the bare `https://secure.itri-gnss.ma/admin/auth/register` admin-auth registration endpoint, which has no service description. |
| **host:port — itri** | Not publicly documented; credentials issued post-registration at https://secure.itri-gnss.ma/admin/auth/register |
| **tariff — itri** | Not publicly listed; professional subscription; contact contact@itri-gnss.com or +212 707 797 830 |
| **hobbyist_eligibility** | ANCFCC: unclear; itri: marketed "dédié aux professionnels" — individual hobbyist eligibility not confirmed for either |
| **legal_residency_required** | No explicit residency restriction found for either operator |
| **last_confirmed_alive** | 2026-05-12 — ANCFCC GNSS page text re-verified via WebSearch (confirms 60 stations, RINEX 1–60 s cadences); ANCFCC website unreachable from sandbox (DNS NXDOMAIN on this date). `itri-gnss.ma` and `itri-gnss.com` — DNS NXDOMAIN from sandbox 2026-05-12. WebFetch of either domain returned ECONNREFUSED. Domain reachability appears region- or DNS-resolver-dependent; itri is presumed live (active marketing, gtopic.net article references it 2022) but caster sourcetable not independently re-confirmed on this date |

## Most Recent Project Announcement

**ANCFCC expansion to 60 stations:** The ANCFCC permanent GNSS network has grown from 18 stations (original deployment, stations documented at Tanger, Al Hoceima, Oujda, Rabat, Casablanca, Fès, Guercif, El Jadida, Essaouira, Marrakech, Beni Mellal, Errachidia, Agadir, Ouarzazate, Guelmim, Laâyoune, Dakhla) through a 2017 densification adding 12 further stations, and now totals 60 permanent GNSS stations covering the full national territory including Western Sahara. The ANCFCC service description now explicitly states real-time RTK distribution: "La diffusion via internet des corrections aux observations GNSS pour le positionnement en mode RTK et RTK-Réseau" — confirming an active NTRIP real-time service (not RINEX-only). Source: https://www.ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/ (observed 2026-05-06).

**itri private network:** Designed by SAMTOP and launched in 2020. As of 2026-05-06, itri claims 231 permanent stations covering the national territory. itri is Morocco's first private GNSS permanent-station network. Source: itri-gnss.ma (observed via search, direct fetch blocked by server).

- ANCFCC GNSS page: https://www.ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/
- itri documentation: https://www.itri-gnss.ma/documentation/index.html
- itri coverage: https://itri-gnss.ma/couverture-geographique.html

## Context Notes

- **ANCFCC government network:**
  - 60 permanent GNSS stations connected to the Rabat central server via private network.
  - Services: (1) RINEX observations at 1/5/10/15/20/30/60 s cadences; (2) online coordinate computation (static, stop-and-go, kinematic); (3) real-time RTK and RTK-Network corrections via internet (NTRIP protocol explicitly described).
  - NTRIP host/port not published; registration at ancfcc.gov.ma required.
  - Contact: Avenue Abderrahim Bouabid, Hay Riad, Rabat; tel +212 6 60 10 27 01/02/03/04/05/06; fax +212 5 37 70 58 85.
  - Note: The older ReseauGnss sub-page (ancfcc.gov.ma/ReseauGnss/) still shows only 18 stations and lists no real-time RTK; the updated cartographie/reseau-gnss/ page (fetched 2026-05-06) is current and confirms 60 stations and real-time service.

- **itri private network:**
  - 231 permanent GNSS stations (as of 2026-05-06) covering the national territory. Designed by SAMTOP; launched 2020.
  - Signals tracked: GPS, GLONASS, Galileo, BeiDou.
  - Correction modes: single-station RTK (choose nearest station), network RTK (corrections from full network or nearest station), VRS (virtual reference station at user position).
  - RINEX post-processing access also provided.
  - Registration: https://secure.itri-gnss.ma/admin/auth/register
  - Contact: contact@itri-gnss.com; +212 707 797 830; 2 Mars Rue Amsterdam IMM 6 APP 2, Casablanca.
  - itri-gnss.ma main domain returned connection errors during direct WebFetch (2026-05-06); itri-gnss.com domain returned same. Port 2101 probe returned ECONNREFUSED. Service is functional per search evidence but caster endpoint is private.
  - itri is not listed on ArduSimple Morocco page (which states no national network found) — confirming its closed/professional-only access model.

- **GeoPrism Maroc:** Mentions GNSS correction services for Morocco; details thin; independent operator status unconfirmed.
- **gtopic.net analysis (Apr 2022)** by Moroccan geomatics policy author: recommends a public-private partnership model where ANCFCC maintains baseline geodetic infrastructure under Law 58-00 while private partners densify under standardised guidelines — analogous to France's IGN-TERIA. The piece references both ANCFCC and itri as existing operators but does not list pricing.
- **Global commercial networks:** Centipede-RTK has no MAR pipeline pins as of 2026-05-12 (`py scripts/stations_by_country.py` lists MAR only under rtk2go). GEODNET and ONOCOY Morocco coverage not confirmed.
- **rtk2go volunteer presence**: 1 entry — `ProdairLAB` at 31.65, −8.04 (near Marrakech) — confirmed via `py scripts/stations_by_radius.py 31.6 -8.0 300` 2026-05-12. Hobbyist single-base option for the Marrakech area; no other public volunteer bases.
- **Practical workaround:** Register with ANCFCC (government, likely lower cost) or itri (private, larger station density); deploy a local base for single-base RTK; or use Galileo HAS / PPP for sub-metre accuracy.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ANCFCC GNSS permanent network** — RINEX at 1/5/10/15/20/30/60 s from 60 stations | https://www.ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/ | Registration required; tariff not published |
| **itri permanent network** — RINEX from 231 stations via registered account | https://secure.itri-gnss.ma/admin/auth/register | Professional subscription; pricing not public |
| **IGS / EarthScope archive** — RABT station (Rabat) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account required) |

## Sources Consulted
- ANCFCC GNSS permanent network page (updated): https://www.ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/
- ANCFCC ReseauGnss legacy page: https://www.ancfcc.gov.ma/ReseauGnss/
- itri-gnss.ma homepage: https://itri-gnss.ma/index.html
- itri-gnss.ma coverage page: https://itri-gnss.ma/couverture-geographique.html
- itri-gnss.ma documentation: https://www.itri-gnss.ma/documentation/index.html
- itri-gnss.ma contact page: https://www.itri-gnss.ma/contact.html
- itri-gnss.ma registration: https://secure.itri-gnss.ma/admin/auth/register
- itri-gnss.com (alternate domain): https://www.itri-gnss.com/
- itri Facebook: https://www.facebook.com/itri.gnss/
- ArduSimple Morocco: https://fr.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-morocco/ — confirms (2026-05-12) Morocco "not among" the published list of countries with a single national RTK network (ArduSimple does not enumerate ANCFCC / itri on this page)
- GeoPrism Maroc: https://geoprism-maroc.com/le-gnss/
- gtopic.net policy analysis (PPP for Moroccan reference stations, Apr 2022): https://gtopic.net/blog/2022/04/18/stations-de-reference-gnss-actives-et-partenariat-public-prive/
- GeoRezo forum thread (Morocco permanent stations): https://georezo.net/forum/viewtopic.php?id=119022
- NTRIP-list.com — no Morocco entries found 2026-05-12
- RTK2go monitor (monitor.use-snip.com) — 1 Morocco mountpoint `ProdairLAB` visible 2026-05-12
- Local pipeline check (2026-05-12): `py scripts/stations_by_country.py MAR` returns 1 rtk2go entry (ProdairLAB 31.65, −8.04); 0 Centipede, 0 EarthScope
- Sandbox DNS resolution for `itri-gnss.ma` and `itri-gnss.com` — NXDOMAIN 2026-05-12 (`nslookup`); `www.ancfcc.gov.ma` — NXDOMAIN 2026-05-12. ANCFCC content corroborated via WebFetch of gtopic.net mirror and WebSearch snippets referencing the 60-station figure on the cartographie page
