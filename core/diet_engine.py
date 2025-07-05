def generate_diet_plan(health_data):
    weight = health_data.get("weight", 180)
    height = health_data.get("height", 70)
    age = health_data.get("age", 30)
    activity = health_data.get("activity_level", "moderate")

    # Base TDEE estimate
    if activity == "light":
        tdee = weight * 13
    elif activity == "moderate":
        tdee = weight * 15
    else:
        tdee = weight * 17

    # Adjust for special conditions
    if health_data.get("diabetic"):
        carb_ratio = 0.3
        fat_ratio = 0.3
        protein_ratio = 0.4
    else:
        carb_ratio = 0.5
        fat_ratio = 0.25
        protein_ratio = 0.25

    calories = int(tdee)
    protein = int((calories * protein_ratio) / 4)
    carbs = int((calories * carb_ratio) / 4)
    fat = int((calories * fat_ratio) / 9)

    return {
        "calories": calories,
        "protein_g": protein,
        "carbs_g": carbs,
        "fat_g": fat
    }
