# Bahrain [BH] — NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Summary

One free government NTRIP service — SLRB Permanent Reference Network (PRN),
operated by the Survey & Land Registration Bureau, available to both
Individual and Agent applicants by email application with credentials
issued in 1–2 working days. Application surface lives on the SLRB site;
caster host:port, mountpoint names, RTCM versions, and per-station
inventory are not published — they are issued in the credentials email
after approval. The kingdom is small (~765 km²) and a single well-sited
base covers most of it at <30 km baselines. SLRB notes the service "may
incur charges in the future" but no pricing has been announced through
2026-05-23.

No rtk2go / Centipede / EarthScope / IGS-IP / federated mountpoint is
visible in BH 2026-05-23. The Bahrain legacy IGS site BAHR was
decommissioned 2008; its NGA replacement BHR4 does not feed any public
NTRIP stream.

## Casters

### SLRB PRN — Permanent Reference Network

- operator: Survey & Land Registration Bureau (SLRB), Kingdom of Bahrain
- landing_url: https://www.slrb.gov.bh/en/permanent-reference-networkprn
  (ArduSimple's BH page cites an older InformationCenter URL —
  `slrb.gov.bh/InformationCenter/GeneralInfoDetail/?PageId=942&ChnlId=63&ChnlId2=62`
  — which now 404s 2026-05-23; the current entry point is the
  `/en/permanent-reference-networkprn` slug above)
- access_url: https://www.slrb.gov.bh/en/permanent-reference-networkprn
  (same page hosts the application form PDF and the contact email
  PRN@slrb.gov.bh)
- access_type: free-signup — SLRB states *"Kindly note that this service
  may incur charges in the future"* implying free now; one-device-per-
  credential terms; processing 1–2 working days (WebFetch 200 2026-05-23)
- coverage: full Kingdom of Bahrain (~765 km²); SLRB describes the
  service as available "24 hours a day, seven days a week" to the whole
  kingdom
- num_stations: not published — SLRB does not disclose the number or
  location of physical CORS in the PRN (checked: slrb.gov.bh PRN page
  2026-05-23 via WebFetch — technical infrastructure details not
  disclosed; ArduSimple Bahrain page 2026-05-23 via WebFetch — confirms
  free national service, no host:port published). Single-station
  coverage of the whole kingdom is technically feasible at <30 km
  baselines.
- hobbyist_eligibility: yes — application form accepts both "Individual"
  and "Agent" applicant types; no licensed-surveyor requirement stated
  in public terms
- residency_required: ? — not stated as a hard requirement in the public
  terms; the mailing-address field on the form does not enforce a BH
  postal code and Individual applicants are accepted in principle
  (checked: slrb.gov.bh PRN page 2026-05-23 WebFetch — eligibility
  Individual + Agent, no nationality clause; ArduSimple Bahrain page
  2026-05-23 WebFetch — same)
- sourcetable: omitted — SLRB does not publish a host:port. Nothing to
  curl. No DNS A record for `prn.slrb.gov.bh` 2026-05-23 (negative
  resolve); host is issued post-approval in the credentials email.
- vrs: ? — SLRB describes the system as a "Permanent Reference Network"
  delivering real-time high-precision positioning; mode (single-base /
  VRS / MAC) is not explicitly stated in any public material (checked:
  slrb.gov.bh PRN 2026-05-23 WebFetch; ArduSimple Bahrain 2026-05-23
  WebFetch; SLRB Topographic Survey directorate page 2026-05-23 via
  WebSearch)
- stations_source: omitted — no public station list. The application
  form PDF is the only document and lists no station inventory.
- datum_epoch: omitted — no citable URL with an explicit PRN datum +
  epoch declaration. Bahrain historically uses *Ain el Abd 1970*
  (EPSG:4204; Hayford 1909 ellipsoid) for cadastral work; the PRN
  realisation frame is not declared on any accessible SLRB page.

Application process:
1. Download the GPS Network Application Form (PDF linked from the SLRB
   PRN page; file dated 2025-06-15).
2. Email the completed form together with a covering letter to
   `PRN@slrb.gov.bh`.
3. SLRB issues credentials within 1–2 working days.
4. Use is limited to one device per credential; sharing is prohibited.

Contact: PRN@slrb.gov.bh (preferred), info@slrb.gov.bh; +973 17507000;
Building 517, Road 1010, Manama 410, Kingdom of Bahrain.

## Disqualified / not applicable

- **rtk2go, Centipede, EarthScope, IGS-IP** — 0 BH-coded mountpoints
  2026-05-23 (`py scripts/stations_by_country.py BHR` → "No stations for
  'BHR'"). `py scripts/stations_by_radius.py 26.2 50.6 200` → no
  stations within 200 km of Manama on any tracked source.
- **GEODNET, onocoy, PointOne, HxGN SmartNet, Trimble VRS Now, Swift
  Skylark** — no Bahrain coverage advertised 2026-05-23.
- **KSA-CORS cross-border** — Saudi CORS in the Dammam / Al-Ahsa
  corridor sit ~25–50 km from Bahrain Island; KSA-CORS is IP-gated to
  non-SA addresses (see `SA_SaudiArabia.md`) so unusable in practice
  from a Bahrain IP. With SLRB PRN free, no need to rely on this.
- **BAHR (legacy IGS)** — NGA-operated Manama site (26.21, 50.61);
  operated 1995-03-20 to 2008-09-16; decommissioned, historical RINEX
  only. Replacement BHR4 is NGA co-located at the same location; data
  via CDDIS/SONEL; no NTRIP stream.

## Post-Processing (RINEX) fallback

| Service | URL | Notes |
|---|---|---|
| SLRB PRN RINEX | https://www.slrb.gov.bh/en/permanent-reference-networkprn | Likely available to subscribers; not separately advertised as a product. Contact required. |
| SONEL — BAHR (decommissioned) | https://sonel.org/spip.php?idStation=633&page=gps | Historical 1995-2008 RINEX only |
| SONEL — BHR4 (current NGA co-located) | https://sonel.org/spip.php?idStation=3613&page=gps | RINEX via CDDIS/SONEL; no NTRIP |
| EarthScope / IGS | https://www.earthscope.org/data/gnss-data/ | Free non-commercial; no active station in Bahrain |

## Sources Consulted

- SLRB PRN subscription page (WebFetch 200 2026-05-23 — confirmed free
  of charge, application via PRN@slrb.gov.bh, 1–2 day processing, 24/7,
  Individual + Agent eligibility, single-device clause, form PDF dated
  2025-06-15):
  https://www.slrb.gov.bh/en/permanent-reference-networkprn
- SLRB Products & Services:
  https://www.slrb.gov.bh/en/products-and-services
- SLRB Topographic Survey Directorate (Permanent GNSS Reference Network
  is managed here): https://www.slrb.gov.bh/about/DirectorateDetails/?PageId=82&ChnlId=59&PageId2=20&ChnlId2=56
- SLRB E-Services: https://www.slrb.gov.bh/en/e-services
- ArduSimple Bahrain NTRIP page (confirms PRN as free national service;
  no host:port published; WebFetch 200 2026-05-23):
  https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kingdom-of-bahrain/
- SONEL BAHR station record:
  https://www.sonel.org/spip.php?page=gps&idStation=633
- SONEL BHR4 station record:
  https://sonel.org/spip.php?idStation=3613&page=gps
- EPSG codes for Bahrain (Ain el Abd, WGS 84, ITRF2020):
  https://epsg.io/?q=Bahrain
- Negative DNS probe 2026-05-23 of `prn.slrb.gov.bh:2101` →
  "Could not resolve host" (no PRN subdomain advertised in DNS).
- Local data 2026-05-23: `py scripts/stations_by_country.py BHR` →
  no stations; `py scripts/stations_by_radius.py 26.2 50.6 200` →
  no stations within 200 km of Manama.
