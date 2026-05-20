# Andorra [AD] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (prior: 2026-05-15)

## Status: ACTIVE — ERGAND publishes two free single-base NTRIP casters (RULL + PCAR) on cartografia.ad. Both casters confirmed live 2026-05-17 by direct TCP sourcetable fetch.

## ERGAND — RULL (Roc del Pui de Rull, station #1)

| Field | Value |
|---|---|
| **landing_url** | `https://www.cartografia.ad/ergand` — operator-owned (Govern d'Andorra, Àrea de Cartografia). Describes ERGAND, both stations, and links real-time + post-processing services. |
| **access_url** | `https://www.cartografia.ad/serveis-a-temps-real` — same operator, publishes host/port/mountpoints/credentials in Catalan, and the `ergand@govern.ad` contact for issues. |
| **host:port** | `194.158.95.189:2101` — TCP-probed 2026-05-17, `SOURCETABLE 200 OK`, server `GR30 4.31.101/1.0` |
| **mountpoints** | `RTCM3` (RTCM 3.x GPS+GLO), `RTCM32` (RTCM 3.2 MSM5 GPS+GLO+GAL+BDS). Operator page still advertises a third mount `RTCM23` (RTCM 2.3) on 2026-05-17 but the live sourcetable does not list it — operator page remains stale on this entry. |
| **credentials** | `rull` / `rull` (operator publishes these openly on the public web page; access page also states some streams are "de lliure accés" with no auth) |
| **tariff** | Free, no fee listed; no VAT statement (operator is a government agency, page is informational) — source: `https://www.cartografia.ad/serveis-a-temps-real`, observed 2026-05-17 |
| **num_stations** | 1 (single-base, this caster carries only RULL) |
| **vrs** | no |
| **hobbyist_eligibility** | yes (publicly published creds, no application form) |
| **legal_residency_required** | no (no residency gate on the page) |
| **last_confirmed_alive** | 2026-05-17 — `194.158.95.189:2101` returned `SOURCETABLE 200 OK` via direct TCP probe |

## ERGAND — PCAR (Pic de Carroi, ~2,520 m, ~5 km from Andorra la Vella)

| Field | Value |
|---|---|
| **landing_url** | `https://www.cartografia.ad/ergand` |
| **access_url** | `https://www.cartografia.ad/serveis-a-temps-real` |
| **host:port** | `185.194.59.113:2101` — TCP-probed 2026-05-17, `SOURCETABLE 200 OK`, server `GR50 4.80.109/1.0` |
| **mountpoints** | `PCAR3` (RTCM 3.x GPS+GLO), `PCAR3M` (RTCM 3.2 MSM5 GPS+GLO+GAL+BDS) — verbatim from live sourcetable |
| **credentials** | `pcar` / `pcar` (publicly published) |
| **tariff** | Free — same source/date as RULL |
| **num_stations** | 1 (this caster carries only PCAR) |
| **vrs** | no |
| **hobbyist_eligibility** | yes |
| **legal_residency_required** | no |
| **last_confirmed_alive** | 2026-05-17 — `185.194.59.113:2101` returned `SOURCETABLE 200 OK` via direct TCP probe |

PCAR is also an EPN station (`PCAR00AND0`) and is **separately** redistributed by the EUREF-IP federation (BKG `euref-ip.net:2101`, ROB `www.euref-ip.be:2101`, ASI `euref-ip.asi.it:2101`) under standard EUREF registration. EPN status page returned HTTP 403 on 2026-05-17. Pipeline file `docs/rtk_inventory.md` (last updated 2026-05-13) records PCAR00AND0 as live on all three EUREF-IP broadcasters.

RULL is listed as an EPN member but `docs/rtk_inventory.md` notes it has historically been **RINEX-only on EUREF-IP** (not exposed as a real-time stream by BKG/ROB/ASI). The cartografia.ad caster is the only real-time path to RULL.

## Datum / Epoch

Could not find a citable official declaration of datum + epoch for ERGAND on cartografia.ad — the `serveis-a-temps-real` page does not state one and the `/ergand` page links go no deeper on this within the content WebFetch returned. Andorra is in the ETRS89 area of use and ERGAND is an EPN contributor (which implies ETRS2000 alignment in practice), but per the strict rule that the field must be accompanied by a URL to the official declaration, **the datum_epoch field is omitted**.

## Volunteer / Federated Coverage in Andorra

- **rtk2go**: 0 AD stations. Verified 2026-05-17: `py scripts/stations_by_country.py AND` → "No stations for 'AND'". (Script reports no AD tag at all in stations.json.)
- **Centipede**: 0 AD nodes (same script returned nothing).
- **EarthScope**: 0 AD stations (same).
- **Within 50 km of (42.54, 1.60)**: 0 stations. Verified 2026-05-17: `py scripts/stations_by_radius.py 42.54 1.60 50` → "No stations within 50 km".

## Cross-Border Alternatives

| Service | Country | Why relevant | Caveat |
|---|---|---|---|
| ERGNSS (IGN Spain) `ergnss-ip.ign.es:2101`, multi-constellation SPTR `ergnss-tr.ign.es:2102` | ES | Free with registration at `http://ergnss.ign.es/gnuserportal/`; Catalan border stations are < 70 km of all Andorran territory; full VRS network | Spanish IGN account required; not residency-gated but a citizen-ID field exists on the form |
| Centipede-RTK (FR) | FR | Sparse community nodes in Ariège / Pyrénées-Orientales may touch the northern Andorran border | Coverage in Pyrenean highlands is thin; not guaranteed |
| EUREF-IP federation (PCAR redistribution) | DE/BE/IT | Standard EUREF account at BKG, ROB, or ASI grants access to `PCAR00AND0` | Different account than ergand@govern.ad; useful if multi-station EUREF use is also planned |

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| ERGAND post-processing (RULL, PCAR) | `https://www.cartografia.ad/ergand` (Serveis de postprocés) | Free; contact `ergand@govern.ad` |
| EPN central archive (PCAR00AND, RULL if EPN-registered) | `https://epncb.oma.be/` → data access | Free with EPN data registration |
| ERGNSS RINEX (Catalan border stations) | `https://www.ign.es/web/ign/portal/gds-gnss-tiempo-real` | Free with ergnss.ign.es registration |

## URLs Live-Probed 2026-05-17

| URL | Tool | Result |
|---|---|---|
| `https://www.cartografia.ad/` | WebFetch | 200, Catalan/Spanish landing page |
| `https://www.cartografia.ad/ergand` | WebFetch | 200, RULL+PCAR + `ergand@govern.ad` contact |
| `https://www.cartografia.ad/descripcio-dels-serveis` | WebFetch | 200, real-time + post-processing service description, GPS+GLO+GAL+BDS |
| `https://www.cartografia.ad/serveis-a-temps-real` | WebFetch | 200, full caster config (IPs, ports, mountpoints, credentials, RTCM types). Operator lists 3 RULL mounts — live sourcetable shows only 2 (see below); operator page is stale on the RTCM23 entry. |
| `https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-andorra/` | WebFetch | 200, confirms ERGAND as a free national service |
| `194.158.95.189:2101` (RULL caster) | curl --http0.9 | **`SOURCETABLE 200 OK`** — server `GR30 4.31.101/1.0`, 2 mounts: `RTCM3` (GPS+GLO), `RTCM32` (GPS+GLO+GAL+BDS) |
| `185.194.59.113:2101` (PCAR caster) | curl --http0.9 | **`SOURCETABLE 200 OK`** — server `GR50 4.80.109/1.0`, 2 mounts: `PCAR3` (GPS+GLO), `PCAR3M` (GPS+GLO+GAL+BDS) |
| `https://epncb.oma.be/_networkdata/data_access/real_time/broadcasters.php` | WebFetch | 403 |

## What Changed vs Prior Research

- Prior file claimed **"NO domestic caster"** — incorrect. ERGAND publishes a fully documented public NTRIP service on `cartografia.ad/serveis-a-temps-real` with two casters, four live mountpoints across two RTCM versions (3.x GPS+GLO, 3.2 MSM5), and openly-published credentials. Operator page still advertises a third RULL mount `RTCM23` (RTCM 2.3), but live sourcetable 2026-05-17 does not list it — operator page stale. This page exists in Catalan/Spanish and was not consulted in the prior pass.
- Prior file's "EUREF-IP is the only path" framing demoted to a cross-border alternative; ERGAND's own caster is the primary access route.
- ArduSimple's "Andorra has no established national RTK network" assertion (cited 2026-05-12) appears to be either out of date or was misread last pass — the current Ardusimple Andorra page explicitly lists ERGAND as a free national service.
- Removed unsupported claims about datum/epoch (no citable source found).

## Sources Consulted

- IDE Andorra i Cartografia (landing): `https://www.cartografia.ad/`
- ERGAND area: `https://www.cartografia.ad/ergand`
- ERGAND real-time services: `https://www.cartografia.ad/serveis-a-temps-real`
- ERGAND service description: `https://www.cartografia.ad/descripcio-dels-serveis`
- ArduSimple Andorra: `https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-andorra/`
- IGN Spain ERGNSS portal: `https://www.ign.es/web/ign/portal/gds-gnss-tiempo-real`
- ERGNSS registration: `http://ergnss.ign.es/gnuserportal/`
- EPN Central Bureau: `https://epncb.oma.be/` (broadcasters / status / maps pages all returned 403 to this sandbox 2026-05-17)
- EUREF-IP @ ROB: `https://www.euref-ip.be/`
- BKG broadcaster: `https://euref-ip.net/home`
- Centipede-RTK map: `https://map.centipede-rtk.org/`
- Local data verification (2026-05-17): `scripts/stations_by_country.py AND` (no entries), `scripts/stations_by_radius.py 42.54 1.60 50` (no stations within 50 km)
