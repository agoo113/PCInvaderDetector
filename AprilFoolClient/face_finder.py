import cv2
import os


def get_region_of_interest(image, coordinates):
    x, y, w, h = coordinates
    return image[y:y + h, x:x + w]


class FaceFinder:
    def __init__(self):
        profile_dir = os.path.join('cascades', 'data')
        profiles = [
            os.path.join('haarcascades', 'haarcascade_frontalface_default.xml'),
            # os.path.join('haarcascades', 'haarcascade_frontalface_alt.xml'),
            os.path.join('haarcascades', 'haarcascade_frontalface_alt2.xml'),
            os.path.join('lbpcascades', 'lbpcascade_frontalface_improved.xml')
        ]

        self.finders = [cv2.CascadeClassifier(os.path.join(profile_dir, profile))
                        for profile in profiles]

    def find(self, image, scale_factor=1.5, min_neighbors=5):
        faces = []
        for finder in self.finders:
            faces.extend(finder.detectMultiScale(image, scaleFactor=scale_factor, minNeighbors=min_neighbors))

        return faces
