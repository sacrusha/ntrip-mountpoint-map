# Cuba [CU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12 (initial 2026-05-06)

## Status: PROJECT EXISTS, NO PUBLIC ENDPOINT — GEOCUBA has built a national NTRIP GNSS service on 13 permanent stations (2014–2019) using BKG NtripCaster open-source software; the service is hosted at GEOCUBA's Centro de Información Geoespacial but **caster host, port, registration URL, and tariff are not published on any public web page** as of 2026-05-12. No hobbyist-accessible endpoint identified.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Project active; endpoint not publicly indexed |
| **Operator** | GEOCUBA (Grupo Empresarial GEOCUBA — Empresa de Geoinformática y Cartografía) under MINFAR; Centro de Información Geoespacial |
| **Network name** | "Servicio NTRIP GNSS Nacional" (no official short brand documented) |
| **host:port** | Not published — no public endpoint found |
| **VRS** | Unknown (the literature describes single-station broadcasting; no VRS computed-stream documented) |
| **Stations** | 13 continuous/permanent GNSS stations installed 2014–2019 across Cuban provinces |
| **Software stack** | BKG NtripCaster (open-source, free German implementation) |
| **tariff** | Not published; institutional/governmental access implied; no public pricing |
| **hobbyist_eligibility** | No — self-service registration not available via any public URL |
| **legal_residency_required** | Yes (implied — institutional/sector accounts only) |
| **last_confirmed_alive** | GEOCUBA corporate site (geocuba.cu) and Revista Cubana de Geomática (geomatica.geocuba.cu) HTTP 200 confirmed 2026-05-12; no NTRIP endpoint reachable from the research environment |
| **Most recent project announcement** | "Servicio NTRIP GNSS en Cuba. Perspectivas y Retos" (Capote et al.), Informática Habana 2024 / Revista Cubana de Geomática 2024 — describes operational launch and 13-station network; identifies future expansion targets including coverage for nearer Caribbean countries |

## Context Notes

- **GEOCUBA** was established on May 1, 1995, merging the former Instituto Cubano de Hidrografía and the Instituto Cubano de Geodesia y Cartografía. It operates under the Ministerio de las Fuerzas Armadas Revolucionarias (MINFAR).
- **Service launched between 2019 and 2024**: A 2024 conference paper at Informática Habana 2024 (and republication in Revista Cubana de Geomática, 2024) describes the **operational deployment** of a national NTRIP GNSS service in Cuba based on the 13 continuous stations installed 2014–2019, running on BKG NtripCaster open-source software, hosted by GEOCUBA's Centro de Información Geoespacial. The paper highlights real-time use cases for terrestrial, maritime and aerial positioning in priority economic sectors. No public sourcetable URL is given in the abstract / open-access references; the full paper is paywalled / requires ResearchGate login.
- **No public registration portal**: As of 2026-05-12, no public-facing registration URL, sourcetable URL, pricing schedule, or eligibility document has been published on geocuba.cu, minfar.gob.cu, or the Revista Cubana de Geomática site for the NTRIP service. The service appears restricted to government / state-sector users.
- **US trade embargo** (OFAC regulations) restricts import of most GNSS survey equipment and software to Cuba, compounding the barrier to RTK adoption by hobbyists; payments from US-affiliated entities would face additional legal exposure even if the service were opened.
- **SIRGAS**: Cuba participates in SIRGAS-CON (Sistema de Referencia Geocéntrico para las Américas). A subset of Cuban stations appears in the SIRGAS station list; SIRGAS data is published as daily RINEX for academic post-processing only, not as public real-time NTRIP.
- **Volunteer networks**: Zero CU-coded stations in rtk2go and Centipede 2026-05 archives.
- **Hobbyist outlook**: Even if the GEOCUBA service became technically reachable, OFAC exposure, lack of payment-route to GEOCUBA from US-affiliated visitors, and the absence of public registration likely keep this off-limits for non-Cuban hobbyists for the foreseeable future. Practical workaround: a self-operated base station + standalone rover, or PPP (Galileo HAS).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **SIRGAS station archive** — limited Cuban CORS data | https://sirgas.ipgh.org/ | Free (research/academic) |

## Sources Consulted
- GEOCUBA corporate site: http://www.geocuba.cu/ (2026-05-12; HTTP 200; no NTRIP product page)
- MINFAR / GEOCUBA: https://www.minfar.gob.cu/sistema-empresarial/grupo-empresarial-geocuba
- Revista Cubana de Geomática (Centro de Información Geoespacial): https://geomatica.geocuba.cu/rcg (2026-05-12; HTTP 200)
- Capote Lemes et al., "Servicio NTRIP GNSS en Cuba. Perspectivas y Retos" (2024): https://www.researchgate.net/publication/379300548 (abstract only — full text requires ResearchGate account)
- Informática Habana 2024 conference activity: https://www.informaticahabana.cu/actividad/servicio-ntrip-gnss-en-cuba-perspectivas-y-retos/ (HTTP 404 at 2026-05-12; referenced via search index)
- SIRGAS station list (Cuba): https://sirgas.ipgh.org/en/gnss-network/stations/station-list/
- WebSearch ("Cuba GEOCUBA NTRIP gnss.geocuba.cu", "servicio NTRIP Cuba estaciones permanentes BKG") — no public host:port found

## Known Data Gaps
- **Caster host:port**: Unknown. Likely a `*.geocuba.cu` or static IP not publicly advertised. Direct contact with GEOCUBA's Centro de Información Geoespacial would be needed to confirm.
- **Public availability**: Unclear whether GEOCUBA intends to open the service to non-state users or to commercialize it; the 2024 paper hints at future expansion to Caribbean countries but does not commit to a public-access model.
- **Tariff**: Not published. State sectors likely receive corrections under inter-agency cooperation rather than commercial billing.
