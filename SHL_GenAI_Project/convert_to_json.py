import pandas as pd
import json

"""
Usage:
  pip install pandas openpyxl
  python convert_to_json.py "Gen_AI Dataset.xlsx"

This script reads the Excel file and writes products.json in the same folder.
It handles missing columns gracefully.
"""

import sys
from pathlib import Path

INPUT = sys.argv[1] if len(sys.argv) > 1 else "Gen_AI Dataset.xlsx"

def safe_list_split(val):
    if not val or (isinstance(val, float) and pd.isna(val)):
        return []
    if isinstance(val, list):
        return [str(x).strip().lower() for x in val if str(x).strip()]
    return [s.strip().lower() for s in str(val).split(',') if s.strip()]


def main():
    path = Path(INPUT)
    if not path.exists():
        print(f"File not found: {path}. Please place the Excel file next to this script or pass its path as an argument.")
        return

    df = pd.read_excel(path, engine='openpyxl')
    df = df.fillna("")

    records = []
    for _, row in df.iterrows():
        pid = row.get("Product ID") or row.get("ID") or row.get("product_id") or ""
        title = row.get("Title") or row.get("title") or ""
        description = row.get("Description") or row.get("description") or ""
        skills = safe_list_split(row.get("Skills") or row.get("skills") or "")
        tags = safe_list_split(row.get("Tags") or row.get("tags") or "")
        duration = 0
        if "Duration" in df.columns:
            try:
                duration = int(row.get("Duration") or 0)
            except Exception:
                duration = 0
        rec = {
            "id": str(pid).strip(),
            "title": str(title).strip(),
            "description": str(description).strip(),
            "skills": skills,
            "tags": tags,
            "durationMinutes": duration
        }
        records.append(rec)

    out = {"products": records}
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print("✅ Created products.json with", len(records), "entries")

if __name__ == '__main__':
    main()
