# Colombia [CO] — NTRIP RTK Caster Research
**Date researched:** 2026-05-22

## Status: YES — free national NTRIP RTK service (IGAC MAGNA-ECO) live on two ports; open registration; only free national RTK in Colombia

## igac — IGAC MAGNA-ECO

| Field | Value |
|---|---|
| **Operator** | IGAC — Instituto Geográfico Agustín Codazzi, Centro de Control Geodésico Nacional |
| **Network name** | MAGNA-ECO — Estaciones Continuas Operativas del Marco Geocéntrico Nacional MAGNA-SIRGAS |
| **landing_url** | https://redgeodesica.igac.gov.co/ (operator-owned portal, officialized by Resolución IGAC 1771 de 2024-11-01) |
| **access_url** | https://redgeodesica.igac.gov.co/herramientas/servicios.html (describes free access, host:port for ports 2101/2102, SBC registration workflow; more useful than the bare SBC registration form) |
| **host:port (network/VRS)** | `sbc.igac.gov.co:2101` — `SOURCETABLE 200 OK` 2026-05-22, Content-Length 3055, 28 STR mountpoints (Leica GNSS Spider 7.11.0.96) |
| **host:port (single-base)** | `sbc.igac.gov.co:2102` — `SOURCETABLE 200 OK` 2026-05-22, Content-Length 15869, **144 STR mountpoints**; byte-identical to 2026-05-17, 2026-05-13, indicating no station-count change since mid-May |
| **tariff** | Free — COP 0. Mandate: Ley 1955/2019 (Plan Nacional de Desarrollo, Art. 281); free access policy restated on https://redgeodesica.igac.gov.co/herramientas/servicios.html (observed 2026-05-22). VAT N/A. |
| **num_stations** | 144 single-station mountpoints on port 2102 (2026-05-22). IGAC publicly cites a larger physical CORS inventory (~260 IGAC+SGC), of which 144 are piped into the public RTK service. |
| **vrs** | Yes — port 2101 advertises `MSM_VIRS`, `MSM_IMAX`, `MSM_NEAR`, plus legacy `RTCM3_VIRS / IMAX / NEAR`, `RTCM2_VIRS / IMAX / NEAR / DGPS / DGPS_VIRS / DGPS_IMAX`, `CMR_NEAR`, `CMRP_NEAR/IMAX/VIRS`, `Leica4G_NEAR`, and three regional cells `LLANOS_RTCM3`, `SUR_OESTE_RTCM3`, `NOROESTE_RTCM3` |
| **hobbyist_eligibility** | Yes — online registration via the Spider Business Center; no professional licence required; individual (persona natural) accounts available. Subscription request is gated by manual IGAC approval (see Registration); turnaround SLA + community-reported rejection rate not published |
| **legal_residency_required** | ? — SBC registration form accepts non-Colombian ID types in principle, but IGAC publishes no explicit statement on foreign-passport approvals. Real-world test not done. |
| **last_confirmed_alive** | 2026-05-22 — sourcetable fetches successful on both ports (2101 + 2102) |
| **datum_epoch** | omitted — no operator-portal declaration of the in-broadcast frame/epoch for the NTRIP service itself. MAGNA-SIRGAS 2018 is the official national datum (IGAC Resolución 715 de 2018, https://redgeodesica.igac.gov.co/documentos/resolucion_igac_715-2018.pdf) but the broadcast-frame declaration is not exposed on a freely-fetched page. Per primer `[datum-epoch]` rule (operator portal/spec/decree only), omit. |

## Registration

1. https://redgeodesica-sbc.igac.gov.co/sbc/Account/Register (Leica Spider Business Center)
2. Confirm email
3. Request NTRIP subscription ("Solicitar nueva suscripción")
4. After IGAC approval, connect rover to `sbc.igac.gov.co:2101` (network solutions) or `sbc.igac.gov.co:2102` (single-base)

## Network details

- **Platform:** Leica Spider Business Center; NTRIP caster software Leica GNSS Spider 7.11.0.96
- **Hardware (2024 densification):** Leica GR50 receivers + AR20 antennas per IGAC Resolución 1468 de 2021 specifications
- **Reference frame:** MAGNA-SIRGAS 2018 (national official datum per Resolución 715 de 2018); the NTRIP broadcast frame itself is not separately declared on the operator portal
- **Coverage:** Densest along Andean corridor (Bogotá–Medellín–Cali) and Caribbean coast; sparser in Amazon/Orinoco basins. Three regional VRS cells: LLANOS (eastern plains), SUR_OESTE (Pasto/Nariño), NOROESTE (Caribbean coast)
- **Constellations:** GPS+GLO+GAL+BDS on MSM mountpoints; GPS+GLO on most legacy RTCM3 single-base mountpoints; GPS-only on some RTCM2/DGPS variants
- **NMEA GGA:** Required upstream for VRS/IMAX/NEAR mountpoints on port 2101; not required for single-station mountpoints on port 2102

## Recent project announcements

- **Resolución IGAC 1771 de 2024-11-01** — officialized `redgeodesica.igac.gov.co` as the National Geodetic Network portal (https://www.igac.gov.co/transparencia-y-acceso-a-la-informacion-publica/normograma/resolucion-1771-de-2024)
- **April 2024** — Centro de Control Geodésico Nacional formally launched at SIRGAS conference (presentation: https://sirgas.ipgh.org/wp-content/uploads/2024/05/IGAC-Colombia-RT.pdf)
- **2022-2024 densification** — 39 new stations via Cuatro Conceptos contract; 26 stations installed in priority cadastral-deficient municipalities (Revista Geodata edición 5, https://revistageodata.icde.gov.co/edicion-5/red-geodesica-nacional-activa-magna-eco-densificacion-y-cobertura-de-estaciones-cors-en)

## Alternative networks

- **Servicio Geológico Colombiano GeoRED** — 105+ permanent GNSS stations for geodynamic monitoring (geored2.sgc.gov.co); processed in ITRF2014 via NASA Gipsy-X. **Post-processing only**, no real-time NTRIP service.
- **Topored** — Casa del Topógrafo commercial NTRIP network (28 stations across Panama and Colombia, control centre in Bogotá). Pricing not publicly listed; commercial, not free. Tracked in `docs/rtk_inventory.md` under `topored_pa`.
- **Volunteer / global coverage** — zero CO-coded rtk2go nodes; zero Centipede nodes (verified via `py scripts/stations_by_country.py COL` 2026-05-22: only IGAC + earthscope + igs_ip stations present). onocoy + GEODNET expose coverage only via their web explorers (no machine-readable country lists in public docs); neither has been confirmed to operate CO base stations as of 2026-05-22 — user must check explorer for current state.

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| IGAC MAGNA-ECO RINEX | https://redgeodesica-sbc.igac.gov.co/sbc (account required) | Free |
| SIRGAS regional archive | https://sirgas.ipgh.org/ | Free |
| SGC GeoRED archive (post-processing only, ITRF2014) | https://geored2.sgc.gov.co/ | Free |
| EarthScope (handful of CO stations) | https://www.earthscope.org/data/gnss-data/ | Free for non-commercial |

## Station-count dedup methodology

Canonical method for port-2102 station count (use for future re-counts):

```
curl --http0.9 http://sbc.igac.gov.co:2102/ \
  | grep '^STR;' \
  | awk -F';' '{print $10","$11}' \
  | sort -u \
  | wc -l
```

The 124/127/137 prior-count drift was a dedup-method artifact (rounding granularity); 143→144 at 2026-05-17 was a real new station; 2026-05-22 confirms 144 unchanged.

## Sources

- IGAC Red Geodésica Nacional portal: https://redgeodesica.igac.gov.co/
- IGAC NTRIP services page: https://redgeodesica.igac.gov.co/herramientas/servicios.html
- IGAC Geodesia FAQ: https://www.igac.gov.co/el-igac/areas-estrategicas/direccion-de-gestion-de-informacion-geografica/geodesia/preguntas-frecuentes-geodesia
- Spider Business Center login: https://redgeodesica-sbc.igac.gov.co/sbc
- SBC registration: https://redgeodesica-sbc.igac.gov.co/sbc/Account/Register
- Resolución IGAC 1771 de 2024: https://www.igac.gov.co/transparencia-y-acceso-a-la-informacion-publica/normograma/resolucion-1771-de-2024
- Resolución IGAC 715 de 2018 (MAGNA-SIRGAS 2018 adoption): https://redgeodesica.igac.gov.co/documentos/resolucion_igac_715-2018.pdf
- SIRGAS Colombia RT presentation (Apr 2024): https://sirgas.ipgh.org/wp-content/uploads/2024/05/IGAC-Colombia-RT.pdf
- Revista Geodata edición 5: https://revistageodata.icde.gov.co/edicion-5/red-geodesica-nacional-activa-magna-eco-densificacion-y-cobertura-de-estaciones-cors-en
- IGAC MAGNA-ECO procedure manual (PDF): https://www.igac.gov.co/sites/default/files/listadomaestro/p30100-05-18.v4_red_estaciones_contin_marco_geocentrico_nal_magna_eco_0.pdf
- Servicio Geológico Colombiano GeoRED: https://geored2.sgc.gov.co/
- ArduSimple Colombia page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-colombia/
- Direct sourcetable fetches (2026-05-22): `http://sbc.igac.gov.co:2101/` (Content-Length 3055, 28 STR), `http://sbc.igac.gov.co:2102/` (Content-Length 15869, 144 STR)

## Known data gaps

- **Foreign-resident registration outcome** — SBC accepts non-Colombian ID types in form but no public confirmation IGAC approves foreign-passport-only subscriptions
- **GeoRED real-time** — SGC has not announced an NTRIP caster
- **Operator-cited datum/epoch for NTRIP broadcast** — IGAC declares MAGNA-SIRGAS 2018 as the national datum, but the in-broadcast frame for the SBC NTRIP service is not separately declared on a freely-fetched operator page
