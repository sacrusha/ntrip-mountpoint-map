# Free RTK NTRIP — small territories survey

_Research for Malta (MT) and Macao (MO). Format follows `docs/country-survey.md`._
_Findings based on local data in `data/stations.json` and cached sourcetables._
_Date: 2026-04-21._

---

## Europe — Southern (territories)

### MT — Malta

- **Free government RTK**: none confirmed. The Malta Environment and Planning
  Authority (MEPA, now MCESD/PA) and the Land Registry do not operate a public
  NTRIP caster. No national CORS network with public NTRIP has been identified
  through Alberding directory or EUREF listings.
- **Volunteer**: rtk2go 1 base — `EneGIS` at Naxxar (35.92°N, 14.44°E), RTCM
  3.2 MSM, carrier L1+L2, country code `MLT`. Single station covering the
  Maltese archipelago; baseline to Gozo ~25 km (marginal RTK range). No
  Centipede nodes detected in Malta bounding box.
- **Gap**: one rtk2go volunteer base is the only free RTK option for the entire
  archipelago (Malta + Gozo + Comino, ~316 km²). Coverage is practical for
  Malta island; Gozo is at the edge of a single-base baseline. No government
  network, no VRS. Nearest government NTRIP is ERGNSS (ES, ~1,700 km) or APOS
  (AT, ~1,400 km) — both useless at that range.
- **Closest paid alternative**: commercial surveying networks in Italy
  (NetGEO/TopNET ~€360/yr) offer no Malta coverage. GEODNET EU node density
  for Malta is unknown; worth checking if a node exists on the island.

---

## Asia Pacific — East Asia (special administrative regions)

### MO — Macao SAR (China)

- **Free government RTK**: none confirmed with a public NTRIP endpoint. The
  Cartography and Cadastre Bureau (DSCC / Direcção dos Serviços de Cartografia
  e Cadastro) operates reference stations but does not publish a public NTRIP
  caster. No Macao entry found in Alberding directory, EUREF listings, or any
  cached sourcetable.
- **Adjacent network — SatRef (HK)**: Hong Kong SatRef
  (`ntrip.geodetic.gov.hk:2101`, free with email registration) has three
  stations within practical range of Macao:
  - `HKCL_32`: 22.30°N, 113.91°E — ~40 km from Macao peninsula
  - `HKNP_32`: 22.25°N, 113.89°E — ~37 km from Macao peninsula
  - `HKSL_32`: 22.37°N, 113.93°E — ~45 km from Macao peninsula

  These baselines (37–45 km) are at the edge of reliable single-base RTK
  (~30–40 km practical limit for cm-level accuracy). VRS from SatRef would
  reduce effective baseline to ~10–15 km and is the more reliable option; VRS
  mountpoint `VRS32G` covers all of Hong Kong and potentially reaches Macao.
  Whether SatRef's NRTK VRS engine extends its virtual reference points to
  Macao coordinates is not confirmed — depends on server-side polygon extent.
  → networks.md: `satref`
- **Volunteer**: no rtk2go or Centipede stations in the Macao bounding box
  (22.0–22.2°N, 113.5–113.6°E). Macao is a ~32 km² peninsula/island cluster;
  the volunteer station density for such a small urban enclave is effectively zero.
- **Gap**: Macao hobbyists have no local free RTK. The most practical path is
  SatRef (HK) VRS — free, requires email registration, and the VRS virtual
  reference is compute-generated at the rover's reported position, so it may
  extend to Macao coordinates if the server polygon covers it. Mainland China's
  Qianxun (¥3,600–3,800/yr) and provincial CORS networks are restricted to
  licensed surveyors under Surveying and Mapping Law 2017 — not a hobbyist path.
  GEODNET has nodes in the Pearl River Delta; the $40/month tier (~$160 for
  4-month season) is under the $200/yr cutoff.
