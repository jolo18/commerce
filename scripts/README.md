# scripts

| Script | What it does | Status |
|---|---|---|
| `new-store <slug> "<Store Name>" <shop-domain>` | Scaffolds `stores/<slug>/` and `wiki/Stores/<Store Name>/` from templates | Ready |
| `gen_images.py` | Builds prompts from `brand.json` + a shot list, calls fal, downloads results, registers them in `assets.json` | Draft, finalised in step A5/B2 |
| `sync_store.py` | Pulls live Shopify state into `store.json` | Stub. Today the sync runs through Claude's Shopify connector |
