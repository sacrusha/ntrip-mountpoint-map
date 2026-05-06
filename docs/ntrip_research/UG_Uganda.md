# Uganda [UG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-06

## Status: YES — free national NTRIP (UGRF CORS); registration via Spider Business Center required

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes |
| **Operator** | MLHUD — Ministry of Lands, Housing and Urban Development; Department of Surveys and Mapping |
| **Service name** | UGRF (Uganda Geodetic Reference Frame) CORS Network |
| **host:port** | `ugrf.mlhud.go.ug:2101` (IP: 154.72.216.21:2101) |
| **VRS** | Yes — mountpoints: VRSRTCM3, MAXRTCM3 (network RTK); also iMAX_RTCM, FKP_RTCM |
| **Constellations** | GPS+GLONASS (primary); GPS+GLO+GAL+BDS on NEAREST mountpoint |
| **Number of reference stations** | 40 government stations (78 total including 38 private); 44 mountpoints visible in sourcetable |
| **tariff** | Free — expected to remain free for the foreseeable future; future maintenance fee possible |
| **hobbyist_eligibility** | Yes — no professional licence requirement stated; open registration |
| **legal_residency_required** | Unclear — registration via ugrf.mlhud.go.ug/SBC; no explicit residency restriction found |
| **last_confirmed_alive** | `ugrf.mlhud.go.ug:2101` returned SOURCETABLE 200 OK on 2026-05-06; Leica GNSS Spider 7.10.1.168; 44 mountpoints |

## Sourcetable Observations (2026-05-06)

Confirmed mountpoints include: `ENTB` (Entebbe ref station), `NEAREST`, `MAXRTCM3`, `VRSRTCM3`, `iMAX_RTCM`, `FKP_RTCM`, `JING` (Jinja), `MBAL` (Mbarara), `FPRT` (Fort Portal), `GULU`, `ARUA`, `KBLE` (Kabale), `LIRA`, `MRTO` (Moroto). All RTCM 3; GPS+GLO primary. VRS (VRSRTCM3) and network correction (MAXRTCM3, iMAX_RTCM, FKP_RTCM) mountpoints confirm network RTK capability, not just single-base.

## Context Notes

- UGRF is one of the few free, publicly accessible national NTRIP casters in Sub-Saharan Africa with a confirmed live sourcetable.
- The network comprises 40 government CORS + 38 private stations = 78 total. 14+ station names visible in sourcetable covering the country from Arua (north) to Kabale (south), Moroto (east) to Fort Portal (west).
- VRS accuracy: better than 1–2 cm within 20 km of a station; 5 cm within 80 km with network RTK.
- Registration: create account at https://ugrf.mlhud.go.ug/SBC (Spider Business Center login page). NTRIP credentials provided after account creation.
- The UGRF portal (ugrf.mlhud.go.ug) returned ECONNREFUSED on HTTP fetch but the NTRIP port 2101 responded normally — portal may be HTTPS-only or temporarily misconfigured.
- National Workshop on UGRF held November 2024; network expansion, enhanced training, and updated legal frameworks discussed.
- Post-processing RINEX download also available via the SBC portal.
- 40 government CORS stations provide geodetic data for land administration, infrastructure, disaster monitoring, and cadastral surveys.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **UGRF SBC RINEX download** | https://ugrf.mlhud.go.ug/SBC | Free (account required) |
| **IGS online post-processing via EarthScope** | https://www.earthscope.org/data/gnss-data/ | Free non-commercial |

## Sources Consulted
- Uganda UGRF FAQ (CORS access): http://ugrf.mlhud.go.ug/faq/cors-real-time-corrections (ECONNREFUSED 2026-05-06; content from cached search result)
- Uganda UGRF Spider Business Center: http://ugrf.go.ug/SBC (accessed via search result)
- MLHUD National Workshop on UGRF 2024: https://mlhud.go.ug/national-workshop-on-ugandas-geodetic-reference-framework-2024/ (observed 2026-05-06)
- MLHUD Department of Surveys and Mapping: https://mlhud.go.ug/lands-managment/department-of-surveys-and-mapping/ (observed 2026-05-06)
- GIM International UGRF article: https://www.gim-international.com/content/article/establishing-an-accurate-geodetic-reference-network-for-uganda
- curl probe of `ugrf.mlhud.go.ug:2101` (154.72.216.21:2101) — SOURCETABLE 200 OK on 2026-05-06; Leica GNSS Spider 7.10.1.168; 44 mountpoints
