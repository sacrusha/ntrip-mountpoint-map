# Popout UI Proposals — NTRIP Mountpoint Map

## Context

The app has three popout UI surfaces, all using non-standard or inconsistent patterns:

1. **"How it works" banner expansion** (`#banner-more`) — custom JS `body.classList` toggle,
   custom chevron `::after`, no ARIA, ESC does not close it, consumes 56 px permanently.
2. **Sources/Filters panel** (`#toggles`) — topright Leaflet control with `<details>/<summary>`
   inside a plain `<div>`. On mobile: cramped top-right corner, `max-height:55vh` scroll,
   no close gesture, nested `<details>` sub-sections hard to discover on touch.
3. **Station & VRS marker popups** — Leaflet `bindPopup()`. Closes on map pan, ×12 px close
   button (far below 44×44 px touch target), can appear off-screen on mobile, no ARIA.

---

## Proposal 0 — Do Nothing

Keep all three popouts exactly as they are today.

**Rationale for keeping:** The app works. All three surfaces are functional, and a rewrite
carries risk of regressions. Users who have already learned the UI would need to re-learn it.
Development time spent here is time not spent on data quality, new networks, or coverage polygons.

---

## Proposal 1 — `<dialog>` for "how it works" + bottom sheet for filters + persistent panel for station details
*(Three targeted fixes, one per surface)*

**Surface 1 — Banner "how it works":**
Replace the 56 px banner + custom drop-down with a compact ribbon (≤ 32 px) containing an
ⓘ button. Clicking it calls `howDialog.showModal()` on a `<dialog>` element containing the
existing primer text. The browser provides: backdrop, focus trap, ESC dismissal, `aria-modal`.
First-time visitors auto-open the dialog. `localStorage` marks it seen.

**Surface 2 — Sources/Filters panel:**
Keep the Leaflet control for `min-width: 601px`. Below 600 px: hide the control, show a fixed
"Filters ☰" button in the thumb zone (`bottom:16px; right:16px`). Tapping it slides up a bottom
sheet (`position:fixed; bottom:0; left:0; right:0; transform:translateY(0/100%); transition:transform 0.25s`).
Same checkbox DOM, different container.

**Surface 3 — Station & VRS popups:**
Add `<div id="station-panel">` fixed to the bottom on mobile, right edge on desktop. Replace
`.bindPopup()` with `.on('click', openPanel)`. Panel persists through pans; closed by explicit
button or background tap. Gives full room for multi-source station details without overflow.

**Trade-off:** Three separate patterns to implement and maintain. Each surface is solved
optimally for its use case, but a user encounters three different UI mechanisms.

---

## Proposal 2 — `<dialog>` for every overlay surface
*(Single primitive, two modes)*

Use the native `<dialog>` element for all three popouts:

- **`dialog.showModal()`** (modal, backdrop, ESC): "How it works" content — informational,
  warrants full attention before map interaction.
- **`dialog.show()`** (non-modal, map stays interactive): Station/VRS details and the filter
  panel — positioned via CSS as bottom sheets on mobile, right-anchored on desktop.

The banner collapses to a ribbon with an ⓘ button. `bindPopup()` calls become `.on('click', …)`
injecting existing `buildPopup()` HTML into a shared station `<dialog>`. The Sources control
becomes a button opening a filter `<dialog>`. All three share: browser-native semantics,
`::backdrop` styling, ESC dismissal, one CSS `@media` block for positioning.

**Trade-off:** `<dialog>` non-modal positioning requires careful CSS (it renders in the
top layer, so `position:fixed` coordinates are relative to the viewport — generally fine here).
Baseline 2022 browser support; works in all evergreen browsers without a polyfill.

---

## Proposal 3 — One shared bottom-sheet / side-drawer panel for every overlay surface
*(Single component, content-swapped)*

One `<div id="panel">` element serves all three surfaces by swapping its inner content:

- **Mobile:** `position:fixed; bottom:0; left:0; right:0` — slides up from the bottom.
- **Desktop:** `position:fixed; top:0; right:0; width:320px; bottom:0` — slides in from the right.
- **Open/close:** `transform:translateY(0/100%)` (mobile) or `translateX(0/100%)` (desktop),
  `transition:transform 0.25s ease`. One close button, consistent location.

All three popouts become content loads into this one panel:
- ⓘ button → loads "how it works" text → opens panel
- Marker click → loads `buildPopup()` HTML → opens panel (persists through pans)
- "Filters" button (fixed, thumb zone) → loads sources checkboxes → opens panel

The banner is eliminated entirely; its content moves into the panel. The result is one dismiss
gesture and one close-button location the user learns once.

**Trade-off:** Only one panel is visible at a time — a user can't have filters open while
reading station details. This is the established tradeoff in Google Maps, Apple Maps, Organic
Maps. It is a real constraint for power users who want to cross-reference.

---

## Summary Table

| # | Pattern | Surfaces addressed | Mobile UX | New abstractions | Effort |
|---|---------|-------------------|-----------|-----------------|--------|
| 0 | Do nothing | — | Current (poor) | None | None |
| 1 | Targeted fixes (dialog + bottom sheet + panel) | All 3, separately | Good per surface | 3 separate | Medium |
| 2 | `<dialog>` everywhere | All 3, unified primitive | Good | 1 element type | Low–Medium |
| 3 | Shared panel (bottom sheet / drawer) | All 3, one component | Excellent | 1 component | Medium |
