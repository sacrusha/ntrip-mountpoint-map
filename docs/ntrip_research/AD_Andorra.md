# Andorra [AD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (originally 2026-05-06)

## Status: NO domestic caster; PCAR00AND streams via EUREF-IP broadcasters (single-base, free, registration); Spanish ERGNSS border stations are the practical VRS option

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (Andorran)** | No |
| **PCAR00AND** | EPN station at Pic de Carroi — confirmed in EPN real-time map, streams via EUREF-IP broadcasters in RTCM (free with BKG/ROB/ASI registration); raw 1 Hz GNSS, not VRS |
| **RULL** | Second ERGAND station; EPN/EPOS member; real-time streaming status less prominent in EPN broadcaster map |
| **EUREF-IP broadcasters** | `euref-ip.net:2101` (BKG, Frankfurt); `www.euref-ip.be:2101` (ROB, Brussels); ASI (Italy) — all three federate the EPN streams |
| **Volunteer (rtk2go)** | 0 AD stations (confirmed via `stations_by_country.py AND` — no entries; `stations_by_radius.py 42.54 1.60 50` — no stations within 50 km) |
| **Volunteer (Centipede)** | 0 AD nodes (same checks) |
| **hobbyist_eligibility** | Yes for the EPN PCAR stream via euref-ip.net (free, BKG account); n/a for a domestic VRS service |
| **legal_residency_required** | No (EUREF-IP registration is open globally) |
| **last_confirmed_alive** | PCAR00AND listed in EPN real-time map 2026-05-12; ERGAND domestic NTRIP — none to probe |

## URL Fields (for the ergand country marker)

- **landing_url**: `https://www.cartografia.ad/` — operator-owned (Govern d'Andorra, Cartografia / IDE Andorra) landing page for ERGAND and Andorran geodesy. Describes the agency, EPN station role, post-processing services.
- **access_url**: `https://www.epncb.oma.be/_networkdata/data_access/real_time/broadcasters.php` — EPN central description of the three EUREF-IP broadcasters and how to register for access to PCAR00AND streams. More useful than the bare BKG CGI form `register.rtcm-ntrip.org/cgi-bin/registration.cgi`, which is the registration submission endpoint without service description.

## No Active Government Caster

No Andorran NTRIP RTK caster has been identified. ERGAND (Govern d'Andorra geodetic agency under Cartografia / IDE Andorra) operates two EUREF Permanent Network (EPN) reference stations:

- **PCAR00AND** (Pic de Carroi, ~2,520 m elevation) — confirmed in EPN real-time map; streams via EUREF-IP federated broadcasters (BKG/ROB/ASI) in RTCM format.
- **RULL** — second ERGAND station; EPN member; real-time streaming status less prominent in EPN broadcaster listings.

ERGAND additionally provides post-processing services and the AND08 / GEOAND01 national geoid model (Leica/Topcon/Trimble formats). No domestic NTRIP caster for VRS or network RTK has been announced or discovered.

Post-2025 EUREF Symposium policy: all EPN stations are by default integrated into the GNSS network of the European Plate Observing System (EPOS), with EPN metadata and RINEX data becoming discoverable within EPOS from 2026.

ArduSimple's Andorra page (re-checked 2026-05-12) still identifies Andorra as having no established national RTK network, offering only global fallbacks and global commercial services (Galileo HAS, Skylark Nx RTK).

## Practical RTK Options via Spanish ERGNSS

**ERGNSS** (Red Nacional de Estaciones de Referencia GNSS, IGN Spain) is the most practical free option for users in Andorra:

| Field | Value |
|---|---|
| **host:port** | `ergnss-ip.ign.es:2101` (primary); `ergnss-tr.ign.es:2102` (multiconstellation SPTR) |
| **tariff** | Free; registration required at http://ergnss.ign.es/gnuserportal/ |
| **VRS** | Yes (VRS + single-base nearest-station mountpoints) |
| **hobbyist_eligibility** | Yes — any individual can register; no professional licence required |
| **legal_residency_required** | No; foreign nationals accepted |
| **Coverage near Andorra** | ERGNSS has stations in Catalonia (the Autonomous Community bordering Andorra to the south and east). The nearest ERGNSS physical stations are in the Lleida/Girona zone of Catalonia. Andorra's territory (~468 km²) lies within VRS network range of the Catalan station cluster; baselines should be < 70 km. |

**Centipede (FR)** border nodes in the Ariège/Pyrénées-Orientales (France, north of Andorra) may also provide marginal coverage at the northern edge of Andorra.

## Most Recent Project Announcement

No Andorran government RTK project announcement found as of 2026-05-12. ERGAND's website (cartografia.ad) and EPN Central Bureau listings show only post-processing services and EPN/EPOS participation; no national real-time RTK / VRS service is planned or mentioned. The 2025 EUREF Symposium / EPN 2026 newsletter signals broader EPN→EPOS integration but no Andorra-specific RTK service launch.

## Context Notes

- **PCAR00AND (Pic de Carroi)**: EPN station at ~2,520 m elevation. Confirmed in EPN real-time map; streams in RTCM through the three EPN broadcasters (BKG `euref-ip.net:2101`, ROB `www.euref-ip.be:2101`, ASI). Free with registration at any of the broadcasters. Raw 1 Hz observations — usable as a single-base mountpoint, not VRS. ~5 km from Andorra la Vella; a single base at this location covers all of Andorra at < 30 km baseline.
- **RULL**: Second ERGAND station. Time-series confirmed in EPN; real-time stream status in EPN broadcaster table is less prominent than PCAR.
- **French border reach**: Centipede-RTK nodes in France's Ariège / Pyrénées-Orientales departments (e.g., Foix area, ~50 km north of Andorra la Vella) may offer marginal coverage at the northern border. Node density in the Pyrenean highlands is low; coverage is not guaranteed.
- **Spanish SPTR service** (`ergnss-tr.ign.es:2102`): multi-constellation (GPS+GLONASS+Galileo+BeiDou) VRS corrections; new as of 2024–2025; free with the same ergnss.ign.es registration.
- **Skylark Nx RTK** (Swift Navigation): lists Andorra in EU coverage per Ardusimple/Skylark marketing; commercial, requires subscription.
- **No volunteer bases** on rtk2go or Centipede within Andorra: confirmed via `scripts/stations_by_country.py AND` (no entries) and `scripts/stations_by_radius.py 42.54 1.60 50` (no stations within 50 km of approximate Andorran centroid) on 2026-05-12.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ERGAND / EPN RINEX** (PCAR, RULL) | https://epncb.oma.be/ → data access | Free with EPN data registration |
| **ERGNSS RINEX** (Catalan border stations) | https://www.ign.es/web/ign/portal/gds-gnss-tiempo-real | Free with ergnss.ign.es registration |

## Sources Consulted
- ArduSimple Andorra RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-andorra/
- IDE Andorra i Cartografia (Govern d'Andorra): https://www.cartografia.ad/
- IGN Spain ERGNSS portal: https://www.ign.es/web/ign/portal/gds-gnss-tiempo-real
- ERGNSS user registration: http://ergnss.ign.es/gnuserportal/
- EUREF Permanent GNSS Network (EPN) home: https://epncb.oma.be/
- EPN Real-Time map: https://www.epncb.oma.be/_networkdata/data_access/real_time/map.php
- EUREF-IP NTRIP broadcasters: https://www.euref-ip.be/ · https://euref-ip.net/home
- EPN NTRIP broadcaster list: https://www.epncb.oma.be/_networkdata/data_access/real_time/broadcasters.php
- EPN/EPOS newsletter (Dec 2025, EPN→EPOS integration starting 2026): http://www.epncb.oma.be/_documentation/newsletters/EUREF_Newsletter_2025_01.pdf
- ArduSimple Spain RTK page (ERGNSS details): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-spain/
- Centipede-RTK network map: https://map.centipede-rtk.org/
- Local data verification (2026-05-12): `scripts/stations_by_country.py AND` (no entries), `scripts/stations_by_radius.py 42.54 1.60 50` (no stations within 50 km)
