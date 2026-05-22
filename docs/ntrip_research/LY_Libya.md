# Libya [LY] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status

No active public NTRIP RTK caster identified for Libya. Civil-conflict-induced
institutional fragmentation since 2011 has prevented deployment of a national
CORS network. No public, semi-public, or volunteer caster confirmed alive.

## Disqualified / non-existent candidates

### Libyan national CORS (nominal, not realised)

- operator: nominally the General Authority for Information and Communication
  Technology (GAICT) and the National Centre for Remote Sensing and Space
  Sciences (NCRSSS); no operational owner
- landing_url: none (no operator-owned page advertises a CORS / NTRIP service)
- access_url: n/a
- access_type: n/a — service does not exist
- coverage: none
- num_stations: 0 confirmed
- hobbyist_eligibility: no — no service exists
- datum_epoch: omitted — no operator declaration to cite

No formal announcement of a Libyan national NTRIP / RTK caster has been located
in development-bank, UN, or geospatial-press sources. Targeted web searches in
English and Arabic (2026-05) return no announcement, sourcetable, or operator
portal. Libya does not appear in the AFREF reference-frame station coverage
maps maintained by the AFREF Technical Working Group (checked:
afrefdata.org search 2026-05-23; UNECA AFREF status reports 2026-05-23 — no
LY-coded permanent stations listed).

### Cross-border options (out of useful range)

OTC GNSS (Tunisia, paid; covered in `TN_Tunisia.md`) and Egypt's ESA CORS
(restricted; covered separately) are the closest national networks. Public
international rebroadcasts (EUREF-IP, IGS-IP, sicilianet, rtk2go, Centipede)
are accessible from Libyan IPs but their nearest stations sit on Lampedusa /
Malta / Sicily / Crete. From Tripoli the closest pipeline entries are
LAMP00ITA0 (Lampedusa, ~294 km) and EneGIS (Malta, ~355 km); from Benghazi the
closest is GVDG00GRC0 (Crete, ~481 km). All exceed the ~30 km useful range of
single-base RTK and sit well outside any NRTK hull, so they silently
extrapolate to dm–m errors with no warning.

### Volunteer / community casters

- `py scripts/stations_by_country.py LBY` — no entries on rtk2go, Centipede,
  EarthScope, igs_ip, or euref_ip (verified 2026-05-23).
- `py scripts/stations_by_radius.py 26.0 17.0 500` returns zero stations
  within 500 km of central Libya across the pipeline.
- igs_ip / euref_ip sourcetable inspection: zero LBY-coded stations
  (checked: `data/igs_ip.sourcetable` 2026-05-23;
  `data/euref_ip.sourcetable` 2026-05-23).

### Commercial global networks

GEODNET, onocoy, Point One, Trimble VRS Now, and SmartNet publish no LY
coverage as of 2026-05.

## Practical recommendation

Hobbyist options inside Libya today: deploy a private base station for
single-base RTK over short baselines, or use Galileo HAS / Trimble RTX / Fugro
StarFix PPP-class corrections for decimetre-to-sub-metre accuracy without a
local caster.

## Sources Consulted

- ArduSimple country selector — Libya not listed
  (https://www.ardusimple.com/rtk-correction-services-in-your-country/)
- AFREF literature on African CORS coverage gaps
- BKG NTRIP streams / EUREF — no LY entries
- RTK2GO monitor (`monitor.use-snip.com`) — no LY mountpoints
- ntrip-list.com Africa — no LY entries
- GEODNET, onocoy, Point One — no LY coverage advertised
- Geospatial Libya (private consultancy, no CORS):
  https://geospatiallibya.ly/en/our-services/
- Local pipeline check (2026-05-23):
  `py scripts/stations_by_country.py LBY` → no entries;
  `py scripts/stations_by_radius.py 26.0 17.0 500` → 0 stations
