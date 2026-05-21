#!/usr/bin/env python3
"""Per-station coord sanity check using ISO3 country bounding boxes.

Two reports, both driven from `data/stations.json` (with each station's
country tag from the sourcetable) against a hard-coded BBOX table here:

  sign     -- candidates for `data/coord_overrides.json`: declared coord
              falls outside the country bbox, but exactly one sign-flip
              (lat / lon / both) lands inside. Already-overridden entries
              are excluded.
  country  -- mistag report: declared coord doesn't fit the declared
              country and no sign-flip rescues it; lists which country
              bboxes WOULD fit. Mostly operator-side data quality
              (centipede default-tags many foreign stations as FRA).

Usage:
    py scripts/coord_check.py            # both reports
    py scripts/coord_check.py sign       # sign-flip candidates only
    py scripts/coord_check.py country    # country-tag mismatches only
    py scripts/coord_check.py -h

Not pipeline-wired. Run after a fresh fetch to surface anything new for
manual triage; promote confirmed fixes into `data/coord_overrides.json`.

BBOX coverage is partial (~180 ISO3 codes, generously padded). Long-tail
country codes show up under `unboxed` in the summary -- extend the table
here if a network's stations are silently skipped.

Related tools (in this directory):
    palette_check.py         color-assignments / PALETTE contract check
    stations_inspect.py      data/stations.json schema + per-source summary
    stations_by_country.py   list stations for an ISO3 across all sources
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATIONS = ROOT / "data" / "stations.json"
OVERRIDES = ROOT / "data" / "coord_overrides.json"

# Aliases from non-ISO tags to ISO3.
#   Centipede customs: CHZ=CHE (Switzerland, NOT Czechia), ENG=GBR,
#     SER=SRB, DAN=DNK, ROM=ROU.
#   Alpha-2 fallback for sources that emit a2 instead of a3.
ALIASES = {
    "CHZ":"CHE","ENG":"GBR","SER":"SRB","DAN":"DNK","ROM":"ROU",
    "CA":"CAN","US":"USA","AU":"AUS","NZ":"NZL","DE":"DEU","FR":"FRA","ES":"ESP",
    "BE":"BEL","NL":"NLD","AT":"AUT","CH":"CHE","PT":"PRT","PL":"POL","RO":"ROU",
    "HR":"HRV","SI":"SVN","SK":"SVK","EE":"EST","LV":"LVA","LT":"LTU","LU":"LUX",
    "SE":"SWE","NO":"NOR","FI":"FIN","DK":"DNK","IE":"IRL","GB":"GBR","TR":"TUR",
    "GR":"GRC","BG":"BGR","JP":"JPN","KR":"KOR","CN":"CHN","HK":"HKG","TH":"THA",
    "ID":"IDN","MY":"MYS","SG":"SGP","PH":"PHL","VN":"VNM","IN":"IND","SA":"SAU",
    "AE":"ARE","IL":"ISR","ZA":"ZAF","BR":"BRA","AR":"ARG","CL":"CHL","PE":"PER",
    "EC":"ECU","MX":"MEX","IT":"ITA","CO":"COL","UY":"URY","UG":"UGA",
}

# (min_lat, max_lat, min_lon, max_lon). Padded ~0.5 deg.
# Wide bboxes preferred -- false negatives (missing a real sign error)
# are cheap; false positives (flagging a correct station) cost trust.
BBOX = {
    "USA":(17.5, 72.0,-180.0,-65.0),  # incl. Alaska wraps to dateline
    "AUS":(-45.0,-9.0, 112.0, 160.0),
    "FRA":(41.0, 52.0, -5.5, 10.0),   # mainland + Corsica
    "KOR":(33.0, 39.5, 124.0, 132.5),
    "HUN":(45.5, 49.0, 16.0, 23.0),
    "ARG":(-56.0,-21.0,-74.0,-52.5),
    "BRA":(-34.0, 6.0,-75.0,-34.0),
    "ESP":(27.0, 44.5,-19.0, 5.0),    # incl. Canary
    "NZL":(-48.0,-33.0, 165.0, 180.0),  # plus Chatham trans-dateline (EXTRA_BOXES)
    "FIN":(59.0, 71.0, 19.0, 32.0),
    "CAN":(41.0, 84.0,-141.5,-52.0),
    "ITA":(35.0, 47.5, 6.0, 19.0),
    "NLD":(50.0, 54.0, 3.0, 7.5),
    "JPN":(20.0, 46.5, 122.0, 154.0),
    "ZAF":(-35.5,-22.0, 16.0, 33.5),
    "DEU":(47.0, 55.5, 5.0, 15.5),
    "GBR":(49.5, 61.0,-9.0, 2.5),
    "PRT":(30.0, 43.0,-32.0,-6.0),    # incl. Azores+Madeira
    "POL":(49.0, 55.0, 14.0, 24.5),
    "NOR":(57.5, 81.5, 4.0, 32.0),    # incl. Svalbard
    "SWE":(55.0, 69.5, 10.0, 25.0),
    "MNG":(41.0, 52.5, 87.0, 120.0),
    "CZE":(48.0, 51.5, 12.0, 19.0),
    "BEL":(49.0, 52.0, 2.0, 7.0),
    "SRB":(41.5, 47.0, 18.5, 23.5),
    "HKG":(22.0, 23.0, 113.5, 114.5),
    "AUT":(46.0, 49.5, 9.0, 17.5),
    "DNK":(54.0, 58.0, 8.0, 15.5),
    "CHE":(45.5, 48.0, 5.5, 11.0),
    "CRI":(8.0, 11.5,-86.0,-82.0),
    "MEX":(14.0, 33.0,-118.5,-86.0),
    "ATA":(-90.0,-60.0,-180.0, 180.0),
    "IRL":(51.0, 55.5,-11.0,-5.0),
    "ISL":(63.0, 67.0,-25.0,-13.0),
    "THA":(5.0, 21.0, 97.0, 106.0),
    "DOM":(17.0, 20.5,-73.0,-67.5),
    "ROU":(43.0, 48.5, 20.0, 30.0),
    "IDN":(-11.5, 6.5, 94.5, 141.5),
    "PYF":(-28.0,-7.0,-160.0,-134.0),
    "BGR":(41.0, 45.0, 22.0, 29.0),
    "NCL":(-23.0,-19.0, 163.0, 168.5),
    "BES":(12.0, 18.0,-69.0,-62.0),
    "SVK":(47.5, 50.0, 16.0, 23.0),
    "GRC":(34.5, 42.0, 19.0, 30.0),
    "CHN":(17.5, 54.5, 73.0, 135.5),
    "SVN":(45.0, 47.5, 13.0, 17.0),
    "CHL":(-57.0,-17.0,-110.0,-66.0),
    "EST":(57.0, 60.0, 21.0, 28.5),
    "TUR":(35.5, 43.0, 25.0, 45.0),
    "LVA":(55.0, 58.5, 20.0, 28.5),
    "IND":(6.0, 36.5, 68.0, 98.0),
    "PHL":(4.0, 21.5, 116.0, 127.0),
    "REU":(-22.0,-20.0, 55.0, 56.0),
    "UKR":(44.0, 53.0, 22.0, 41.0),
    "PER":(-19.0, 0.5,-82.0,-68.0),
    "ATF":(-50.0,-37.0, 50.0, 78.0),
    "ECU":(-5.5, 2.5,-92.5,-75.0),
    "SGP":(1.0, 2.0, 103.0, 105.0),
    "PAN":(7.0, 10.0,-83.5,-77.0),
    "MSR":(16.0, 17.0,-63.0,-62.0),
    "CYP":(34.5, 36.0, 32.0, 35.0),
    "FJI":(-22.0,-12.0, 174.0, 180.0),
    "MTQ":(14.0, 15.0,-62.0,-60.0),
    "FSM":(0.0, 10.5, 138.0, 164.0),
    "SYC":(-10.5,-3.0, 45.0, 56.0),
    "CUW":(12.0, 13.0,-69.5,-68.5),
    "RWA":(-3.0,-1.0, 28.0, 31.0),
    "HND":(12.0, 17.5,-90.0,-83.0),
    "MDG":(-26.0,-11.0, 43.0, 51.0),
    "ARE":(22.0, 26.5, 51.0, 56.5),
    "COL":(-5.0, 14.0,-80.0,-66.0),
    "ISR":(29.0, 33.5, 34.0, 36.0),
    "CPV":(14.0, 18.0,-26.0,-22.0),
    "SEN":(12.0, 17.0,-18.0,-11.0),
    "GUF":(2.0, 6.0,-55.0,-51.0),     # French Guiana
    "GLP":(15.0, 17.0,-62.5,-60.5),   # Guadeloupe
    "MAF":(18.0, 18.5,-63.5,-62.5),
    "VEN":(0.5, 12.5,-74.0,-59.0),
    "JAM":(17.0, 19.0,-79.0,-76.0),
    "BMU":(32.0, 33.0,-65.0,-64.0),
    "GRL":(59.0, 84.0,-74.0,-11.0),
    "RUS":(41.0, 82.0, 19.0, 180.0),  # crosses dateline; no auto sign-flip for lon
    "BLR":(51.0, 57.0, 23.0, 33.0),
    "KAZ":(40.0, 56.0, 46.0, 88.0),
    "UZB":(37.0, 46.0, 55.0, 73.5),
    "GEO":(41.0, 44.0, 39.0, 47.0),
    "ARM":(38.5, 41.5, 43.0, 47.0),
    "AZE":(38.0, 42.0, 44.0, 51.0),
    "VNM":(8.0, 24.0, 102.0, 110.0),
    "MYS":(0.5, 8.0, 99.0, 120.0),
    "LAO":(13.5, 22.5, 100.0, 108.0),
    "LKA":(5.5, 10.0, 79.5, 82.0),
    "NPL":(26.0, 31.0, 80.0, 89.0),
    "PAK":(23.0, 38.0, 60.0, 78.0),
    "BGD":(20.0, 27.0, 88.0, 93.0),
    "OMN":(16.0, 27.0, 51.0, 60.0),
    "JOR":(29.0, 34.0, 34.0, 40.0),
    "SAU":(15.5, 33.0, 34.0, 56.0),
    "QAT":(24.0, 27.0, 50.0, 52.0),
    "KWT":(28.0, 31.0, 46.0, 49.0),
    "BHR":(25.5, 26.5, 50.0, 51.0),
    "EGY":(21.5, 32.0, 24.0, 37.0),
    "MAR":(21.0, 36.5,-17.5,-1.0),
    "DZA":(18.0, 38.0,-9.0, 12.0),
    "TUN":(30.0, 38.0, 7.0, 12.0),
    "LBY":(19.0, 34.0, 9.0, 25.5),
    "NGA":(4.0, 14.0, 2.5, 15.0),
    "GHA":(4.5, 11.5,-3.5, 1.5),
    "TGO":(6.0, 11.5, 0.0, 1.8),
    "BEN":(6.0, 12.5, 0.7, 4.0),
    "BFA":(9.0, 15.5,-5.5, 2.5),
    "MLI":(10.0, 25.0,-12.5, 4.5),
    "NER":(11.5, 23.5, 0.0, 16.0),
    "TCD":(7.5, 24.0, 13.0, 24.0),
    "CMR":(2.0, 13.0, 8.5, 16.5),
    "GAB":(-4.0, 2.5, 8.5, 14.5),
    "COD":(-14.0, 5.5, 12.0, 31.5),
    "COG":(-5.5, 4.0, 11.0, 19.0),
    "KEN":(-4.7, 5.0, 33.5, 42.0),
    "TZA":(-12.0,-0.5, 29.0, 41.0),
    "UGA":(-1.5, 4.5, 29.5, 35.5),
    "ETH":(3.0, 15.0, 32.5, 48.0),
    "SOM":(-2.0, 12.0, 40.0, 52.0),
    "ZMB":(-18.5,-8.0, 21.5, 34.0),
    "ZWE":(-23.0,-15.5, 25.0, 33.5),
    "MWI":(-17.5,-9.0, 32.5, 36.0),
    "BWA":(-27.0,-17.5, 19.5, 29.5),
    "NAM":(-29.5,-16.5, 11.5, 25.5),
    "MOZ":(-27.0,-10.0, 30.0, 41.0),
    "MUS":(-21.0,-19.5, 57.0, 64.0),
    "ALB":(39.5, 43.0, 19.0, 21.5),
    "MKD":(40.5, 42.5, 20.0, 23.5),
    "BIH":(42.5, 45.5, 15.5, 20.0),
    "MNE":(41.5, 43.5, 18.0, 20.5),
    "KOS":(41.5, 43.5, 20.0, 22.0),
    "MDA":(45.0, 49.0, 26.0, 30.5),
    "LTU":(53.5, 56.5, 20.5, 27.0),
    "FRO":(61.0, 62.5,-7.5,-6.0),
    "MLT":(35.5, 36.5, 14.0, 15.0),
    "URY":(-35.0,-30.0,-59.0,-53.0),
    "PRY":(-28.0,-19.0,-63.0,-54.0),
    "BOL":(-23.0,-9.5,-69.5,-57.5),
    "GUY":(1.0, 9.0,-62.0,-56.0),
    "SUR":(1.5, 6.0,-58.5,-53.5),
    "TTO":(10.0, 12.0,-62.0,-60.0),
    "BRB":(13.0, 13.5,-60.0,-59.0),
    "ATG":(17.0, 18.0,-62.5,-61.5),
    "BLZ":(15.5, 18.5,-89.5,-87.5),
    "GTM":(13.5, 18.0,-92.5,-88.0),
    "NIC":(10.5, 15.5,-87.5,-82.5),
    "SLV":(13.0, 15.0,-90.5,-87.5),
    "BHS":(22.5, 27.5,-79.5,-72.5),
    "CYM":(19.0, 20.0,-82.0,-79.0),
    "TCA":(21.0, 22.0,-72.5,-71.0),
    "ABW":(12.0, 12.7,-70.5,-69.5),
    "PRI":(17.5, 18.7,-67.5,-65.0),
    "VIR":(17.5, 18.5,-65.5,-64.5),
    "VGB":(18.0, 19.0,-65.0,-64.0),
    "AIA":(18.0, 18.5,-63.5,-62.5),
    "KNA":(17.0, 17.5,-63.0,-62.0),
    "DMA":(15.0, 16.0,-61.5,-61.0),
    "LCA":(13.5, 14.5,-61.5,-60.5),
    "VCT":(12.5, 13.5,-61.5,-61.0),
    "GRD":(11.5, 12.5,-62.0,-61.0),
    "HTI":(17.5, 20.5,-74.5,-71.5),
    # KIR (Kiribati): dateline-crosser, skip auto-fix
    "VUT":(-21.0,-13.0, 166.0, 171.0),
    "TON":(-23.0,-15.0,-176.0,-173.0),
    "WSM":(-15.0,-13.0,-173.0,-171.0),
    "ASM":(-15.0,-14.0,-171.5,-169.0),
    "GUM":(13.0, 14.0, 144.0, 145.5),
    "MNP":(14.0, 21.0, 144.0, 146.5),
    "MHL":(4.0, 15.0, 160.0, 173.0),
    "PLW":(2.5, 8.5, 131.0, 135.0),
    "SLB":(-12.0,-5.0, 155.0, 170.0),
    "TUV":(-10.0,-5.0, 175.0, 180.0),
    "NIU":(-20.0,-18.0,-170.5,-169.0),
    "COK":(-22.0,-9.0,-166.0,-157.0),
    "PNG":(-12.0,-1.0, 140.0, 156.0),
    "TLS":(-10.0,-8.0, 124.0, 127.5),
    "BRN":(4.0, 5.5, 114.0, 115.5),
    "KHM":(10.0, 15.0, 102.5, 108.0),
    "MMR":(9.5, 28.5, 92.0, 102.0),
    "AFG":(29.0, 39.0, 60.0, 75.0),
    "BTN":(26.5, 28.5, 88.5, 92.5),
    "MDV":(-1.0, 8.0, 72.5, 74.0),
    "YEM":(12.0, 19.0, 42.5, 54.5),
    "IRN":(25.0, 40.0, 44.0, 64.0),
    "IRQ":(29.0, 38.0, 38.0, 49.0),
    "LBN":(33.0, 35.0, 35.0, 37.0),
    "SYR":(32.0, 37.5, 35.5, 42.5),
    "LSO":(-31.0,-28.0, 27.0, 29.5),
    "SWZ":(-27.5,-25.5, 30.5, 32.5),
    "DJI":(10.5, 13.0, 41.5, 43.5),
    "ERI":(12.5, 18.0, 36.5, 43.5),
    "SSD":(3.0, 13.0, 24.0, 36.0),
    "SDN":(8.5, 23.5, 21.5, 39.0),
    "AGO":(-19.0,-4.0, 11.5, 24.5),
    "MRT":(14.5, 28.0,-17.5,-4.5),
    "GMB":(13.0, 14.0,-17.0,-13.5),
    "GIN":(7.0, 13.0,-15.5,-7.5),
    "GNB":(10.5, 13.0,-17.0,-13.5),
    "LBR":(4.0, 9.0,-12.0,-7.0),
    "SLE":(6.5, 10.0,-13.5,-10.0),
    "CIV":(4.0, 11.0,-9.0,-2.5),
    "CAF":(2.0, 11.5, 14.0, 28.0),
    "STP":(-0.5, 2.0, 6.0, 8.0),
    "GNQ":(0.5, 4.0, 5.5, 12.0),
    "BDI":(-5.0,-2.0, 28.5, 31.0),
    "COM":(-13.0,-11.0, 43.0, 45.5),
    "SHN":(-17.0,-7.5,-15.0,-5.5),    # incl. Ascension
}

# Secondary rectangles for countries that span the antimeridian or
# otherwise need a disjoint extra box.
EXTRA_BOXES = {
    "NZL":[(-45.0,-43.0,-178.5,-175.5)],  # Chatham Islands east of dateline
}


def alias_iso3(code: str) -> str:
    c = (code or "").strip().upper()
    return ALIASES.get(c, c) if len(c) <= 3 else c


def inside_any(boxes, lat, lon) -> bool:
    for mn_la, mx_la, mn_lo, mx_lo in boxes:
        if mn_la <= lat <= mx_la and mn_lo <= lon <= mx_lo:
            return True
    return False


def country_boxes(iso3):
    primary = BBOX.get(iso3)
    if not primary:
        return None
    return [primary] + EXTRA_BOXES.get(iso3, [])


def load_overrides() -> set:
    """Return set of (mountpoint, bad_lat, bad_lon) already in
    coord_overrides.json so the sign report doesn't re-suggest fixes
    already wired."""
    if not OVERRIDES.exists():
        return set()
    try:
        raw = json.loads(OVERRIDES.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return set()
    return {(e["mountpoint"], e["bad"]["lat"], e["bad"]["lon"])
            for e in raw.get("overrides", [])}


def sign_report(stations_data: dict) -> int:
    """List sign-flip candidates not already covered by coord_overrides.json.
    Returns count of unique suggestions."""
    already = load_overrides()
    fixable, ambiguous = [], []
    for sid, src in stations_data["sources"].items():
        for st in src["stations"]:
            la, lo = st.get("lat"), st.get("lon")
            if la is None or lo is None:
                continue
            iso3 = alias_iso3(st.get("country"))
            boxes = country_boxes(iso3) if iso3 else None
            if not boxes or inside_any(boxes, la, lo):
                continue
            matches = []
            for fl_la, fl_lo in ((-1, 1), (1, -1), (-1, -1)):
                cla, clo = fl_la * la, fl_lo * lo
                if inside_any(boxes, cla, clo):
                    flip = ("lat" if (fl_la, fl_lo) == (-1, 1)
                            else "lon" if (fl_la, fl_lo) == (1, -1) else "both")
                    matches.append((flip, cla, clo))
            if (st["name"], la, lo) in already:
                continue  # already wired
            if len(matches) == 1:
                fixable.append((sid, st["name"], iso3, la, lo, *matches[0]))
            elif len(matches) > 1:
                ambiguous.append((sid, st["name"], iso3, la, lo, matches))

    print("=== SIGN-FLIP CANDIDATES ===")
    print(f"{len(fixable)} fixable (single unambiguous flip), "
          f"{len(ambiguous)} ambiguous, {len(already)} already in coord_overrides.json")
    if fixable:
        by_src = defaultdict(list)
        for r in fixable:
            by_src[r[0]].append(r)
        for sid, rows in sorted(by_src.items(), key=lambda kv: -len(kv[1])):
            print(f"\n-- {sid}: {len(rows)}")
            for _, name, iso3, la, lo, flip, nla, nlo in rows[:12]:
                print(f"    {name:<22} [{iso3}]  ({la:>9.3f},{lo:>10.3f})"
                      f" -> ({nla:>9.3f},{nlo:>10.3f})  flip {flip}")
            if len(rows) > 12:
                print(f"    ... +{len(rows) - 12} more")
    if ambiguous:
        print(f"\n-- ambiguous ({len(ambiguous)}; multiple flips fit, need manual pick):")
        for sid, name, iso3, la, lo, ms in ambiguous[:10]:
            print(f"    {sid}/{name} [{iso3}] ({la},{lo}) -> {ms}")
    return len(fixable)


def country_report(stations_data: dict) -> int:
    """List stations whose declared country tag doesn't fit their coord
    AND no sign-flip rescues. Returns count."""
    mismatches = []
    for sid, src in stations_data["sources"].items():
        for st in src["stations"]:
            la, lo = st.get("lat"), st.get("lon")
            if la is None or lo is None:
                continue
            raw_cc = (st.get("country") or "").strip().upper()
            iso3 = alias_iso3(raw_cc)
            boxes = country_boxes(iso3) if iso3 else None
            if not boxes or inside_any(boxes, la, lo):
                continue
            # not inside declared country bbox; check if a sign-flip fixes
            sign_fits = any(inside_any(boxes, fla * la, flo * lo)
                            for fla, flo in ((-1, 1), (1, -1), (-1, -1)))
            if sign_fits:
                continue  # covered by sign report
            fits = [c for c, bb in BBOX.items() if inside_any([bb], la, lo)]
            mismatches.append((sid, st["name"], raw_cc, iso3, la, lo, fits))

    print("=== COUNTRY-TAG MISMATCHES ===")
    print(f"{len(mismatches)} stations whose declared country doesn't fit "
          "their coord (operator-side data quality; no auto-fix)")
    if mismatches:
        by_src = defaultdict(list)
        for r in mismatches:
            by_src[r[0]].append(r)
        for sid, rows in sorted(by_src.items(), key=lambda kv: -len(kv[1])):
            print(f"\n-- {sid}: {len(rows)}")
            for _, name, raw_cc, iso3, la, lo, fits in rows[:15]:
                alias = f" (alias {raw_cc}->{iso3})" if raw_cc != iso3 else ""
                fit_s = ",".join(fits) if fits else "(no bbox match)"
                print(f"    {name:<14} tag={raw_cc}{alias:<20}"
                      f"  ({la:>8.3f},{lo:>8.3f})  fits-> {fit_s}")
            if len(rows) > 15:
                print(f"    ... +{len(rows) - 15} more")
    return len(mismatches)


def main() -> int:
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        return 0
    mode = sys.argv[1] if len(sys.argv) > 1 else "both"
    if mode not in ("sign", "country", "both"):
        print(f"unknown mode: {mode!r}; try sign | country | both | -h",
              file=sys.stderr)
        return 2
    data = json.loads(STATIONS.read_text(encoding="utf-8"))
    if mode in ("sign", "both"):
        sign_report(data)
        if mode == "both":
            print()
    if mode in ("country", "both"):
        country_report(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
