# Agent intended Edit
- batch: usse
- target: D:\Projects\ntrip-mountpoint-map\docs\ntrip_research\US-SE_Southeast.md
- transcript line: 154

## OLD_STRING

```markdown
| **host:port** | `www.myfloridagps.com` / IP `40.121.5.206`; NTRIP port scheme via myfloridagps.com/links/2025products.pdf (port 10000 series for network RTK; port scheme not directly confirmed by probe — port 10000 timed out from this network on 2026-05-07) |
```

## NEW_STRING

```markdown
| **host:port** | `www.myfloridagps.com` / IP `48.223.232.215` (FAQ 2025); legacy IP `40.121.5.206` deprecated. Port `10000` for NAD83 Network Solutions (NTRIP); 11000-series ports for TCP/IP. `48.223.232.215:10000` returned `SOURCETABLE 200 OK` on 2026-05-07 (curl probe; Leica GNSS Spider 7.11.1.109 caster). |
```
