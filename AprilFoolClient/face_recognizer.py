import cv2


class FaceRecognizer:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    def load(self, saved_model_path):
            self.recognizer.read(saved_model_path)

    def train(self, x_train, y_labels, saved_model_path):
        self.recognizer.train(x_train, y_labels)
        self.recognizer.save(saved_model_path)

    def predict(self, region_of_interest):
        return self.recognizer.predict(region_of_interest)