---
type: decision
store: house-of-jess
step: A2
status: approved
date: 2026-09-28
---
# 004 Colour palette: House Evolved

## Context
Live theme ran Sense defaults: cream, plum ink, magenta buttons, lime gradients. Eleven options were explored on one homepage mock with contrast checks. See [Colour Palette](<../Brand/Colour Palette.md>).

## Decision
01 House Evolved.

| Role | Hex |
|---|---|
| Background | #FDFBF7 |
| Surface | #F3EEE6 |
| Text | #2E2A39 |
| Muted text | #6E6878 |
| Accent | #6B2F5B |
| Button | #2E2A39 |
| Button text | #FDFBF7 |

Usage: plum accent used sparingly (eyebrows, links, small details). Buttons are ink. No gradients.

## Why
Keeps the cream and plum ink the store already had, drops the clashing magenta and lime. All pairs pass WCAG AA.
- [Evolve existing brand colours before replacing them](<../../../Zettel/202609281620 Evolve existing brand colours before replacing them.md>)
- [A small brand looks established through restraint not decoration](<../../../Zettel/202609281603 A small brand looks established through restraint not decoration.md>)

## Affects
- Data: `brand.json` palette.
- Theme (D2): Dawn color schemes built from these.
- Photos (A5): backdrops should sit near #F3EEE6.
