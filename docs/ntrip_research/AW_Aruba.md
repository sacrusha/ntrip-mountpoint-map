# Aruba [AW] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: NO national NTRIP caster; 1 rtk2go volunteer base (PINOST1) + 1 EarthScope NOTA station (CN19) provide partial free coverage

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No national service. Free coverage = 1 rtk2go base + 1 EarthScope NOTA stream |
| **Volunteer rtk2go coverage** | Yes — **PINOST1** (Santa Cruz area, 12.50°N, −69.98°W, country code `ABW`); single base via `rtk2go.com:2101` |
| **EarthScope / NOTA coverage** | Yes — **CN19_RTCM3P3** (NW Aruba near California Lighthouse, 12.61°N, −70.05°W); stream via `ntrip.earthscope.org:2101` under NULA non-commercial licence |
| **Free RINEX / post-processing** | Yes — via EarthScope (CN19 RINEX archive) and historical UNAVCO COCONet datasets |
| **hobbyist_eligibility** | rtk2go PINOST1: yes (open, no registration). EarthScope: yes, free non-commercial after EarthScope account |
| **legal_residency_required** | No — both free paths are accessible globally |
| **last_confirmed_alive** | 2026-05-12 — PINOST1 present in `data/stations.json` rtk2go snapshot; CN19 present in EarthScope station list (re-verified from `data/stations.json`) |
| **Most recent project announcement** | None found 2024–2026; CN19 continues per EarthScope's NOTA transition to the new streaming platform |

## Coverage Geometry

Aruba is ~30 km × 9 km. Two free bases — PINOST1 (centre / Santa Cruz) and CN19 (NW coast) — are ~16 km apart and together cover the entire island within typical RTK baseline (<20 km). Either station alone provides usable cm-level positioning over essentially the whole island.

## Context Notes

- **No national RTK service in Aruba.** Aruba (ISO 3166-1 AW) is an autonomous constituent country of the Kingdom of the Netherlands but is **not** covered by Kadaster/NSGI AGRS.BES, which serves only the BES special municipalities (Bonaire, Sint Eustatius, Saba). Aruba, Curaçao, and Sint Maarten have separate constitutional status and are not in AGRS.BES. See `CW_Dutch_Caribbean.md` and `BQ_Bonaire.md`.
- **COCONet / NOTA CN19**: Installed by UNAVCO engineers 2–9 June 2013 in cooperation with the Meteorological Department of Aruba, near California Lighthouse on Aruba's NW tip. Part of EarthScope's Network of the Americas (NOTA). Real-time RTCM 3 stream confirmed in current `data/stations.json` snapshot under mountpoint `CN19_RTCM3P3`.
- **PINOST1 (rtk2go)**: Volunteer base in Santa Cruz, Aruba. Visible in `data/stations.json` under country code `ABW`. As with all rtk2go nodes, uptime and signal quality depend on the host; check `monitor.use-snip.com` for live status before relying on it.
- **Aruba government survey capacity**: The Department for Infrastructure Management and Planning (DIP, `gobierno.aw`) handles survey and land registration. No CORS or RTK network infrastructure is found on the public site.
- **Cross-border alternatives within ~50 km**: None. The nearest cross-border free streams (AGRS.BES on Bonaire via `ntrip.kadaster.nl:2101`) are ~130 km east — well beyond usable RTK baseline range. Practical fallback if both PINOST1 and CN19 are down: deploy a local base/rover pair, or use Galileo HAS (~40 cm) or a commercial PPP service.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / NOTA** — CN19 RINEX archive | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA) |
| **UNAVCO GNSS data portal** — historical CN19 dataset | https://www.unavco.org/data/doi/10.7283/T5HD7SZB | Free |

## Sources Consulted
- UNAVCO COCONet CN19 Aruba installation report: https://www.unavco.org/news/unavco-installs-coconet-cgps-site-in-aruba/
- EarthScope NOTA network description: https://www.earthscope.org/nota/
- EarthScope new streaming platform announcement: https://www.earthscope.org/news/transition-to-new-real-time-gnss-streaming-platform/
- Kadaster BES sourcetable (no AW entries): http://ntrip.kadaster.nl:2101/sourcetable.htm
- NL_Netherlands.md and CW_Dutch_Caribbean.md research notes (AGRS.BES scope)
- Government of Aruba DIP: https://www.gobierno.aw/en/department-for-infrastructure-management-and-planning-dip-0
- `data/stations.json` 2026-05-12 — rtk2go `PINOST1` [ABW] (12.50, −69.98) and EarthScope `CN19_RTCM3P3` [ABW] (12.61, −70.05) confirmed present
- RTK2go monitor: http://monitor.use-snip.com/?hostUrl=rtk2go.com&port=2101 (TLS-cert mismatch from this env; check live status manually)
