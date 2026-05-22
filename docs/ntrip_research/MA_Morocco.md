# Morocco [MA] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

Two national-scale NTRIP operators in Morocco — ANCFCC (government, 60
permanent stations, registration-only) and itri (private, claims 231 stations,
professional subscription). Neither publishes a host:port or a tariff; both
require account negotiation through their portals. Two volunteer rtk2go base
stations exist (Marrakech area and Sidi Rahal on the Atlantic coast),
providing the only zero-friction free option for the central Atlantic strip.
No published cheap-and-accessible national tier; cheapest cm-accurate path is
ANCFCC subscription if negotiable, otherwise the local rtk2go base.

## Casters

### ANCFCC — Réseau GNSS Permanent (government, restricted-registration)

- operator: Agence Nationale de la Conservation Foncière du Cadastre et de la
  Cartographie (ANCFCC)
- landing_url: https://www.ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/
  (re-verified text via WebSearch 2026-05-23; cited 60-station figure and
  RINEX cadences. Direct WebFetch returned 404 from sandbox 2026-05-23 —
  resolvable only from MA-region clients or via cached search snippets)
- access_url: same as landing_url; no separate self-service registration
  portal published
- access_type: restricted — no public NTRIP endpoint, no published tariff; ANCFCC
  must be contacted directly to negotiate access
- coverage: 60 permanent stations nationwide. Original 18-station core listed
  in named cities (Tanger, Al Hoceima, Oujda, Rabat, Casablanca, Fès,
  Guercif, El Jadida, Essaouira, Marrakech, Beni Mellal, Errachidia, Agadir,
  Ouarzazate, Guelmim, Laâyoune, Dakhla); 2017 densification added 12; current
  total 60, including Western Sahara (Laâyoune, Dakhla).
- num_stations: 60 (operator-declared on the cartographie/reseau-gnss page)
- hobbyist_eligibility: ? — no published individual / hobbyist sign-up path;
  service framed for cadastral and professional users
- residency_required: ? — undocumented; the cartographie page does not state
  any residency rule, but access is by direct contact only
- datum_epoch: omitted — operator pages observed do not state datum and
  epoch in citable form. The legacy classical datum Merchich (Clarke 1880
  ellipsoid, EPSG 4261 family) is widely documented in EPSG / cadastral
  sources but is not the GNSS reference frame; the modern GNSS frame is not
  operator-declared on the cartographie pages observed.

Services per operator description: (1) RINEX observations at 1 / 5 / 10 / 15
/ 20 / 30 / 60 s cadences; (2) online coordinate computation; (3) real-time
RTK and RTK-Network corrections via internet — *"La diffusion via internet
des corrections aux observations GNSS pour le positionnement en mode RTK et
RTK-Réseau"*. Host:port not published; central server in Rabat.

Contact: Avenue Abderrahim Bouabid, Hay Riad, Rabat; +212 6 60 10 27 01–06;
fax +212 5 37 70 58 85.

Sourcetable: not externally reachable; no public host:port. The older
`ancfcc.gov.ma/ReseauGnss/` sub-page still shows the legacy 18-station view
and RINEX-only services; the `nos-metiers/cartographie/reseau-gnss/` page is
the current one with the 60-station figure and RTK service.

### itri — private national network

- operator: SAMTOP / itri (Casablanca)
- landing_url: https://itri-gnss.ma/index.html (FR; service description,
  coverage, modes). Alternative mirror: https://www.itri-gnss.com/
- access_url: https://www.itri-gnss.ma/documentation/index.html
  (documentation hub; preferred over the bare admin-auth
  https://secure.itri-gnss.ma/admin/auth/register registration endpoint)
- access_type: paid — professional subscription, tariff not published; contact
  contact@itri-gnss.com / +212 707 797 830
- coverage: claimed nationwide; operator advertises 231 permanent stations
  (claim per itri 2026-05, not independently confirmed because the caster
  sourcetable is not externally reachable). Networked modes: single-base RTK
  (nearest station), Network-RTK, VRS.
- num_stations: 231 claimed (operator-declared; sourcetable not externally
  visible to confirm)
- hobbyist_eligibility: ? — marketed *"dédié aux professionnels"*, no
  individual tier published, but no explicit prohibition on hobbyist sign-up
  either; sign-up requires contacting itri directly (checked: itri-gnss.ma
  homepage 2026-05-23 via WebSearch cache; itri-gnss.ma documentation hub
  2026-05-23 — site ECONNREFUSED outside MA-region resolvers).
- residency_required: ? — undocumented
- datum_epoch: omitted — no operator-declared datum/epoch found

Signals: GPS + GLONASS + Galileo + BeiDou. RINEX post-processing also
provided. Both `itri-gnss.ma` and `itri-gnss.com` resolved NXDOMAIN /
ECONNREFUSED from sandbox 2026-05-12 and 2026-05-23; reachability is
region/DNS-resolver dependent. Service is presumed live (active marketing,
Facebook activity, gtopic.net 2022 reference) but caster sourcetable not
independently re-confirmed.

### rtk2go — volunteer single-base coverage (free)

- operator: SNIP / use-snip.com (global aggregator; covered in
  `RTK2GO.md`)
- access_type: free, no registration (user = any email; password `none`)
- num_stations (MAR): 2 (verified 2026-05-23 via
  `py scripts/stations_by_country.py MAR`)
  - **ProdairLAB** — 31.65, −8.04 (Marrakech area; RTCM 3.3 multi-constellation
    including GPS+GLO+GAL+BDS+QZSS MSM7, station-coord 1006)
  - **SidiRahal** — 33.45, −8.03 (Sidi Rahal Chataï, Atlantic coast east of
    Casablanca; RTCM 3.2 multi-constellation MSM, station-coord 1006)
- coverage: two isolated single-base stations on the Atlantic strip; both
  give cm-grade RTK within ~10–30 km, degrading via ppm. No NRTK; no Atlas /
  Rif / east / south coverage.
- See `RTK2GO.md` for credentials / etiquette / known-unreliable warning.

### IGS — RABT00MAR0

- operator: IGS / EarthScope rebroadcast (covered in `IGS.md` and
  `Earthscope.md`)
- host: caster.cddis.eosdis.nasa.gov:443 (TLS), mountpoint RABT00MAR0 at
  Rabat (34.00, −6.85), Ashtech UZ-12, RTCM 3 / MSM2 1076
- access_type: restricted — IGS registration required
- This is a low-density scientific stream; useful for Rabat-area
  post-processing or as an absolute-frame check, not for dense RTK coverage.

## Undetermined / disqualified

- **GeoPrism Maroc** (https://geoprism-maroc.com/le-gnss/) — *undetermined*,
  not disqualified. Page is educational material about RTK/NRTK concepts; it
  does not state whether GeoPrism owns CORS infrastructure, resells ANCFCC /
  itri, or merely consults. No host:port, no tariff, no station list.
  Insufficient evidence to classify (checked: geoprism-maroc.com/le-gnss/
  2026-05-23).
- **Centipede-RTK** — *disqualified*: no Morocco base stations as of
  2026-05-23 (`py scripts/stations_by_country.py MAR` lists no centipede
  entries).
- **GEODNET, onocoy, Trimble VRS Now, SmartNet** — *disqualified*: no MA
  coverage advertised.
- **ArduSimple Morocco page**
  (https://fr.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-morocco/) —
  does not enumerate ANCFCC or itri; lists only the global trio
  rtk2go + IGS + EarthScope. ArduSimple is usually thorough on national
  operators, so the omission is completeness-relevant: it most likely
  reflects that neither ANCFCC nor itri publishes a self-service NTRIP
  endpoint reachable from a generic European consumer client (both gate
  access behind direct contact / region-locked DNS).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| ANCFCC RINEX from 60 stations, cadences 1–60 s | https://www.ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/ | Registration required; tariff not published |
| itri RINEX from claimed 231 stations | https://www.itri-gnss.ma/documentation/index.html | Professional subscription; pricing not public |
| IGS / EarthScope archive — RABT (Rabat) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account) |

## Sources Consulted

- ANCFCC GNSS permanent network page (current 60-station description; sandbox
  WebFetch returned 404 2026-05-23, content corroborated via WebSearch
  excerpt): https://www.ancfcc.gov.ma/nos-metiers/cartographie/reseau-gnss/
- ANCFCC ReseauGnss legacy sub-page (18-station view, RINEX only):
  https://www.ancfcc.gov.ma/ReseauGnss/
- itri-gnss.ma homepage: https://itri-gnss.ma/index.html
- itri-gnss.ma coverage page: https://itri-gnss.ma/couverture-geographique.html
- itri-gnss.ma documentation: https://www.itri-gnss.ma/documentation/index.html
- itri-gnss.ma registration: https://secure.itri-gnss.ma/admin/auth/register
- itri-gnss.com (alternate domain): https://www.itri-gnss.com/
- itri Facebook: https://www.facebook.com/itri.gnss/
- ArduSimple Morocco (re-verified 2026-05-23; no national network recommended
  by them): https://fr.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-morocco/
- GeoPrism Maroc: https://geoprism-maroc.com/le-gnss/
- gtopic.net policy analysis (Apr 2022; references ANCFCC and itri as
  existing operators): https://gtopic.net/blog/2022/04/18/stations-de-reference-gnss-actives-et-partenariat-public-prive/
- GeoRezo forum thread on Moroccan permanent stations:
  https://georezo.net/forum/viewtopic.php?id=119022
- ntrip-list.com — no Morocco entries 2026-05-23
- RTK2go monitor (`monitor.use-snip.com`) — 2 Morocco mountpoints visible
  2026-05-23: ProdairLAB, SidiRahal
- Local pipeline check 2026-05-23:
  `py scripts/stations_by_country.py MAR` → igs_ip:1 (RABT00MAR0),
  rtk2go:2 (ProdairLAB, SidiRahal); 0 Centipede; 0 EarthScope.
- Sandbox DNS resolution 2026-05-23: `itri-gnss.ma` / `itri-gnss.com` /
  `www.ancfcc.gov.ma` resolve only from MA-region resolvers; ports return
  ECONNREFUSED outside.
