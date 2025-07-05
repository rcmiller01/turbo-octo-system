import time
from core.workout_planner import generate_workout_plan
from models.pose_detection.pose_estimator import PoseEstimator
from utils.visual_aide import VisualAide
from utils.voice_output import VoiceOutput
from PIL import Image
import cv2

def preprocess_frame(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb)

def run_workout_session(goal="fat_loss", equipment=None, duration=30, health_flags=None):
    if equipment is None:
        equipment = ["bodyweight"]

    print("📋 Generating personalized workout plan...")
    plan = generate_workout_plan(goal, equipment, duration, health_flags)
    exercises = plan["exercises"]

    voice = VoiceOutput()
    pose_model = PoseEstimator()
    aide = VisualAide()

    print("🎬 Starting live workout. Press 'q' to quit.")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access camera.")
        return

    for exercise in exercises:
        voice.speak(f"Next: {exercise}. Get ready!")
        time.sleep(3)

        voice.speak(f"Begin {exercise} now.")
        start_time = time.time()
        session_duration = 20  # seconds per exercise

        while time.time() - start_time < session_duration:
            ret, frame = cap.read()
            if not ret:
                break

            image = preprocess_frame(frame)
            keypoints = pose_model.estimate_pose(image)
            feedback = aide.check_form(keypoints)

            if feedback["spoken"]:
                voice.speak(feedback["spoken"])

            cv2.imshow("Workout Camera (Press 'q' to exit)", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        voice.speak("Rest for 10 seconds.")
        time.sleep(10)

    cap.release()
    cv2.destroyAllWindows()
    voice.speak("Workout complete. Great job!")

if __name__ == "__main__":
    run_workout_session()
