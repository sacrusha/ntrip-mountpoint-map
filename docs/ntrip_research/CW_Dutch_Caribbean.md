# Dutch Caribbean [CW / AW / BQ / SX] — NTRIP RTK Research

**researched:** 2026-05-17 (prior: 2026-05-12)

**scope note:** file covers 4 ISO codes — CW (Curaçao), AW (Aruba), BQ (Bonaire/St Eustatius/Saba), SX (Sint Maarten) — under single CW filename for now. Each territory has separate ISO-2 + separate operator landscape; treat per-island sections as independent country entries when consuming downstream (markers, fetch). Filename rename = pipeline change deferred; per-territory coverage status in Summary table below.

## Summary

| Territory | ISO2 | National caster? | Free RTK? | Status |
|---|---|---|---|---|
| Curaçao | CW | no | yes (volunteer) | 3 rtk2go JAJO bases + 1 EarthScope CN40, all Willemstad-cluster |
| Aruba | AW | no | — | none |
| Bonaire / St Eustatius / Saba | BQ | yes | yes (free) | AGRS.BES via Kadaster NL / NSGI |
| Sint Maarten | SX | no | — | none |

---

## [BQ] BES — AGRS.BES (Kadaster NL / NSGI)

| field | value |
|---|---|
| landing_url | https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams |
| access_url | https://ntrip.kadaster.nl/streamtable |
| operator | NSGI / Kadaster Netherlands on behalf of Kadaster BES |
| host:port | `ntrip.kadaster.nl:2101` (plain) · `ntrip.cloud.kadaster.nl:443` (TLS) |
| vrs | no — raw single-station |
| num_stations | 3 physical (Bonaire, Saba, Sint Eustatius); 5 MSM mountpoints + 2 legacy + 1 RAW |
| tariff | free — "gratis real-time data" per NSGI page; no registration, no auth required (optional email username for outage notices). NETPOS (NL mainland subset) is paid (€475/yr stations 1–5) — separate service. |
| hobbyist_eligibility | yes — fully anonymous |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-17 — `ntrip.kadaster.nl:2101` sourcetable returned 5 BES STR; NSGI page 200 |
| datum_epoch | omitted — no operator declaration on NSGI streams page citable per primer rule |

### BES mountpoints (`ntrip.kadaster.nl:2101`, RTCM 3.3 MSM, country `BES`)

| MP | Station | Island | lat | lon | systems | Format |
|---|---|---|---|---|---|---|
| BON200BES0 | Bonaire (Stonex SC2200) | Bonaire | 12.15 | -68.27 | GPS+GLO+GAL+BDS | RTCM 3.3 |
| BONK00BES0 | Bonaire (Leica GR30) | Bonaire | 12.15 | -68.27 | GPS+GLO+GAL+BDS | RTCM 3.3 |
| SABY0 | Saba | Saba | 17.65 | -63.22 | GPS+GLO | RTCM 3.1 legacy |
| SABY00BES0 | Saba (Septentrio PolaRx5E) | Saba | 17.65 | -63.22 | GPS+GLO+GAL+BDS | RTCM 3.3 |
| SABY00BES1 | Saba | Saba | 17.65 | -63.22 | GPS+GLO+GAL+BDS | SBF RAW |
| SEUS0 | Sint Eustatius | St Eustatius | 17.50 | -62.98 | GPS+GLO | RTCM 3.1 legacy |
| SEUS00BES0 | Sint Eustatius (Septentrio PolaRx5) | St Eustatius | 17.50 | -62.98 | GPS+GLO+GAL+BDS | RTCM 3.3 |

---

## [CW] Curaçao — no national caster; JAJO rtk2go cluster + EarthScope CN40

Kadaster Curaçao (`kadaster.cw`) runs a parcel map viewer only; no NTRIP. NSGI explicitly excludes Curaçao from its mandate. Practical RTK = volunteer streams clustered in Willemstad.

| field | value |
|---|---|
| landing_url (national) | https://kadaster.cw/ (no GNSS section) |
| host:port (rtk2go) | `rtk2go.com:2101` — anonymous, arbitrary user, email-as-username convention |
| host:port (EarthScope) | `gnss.earthscope.org:2101` — free NULA + GNSS data agreement |
| vrs | no — physical single-base |
| tariff | free (rtk2go volunteer pool; EarthScope NULA non-commercial) |
| hobbyist_eligibility | yes (rtk2go anonymous; EarthScope NULA = personal yes, paid-work no) |
| legal_residency_required | no |
| last_confirmed_alive | 2026-05-17 — JAJO + CN40 streams present in project rtk2go + EarthScope archives |
| datum_epoch | omitted — no operator declaration |

### CW streams (project archive)

| MP | source | lat | lon | location | format |
|---|---|---|---|---|---|
| CWM_JAJO_RTK_RTCM3_X | rtk2go | 12.12 | -68.91 | Willemstad | RTCM 3.3 |
| MPA_JAJO_RTK_RTCM3_X | rtk2go | 12.17 | -68.98 | Gato/Willemstad | RTCM 3.2 |
| UTE_JAJO_RTK_RTCM3_X | rtk2go | 12.15 | -68.91 | Willemstad | RTCM 3.2 |
| CN40_RTCM3P3 | EarthScope NOTA | 12.18 | -68.96 | Willemstad | RTCM 3.3 |

JAJO mounts = Mijnmaatschappij Curaçao (JAJO group's limestone quarry op, `miningcompanycuracao.com`). All 4 streams cluster within ~8 km, south coast. Westpunt + Oostpunt baselines stretch >30 km — marginal single-base.

---

## [AW] Aruba — DLV
No public NTRIP. Dienst Landmeetkunde en Vastgoedregistratie (Sabana Blanco 68, Oranjestad; +297 528-8359) does not publish a caster. `dlv.aw` no live result. Aruba outside NSGI mandate.

## [SX] Sint Maarten — Kadaster Sint Maarten / VROMI
No public NTRIP. Early-2026 MOU between VROMI / Kadaster Sint Maarten + Kadaster NL is institutional only, not a service. Outside NSGI mandate.

---

## Sources
- NSGI real-time streams: https://www.nsgi.nl/referentiepunten-en-gnss-data/gnss-data/real-time-streams (confirms BES free, anonymous; NETPOS paid)
- Live streamtable: https://ntrip.kadaster.nl/streamtable
- Direct sourcetable fetch `http://ntrip.kadaster.nl:2101/` (2026-05-17): 5 BES MSM STR + 2 legacy + RAW
- Kadaster BES: https://bes.kadaster.nl/
- Kadaster BES 2026 tariff PDF: https://kadorbonaire.com/wp-content/uploads/2025/12/Tarieven-Kadaster-BES-2026.pdf (binary; no GNSS line confirmed via WebFetch)
- Kadaster Curaçao: https://kadaster.cw/
- Mining Company Curaçao (JAJO): https://miningcompanycuracao.com/ + https://www.jajo.com/en/companies/mining-company-curacao/
- `data/rtk2go.sourcetable` 2026-05 snapshot — 3 CUW JAJO STR
- `data/earthscope.sourcetable` 2026-05 snapshot — 1 CUW STR (CN40)
- NSGI FAQ on territory scope

## Gaps
- BES tariff PDF (Tarieven-Kadaster-BES-2026.pdf) returns binary that WebFetch cannot text-extract here. NSGI page confirms "gratis" for AGRS.BES streams.
- Datum/epoch for AGRS.BES not declared on NSGI streams page.
- Aruba + Sint Maarten future plans unknown.
