import cv2
import numpy as np
from PIL import Image
from models.pose_detection.pose_estimator import PoseEstimator
from utils.visual_aide import VisualAide

def preprocess_frame(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    return image

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access camera.")
        return

    pose_model = PoseEstimator()
    coach = VisualAide()

    print("🔍 Starting camera. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        image = preprocess_frame(frame)
        keypoints = pose_model.estimate_pose(image)

        feedback = coach.check_form(keypoints)
        for msg in feedback["spoken"]:
            print("🗣️", msg)

        cv2.imshow("Live Feed (Press 'q' to exit)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
