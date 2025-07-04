import numpy as np
import tensorflow.lite as tflite
from PIL import Image

class PoseEstimator:
    def __init__(self, model_path='models/pose_detection/movenet.tflite'):
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def preprocess(self, image: Image.Image):
        image = image.resize((192, 192))
        image = np.array(image, dtype=np.float32)
        image = np.expand_dims(image, axis=0)
        return image

    def estimate_pose(self, image: Image.Image):
        input_data = self.preprocess(image)
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        keypoints = self.interpreter.get_tensor(self.output_details[0]['index'])
        return keypoints
