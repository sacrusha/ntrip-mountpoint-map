# Madagascar [MG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (refreshed 2026-05-12)

## Status: NO national caster; 2 Centipede-RTK volunteer bases active (caster.centipede.fr:2101)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster (national)** | No |
| **Volunteer (Centipede-RTK)** | 2 bases tagged `MDG` in caster.centipede.fr:2101 sourcetable: `MAHA` (-15.711, 46.338 — near Mahajanga/north-west coast) and `MIRACAD` (-18.822, 47.441 — near Antananarivo). Verified via `py scripts/stations_by_country.py MDG` on 2026-05-12. |
| **host:port (Centipede)** | `caster.centipede.fr : 2101` — free, registration required at centipede-rtk.org |
| **rtk2go / EarthScope** | No Madagascar stations in either source on 2026-05-12 |
| **tariff** | Centipede: free (volunteer/research network) |
| **hobbyist_eligibility** | Centipede: yes — open to anyone; register at centipede-rtk.org |
| **legal_residency_required** | No (Centipede is open globally) |
| **last_confirmed_alive** | 2026-05-12 — MAHA and MIRACAD present in current Centipede sourcetable per local data |

## Most Recent Project Announcement

**IOGA4MET-EI expansion** (c. 2019–2020): Five permanent Trimble NetR9 GNSS stations deployed across Madagascar as part of the INTERREG-5 Indian Ocean "ReNovRisk Cyclones and Climate Change" project. These are research stations for tropospheric water-vapor sensing — they do NOT expose NTRIP mountpoints for RTK corrections.

Stations: DSUA (Antsiranana), MASM (Sainte-Marie), MATA (Toamasina), MAFD (Tôlanaro), NOSY (Nosy Be)

**Source URL:** https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2020.566105/full

**AFREF Workshop 2024** (August 12–15, 2024): Geodetic capacity-building across Africa including Madagascar participation; no NTRIP caster launch announced.
**Source URL:** https://ric2024.rcmrd.org/afref

## Context Notes

- **Centipede-RTK volunteer coverage**: Two community-operated bases reachable on `caster.centipede.fr:2101`:
  - `MAHA` near Mahajanga (-15.711, 46.338) — covers parts of north-west Madagascar within ~35 km
  - `MIRACAD` near Antananarivo (-18.822, 47.441) — covers central highlands / capital region within ~35 km
  Coastal south, far north, and east are not covered.
- **FTM** (Foiben-Taosarintanin'i Madagasikara, national mapping agency): No evidence of operating or planning a public NTRIP caster.
- **AFREF**: Madagascar reportedly has at least one CORS station contributing RINEX data for post-processing — not RTK.
- **ASECNA SBAS**: Covers Madagascar for aviation sub-meter accuracy — excluded (DGNSS/SBAS only).
- Global commercial networks (GEODNET, ONOCOY, Trimble RTX, Point One): No confirmed Madagascar coverage.
- Practical reality: Within ~35 km of Antananarivo or Mahajanga, use the Centipede MIRACAD/MAHA base; elsewhere, use a local owned base station or post-process against AFREF/IGS RINEX archive.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGS/CDDIS** (NASA) — global IGS archive; Madagascar AFREF station(s) if contributed | https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/daily_30second_data.html | Free (NASA Earthdata account required) |
| **RGP** (French IGN) — archives IOGA4MET station data (DSUA, MASM, MATA, MAFD, NOSY) | https://rgp.ign.fr/ | Free |

## Sources Consulted
- py scripts/stations_by_country.py MDG (2026-05-12) — Centipede has 2 Madagascar stations: MAHA (-15.711, 46.338) and MIRACAD (-18.822, 47.441)
- Centipede-RTK official map: https://map.centipede-rtk.org/ — confirms collaborative global coverage; specific MDG entries verified via local sourcetable
- Centipede-RTK home: https://www.centipede-rtk.org/
- RTK2GO sourcetable (rtk2go.com:2101) — no MDG entries
- SNIP Monitor
- NTRIP-list Africa (ntrip-list.com/africa/)
- IGS Network (network.igs.org)
- GAGE/UNAVCO
- GEODNET, ONOCOY, TrigNet, Point One Navigation — no MG coverage
- UN-SPIDER AFREF Knowledge Portal
- GIM International CORS Africa map
- UN-GGIM Africa Activities Report 2025
