def parse_health_questionnaire(answers):
    """
    Takes a dictionary of user responses and returns flags for personalized adjustments.
    Example input:
    {
        "diabetic": true,
        "hypertension": false,
        "mobility_limitations": ["knee", "lower_back"]
    }
    """
    conditions = {
        "diabetic": answers.get("diabetic", False),
        "hypertension": answers.get("hypertension", False),
        "mobility_limitations": answers.get("mobility_limitations", []),
        "age": answers.get("age", 30),
        "weight": answers.get("weight", 180),
        "height": answers.get("height", 70),
        "activity_level": answers.get("activity_level", "moderate")
    }
    return conditions
