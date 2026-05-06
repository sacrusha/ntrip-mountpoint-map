# Colombia [CO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free national NTRIP caster (IGAC MAGNA-ECO); ~237–260+ stations; VRS available; registration required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | IGAC — Instituto Geográfico Agustín Codazzi, Centro de Control Geodésico Nacional |
| **host:port** | `sbc.igac.gov.co:2101` |
| **VRS** | Yes — network RTK corrections available via Leica Spider Business Center (SBC) platform |
| **tariff** | **Free — COP 0 / $0.00.** Mandated by Law 1955/2019 (Plan Nacional de Desarrollo, Art. 281) as part of national spatial data infrastructure. Date observed: 2026-05-06. Source: https://redgeodesica.igac.gov.co/herramientas/servicios.html |
| **hobbyist_eligibility** | **Yes** — open registration; no professional licence requirement stated |
| **legal_residency_required** | **Unclear** — registration form requests national ID (cédula); foreign passport may be accepted; no explicit international block found |
| **last_confirmed_alive** | Spider Business Center portal (redgeodesica-sbc.igac.gov.co) HTTP 200 confirmed 2026-05-06; IGAC geodetic portal active 2026-05-06 |

## Registration Process

1. Go to `https://redgeodesica-sbc.igac.gov.co/sbc`
2. Create user account and confirm via email
3. Request a NTRIP subscription within the Spider Business Center (SBC) portal
4. Connect GNSS receiver to `sbc.igac.gov.co:2101` using confirmed credentials

## Network Details

- **Platform:** Leica Spider Business Center (SBC) — Spider is Leica's CORS network management software
- **Reference frame:** MAGNA-SIRGAS (Colombia's national geodetic reference frame; ITRF-aligned; ECO = Estaciones Continuas Operativas)
- **Stations:** ~237 CORS stations as of late 2023; ~260 by end-2024 (expansion ongoing — 26 new stations added in 2024 using Leica GR50 receivers + AR20 antennas; target ~300 nationally); 39 stations added 2022–2024 via Cuatro Conceptos contract
- **Coverage:** ~67% of municipalities as of 2023; priority areas include cadastral-deficient zones (Amazon, Pacific coast); Andean highlands and Caribbean coast better covered
- **Constellations:** GPS, GLONASS, Galileo, BeiDou (Leica GR50 multi-constellation)
- **Services offered:** Real-time NTRIP, VRS, online PPP, differential post-processing

## Context Notes

- IGAC launched the Centro de Control Geodésico Nacional formally in April 2024 (SIRGAS conference presentation), consolidating real-time NTRIP/VRS services under a single Leica SBC platform.
- Law 1955/2019 (Plan Nacional de Desarrollo 2018–2022, Art. 281) mandated free public access to the CORS/NTRIP service as part of Colombia's national spatial data infrastructure; this mandate has carried through subsequent plans.
- No independent private NTRIP network comparable to Chile's KollNET was identified in Colombia.
- Colombia is not present on RTK2go or Centipede volunteer sourcetables in any significant count.
- The SIRGAS April 2024 presentation describes VRS as available; the standard mountpoint for VRS is routed through the Spider SBC interface.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **IGAC CORS RINEX archive** — available via SBC portal | https://redgeodesica-sbc.igac.gov.co/sbc | Free (account required) |
| **SIRGAS regional archive** — includes Colombian CORS stations | https://sirgas.ipgh.org/ | Free |

## Sources Consulted
- IGAC Red Geodésica Nacional portal: https://redgeodesica.igac.gov.co/
- IGAC NTRIP services page: https://redgeodesica.igac.gov.co/herramientas/servicios.html
- IGAC Centro de Control Geodésico: https://igac-cc.azurewebsites.net/
- Spider Business Center login: https://redgeodesica-sbc.igac.gov.co/sbc
- SIRGAS Colombia RT presentation (Apr 2024): https://sirgas.ipgh.org/wp-content/uploads/2024/05/IGAC-Colombia-RT.pdf
- Revista Geodata — MAGNA-ECO densification: https://revistageodata.icde.gov.co/edicion-5/red-geodesica-nacional-activa-magna-eco-densificacion-y-cobertura-de-estaciones-cors-en
- IGAC 23 nuevas estaciones announcement: https://www.igac.gov.co/noticias/hay-23-nuevas-estaciones-para-la-red-geodesica-del-pais-su-informacion-es-util-para-el-catastro-multiproposito
- ArduSimple Colombia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-colombia/
- curl probe of sbc.igac.gov.co not attempted (ECONNREFUSED from outside Colombia on 2026-05-06); web portal HTTP 200 confirmed
