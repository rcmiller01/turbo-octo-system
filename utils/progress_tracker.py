import json
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

LOG_DIR = Path("logs")

def load_log_data(log_type):
    data = []
    for file in sorted(LOG_DIR.glob(f"{log_type}_*.json")):
        with open(file, "r") as f:
            entries = json.load(f)
            for entry in entries:
                timestamp = entry["timestamp"]
                record = entry["data"]
                data.append((timestamp, record))
    return data

def plot_weight_trend():
    data = load_log_data("health")
    dates, weights = [], []
    for timestamp, record in data:
        if "weight" in record:
            dates.append(datetime.fromisoformat(timestamp))
            weights.append(record["weight"])
    if dates:
        plt.figure()
        plt.plot(dates, weights, marker="o", label="Weight (lbs)")
        plt.title("Weight Trend")
        plt.xlabel("Date")
        plt.ylabel("Weight (lbs)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig("progress/weight_trend.png")
        plt.close()

def plot_reps_trend():
    data = load_log_data("workout")
    dates, reps = [], []
    for timestamp, record in data:
        if "total_reps" in record:
            dates.append(datetime.fromisoformat(timestamp))
            reps.append(record["total_reps"])
    if dates:
        plt.figure()
        plt.plot(dates, reps, marker="s", color="orange", label="Reps")
        plt.title("Total Reps per Session")
        plt.xlabel("Date")
        plt.ylabel("Reps")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig("progress/reps_trend.png")
        plt.close()

def plot_hr_zones():
    data = load_log_data("health")
    zones = {"zone_1": [], "zone_2": [], "zone_3": []}
    dates = []
    for timestamp, record in data:
        if all(k in record for k in zones):
            dates.append(datetime.fromisoformat(timestamp))
            for k in zones:
                zones[k].append(record[k])
    if dates:
        plt.figure()
        for k in zones:
            plt.plot(dates, zones[k], marker="^", label=k)
        plt.title("Heart Rate Zones")
        plt.xlabel("Date")
        plt.ylabel("Minutes")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig("progress/hr_zones.png")
        plt.close()
