# Lithuania [LT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified via WebSearch; 35 LT stations, dual-IP caster, EUPOS cross-border setup unchanged since 2026-05-12)

## Status: YES — free national NTRIP RTK caster operating (LitPOS, VRS-network); free of charge for any registered user; primary IP `193.219.10.2:2101` and secondary IP `195.182.72.152:2101` both serve identical sourcetables.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — free of charge, registration required |
| **Network name** | LitPOS — Lithuanian Positioning System |
| **Operator** | VšĮ Statybos sektoriaus vystymo agentūra (Construction Sector Development Agency / SSVA), as the manager of the Spatial Information Portal of Lithuania (`geoportal.lt`); formerly under Nacionalinė žemės tarnyba (NZT — National Land Service); GIS-Centras (within SSVA) is the technical operator. Caster software: Trimble Pivot Platform |
| **Mandate basis** | LitPOS is Lithuania's permanent reference GNSS network, operational since July 2007. EUPOS member; participates in cooperation agreements granting LitPOS users access to 3 ASG-EUPOS (Polish) stations and 6 LATPOS (Latvian) stations |
| **host:port — primary** | `193.219.10.2:2101` (VilniusTech Geodesy Institute, Vilnius) — re-confirmed live 2026-05-12: `SOURCETABLE 200 OK ENDSOURCETABLE` from `NTRIP Trimble Ntrip Caster 5.2`, 12 STR rows |
| **host:port — secondary** | `195.182.72.152:2101` (GIS-Centras / SSVA) — re-confirmed live 2026-05-12: `SOURCETABLE 200 OK`, 12 STR rows. Both servers expose the same mountpoints; no DNS hostname is published for either IP. Some user docs additionally cite alternate port `2111` |
| **VRS** | Yes — primary product is VRS network solution. Mountpoints `VRS_RTCM31`, `VRS_RTCM23`, `VRS_RTCM32` (RTCM 3.4 with MSM5 GPS+GLO+GAL+BDS), `VRS_CMRx` (Trimble CMRx), `VRS_CMR_plus`. Plus DGNSS streams (`DGPS_RTCM24`, `DGPS`) and Trimble RTX-style `RTX_RTCM34` and `RTX_RTCM34_GPS_GALILEO`. Single-base RTK is provided via the network mountpoints (no per-station mountpoints in the public sourcetable) |
| **GNSS systems** | RTCM 3.4 mountpoints emit MSM5 / MSM7 → GPS+GLONASS+Galileo+BeiDou. Older RTCM 2.3 / 3.1 mountpoints are GPS-only or GPS+GLONASS |
| **tariff** | Free of charge — usage rules §3 (geoportal.lt LitPOS-paslauga page) state *"visi LitPOS duomenys yra vieši ir teikiami nemokamai"* ("all LitPOS data are public and provided free of charge") |
| **Number of stations** | 35 LT stations covering all of Lithuanian territory at ~50 km mean spacing; plus 3 Polish (ASG-EUPOS) + 6 Latvian (LATPOS) stations available under EUPOS cooperation |
| **hobbyist_eligibility** | Yes — usage rules §6 explicitly admits **both natural and legal persons** (fiziniai ir juridiniai asmenys); no professional surveying licence required. Registration form publicly accessible at `https://www.geoportal.lt/geoportal/web/litpos-en/registration` |
| **legal_residency_required** | No formal residency clause found. Registration form is bilingual (Lithuanian + English); foreign-user policy is permissive but not loudly advertised. Cross-border data sharing with Poland and Latvia is documented in the usage rules. **Non-Lithuanian registration not explicitly confirmed but also not excluded** |
| **last_confirmed_alive** | 2026-05-12 — `193.219.10.2:2101` and `195.182.72.152:2101` both returned `SOURCETABLE 200 OK` (NTRIP Trimble Ntrip Caster 5.2), 12 STR rows each (identical mountpoint list to 2026-05-07 sourcetable); geoportal.lt LitPOS-EN portal accessible |
| **datum_epoch** | omitted — no citable declaration (no operator-cited reference frame/epoch found on geoportal.lt LitPOS-EN or litpos-paslauga pages) |

## Mountpoint Catalogue — both servers (sourcetable 2026-05-12)

| Mountpoint | Format | Type | Constellations |
|---|---|---|---|
| `VRS_RTCM23` | RTCM 2.3 | Network VRS | GPS + GLONASS |
| `VRS_RTCM31` | RTCM 3.1 | Network VRS | GPS + GLONASS |
| `VRS_RTCM32` | RTCM 3.4 with MSM5 | Network VRS | GPS+GLO+GAL+BDS |
| `VRS_CMR_plus` | CMR+ | Network VRS | GPS + GLONASS |
| `VRS_CMRx` | CMRx | Network VRS | GPS+GLO+GAL+BDS |
| `DGPS` | RTCM 2.3 | Network DGPS | GPS |
| `DGPS_RTCM24` | RTCM 2.4 | Network DGPS | GPS + GLONASS |
| `RTCM_23` | RTCM 2.3 | GPS-only network | GPS |
| `RTCM_30` | RTCM 3.1 | GPS-only network | GPS |
| `CMR` | CMR | GPS-only network | GPS |
| `RTX_RTCM34` | RTCM 3.4 with MSM7 | Trimble RTX-style | GPS+GLO+GAL+BDS |
| `RTX_RTCM34_GPS_GALILEO` | RTCM 3.4 with MSM7 | Trimble RTX-style | GPS + GAL |

All mountpoints carry coordinates `54, 23` (Lithuania centroid) and `solution=1` (network solution) — no per-station entries are exposed in the public sourcetable, consistent with the "vrs-only" map type assigned in the existing networks.md entry.

## Service Details

### Registration (free)

1. Create a `geoportal.lt` account.
2. Submit the LitPOS registration application: `https://www.geoportal.lt/geoportal/web/litpos-en/registration` (English form available).
3. Approval issues NTRIP credentials (username + password) by email; LitPOS@geoportal.lt is the documented service contact.
4. NTRIP client setup:
   - **Caster Host (primary)**: `193.219.10.2`, port `2101` (or `2111` per some user docs)
   - **Caster Host (secondary)**: `195.182.72.152`, port `2101`
   - **Mountpoint**: `VRS_RTCM32` recommended for modern multi-constellation rovers
5. Live monitoring of one's own session is available at `https://www.geoportal.lt/app/litpos`.

### Coverage

- **Lithuania**: 35 LitPOS stations, ~50 km mean spacing, full-territory VRS coverage including the Klaipėda coast, Curonian Spit, and Vilnius region.
- **Cross-border**: 3 ASG-EUPOS stations from Poland and 6 LATPOS stations from Latvia are accessible to LitPOS users by virtue of EUPOS cooperation, extending effective coverage into northern Poland (Suwałki area) and southern Latvia (Daugavpils area).

## Context Notes

- **Pricing**: Free since the public deployment of LitPOS in 2007; no commercial tier. The previous research note in this file claiming "tariff not publicly listed" was incorrect — the LitPOS usage rules (§3) explicitly state the service is `nemokamai` (free of charge) for all registered users.
- **Operator handover**: The Spatial Information Portal of Lithuania (`geoportal.lt`) was historically administered by Nacionalinė žemės tarnyba (National Land Service under the Ministry of Agriculture). As of 2024–2026, the portal manager is **VšĮ Statybos sektoriaus vystymo agentūra** (Construction Sector Development Agency); GIS-Centras (within SSVA) operates the secondary caster IP. The footer of geoportal.lt confirms this. Service continuity is unaffected.
- **Two parallel casters**: The primary IP (`193.219.10.2`, VilniusTech Geodesy Institute) and the secondary IP (`195.182.72.152`, GIS-Centras) provide identical streams. Either is suitable; failover is manual in the rover. No DNS hostname has been published, so users configure raw IPs.
- **EUPOS membership**: LitPOS is a member of EUPOS (European Position Determination System), the consortium of 17+ Central and Eastern European national CORS networks. EUPOS reciprocal access provides 3 PL + 6 LV reference stations for free use by LitPOS account holders.
- **Caster software**: Trimble Pivot Platform (sourcetable banner). Same platform used by ZAKPOS (UA), NRTK Suomi (FI), several SAPOS Bundesländer (DE) and others — facilitates standard MSM5/7 streams and mature DGPS variants.
- **Live status / sessions**: `https://www.geoportal.lt/app/litpos` shows real-time session monitoring, sourcetable, and station status. Useful for both the operator and end-users.
- **Pipeline status**: Existing pipeline status is `candidate` in networks.md; sourcetable contains only 12 VRS-style entries (all coordinates 54,23 / `solution=1`), so map type is `vrs-only` and pipeline yields 0 physical pins. No NRTK polygon implementation yet means LitPOS does not surface visible pins on the map; it is announced via documentation and data only.
- **Stations.json 2026-05-12 fetch**: LT (LTU) returns 1 Centipede pin only — `AKIS` (54.85, 24.345) near Kaunas — via `py scripts/stations_by_country.py LTU`. LitPOS itself contributes 0 mappable pins given the VRS-only sourcetable. rtk2go has zero LT entries.
- **English-language portal**: `https://www.geoportal.lt/geoportal/web/litpos-en/` provides full English-language pages: About, Status, Application, Registration, Contacts. The Lithuanian-language equivalents (`litpos-paslauga`) carry the formal usage rules and FAQ (DUK).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **LitPOS RINEX (FTPS)** | `https://www.geoportal.lt/geoportal/en/web/litpos-paslauga/duk` (FTPS access via FileZilla; documented in DUK) | Free (LitPOS account) |
| **EUREF / EPN — Lithuanian stations** | https://www.epncb.oma.be (e.g. `VLNS00LTU`, `KLPD00LTU`) | Free |

## Sources Consulted

- LitPOS English about page: https://www.geoportal.lt/geoportal/web/litpos-en (text extracted 2026-05-07: "Total number of LitPOS GNSS stations is 35", "users can use 3 ASG-EUPOS Polish stations and 6 LATPOS Latvian stations"; page re-checked 2026-05-12, content unchanged)
- LitPOS English registration: https://www.geoportal.lt/geoportal/web/litpos-en/registration
- LitPOS English status / application / contacts: respective `/litpos-en/` paths
- LitPOS Lithuanian usage rules + FAQ: https://www.geoportal.lt/geoportal/en/web/litpos-paslauga/duk and https://www.geoportal.lt/geoportal/en/web/litpos-paslauga (free-of-charge clause §3, eligibility §6)
- Geoportal LitPOS app (live sessions): https://www.geoportal.lt/app/litpos
- Live primary sourcetable: `curl --http0.9 http://193.219.10.2:2101/` → `SOURCETABLE 200 OK ENDSOURCETABLE` Server: `NTRIP Trimble Ntrip Caster 5.2`, 12 STR rows (re-confirmed 2026-05-12; Content-Length 1677)
- Live secondary sourcetable: `curl --http0.9 http://195.182.72.152:2101/` → identical structure (re-confirmed 2026-05-12; Content-Length 1713)
- M3G LitPOS GNSS metadata: https://gnss-metadata.eu/MOID/projnet.5f366a387e27d32c1b218ac2
- LitPOS performance analysis (Vilnius Tech, 2017): https://etalpykla.vilniustech.lt/bitstream/handle/123456789/155251/10th_ICEE_2017-161.pdf
- ArduSimple Lithuania: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-lithuania/
- Existing networks.md `litpos` entry (candidate status, two-IP setup, EUPOS context, pipeline VRS-only)
- Stations.json 2026-05-12 fetch: LT (LTU) = 1 Centipede entry (AKIS); LitPOS contributes 0 mappable pins (vrs-only)
