# Togo [TG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: CORS network announced March 2026 — installation phase; NO active public NTRIP caster yet

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — nationwide CORS installation announced 9 March 2026; service not yet operational |
| **host:port** | null — no caster announced |
| **tariff** | null |
| **hobbyist_eligibility** | null — pre-operational |
| **legal_residency_required** | null — pre-operational |
| **last_confirmed_alive** | null — no caster |

## Most Recent Project Announcement

**9 March 2026:** Government of Togo announced a comprehensive reform of the national geodetic reference system, including installation of a nationwide CORS network and establishment of standardised geodetic benchmarks (levelling) across the country. The reform is intended to standardise spatial data and enable centimetre-level GNSS positioning for surveying, urban planning (Lomé), cadastre, precision agriculture, and disaster risk reduction.

The announcement aligns with broader African Union and international geodetic body efforts to modernise West African national spatial data infrastructure.

- GIS Resources report (2026-03-12): https://gisresources.com/togo-launches-national-cors-network-and-geodetic-reference-system-to-standardise-spatial-data/
- Source agencies cited: Ecofin Agency, Togo First (2026-03-09)

## Context Notes

- **Scope of announcement:** Nationwide CORS installation + national geodetic reference system reform + vertical datum (levelling benchmarks). No operator name, station count, or NTRIP caster details have been published.
- **Timeline:** The project is in the announcement / early installation phase as of May 2026; no operational date has been stated publicly.
- **Existing GNSS presence:** Prior to this announcement, Togo had at most a handful of IGS-class stations for scientific purposes; no national RTK network existed.
- **Regional context:** Neighbouring Benin has a 7-station CORS network (RTK-capable since 2022); Ghana operates a national CORS network. Togo's announcement follows this West African trend.
- **Global commercial networks:** No Togo coverage confirmed for GEODNET, ONOCOY, Centipede-RTK, or PointOne.
- Practical workaround: Deploy a local base station for single-base RTK; use PPP (Galileo HAS, Trimble RTX); monitor gisresources.com for CORS network go-live announcements.

## Post-Processing (RINEX) Fallback

No confirmed publicly accessible CORS RINEX archive for Togo found. The incoming CORS network may eventually provide RINEX archiving.

## Sources Consulted
- GIS Resources announcement (https://gisresources.com/togo-launches-national-cors-network-and-geodetic-reference-system-to-standardise-spatial-data/)
- RTK2GO monitor (monitor.use-snip.com) — no Togo mount points
- NTRIP-list.com Africa page — no Togo entries
- ArduSimple country selector — Togo not listed as having national RTK network
- AFREF literature — no active Togo CORS entry found
- GEODNET, ONOCOY — no Togo coverage confirmed
