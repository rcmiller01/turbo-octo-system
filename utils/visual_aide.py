import numpy as np

class VisualAide:
    def __init__(self, keypoint_labels=None):
        self.keypoint_labels = keypoint_labels or [
            "nose", "left_eye", "right_eye", "left_ear", "right_ear",
            "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
            "left_wrist", "right_wrist", "left_hip", "right_hip",
            "left_knee", "right_knee", "left_ankle", "right_ankle"
        ]

    def check_form(self, keypoints):
        """
        Accepts keypoints from pose_estimator (shape: 1x17x3).
        Returns a list of spoken and textual corrections.
        """
        corrections = []
        spoken = []
        text = []

        kp = keypoints[0]  # (17, 3)
        def get_angle(a, b, c):
            ba = np.array(a[:2]) - np.array(b[:2])
            bc = np.array(c[:2]) - np.array(b[:2])
            cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-5)
            angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))
            return angle

        try:
            # Example: Check knee angle during squat
            left_knee_angle = get_angle(kp[11], kp[13], kp[15])  # hip-knee-ankle
            if left_knee_angle < 70:
                spoken.append("Try squatting deeper for full range.")
                text.append("Knee angle is shallow — aim for 90° or more.")

            # Check back alignment
            shoulder_slope = abs(kp[5][1] - kp[6][1])
            if shoulder_slope > 30:
                spoken.append("Keep your shoulders level.")
                text.append("Back alignment issue detected — uneven shoulders.")

            # Check head alignment
            head_tilt = abs(kp[0][0] - ((kp[5][0] + kp[6][0]) / 2))
            if head_tilt > 40:
                spoken.append("Look forward, not down.")
                text.append("Head position misaligned — too far forward/down.")

        except Exception as e:
            text.append(f"Pose analysis error: {e}")

        return {"spoken": spoken, "text": text}
