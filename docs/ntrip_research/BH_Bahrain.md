# Bahrain [BH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: YES — SLRB PRN (Permanent Reference Network) is FREE for registered users; covers entire kingdom; access by email application

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (registration required; free) |
| **Network name** | PRN — Permanent Reference Network |
| **Operator** | Survey & Land Registration Bureau (SLRB), Kingdom of Bahrain |
| **landing_url** | https://www.slrb.gov.bh/en/permanent-reference-networkprn |
| **access_url** | https://www.slrb.gov.bh/en/permanent-reference-networkprn |
| **host:port** | Not publicly advertised; issued in credentials email after application approval |
| **num_stations** | not disclosed by SLRB |
| **vrs** | ? |
| **tariff** | Free of charge (observed 2026-05-15 at SLRB PRN subscription page). Exact site text: "*Kindly note that this service may incur charges in the future." No tier structure; no VAT applicable. |
| **hobbyist_eligibility** | yes — application form accepts both "Individual" and "Agent" applicant types; no licensed-surveyor requirement stated in public terms |
| **legal_residency_required** | ? — not stated as a hard requirement in the public terms; mailing address on the application form supports both local and foreign applicants in principle. Practical screening at SLRB's discretion. |
| **last_confirmed_alive** | 2026-05-15 — SLRB PRN subscription page (slrb.gov.bh/en/permanent-reference-networkprn) returned the live PRN page; application form PDF (filename-dated 15062025, i.e. 15 June 2025, DDMMYYYY) downloadable; processing time stated as 1–2 working days |
| **datum_epoch** | omitted — no citable URL with an explicit PRN datum+epoch declaration. Bahrain historically uses *Ain el Abd 1970* (EPSG:4204; Hayford 1909 ellipsoid) for cadastral work; PRN realisation frame is a documented research gap — not declared on any accessible SLRB page (2026-05-15). |

---

## Service Details

### Application Process

1. Download the **GPS Network Application Form** (PDF, linked on the SLRB PRN subscription page; file dated 2025-06-15).
2. Send the completed form together with a covering letter to **PRN@slrb.gov.bh**.
3. SLRB issues credentials within **1–2 working days**.
4. Use of access permission is limited to **one device per credential**; sharing is prohibited per the published Terms & Conditions.

### Coverage & Availability

- Service available **24/7** to the entire Kingdom (~765 km²).
- SLRB does not disclose the number or location of physical CORS in the PRN. Single-station coverage of the whole kingdom is technically feasible at <30 km baselines.

### Technical Specifications

NTRIP host:port, mountpoint names, RTCM versions, VRS type, and supported constellations are **not published on the public SLRB website**. They are issued only in the credentials email after approval.

### Contact

- **Email**: PRN@slrb.gov.bh (preferred) or info@slrb.gov.bh
- **Phone**: +973 17507000
- **Address**: Building 517, Road 1010, Manama 410, Kingdom of Bahrain

---

## Volunteer / Community Coverage

- **rtk2go**: zero BH-coded mountpoints (verified `data/stations.json` 2026-05-15).
- **Centipede-RTK**: zero BH nodes.
- **EarthScope / IGS-IP**: no BH stations.
- **Bounding-box scan** of 25°–27°N, 49°–52°E (entire Bahrain + adjacent Saudi/Qatar coastline) across all 84 fetched sources in `data/stations.json`: **0 results**. SLRB PRN is therefore the only realistic free RTK path in or near Bahrain.

---

## Cross-Border & Alternative Options

- **KSA-CORS spill (Saudi Arabia)**: KSA-CORS stations near Dammam / Al-Ahsa are ~25–50 km from Bahrain Island and *may* provide marginal RTK in the northern Manama / Muharraq area, but KSA-CORS is reachability-restricted (non-SA IPs are typically blocked at portal level — see `SA_SaudiArabia.md`). With SLRB PRN free, this fallback is no longer needed.
- **Commercial global networks** (GEODNET, PointOne, HxGN SmartNet, ONOCOY, Swift Skylark): no public documentation lists Bahrain coverage as of 2026-05.
- **Galileo HAS (PPP, free, global)**: ~20–40 cm horizontal once converged; works in Bahrain with no caster connectivity. Useful where RTK is unavailable.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Notes |
|---|---|---|
| **SLRB PRN RINEX** | https://www.slrb.gov.bh/en/permanent-reference-networkprn | Likely available to subscribers; not publicly documented as a separate product. Contact required. |
| **IGS — BAHR (decommissioned)** | https://sonel.org/spip.php?idStation=633&page=gps | NGA-operated, Manama (26.209°N, 50.608°E); operated 1995-03-20 to 2008-09-16. Historical RINEX only. |
| **IGS — BHR4 (replacement)** | https://sonel.org/spip.php?idStation=3613&page=gps | NGA co-located continuation site at the same location; data products via CDDIS/SONEL. No NTRIP stream. |
| **EarthScope** | https://www.earthscope.org/data/gnss-data/ | No active station in Bahrain. |

---

## Key Caveats

- SLRB does not publish NTRIP technical parameters (host:port, mountpoints, RTCM, VRS confirmation, datum+epoch) on its public website. All such fields are issued post-approval. Treat the "Yes" status as confirmed for **eligibility and free access**, but treat the protocol details as **opaque until subscribed**.
- The wording "this service may incur charges in the future" has been on the SLRB page since at least 2024 with no observed change; no pricing has been announced as of 2026-05-15.
- Bahrain's last open IGS station (BAHR, NGA) was decommissioned in 2008; the replacement BHR4 is NGA-operated and not part of any public NTRIP feed.

---

## Sources Consulted (2026-05-15)

- SLRB PRN subscription page: https://www.slrb.gov.bh/en/permanent-reference-networkprn — WebFetch confirmed: free of charge, application via PRN@slrb.gov.bh, 1–2 day processing, 24/7, single-device clause, form PDF dated 2025-06-15
- SLRB Products & Services: https://www.slrb.gov.bh/en/products-and-services — PRN listed under Topographic Survey
- SLRB E-Services: https://www.slrb.gov.bh/en/e-services
- ArduSimple Bahrain NTRIP page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kingdom-of-bahrain/ — confirms PRN as free national service; no host:port published
- SONEL BAHR station record: https://www.sonel.org/spip.php?page=gps&idStation=633 — decommissioned 2008-09-16
- SONEL BHR4 station record: https://sonel.org/spip.php?idStation=3613&page=gps — current NGA co-located site
- EPSG codes for Bahrain (Ain el Abd, WGS 84, ITRF2020): https://epsg.io/?q=Bahrain
- `data/stations.json` (updated 2026-05-15T16:22Z): bounding-box and per-source verification — zero free public NTRIP stations within 150 km of Manama on any of the 84 tracked sources
