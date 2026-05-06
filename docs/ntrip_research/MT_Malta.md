# Malta [MT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO government caster — one rtk2go volunteer base is the only free RTK option; no GEODNET node confirmed; Italian commercial networks do not extend to Malta

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No government or commercial Maltese caster |
| **Volunteer (rtk2go)** | 1 base — `EneGIS` at Naxxar (35.92°N, 14.44°E), RTCM 3.2 MSM, GPS+GLONASS L1+L2; country code `MLT` |
| **Volunteer (Centipede)** | 0 nodes detected in Malta bounding box |
| **GEODNET** | No confirmed node on Malta or Gozo as of 2026-05-06 (coverage map shows no hexagon over the Maltese archipelago) |
| **Italian commercial networks** | NetGEO/TopNET Live (~€360/yr national Italy subscription) — coverage does not extend to Malta per published maps |
| **hobbyist_eligibility** | rtk2go EneGIS base: yes, free, no registration |
| **legal_residency_required** | n/a (rtk2go is open globally) |
| **last_confirmed_alive** | rtk2go EneGIS base confirmed present in rtk2go sourcetable; exact last-probe date not separately recorded |

## No Active Government/Commercial Caster

No Maltese government caster has been identified. The Malta Environment and Planning Authority (MEPA, now MCESD/Planning Authority) and the Land Registry do not operate a public NTRIP endpoint. No national CORS network with NTRIP streaming has been identified through Alberding directory listings, EUREF/EPN listings, or NTRIP-list.com's Europe table.

ArduSimple's Malta page (checked 2026-05-06) notes: "Malta does not have an established National RTK Network, as far as we are aware."

## Most Recent Project Announcement

No government RTK project announcement for Malta found. The Malta Spatial Data Infrastructure portal (msdi.data.gov.mt) and GeoHub (geohub.gov.mt) are active for geospatial data but contain no RTK/CORS programme references.

## Context Notes

- **Coverage reality**: The single rtk2go EneGIS base at Naxxar (Malta island, NW quadrant) covers Malta island adequately within ~25 km. Gozo (at ~25 km north) sits at the edge of practical single-base RTK range; Comino is in between. For reliable RTK on Gozo a dedicated base station would be needed.
- **GEODNET**: GEODNET's network has >15,000 stations in 140+ countries, but no hexagon covering Malta appears on rtk.geodnet.com/coverage as of 2026-05-06. GEODNET offers free access to stations within range; a node on Malta or Gozo would materially change the situation.
- **Italian commercial networks**: NetGEO/TopNET (Topcon Positioning Italy, >200 stations, covers mainland Italy and Sardinia/Sicily) does not publish Malta coverage. Sicili@net (INGV Catania, `193.206.223.39:2101`, ~80 stations in Sicily and southern Calabria) is the nearest free Italian caster at ~90 km from Malta — outside reliable RTK range.
- **Nearest government NTRIP**: ERGNSS (Spain, `ergnss-ip.ign.es:2101`) is ~1,700 km away. APOS (Austria) ~1,400 km. Both useless.
- **Global commercial fallbacks with possible Malta coverage**: Skylark Nx RTK (Swift Navigation) lists Andorra (and by extension Mediterranean Europe) in its coverage — may cover Malta; not verified. PPP alternatives (Galileo HAS, ~40 cm) available globally.
- **Malta is absent** from ntrip-list.com's Europe table.

## Post-Processing (RINEX) Fallback

No dedicated Maltese CORS RINEX archive identified. EPN station `MALT` (EUREF permanent network) in Malta provides post-processing RINEX data via the EPN Central Bureau (epncb.oma.be) — free with BKG/ROB broadcaster registration.

## Sources Consulted
- ArduSimple Malta RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-malta/
- GEODNET coverage map: https://rtk.geodnet.com/coverage/rtk-service
- TopNET Live Italy network: https://rtk.topnetlive.com/italy/networks/topnet-live-italy
- NTRIP-list Europe: https://ntrip-list.com/europe/
- Malta Spatial Data Infrastructure: https://msdi.data.gov.mt/
- Malta GeoHub: https://geohub.gov.mt/
- rtk2go sourcetable (EneGIS mountpoint, country code MLT): http://rtk2go.com/
- EUREF Permanent GNSS Network: https://epncb.oma.be/
