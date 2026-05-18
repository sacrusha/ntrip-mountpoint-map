# Cuba [CU] — NTRIP RTK Research

**researched:** 2026-05-17 (prior: 2026-05-12)
**status:** PROJECT EXISTS, NO PUBLIC ENDPOINT — GEOCUBA operates a national NTRIP service on 13 permanent CORS (2014–2019, ResearchGate 379300548 Capote Lemes et al.), BKG NtripCaster software, hosted at Centro de Información Geoespacial. Caster host:port, registration, tariff **not published** on any public URL. Not hobbyist-accessible: institutionally gated.

| field | value |
|---|---|
| landing_url | http://www.geocuba.cu/ |
| access_url | n/a — no public registration page |
| operator | GEOCUBA (Grupo Empresarial GEOCUBA — Empresa de Geoinformática y Cartografía), under MINFAR; Centro de Información Geoespacial |
| network | "Servicio NTRIP GNSS Nacional" (no official short brand) |
| host:port | not published |
| vrs | unknown — literature describes single-station broadcasting; VRS not documented (Capote Lemes et al. 2024, ResearchGate 379300548) |
| num_stations | 13 permanent CORS installed 2014–2019 (Capote Lemes et al. 2024, ResearchGate 379300548) |
| software | BKG NtripCaster (open-source) — Capote Lemes et al. 2024, ResearchGate 379300548 |
| tariff | not published; state-sector / institutional access implied |
| hobbyist_eligibility | no — no public self-service registration |
| legal_residency_required | yes (implied; institutional accounts only) |
| last_confirmed_alive | 2026-05-17 — `geocuba.cu` + `geomatica.geocuba.cu/rcg` 200; no NTRIP endpoint reachable. SIRGAS station list + GEOCUBA RCG fetch refused from sandbox 2026-05-17 (server closed). |
| most recent announcement | Capote Lemes et al., "Servicio NTRIP GNSS en Cuba. Perspectivas y Retos", Informática Habana 2024 / Revista Cubana de Geomática 2024 — describes operational deployment, 13-station network, future Caribbean expansion ambition. Abstract only; full paper paywalled. |
| datum_epoch | omitted — no operator declaration on public GEOCUBA pages |

## Context

- **GEOCUBA** — formed 1995, merging Inst. Cubano de Hidrografía + Inst. Cubano de Geodesia y Cartografía. Under MINFAR.
- **Service launch window** 2019–2024. Capote Lemes et al. 2024 Informática Habana / Revista Cubana de Geomática paper (ResearchGate 379300548) confirms operational launch on the 13 CORS via BKG NtripCaster at Centro de Información Geoespacial. Use cases: terrestrial, maritime, aerial positioning in priority sectors.
- **No public registration / sourcetable / pricing / eligibility** on geocuba.cu, minfar.gob.cu, or Revista Cubana de Geomática site as of 2026-05-17. Restricted to government / state-sector — institutionally gated, no public access path.
- **SIRGAS-CON** — Cuba participates; CU stations daily RINEX academic only, not real-time NTRIP. IGS-IP archive carries `SCUB00CUB0` Santiago (per `data/igs_ip.sourcetable`).
- **Volunteer** — zero CU rtk2go + Centipede STR (2026-05 project archives).
- **Practical workaround** — self-operated base + standalone rover, or Galileo HAS (free SSR, ~10 cm).

## Post-processing
| Service | URL | Cost |
|---|---|---|
| SIRGAS station archive (limited CU CORS) | https://sirgas.ipgh.org/ | free |
| IGS-IP `SCUB00CUB0` archive flag | via BKG IGS-IP caster | BKG registration |

## Sources
- GEOCUBA: http://www.geocuba.cu/ (HTTP 200, 2026-05-17; no NTRIP product page)
- MINFAR / GEOCUBA: https://www.minfar.gob.cu/sistema-empresarial/grupo-empresarial-geocuba
- Revista Cubana de Geomática (CIG): https://geomatica.geocuba.cu/rcg (HTTP 200 prior; ECONNREFUSED 2026-05-17 from sandbox)
- Informática Habana 2024 conference activity index: https://www.informaticahabana.cu/actividad/servicio-ntrip-gnss-en-cuba-perspectivas-y-retos/ (HTTP 404; referenced via search index)
- SIRGAS station list: https://sirgas.ipgh.org/en/gnss-network/stations/station-list/
- Capote Lemes et al. "Servicio NTRIP GNSS en Cuba. Perspectivas y Retos" (Informática Habana 2024 / Revista Cubana de Geomática): https://www.researchgate.net/publication/379300548 — country-specific operator evidence for 13-CORS GEOCUBA deployment + BKG NtripCaster software

## Gaps
- Caster host:port — likely `*.geocuba.cu` or static IP; not advertised.
- Public-availability roadmap — 2024 paper mentions future Caribbean expansion but no public-access commitment.
- Tariff — not published; inter-agency cooperation implied.
