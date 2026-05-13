# Hungary [HU] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07 (updated 2026-05-12: re-verified `ntrip.gnssnet.hu:2101` returns same 10 SGO_* streams; Centipede-RTK HU node count is 216 in current data/stations.json fetch, slight drop from 224)

## Status: YES — national NTRIP caster operating (GNSSnet.hu, paid). Centipede-RTK volunteer network gives effective free national coverage (~216 nodes — single largest non-French Centipede cluster).

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network 1 — name** | GNSSnet.hu |
| **Operator — GNSSnet.hu** | Lechner Nonprofit Kft. (Lechner Tudásközpont / Lechner Knowledge Centre); GNSS Service Center hosted at Penc Cosmic Geodetic Observatory (KGO) |
| **Mandate basis — GNSSnet.hu** | Lechner Nonprofit Kft. is the central state-controlled mapping/geoinformatics organisation; legacy continuation of FÖMI's GNSS service |
| **host:port — primary (Budapest)** | `ntrip1.gnssnet.hu:2101` |
| **host:port — secondary (Penc)** | `ntrip2.gnssnet.hu:2101` |
| **host:port — alias** | `ntrip.gnssnet.hu:2101` (resolves to caster IP `37.220.132.38:2101`; `SOURCETABLE 200 OK` returned by `GNSMART_Caster 2.0/1.0`, confirmed 2026-05-07) |
| **VRS — GNSSnet.hu** | Yes — network solution streams (PRS = iMAX/VRS, FKP, MAC) plus single-base RTK and DGNSS |
| **Mountpoint catalogue** | 10 streams: `SGO_RTK3.1`, `SGO_RTK3.2`, `SGO_RTK3.2_VV` (single-base RTK); `SGO_FKP3.1`, `SGO_FKP3.2`, `SGO_MAC3.1` (network FKP/MAC); `SGO_PRS3.1`, `SGO_PRS3.2`, `SGO_PRS3.2_VV` (network PRS — VRS/iMAX); `SGO_DGNSS3.0` (DGNSS). RTCM 3.2 streams emit MSM 1075/1085/1095/1125 → GPS+GLO+GAL+BDS |
| **tariff — registration** | 12,000 HUF + ÁFA, one-time per company, regardless of services subscribed |
| **tariff — per-minute (default if no flat-rate active)** | RTK 8 HUF/min; Network RTK 12 HUF/min; DGNSS 3 HUF/min — RTK ≈ 480 HUF/hr (~€1.20/hr); Network RTK ≈ 720 HUF/hr (~€1.80/hr) |
| **tariff — 30-day flat, within 50 km of one fixed coordinate** | RTK or Network RTK 15,000 HUF; DGNSS 6,000 HUF (outside the 50 km radius the same session falls back to per-minute billing without separate notice) |
| **tariff — 30-day flat (consume within 365 days)** | RTK / Network RTK 36,000 HUF; DGNSS 12,000 HUF |
| **tariff — 90-day flat (consume within 365 days)** | RTK / Network RTK 72,000 HUF; DGNSS 24,000 HUF |
| **tariff — 150-day flat (consume within 365 days)** | RTK / Network RTK 108,000 HUF; DGNSS 36,000 HUF |
| **tariff — 365-day continuous** | RTK / Network RTK 150,000 HUF (~€375 / ~$415); DGNSS 54,000 HUF |
| **multi-subscription discount** | −10 % on the 2nd simultaneous flat subscription of same type/duration; −20 % on the 3rd onwards (applied only to second-and-further line items) |
| **VAT status** | Net of ÁFA (Hungarian VAT, 27 %). Pricing PDF footnote 1 reads *"A feltüntetett árak az ÁFA-t nem tartalmazzák"*. VAT applies to private (non-business) buyers; intra-EU B2B reverse-charge or non-EU export rules may apply per Hungarian VAT law |
| **Schedule effective date** | Current schedule reflects price *reduction* effective 2023-02-01 (per Lechner news article); PDF served 2026-05-07 matches the 2023 schedule |
| **hobbyist_eligibility — GNSSnet.hu** | Unclear — leans no for the annual flat (~€375 + 27 % ÁFA → ~€476 / ~$540, over the $200/yr cutoff). The 30-day 50-km local pass (~€38 net + ÁFA = ~€48 / ~$54) is feasible for a single project. The 365-day per-minute fallback (~€1.20/hr RTK) suits ad-hoc users up to ~150 hours/year. Pricing PDF footnote 3 phrases the registration fee as paid *"by a company"* (`egy cég`), suggesting the contract template assumes a business counterparty; no separate natural-person tier is documented in the public FAQ |
| **legal_residency_required — GNSSnet.hu** | Unclear — no explicit residency clause; English registration form not published; invoicing in HUF assumes a Hungarian-tax-number-bearing counterparty. Foreign EU users probably accommodated under reverse-charge VAT but procedure not documented online |
| **last_confirmed_alive — GNSSnet.hu** | 2026-05-12 — `ntrip.gnssnet.hu:2101` re-verified, `SOURCETABLE 200 OK Server: NTRIP GNSMART_Caster 2.0/1.0`, identical 10 SGO_* mount catalogue (Content-Length 2131); pricing schedule unchanged from 2023-02-01 Feb-2023 reduction |
| **Network 2 — name** | Centipede-RTK |
| **Operator — Centipede-RTK** | Open community project (INRAE-originated, France); Hungarian nodes operated by individual volunteers and farmers |
| **host:port — Centipede-RTK** | `caster.centipede.fr:2101` |
| **VRS — Centipede-RTK** | No — individual base-station streams; nearest-base selection |
| **tariff — Centipede-RTK** | Free, open access |
| **hobbyist_eligibility — Centipede-RTK** | Yes |
| **legal_residency_required — Centipede-RTK** | No |
| **last_confirmed_alive — Centipede-RTK** | 2026-05-12 (216 HU nodes in `data/stations.json` 2026-05-12 fetch via `stations_by_country.py HUN` — single largest non-France country in the Centipede sourcetable; minor net churn from peak 224 in 2026-05-06 fetch) |

## Mountpoint Catalogue — GNSSnet.hu (sourcetable 2026-05-07)

| Mount | Format | Type | Constellations |
|---|---|---|---|
| `SGO_DGNSS3.0` | RTCM 3.0 | single-base DGNSS | GNSS |
| `SGO_FKP3.1` | RTCM 3.1 | network FKP | GPS+GLO |
| `SGO_FKP3.2` | RTCM 3.2 MSM | network FKP | GPS+GLO+GAL+BDS |
| `SGO_MAC3.1` | RTCM 3.1 | network MAC | GPS+GLO |
| `SGO_PRS3.1` | RTCM 3.1 | network PRS (iMAX/VRS) | GPS+GLO |
| `SGO_PRS3.2` | RTCM 3.2 MSM | network PRS (iMAX/VRS) | GPS+GLO+GAL+BDS |
| `SGO_PRS3.2_VV` | RTCM 3.2 MSM | network PRS (variant) | GPS+GLO+GAL+BDS |
| `SGO_RTK3.1` | RTCM 3.1 | single-base RTK | GPS+GLO |
| `SGO_RTK3.2` | RTCM 3.2 MSM | single-base RTK | GPS+GLO+GAL+BDS |
| `SGO_RTK3.2_VV` | RTCM 3.2 MSM | single-base RTK (variant) | GPS+GLO+GAL+BDS |

All streams are single-coordinate VRS-style entries from the caster's central point (47.79 N, 19.28 E — Penc); per-station coordinates are not exposed in the sourcetable. The underlying physical network has ~35 domestic stations historically.

## Volunteer Free Coverage

- **Centipede-RTK**: 216 HU nodes in `data/stations.json` 2026-05-12 fetch (down from peak 224 a week earlier — minor churn). Densest in the Great Hungarian Plain (Alföld) and northern Hungary (Borsod-Abaúj-Zemplén, Heves). Free, no auth on raw streams. Hungary has the densest non-French Centipede footprint, with ~130 nodes documented by INRAE in the 2024 expansion narrative growing to ~220 by 2026-05.
- **rtk2go**: 5 HU bases in current snapshot (`BALO`, `FMPT`, `SanyiGazda`, `Szarka`, `SzentkiralySZLA`) — small-shop hobbyist deployments under the rtk2go "Free Open NTRIP Streams" model.
- Combined ~221 HU bases give effective national free RTK coverage for hobbyists in most populated regions, without sign-up. No formal nationwide free government tier exists.

## Context Notes

- **Pricing reduction (2023-02-01)**: A site notice on lechnerkozpont.hu confirms the current schedule reflects a price *reduction* effective 2023-02-01. The PDF currently served (`gnss_valosideju_szolg_arak.pdf`) is the post-reduction schedule. Pre-2023 annual cost was higher.
- **Per-minute fallback**: Per-minute billing is the *automatic* default whenever a user does not have an active flat-rate subscription (footnote 4: *"Érvényes átalánydíjas előfizetés híján automatikusan percalapú a valós idejű adatszolgáltatás"*). For occasional hobbyist use up to ~150 hours/year, the per-minute RTK rate (~€1.20/hr) keeps total spend under the $200/yr threshold.
- **50 km local-radius product**: A targeted single-project tariff. 30 days unlimited within 50 km of one user-supplied coordinate for 15,000 HUF (RTK/Network RTK) or 6,000 HUF (DGNSS) net; outside the radius, the session is silently re-priced as per-minute. Aimed at survey-style projects bounded to one site.
- **Caster software**: Geo++ GNSMART (sourcetable banner `NTRIP GNSMART_Caster 2.0/1.0`); Lechner has been operating GNSMART since the FÖMI era.
- **English-language portal**: Limited. The lechnerkozpont.hu English page (`/en/oldal/services`) describes services in English but the registration flow, contract templates, and pricing PDF are Hungarian-only. Contact: `support@gnssnet.hu`, +36 27 200-930 / -931 (8:00–16:00 CET, working days). Contact for foreign-user enquiries is the only documented path.
- **Map / app**: Lechner publishes the EHT 2.0 platform (`eht2.gnssnet.hu`) for post-processing services; separate from the realtime caster.
- **No SAPOS-like state-funded free tier exists** — Hungary deliberately operates GNSSnet on cost-recovery, distinguishing it from neighbouring Slovakia (paid SKPOS), Slovenia (paid SIGNAL), Austria (paid APOS) — and from Poland (free ASG-EUPOS) and Croatia (paid CROPOS). Aligns with Central-European cost-recovery norms.
- **FarmRTK.hu** (`farmrtk.hu`): Lechner-affiliated agricultural RTK service targeting precision agriculture with optimised mountpoints; pricing distinct from GNSSnet.hu and not detailed in this brief.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GNSSnet.hu post-processing (EHT 2.0)** | https://eht2.gnssnet.hu | Paid (separate tariff in Appendix A of ÁSZF, not detailed in the realtime PDF) |
| **Centipede archive (RINEX)** | https://centipede.fr | Free; archive availability per-station; 224 HU stations |
| **EUREF / EPN** | https://www.epncb.oma.be | Free; Hungarian EPN stations (PENC, BUTE, BUDP) provide RINEX through EUREF data centres |

## Sources Consulted

- GNSSnet.hu service homepage: https://www.gnssnet.hu (observed 2026-05-07; HU-only)
- GNSSnet.hu realtime services page: https://www.gnssnet.hu/index.php?r=site/realtime (observed 2026-05-07; lists `ntrip1.gnssnet.hu:2101` and `ntrip2.gnssnet.hu:2101`)
- GNSSnet.hu realtime tariff PDF: https://www.gnssnet.hu/pdf/gnss_valosideju_szolg_arak.pdf (full pdftotext extraction 2026-05-07; current schedule, post-2023 reduction)
- GNSSnet.hu service description PDF: https://www.gnssnet.hu/pdf/gnssnet.hu_szolgaltatas_leiras.pdf
- GNSSnet.hu FAQ (GYIK): https://www.gnssnet.hu/index.php?r=site/gyik (mentions monthly per-minute billing summaries)
- Lechner Tudásközpont GNSS service overview (HU): https://lechnerkozpont.hu/oldal/gnss
- Lechner Tudásközpont services (EN): https://lechnerkozpont.hu/en/oldal/services
- Lechner price-reduction announcement (HU, 2023-02-01): https://lechnerkozpont.hu/cikk/arcsokkenes-a-gnssnet-hu-atalanydijas-szolgaltatasaiban
- Live caster sourcetable: `curl http://ntrip.gnssnet.hu:2101/` → `SOURCETABLE 200 OK Server: NTRIP GNSMART_Caster 2.0/1.0` (10 STR rows, 2026-05-07; caster IP `37.220.132.38:2101`)
- HTE InfoKommunikáció Fogalomtár — GNSSnet.hu: https://www.fogalomtar.hte.hu/en/wiki/-/wiki/HTE+Infokommunikacios+Fogalomtar/GNSSnet.hu
- GIS Open 2025 conference paper on GNSSnet.hu (HU): https://www.gisopen.hu/data/pdf/2025/f2.pdf
- Centipede-RTK home: https://www.centipede-rtk.org/
- Centipede-RTK Hungary article (INRAE 2024): https://www.inrae.fr/en/news/democratising-precision-guided-agriculture-ever-expanding-centipede-rtk-network
- Centipede HU node count: `data/stations.json` 2026-05-06 fetch (224 HUN entries in `centipede` source)
- rtk2go HU node count: `data/stations.json` 2026-05-06 fetch (6 HUN entries in `rtk2go` source)
- ArduSimple Hungary: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-hungary/
