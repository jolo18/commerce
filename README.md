# commerce

Monorepo for running multiple Shopify stores, plus a Zettelkasten wiki that holds everything reusable across them.

| Path | What lives here |
|---|---|
| `wiki/` | Obsidian vault. Open **this folder** as the vault, not the repo root. |
| `stores/<slug>/` | One folder per store: config, theme source, machine-readable data. |
| `scripts/` | Shared tooling: new store scaffold, image generation, Shopify sync. |
| `.github/workflows/` | CI. Theme deploys via Shopify CLI. |

## Stores

| Store | Slug | Shop domain | Status |
|---|---|---|---|
| House of Jess | `house-of-jess` | `88d457-c1.myshopify.com` | Pre-relaunch |

## How work flows

1. Every task has an input, an output and an approval gate. See `wiki/Stores/<store>/Plan.md`.
2. On approval: write a Decision note, extract reusable insight into a Zettel, update `stores/<slug>/data/*.json`, commit all of it together.
3. Theme changes under `stores/<slug>/theme/` deploy to an **unpublished** theme through CI. Publishing is always manual.

## Setup

```bash
cp .env.example .env        # fill in FAL_KEY etc. Never commit .env
```

Obsidian: open `wiki/` as a vault. Links are standard markdown links so they also render on GitHub.
