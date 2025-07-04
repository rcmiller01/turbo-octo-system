import json
from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")

def load_latest_data(log_type):
    files = sorted(LOG_DIR.glob(f"{log_type}_*.json"))
    if not files:
        return None
    with open(files[-1], "r") as f:
        data = json.load(f)
        return data[-1] if data else None

def generate_daily_summary():
    workout = load_latest_data("workout")
    diet = load_latest_data("diet")
    health = load_latest_data("health")

    summary = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "workout_summary": workout.get("data") if workout else "No data",
        "diet_summary": diet.get("data") if diet else "No data",
        "health_metrics": health.get("data") if health else "No data",
    }

    return summary
