# Free RTK NTRIP — South/Southeast Asia survey: Pakistan, Nepal, Afghanistan, Myanmar

_Research date: 2026-04-21. Entries follow the format and scope of
`docs/country-survey.md` and are ready to paste into the
"Asia Pacific — South & SE Asia" section._

---

### PK — Pakistan

- **Free government RTK**: none confirmed for hobbyists. SUPARCO (Space and
  Upper Atmosphere Research Commission) operates Pak-Rehber, an NRTK
  (Network RTK) service delivering cm-level corrections via GNSS CORS
  network. SUPARCO documentation describes Pak-GBAS as a "proof of concept"
  providing corrections "to authorized users" in Karachi, extendable to
  other regions on request. No public-facing NTRIP host:port, open
  registration portal, or sourcetable has been found; registration
  appears to require direct contact with SUPARCO (Islamabad: +92-51-9075055,
  Karachi: +92-21-34690765). A 2024 IEEE paper used Pak-Rehber for a
  smartphone localisation application, confirming the service is operational,
  but the paper does not disclose station count, endpoint, or access terms.
  Survey of Pakistan (federal mapping authority) does not appear to operate a
  separate public NTRIP caster. SUPARCO is also deploying Pak-SBAS
  (L-band SBAS via PakSAT-MM1) for sub-metre SBAS accuracy — out of scope
  (satellite-delivered, not NTRIP).
- **Volunteer**: rtk2go — 0 confirmed PK bases (bounding box 24–37°N,
  61–77°E returns no stations in data/stations.json as of 2026-04-19).
  Centipede — negligible.
- **Gap**: No free public RTK for hobbyists. Pak-Rehber is restricted to
  authorized users; neither the endpoint nor an open registration path is
  publicly documented. Pakistan's large area (881,000 km²) and varied terrain
  (plains, Balochistan plateau, Himalayas/Karakoram) would require a dense
  network; coverage extent is unknown. Hobbyists must currently deploy a
  local base station or contact SUPARCO directly to explore access.

### NP — Nepal

- **Free government RTK**: none confirmed for public/hobbyist access. Nepal's
  Survey Department (Geodetic Survey Division, dos.gov.np) is actively
  building a CORS network: as of published reports (c. 2019–2022) it had
  established 4 CORS stations at Nagarkot, Minbhawan (Kathmandu), and 2
  additional sites, with a mandate to expand to 27–50 stations nationwide
  at ~70–80 km inter-station spacing. No public NTRIP caster, host:port,
  or open registration portal has been found; the network appears to serve
  geodetic reference frame maintenance rather than real-time public streaming.
  UNAVCO / EarthScope (now merged) hosts ~11 research CORS stations in Nepal
  (operated with Dept of Mines and Geology and Caltech; station IDs: JMLA,
  NPGJ, JMSM, BESI, CHLM, NAST, SYBC, SNDL, RMJT, BRNZ, plus 5 newer
  ones). GAGE/EarthScope real-time NTRIP streams for these stations require
  an account (email rtgps@unavco.org); research-use orientation, not
  designed for hobbyist rovers; tectonic monitoring purpose.
- **Volunteer**: rtk2go — 0 confirmed NP bases (bounding box 26–30°N,
  80–88°E returns no stations as of 2026-04-19). Centipede — negligible.
- **Gap**: No free public RTK for hobbyists. The Survey Department CORS
  rollout is ongoing but the endpoint is internal; UNAVCO research stations
  require account approval and are sparse (~70–100 km spacing — marginal for
  rover RTK). Nepal's terrain (Terai plains in the south, high Himalaya in
  the north) and limited internet infrastructure outside major urban centres
  further constrain practical NTRIP use. Hobbyists must deploy a local base
  station. Worth re-checking once the Survey Department CORS expansion is
  reported complete (no confirmed completion date as of 2026-04).

### AF — Afghanistan

- **Free government RTK**: none. AGCHO (Afghan Geodesy and Cartography Head
  Office), founded 1958, was the national cartographic authority. NOAA CORS
  records show two AGCHO-operated stations were registered: AFHT (Herat,
  decommissioned 2010) and AFKB (Kabul, decommissioned 2010–2011). These
  decommissioned stations predate any public NTRIP service. The Taliban
  takeover (August 2021) and the subsequent withdrawal of international
  development assistance have made any further infrastructure development
  highly unlikely; AGCHO's activities since 2021 are not documented in
  open sources. No public NTRIP endpoint has ever been discovered for
  Afghanistan.
- **Volunteer**: rtk2go — 0 confirmed AF bases (bounding box 29–38°N,
  60–75°E returns no stations as of 2026-04-19). Centipede — negligible.
- **Gap**: No RTK infrastructure accessible to hobbyists. The security
  environment, internet infrastructure gaps, and collapse of international
  geodetic cooperation since 2021 make a public NTRIP caster implausible
  in the near to medium term. GEODNET and global commercial services
  (Trimble, Hexagon) do not cover Afghanistan in their stated footprints.
  Local base station deployment is the only practical option.

### MM — Myanmar

- **Free government RTK**: none confirmed for public access. Myanmar's
  Survey Department (surveydepartment.gov.mm) is responsible for GPS
  control stations and is reported to have established a CORS network
  concept with a Yangon CORS Data Center. However, no public NTRIP
  host:port, open sourcetable, or registration portal has been found.
  The Settlement and Land Records Department (SLRD) procured 520
  CHC X91+ GNSS receivers for cadastral work, indicating operational
  RTK use, but this is internal government surveying, not a public
  NTRIP service. The February 2021 military coup and subsequent civil
  conflict have severely degraded civilian infrastructure and internet
  access across many regions; geospatial data is typically treated as
  sensitive under military governance.
- **Volunteer**: rtk2go — 0 confirmed MM bases (bounding box 9–28°N,
  92–101°E returns no stations as of 2026-04-19). Centipede — negligible.
- **Gap**: No free public RTK for hobbyists. The Survey Department CORS
  network may exist internally but is not publicly accessible. The 2021
  coup and ongoing conflict have further reduced the likelihood of a
  public service becoming available. Hobbyists must deploy a local base
  station; connectivity constraints in much of Myanmar make even that
  scenario difficult. No commercial NTRIP provider lists Myanmar coverage.

---

_Notes for integration:_

- All four entries belong in the existing `## Asia Pacific — South & SE Asia`
  section of `docs/country-survey.md`, inserted in alphabetical order by
  country code (AF before BD, MM between MY and PH, NP between MY and PH,
  PK between PH and TH — check the current order and slot accordingly).
- None of these countries warrants a `networks.md` entry at this time:
  no pipeline candidate or deferred endpoint was found. If SUPARCO
  publishes a public registration portal, a `pak_rehber` deferred entry
  would be appropriate.
- Volunteer counts in `data/stations.json` were verified by bounding-box
  query as of 2026-04-19; all four countries return 0 stations.
