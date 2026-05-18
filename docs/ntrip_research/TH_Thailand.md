# Thailand [TH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified from 2026-05-13 — dol-rtknetwork.com homepage HTTP 200; Thai-ID-only registration unchanged; trial / no published fee unchanged)

## Status: YES — DOL LandGNSS / RTK GNSS Network operational; currently free trial ("ทดลองใช้งาน"); Thai national ID required to register, no foreigner path

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **operator** | Thailand Department of Lands (กรมที่ดิน, DOL), Division of Mapping Technology, Ministry of Interior |
| **portal** | https://dol-rtknetwork.com |
| **host:port — Central zone** | `122.155.131.34:2101` (Bangkok, Nonthaburi, surrounding provinces) |
| **host:port — other zones** | Same IP `122.155.131.34`, zone-specific port; full port list in zone PDF (URL still 404 on 2026-05-13); contact `dol.rtknetwork@gmail.com` for other regions |
| **mountpoint** | `VRS_RTCM32` (Network-RTK / VRS; RTCM 3.2) |
| **tariff** | Currently free trial ("ทดลองใช้งาน") — no published fee schedule. A DOL procurement document (dol.go.th/media/2026/03, 403 Forbidden) references a future credit / billing system; whether a paid tier has activated as of 2026-05-13 is still unknown |
| **hobbyist_eligibility** | Yes — "ประชาชนทั่วไป" (general public) is an explicit registration category in the form; no surveying licence required |
| **legal_residency_required** | Yes in practice — the registration form **explicitly requires a 13-digit Thai national ID** ("หมายเลขบัตรประจำตัวประชาชน"); no alternative identifier (passport, work-permit number) is accepted. Reconfirmed 2026-05-13 from `dol-rtknetwork.com/index.php/register_gnss_beta` |
| **last_confirmed_alive** | 2026-05-17 — `dol-rtknetwork.com` home HTTP 200; portal returned LandGNSS Thai-language header (login + registration not re-probed this pass; last full registration form inspection 2026-05-13) |

## Registration Requirements (reconfirmed 2026-05-13)

The DOL registration form (`dol-rtknetwork.com/index.php/register_gnss_beta`) mandates:

- Full name
- Thai national ID (13 digits, no alternative)
- Address
- Email
- Phone number (digits only)
- Purpose of use (land surveying / construction / hydrographic surveying / other)
- Organization type (government agency / partnership-company / general public)
- Supporting document (national-ID photo or employee card upload)

Foreigners without a Thai national-ID card are effectively excluded by the form's validation. No alternate (e.g. passport / work-permit) registration pathway is documented.

## Volunteer (rtk2go) Coverage Inside Thailand

For users who cannot obtain a Thai national ID, three community rtk2go bases are operating in Thailand (cross-checked 2026-05-13 via `py scripts/stations_by_radius.py 13.75 100.5 300`):

| Mountpoint | Lat | Lon | Distance from Bangkok | Notes |
|---|---:|---:|---:|---|
| `TH-Kukot` | 13.96 | 100.65 | ~28 km N of central Bangkok | Bangkok metropolitan |
| `sylvania` | 13.28 | 101.38 | ~109 km SE of Bangkok | Chonburi / Rayong area |
| `LivingOnCrypto` | 15.46 | 100.26 | ~192 km N of Bangkok | Central plain (Nakhon Sawan area) |

All accessible at `rtk2go.com:2101` after an rtk2go email registration; single-base RTCM 3 streams, free under SNIP fair-use. Reliability is operator-dependent — check `monitor.use-snip.com` before fieldwork.

## Context Notes

- The network is officially named **ระบบโครงข่ายการรังวัดด้วยดาวเทียมแบบจลน์ RTK GNSS Network** (LandGNSS / RTK GNSS Network). It delivers VRS / Network-RTK corrections, not single-base or DGNSS-only.
- A KM DOH user guide (October 2023) confirms public registration is available and free of charge at that time. A Satlab Thailand Facebook post (~2019) described the service as having "no fees or additional charges." A 2026-03 DOL procurement TOR indexed by Google references per-user credit / fee tracking — this may signal a future paid tier but was not confirmed active.
- The port-zone PDF at `https://dol-rtknetwork.com/files/manual/1(PortNumber).pdf` was 404 on 2026-05-13; zone ports other than Central (2101) remain not publicly confirmed.
- The DOLNet monitoring dashboard at `dol-dms.com:8080` returned a connection error on 2026-05-04 and could not be re-verified in this session.
- The ArduSimple Thailand NTRIP page (updated 2026-04-05) incorrectly states no national RTK network exists in Thailand — it has not indexed the DOL service.

## Sources Consulted
- DOL RTK Network portal: https://dol-rtknetwork.com/ (login, registration, regulations pages; reconfirmed 2026-05-13)
- Registration page: https://dol-rtknetwork.com/index.php/register_gnss_beta — Thai national ID requirement reconfirmed 2026-05-13
- News / main info page: https://dol-rtknetwork.com/index.php/npage
- KM DOH user guide (Oct 2023): km.doh.go.th (site unreachable 2026-05-13; indexed by Google)
- Port / zone document (404): https://dol-rtknetwork.com/files/manual/1(PortNumber).pdf
- ArduSimple Thailand page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-thailand/ (last updated 2026-04-05)
- `data/stations.json` cross-check (`py scripts/stations_by_radius.py 13.75 100.5 300`) — TH-Kukot, sylvania, LivingOnCrypto rtk2go bases inside TH territory
- Contact: dol.rtknetwork@gmail.com / +66 2503 3367
