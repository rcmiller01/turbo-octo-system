import unittest
from core.diet_engine import generate_diet_plan
from core.workout_planner import generate_workout_plan

class TestFitnessCoachCore(unittest.TestCase):

    def test_diet_plan_output(self):
        health_data = {"weight": 200, "height": 70, "age": 40, "activity_level": "light"}
        result = generate_diet_plan(health_data)
        self.assertIn("calories", result)
        self.assertIn("protein_g", result)

    def test_workout_plan_output(self):
        plan = generate_workout_plan("muscle_gain", ["barbell"], 30)
        self.assertIsInstance(plan, dict)

if __name__ == "__main__":
    unittest.main()
