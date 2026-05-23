# Kazakhstan [KZ] - NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: PARTIAL - national operator (NCGPI / KGS) runs an 86-station reference network with RTK + RINEX services; no public NTRIP host:port published; access is contract-based via NCGPI or 3+ commercial resellers (GeoComm, EFT, RTKNet). One free rtk2go volunteer base in northern Kazakhstan.

## NCGPI / Qazgeodesy - national operator

| Field | Value |
|---|---|
| operator | RGP "National Centre of Geodesy and Spatial Information" (NCGPI / Qazgeodesy) under the Committee of Geodesy and Cartography; high-precision satellite navigation system mandate vested in JSC NC Qazaqstan Garysh Sapary (KGS) per Government Decree RK No 721 (2012-05-31) |
| landing_url | https://qazgeodesy.kz/en/ |
| access_url | https://ggo.gov.kz/correct-info |
| access_type | paid |
| coverage | conflicting station counts (see num_stations); ~180 km mean spacing implied by the 86 figure across 2.72 million km^2; densest in the populated north (Astana-Pavlodar-Karaganda) and southeast (Almaty); thin in the western steppe and Caspian region. No public coverage map. |
| num_stations | conflicting - geocomm.kz/bazovye-stanczii states KGS "owns 60 navigation stations" (refetched 2026-05-23); qazgeodesy.kz "National Spatial Data Infrastructure" programme materials cite 86 as the current build-out; no operator-side authoritative reconciliation surfaced. Either figure is plausible (60 = KGS-owned core, 86 = total including newer additions). |
| tariff | not published - qazgeodesy.kz/en lists "Corrective information services in RTK mode" without prices; rtk.qgeo.kz portal is a logo + form; ggo.gov.kz/correct-info routes through subscription form; no AOC/KZT figures surfaced (checked: qazgeodesy.kz/en 2026-05-23; ggo.gov.kz/correct-info 2026-05-23; geocomm.kz/bazovye-stanczii 2026-05-23; eft.kz/base 2026-05-23; web search "qazgeodesy qgeo.kz RTK tariff 2026" 2026-05-23) |
| hobbyist_eligibility | ? - all providers oriented to surveyors / engineering firms; no individual / hobbyist tier advertised; non-professionals are not explicitly excluded but Kazakh-language contract + KZT bank transfer + IIN (individual) / BIN (business) workflow is the practical barrier (checked: qazgeodesy.kz/en 2026-05-23; ggo.gov.kz/correct-info 2026-05-23) |
| datum_epoch | QazTRF-23 (Qazaqstan Terrestrial Reference Frame 2023) - national geodetic coordinate system launched 2025-01-01 by the Ministry of Digital Development, Innovation and Aerospace Industry alongside the CORS network (citation: tengrinews.kz 2025-02-03 "Kazakhstan launches its own geodetic coordinate system"; tvbrics.com 2025-02-03; MINEX Forum 2025-02-03; ggo.gov.kz hosts QazTRF-23 catalogues). Replaces Soviet SK-42 / SK-95. Epoch not specified in news sources; ITRF realization tie not declared publicly. |
| sourcetable | none published - no public host:port surfaced for the national network; reseller portals (geocomm, eft, geokurs, southinstrument) all gate live endpoints behind contract (checked: ggo.gov.kz/correct-info 2026-05-23; qazgeodesy.kz/en 2026-05-23; rtk.qgeo.kz 2026-05-23; geocomm.kz 2026-05-23; eft.kz/base 2026-05-23; monitor.use-snip.com 2026-05-23) |
| vrs | ? - 180 km mean spacing exceeds the ~70 km NRTK hull rule (primer accuracy); operator portal silent on VRS/MAC/FKP/iMAX. NRTK across the full country is implausible unless densified in metro clusters; no operator declaration surfaced (checked: ggo.gov.kz/correct-info 2026-05-23; qazgeodesy.kz/en 2026-05-23) |
| residency_required | yes - KZT bank transfer + IIN (individual taxpayer ID) / BIN (business ID) + Kazakh-language contract are practical barriers to non-resident signup |
| stations_source | https://qazgeodesy.kz/en/ + https://geocomm.kz/bazovye-stanczii/ (no public coverage map; station counts disclosed in textual marketing only) |

NCGPI is the operational descendant of the 2012 mandate (Government Decree RK No 721, 2012-05-31, cited in KGS / NCGPI literature - no canonical URL); the landing has migrated through qgeo.kz -> qazgeodesy.kz -> ggo.gov.kz (the canonical correction-services page is now ggo.gov.kz/correct-info, reachable 2026-05-23, with subscription contact rtk@qgeo.kz / +7 7172 277-726). The earlier `rtk.qgeo.kz` portal has degraded to a near-empty header. The legacy `kazgeodeziya.kz` domain returns hosting-expired error. Connection requires GNSS receiver + GPRS/4G modem + service contract via NCGPI or a reseller. QazTRF-23 (Qazaqstan Terrestrial Reference Frame 2023) became the official national datum on 2025-01-01, displacing earlier Soviet SK-42 / SK-95 contexts and the academic GSK-2011 / WGS84 references that appeared in pre-2025 literature.

## Commercial resellers / private CORS layer

- **GeoComm LLP** (geocomm.kz; Karaganda, Moskovskaya 16/1) - private CORS network + resells KGS national; price on contact (Anatoly +7 (771) 180-78-99 / saa@geocomm.kz; main +7 (7212) 79-12-12 / info@geocomm.kz). Station count not publicly disclosed; 24/7 marketing.
- **EFT** (eft.kz/base; Almaty, Pirogova 37) - EFT RS1 GPS+GLO+BeiDou+Galileo receivers, "continuous RTK across Kazakhstan"; RINEX post-processing free after registration; RTK price gated behind registration form ("Cena: tenge" with no rate). Contact +7 (727) 310 00 81 / info@eft.kz.
- **Geokurs** (bs.geokurs.kz; Almaty, +7 727 229 00 00) - resells Trimble CenterPoint RTX (SSR/PPP via satellite); out of scope per project rule (PPP not RTK-NTRIP, see guide for HAS/PPP alternative).
- **RTKNet (TOO Geo Master A)** (southinstrument.kz/rtknet; Almaty) - equipment-distributor-operated network; sales-only page; no endpoint, mountpoint, or KZT pricing on public web.

## Free / volunteer fallback

| Source | Mountpoint | Lat / Lon | Notes |
|---|---|---|---|
| rtk2go | `GerAndry` | 53.09 N, 77.44 E | Single volunteer base near Pavlodar (Ilichyovka), verified 2026-05-23 in `data/rtk2go.sourcetable`. RTCM 3.2 GPS+GLO+GAL+BDS, single-base; rtk2go convention any-email / no password. Usable within ~20-30 km. |

No Centipede, EarthScope, GEODNET, ONOCOY ground stations confirmed inside Kazakhstan as of 2026-05-23. The nearest IGS-class stations for post-processing only are KITG (Uzbekistan, ~175 km from Dushanbe but well outside KZ).

## Hobbyist path

1. **Near Pavlodar (<=30 km of 53.09/77.44)** - rtk2go `GerAndry` (free, single-base).
2. **Elsewhere in Kazakhstan** - no free RTK path. NCGPI / KGS or a reseller contract is the only cm-class option, all priced on request via Russian/Kazakh-language sales channels. Practical barrier: KZT bank transfer + IIN/BIN + Kazakh-language contract.
3. **PPP / SSR fallback** - Galileo HAS (~20 cm horizontal, free, satellite-delivered) for sub-metre work; Trimble CenterPoint RTX via Geokurs is a paid SSR option for non-residents but out of project scope.

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| NCGPI national RINEX archive (via subscription) | https://qazgeodesy.kz/en/ | Sales-contact only |
| EFT RINEX post-processing archive | https://eft.kz/base | Free after registration |
| EarthScope GNSS data archive (regional IGS holdings - ARTI / ARTU / KIT3) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA) |
| BKG NTRIP IGS real-time (Central Asian stations) | https://igs.bkg.bund.de/ntrip/ | Free (account) |

## Sources

- qazgeodesy.kz EN landing (refetched 2026-05-23): https://qazgeodesy.kz/en/
- ggo.gov.kz/correct-info (canonical correction-services page; subscription contact rtk@qgeo.kz / +7 7172 277-726): https://ggo.gov.kz/correct-info
- rtk.qgeo.kz (legacy logo-only header): https://rtk.qgeo.kz/
- gharysh.kz (JSC NC Qazaqstan Garysh Sapary corporate; KGS mandate): https://gharysh.kz/
- geocomm.kz/bazovye-stanczii (refetched 2026-05-23 - 60-station legacy + 86-station current figures attributed to KGS; contact details): https://geocomm.kz/bazovye-stanczii/
- eft.kz/base (refetched 2026-05-23 - GPS+GLO+BeiDou+Galileo, free RINEX, RTK price gated): https://eft.kz/base
- bs.geokurs.kz/rtx (Geokurs Trimble CenterPoint RTX): https://bs.geokurs.kz/rtx
- southinstrument.kz/rtknet (RTKNet / TOO Geo Master A): https://southinstrument.kz/rtknet
- ArduSimple Kazakhstan: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-kazakhstan/
- 2gis.kz business directory (KGS HQ Astana, Turan Avenue 89)
- Government Decree RK No 721 (2012-05-31) cited in KGS / NCGPI literature (no canonical URL)
- QazTRF-23 launch coverage (2025-02-03): https://en.tengrinews.kz/kazakhstan_news/kazakhstan-launches-its-own-geodetic-coordinate-system-266558/; https://tvbrics.com/en/news/kazakhstan-launches-national-geodetic-coordinate-system-to-enhance-spatial-data-infrastructure/; https://minexforum.com/2025/02/03/kazakhstan-launches-its-own-geodetic-coordinate-system/
- Local 2026-05-23: `data/rtk2go.sourcetable` row 219 `GerAndry;Ilichyovka;...;KAZ;53.09;77.44` confirmed; `scripts/stations_by_country.py KAZ` -> 1 rtk2go station only
