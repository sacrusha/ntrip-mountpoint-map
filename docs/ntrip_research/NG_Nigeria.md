# Nigeria [NG] — NTRIP RTK Caster Research
**Date researched:** 2026-05-12

## Status: YES — NIGNET operates a live NTRIP caster ("MIRACaster") at `ntrip.nignet.net:21011` via the MIRAnet portal `miranet.nignet.net` (operator MIRASpaco under contract to OSGOF). Pricing/registration policy not published publicly — account approval is manual.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes (MIRACaster), but account approval is manual and not self-service |
| **Network name** | NIGNET (Nigerian GNSS Reference Network) |
| **Operator** | Office of the Surveyor-General of the Federation (OSGOF) — osgof.gov.ng — service hosted and operated by MIRASpaco (miraspaco.com) |
| **Caster portal** | https://miranet.nignet.net/ (MIRAnet — "GNSS Data Management Platform") |
| **host:port** | `ntrip.nignet.net:21011` (MIRACaster). Authentication: username + auto-generated password issued by OSGOF/MIRASpaco after manual approval |
| **mountpoints** | Sourcetable not publicly browsable without credentials. Historical academic test used mountpoint CLBR (Calabar). Other documented NIGNET stations: ABUZ (Zaria), BKFP (Birnin Kebbi), CGGT (Toro), FUTY (Yola), GEMB (Gembu), HUKP (Kano), MDGR (Maiduguri), OSGF (Abuja), RUST (Port Harcourt), ULAG (Lagos), UNEC (Enugu), UNIPORT, UYAK, etc. — assumed represented as caster mountpoints when stations are live |
| **tariff** | Not publicly published. OSGOF's own communications state "after payment of subscription fees"; specific NGN amounts and tier structure are not on the public MIRAnet/OSGOF pages |
| **VRS** | Unclear — MIRAnet platform supports raw single-base streams; whether a network/VRS product is offered is not documented publicly |
| **hobbyist_eligibility** | Unclear / unlikely in practice — registration form collects "Full Name, Email, Organization, Telephone, Preferred Username" suggesting institutional intent; no explicit hobbyist tier published |
| **legal_residency_required** | Not explicitly stated — registration form does not require a Nigerian ID number or address, but practical approval workflow is at OSGOF/MIRASpaco discretion |
| **last_confirmed_alive** | miranet.nignet.net live with current UTC clock (observed 2026-05-12); osgof.gov.ng reachable 2026-05-12; raw sourcetable port 21011 not anonymously probable from this sandbox |

## NIGNET Network Details

- **Origin**: NIGNET established by OSGOF in 2008 with 15 stations as Nigeria's contribution to AFREF.
- **Expansion plan**: OSGOF announced a 165-station expansion in 2021 (target ~200 stations at ≤50 km spacing nationwide). Status of rollout is opaque; academic literature flags inconsistent uptime and data continuity at the original ~15 stations.
- **NTRIP implementation history**: A 2017 University of Beira Interior thesis documented building a BKG-based NTRIP caster + PHP/MySQL management system + PayPal billing for NIGNET. The current production deployment (`miranet.nignet.net` + MIRACaster on port 21011) appears to be the productionised continuation of that effort, run by MIRASpaco — a private operator that also installs/rehabilitates GNSS CORS networks in Nigeria, Mozambique, and Angola.
- **OSGOF site link**: The OSGOF homepage menu explicitly links to https://miranet.nignet.net/ as "osgof-cors station", confirming the public-facing portal is the official NIGNET access route.

## MIRACaster Operator (MIRASpaco)

- **Company**: MIRASpaco (miraspaco.com) — develops GNSS CORS installation and rehabilitation systems, dedicated hardware/software, and remote-access management for sub-centimetre precision applications.
- **Public listed activities**: Geocentric reference frame definition, coordinate estimation, post-processing + RTK data management.
- **Public role on NIGNET**: Provides the MIRAnet/MIRACaster platform that fronts NIGNET to subscribed users on behalf of OSGOF.
- No public price list or hobbyist tier on miraspaco.com as of 2026-05-12.

## Volunteer & Open Coverage

- **rtk2go**: 1 NGA station — `fssoyo` (Oyo, 7.84 N 3.95 E; Mobile Geographic SNIP stream, no fee, no auth, RTCM 3.2 MSM). Useful only in the immediate Oyo/Ibadan area.
- **Centipede**: 0 NGA stations.
- **EarthScope (NOTA)**: 0 NGA streams in the NTRIP sourcetable; IGS station ABUZ exists as RINEX archive only.
- **GEODNET / ONOCOY / PointOne**: No NG coverage confirmed as of 2026-05-12.
- **Galileo HAS**: Free PPP-RTK service usable across Nigeria for decimetre-class accuracy (~5 min convergence).

## Most Recent Project Announcement

- **2021**: 165-CORS expansion announcement (Space Watch Africa).
- **2017–present**: NTRIP/MIRAnet productionisation by MIRASpaco for OSGOF.
- **2018+**: NIGNET rehabilitation contract — network design, IT equipment, CORS supply/installation, management software.

No newer 2024–2026 public press release on NIGNET coverage or pricing has been found.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---------|-----|------|
| **NIGNET RINEX archive** — via OSGOF / MIRAnet portal | https://miranet.nignet.net/ | Unknown — account required |
| **IGS / EarthScope** — ABUZ (Zaria) Nigerian IGS station | https://www.earthscope.org/data/gnss-data/ | Free non-commercial (NULA + seat) |

## Sources Consulted
- OSGOF official site: https://osgof.gov.ng/ (observed 2026-05-12; menu links to miranet.nignet.net as "osgof-cors station")
- MIRAnet portal: https://miranet.nignet.net/ (observed 2026-05-12 — host `ntrip.nignet.net`, port 21011, live UTC clock)
- MIRAnet pre-registration form: https://miranet.nignet.net/pre-registration/form (observed 2026-05-12)
- MIRASpaco company page: https://miraspaco.com/ and https://miraspaco.com/gnss/ (observed 2026-05-12)
- UBI thesis on NIGNET NTRIP implementation (2017): https://ubibliorum.ubi.pt/handle/10400.6/5840
- Space Watch Africa — Nigeria 165 CORS expansion: https://spacewatchafrica.com/nigeria-to-establish-new-165-cors-station-beginning-from-2021/
- FMIC — UNECA donation of CORS equipment to OSGOF: https://fmic.gov.ng/uneca-donates-equipment-of-cors-to-osgof/
- DOAJ — NIGNET stability evaluation: https://doaj.org/article/5d416470808f4841bc1d945385f7b1b9
- Academia.edu — Ojigi paper on NIGNET RTK services: https://www.academia.edu/8484226
- ArduSimple Nigeria: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-nigeria/
- Local data: `py scripts/stations_by_country.py NGA` — 1 rtk2go station (`fssoyo`, Oyo), 0 Centipede, 0 EarthScope NTRIP (2026-05-12)
