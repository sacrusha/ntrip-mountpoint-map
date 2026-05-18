# San Marino [SM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-probed; HxGN SmartNet IT `it.nrtk.eu:2101` ST now reachable -- 12+ STR mountpoints visible (AG_NET_*/AG_RTK_* CMR+/MSM/MSM4/MSM5/RTCM/RTCM3, IQProxy 1.2/1.0); NetGEO `rtk.topnetlive.com:2101` still SOURCETABLE 200 OK; no SM-domestic caster)

## Status: NO domestic caster — Italian commercial networks (HxGN SmartNet / NetGEO / SPIN3) physically cover the territory

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No domestic caster |
| **Italian network coverage of SM territory** | Yes — Italian private NTRIP networks reach SM (enclosed microstate, ~61 km²); no SM-specific caster or portal |
| **hobbyist_eligibility** | Depends on Italian network chosen (see below) |
| **legal_residency_required** | Varies by network; HxGN SmartNet and NetGEO accept EU subscribers |
| **last_confirmed_alive** | N/A (no domestic caster). Italian fallbacks re-probed 2026-05-17: NetGEO `rtk.topnetlive.com:2101` SOURCETABLE 200 OK (Server: GNSS Spider 7.11.0.96/1.0; 11 STR Leica Spider mountpoints visible -- NRT2-RDN, VRS3-RDN-MSM, IMAX3-RDN-MSM, MAX3-RDN, FKP2-RDN, etc.); HxGN SmartNet `it.nrtk.eu:2101` SOURCETABLE 200 OK (Server: NTRIP IQProxy 1.2/1.0; AG_NET_*/AG_RTK_* in CMR+/MSM/RTCM3 variants) |
| **datum_epoch** | omitted -- no citable declaration (no SM-domestic operator; Italian commercial NetGEO + HxGN do not publish datum/epoch on their public-facing pages; ETRF2000 is the de-facto Italian network frame but inferring it from EPSG / IGM publications is not citable per primer rule) |

## Italian Networks Covering San Marino

San Marino is a 61 km² microstate entirely enclosed by the Italian region of Emilia-Romagna. Any Italian national NTRIP network with coverage in Emilia-Romagna will physically cover SM territory. The nearest Italian RTK reference stations are in Rimini, Pesaro, Forlì, and Cesena (all within 40–60 km of SM centre).

### HxGN SmartNet Italy (ItalPOS / it.nrtk.eu)
- **host:port:** `it.nrtk.eu:2101` (IP: 69.64.185.120:2101)
- **Operator:** Hexagon / Leica Geosystems Italy
- **Coverage:** Claims to cover "tutto il territorio italiano" (all Italian territory); SM physically within Italian network extent
- **num_stations:** ~130 (Hexagon Italy network claim)
- **Tariff:** Not publicly listed; contact hxgnsmartnet.com/it-it for quote — typically subscription-based, commercially priced
- **VRS:** Yes
- **hobbyist_eligibility:** Unclear — professional service orientation; no explicit hobbyist block
- **Portal:** https://hxgnsmartnet.com/it-it

### NetGEO / TopNET Live (rtk.topnetlive.com)
- **host:port:** `rtk.topnetlive.com:2101` (IP: 88.86.116.1:2101)
- **Operator:** Topcon Positioning Italy
- **Coverage:** "I servizi Topnet Live sono utilizzabili nel territorio italiano" — Italian territory; SM physically within range
- **num_stations:** ~200 (Topcon Italy network claim)
- **Tariff:** Not publicly listed on portal; available via shop.netgeo.it after registration
- **VRS:** Yes (VRS, FKP, iMAX)
- **hobbyist_eligibility:** Unclear
- **Confirmed alive:** `rtk.topnetlive.com:2101` returned `SOURCETABLE 200 OK` on 2026-05-17 (Server: GNSS Spider 7.11.0.96/1.0; 11 STR mountpoints: NRT2-RDN, NRT3-RDN, IMAX2/3-RDN, MAX3-RDN, VRS3-RDN, FKP2-RDN, VRS2-RDN, NRT3-RDN-MSM, VRS3-RDN-MSM, IMAX3-RDN-MSM, all at 44.92°N 8.62°E -- Piemonte caster reference, but coverage extends nationwide per Topcon docs)
- **Contact:** tpi-assistenza-reti@topcon.com / +39 071.21.325.288

### SPIN3 GNSS — Piemonte/Lombardia/VdA, does not cover SM (~700 km away; out of coverage).

### GeoDAF (INGV passive data — not real-time NTRIP)
- No real-time NTRIP service; RINEX archive only for post-processing.

## Context Notes

- San Marino has no domestic geodetic agency operating a CORS/NTRIP infrastructure. The Ufficio del Catasto (Cadastral Office) handles land registration but has no known real-time GNSS service.
- ArduSimple's San Marino page confirms "San Marino is not among them" (countries with a national RTK network) as of 2026.
- The EUREF Permanent Network (EPN) does not list a permanent station on SM territory as of 2026.
- For practical use: HxGN SmartNet (it.nrtk.eu:2101) or NetGEO (rtk.topnetlive.com:2101) are the most accessible options; both require a paid Italian subscription but physically cover San Marino. Contact directly for exact pricing and registration.
- No free national NTRIP exists covering SM territory. EUREF streams (BKG) contain nearby Italian stations but baseline distances are 200–400 km — too long for RTK.
- No rtk2go or Centipede volunteer bases found specifically for San Marino (SM-coded).
- **Local data check (2026-05-13)**: `py scripts/stations_by_radius.py 43.94 12.45 100` returns **1 rtk2go ITA station within 100 km** — `Basertk-fogli` at 44.71°N, 12.17°E (88.5 km north, in northern Emilia-Romagna). Outside the ~30–40 km practical RTK range but the closest free volunteer base. No closer Centipede or EarthScope nodes.
- **ArduSimple San Marino page (re-checked 2026-05-13)** still describes SM as having no national network and recommends generic global free options (rtk2go, IGS, EarthScope, EUREF) or paid SSR services (PointPerfect, Skylark), without naming Italian commercial coverage of SM territory.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GeoDAF (INGV/ASI)** — nearest Italian CORS RINEX | https://geodaf.mt.asi.it/ | Free with registration |
| **EPN / EUREF** — nearest EPN stations (Padova ~200 km) | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- ArduSimple San Marino page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-san-marino/ (observed 2026-05-13)
- HxGN SmartNet Italy: https://hxgnsmartnet.com/it-it (403 on direct fetch)
- NetGEO / Topcon Positioning Italy: https://shop.netgeo.it/la-rete-ed-i-servizi/ (observed 2026-05-06)
- SPIN3 GNSS coverage: https://www.spingnss.it/i-servizi/ (Piemonte/Lombardia/VdA only — not SM)
- Italian GNSS network overview: https://topografo.it/rtk-gps-gnss (observed 2026-05-06)
- Ufficio Tecnico del Catasto e Cartografia, San Marino: https://www.gov.sm/pub1/GovSM/Dipartimenti/Dipartimento-Territorio-e-Ambiente/Ufficio-Tecnico-del-Catasto-e-Cartografia.html (cadastral office; no public NTRIP service)
- TCP probe of `rtk.topnetlive.com:2101` (NetGEO) — SOURCETABLE 200 OK 2026-05-17, 11 mountpoints, Server: GNSS Spider 7.11.0.96/1.0
- TCP probe of `it.nrtk.eu:2101` (HxGN SmartNet IT) — SOURCETABLE 200 OK 2026-05-17, Server: NTRIP IQProxy 1.2/1.0, AG_NET_*/AG_RTK_* family
