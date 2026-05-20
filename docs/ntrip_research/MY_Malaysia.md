# Malaysia [MY] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; MyRTKnet tariff structure + portal URLs unchanged from 2026-05-12 observation; `gogainet` rtk2go MYS still present)

## Status: YES — MyRTKnet operational; paid only; expensive for hobbyists; no free alternative

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (paid) |
| **landing_url** | https://myrtknet.jupem.gov.my/ (operator-owned MyRTKnet portal — JUPEM Department of Survey and Mapping Malaysia) |
| **access_url** | https://mytransformasinet.jupem.gov.my/ (operator-owned MyRTKnet 2.0 registration / subscription / credential management portal; same JUPEM credentials) |
| **num_stations** | ~78 physical CORS (65 Peninsular + ~13 Sabah & Sarawak; spaced 30–150 km). Cited by JUPEM via the MyRTKnet history pages and FIG 2010 + Coordinates magazine articles; precise current count not exposed on the public portal as live sourcetable is creds-gated. |
| **datum_epoch** | omitted — MyRTKnet portal not reachable from this sandbox (HTTPS TLS verification failure 2026-05-17; ECONNREFUSED on alternate endpoints); no citable GDM2000 declaration confirmed on `myrtknet.jupem.gov.my` or `mytransformasinet.jupem.gov.my`. Per primer, do NOT infer from JUPEM's national datum (GDM2000) declared elsewhere; only operator portal/spec is citable. |
| **host:port — VRS/MAC/iMAX/DGPS** | `pxy.myrtknet.gov.my:2101` |
| **host:port — SB Sabah & Sarawak** | `pxy.myrtknet.gov.my:2102` |
| **host:port — SB Peninsular** | `pxy.myrtknet.gov.my:2103` |
| **network type** | VRS / MAC / iMAX / single-base / DGPS — multiple correction product types |
| **tariff — registration** | RM 1,000 one-time (private sector); RM 500 (government / public university) — observed 2026-05-06; source: myrtknet.jupem.gov.my. *Note: a 50% promotional discount applied Oct 2021–Sep 2022 reducing private registration to RM 500; current standard rate is RM 1,000.* |
| **tariff — annual subscription** | RM 3,000/yr real-time RTK subscription (~USD 670/yr at May 2026 rates) |
| **tariff VAT note** | SST (Sales and Service Tax) status for JUPEM subscriptions not confirmed; above prices are as published, VAT inclusive/exclusive status unconfirmed |
| **hobbyist_eligibility** | Technically yes — no surveying licence required; any entity or individual may apply. Practically prohibitive at RM 1,000 + RM 3,000/yr for a hobbyist |
| **legal_residency_required** | Unclear — registration at myrtknet.jupem.gov.my; no documented explicit residency requirement, but practical friction for foreign applicants (local contact, Malaysian banking) is likely |
| **last_confirmed_alive** | myrtknet.jupem.gov.my and mytransformasinet.jupem.gov.my both returned HTTP 200 on 2026-05-06; MyRTKnet mobile apps (iOS and Android) active on respective stores |

## MyRTKnet Network Details

- **Operator**: JUPEM — Jabatan Ukur dan Pemetaan Malaysia (Department of Survey and Mapping Malaysia), under the Ministry of Energy and Natural Resources
- **Legal basis**: Mandatory cost-recovery service under the Survey Act; JUPEM is not permitted to provide the service free of charge
- **Station count**: ~78 physical reference stations — 65 in Peninsular Malaysia, ~13 in Sabah and Sarawak; spaced 30–150 km apart
- **History**: First deployed 2003 with 27 stations; expanded to 78 stations by 2008. MyRTKnet 2.0 portal (mytransformasinet.jupem.gov.my) is the current version
- **Correction products**: VRS (Virtual Reference Station), MAC (Master-Auxiliary Corrections), iMAX (Individualised Master-Auxiliary), Nearest Base (SB Peninsular, SB Sabah & Sarawak), Network DGPS
- **Registration portal**: https://myrtknet.jupem.gov.my — account creation, subscription purchase, and credential management
- **Contact**: admin.myrtknet@jupem.gov.my
- **Mobile app**: available on Google Play and App Store for station status and subscription monitoring

## Sabah and Sarawak Coverage

MyRTKnet covers both East Malaysian states (Sabah and Sarawak on Borneo) via the dedicated port `:2102`. With ~13 stations covering ~329,847 km² of Borneo territory, average inter-station spacing exceeds 150 km in many areas — the network meets minimum coverage but precision degrades at larger distances from the nearest physical base. Brunei (which surrounds the eastern Sarawak corridor) has no independent NTRIP caster; the nearest practical correction source for Brunei is MyRTKnet Sabah & Sarawak, though cross-border validity requires direct confirmation with JUPEM.

## Volunteer Coverage

rtk2go carries one MYS volunteer base — `gogainet` in Durian Tunggal, Melaka (2.31 N, 102.32 E), still present in the local snapshot 2026-05-12. RTCM 3.3 MSM, no auth, no fee. This single volunteer base provides free RTK within approximately 30–40 km for users in its vicinity but offers no practical alternative for most of the country. No Centipede nodes are present in Malaysia.

## Commercial and Cheaper Alternatives

No cheaper domestic Malaysian commercial NTRIP caster has been identified:
- GEODNET: no confirmed Malaysia production coverage as of 2026-05-06
- HxGN SmartNet / Trimble VRS Now: no confirmed Malaysia production network found; local distributors (JUPEM-licensed vendors) sell hardware but no independent VRS network
- RTKdata / PointOne: no Malaysia production coverage confirmed
- ArduSimple Malaysia page lists MyRTKnet and Galileo HAS (free, 40 cm, no NTRIP) as the only documented options

Galileo High Accuracy Service (HAS) provides a free PPP-RTK correction globally (including Malaysia) without a caster subscription, achieving ~40 cm accuracy after ~5 minutes convergence — not RTK-grade but usable for lower-precision hobbyist applications (drone mapping, GIS fieldwork, hiking).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **MyRTKnet / JUPEM** — RINEX download from reference stations | https://myrtknet.jupem.gov.my/ | Paid subscription required (same credentials) |
| **EarthScope / IGS** — NTUS (Singapore, ~350 km from Kuala Lumpur), BAKO (Indonesia), Darwin | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **SOPAC / IGS archive** — KUAN (Kuantan) if available | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- MyRTKnet portal: https://myrtknet.jupem.gov.my/
- MyRTKnet 2.0 portal: https://mytransformasinet.jupem.gov.my/
- JUPEM official site: https://www.jupem.gov.my/
- "MyRTKnet: Get set and go!" (Coordinates magazine): https://mycoordinates.org/myrtknet-get-set-and-go/all/1/
- "The Malaysia Real-Time Kinematic GNSS Network (MyRTKnet) in 2010 and Beyond" (FIG 2010): http://fig.net/resources/proceedings/fig_proceedings/fig2010/papers/ts08f/ts08f_hasan_azhari_et_al_4742.pdf
- "Assessment of the Accuracy and Precision of MyRTKnet Real-Time Services": https://www.researchgate.net/publication/347669197_ASSESSMENT_OF_THE_ACCURACY_AND_PRECISION_OF_MyRTKnet_REAL-TIME_SERVICES
- Malaysia Gazette — 50% fee reduction announcement (Oct 2021): https://malaysiagazette.com/2021/10/11/bayaran-pendaftaran-pembaharuan-baharu-myrtknet-dikurangkan-50/
- Sinar Harian — MyRTKnet fee reduction: https://www.sinarharian.com.my/article/166400/BERITA/Nasional/Bayaran-daftar-baharu-pembaharuan-MyRTKnet-dikurang-50-peratus
- ArduSimple — RTK correction services Malaysia: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-malaysia/
- NTRIP-list.com Asia: https://ntrip-list.com/asia/
- country-survey.md MY stub (2026-04-29)
- rtk_inventory.md `myrtk` entry
