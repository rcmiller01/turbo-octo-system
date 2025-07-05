from utils.equipment_profile import get_user_equipment

EXERCISE_LIBRARY = {
    "barbell": [
        "Barbell Bench Press", "Barbell Back Squat", "Barbell Deadlift", "Barbell Rows",
        "Barbell Overhead Press", "Barbell Front Squat", "Barbell Romanian Deadlift"
    ],
    "dumbbell": [
        "Dumbbell Lateral Raises", "Incline Dumbbell Curl", "Dumbbell Shrugs", "Dumbbell Lunges",
        "Incline Dumbbell Press", "1-Arm Dumbbell Row"
    ],
    "cable_machine": [
        "Cable Crossovers", "Cable Pushdowns", "Cable Reverse Flys", "Cable Lateral Raises"
    ],
    "machines": [
        "Leg Curl Machine", "Leg Press Machine", "Seated Fly Machine", "Seated Calf Raise",
        "Machine Reverse Fly"
    ],
    "bodyweight": [
        "Pull-ups", "Dips", "Hanging Leg Raises", "Chin-ups"
    ]
}

def generate_workout_plan(goal, equipment=None, time_minutes=45, health_flags=None):
    user_equipment = equipment or get_user_equipment()
    plan = {
        "goal": goal,
        "duration_minutes": time_minutes,
        "exercises": []
    }

    selected_exercises = []
    for category, enabled in user_equipment.items():
        if enabled:
            selected_exercises.extend(EXERCISE_LIBRARY.get(category, []))

    # Sample 6-8 exercises from allowed pool (random or based on goal later)
    plan["exercises"] = selected_exercises[:8]
    return plan
