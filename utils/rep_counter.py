import numpy as np

class RepCounter:
    def __init__(self, exercise_type="squat"):
        self.exercise_type = exercise_type
        self.state = "UP"
        self.count = 0

    def get_angle(self, a, b, c):
        a, b, c = np.array(a[:2]), np.array(b[:2]), np.array(c[:2])
        ba = a - b
        bc = c - b
        cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-5)
        return np.degrees(np.arccos(np.clip(cosine, -1.0, 1.0)))

    def update(self, keypoints):
        if self.exercise_type == "squat":
            # Use left hip (11), knee (13), ankle (15)
            angle = self.get_angle(keypoints[11], keypoints[13], keypoints[15])
            if self.state == "UP" and angle < 70:
                self.state = "DOWN"
            elif self.state == "DOWN" and angle > 160:
                self.state = "UP"
                self.count += 1
        return self.count
