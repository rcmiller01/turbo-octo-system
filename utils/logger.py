import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

def log_event(event_type, data):
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file = LOG_DIR / f"{event_type}_{date_str}.json"

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "data": data
    }

    if log_file.exists():
        with open(log_file, "r+") as f:
            log_data = json.load(f)
            log_data.append(log_entry)
            f.seek(0)
            json.dump(log_data, f, indent=2)
    else:
        with open(log_file, "w") as f:
            json.dump([log_entry], f, indent=2)

def log_workout(session_data):
    log_event("workout", session_data)

def log_diet(diet_data):
    log_event("diet", diet_data)

def log_health_metrics(metrics):
    log_event("health", metrics)
