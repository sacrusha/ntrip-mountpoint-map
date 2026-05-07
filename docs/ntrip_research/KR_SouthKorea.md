# South Korea [KR] — NTRIP RTK Caster Research
**Date researched:** 2026-05-07

## Status: YES — free national NTRIP single-base caster operating (GNSS Data Center, `www.gnssdata.or.kr:2101`); aggregates ~173 physical stations across 8 contributing agencies. No national ID required for registration. Network RTK / VRS service is operated separately by NGII (`map.ngii.go.kr`); free for registered Korean residents but practical access for foreign individuals is unconfirmed.

| Field | Value |
|---|---|
| **Active public NTRIP RTK caster** | Yes — free of charge, free registration |
| **Network 1 — name** | GNSS Data Center / GNSS 데이터 통합관리센터 (national real-time RTCM aggregator) |
| **Operator — Network 1** | GNSS 데이터 통합관리센터 (GNSS Data Integration Management Center) — a federated portal aggregating real-time streams from 8 Korean GNSS reference-station operating agencies (the sourcetable shows agency tags `KORREF`, `Single Base`, `SMG` and several blank values — KORREF = NGII reference network, SMG = Seoul Metropolitan Government) |
| **host:port — Network 1** | `www.gnssdata.or.kr:2101` — confirmed live 2026-05-07: `SOURCETABLE 200 OK` from `NTRIP Caster 1.1`, **546 STR rows** spanning ~173 unique physical stations |
| **Mountpoint format** | `STATIONNAME-FORMAT` — e.g. `SUWN-RTCM31` (Suwon, RTCM 3.1), `ANHN-RTCM30`, `BHAO-RTCM32`. Each station typically published in 3–4 format variants (RTCM 2.3, RTCM 3.0, RTCM 3.1, RTCM 3.2; some BINEX) |
| **VRS — Network 1** | No — single-base raw RTCM observations only (rover computes RTK baseline). Constellations vary by station: most are GPS+GLONASS (RTCM 2.3/3.0/3.1) with newer KORREF entries adding multi-constellation MSM (RTCM 3.2). DGPS+RTK / "FROMSERVER" tags on KORREF mounts |
| **tariff — Network 1** | Free (no payment / no commercial tier) |
| **NTRIP credentials** | NTRIP **username** = the account email used for `gnssdata.or.kr` login; NTRIP **password** = the literal string `gnss` (per official RTCM page: *"비밀번호 : gnss (로그인 비밀번호 아님)"* — "Password: `gnss`, NOT the login password"). The portal login password and the NTRIP password are intentionally distinct |
| **hobbyist_eligibility — Network 1** | Yes — registration form (`/user/agree.do`) collects only *email + password*. Personal-information consent text confirms: *"개인정보 수집 항목 : 이메일, 비밀번호"* (collected items: email, password). **No national ID (주민등록번호), no Korean phone, no Korean address required.** A foreign hobbyist can register with any email |
| **legal_residency_required — Network 1** | No — registration form has no nationality, residency, or citizenship field. Portal is Korean-only (English subdomain `eng/main.do` returns ERROR page 2026-05-07) but the form structure is simple enough to navigate with browser translation |
| **Account auto-expiry** | 50 days inactivity → automatic account deletion (*"최종접속날짜 기준 50일 이상 미접속시 계정이 자동 삭제됨"*) — practical implication: log in at least every ~7 weeks |
| **last_confirmed_alive — Network 1** | 2026-05-07 — `www.gnssdata.or.kr:2101` returned 546-row `SOURCETABLE`; main portal `/main/getMainView.do` reachable; registration page `/user/agree.do` reachable |
| **Network 2 — name** | NGII Network RTK (VRS + FKP) |
| **Operator — Network 2** | NGII (National Geographic Information Institute / 국토지리정보원), Ministry of Land, Infrastructure and Transport |
| **host:port — Network 2** | `vrs3.ngii.go.kr:2101` (VRS) and `fkp.ngii.go.kr:2201` (FKP) — endpoints documented in academic papers and NGII notice (sq=77502, May 2022 address change). Live-tested response **not directly confirmed in this round**; physical stations of NGII (KORREF) are accessible as raw streams via Network 1 above |
| **VRS — Network 2** | Yes — VRS (Geo++ GNSMART) and FKP corrections; centimetre-level network solution from ~60 NGII stations at ~40 km spacing |
| **tariff — Network 2** | Free, but separate registration on the NGII unified portal (`ngii.go.kr/member/login.do`) and a service-application step on `map.ngii.go.kr` are required |
| **hobbyist_eligibility — Network 2** | Unclear — NGII unified registration historically uses Korean PASS / mobile identity verification (휴대폰 본인인증) which requires a Korean carrier and resident registration number. **Practical access for foreign individuals is restricted** even though no formal English-language exclusion exists |
| **legal_residency_required — Network 2** | Yes (effectively) — Korean phone-based identity verification gate at registration. Email-only registration like Network 1 is not offered |
| **last_confirmed_alive — Network 2** | Documented 2022-05-02 address-change notice (`sq=77502`) on ngii.go.kr; portal active 2026-05-06 per existing networks.md note. Direct sourcetable curl not attempted in this round (NGII VRS endpoint typically requires authenticated CONNECT) |

## Mountpoint Sample — GNSS Data Center (sourcetable 2026-05-07)

Sourcetable returns 546 STR rows across ~173 unique physical stations, each in 3–4 format variants. Selection:

| Station code | Region | Agency tag | Formats available | Coordinates |
|---|---|---|---|---|
| `ANHN` | Anheung (충남) | KORREF (NGII) | RTCM 2.3 / 3.0 / 3.2 | 36.67, 126.13 |
| `ANSG` | Ansan (경기) | Single Base | RTCM 2.3 / 3.1 | 37.01, 127.27 |
| `BHAO` | Bonghwa | Single Base (KASI) | RTCM 3.0 / 3.2 | 36.16, 128.97 |
| `BOEN` | Boeun | Single Base | BINEX / RTCM 2.3 / 3.0 / 3.2 | 36.49, 127.73 |
| `BSNG` | Boseong | Single Base | BINEX / RTCM 2.3 / 3.0 / 3.2 | 34.89, 127.13 |
| `CHJU` | Cheju (Jeju Island) | Single Base | (multi-format) | (Jeju) |
| `DAEJ` | Daejeon | Single Base | (multi-format) | (Daejeon) |
| `DBON` | Dobong (Seoul) | SMG | (multi-format) | 37.6, 127 (Seoul) |
| `GANS` | Gangseo (Seoul) | SMG | (multi-format) | 37.5, 126.9 (Seoul) |
| `SUWN` | Suwon | KORREF | RTCM 3.1 (`SUWN-RTCM31`), 3.2 | (Gyeonggi-do) |
| `DOKD` | Dokdo (Liancourt Rocks) | KORREF | (multi-format) | (East Sea) |

Source-tag breakdown across the 546 rows: 433 `Single Base`, 94 `KORREF` (NGII), 10 `SMG` (Seoul Metropolitan Government), plus 2 KORREF variants and 7 untagged. Approximate physical-station diversity: ~173 unique base codes.

## Service Details

### How to connect (Network 1, free)

1. Register at `https://www.gnssdata.or.kr/user/agree.do` — email + password only.
2. Confirm email (account auto-expires after 50 days inactivity).
3. NTRIP client setup:
   - **Caster Host**: `www.gnssdata.or.kr`
   - **Port**: `2101`
   - **User ID**: your portal login email
   - **Password**: literal `gnss` (NOT your portal password — distinct by design)
   - **Mountpoint**: `STATIONNAME-FORMAT` (e.g. `SUWN-RTCM31`, `BHAO-RTCM32`)
4. Apply for the real-time service via `/rtcm/getRtcmView.do` after logging in (one-click "Apply"/"Cancel" toggle).

### How to connect (Network 2, NGII Network RTK)

1. Register at `https://www.ngii.go.kr/member/login.do` — Korean PASS / mobile identity verification gate (foreign-resident-friendly path is not publicly documented).
2. Apply for the Network RTK service at `map.ngii.go.kr` (separate from the unified member registration).
3. NTRIP client setup:
   - VRS: `vrs3.ngii.go.kr:2101` (decommissioned old `vrs.ngii.go.kr`)
   - FKP: `fkp.ngii.go.kr:2201`
   - Credentials issued per account.

## Context Notes

- **Network 1 is the practical hobbyist endpoint**: 173 single-base stations across 8 agencies, no Korean ID barrier, free, single shared NTRIP password (`gnss`). Foreign users can sign up with any email. ~40 km nationwide spacing makes single-base RTK practical for most of South Korea.
- **Network 2 (NGII VRS/FKP) is the cm-level network-solution tier**, but Korean residency is effectively required for registration via PASS/mobile-ID. The same physical stations (94 KORREF) are exposed in raw form through Network 1 — so a foreign user gets nearly equivalent functional coverage by computing the RTK baseline at the rover.
- **Seoul Metropolitan Government (SMG)** contributes 10 streams covering the Seoul metropolitan area (DBON Dobong, GANS Gangseo, etc.) into Network 1 — additional density for the capital region. A separate Seoul-city portal at `gnss.eseoul.go.kr/system_sub2_03` exists for VRS/FKP service applications.
- **Constellations**: KORREF newer mounts (RTCM 3.2) generally output GPS+GLONASS+Galileo+BeiDou; older RTCM 2.3 / 3.0 mounts are GPS+GLONASS only. BINEX is offered on a few stations for high-rate research use.
- **Pipeline coverage** (stations.json 2026-05-06 fetch): KR = 493 cors_korea + 3 rtk2go entries. The cors_korea pipeline source corresponds to `www.gnssdata.or.kr:2101` (Network 1).
- **Maritime DGPS (NMPNT)**: The Ministry of Oceans and Fisheries operates a separate maritime NTRIP service at `nmpnt.go.kr` for DGPS corrections (sub-metre, not RTK). Out of scope for this RTK research per the project's "DGNSS out of scope" rule.
- **ardusimple.com KR guide** (observed 2026-05-07): mentions NGII's `map.ngii.go.kr/ms/svcIntrcn/gnss/baseInfo.do` (which 400-errors today) and recommends the separate community option of GNSS Data Center / `gnssdata.or.kr` was not previously highlighted as the easier free path.

## Post-Processing (RINEX) Fallback

| Service | URL | Cost |
|---|---|---|
| **GNSS Data Center RINEX archive** | https://www.gnssdata.or.kr/board/getDataView.do (자료실) | Free (account) |
| **NGII CORS RINEX** | https://map.ngii.go.kr/ms/mesrInfo/gnss/vrsUserView.do | Free (NGII unified account) |
| **EUREF / IGS — DAEJ, SUWN** | https://www.epncb.oma.be/_networkdata/siteinfo4onestation.php?station=DAEJ00KOR | Free |

## Sources Consulted

- GNSS Data Center main portal: https://www.gnssdata.or.kr/main/getMainView.do (Korean; observed 2026-05-07)
- GNSS Data Center registration: https://www.gnssdata.or.kr/user/agree.do (collects email + password only; 50-day auto-expiry confirmed)
- GNSS Data Center real-time RTCM page: https://www.gnssdata.or.kr/rtcm/getRtcmView.do (host/port/credential format documented; password literal `gnss` is the official setting)
- Live caster sourcetable: `curl http://www.gnssdata.or.kr:2101/` → `SOURCETABLE 200 OK Server: NTRIP Caster 1.1` (546 STR rows, ~173 unique stations, 2026-05-07)
- ArduPilot Discourse thread on `gnssdata.or.kr` login: https://discuss.ardupilot.org/t/rtk-service-login-error-issue-for-ntrip-protocol-in-mission-planner/120162 (third-party confirmation of email-as-username + literal `gnss` password format)
- NGII Network RTK service page (404 today): https://www.ngii.go.kr/eng/contents/contentsView.do?rbsIdx=174
- NGII member login: https://www.ngii.go.kr/member/login.do
- NGII service-address-change notice (May 2022): https://www.ngii.go.kr/kor/board/view.do?sq=77502
- IGS Workshop 2017 paper — GNSS CORS and Network-RTK in Korea: https://files.igs.org/pub/resource/pubs/workshop/2017/W2017-PS06-06%20-%20Kim.pdf (NGII context, ~60 stations at ~40 km, GNSMART/Pivot software)
- ArduSimple South Korea: https://www.ardusimple.com/rtk-correction-services-and-ntrip-casters-in-south-korea/
- Seoul GNSS portal: https://gnss.eseoul.go.kr/system_sub2_03
- Maritime PNT Office (DGPS, out of scope): https://www.nmpnt.go.kr/html/en/dgnss/dgnss_0303.html
- Existing networks.md `cors_korea` entry: `www.gnssdata.or.kr:2101`, ~498 stations, physical-coord VRS, sourcetable public
- Stations.json 2026-05-06 fetch: KR = 493 cors_korea + 3 rtk2go entries
