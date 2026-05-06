# Thailand [TH] — NTRIP RTK Caster Research
**Date researched:** 2026-05-04

## Status: YES — DOL LandGNSS / RTK GNSS Network operational; currently free trial; Thai national ID required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **operator** | Thailand Department of Lands (กรมที่ดิน, DOL), Division of Mapping Technology, Ministry of Interior |
| **portal** | https://dol-rtknetwork.com |
| **host:port — Central zone** | `122.155.131.34:2101` (Bangkok, Nonthaburi, surrounding provinces) |
| **host:port — other zones** | Same IP `122.155.131.34`, zone-specific port; full port list in zone PDF (URL currently 404); contact dol.rtknetwork@gmail.com for other regions |
| **mountpoint** | `VRS_RTCM32` (Network-RTK / VRS; RTCM 3.2) |
| **tariff** | Currently free trial ("ทดลองใช้งาน") — no published fee schedule; a DOL procurement document (dol.go.th/media/2026/03, 403 Forbidden) references a future credit/billing system; whether a paid tier has activated as of 2026-05-04 is unknown |
| **hobbyist_eligibility** | Yes — "ประชาชนทั่วไป" (general public) is an explicit registration category; no surveying licence required |
| **legal_residency_required** | Yes in practice — registration and NTRIP login use 13-digit Thai national ID; no pathway for foreigners without a Thai citizen ID documented |
| **last_confirmed_alive** | 2026-05-04 — portal, login page, and public registration page all loaded correctly |

## Context Notes

- The network is officially named **ระบบโครงข่ายการรังวัดด้วยดาวเทียมแบบจลน์ RTK GNSS Network** (LandGNSS / RTK GNSS Network). It delivers VRS/Network-RTK corrections, not single-base or DGNSS-only.
- A KM DOH user guide (October 2023) confirms public registration is available and free of charge at that time. A Satlab Thailand Facebook post (~2019) described the service as having "no fees or additional charges." A 2026-03 DOL procurement TOR indexed by Google references per-user credit/fee tracking — this may signal a future paid tier but was not confirmed active.
- The port-zone PDF at `https://dol-rtknetwork.com/files/manual/1(PortNumber).pdf` returned 404 on 2026-05-04; zone ports other than Central (2101) are not publicly confirmed.
- The DOLNet monitoring dashboard at `dol-dms.com:8080` returned a connection error on 2026-05-04.
- The ArduSimple Thailand NTRIP page (updated 2026-04-05) incorrectly states no national RTK network exists in Thailand — it has not indexed the DOL service.

## Sources Consulted
- DOL RTK Network portal: https://dol-rtknetwork.com/ (login, registration, regulations pages; observed 2026-05-04)
- Registration page: https://dol-rtknetwork.com/index.php/register_gnss_beta
- KM DOH user guide (Oct 2023): km.doh.go.th (site unreachable 2026-05-04; indexed by Google)
- Port/zone document (404): https://dol-rtknetwork.com/files/manual/1(PortNumber).pdf
- ArduSimple Thailand page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-thailand/ (updated 2026-04-05)
- Contact: dol.rtknetwork@gmail.com / +66 2503 3367
