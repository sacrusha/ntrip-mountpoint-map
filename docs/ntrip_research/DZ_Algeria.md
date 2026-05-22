# Algeria [DZ] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

Algeria has one operational national CORS network (AL-CORS-Net / SAAP), but it
is restricted: no public registration portal, no published tariff, no
advertised NTRIP host:port. Operated by INCT under the Ministry of National
Defence, with civilian access only through direct institutional contact. No
free public alternative exists in-country; no commercial third-party RTK
provider has confirmed Algeria coverage.

## Casters

### AL-CORS-Net / SAAP — restricted national NRTK

- operator: Institut National de Cartographie et de Télédétection (INCT),
  Ministry of National Defence
- landing_url: http://inct.mdn.dz/ (institutional portal; SSL warnings and
  ECONNREFUSED reconfirmed 2026-05-23; INCT GPS sub-page
  http://www.inct.mdn.dz/site_anglais/source/gps lists the original 6-station
  anchor set but no public NTRIP endpoint)
- access_url: no public signup / conditions page exists. Access negotiated by
  direct contact only: contact@inct.dz / inct@mdn.dz / +213 23 79 50 26.
- access_type: restricted — operated under the Ministry of National Defence;
  no self-service civilian onboarding documented
- coverage: nationwide, North + South subdivisions. Anchor stations: Algiers
  (DZAL), Oran (DZOR), Constantine (DZCO), Ouargla (OGLA), Béchar (BECH),
  Tindouf (TIND). Documented in INCT publications and Takka et al. 2023.
- num_stations: 189 permanent stations (cited in Takka et al. 2023,
  "Assessment of VRS performances of the Algerian-CORS-Network",
  https://asjp.cerist.dz/en/article/216928, and in INCT documentation). The
  same article confirms VRS sessions ran live Oct 2021 – Jan 2022 with ~1.3 cm
  horizontal / ~2.2 cm vertical precision (1σ); 97.25 % VRS availability;
  98.8 % horizontal, 94.9 % vertical integrity.
- hobbyist_eligibility: no — operator is the national mapping institute of
  the Defence Ministry; no hobbyist tier or civilian onboarding path
  published. The "no" is de-facto, not a written prohibition.
- residency_required: ? — undocumented; access is by negotiated institutional
  request, residency may be implicit.
- datum_epoch: omitted — INCT portal unreachable for direct citation; AL-CORS
  paper is not an operator portal / spec / decree.

Backend: Geo++ GNSMART (Network RTK / VRS over NTRIP), per Takka et al.

### REGAT — disqualified, not RTK

REGAT (*REseau Géodésique de l'ATlas*) — 53 continuously-recording GPS
stations operated by CRAAG (Centre de Recherche en Astronomie, Astrophysique
et Géophysique). Geographic scope is the Algerian Atlas (coastal margin
spanning the country's width, reaching ~300 km inland, plus one Tamanrasset
site in the deep south); inter-site spacing ~100 km. Built for crustal-
deformation / seismotectonic monitoring of the Nubia-Eurasia plate boundary
following the 2003 Boumerdes earthquake; no real-time RTK service dispensed.
Sources: Yelles-Chaouche et al., "REGAT: A permanent GPS network in Algeria,
configuration and first results" (https://pmc.ncbi.nlm.nih.gov/articles/PMC6460426/);
CRAAG https://www.craag.dz/index.php/reseau-geodesique/.

### Commercial / global

No commercial RTK provider (Trimble VRS Now, Leica SmartNet, Topcon TopNET
Live, Hexagon, GEODNET, onocoy, Point One) has confirmed Algeria coverage as
of 2026-05.

### Volunteer / community

`py scripts/stations_by_country.py DZA` → zero rtk2go, Centipede, or
EarthScope entries (verified 2026-05-23). IGS-IP / EUREF-IP cached
sourcetables likewise contain zero DZ-coded stations (checked:
`data/igs_ip.sourcetable` 2026-05-23; `data/euref_ip.sourcetable` 2026-05-23 —
Algiers / DZAL appears in historical IGS RINEX archives but is not exposed on
the real-time IGS / EUREF NTRIP caster). ArduSimple Algeria page states
explicitly there is no national RTK network it can recommend; it lists only
rtk2go, IGS, EarthScope as generic global alternatives, but none has Algeria
stations.

## Practical recommendation

Hobbyist options inside Algeria today: contact INCT directly to request
AL-CORS-Net access (uncertain availability for individuals); deploy a private
base for single-base RTK; or use Galileo HAS / Trimble RTX / PPP for
decimetre-to-sub-metre accuracy without a national-caster account.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| IGS / CDDIS — sparse scientific stations in DZ; nearest dense coverage in TN/MA | https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/ | Free (NASA Earthdata account) |

## Sources Consulted

- INCT institutional page (SSL broken; ECONNREFUSED 2026-05-23):
  http://www.inct.mdn.dz/
- INCT GPS sub-page (lists 6 anchor stations):
  http://www.inct.mdn.dz/site_anglais/source/gps
- INCT SAAP page (re-verified link 2026-05-23, TLS cert error returned by
  asjp.cerist.dz mirror): http://www.inct.mdn.dz/source/act-saap.php
- Takka Elhadi, Touabet Touabet, Boudrassene Abdennour, "Assessment of VRS
  performances of the Algerian-CORS-Network" (survey Oct 2021 – Jan 2022;
  published 2023): https://asjp.cerist.dz/en/article/216928
- ArduSimple Algeria: no national RTK network listed —
  https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-algeria/
- GIM International CORS Africa map:
  https://www.gim-international.com/content/article/developing-a-fully-fledged-cors-map-for-africa
- RTK2GO, ntrip-list.com/africa/, corsstations.com — no DZ entries observed
  2026-05-23
- Local pipeline check 2026-05-23:
  `py scripts/stations_by_country.py DZA` → no entries
- GEODNET, onocoy, Trimble VRS Now, SmartNet, Topcon TopNET Live — no DZ
  coverage confirmed
