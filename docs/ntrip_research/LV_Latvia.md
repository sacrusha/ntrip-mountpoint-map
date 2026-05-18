# Latvia [LV] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; service unchanged since 2026-05-12; sandbox live probe returned HTTP 000 today, content corroborated via prior 2026-05-12 SOURCETABLE 200 OK)

## Status: YES — free government NTRIP caster (LatPos) operating

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (LatPos — free since 2018) |
| **landing_url — LatPos** | `https://www.lgia.gov.lv/en/latpos` — operator-owned LatPos info page on the LGIA agency site (EN; LV variant at `/lv/latpos`). Describes the service, free-access policy, station network. |
| **access_url — LatPos** | Skip — landing_url describes the registration path. The SBC entry at `https://latpos.lgia.gov.lv/SBC/Account/Register` is a bare registration form with no service description. |
| **host:port — LatPos** | `latpos.lgia.gov.lv:5001` (IP: 91.216.2.20) |
| **VRS** | Yes — network RTK corrections; 27 Latvian + 5 Estonian + 4 Lithuanian base stations enable network-level solution. 7 mountpoints exposed: `SITE` (nearest single base, GPS+GLO RTCM 3), `NETW-MAX` (master-auxiliary RTCM 3 GPS+GLO), `NETW-iMAX` (iMAX GPS+GLO), `VIRTUAL-RS` (VRS RTCM 3 extended GPS+GLO), `SITE-BeiDOU` (GPS+GLO+BDS), `NETW-iMAX-BeiDOU` (iMAX GPS+GLO+BDS), `VRS-BeiDOU` (VRS GPS+GLO+BDS) |
| **tariff** | Free — explicit free-access policy in force since 2018 ("government-supported maintenance and open access") |
| **hobbyist_eligibility** | yes — any user may register; no professional licensing stated |
| **legal_residency_required** | unclear — not explicitly required; free public service with registration. Sign-up portal available at `https://latpos.lgia.gov.lv/SBC/Account/Register` |
| **last_confirmed_alive** | 2026-05-12 — `curl --http0.9 http://latpos.lgia.gov.lv:5001/` returned `SOURCETABLE 200 OK` (Server: `GNSS Spider 7.11.1.109/1.0`, Latvian-language Date header `Otrd., 12 maijs 2026`, Content-Length 768); 7 STR rows confirmed |
| **datum_epoch** | omitted — no citable declaration (LKS92 tied to ETRS89 mentioned in prose context but not as an operator-cited datum/epoch declaration; LGIA's LatPos pages do not expose the reference-frame statement) |

## Context Notes

- **LatPos**: Permanent GNSS reference station network operated by the Latvian Geospatial Information Agency (LGIA / Latvijas Ģeotelpiskās informācijas aģentūra). Made free to all registered users in 2018.
- **Infrastructure**: 27 base stations in Latvia, 5 in Estonia, 4 in Lithuania operating continuously. Distributes corrections via mobile internet (GPRS/UMTS/4G). Signals from GPS, GLONASS, Galileo, BeiDou.
- **Real-time accuracy**: ~2 cm horizontal in real-time; ~5 mm in post-processing.
- **Access**: Registration required via the LatPos SBC (Spider Business Center) portal. Users must accept LatPos terms of use before account activation. Portal navigation reportedly not user-friendly.
- **Note from country-survey.md**: In CI, latpos.lgia.gov.lv port 5001 had been timing out (suspected egress firewall on non-standard port from some external networks); the caster has responded reliably from this research environment on both 2026-05-06 and 2026-05-12.
- **Volunteer presence on rtk2go / Centipede**: `py scripts/stations_by_country.py LVA` returns 3 rtk2go pins (`Bracas` 57.07,24.83; `KALSNAVA` 56.73,25.96; `mnt239_1` 56.90,24.19) and 1 Centipede pin (`RIGA` 56.905,24.191). These are unofficial — LatPos is the authoritative service.
- **Operator contact**: LGIA, Rīga; service email `latpos@lgia.gov.lv`; agency portal `https://www.lgia.gov.lv/en`

## Post-Processing (RINEX) Fallback

RINEX data available via LatPos portal at no cost after registration.

## Sources Consulted
- LatPos page (LGIA): https://www.lgia.gov.lv/en/latpos and https://www.lgia.gov.lv/en/latpos-0
- LatPos sign-up portal: https://latpos.lgia.gov.lv/SBC/Account/Register
- Alberding caster map (LatPos): https://www.alberding.eu/cgi-bin/map.cgi?caster=latpos.lgia.gov.lv&port=5001&lang=en&gencgi=1
- ArduSimple Latvia RTK page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-latvia/
- Inside GNSS article on LatPos free access: https://insidegnss.com/latvias-latpos-network-consolidates-free-access-and-operational-resilience/
- Older LGIA LatPos page (legacy URL still live): http://map.lgia.gov.lv/index.php?lang=2&cPath=2&txt_id=13
- Live caster probe (2026-05-12): `curl --http0.9 http://latpos.lgia.gov.lv:5001/` → SOURCETABLE 200 OK; 7 STR rows; Server `GNSS Spider 7.11.1.109/1.0`
- Local pipeline check (2026-05-12): `py scripts/stations_by_country.py LVA` returns 3 rtk2go + 1 Centipede LV pins (Bracas, KALSNAVA, mnt239_1, RIGA)
