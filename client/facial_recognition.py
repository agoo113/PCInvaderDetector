import cv2

from datetime import datetime
from face_finder import FaceFinder, get_region_of_interest
from face_recognizer import FaceRecognizer


class InvaderDetectorWithFace:
    def __init__(self):
        self.face_finder = FaceFinder()
        self.recognizer = FaceRecognizer()
        self.recognizer.load('trainer.yml')
        self.security_trigger = Trigger(20, lambda similarity: similarity > 80)

    def on_enabled_start(self):
        pass

    def on_disabled_update(self):
        pass

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_finder.find(gray)

        best_face = None
        best_confidence = 1000
        for coordinates in faces:
            region_of_interest = get_region_of_interest(gray, coordinates)
            id_, conf = self.recognizer.predict(region_of_interest)

            if conf < best_confidence:
                best_face = region_of_interest
                best_confidence = conf

            print('{}, {}, {}'.format(datetime.now(), id_, conf))

            # save_region_of_interest(gray, coordinates)
            self.highlight_face(frame, coordinates)

        if best_face is not None:
            if self.security_trigger.update(best_confidence):
                print('Face not match!')

                return True

        return False

    def highlight_face(self, image, coordinates, color=(0, 0, 255)):
        x, y, w, h = coordinates
        x_end = x + w
        y_end = y + h
        stroke = 2
        cv2.rectangle(image, (x, y), (x_end, y_end), color, stroke)


class Trigger:
    def __init__(self, trigger_count, predicate):
        self.predicate = predicate
        self.trigger_count = trigger_count
        self.count = 0

    def update(self, *args):
        if self.predicate(*args):
            self.count += 1
            if self.count >= self.trigger_count:
                self.count = 0
                return True

        else:
            self.count = 0

        return False

