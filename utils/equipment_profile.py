def get_user_equipment():
    """
    Returns a dictionary representing user's available equipment.
    This could later be user-editable via UI or loaded from a config.
    """
    return {
        "barbell": True,
        "dumbbell": True,
        "cable_machine": False,
        "machines": False,
        "bodyweight": True
    }
