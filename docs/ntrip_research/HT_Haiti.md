# Haiti [HT] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (re-verified 2026-05-12: no HTI entry in any source of data/stations.json; no public NTRIP announcement found in web searches; status unchanged)

## Status: NO active public NTRIP caster

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — no public caster has ever been confirmed alive |

## Most Recent Project Announcement

**Date:** September 26, 2018
**Description:** Spectra Geospatial / Ashtech donation article — CNIGS and partners stated intention to expand from a single Port-au-Prince CORS station to a national NTRIP CORS system throughout Haiti. No implementation date given; no subsequent public update found.
**URL:** https://spectrageospatial.com/haiti-reconstruction-aid-with-ashtech-donation/

Earlier planning document (2015 SIRGAS): 23-station national CORS network planned with Trimble NetR9 + Pivot + VRS, target end of 2016 — never materialised.
**URL:** https://sirgas.ipgh.org/docs/Boletines/Bol20/11_Sauveur_2015_Geodetic_infrastructure_in_Haiti.pdf

## Context Notes

- **CNIGS** (Centre National de l'Information Géo-Spatiale): Website cnigs.ht was unreachable (ECONNREFUSED) at time of research; no documented RTK/NTRIP service found.
- **COCONet stations**: CN09 (Cap-Haïtien) and JME2 (Petit-Goâve) exist but feed post-processing RINEX archives via UNAVCO/EarthScope — not a public RTK stream. Marked "archival only."
- **2010 earthquake response**: UNAVCO installed 6 Trimble NetRS continuous GPS stations; NTRIP streaming was noted as a "future possibility" only.
- **Practical workaround**: Field surveys in Haiti use satellite-delivered PPP corrections (Atlas/Trimble RTX, u-blox PointPerfect) or local owned base stations.
- Global commercial networks (GEODNET, ONOCOY, Centipede-RTK, RTK2GO): No Haiti mountpoints found in any index.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope GNSS Data Archive** — COCONet stations CN09 (Cap-Haïtien) and JME2 (Petit-Goâve); archival RINEX only | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA); $1,000/seat/yr commercial |

## Sources Consulted
- RTK2GO sourcetable (rtk2go.com:2101)
- NTRIP-list.com (North America + South America pages)
- corsstations.com, ArduSimple country DB
- COCONet / GAGE/UNAVCO real-time data
- SONEL GNSS station database
- BKG IGS NTRIP (igs-ip.net, euref-ip.net)
- CNIGS website (cnigs.ht) — offline
- Spectra Geospatial, SIRGAS 2015 proceedings
- Shadowserver accessible-NTRIP report
