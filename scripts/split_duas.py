"""Regenerate duas/<topic>.json from Duas.json (the single source of truth).

Usage: python scripts/split_duas.py
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.loads((root / "Duas.json").read_text(encoding="utf-8"))
out_dir = root / "duas"
out_dir.mkdir(exist_ok=True)

for t in data["topics"]:
    duas = [d for d in data["duas"] if d["topic"] == t["topic"]]
    doc = {"topic": t["topic"], "title_en": t["title_en"], "title_ur": t["title_ur"],
           "count": len(duas), "duas": duas}
    (out_dir / f"{t['topic']}.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{t['file']}: {len(duas)}")
