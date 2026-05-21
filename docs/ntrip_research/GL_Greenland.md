# Greenland [GL] — NTRIP RTK Caster Research

## Status: NO — no public NTRIP RTK caster; GNET infrastructure exists for post-processing only

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — no Greenland-operated caster; BKG IGS-IP carries zero GRL-tagged mountpoints per local sourcetable snapshot 2026-05-19 (IGS DB marks KELY/QAQ1 as RT-capable but current feed does not carry them; see "Real-time IGS-IP Coverage" below) |
| **Operator — GNET** | Klimadatastyrelsen (KDS / Danish Agency for Climate Data) + DTU Space; Asiaq (Greenland Survey) assists in-country logistics |
| **landing_url — GNET** | https://go-gnet.org (post-processing portal; operator-owned) |
| **access_url — GNET** | https://dataforsyningen.dk (RINEX download; free, account required) |
| **host:port** | null — no Greenland-operated NTRIP caster |
| **num_stations — GNET** | ~71 stations (2025 ESSD preprint essd-2026-198: 71 stations across 67 unique locations, 19 town + 48 remote; go-gnet.org station list shows ~73 entries as of 2026-05-17; the prior "~55 stations per public GNET page" figure is stale). Post-processing network operated jointly by Klimadatastyrelsen / KDS and DTU Space with support from the EarthScope Consortium (ESC); not streamed as RTCM. |
| **vrs** | null — no NRTK service exists |
| **tariff** | null |
| **hobbyist_eligibility** | null — no Greenland NTRIP service; no confirmed real-time free path (BKG IGS-IP carries 0 GRL streams per 2026-05-19 sourcetable; post-processing via Dataforsyningen only) |
| **legal_residency_required** | null |
| **datum_epoch** | omitted — no citable declaration. go-gnet.org landing page (2026-05-17 fetch) does not declare a datum/epoch for the GNET network. |
| **last_confirmed_alive — caster** | null (none found) |
| **last_confirmed_alive — post-processing portal** | `go-gnet.org`: HTTP 200 confirmed 2026-05-21 · `asiaq.gl` homepage: 2026-05-01 |

## Context Notes

- **GNET** (Greenland GNSS Network, `go-gnet.org`) is the geodetic infrastructure for Greenland, operated jointly by the **Danish Agency for Climate Data (KDS / Klimadatastyrelsen)**, **DTU Space**, and with support from the **EarthScope Consortium (ESC)**. The 2025 ESSD preprint (essd-2026-198) states **71 stations across 67 unique locations** (19 town + 48 remote); the earlier "~55 stations per public GNET page" figure is stale. GNET distributes RINEX 2/3 observation files via Dataforsyningen (`dataforsyningen.dk`) for post-processing only. No real-time RTCM/NTRIP stream is advertised at any GNET, KDS, or DTU Space URL.
- **Asiaq** (`asiaq.gl`, Greenland's survey and consulting institute) lists "Survey" and "Construction" services on its website but publishes no GNSS correction product or NTRIP endpoint.
- No Greenland entry appears on ntrip-list.com/europe, RTK2go, RTKdata, Radiodetection's Europe list, or ArduSimple's Denmark page. Verified 2026-05-12 against local `data/stations.json` — no GRL stations on rtk2go, Centipede, or EarthScope.

## Real-time IGS-IP Coverage

**No practical real-time hobbyist NTRIP in Greenland confirmed today.**

Local sourcetable snapshots (data/igs_ip.sourcetable + data/euref_ip.sourcetable, 2026-05-19) contain **zero GRL-tagged mountpoints**. The IGS network database marks KELY00GRL and QAQ1 as real-time-capable, but the current BKG IGS-IP feed does not carry them. No other public caster carries Greenland streams per project sourcetable archive.

Post-processing via Dataforsyningen RINEX (account required) remains the only confirmed free path.

KELY/QAQ1/SCOR: IGS DB marks these as RT-capable but BKG IGS-IP feed does not carry them per 2026-05-19 sourcetable snapshot.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GNET / Dataforsyningen** — RINEX observation download | https://dataforsyningen.dk | Free (account required) |

## Sources Consulted
- GNET portal: https://go-gnet.org (re-probed 2026-05-21, HTTP 200)
- ESSD preprint essd-2026-198 (2025): 71 stations, 67 unique locations, 19 town + 48 remote — canonical station count source
- Local sourcetable snapshots data/igs_ip.sourcetable + data/euref_ip.sourcetable (2026-05-19): 0 GRL-tagged mountpoints on BKG IGS-IP
- Asiaq website: https://asiaq.gl (2026-05-01)
- Klimadatastyrelsen: https://eng.klimadatastyrelsen.dk (2026-05-01)
- Dataforsyningen GNSS data: https://dataforsyningen.dk (2026-05-01)
- ntrip-list.com/europe (2026-05-12 — no GL entry)
- RTK2go map (2026-05-12 — no GL entry)
- ArduSimple Denmark NTRIP page (2026-05-01)
- WebSearch 2026-05-12 ("Greenland GNET NTRIP RTK real-time correction caster 2026") — no real-time stream surfaced; only post-processing remains
