---
type: decision
store: house-of-jess
step: 1
status: approved
date: 2026-09-28
---
# 002 Monorepo with Zettelkasten wiki

## Context
Need to track every decision, brand guideline and design concept, and reuse knowledge when launching more stores.

## Options
1. Separate repos per store plus a wiki repo.
2. One monorepo: `wiki/` vault, `stores/<slug>/`, shared `scripts/`, CI.

## Decision
Option 2, repo `jolo18/commerce`. Themes deploy with Shopify CLI from GitHub Actions to an unpublished theme.

## Why
[202609281612 Shopify GitHub sync expects the theme at the repo root](<../../../Zettel/202609281612 Shopify GitHub sync expects the theme at the repo root.md>) · [202609281615 Keep the knowledge vault separate from code folders](<../../../Zettel/202609281615 Keep the knowledge vault separate from code folders.md>)
