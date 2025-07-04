from core.workout_planner import generate_workout_plan
from core.diet_engine import generate_diet_plan
from core.health_parser import parse_health_data
from models.pose_detection.pose_estimator import PoseEstimator
from models.food_classifier.food_estimator import FoodEstimator
from models.voice_commands.voice_listener import VoiceListener
from PIL import Image

def run_coach():
    print("🏋️ AI Fitness Coach Lite\n")
    user_goal = "fat_loss"
    equipment = ["dumbbells", "barbell"]
    time_available = 45
    health_data = {
        "age": 35,
        "weight": 180,
        "height": 70,
        "activity_level": "moderate"
    }

    print("🧠 Generating workout plan...")
    workout = generate_workout_plan(user_goal, equipment, time_available)
    print(workout)

    print("\n🍽️ Generating diet plan...")
    diet = generate_diet_plan(health_data)
    print(diet)

    # Optional: test image-based pose or food estimator
    try:
        print("\n📷 Running mock pose estimation...")
        image = Image.new("RGB", (192, 192))  # Placeholder image
        pose_model = PoseEstimator()
        keypoints = pose_model.estimate_pose(image)
        print("Keypoints:", keypoints.shape)

        print("\n🍲 Running mock food classification...")
        food_model = FoodEstimator()
        food_pred = food_model.classify_food(image)
        print("Raw prediction:", food_pred)

        print("\n🎙️ Testing voice listener stub...")
        voice = VoiceListener()
        command = voice.transcribe_audio("fake_path.wav")
        print("Recognized Command:", command)

    except Exception as e:
        print("Some modules require real input or models:", e)

if __name__ == "__main__":
    run_coach()
