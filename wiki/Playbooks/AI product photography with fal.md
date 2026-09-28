---
type: playbook
status: draft
created: 2026-09-28
---
# AI product photography with fal

1. Shoot a clean reference of each real product (phone is fine, even light, plain background).
2. Lock the photo style in `brand.json` (backdrop, lighting, props, prompt template).
3. Write a shot list per product: packshot, worn, macro, flat lay, scale.
4. Run `scripts/gen_images.py <slug> <shotlist.json>`. Edit models for anything showing the product.
5. Review candidates, mark approved or rejected in `assets.json`.
6. Upload approved images to Shopify Files, record `shopify_url`.

Principles: [202609281613 AI product photos must be edited from real product references](<../Zettel/202609281613 AI product photos must be edited from real product references.md>) · [202609281614 Host generated images on Shopify not on the generator's URLs](<../Zettel/202609281614 Host generated images on Shopify not on the generator's URLs.md>) · [202609281608 Consistent photography matters more than the theme](<../Zettel/202609281608 Consistent photography matters more than the theme.md>)
