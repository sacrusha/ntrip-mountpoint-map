# Kuwait [KW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06; reverified 2026-05-17 (no new public endpoint surfaced; stations_by_country.py KWT = 0; paci.gov.kw/en ECONNREFUSED on WebFetch attempt, fetched 2026-05-17 -- may be sandbox-only; no open-access policy change)

## Status: NO confirmed public NTRIP caster; government CORS exists (14 stations, joint PACI / Kuwait Municipality); access restricted to licensed firms; no policy change found in 2025–2026

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No confirmed public endpoint |
| **landing_url** | https://www.paci.gov.kw/en (PACI — Public Authority for Civil Information, joint CORS operator with Kuwait Municipality; sandbox WebFetch ECONNREFUSED 2026-05-17, may be IP-restricted) |
| **access_url** | Skip — no public self-serve registration; access is restricted to licensed surveying firms under municipal/government contract; no signup surface published. |
| **num_stations** | 14 physical CORS — secondary citation via Mahdi & Ahmed 2024 academic study (processed 14 days of GNSS data for these 14 Kuwait CORS integrated with 27 IGS stations using Bernese). Not declared on a first-party operator portal in sandbox-reachable form; treat as secondary-source. |
| **vrs** | ? — no operator technical declaration; 14 stations across 17,818 km² supports a network solution but mode (VRS/MAC/FKP/single-base) unverified. |
| **host:port** | null — not published |
| **tariff** | null — not applicable (licensed firms only) |
| **hobbyist_eligibility** | No — access confirmed restricted to licensed surveying firms under municipal/government contract |
| **legal_residency_required** | Unclear — no individual registration path at any price found |
| **last_confirmed_alive** | null — no public NTRIP stream confirmed at any date |
| **datum_epoch** | omitted -- no operator NTRIP caster; no operator-portal declaration to cite. (Academic literature references "KW-FWGM2022" geoid + WGS84-aligned national frame, but per primer rule these are not operator-portal citations.) |

---

## Service Details

### Kuwait Geodetic Network (KGN) / CORS Infrastructure

Kuwait operates a government GNSS CORS network managed jointly by **PACI** (Public Authority for Civil Information) and **Kuwait Municipality**. The network is used for cadastral and infrastructure surveying.

**Station count (per academic research, 2023–2024):** 14 CORS stations distributed across Kuwait's territory (~17,818 km²). A 2024 academic study (Mahdi & Ahmed) processed 14 days of GNSS data for these 14 Kuwait CORS integrated with 27 IGS stations using Bernese software to determine precise coordinates in the latest terrestrial geodetic frame.

**Datum / geoid:** The "KW-FWGM2022" geoid model (accuracy < 1.8 cm standard deviation) was developed specifically for Kuwait, suitable for GIS and geomatics applications. The underlying coordinate datum is based on WGS84 / Kuwait national geodetic framework.

**Access policy:** Streams are issued only to licensed surveying firms operating under municipal or government contract. No public caster host:port has been identified in any indexed source. No individual or hobbyist registration path at any price has been found.

### Coverage Assessment

Kuwait is small and topographically flat (~17,818 km²). A 14-station CORS network would theoretically provide sub-cm RTK coverage across the entire territory at typical baseline lengths of ~30–40 km. The infrastructure is adequate for national RTK if opened, but no open-access mandate has been announced.

---

## Commercial Alternatives

No independent commercial NTRIP provider with confirmed Kuwait coverage has been identified. ArduSimple does not list a dedicated Kuwait NTRIP page (no `rtk-correction-services-and-ntrip-casters-in-kuwait` page found in search results). Global networks (GEODNET, PointOne, HxGN SmartNet, ONOCOY) do not list Kuwait coverage from public documentation.

**KSA-CORS spill:** The nearest confirmed active NTRIP caster is KSA-CORS (`ksacors.geoportal.sa:2101`). The closest Saudi stations would be in the Al-Hafuf / Dammam / Al-Wafrah corridor. Given Kuwait's southern border proximity (~50 km from KSA), KSA-CORS VRS *may* provide marginal RTK coverage in southern Kuwait, but this is unconfirmed and KSA-CORS itself has reachability issues from non-SA IPs (see SA_SaudiArabia.md).

Global free fallback: **Galileo HAS** (~40 cm accuracy, no connectivity required, globally available including Kuwait).

---

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGS / EarthScope** — IGS-affiliated station(s) in or near Kuwait; check EarthScope archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

No public RINEX download portal for the Kuwait CORS network was found.

---

## Negative Findings (reconfirmed 2026-05-17)

- PACI / Kuwait Municipality CORS: no public host:port published
- rtk2go: zero KW mountpoints (`py scripts/stations_by_country.py KWT` → no stations, 2026-05-17)
- Centipede + EarthScope: zero KW nodes (same probe, 2026-05-17)
- ArduSimple: no Kuwait-specific NTRIP page indexed
- GEODNET, PointOne, HxGN SmartNet: no Kuwait coverage confirmed in public documentation
- No open-access mandate or policy change toward individual access found in 2024–2026 sources
- paci.gov.kw/en: WebFetch ECONNREFUSED 2026-05-17 (sandbox-side; site may be IP-restricted) -- no further public detail extractable from sandbox

---

## Sources Consulted
- Investigation notes next.txt entry 83 (project internal)
- country-survey.md entry `KW — Kuwait` (project internal, date_added 2026-04-28)
- ScienceDirect — "Refinement of the Kuwait geoid using modified Stokes' kernel and Airy-Heiskanen isostatic reduction" (KW-FWGM2022): https://www.sciencedirect.com/science/article/pii/S1110982323000261
- GPS World — "Kuwait high-rise goes up with assist from BeiDou": https://www.gpsworld.com/kuwait-high-rise-goes-up-with-assist-from-beidou/
- EPSG — coordinate reference systems for Kuwait: https://epsg.io/?q=Kuwait
- mvarga1989 GitHub — community CORS/RTK networks list (Kuwait not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- ArduSimple country listing (Kuwait not listed with dedicated page): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- SA_SaudiArabia.md — KSA-CORS context (project internal)
