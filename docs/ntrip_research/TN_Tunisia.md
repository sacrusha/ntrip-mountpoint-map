# Tunisia [TN] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

OTC GNSS is the sole national NTRIP caster. Paid subscription only; published
tariff in TND from 60 TND/day to 6 000 TND/yr. No free national alternative.
Cheapest cm-accurate option is OTC's 60 TND/day day pass. No free volunteer or
academic caster in Tunisia; cross-border free options are out of reliable RTK
range.

## Casters

### OTC GNSS — paid national NRTK

- operator: Office de la Topographie et du Cadastre (OTC), Ministère de
  l'Équipement et de l'Habitat
- landing_url: https://www.otc.nat.tn/geodesy/gnss
- access_url: https://www.otc.nat.tn/geodesy/gnss/subscription
- access_type: paid
- coverage: 23 permanent stations across Tunisia, **excluding the Saharan
  south** (roughly south of the Gafsa / Tozeur latitude). Initial deployment
  2005 (Tunis, Monastir, Sfax); full 23-station network operational since 2011
  (https://www.otc.nat.tn/geodesy/gnss). Operator advertises Network RTK
  ("permettant de s'affranchir des stations de base mobiles").
- num_stations: 23 physical CORS (operator-declared,
  https://www.otc.nat.tn/geodesy/gnss). Each station carries a met sensor
  (temperature, pressure, humidity), GSM modem, UHF radio, tilt-meter.
- tariff (observed 2026-05-23,
  https://www.otc.nat.tn/geodesy/gnss/subscription; VAT applicability not
  stated on page):
  - 60 TND / 1 day
  - 480 TND / 15 days
  - 840 TND / 30 days
  - 2 400 TND / 3 months
  - 3 600 TND / 6 months
  - 4 800 TND / 9 months
  - 6 000 TND / 12 months
  - Each tier requires downloading a "document requis" before commercial
    department issues NTRIP credentials.
- hobbyist_eligibility: ? — operator pages enumerate only institutional /
  professional client categories (OTC departments, AFA, SONEDE, STEG, ONAS,
  Telecom, private surveyors); no individual / hobbyist tier is explicitly
  named. Subscription page lists tariffs with no published eligibility text,
  and "no exclusion of individuals is published" is negative evidence, not
  confirmation. Day-pass at 60 TND (~$21) is priced for experimentation if
  individuals can sign up — verifiable only by direct contact with the
  Direction Commerciale (checked: otc.nat.tn/geodesy/gnss 2026-05-23;
  otc.nat.tn/geodesy/gnss/subscription 2026-05-23).
- datum_epoch: ITRF2000 — operator declares *"Le réseau de stations GNSS de
  l'OTC est rattaché au système mondial WGS84 - ITRF 2000"*
  (https://www.otc.nat.tn/geodesy/gnss). Epoch not stated on operator pages.
  This is the RTK correction frame. The classical cadastral datum NTT
  (Nouvelle Triangulation Tunisienne, Clarke 1880 ellipsoid, UTM Zone 32 North
  projection; established by Arrêté du 10 February 2009 of the Minister of
  National Defence, https://www.otc.nat.tn/geodesy/ntt) is a separate legacy
  frame used for cadastral coordinates, not for RTK corrections.
- sourcetable: not on `otc.nat.tn:2101` — TCP connect timed out on probes
  2026-05-06, 2026-05-13, 2026-05-17, and reconfirmed unreachable 2026-05-23
  (caster hostname/port not exposed publicly; actual host distributed
  post-subscription with credentials).
- vrs: yes — operator describes Network-RTK service explicitly.
- residency_required: no — no published residency restriction; service is
  Tunisia-focused but no overseas exclusion documented.
- stations_source: operator-described station list and station-count is on
  https://www.otc.nat.tn/geodesy/gnss; no public map. Sourcetable not
  externally reachable.

Contact (Direction Commerciale): +216 71 771 100 ext. 301 / +216 71 891 477
ext. 301; fax +216 71 770 448; d.commerciale@otc.nat.tn.

### Cross-border free options (disqualified for mainland Tunisia)

`py scripts/stations_by_radius.py 36.8 10.18 600` (2026-05-23):

- Italy / Sicily — sicilianet, gnss_campania, euref_ip, centipede, rtk2go,
  igs_ip clusters; nearest station ~278 km from Tunis (FM01 / Sicily).
  Baseline >250 km kills single-base RTK; NRTK extrapolates silently outside
  hull.
- Malta — EneGIS on rtk2go (~394 km from Tunis). Sea-only line, beyond NRTK
  hull.

These are not viable substitutes for OTC inside Tunisia.

### Volunteer / community

- rtk2go: zero TUN-coded entries (verified 2026-05-23,
  `py scripts/stations_by_country.py TUN`).
- Centipede: zero TUN entries.
- EarthScope NOTA: no TUN public real-time stations.
- IGS-IP / EUREF-IP: zero TUN-coded stations in either cached sourcetable
  (checked: `data/igs_ip.sourcetable` 2026-05-23;
  `data/euref_ip.sourcetable` 2026-05-23). TUNIS appears in historical IGS
  RINEX archives but is not present on the IGS / EUREF NTRIP caster.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| OTC GNSS delayed-mode RINEX from 23 stations | https://www.otc.nat.tn/geodesy/gnss | Same OTC subscription |
| IGS / EarthScope archive — TUNIS historical RINEX | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account) |

## Sources Consulted

- OTC GNSS page (re-verified 2026-05-23): https://www.otc.nat.tn/geodesy/gnss
- OTC subscription page, full tariff table re-verified 2026-05-23:
  https://www.otc.nat.tn/geodesy/gnss/subscription
- OTC geodetic networks page: https://www.otc.nat.tn/geodesy/networks
- OTC NTT page (re-verified 2026-05-23, decree 10 Feb 2009 confirmed):
  https://www.otc.nat.tn/geodesy/ntt
- OTC missions page: https://otc.nat.tn/mission
- ArduSimple Tunisia (lists OTC + rtk2go + IGS + Earthscope; no other
  Tunisian operator named): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-tunisia/
- ResearchGate / academia.edu — NTT documentation confirming ITRF2000 tie and
  2009 decree
- ntrip-list.com — no Tunisia entries found 2026-05-23
- RTK2go monitor (`monitor.use-snip.com`) — no Tunisia mountpoints
- Local pipeline check 2026-05-23:
  `py scripts/stations_by_country.py TUN` → no entries;
  `py scripts/stations_by_radius.py 36.8 10.18 600` lists Sicilian / Maltese
  clusters as nearest stations (>278 km).
