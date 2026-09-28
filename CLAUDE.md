# Working agreement for agents in this repo

## Layout
- `wiki/` is the Obsidian vault. Store-agnostic knowledge goes in `wiki/Zettel`, `wiki/Maps`, `wiki/Playbooks`, `wiki/Sources`. Store-specific notes go in `wiki/Stores/<Store Name>/`.
- `stores/<slug>/data/*.json` is the machine-readable source of truth. `brand.json` feeds theme settings and image prompts. `store.json` mirrors Shopify state. `assets.json` registers every image.
- `stores/<slug>/theme/` is theme source. Never publish a theme from automation.

## Rules
- No secrets in git. Keys live in `.env` (ignored). CI secrets live in GitHub Actions.
- Links in the wiki are relative markdown links with angle brackets: `[Title](<../Zettel/202609281601 Title.md>)`. No `[[wikilinks]]`.
- Frontmatter on every wiki note: `id`, `type`, `status`, `tags`, `created`.
- When a decision is approved, commit together: the Decision note, any new or updated Zettel, the Map entry, the JSON data change and the Log line.
- Any change made to Shopify through the API is reflected in `store.json` in the same commit.
- Commit messages: `<store-slug>: <step id> <summary>` for store work, `wiki: <summary>` for knowledge-only changes.
- No em dashes in any written content.

## Zettel rules
- One idea per note. Title is the claim, written as a statement.
- Store-agnostic. If it only makes sense for one store, it is a Decision, not a Zettel.
- ID is `YYYYMMDDHHMM`. Filename is `<id> <Title>.md`.
- Link at least one Map. Record which stores applied it in `used_by`.
