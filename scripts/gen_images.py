"""Generate on-brand images with fal and register them in assets.json.

Draft. The prompt template and model choices are locked in step A5 (photo style guide).

Usage:
    python scripts/gen_images.py <store-slug> <shotlist.json>

shotlist.json:
    [{"id": "heart-pendant-packshot", "purpose": "product:heart-pendant",
      "shot": "packshot", "subject": "gold heart pendant on a fine chain",
      "reference_image": "stores/house-of-jess/assets/raw/heart.jpg",
      "aspect_ratio": "4:5", "n": 2}]
"""
import json, os, sys, pathlib, datetime, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]

def load_env():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

def build_prompt(brand, item):
    style = brand.get("photo_style", {})
    template = style.get("prompt_template") or "{subject}, {shot}, {backdrop}, {lighting}"
    return template.format(
        subject=item["subject"],
        shot=style.get("shots", {}).get(item["shot"], item["shot"]),
        backdrop=style.get("backdrop", "warm cream linen backdrop"),
        lighting=style.get("lighting", "soft natural window light"),
    )

def main(slug, shotlist_path):
    load_env()
    import fal_client  # pip install fal-client

    store = ROOT / "stores" / slug
    brand = json.loads((store / "data/brand.json").read_text())
    reg_path = store / "data/assets.json"
    registry = json.loads(reg_path.read_text())
    out_dir = store / "assets/generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    models = brand.get("photo_style", {}).get("models", {})

    for item in json.loads(pathlib.Path(shotlist_path).read_text()):
        prompt = build_prompt(brand, item)
        args = {"prompt": prompt, "num_images": item.get("n", 1)}
        if item.get("reference_image"):
            model = models.get("edit", "fal-ai/flux-pro/kontext")
            args["image_url"] = fal_client.upload_file(str(ROOT / item["reference_image"]))
        else:
            model = models.get("generate", "fal-ai/flux-pro/v1.1-ultra")
            args["aspect_ratio"] = item.get("aspect_ratio", "4:5")
        result = fal_client.subscribe(model, arguments=args)
        for i, img in enumerate(result.get("images", [])):
            local = out_dir / f"{item['id']}-{i + 1}.jpg"
            urllib.request.urlretrieve(img["url"], local)
            registry["assets"].append({
                "id": f"{item['id']}-{i + 1}",
                "purpose": item["purpose"],
                "shot": item["shot"],
                "model": model,
                "prompt": prompt,
                "fal_url": img["url"],
                "local_path": str(local.relative_to(ROOT)),
                "shopify_url": None,
                "status": "candidate",
                "created": datetime.date.today().isoformat(),
            })
            print("saved", local.relative_to(ROOT))
    reg_path.write_text(json.dumps(registry, indent=2) + "\n")

if __name__ == "__main__":
    main(*sys.argv[1:3])
