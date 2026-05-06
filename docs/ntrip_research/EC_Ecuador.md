# Ecuador [EC] — NTRIP RTK Caster Research
**Date researched:** 2026-05-01

## Status: YES — free public NTRIP RTK caster operating (REGME-IP / IGM Ecuador)

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — free national service |
| **host:port** | `ntrip.igm.gob.ec:2101` |
| **tariff** | Free — stated as "totalmente libre y gratuito" (entirely free and open) |
| **VRS** | Yes (network RTK / VRS implied by REGME-IP multi-station network) |
| **hobbyist_eligibility** | Yes — open online registration, no surveying licence required |
| **legal_residency_required** | Unclear — registration form is online; no explicit residency restriction stated |
| **last_confirmed_alive** | 2026-05-01 (geoportal registration page reachable) |

## Context Notes

- **REGME-IP** (Red GNSS Militar Ecuatoriana de Posicionamiento en tiempo real): Operated by the Instituto Geográfico Militar (IGM) of Ecuador. This is Ecuador's national military geographic institute, equivalent to the mapping agencies of other Andean countries.
- The NTRIP caster at `ntrip.igm.gob.ec:2101` was confirmed active in a 2022 SIRGAS bulletin (sirgas.ipgh.org) which explicitly names this address and port.
- Registration is required via the IGM geoportal at `https://www.geoportaligm.gob.ec/ntrip/`. The public viewer is accessible at `https://www.geoportaligm.gob.ec/ntrip/public/visor`.
- The service is described as completely free — there are no subscription tiers or usage fees.
- Ecuador is one of the few Latin American countries operating a live, free public NTRIP RTK caster.

## Registration

- URL: https://www.geoportaligm.gob.ec/ntrip/
- Process: Online self-registration (account required to receive credentials for the caster).
- No professional/surveying credential requirement documented.

## Sources Consulted
- IGM Ecuador geoportal NTRIP registration: https://www.geoportaligm.gob.ec/ntrip/
- IGM Ecuador NTRIP public viewer: https://www.geoportaligm.gob.ec/ntrip/public/visor
- SIRGAS 2022 bulletin citing `ntrip.igm` on port 2101: https://sirgas.ipgh.org/docs/Boletines/Bol14/10.cisneros.pdf
