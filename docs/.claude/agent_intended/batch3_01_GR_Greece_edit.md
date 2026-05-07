# Agent intended Edit
- batch: batch3
- target: D:\Projects\ntrip-mountpoint-map\docs\ntrip_research\GR_Greece.md
- transcript line: 165

## OLD_STRING

```markdown
# Greece [GR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — national NTRIP RTK caster operating (HEPOS); paid subscription; second private network (JGC-Net) also available

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Network name — primary** | HEPOS (Hellenic POsitioning System) |
| **Operator — HEPOS** | KTIMATOLOGIO S.A. (Hellenic Cadastre) |
| **host:port — HEPOS** | `ntrip.hepos.gr:2101` (also documented as `www.hepos.gr:2101`; credentials issued after registration) |
| **VRS — HEPOS** | Yes — Network RTK / VRS corrections; RTCM 3.1 (GPS+GLONASS) and RTCM 3.2 MSM (full GNSS) |
| **tariff — 3 months flat-rate RTK** | €160.00 excl. VAT (source: hepos.gr/en/product/real-time-services-flat-rate-3-months-rtk/, observed 2026-05-06) |
| **tariff — 1 year flat-rate RTK** | €480.00 excl. VAT (source: hepos.gr/en/product/real-time-services-flat-rate-1-year-rtk/, observed 2026-05-06) |
| **tariff — per-minute RTK** | €90.00 excl. VAT per bundle (source: hepos.gr/en/product/real-time-services-per-minute/, observed 2026-05-06) |
| **VAT** | Greek standard VAT is 24%; prices listed above are net |
| **hobbyist_eligibility** | Yes — individual registration accepted; no licensed surveyor requirement stated |
| **legal_residency_required** | Unclear — subscription/payment is online; no explicit residency restriction stated; Greek VAT registration may be required for invoice |
| **last_confirmed_alive** | 2026-05-06 (hepos.gr loaded normally; product/subscription pages returned HTTP 200; Akamai CDN 403 blocks direct curl but pages confirmed via search-engine cache) |
| **Network name — secondary** | JGC-Net |
| **Operator — JGC-Net** | JGC Geoinformation Systems S.A. (private distributor) |
| **host:port — JGC-Net** | Not publicly listed; credentials issued after commercial registration with JGC |
| **tariff — JGC-Net** | Not publicly listed; contact jgc.gr |
| **VRS — JGC-Net** | Yes — fixed to HTRS07 reference system; ~2 cm accuracy within 50 km of each station |
```

## NEW_STRING

```markdown
# Greece [GR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06 (updated 2026-05-07: separated URANUS from HEPOS; URANUS is a private commercial network, not a HEPOS hostname)

## Status: YES — national NTRIP RTK caster operating (HEPOS, paid); two private commercial networks (URANUS / TopNET, JGC-Net) also available

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid only — no free national NTRIP RTK in Greece) |
| **Network name — primary** | HEPOS (Hellenic POsitioning System) |
| **Operator — HEPOS** | KTIMATOLOGIO S.A. (Ελληνικό Κτηματολόγιο / Hellenic Cadastre) |
| **host:port — HEPOS** | Issued to user after registration (port 2101 standard NTRIP). Public-facing site at `www.hepos.gr`; the actual NTRIP caster hostname is delivered with credentials. Earlier documentation has cited `ntrip.hepos.gr:2101` but no public sourcetable is reachable without an account. Akamai CDN blocks anonymous curl on hepos.gr (returns HTTP 403 Forbidden) so direct pipeline scraping is not feasible. |
| **VRS — HEPOS** | Yes — Network RTK / VRS corrections; RTCM 3.1 (GPS+GLONASS) and RTCM 3.2 MSM (full GNSS) |
| **tariff — 3 months flat-rate RTK** | €160.00 excl. VAT (source: hepos.gr/en/product/real-time-services-flat-rate-3-months-rtk/, observed 2026-05-06) |
| **tariff — 1 year flat-rate RTK** | €480.00 excl. VAT (source: hepos.gr/en/product/real-time-services-flat-rate-1-year-rtk/, observed 2026-05-06) |
| **tariff — per-minute RTK bundle** | €90.00 excl. VAT one-time bundle (per-minute rate not separately published; source: hepos.gr/en/product/real-time-services-per-minute/, observed 2026-05-06) |
| **VAT** | Greek standard VAT is 24%; prices listed above are net |
| **hobbyist_eligibility — HEPOS** | Yes — individual registration accepted; no licensed surveyor requirement stated |
| **legal_residency_required — HEPOS** | Unclear — subscription/payment is online; no explicit residency restriction stated; Greek VAT registration may be required for invoice |
| **last_confirmed_alive — HEPOS** | 2026-05-06 (hepos.gr loaded normally; product/subscription pages returned HTTP 200; Akamai CDN 403 blocks anonymous curl but pages confirmed via search-engine cache) |
| **Network name — secondary 1** | URANUS — TopNET Live Greece |
| **Operator — URANUS** | Tree Company Corporation A.E.B.E. (Treecomp) — private commercial Topcon distributor |
| **host:port — URANUS** | `www.uranus.gr` / NTRIP caster credentials issued after registration; ntrip-list.com lists URANUS as the public free-trial face (3-day trial); commercial subscription thereafter |
| **VRS — URANUS** | Yes — VRS Network RTK; 117 reference stations across Greece + Cyprus; advertised 99% coverage; GPS, GLONASS, Galileo, BeiDou |
| **tariff — URANUS** | Paid (rates not publicly listed; 3-day free trial available; contact uranus@treecomp.gr / +30 210 9473600) |
| **last_confirmed_alive — URANUS** | 2026-05-06 (uranus.gr/home-page loaded HTTP 200; service marketed as 24/7 operational) |
| **Network name — secondary 2** | JGC-Net |
| **Operator — JGC-Net** | JGC Geoinformation Systems S.A. (private Spectra/Nikon/NovAtel distributor) |
| **host:port — JGC-Net** | Not publicly listed; credentials issued after commercial registration with JGC |
| **tariff — JGC-Net** | Not publicly listed; contact jgc.gr |
| **VRS — JGC-Net** | Yes — fixed to HTRS07 reference system; ~2 cm accuracy within 50 km of each station |
```
