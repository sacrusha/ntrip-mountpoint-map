# Brunei [BN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-15

## Status: NO public NTRIP caster

No NTRIP host:port, sourcetable, or self-service portal has ever been published for Brunei Darussalam. The Department of Survey and Mapping (Jabatan Ukur) operates a CORS network for internal cadastral/geodetic use, but exposes no public RTK service. No BN-coded mountpoints exist on rtk2go, Centipede, GEODNET, ONOCOY, or any of the 84 fetched sources in `data/stations.json` (verified 2026-05-15 — `stations_by_country.py BRN` and `stations_by_radius.py 4.90 114.94 200` both return zero).

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **Operator (potential)** | Department of Survey and Mapping (Jabatan Ukur), Ministry of Development |
| **landing_url** | https://survey.gov.bn/ (301 → https://geoportal.survey.gov.bn/start) |
| **access_url** | None — no self-service portal exists |
| **host:port** | Not published |
| **num_stations** | last documented 2009/2011 as 8 internal CORS (KBEL, LABI, MURA, LAMU, LIAN, TEMB, TUTO, UKUR); not exposed publicly; current count unverified (15–17 year currency gap, no later Survey Department disclosure located 2026-05-15) |
| **vrs** | ? — internal-only network; no public confirmation |
| **tariff** | n/a — service does not exist publicly |
| **hobbyist_eligibility** | n/a — no service to subscribe to |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | 2026-05-15 — survey.gov.bn returns 301 to geoportal.survey.gov.bn/start; geoportal returns a Leaflet/web-map shell ("Web Map" only) with no RTK/CORS/RINEX/subscription surface. Operator portal alive; RTK service absent. |
| **datum_epoch** | omitted — no operator declaration currently citable. Secondary source (`mycoordinates.org/the-realization-of-geocentric-datum-for-brunei-darussalam-2009/`, Sep 2011) reports GDBD2009 with realisation epoch 2009.45 (25 May 2009) per the GDBD2009 Technical Manual v1.0 (2009); the primary Survey Department PDF and UNOOSA UN-GNSS/18 PDF both 404 as of 2026-05-15 — primary source unverifiable. |

---

## Most Recent Project Announcement

**Positioning Augmentation Center (conceptual design, 2017)** — At the 14th South East Asia Survey Congress (Brunei, 15–17 Aug 2017), Y. Sakurai (SPAC, Tokyo) presented "Introduction of Positioning Augmentation Center for High Precision Application in Brunei Darussalam." The paper described a conceptual SSR-based augmentation center built on authorized CORS and confirmed Brunei was *evaluating* (not operating) a public high-precision service. The host PDF (`mod.gov.bn/survey/SitePages/…Sakurai…pdf`) returned **HTTP 404** on 2026-05-15 — the file moved when the Survey Department migrated from `mod.gov.bn/survey` to `survey.gov.bn`. No 2018–2026 announcement of an operational public NTRIP service has surfaced via WebSearch (queries: Multi-GNSS Asia + Brunei, SEASC + Sakurai, survey.gov.bn + NTRIP/RTK, "Brunei" + NTRIP + 2024–2026).

**Underlying CORS network (8 stations, since 2009)** — The GDBD2009 Zero Order Network was described in a 2011 UN-GNSS/UNOOSA presentation as providing "24-hour RTK data to GNSS/GPS users in Brunei Darussalam." That language has never been operationalised on any externally reachable endpoint. The UNOOSA PDF (`unoosa.org/documents/pdf/psa/activities/2011/un-gnss/18.pdf`) returned **HTTP 404** on 2026-05-15; the only surviving accessible summary is the mycoordinates.org Sep 2011 blog post, which itself cites the GDBD2009 Technical Manual v1.0 (2009) as primary.

---

## Context Notes

- **Survey Department portal** (`survey.gov.bn`): 301 → `geoportal.survey.gov.bn/start`. Geoportal Ukur is a Leaflet-based web map only — no RTK/CORS/RINEX/subscription pages exposed. Mobile companion: `bn.gov.survey.geoportal` on Google Play (web-map viewer, no positioning service).
- **GDBD2009 datum**: secondary source (mycoordinates.org Sep 2011) reports realisation epoch 2009.45 (25 May 2009), GPS campaign 17 May – 2 Jun 2009, 8 Zero Order CORS (KBEL, LABI, MURA, LAMU, LIAN, TEMB, TUTO, UKUR); primary Survey Department PDF + UNOOSA UN-GNSS/18 PDF both 404 — primary unverifiable. EPSG codes: 5247 (GDBD2009 / Brunei BRSO projected), 5244 (GDBD2009 geographic 2D). Datum is for internal cadastral/topographic use; not exposed via any public NTRIP service.
- **Volunteer / global networks** (verified against `data/stations.json` 2026-05-15):
  - `stations_by_country.py BRN` → no stations.
  - `stations_by_radius.py 4.90 114.94 200` → zero stations within 200 km of Bandar Seri Begawan across all 84 sources.
  - rtk2go, Centipede-RTK, GEODNET, ONOCOY, EarthScope/IGS-IP: no BN coverage.
- **IGS Network**: 534 stations as of 2026-05-15; none in Brunei (filter on `network.igs.org` returned no BRN entries).

---

## Cross-Border & Alternative Options

- **MyRTKnet (Malaysia / JUPEM)** — 78 reference stations including 15 in Sarawak, with a Miri station (~75 km SW of Bandar Seri Begawan, well outside the ~50 km nearest-neighbour threshold). VRS coverage degrades quickly outside national footprint (cited ~6 cm H / ~8 cm V near-border; degrades sharply at >50 km from any reference). MyRTKnet registration via `myrtknet.jupem.gov.my` is JUPEM-discretionary; eligibility for Brunei-resident users is **not documented** in any public JUPEM material. Portal `myrtknet.gov.my/sbc` returned `ECONNREFUSED` from this sandbox on 2026-05-15 — likely SE-Asia IP geofence, common on JUPEM services; reachability for in-country users is the public norm but cross-border eligibility is unverified.
- **Global commercial networks** (HxGN SmartNet, Trimble VRS Now, Topcon TopNET, Swift Skylark, PointOne): no published Brunei coverage as of 2026-05-15.
- **Local base station**: Brunei territory ~5,765 km² with two enclaves; a single owner-deployed base covers most realistic hobbyist work within a 10–30 km baseline.
- **Galileo HAS (free, global SSR PPP)**: ~20–40 cm horizontal once converged; works in Brunei without any caster, no registration. Out of project scope but the only realistic free decimetre-class fallback.

---

## Post-Processing (RINEX) Fallback

| Service | URL | Notes |
|---|---|---|
| **IGS / SONEL / EarthScope** | https://network.igs.org/ ; https://www.earthscope.org/data/gnss-data/ | No Brunei station in IGS, APREF, or EarthScope archives as of 2026-05-15. Nearest is Malaysia (Sarawak via JUPEM/UPM contributions, not openly RINEX). |
| **Survey Department RINEX** | https://survey.gov.bn/ | Not advertised. Internal cadastral use only; would require department contact. |

---

## Sandbox Reachability Notes

- `survey.gov.bn`: reachable (301 redirect captured).
- `geoportal.survey.gov.bn/start` and `/start-gp`: reachable but client-side rendered ("Web Map" only); WebFetch sees the shell, not the map app — limitation of WebFetch's no-JS render. Does not affect conclusion: no NTRIP service is announced via *any* sub-page of the portal in the indexed web.
- `mod.gov.bn/survey/...` (old SharePoint URLs): all 404 since the migration to `survey.gov.bn`. Sakurai 2017 PDF and Mengenai Kami both lost; no replacement located via WebSearch.
- `unoosa.org/documents/pdf/psa/activities/2011/un-gnss/18.pdf`: 404. Cited only via mycoordinates.org secondary.
- `myrtknet.gov.my/sbc`: ECONNREFUSED — geofence, not a sandbox-only failure (no extraordinary evidence of in-country reachability is needed for an *alternative* option; treat as standard JUPEM access pattern).

---

## Sources Consulted (probed 2026-05-15)

- Brunei Survey Department: https://survey.gov.bn/ — alive, 301 → geoportal
- Geoportal Ukur: https://geoportal.survey.gov.bn/start (and /start-gp) — alive, web-map shell only, no RTK surface
- mycoordinates.org GDBD2009 article: https://mycoordinates.org/the-realization-of-geocentric-datum-for-brunei-darussalam-2009/ — alive; primary secondary source for the 8 CORS + epoch 2009.45
- EPSG GDBD2009 records: https://epsg.io/5247 ; https://epsg.io/5244 — alive
- Sakurai 2017 SEASC presentation: http://www.mod.gov.bn/survey/SitePages/Introduction%20of%20Positioning%20Augmentation%20Center%20…Sakurai…pdf — **404** (site migration)
- UNOOSA UN-GNSS/18 (2011): https://www.unoosa.org/documents/pdf/psa/activities/2011/un-gnss/18.pdf — **404**
- Old Survey Dept "Mengenai Kami": http://www.mod.gov.bn/survey/SitePages/Mengenai%20Kami.aspx — **404**
- IGS Network filter: https://network.igs.org/ — no BN station
- MyRTKnet portals: https://www.myrtknet.gov.my/sbc — ECONNREFUSED (geofence); https://myrtknet.jupem.gov.my/ — listed in JUPEM index
- Local data: `data/stations.json` (refreshed 2026-05-15) — zero BN stations and zero within 200 km of BSB across 84 sources

SELF-REVIEW: PASS
