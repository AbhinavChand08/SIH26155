from pathlib import Path
import json

from drain3.template_miner import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig

from flattener import flatten_file


# --------------------------
# Folder setup
# --------------------------

CONFIG_DIR = Path("configs")
FLAT_DIR = Path("output/flattened")
TEMPLATE_DIR = Path("output/templates")

FLAT_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATE_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------
# Drain3 setup
# --------------------------

config = TemplateMinerConfig()
config.load("drain3.ini")

template_miner = TemplateMiner(config=config)


# --------------------------
# Process every config file
# --------------------------

for cfg in CONFIG_DIR.iterdir():

    if not cfg.is_file():
        continue

    print(f"\n{'='*70}")
    print(f"Processing: {cfg.name}")
    print(f"{'='*70}")

    try:

        flattened_file = flatten_file(cfg, FLAT_DIR)

        print(f"Flattened file: {flattened_file.name}")

        templates = []

        with open(flattened_file, "r", encoding="utf-8") as f:

            for line in f:

                line = line.strip()

                if not line:
                    continue

                result = template_miner.add_log_message(line)

                templates.append({
                    "original_command": line,
                    "cluster_id": result["cluster_id"],
                    "template": result["template_mined"]
                })

        output_json = TEMPLATE_DIR / f"{cfg.stem}_templates.json"

        with open(output_json, "w", encoding="utf-8") as out:
            json.dump(templates, out, indent=4)

        print(f"Templates saved: {output_json.name}")

    except NotImplementedError as e:

        print(f"Skipped {cfg.name}: {e}")

print("\nPipeline completed.")