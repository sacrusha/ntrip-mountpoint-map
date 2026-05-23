# Kyrgyzstan [KG] - NTRIP RTK Caster Research

last_verified_date: 2026-05-23
last_gap_fill_date: 2026-05-23
last_caster_search_date: 2026-05-23
agent_version: 0.1

## Status: YES - KyrPOS national CORS/RTK network active and priced; contract registration required; endpoint port 8085 not reachable from outside Kyrgyzstan. One IGS station (BIK000KGZ0) in Bishkek for scientific use only.

## KyrPOS - State Agency for Land Resources, Cadastre, Geodesy and Cartography

| Field | Value |
|---|---|
| operator | GAZRKGK (State Agency for Land Resources, Cadastre, Geodesy and Cartography of the Kyrgyz Republic; gosatlas/gosreg.gov.kg) |
| landing_url | https://gosreg.gov.kg/ky/?page_id=3029 |
| access_url | https://gosreg.gov.kg/ky/?page_id=3029 |
| access_type | paid |
| coverage | 18 permanent CORS across 5 oblasts: Chui/Bishkek 6, Fergana Valley/Osh 8, Naryn 1, Issyk-Kul 3. Chui plain and Fergana have best coverage; Naryn, Batken, parts of Jalal-Abad underserved. High terrain in mountain corridors degrades VRS. |
| num_stations | 18 |
| tariff | 170 KGS / day per receiver; 3,180 KGS / month per receiver (minimum 1 month; weekends and public holidays not counted). At May 2026 KGS/USD ~86, 3,180 KGS ~= USD 37 / month. VAT inclusion not declared. Date observed: 2026-05-23 via gosreg.gov.kg/ky/?page_id=3029 |
| hobbyist_eligibility | ? - registration requires a signed contract with the receiver's make, model, and serial number; no individual / hobbyist category listed; non-professionals are not explicitly excluded but workflow (signed contract, postal mailing, KGS bank transfer) is a bureaucratic barrier (checked: gosreg.gov.kg/ky/?page_id=3029 2026-05-23) |
| sourcetable | host:port `cors.gosreg.gov.kg:8085` published (non-standard NTRIP port); ECONNREFUSED from sandbox 2026-05-23; no third-party confirmation of geo-block / firewall published (checked: gosreg.gov.kg/ky/?page_id=3029 2026-05-23; monitor.use-snip.com 2026-05-23; ntrip-list.com 2026-05-23) |
| vrs | ? - 18 stations across 5 oblasts with Chui plain density potentially under 70 km could enable NRTK; operator portal lists tariff per "receiver" without product distinction; no NRTK / VRS / MAC declaration surfaced (checked: gosreg.gov.kg/ky/?page_id=3029 2026-05-23) |
| residency_required | ? - contract workflow involves Kyrgyz postal mailing of signed copies + KGS bank transfer + physical office visit (Bishkek, ul. Orozbekova 44); non-resident eligibility not addressed by the portal |
| stations_source | https://gosreg.gov.kg/ky/?page_id=3029 (text-only oblast breakdown; no public station map; sourcetable not externally reachable to confirm mountpoint list) |

The connection form, detailed service description, host:port `cors.gosreg.gov.kg:8085`, and tariff are re-confirmed at https://gosreg.gov.kg/ky/?page_id=3029 (refetched 2026-05-23). Port 8085 is non-standard for NTRIP (standard 2101) but used here. WebFetch probe of `cors.gosreg.gov.kg:8085` returns ECONNREFUSED from sandbox - likely IP-filtered or restricted to credentialed clients (no third-party confirmation of geo-block, but the consistent ECONNREFUSED across multiple test dates is consistent with a closed credential-gated caster, not a misconfiguration). Access workflow (per the official page): (1) download contract template; (2) fill receiver make/model/serial + period; (3) email contract to kyrposgnss@gosreg.gov.kg; (4) agency issues login credentials; (5) two printed contract copies mailed back; (6) sign + register; (7) bank payment; (8) deliver signed contract + receipt to physical office; (9) phone 0312 664937 for follow-up. Portal registration with QR-code payment is also available; multiple sub-accounts (per receiver) under one portal account. Agency contact: kyrposgnss@gosreg.gov.kg; phone 0312 664937; general gazr@mail.gov.kg; Bishkek, ul. Orozbekova 44. No reference-frame statement appears on the connection page; CAIAG operates BIK000KGZ0 in IGS20 for scientific use, but that is not declared as a national KG frame (checked: gosreg.gov.kg/ky/?page_id=3029 2026-05-23; caiag.kg 2026-05-23; web search "Kyrgyzstan national datum CORS GSK-2011 SK-42 reference frame" 2026-05-23). datum_epoch omitted.

## IGS / scientific station

`BIK000KGZ0` (Bishkek, 42.85 N / 74.53 E) is an active IGS station - Septentrio POLARX5, GPS+GLO+GAL+BDS+QZS+IRS+SBAS, rebroadcast through GFZ on `caster.cddis.eosdis.nasa.gov:443` (verified 2026-05-23 in `data/igs_ip.sourcetable` row 36; `solution=1` flag drops the row from the pipeline output, but the row carries real station coordinates and is a legitimate IGS-IP single-base for credentialed scientific use). The Central Asian Institute for Applied Geosciences (CAIAG, caiag.kg) operates this and related geodynamic stations in Bishkek - scientific only, not an RTK corrections stream.

## Hobbyist path

1. **Cheapest cm-class option**: KyrPOS at 170 KGS/day (~USD 2/day) is the most affordable national RTK in the region if you can complete the contract workflow - bureaucratic friction is high but per-day pricing is hobbyist-grade.
2. **Without contract** - self-host a base, or use Galileo HAS (~20 cm horizontal, free, satellite-delivered) for sub-metre work. No free RTK NTRIP option in country.
3. **Scientific post-processing** - BIK000KGZ0 via CDDIS / EarthScope (free non-commercial).

## Post-processing (RINEX) fallback

| Service | URL | Cost |
|---|---|---|
| EarthScope / GAGE GNSS archive (IGS + CAIAG stations) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (account + NULA) |
| CAIAG (Bishkek, scientific) | http://www.caiag.kg | Contact required |

## Sources

- gosreg.gov.kg/ky/?page_id=3029 (refetched 2026-05-23 - host `cors.gosreg.gov.kg:8085`, tariff 170 KGS/day + 3,180 KGS/month, 6-step registration, contact kyrposgnss@gosreg.gov.kg / 0312 664937)
- gosreg.gov.kg agency home page
- ResearchGate "GNSS Permanent Networks in Kyrgyzstan" (18-station breakdown by oblast)
- UN RCCAP-20 workshop (Azamat Karypov 2020): https://unstats.un.org
- CAIAG: http://www.caiag.kg
- WebFetch probe of `cors.gosreg.gov.kg:8085` - ECONNREFUSED from sandbox 2026-05-23 (consistent with prior probes; closed / credential-gated; not externally confirmed as geo-block)
- Local 2026-05-23: `scripts/stations_by_country.py KGZ` returns no pipeline-visible stations (BIK000KGZ0 is `solution=1`-filtered); `data/igs_ip.sourcetable` row 36 confirms the IGS-IP station exists
