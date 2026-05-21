# Svalbard [SJ] — NTRIP RTK Caster Research

## Status: LIMITED — free single-base options exist: IGS-IP stream LYR100NOR0 at Longyearbyen (~5.8 km from town); Centipede NYAWIPEV at Ny-Ålesund (~113 km from Longyearbyen, useful for Kongsfjorden); EarthScope/EUREF-IP mirror Ny-Ålesund streams. No NRTK/VRS. CPOS (Kartverket) mainland-only; Kartverket Ny-Ålesund observatory raw RTCM = paid commercial agreement.

No SJ-operated public caster. Svalbard stations stream via global casters (IGS-IP, EUREF-IP, EarthScope, Centipede). No NRTK/VRS available; single-base only.

## Option A: IGS-IP / EUREF-IP (BKG) — primary free option

| Field | Value |
|---|---|
| **landing_url** | https://igs.bkg.bund.de/ntrip/ |
| **access_url** | https://igs.bkg.bund.de/ntrip/ (BKG account required; same account grants IGS-IP + EUREF-IP) |
| **host:port — IGS-IP** | `www.igs-ip.net:2101` |
| **host:port — EUREF-IP** | `euref-ip.net:2101` |
| **Svalbard mountpoints on IGS-IP** | `LYR100NOR0` (78.23°N/15.40°E — Longyearbyen, 5.8 km from town); `NABG00NOR0` + `NYA200NOR0` (Ny-Ålesund 78.92°N/11.87°E); `WUTH00NOR0` (Hornsund **77.00°N/15.54°E** — Polish polar station Hornsund, ~130 km SSE of Ny-Ålesund, not Ny-Ålesund region) |
| **Svalbard mountpoints on EUREF-IP** | `NABG00NOR0` + `WUTH00NOR0` (Hornsund); LYR1 is IGS-only |
| **vrs** | No — single-base only |
| **tariff** | Free (BKG account) |
| **hobbyist_eligibility** | Yes |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-21 — local sourcetable 2026-05-19 confirms all mountpoints listed above |
| **datum_epoch** | omitted — no operator declaration per primer [datum-epoch] citation rule (see Datum / Epoch section) |

## Option B: Centipede — Ny-Ålesund only

| Field | Value |
|---|---|
| **landing_url** | https://www.centipede-rtk.org/ |
| **access_url** | https://www.centipede-rtk.org/ (no registration required) |
| **host:port** | `caster.centipede.fr:2101` |
| **Mountpoint** | `NYAWIPEV` at 78.923°N/11.923°E — Ny-Ålesund, operated at AWIPEV Franco-German Arctic research station |
| **vrs** | No — single-base |
| **tariff** | Free |
| **hobbyist_eligibility** | Yes |
| **legal_residency_required** | No |
| **last_confirmed_alive** | 2026-05-21 — confirmed in local centipede.sourcetable 2026-05-19 (SJM country tag) |
| **datum_epoch** | omitted — no operator epoch declaration for non-FR nodes |

## Option C: AUSCORS rebroadcast — Ny-Ålesund

| Field | Value |
|---|---|
| **host:port** | `ntrip.data.gnss.ga.gov.au:2101` |
| **Mountpoint** | `NYA200NOR0` (Ny-Ålesund) |
| **tariff** | Free, CC BY 4.0 |
| **hobbyist_eligibility** | Yes |
| **last_confirmed_alive** | 2026-05-19 (local AUSCORS sourcetable) |

## CPOS / Kartverket (not available to general subscribers)

Kartverket's CPOS service covers "mainland Norway" only (fastlandet — explicitly excludes Svalbard and Jan Mayen). CPOS users in Longyearbyen or elsewhere on Svalbard cannot receive VRS corrections because no Svalbard stations feed the CPOS network solution.

A mountpoint named `SVALBARD` is present in the CPOS sourcetable (live-confirmed 2026-05-21: RTCM 3.1, carrier 2, lat/lon=0, nmea=1 — same VRS/network-product pattern as all other CPOS mountpoints). The Kartverket Guide to CPOS makes no mention of Svalbard coverage. This mountpoint likely routes through Kartverket's Ny-Ålesund geodetic observatory data, available only via paid data agreements (post@kartverket.no; pricing not public) — not via standard CPOS subscription. The "CPOS covers mainland Norway only" conclusion stands.

ETPOS (Kartverket post-processing) similarly uses mainland stations only; NOK 8,000 /yr ex-VAT as a separate line item on the Kartverket price page (not bundled with CPOS; see NO_Norway).

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

- **LYR1, NABG, WUTH, NYA1 (IGS / EUREF-IP / EarthScope mirrors)**: omitted — no operator declaration for these specific streams per primer [datum-epoch] citation rule. Contextual note: IGS stations broadcast in the current IGS realisation of ITRF (IGS-IP and EUREF-IP are themselves the broadcasters; frame depends on which you connect to).
- **Centipede NYAWIPEV**: Centipede docs note "ITRF for positioning outside Europe" (https://docs.centipede.fr/docs/centipede/4_Systeme2reference.html) — citable for outside-Europe nodes; Svalbard is on Eurasian plate but operator does not name an epoch for non-FR nodes.
- **CPOS (mainland NO only, does NOT cover SJ)**: declared EUREF89 (NN1954/NN2000 vertical), per https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos — epoch not stated.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **EarthScope / GAGE** (IGS stations NYA1, NYAL at Ny-Ålesund) | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |
| **Kartverket ETPOS** (mainland-only, NOT Svalbard) | https://www.kartverket.no/en/on-land/posisjon/guide-to-etpos | NOK 8,000 /yr ex-VAT (separate line item; not bundled with CPOS) |

## Sources Consulted
- IGS-IP / EUREF-IP BKG broadcaster: https://igs.bkg.bund.de/ntrip/ — LYR100NOR0 (Longyearbyen); NABG00NOR0 / NYA200NOR0 (Ny-Ålesund); WUTH00NOR0 (Hornsund 77.00°N/15.54°E)
- Local: `py scripts/stations_by_radius.py 78.22 15.65 200` 2026-05-17 → 8 stations across igs_ip + euref_ip + centipede + auscors + mirai
- Centipede reference systems: https://docs.centipede.fr/docs/centipede/4_Systeme2reference.html — ITRF outside Europe; no epoch declared for non-FR nodes
- Kartverket Guide to CPOS: https://www.kartverket.no/en/on-land/posisjon/guide-to-cpos — confirms "mainland Norway" + EUREF89 reference frame (no epoch)
- Kartverket User Guide Positioning Services: https://www.kartverket.no/en/on-land/posisjon/user-guide-positioning-services
- Kartverket Geodetic Earth Observatory: https://www.kartverket.no/en/about-kartverket/geodetic-earth-observatory
- Kartverket Observatory information: https://www.kartverket.no/en/about-kartverket/geodetic-earth-observatory/information-about-the-observatory
- Kartverket satellite and positioning data: https://proxy.kartverket.no/en/api-and-data/satellite-and-positiong-data (2026-05-21 — RTCM 3.2 MSM5 in datum EUREF89/ellipsoidal heights; pricing not public; sold via post@kartverket.no)
- Satref control center: https://satref.geodesi.no/
- AWIPEV Arctic Research Station: https://www.awipev.eu/ · https://institut-polaire.fr/en/arctic/awipev-station/
- Centipede-RTK network: https://www.centipede-rtk.org/ · https://map.centipede-rtk.org/
- EarthScope GNSS realtime: https://www.earthscope.org/data/gnss-realtime/
- High North News Svalbard White Paper analysis: https://www.highnorthnews.com/en/sovereignty-governance-and-infrastructure-analysis-svalbards-white-paper-2023-2024
