import json
import csv
from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")
EXPORT_DIR = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)

def export_logs_to_json():
    export_data = {}
    for file in LOG_DIR.glob("*.json"):
        key = file.stem
        with open(file, "r") as f:
            export_data[key] = json.load(f)
    out_path = EXPORT_DIR / f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(out_path, "w") as out_file:
        json.dump(export_data, out_file, indent=2)
    return out_path

def export_logs_to_csv():
    for log_type in ["workout", "diet", "health"]:
        rows = []
        for file in LOG_DIR.glob(f"{log_type}_*.json"):
            with open(file, "r") as f:
                entries = json.load(f)
                for entry in entries:
                    row = {"timestamp": entry["timestamp"]}
                    row.update(entry["data"])
                    rows.append(row)
        if rows:
            keys = set(k for row in rows for k in row.keys())
            out_path = EXPORT_DIR / f"{log_type}_export.csv"
            with open(out_path, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=sorted(keys))
                writer.writeheader()
                writer.writerows(rows)
