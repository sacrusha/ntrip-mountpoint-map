# Greenland [GL] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (refresh of 2026-05-12 entry; go-gnet.org page fetched 2026-05-17 — still post-processing only, no real-time NTRIP service mentioned; no datum/epoch declared on landing page)

## Status: NO — no public NTRIP RTK caster; GNET infrastructure exists for post-processing only

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No (no Greenland-operated caster); real-time IGS-IP coverage of select Greenland IGS sites exists via BKG (see "Real-time IGS-IP Coverage" below) |
| **landing_url — GNET** | https://go-gnet.org (post-processing portal; operator-owned) |
| **access_url — GNET** | https://dataforsyningen.dk (RINEX download; free, account required) |
| **host:port** | null — no Greenland-operated NTRIP caster |
| **num_stations — GNET** | ~55 stations per public GNET page (post-processing network operated jointly by Klimadatastyrelsen / KDS and DTU Space; not streamed as RTCM) |
| **vrs** | null — no NRTK service exists |
| **tariff** | null |
| **hobbyist_eligibility** | null — no Greenland NTRIP service; real-time fallback via IGS-IP (BKG account; free non-commercial), see below |
| **legal_residency_required** | null |
| **datum_epoch** | omitted — no citable declaration. go-gnet.org landing page (2026-05-17 fetch) does not declare a datum/epoch for the GNET network. |
| **last_confirmed_alive — caster** | null (none found) |
| **last_confirmed_alive — post-processing portal** | `go-gnet.org`: HTTP 200 confirmed 2026-05-12 (curl) · `asiaq.gl` homepage: 2026-05-01 |

## Context Notes

- **GNET** (Greenland GNSS Network, `go-gnet.org`) is the geodetic infrastructure for Greenland, operated jointly by the **Danish Agency for Climate Data (KDS / Klimadatastyrelsen)** and **DTU Space** — a two-party split documented on the GNET public page. The public GNET page enumerates approximately **55 stations** spread along Greenland's coast. GNET distributes RINEX 2/3 observation files via Dataforsyningen (`dataforsyningen.dk`) for post-processing only. No real-time RTCM/NTRIP stream is advertised at any GNET, KDS, or DTU Space URL.
- **Asiaq** (`asiaq.gl`, Greenland's survey and consulting institute) lists "Survey" and "Construction" services on its website but publishes no GNSS correction product or NTRIP endpoint.
- No Greenland entry appears on ntrip-list.com/europe, RTK2go, RTKdata, Radiodetection's Europe list, or ArduSimple's Denmark page. Verified 2026-05-12 against local `data/stations.json` — no GRL stations on rtk2go, Centipede, or EarthScope.

## Real-time IGS-IP Coverage (Practical Hobbyist Fallback)

Although Greenland operates no national NTRIP caster, **several Greenland IGS stations are real-time-capable and streamed via the BKG IGS-IP caster** (`www.igs-ip.net:2101`, free non-commercial registration). Per IGS station pages, the following Greenland sites publish a real-time RTCM stream on IGS-IP:

- **KELY** — Kellyville (W coast, near Kangerlussuaq, ~67.0 N / 50.9 W)
- **QAQ1** — Qaqortoq (S Greenland, ~60.7 N / 46.0 W)
- **SCOR** — Scoresbysund / Ittoqqortoormiit (E coast, ~70.5 N / 22.0 W)
- **SENU** — Sermilik / Sennusoq area (S Greenland)

For a hobbyist with a single dual-frequency receiver, these are the **only practical real-time correction streams covering Greenland today**. Constraints to flag for users:

- IGS-IP carries raw 1 Hz single-base RTCM (no NRTK / VRS); RTK degrades via ppm beyond ~10–30 km baseline (primer §accuracy).
- BKG account required (same credentials work for EUREF-IP); free non-commercial.
- Stations are sparse compared to a national NRTK network — useful only for users within ~30 km of one of the four sites above.

These streams are already ingested locally as part of the `igs_ip` source (see `scripts/stations_by_country.py --country GL` to enumerate from the current `data/stations.json` snapshot).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GNET / Dataforsyningen** — RINEX observation download | https://dataforsyningen.dk | Free (account required) |

## Contact for Follow-Up
- KDS (Klimadatastyrelsen / Danish Agency for Climate Data): kds@kds.dk · +45 (agency main)
- Asiaq: asiaq@asiaq.gl · +299 348800

## Sources Consulted
- GNET portal: https://go-gnet.org (re-probed 2026-05-12, HTTP 200)
- Asiaq website: https://asiaq.gl (2026-05-01)
- Klimadatastyrelsen: https://eng.klimadatastyrelsen.dk (2026-05-01)
- Dataforsyningen GNSS data: https://dataforsyningen.dk (2026-05-01)
- ntrip-list.com/europe (2026-05-12 — no GL entry)
- RTK2go map (2026-05-12 — no GL entry)
- ArduSimple Denmark NTRIP page (2026-05-01)
- WebSearch 2026-05-12 ("Greenland GNET NTRIP RTK real-time correction caster 2026") — no real-time stream surfaced; only post-processing remains
