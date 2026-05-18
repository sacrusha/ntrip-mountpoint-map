# Svalbard [SJ] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17

## Status: LIMITED — free single-base options exist: IGS-IP stream LYR100NOR0 at Longyearbyen (~5.8 km from town); Centipede NYAWIPEV at Ny-Ålesund (~113 km from Longyearbyen, useful for Kongsfjorden); EarthScope/EUREF-IP mirror Ny-Ålesund streams. No NRTK/VRS. CPOS (Kartverket) mainland-only; Kartverket Ny-Ålesund observatory raw RTCM = paid commercial agreement.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | No SJ-operated public caster; mountpoints exist on global casters (IGS-IP, EUREF-IP, EarthScope, Centipede) covering Svalbard physical stations |
| **IGS-IP (BKG)** | `www.igs-ip.net:2101` — `LYR100NOR0` at 78.23°N, 15.40°E = Longyearbyen, 5.8 km from town centre; raw 1 Hz RTCM single-base; BKG account required. Also NABG00NOR0 + WUTH00NOR0 in Ny-Ålesund region |
| **EUREF-IP (BKG/ROB/ASI)** | `euref-ip.net:2101` — `NABG00NOR0` + `WUTH00NOR0` at Ny-Ålesund region; same BKG account; no LYR1 (LYR1 = IGS, not EUREF) |
| **AUSCORS rebroadcast** | `ntrip.data.gnss.ga.gov.au:2101` carries `NYA200NOR0` (Ny-Ålesund) — selected international rebroadcast; gnss.ga.gov.au registration |
| **Volunteer (Centipede)** | 1 node — `NYAWIPEV` at 78.923°N, 11.923°E (Ny-Ålesund) — `caster.centipede.fr:2101`; operated at AWIPEV Franco-German Arctic research station. Local Centipede archive tag SJM, confirmed 2026-05-17 |
| **Volunteer (rtk2go)** | 0 SJ bases |
| **CPOS (Kartverket, Norway)** | Excludes Svalbard — Kartverket Guide to CPOS: "The service covers mainland Norway." `159.162.103.14:2101` |
| **Kartverket geodetic observatory** | Ny-Ålesund Brandal observatory operates permanent GNSS; raw RTCM 3.2 MSM5 available via paid data agreement (post@kartverket.no); not a public caster |
| **hobbyist_eligibility** | Yes — IGS-IP/EUREF-IP free with BKG registration; AUSCORS free CC BY 4.0; Centipede free open; Kartverket commercial only |
| **legal_residency_required** | No (all the free options) |
| **last_confirmed_alive** | 2026-05-17 — `py scripts/stations_by_radius.py 78.22 15.65 200` returns LYR100NOR0 (igs_ip 5.8 km), NYAWIPEV (centipede 113 km), NABG00NOR0 (euref_ip 116 km), NYA200NOR0 (auscors 115 km) |
| **tariff** | IGS-IP/EUREF-IP/AUSCORS/Centipede: free; Kartverket data: price on application |

## CPOS Does Not Cover Svalbard

Kartverket's CPOS service is explicitly described as covering "mainland Norway" (fastlandet). In Norwegian geodetic context this means Norway without Svalbard and Jan Mayen. CPOS users in Longyearbyen or elsewhere on Svalbard cannot receive VRS corrections from the CPOS caster at `159.162.103.14:2101` because no Svalbard reference stations feed into the CPOS network solution.

ETPOS (Kartverket post-processing, included with CPOS subscription) similarly uses mainland stations; NOK 8,000 + VAT/yr if purchased standalone.

## Kartverket Geodetic Observatory at Ny-Ålesund

The Norwegian Mapping Authority operates a geodetic earth observatory at Ny-Ålesund, Svalbard — the northernmost of its kind globally. The Brandal facility (opened 2018) includes a 20 m VLBI radio telescope plus permanent GNSS receivers. Kartverket provides the GNSS station data in RTCM 3.2 MSM5 format to third parties who purchase it under data agreements, for use in their own positioning services. This is not a public NTRIP caster; it is a paid raw-data feed for operators building services.

The Satref control center (`satref.geodesi.no`) monitors Kartverket's positioning infrastructure including Svalbard stations.

## LYR1 — Longyearbyen IGS-IP stream (primary Svalbard option)

The IGS station `LYR1` at 78.23°N, 15.40°E sits ~5.8 km from Longyearbyen town centre. It streams real-time raw 1 Hz RTCM via the BKG IGS broadcaster `www.igs-ip.net:2101` as mountpoint `LYR100NOR0`. Single-base RTK from a rover anywhere in Longyearbyen, Adventdalen, Bjørndalen, etc. (<10 km) is well within ideal single-base baseline. Free with BKG registration; same account as EUREF-IP.

## NYAWIPEV Centipede Node + Ny-Ålesund EUREF-IP stations

For Kongsfjorden / Ny-Ålesund users: Centipede `NYAWIPEV` (free, open), plus EUREF-IP / EarthScope mirrors of `NABG` / `NYA1` / `NYA2`. Practical single-base coverage radius ~20–40 km — sufficient for Ny-Ålesund and Kings Bay operations. Longyearbyen is too far (113 km) from NYAWIPEV — use LYR1 instead.

The AWIPEV Arctic Research Station is jointly operated by the Alfred Wegener Institute (AWI, Germany) and the Institut polaire français Paul-Émile Victor (IPEV, France).

## Most Recent Project Announcement

No announced Kartverket plan to extend CPOS or DPOS to Svalbard as of 2026-05-13. Kartverket's "Guide to CPOS" still states the service covers "mainland Norway" without further extension. Kartverket's 2023–2024 Svalbard white paper analysis (High North News) addresses sovereignty and infrastructure but does not reference a public RTK correction service expansion.

No additional Centipede or rtk2go nodes for Svalbard have been announced.

## Context Notes

- **Practical RTK for Longyearbyen**: LYR1 IGS-IP stream is the answer — 5.8 km baseline, single-base RTK quality, free BKG account.
- **EUREF / IGS / EarthScope** all mirror Ny-Ålesund stations. EarthScope `ntrip.earthscope.org:2101` requires NULA non-commercial click-through; BKG/ROB euref-ip require BKG account. Raw 1 Hz RTCM single-base — no VRS/NRTK.
- **GEODNET / ONOCOY**: No node in Svalbard.
- **Datum of broadcast streams**: LYR1 / NABG / WUTH / NYA1 are IGS-realisation stations — IGS20 / ITRF2020 global frame (rover position lands in global frame; for ETRS89/EUREF89 Norway grid, transform downstream).
- **Hobbyist RTK summary**: Longyearbyen → LYR1 IGS-IP. Ny-Ålesund / Kongsfjorden → Centipede NYAWIPEV (no signup) or BKG EUREF-IP `NABG` / IGS-IP `NYA1`. Rest of Svalbard (Sveagruva, Pyramiden, Barentsburg) → outside single-base range from all options; deploy own base or use PPP.

## Datum / Epoch

- **LYR1, NABG, WUTH, NYA1 (IGS / EUREF-IP / EarthScope mirrors)**: IGS stations broadcast in the current IGS realisation of ITRF. No SJ-specific operator declaration; the streams adopt IGS conventions (currently IGS20 ≈ ITRF2020). `omitted -- no SJ operator declaration` per primer [datum-epoch] citation rule (IGS-IP / EUREF-IP are themselves the operator; declaration depends on which broadcaster you use).
- **Centipede NYAWIPEV**: Centipede docs note "ITRF for positioning outside Europe" (https://docs.centipede.fr/docs/centipede/4_Systeme2reference.html) — citable for outside-Europe nodes; Svalbard is on Eurasian plate but operator does not name an epoch for non-FR nodes.
- **CPOS (mainland NO only, does NOT cover SJ)**: declared EUREF89 (NN1954/NN2000 vertical), per https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos — epoch not stated.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / GAGE** (IGS stations NYA1, NYAL at Ny-Ålesund) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **Kartverket ETPOS** (mainland-only, NOT Svalbard) | https://www.kartverket.no/en/on-land/posisjon/guide-to-etpos | NOK 8,000 + VAT/yr (or free with CPOS subscription) |

## Sources Consulted
- IGS-IP / EUREF-IP BKG broadcaster: https://igs.bkg.bund.de/ntrip/ — LYR1 mountpoint LYR100NOR0 (Longyearbyen, 5.8 km from town); NABG / WUTH / NYA1 / NYA2 in Ny-Ålesund region
- Local: `py scripts/stations_by_radius.py 78.22 15.65 200` 2026-05-17 → 8 stations across igs_ip + euref_ip + centipede + auscors + mirai
- Centipede reference systems: https://docs.centipede.fr/docs/centipede/4_Systeme2reference.html — ITRF outside Europe; no epoch declared for non-FR nodes
- Kartverket Guide to CPOS: https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos — confirms "mainland Norway" + EUREF89 reference frame (no epoch)
- Kartverket User Guide Positioning Services: https://www.kartverket.no/en/on-land/posisjon/user-guide-positioning-services
- Kartverket Geodetic Earth Observatory: https://www.kartverket.no/en/about-kartverket/geodetic-earth-observatory
- Kartverket Observatory information: https://www.kartverket.no/en/about-kartverket/geodetic-earth-observatory/information-about-the-observatory
- Kartverket satellite and positioning data: https://proxy.kartverket.no/en/api-and-data/satellite-and-positiong-data
- Satref control center: https://satref.geodesi.no/
- AWIPEV Arctic Research Station: https://www.awipev.eu/ · https://institut-polaire.fr/en/arctic/awipev-station/
- Centipede-RTK network: https://www.centipede-rtk.org/ · https://map.centipede-rtk.org/
- EarthScope GNSS realtime: https://www.earthscope.org/data/gnss-realtime/
- High North News Svalbard White Paper analysis: https://www.highnorthnews.com/en/sovereignty-governance-and-infrastructure-analysis-svalbards-white-paper-2023-2024
