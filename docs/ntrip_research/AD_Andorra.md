# Andorra [AD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO — no Andorran NTRIP caster; ERGAND is post-processing only; Spanish ERGNSS border stations are the practical RTK option

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **ERGAND NTRIP caster** | None confirmed — ERGAND (Govern d'Andorra geodetic agency) operates 2 EPN reference stations (PCAR at Pic de Carroi, RULL) for post-processing only |
| **EPN real-time stream** | PCAR and RULL may stream via EUREF-IP broadcasters (euref-ip.net:2101 / euref-ip.be) — free with BKG/ROB registration; raw GNSS data, not VRS corrections |
| **Volunteer (rtk2go)** | 0 AD stations (bounding-box confirmed) |
| **Volunteer (Centipede)** | 0 AD nodes (bounding-box confirmed) |
| **hobbyist_eligibility** | n/a (no domestic caster) |
| **legal_residency_required** | n/a |
| **last_confirmed_alive** | No live NTRIP caster to probe |

## No Active Government Caster

No Andorran NTRIP RTK caster has been identified. ERGAND operates two EUREF Permanent Network (EPN) reference stations (PCAR, RULL) and provides post-processing services and the AND08 national geoid model, but no public NTRIP endpoint for real-time RTK corrections has been announced or discovered.

ArduSimple's Andorra page (checked 2026-05-06) identifies Andorra as having no established national RTK network, offering only global fallbacks and global commercial services (Galileo HAS, Skylark Nx RTK).

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

No Andorran government RTK project announcement found as of 2026-05-06. ERGAND's website and EPN Central Bureau listings show only post-processing services and EPN participation; no real-time RTK service is planned or mentioned.

## Context Notes

- **ERGAND EPN stations**: PCAR (Pic de Carroi, ~2,520 m elevation) and RULL are part of the EUREF Permanent Network. EPN stations often stream real-time RTCM data through the euref-ip.net broadcaster (BKG, Frankfurt) and euref-ip.be (ROB, Brussels) — free with registration. These provide raw GNSS observations, not VRS-derived corrections, so they are usable as a single-base NTRIP stream by an NTRIP client but are not a network RTK (VRS) service.
- **French border reach**: Centipede-RTK nodes in France's Ariège department (e.g., Foix area, ~50 km north of Andorra la Vella) may offer marginal coverage at the northern border. Coverage is not guaranteed — node density in the Pyrenean highlands is low.
- **Spanish SPTR service** (`ergnss-tr.ign.es:2102`): multi-constellation (GPS+GLONASS+Galileo+BeiDou) VRS corrections; new as of 2024–2025; free with the same ergnss.ign.es registration.
- **Skylark Nx RTK** (Swift Navigation): lists Andorra in EU coverage per Ardusimple/Skylark marketing; commercial, requires subscription.
- **No volunteer bases** on rtk2go or Centipede within Andorra (ISO country bounding box 42.43°N–42.65°N, 1.41°E–1.79°E) confirmed via sourcetable bounding-box check.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **ERGAND / EPN RINEX** (PCAR, RULL) | https://epncb.oma.be/ → data access | Free with EPN data registration |
| **ERGNSS RINEX** (Catalan border stations) | https://www.ign.es/web/ign/portal/gds-gnss-tiempo-real | Free with ergnss.ign.es registration |

## Sources Consulted
- ArduSimple Andorra RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-andorra/
- IGN Spain ERGNSS portal: https://www.ign.es/web/ign/portal/gds-gnss-tiempo-real
- ERGNSS user registration: http://ergnss.ign.es/gnuserportal/
- EUREF Permanent GNSS Network (EPN) station map: https://epncb.oma.be/
- EUREF-IP NTRIP broadcasters: https://www.euref-ip.be/ · https://euref-ip.net/home
- EPN NTRIP broadcaster list: https://www.epncb.oma.be/_networkdata/data_access/real_time/broadcasters.php
- ArduSimple Spain RTK page (ERGNSS details): https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-spain/
- Centipede-RTK network map: https://map.centipede-rtk.org/
