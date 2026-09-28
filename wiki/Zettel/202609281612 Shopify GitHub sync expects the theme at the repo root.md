---
id: "202609281612"
type: zettel
status: seedling
tags: [tooling, shopify]
applies_to: [shopify, dtc]
used_by: [house-of-jess]
created: 2026-09-28
---
# Shopify GitHub sync expects the theme at the repo root

The native GitHub integration connects a branch whose root is a theme. In a monorepo, deploy with Shopify CLI from CI instead (`shopify theme push --path stores/<slug>/theme`) using a Theme Access password per store. Push to an unpublished theme and publish manually.

---
Maps: [Store ops and tooling](<../Maps/Store ops and tooling.md>)
