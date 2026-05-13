# Ecuador [EC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (revision; original 2026-05-01)

## Status: YES — free public NTRIP RTK caster operating (REGME-IP / IGM Ecuador), live-confirmed

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — free national service |
| **host:port** | `ntrip.igm.gob.ec:2101` — sourcetable retrieved live 2026-05-12 (5 239 bytes; 26 STR rows = 26 physical stations; SNIP simpleNTRIP_Caster [wPRO] R3.19.00 of:Dec 19 2025) |
| **tariff** | Free — stated as "totalmente libre y gratuito" (entirely free and open); EUR/USD 0.00 |
| **num_stations** | 26 physical CORS (live count 2026-05-12; e.g. Alausi ALEC, Ambato ABEC, Babahoyo BHEC, Chaco CHEC, Cotopaxi CXEC, Cuenca CUEC, El Carmen ECEC, Esmeraldas ESEC, ESPE EPEC, FranciscoOrellana FOEC, Guayaquil GQEC, LagoAgrio LAEC, Loja LJEC, Macas MAEC, Machala MHEC, Naranjal NJEC, Pajan JNEC, Pimampiro PIEC, Pinas INEC, Portoviejo POEC, Posorja DPEC, + others) |
| **vrs** | No (live sourcetable shows only single-station mountpoints, each formatted `<Town>-<CODE>-IGM`; no VRS/MAC/FKP rows. Earlier coverage describing REGME-IP as multi-station/VRS appears to have been incorrect — corrected on 2026-05-12 probe.) |
| **format** | RTCM 3 (typically 1004, 1006, 1008, 1012, 1013, 1019, 1020, 1033, 1230); multi-GNSS GPS+GLO+GAL+BDS+QZS+SBAS |
| **hobbyist_eligibility** | Yes — open online registration via geoportal, no surveying licence required |
| **legal_residency_required** | Unclear — registration form is online; no explicit residency restriction stated; service explicitly extends to "national and international" users |
| **registration** | https://www.geoportaligm.gob.ec/ntrip/public/register |
| **last_confirmed_alive** | **2026-05-12** (NTRIP sourcetable retrieved live with 26 STR rows; SNIP build of 2025-12-19 confirms recent maintenance) |

## Context Notes

- **REGME-IP** (Red GNSS Ecuatoriana de Posicionamiento en tiempo real protocol IP): operated by the Instituto Geográfico Militar (IGM) of Ecuador. Single unified national domain `ntrip.igm.gob.ec` introduced February 2024 per IGM Twitter/X announcements.
- The caster is single-station only (nearest-station model). Hobbyists must select the closest `<Town>-<CODE>-IGM` mountpoint manually; no VRS/CERCANA-style auto-routing mountpoint is published.
- The service is described as completely free and voluntary, with no subscription tiers or usage fees. Main server at IGM Quito with backup at ESPOCH Riobamba; service is 365 days/year with guaranteed availability Mon–Fri 07:30–16:30 (technical support window).
- Ecuador is one of the few Latin American countries operating a live, free public NTRIP RTK caster.

## Registration

- URL: https://www.geoportaligm.gob.ec/ntrip/public/register
- Process: Online self-registration (account required to receive credentials for the caster).
- No professional/surveying credential requirement documented.
- Support: regme.igm@geograficomilitar.gob.ec / procesogeodesia.igm@geograficomilitar.gob.ec / +593 02-3975100 ext 4421

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **IGM REGME RINEX archive** — daily RINEX for REGME stations | https://www.geoportaligm.gob.ec/ | Free (account required) |
| **EarthScope / SIRGAS-CON** — Ecuador SIRGAS stations | https://www.earthscope.org/data/gnss-data/ | Free noncommercial; USD 1 000/seat/yr commercial |

## Sources Consulted
- Live sourcetable probe of `ntrip.igm.gob.ec:2101` — 2026-05-12 (26 stations enumerated)
- IGM Ecuador NTRIP registration: https://www.geoportaligm.gob.ec/ntrip/public/register
- IGM Ecuador NTRIP monitor (GitHub Pages): https://geoportaligm-ec.github.io/NTRIP-monitor/
- IGM news — "Único dominio servicio NTRIP" (single-domain announcement): http://www.geograficomilitar.gob.ec/unico-dominio-servicio-ntrip/
- IGM news — "Integración de 4 estaciones al servicio REGME-IP, protocolo NTRIP": http://www.geograficomilitar.gob.ec/integracion-de-4-estaciones-al-servicio-regme-ip-protocolo-ntrip/
- Licencia y políticas de uso PDF: https://www.geoportaligm.gob.ec/ntrip/public/manual/licencia_gnss_ntrip.pdf
- SIRGAS 2022 bulletin citing `ntrip.igm` on port 2101: https://sirgas.ipgh.org/docs/Boletines/Bol14/10.cisneros.pdf
