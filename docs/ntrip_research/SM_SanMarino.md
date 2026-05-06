# San Marino [SM] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: NO domestic caster — Italian commercial networks (HxGN SmartNet / NetGEO / SPIN3) physically cover the territory

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No domestic caster |
| **Italian network coverage of SM territory** | Yes — Italian private NTRIP networks reach SM (enclosed microstate, ~61 km²); no SM-specific caster or portal |
| **hobbyist_eligibility** | Depends on Italian network chosen (see below) |
| **legal_residency_required** | Varies by network; HxGN SmartNet and NetGEO accept EU subscribers |
| **last_confirmed_alive** | N/A (no domestic caster); Italian casters confirmed alive 2026-05-06 |

## Italian Networks Covering San Marino

San Marino is a 61 km² microstate entirely enclosed by the Italian region of Emilia-Romagna. Any Italian national NTRIP network with coverage in Emilia-Romagna will physically cover SM territory. The nearest Italian RTK reference stations are in Rimini, Pesaro, Forlì, and Cesena (all within 40–60 km of SM centre).

### HxGN SmartNet Italy (ItalPOS / it.nrtk.eu)
- **host:port:** `it.nrtk.eu:2101` (IP: 69.64.185.120:2101)
- **Operator:** Hexagon / Leica Geosystems Italy
- **Coverage:** Claims to cover "tutto il territorio italiano" (all Italian territory) with 130+ stations; SM physically within Italian network extent
- **Tariff:** Not publicly listed; contact hxgnsmartnet.com/it-it for quote — typically subscription-based, commercially priced
- **VRS:** Yes
- **hobbyist_eligibility:** Unclear — professional service orientation; no explicit hobbyist block
- **Portal:** https://hxgnsmartnet.com/it-it

### NetGEO / TopNET Live (rtk.topnetlive.com)
- **host:port:** `rtk.topnetlive.com:2101` (IP: 88.86.116.1:2101)
- **Operator:** Topcon Positioning Italy
- **Coverage:** "I servizi Topnet Live sono utilizzabili nel territorio italiano" — Italian territory; 200+ stations; SM physically within range
- **Tariff:** Not publicly listed on portal; available via shop.netgeo.it after registration
- **VRS:** Yes (VRS, FKP, iMAX)
- **hobbyist_eligibility:** Unclear
- **Confirmed alive:** `88.86.116.1:2101` returned SOURCETABLE 200 OK on 2026-05-06 (curl probe)
- **Contact:** tpi-assistenza-reti@topcon.com / +39 071.21.325.288

### SPIN3 GNSS (Northern Italy only — does NOT cover SM)
- **host:port:** `158.102.7.10:2101`
- **Coverage:** Piemonte, Lombardia, Valle d'Aosta only — approximately 700 km northwest of SM; does NOT cover SM
- **Confirmed alive:** SOURCETABLE 200 OK on 2026-05-06

### GeoDAF (INGV passive data — not real-time NTRIP)
- No real-time NTRIP service; RINEX archive only for post-processing.

## Context Notes

- San Marino has no domestic geodetic agency operating a CORS/NTRIP infrastructure. The Ufficio del Catasto (Cadastral Office) handles land registration but has no known real-time GNSS service.
- ArduSimple's San Marino page confirms "San Marino is not among them" (countries with a national RTK network) as of 2026.
- The EUREF Permanent Network (EPN) does not list a permanent station on SM territory as of 2026.
- For practical use: HxGN SmartNet (it.nrtk.eu:2101) or NetGEO (rtk.topnetlive.com:2101) are the most accessible options; both require a paid Italian subscription but physically cover San Marino. Contact directly for exact pricing and registration.
- No free national NTRIP exists covering SM territory. EUREF streams (BKG) contain nearby Italian stations but baseline distances are 200–400 km — too long for RTK.
- No rtk2go or Centipede volunteer bases found specifically for San Marino (SM-coded).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GeoDAF (INGV/ASI)** — nearest Italian CORS RINEX | https://geodaf.mt.asi.it/ | Free with registration |
| **EPN / EUREF** — nearest EPN stations (Padova ~200 km) | https://www.epncb.oma.be/ | Free |

## Sources Consulted
- ArduSimple San Marino page: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-san-marino/ (observed 2026-05-06)
- HxGN SmartNet Italy: https://hxgnsmartnet.com/it-it (403 on direct fetch)
- NetGEO / Topcon Positioning Italy: https://shop.netgeo.it/la-rete-ed-i-servizi/ (observed 2026-05-06)
- SPIN3 GNSS coverage: https://www.spingnss.it/i-servizi/ (Piemonte/Lombardia/VdA only — not SM)
- Italian GNSS network overview: https://topografo.it/rtk-gps-gnss (observed 2026-05-06)
- curl probe of `88.86.116.1:2101` (NetGEO) — SOURCETABLE 200 OK 2026-05-06
- curl probe of `158.102.7.10:2101` (SPIN3) — SOURCETABLE 200 OK 2026-05-06
