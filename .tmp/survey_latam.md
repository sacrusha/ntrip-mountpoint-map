# Free RTK NTRIP — Latin America survey additions: Venezuela and Uruguay

_Research date: 2026-04-21. Entries follow the format and scope of
`docs/country-survey.md` and are ready to paste into the
"Americas — Latin" section._

---

### VE — Venezuela

- **Free government RTK**: REMOS (IGVSB — Instituto Geográfico de Venezuela
  Simón Bolívar). 29 permanent stations installed nationally, 27 with NTRIP
  capability; Maracaibo (MARA) became the first to transmit corrections via
  NTRIP experimentally from Oct 2008. NTRIP caster endpoint **not publicly
  confirmed**: igvsb.gob.ve lists geodetic services but no public-facing
  host:port or registration portal has been found in indexed sources as of
  2026-04. The REMOS NTRIP service appears to have been limited in practice
  (only MARA streaming, with plans for the remainder — status of those plans
  is unclear post-2018). IGVSB is under the Ministry of Environment; economic
  and infrastructure constraints have historically slowed deployment.
- **Volunteer**: rtk2go — 0 confirmed mainland VE bases (3 rtk2go bases
  visible at coordinates 12°N, 68–69°W are on Curaçao/Aruba — Netherlands
  Antilles, not Venezuelan territory). EarthScope NOTA has ~4 stations in
  the southern Caribbean / northern Venezuela area (CN-series), but those
  are on Caribbean islands, not the Venezuelan mainland.
- **Gap**: No confirmed free public NTRIP caster for mainland Venezuela.
  IGVSB/REMOS infrastructure exists on paper (29 stations, NTRIP-capable)
  but the caster endpoint is not publicly discoverable, and operational
  continuity is uncertain given Venezuela's infrastructure situation. hobbyists
  have no confirmed free RTK path on the mainland. GEODNET's South America
  server (`sa.geodnet.com:2101`, paid $40/month) is the nearest practical
  paid fallback.

### UY — Uruguay

- **Free government RTK**: REGNA-ROU (IGM — Instituto Geográfico Militar,
  `rtk.igm.gub.uy:2101`, ~26 stations, single-base + VRS) — confirmed free
  ("El Servicio no tiene costo"); web registration at
  `rtk.igm.gub.uy/SBC/Account/Register`. VRS capable (1–2 cm horizontal
  with dual-frequency equipment). Network expanded to 8 additional
  COMNAV SinoGNSS M300 Pro CORS as of Dec 2025, densifying coverage.
  Reference frame SIRGAS-ROU (ITRF-compatible). 1,000+ registered users.
  → networks.md: `regna_rou` (candidate)
- **Volunteer**: rtk2go — ~2 UY bases (RAMSAC Argentina stations near the
  border appear in the Uruguay bounding box; no dedicated UY volunteer
  streams confirmed on rtk2go). Centipede — negligible.
- **Gap**: REGNA-ROU provides free national coverage; the main friction is
  a registration step and a Spanish-language portal. No confirmed NTRIP
  host:port beyond `rtk.igm.gub.uy:2101` (standard port, confirmed in
  IGM service documentation). Candidate for pipeline ingestion once
  sourcetable accessibility is verified.

---

## networks.md candidate entry

### regna_rou — REGNA-ROU (UY)

**status**:    candidate
**host:port**: `rtk.igm.gub.uy:2101`
**type**:      single-base (point-to-point from chosen physical station);
               VRS also available (1–2 cm; dual-frequency required)
**access**:    free; register at rtk.igm.gub.uy/SBC/Account/Register
**stations**:  ~26 (recently expanded; 8 new SinoGNSS M300 Pro CORS added Dec 2025)
**source**:    igm.gub.uy (IGM — Instituto Geográfico Militar); SIRGAS bulletin Bol22

Operated by Uruguay's Instituto Geográfico Militar. REGNA-ROU (Red Geodésica
Nacional Activa de la República Oriental del Uruguay) has been providing free
NTRIP corrections since ~2012. Reference frame SIRGAS-ROU (ITRF-compatible).
Service page at igm.gub.uy confirms "El Servicio no tiene costo". Caster
software is SBC (Spider Business Centre or equivalent); registration URL
follows the same pattern as several other LatAm IGM instances. Over 1,000
registered users reported. Network was expanded Dec 2025 with 8 additional
multiconstellation CORS.

**missing**: verify sourcetable is publicly readable without credentials at
`rtk.igm.gub.uy:2101` (try NTRIP GET / on port 2101); confirm current station
count from sourcetable; check mountpoint types (single-base vs VRS designation).

---

## networks.md entry for Venezuela (no-endpoint record)

### remos_ven — REMOS (VE)

**status**:    deferred
**host:port**: not publicly found
**type**:      single-base (historically; only MARA station confirmed streaming)
**access**:    intended free per IGVSB mandate; no public registration portal found
**stations**:  29 installed nationally (27 with NTRIP hardware per ~2012–2018 sources);
               operational streaming count unknown
**source**:    igvsb.gob.ve (IGVSB — Instituto Geográfico de Venezuela Simón Bolívar);
               SIRGAS bulletins (Bol14, Bol15); Scielo VE article 2009

Red de Estaciones de Monitoreo Satelital (REMOS). IGVSB's national GNSS monitoring
network. MARA (Maracaibo) station joined IGS NTRIP stream Oct 2008 and served as the
experimental free NTRIP anchor. IGVSB stated intent to activate remaining 26 NTRIP-
capable stations; no evidence this was completed. No public caster host:port found in
current indexed sources (igvsb.gob.ve returns only general geodesy page). Venezuela's
infrastructure and economic situation since ~2015 makes operational continuity uncertain.
Do not add to pipeline without confirmed endpoint and recent (2024+) operational evidence.

**missing**: confirm caster host:port and current operational status — search
igvsb.gob.ve directly; contact geodesia@igvsb.gob.ve; check SIRGAS station list
for active Venezuelan NTRIP streams; verify at least one mountpoint is publicly
accessible before ingesting.
