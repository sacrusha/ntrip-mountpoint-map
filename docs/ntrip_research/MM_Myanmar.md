# Myanmar [MM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-12)

## Status: 10-station CORS built 2019 (Survey Department); no public NTRIP endpoint published externally

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No — internal Survey Department CORS exists; no public NTRIP endpoint published |
| **Network** | 10 CORS stations established 2019 by Myanmar Survey Department for the National Geodetic Reference Frame and RTK network; 3 of the 10 built to IGS-station guidelines (per UN-GGIM 10th Session country report). |
| **host:port** | null (not published externally) |
| **tariff** | null |
| **hobbyist_eligibility** | null — service not externally offered |
| **legal_residency_required** | null |
| **last_confirmed_alive** | null — no public NTRIP stream confirmed. The UN-GGIM country report (10th Session, 2020) confirms the 10-CORS network was operational; status post-2021 coup unknown. |

## Most Recent Project Announcement

- **2020 — UN-GGIM 10th Session country report (Myanmar)**: confirms Myanmar Survey Department established 10 CORS in 2019 for the National Geodetic Reference Frame and RTK network, of which 3 follow IGS-station construction guidelines. The Survey Department expressed intent to share CORS data to support nationally integrated geospatial information and monitoring of deformation in the cluster-plate region. URL: https://ggim.un.org/meetings/GGIM-committee/10th-Session/documents/Proforma_Agenda-item-6_Myanmar.pdf
- **Undated (circa 2018–2021):** Myanmar's Department of Survey (surveydepartment.gov.mm) held an "Introduction of GNSS CORS Network Application Ceremony," indicating that CORS infrastructure was officially launched for internal government use.
- **No subsequent public announcement** of a publicly accessible NTRIP RTK service has been found in English-language or Burmese-language searches as of 2026-05-12. The Feb 2021 coup and ongoing conflict make further announcements unlikely.
- Myanmar Survey Department website: http://www.surveydepartment.gov.mm/eng/ (accessibility intermittent).

## Context Notes

- Myanmar's Department of Survey (Ministry of Natural Resources and Environmental Conservation) is the mandated agency for geodetic CORS and GPS control stations. The 10-CORS network (2019) is documented in the official UN-GGIM country report but has no externally published NTRIP host/port, mountpoint list, or registration channel.
- The political crisis beginning in February 2021 has significantly disrupted government services and internet connectivity in Myanmar; any pre-existing NTRIP infrastructure may be inaccessible or non-operational. International sanctions further constrain availability of commercial RTK services.
- No commercial CORS/RTK network for Myanmar was found in any surveying-industry or hobbyist source.
- Global commercial networks (GEODNET, ONOCOY, PointOne, Centipede): no Myanmar coverage confirmed.
- **Nearest cross-border free RTK**: Centipede station BENGLA4 (22.27°N, 91.81°E) in Bangladesh ~430 km from Mandalay (per `py scripts/stations_by_radius.py 21.9 95.96 500` on 2026-05-12) — far beyond practical single-base RTK range (~35 km).
- Practical workaround: Deploy a local base station, or use satellite-based PPP (Trimble RTX, Galileo HAS — limited coverage at low latitudes in Asia, NRCAN PPP).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope/GAGE archive** — regional IGS-affiliated stations (limited in Myanmar) | https://www.unavco.org/data/gps-gnss/ | Free non-commercial |

## Sources Consulted
- Myanmar Survey Department: http://www.surveydepartment.gov.mm/eng/
- UN-GGIM 10th Session — Myanmar country report (10 CORS, 2019, 3 to IGS standard): https://ggim.un.org/meetings/GGIM-committee/10th-Session/documents/Proforma_Agenda-item-6_Myanmar.pdf
- ArduSimple country RTK list (Myanmar not listed): https://www.ardusimple.com/rtk-correction-services-in-your-country/
- RTK2go monitor (no Myanmar stations observed)
- mvarga1989 GitHub GNSS CORS networks list (Myanmar not listed): https://github.com/mvarga1989/The-list-of-GNSS-CORS-RTK-networks
- GEODNET (no Myanmar coverage)
- EarthScope/GAGE (scientific stations only)
- py scripts/stations_by_radius.py 21.9 95.96 500 (2026-05-12) — only nearby free RTK is Centipede BENGLA4 (~430 km in Bangladesh)
