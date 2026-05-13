AI-only digest of who this project serves.
Abbrev: MP=mountpoint, NRTK=network RTK, CORS=continuously operating reference station, GCP=ground control point.

## In-scope users

[mode:discovery] hobbyist | small shop; needs better-than-phone GPS; no prior NTRIP/RTK/NRTK knowledge -> must learn what exists locally, fit for purpose.
[mode:migration] inherited config; old MP dead; knows geographic area, not new MP name. Might not know about Epoch/datum.

Profile traits (cross-mode):
- Budget: $0 corrections; hardware €275–$3k (ArduSimple → Emlid RS3 tier).
- Tolerance: dead volunteer bases, hand-config, English-only docs, registration friction.
- Output: cm-level positions, one-shot or revisited; no SLA, no certification.
- Receiver: dual-band (L1+L2) minimum; F9P-class typical; phone chip excluded.

## Secondary users 
| budget for paid VRS | no prior NTRIP/RTK/NRTK knowledge -> must learn what exists, what's nearby, fit for purpose.
| Sub-metre DGNSS-only users | RTK as option, HAS pricey for now, needs to know about real accuracy |
| Post-processing-only (EUREF-IP, EPN) | fallback where RTK not available |

## Out-of-scope users (explicit rejects)

| User | Why rejected |
| Enterprise | Has paid path; doesn't need free aggregation |
| Legal cadastral surveyor | Needs certified gear + datum tie + jurisdictional acceptance |
| Commercial machine-control / construction stakeout | Needs uptime SLA + design-datum tie |
| Structural displacement / scientific geodesy | Needs CGNSS + IGS final orbits + 24h+ sessions; mm-class |
| Single-frequency / smartphone-only / Trimble Catalyst DA2 (subscription-locked) | Hardware can't do RTK regardless of MP source |

## Use-case catalogue (canonical in help_topics.json `is-this-for-me`)

Citizen science / heritage / ecology:
- Amateur excavation find recording (~5 cm); community dig 1m×1m grid layout (2–5 cm); fossil site spatial recording (~5 cm); rock art / petroglyph stake-out (5–10 cm); cave entrance tie-ins (10–20 cm).
- Rare-plant demography (3–5 cm); invasive-species eradication follow-up (10 cm); permanent ecology quadrat corners (5–10 cm); nest/den/roost logging (10–20 cm); beach erosion transects (5 cm H, 3–5 cm V).

DIY / maker:
- Robot lawnmower (OpenMower, Ardumower Sunray; 2–5 cm); autonomous RC survey boat + echosounder (20–30 cm H); drone photogrammetry GCPs (3–5 cm).

Personal / civic:
- OSM footway + kerb mapping for wheelchair routing (10–20 cm); landowner boundary stake-out pre-fencing (5–10 cm); foraging-patch archive (50 cm – 1 m, borderline w/ SBAS).

## Audience tone (writers)

- guide.html, help_topics.json, country_markers.json `note` field: plain language, no acronyms unexpanded, no internal jargon (`$200/yr cutoff`, audit phrasing). UK spelling. "GPS" colloquially; "GNSS" only when hardware/signal-structurally correct (L1/L2 ≠ "GPS bands" — Galileo E1/E5b share them).
- gnss-ai-guide.md: hobbyist NTRIP user, decimetre target; sub-decimetre + survey-grade = explicitly not the audience (§13.7).
- README + map UI: hobbyist + small shop assumed; no enterprise framing.
