# Vietnam [VN] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — national government NTRIP caster operating (VNGEONET); paid subscription

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name** | VNGEONET |
| **Operator** | Ministry of Natural Resources and Environment (MONRE) / Department of Survey and Mapping |
| **host:port** | `vngeonet.vn:2101` (IP: 14.238.1.125; also ports 2102, 2103 as alternates) |
| **VRS** | Yes (network RTK corrections) |
| **tariff — RTK 1 month** | VND 750,000 / rover (~$29.5 USD @ 25,420 VND/USD) |
| **tariff — RTK 6 months** | VND 4,280,000 / rover (~$168.4 USD) |
| **tariff — RTK 12 months** | VND 6,750,000 / rover (~$265.6 USD) |
| **tariff — RTK 12 months (sparse zones)** | Free (stations >80 km spacing zones) |
| **VAT status** | Not explicitly stated on public page; Vietnamese government data services subject to state-set fee schedule under Circular TT47/2024; VAT applicability unclear |
| **Fee authority** | Circular No. 47/2024/TT-BTC (Ministry of Finance); original authority Circular No. 03/2020/TT-BTNMT (MONRE, 29 May 2020) |
| **hobbyist_eligibility** | Yes — registration explicitly open to "organizations and individuals" (tổ chức và cá nhân); registration requires scan of Citizen Identity Card or Passport; no surveying licence required |
| **legal_residency_required** | No — Passport-based registration accepted (passport explicitly listed alongside Citizen ID); foreign nationals can register |
| **last_confirmed_alive** | 2026-04-30 (gddt.vngeonet.vn homepage loaded with active service listings) |

## Context Notes

- **VNGEONET** (`vngeonet.vn:2101`): Operated by the Vietnamese government under MONRE. The connection guide at `gddt.vngeonet.vn` documents the endpoint as "IP máy chủ (Host IP): 14.238.1.125 (hoặc vngeonet.vn). Cổng (Port): 2101 hoặc 2102 hoặc 2103." Provides nationwide RTK corrections.
- **Free tier**: Areas with reference station spacing exceeding 80 km qualify for free 12-month access; this likely applies to remote/rural regions where the network is less dense.
- **Registration**: Requires a scan of national ID or passport submitted through the registration portal. Individual access explicitly supported.
- **Pricing source**: Tariff figures published on the gddt.vngeonet.vn homepage service cards (loaded via JavaScript); the authoritative legal schedule is Circular No. 47/2024/TT-BTC.

## Post-Processing (RINEX) Fallback

Post-processing RINEX data is not described as a primary offering; the VNGEONET service is focused on real-time correction delivery. Contact MONRE / gddt.vngeonet.vn for RINEX data availability.

## Sources Consulted
- VNGEONET portal: https://gddt.vngeonet.vn/ (homepage service cards, 2026-04-30)
- Connection guide snippet at gddt.vngeonet.vn (host/port details)
- Circular No. 47/2024/TT-BTC (Ministry of Finance fee schedule)
- Circular No. 03/2020/TT-BTNMT (MONRE, original authority)
