# Ethiopia [ET] — NTRIP RTK Caster Research
**Date researched:** 2026-05-17 (re-verified; original 2026-05-06)

## Status: PARTIAL — national CORS network launched Dec 2024; NTRIP public access endpoint still not confirmed as of 2026-05-17. No SSGI press release, registration portal, host:port or tariff has been published; direct contact with SSGI remains the only documented access path.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Unknown — CORS network operational, NTRIP endpoint not publicly documented |
| **host:port** | Not publicly confirmed (ssgi.gov.et is the issuing authority) |
| **tariff** | Unknown — contact SSGI |
| **hobbyist_eligibility** | Unclear — no public sign-up portal found |
| **legal_residency_required** | Unclear |
| **last_confirmed_alive** | CORS stations confirmed operational Dec 2024 (state media; see sources). No NTRIP-level reachability verifiable as of 2026-05-17. |
| **datum_epoch** | omitted -- no citable operator declaration (no public SSGI portal) |

## Most Recent Project Announcement

**December 2024 — SSGI ETCORS station network inaugurated.** The Space Science and Geospatial Institute (SSGI) launched 10 Continuously Operating Reference Stations: one in Addis Ababa (main control hub), four in Sheger and surrounding towns, and individual stations in Bonga, Semera, Jigjiga, Debre Berhan, and Jimma. The service name "ETCORS" (Ethiopian Continuously Operating Reference Stations) was confirmed live in state press on or around 2024-12-02.

Sources:
- ENA English (state news): https://www.ena.et/web/eng/w/eng_7825046
- AllAfrica: https://allafrica.com/stories/202512020714.html
- Fana Media: https://www.fanamc.com/english/space-science-and-geospatial-institute-launches-new-satellite-data-collection-stations/

SSGI Director Abdisa Yilma stated plans to expand from 10 to 20 stations within the 2024/25 fiscal year and to 30 stations within two years. The eventual target is ~200 CORS for full national coverage. SSGI stated the service is intended for neighboring countries and the global community as well.

Earlier related milestone: October 2024, SSGI commissioned a GNSS receiving station and magnetometer at the Entoto Observatory and Research Center, Addis Ababa.

## Context Notes

- **ETCORS ≠ NTRIP endpoint confirmed**: State media coverage describes centimeter-level accuracy and real-time use, but no public NTRIP caster URL, port, or sign-up form has been documented in open sources as of research date. The system may require direct contact with SSGI.
- **Contact**: ssgi.gov.et; SSGI is the successor to the Ethiopian Mapping Agency (EMA), later EGIA, merged 2022 into SSGI.
- **Coverage gap**: With only 10 stations, areas more than ~70 km from a reference station will not receive reliable network RTK corrections; single-base RTK from nearby SSGI station is more realistic.
- **AFREF**: Ethiopia has one or more IGS-affiliated CORS (Addis Ababa area) in the AFREF network; those stations are not confirmed to expose a public NTRIP RTK stream.
- **Academic context**: A 2024 ASCE paper designed an optimal Ethiopian CORS network requiring ~228 stations. A 2024 ASCE performance evaluation paper benchmarked existing partial networks.
- **Practical workaround**: Deploy a local base station for single-base RTK, or use satellite-based PPP (Galileo HAS, Trimble RTX).

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **EarthScope / GAGE GNSS Archive** — IGS/AFREF stations in Ethiopia (Addis Ababa) | https://www.earthscope.org/data/gnss-data/ | Free noncommercial (account + NULA) |
| **SSGI / Ethio-NSDI** — national spatial data portal | https://ethionsdi.gov.et/ | Unknown |

## Sources Consulted
- ENA (Ethiopian News Agency) English — SSGI station launch Dec 2024
- AllAfrica — SSGI station launch Dec 2024
- Fana Media Corporation — SSGI station launch
- EBC (Ethiopian Broadcasting Corp.) — "Ethiopia Launches Groundbreaking Real-Time Satellite Data Network"
- Space in Africa — GNSS + magnetometer commission, Oct 2024
- SSGI official site: ssgi.gov.et
- Ethio-NSDI portal: ethionsdi.gov.et
- ASCE Journal of Surveying Engineering — CORS network design study (2024)
- ASCE Journal of Surveying Engineering — CORS network performance evaluation (2024)
- Academia.edu — "Optimum CORS Network Design for Geodetic Applications in Ethiopia"
- GIM International — "Developing a Fully Fledged CORS Map for Africa"
- ArduSimple country selector (no Ethiopia page found)
- RTK2go monitor (no Ethiopian streams confirmed)
