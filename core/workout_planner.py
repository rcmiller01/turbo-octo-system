def generate_workout_plan(goal, equipment, time_minutes, health_flags=None):
    plan = {
        "goal": goal,
        "duration_minutes": time_minutes,
        "exercises": []
    }

    # Simple defaults
    full_body = ["squats", "pushups", "rows", "plank", "lunges"]

    # Reduce joint load if knee/back issues
    if health_flags:
        mobility_issues = health_flags.get("mobility_limitations", [])
        if "knee" in mobility_issues:
            full_body = [e for e in full_body if "squat" not in e and "lunge" not in e]
        if "lower_back" in mobility_issues:
            full_body = [e for e in full_body if "plank" not in e and "deadlift" not in e]

    plan["exercises"] = full_body[:min(5, len(full_body))]
    return plan
