# Cuba [CU] — NTRIP RTK Research
**Date researched:** 2026-05-21 (prior: 2026-05-17)

## Status

PROJECT EXISTS, NO PUBLIC ENDPOINT. GEOCUBA (Grupo Empresarial GEOCUBA — Empresa de Geoinformática y Cartografía, under MINFAR) operates a national NTRIP GNSS service on 13 permanent CORS installed 2014-2019, using BKG NtripCaster (open-source), hosted at the Centro de Información Geoespacial. Caster host:port, registration, and tariff are not published on any public URL. Service is institutionally gated; not hobbyist-accessible. No public 2025 update has changed this picture.

| Field | Value |
|---|---|
| landing_url | http://www.geocuba.cu/ (HTTP 301 redirect to https://www.geocuba.cu/ which returns HTTP 404 with curl 2026-05-21; HTTPS also has an expired TLS certificate. No NTRIP product page surfaces. Sub-paths `/geodesia`, `/servicios`, `/ntrip` not separately probed; primary site state appears broken.) |
| access_url | n/a — no public registration page |
| operator | GEOCUBA (Grupo Empresarial GEOCUBA — Empresa de Geoinformática y Cartografía), under MINFAR; Centro de Información Geoespacial |
| network | "Servicio NTRIP GNSS Nacional" (no official short brand) |
| host:port | not published |
| num_stations | 13 permanent CORS installed 2014-2019 (Capote Lemes et al. 2024, ResearchGate 379300548) |
| vrs | unknown — literature describes single-station broadcasting; VRS not documented |
| software | BKG NtripCaster (open-source) — Capote Lemes et al. 2024 |
| tariff | not published; state-sector / institutional access implied |
| hobbyist_eligibility | no — no public self-service registration |
| legal_residency_required | yes (implied; institutional accounts only) |
| last_confirmed_alive | 2026-05-21 — GEOCUBA homepage curl resolves but returns HTTP 404 on the apex (transient or content reorganisation); no public NTRIP endpoint advertised. SIRGAS-CON still lists `SCUB00CUB0` Santiago in IGS-IP. |
| most recent announcement | Capote Lemes et al., "Servicio NTRIP GNSS en Cuba. Perspectivas y Retos", Informática Habana 2024 / Revista Cubana de Geomática 2024 (ResearchGate 379300548). ResearchGate carries the title, authors, conference (Informática Habana 2024), and a Spanish-language abstract; full-text PDF is not openly hosted on ResearchGate from outside Cuba. Abstract summary: 13 GNSS CORS installed 2014-2019, BKG NtripCaster software, Centro de Información Geoespacial GEOCUBA, applications in terrestrial/maritime/aerial real-time precise positioning for prioritised sectors; future expansion ambition toward nearest Caribbean countries. The "BKG NtripCaster" software name and 13-CORS count are both surfaced in the publicly visible ResearchGate abstract/keywords; deeper service-tier details (host:port, datum/epoch declaration, public-access roadmap) require full-text access not currently available from outside Cuba. |
| datum_epoch | omitted — no operator declaration on public GEOCUBA pages. (Cuba participates in SIRGAS-CON via `SCUB`, but that is the IGS station's frame, not a GEOCUBA service declaration.) |

## Context

- **GEOCUBA** — formed 1995, merging Instituto Cubano de Hidrografía + Instituto Cubano de Geodesia y Cartografía. Under MINFAR.
- **Service installed 2014-2019; in regular operational use by 2024.** Capote Lemes et al. 2024 paper documents the 13-CORS network running on BKG NtripCaster at Centro de Información Geoespacial. The abstract does not give an explicit "service launch" date; whether the caster was continuously operational across 2019-2024 versus going live closer to the paper's writing cannot be determined from the publicly visible material. Use cases per the paper: terrestrial, maritime, aerial positioning in priority sectors.
- **No public registration / sourcetable / pricing / eligibility** on geocuba.cu, minfar.gob.cu, or Revista Cubana de Geomática site as of 2026-05-21. Restricted to government / state-sector — institutionally gated; no public access path. Additional barrier: external connectivity to Cuban government infrastructure is filtered.
- **SIRGAS-CON** — Cuba participates; CU stations daily RINEX academic only, not real-time NTRIP. IGS-IP archive carries `SCUB00CUB0` (Santiago) per `data/igs_ip.sourcetable`.
- **Volunteer** — zero CU rtk2go + Centipede STR (2026-05 project archives; `py scripts/stations_by_country.py CUB` returns no stations).
- **Practical workaround** — self-operated base + standalone rover, or Galileo HAS (free SSR, <20 cm horizontal / <40 cm vertical per ESA/Navipedia spec — https://gssc.esa.int/navipedia/index.php/Galileo_High_Accuracy_Service_(HAS) — no internet required).

## Post-processing

| Service | URL | Cost |
|---|---|---|
| SIRGAS station archive (limited CU CORS) | https://sirgas.ipgh.org/ | free |
| IGS-IP `SCUB00CUB0` archive flag | via BKG IGS-IP caster | BKG registration |

## Sources

- GEOCUBA: http://www.geocuba.cu/ (no NTRIP product page; redirects to apex with intermittent 404 2026-05-21)
- MINFAR / GEOCUBA listing: https://www.minfar.gob.cu/sistema-empresarial/grupo-empresarial-geocuba
- Revista Cubana de Geomática (CIG): https://geomatica.geocuba.cu/rcg (intermittent reachability from outside Cuba; ECONNREFUSED 2026-05-21)
- Informática Habana 2024 conference activity index: https://www.informaticahabana.cu/actividad/servicio-ntrip-gnss-en-cuba-perspectivas-y-retos/ (HTTP 404 from sandbox; the talk is cited from the conference index and the paper)
- SIRGAS station list: https://sirgas.ipgh.org/en/gnss-network/stations/station-list/
- Capote Lemes et al. "Servicio NTRIP GNSS en Cuba. Perspectivas y Retos" (Informática Habana 2024 / Revista Cubana de Geomática): https://www.researchgate.net/publication/379300548 — operator evidence for 13-CORS GEOCUBA deployment + BKG NtripCaster software

## Gaps

- Caster host:port — likely `*.geocuba.cu` or static IP; not advertised.
- Public-availability roadmap — 2024 paper mentions future Caribbean expansion but no public-access commitment.
- Tariff — not published; inter-agency cooperation implied.
- Datum/epoch — operator does not declare on any public page.
