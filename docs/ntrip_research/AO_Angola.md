# Angola [AO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: Physical CORS exists (REPANGOL) — NO confirmed public NTRIP endpoint

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No |
| **host:port** | null — no NTRIP caster endpoint ever publicly documented |
| **tariff** | null |
| **hobbyist_eligibility** | null — no service exists |
| **legal_residency_required** | null — no service exists |
| **last_confirmed_alive** | null — REPANGOL website (repangol.net) returned ECONNREFUSED on 2026-05-06 |

## Existing CORS Infrastructure — REPANGOL

| Detail | Value |
|--------|-------|
| **Network name** | REPANGOL (Rede de Estações Permanentes GNSS de Angola) |
| **Operator** | IGCA (Instituto Geográfico e Cadastral de Angola) |
| **Stations** | 18 permanent CORS stations |
| **Installed** | 2010 (geodetic observations 2010–2011) |
| **Reference frame** | ITRF2008 |
| **Maintenance** | TeroMovigo (maintenance completed 2020) |
| **Website** | http://www.repangol.net/ — **offline / ECONNREFUSED** as of 2026-05-06 |
| **Published purpose** | Geodetic reference frame; post-processing support — no public real-time RTK/NTRIP documented |

IGCA website (igca.gov.ao) online as of 2026-05-06 (last news item Sept 2025) — no mention of NTRIP, RTK, or REPANGOL real-time access.

## Most Recent Project Announcements

- **Decreto Presidencial n.º 115/21 (2021)**: Defines IGCA's mandate to manage and expand REPANGOL — no RTK service launch announced.
- **Angola–Russia GLONASS cooperation** (UN/Fiji 2019): Plans for GLONASS ground station in Luanda — no confirmed deployment or RTK output.
- **DGT Portugal / IGCA cooperation agreement**: Knowledge exchange in geodesy, cartography, cadastre — no confirmed NTRIP output.

No World Bank, AfDB, or Portuguese bilateral project on record has resulted in a live NTRIP service for Angola.

## Context Notes

- Angola appears in GIM International's 25-country Corsmap Africa exercise — confirming CORS hardware, but no real-time NTRIP stream documented.
- No AO mountpoints on RTK2GO, NTRIP-list.com Africa, corsstations.com, AFREF, IGS network, GEODNET, ONOCOY, or community CORS lists.
- MIRASpaco (Portuguese GNSS firm): acknowledges past CORS work in Angola but no public NTRIP access details published.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **REPANGOL** — 18-station network built for post-processing/geodetic reference; RINEX access via IGCA direct contact when website is restored | http://www.repangol.net/ (offline 2026-05-06) | Unknown — contact https://www.igca.gov.ao/ |

## Contact
IGCA — https://www.igca.gov.ao/

## Sources Consulted
- http://www.repangol.net/ (offline)
- https://www.igca.gov.ao/
- https://teromovigo.com/project/maintenance-of-repangol-network/
- ntrip-list.com/africa/, corsstations.com
- IGS network.igs.org, RTK2GO
- GIM International CORS Africa map
- GitHub mvarga1989 CORS list
- ArduSimple country directory
