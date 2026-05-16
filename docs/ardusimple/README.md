# ardusimple mirror

Per-country RTK/NTRIP research files mirrored from ardusimple.com's country pages.
Source sitemap: https://www.ardusimple.com/page-sitemap.xml (99 country pages discovered).

**Progress: 38 / 99 done** (as of 2026-05-16)

## Files

| File | Country | National network(s) | Cost |
|------|---------|---------------------|------|
| AD_Andorra.md | Andorra | ERGAND | free |
| AL_Albania.md | Albania | ALBPOS/ASIG | free (404) |
| AR_Argentina.md | Argentina | RAMSAC/IGN | free |
| AT_Austria.md | Austria | APOS/BEV | paid |
| AU_Australia.md | Australia | AUSCORS/Geoscience Australia; CORSnet-NSW (regional) | free; paid |
| BA_Bosnia-Herzegovina.md | Bosnia & Herzegovina | FBiHPOS | paid |
| BD_Bangladesh.md | Bangladesh | Survey of Bangladesh | paid |
| BR_Brazil.md | Brazil | RBMC/IBGE | free |
| CR_CostaRica.md | Costa Rica | SNIT | free |
| CY_Cyprus.md | Cyprus | CYPOS/DLS | paid |
| CZ_CzechRepublic.md | Czech Republic | CZEPOS/ČÚZK | free |
| GR_Greece.md | Greece | HEPOS/Hellenic Cadastre | paid |
| HR_Croatia.md | Croatia | CROPOS | paid |
| HU_Hungary.md | Hungary | GNSSNet | paid |
| IL_Israel.md | Israel | Israel Mapping Center CORS | paid |
| IN_India.md | India | Survey of India CORS | paid |
| IT_Italy2.md | Italy | Geodaf/ASI; SPIN3 GNSS; FReDNet/OGS | free |
| KE_Kenya.md | Kenya | Muya CORS | paid |
| LK_SriLanka.md | Sri Lanka | SLCORSNET/Survey Dept | paid |
| MD_Moldova.md | Moldova | MOLDPOS | paid (404) |
| MK_Macedonia.md | North Macedonia | MAKPOS | paid |
| MY_Malaysia.md | Malaysia | MyRTKnet/JUPEM | paid |
| MX_Mexico.md | Mexico | RGNA/INEGI | free (post-processing) |
| NO_Norway.md | Norway | CPOS/Kartverket | paid (free for research) |
| PH_Philippines.md | Philippines | PAGeNet/NAMRIA | paid |
| RO_Romania.md | Romania | ROMPOS | paid |
| RS_Serbia.md | Serbia | AGROS/RGZ | paid |
| SE_Sweden.md | Sweden | SWEPOS/Lantmäteriet | paid |
| SG_Singapore.md | Singapore | SiReNT/SLA | paid |
| SI_Slovenia.md | Slovenia | SIGNAL | paid |
| SK_Slovakia.md | Slovakia | SKPOS/GKU | paid |
| CH_Switzerland.md | Switzerland | SWIPOS/Swisstopo | paid |
| TN_Tunisia.md | Tunisia | OTC | paid |
| TR_Turkey.md | Turkey | TUSAGA-AKTIF | paid |
| TW_Taiwan.md | Taiwan | EGNSS/NLSC | paid |
| VN_Vietnam.md | Vietnam | VNGEONET | paid |
| XK_Kosovo.md | Kosovo | KOPOS | paid |
| MX_Mexico.md | Mexico | RGNA/INEGI | free (post-processing) |

## Reachability notes

- EUREF (epncb.oma.be) consistently returns HTTP 000 in this environment — TLS/connection issue; classified as `unverified`.
- Several government NTRIP portals (ibge.gov.br Brazil, cuzk.gov.cz Czech Republic access page, agros.rgz.gov.rs Serbia, skpos.gku.sk Slovakia, makpos.katastar.gov.mk Macedonia, vngeonet.vn Vietnam, jupem.gov.my Malaysia, cors.imd.gov.in India) return HTTP 000 — classified as `unverified — HTTP 000 / DNS fail`.
- MOLDPOS Moldova and ALBPOS Albania: 404 not-found.
- SiReNT Singapore: 502 server-error.
- APOS Austria and HEPOS Greece: 403 auth-required.

## Global networks (appear on most pages)

- **RTK2GO** — rtk2go.com:2101 — free community caster
- **IGS** — network.igs.org — free, low density, high quality
- **Earthscope/UNAVCO** — free for non-commercial use
- **EUREF** — epncb.oma.be:2101 — free, European reference frame
- **CENTIPEDE** — caster.centipede.fr:2101 — free, mostly France/Europe
- **u-blox PointPerfect Flex** — paid, ~$5.90/month, free 30-day trial
- **Swift Navigation Skylark** — paid, $29–69/month, free 6-month trial
