import cv2
import os

from face_finder import FaceFinder, get_region_of_interest
from face_recognizer import FaceRecognizer
from image_saver import ImageSaver


test_dir = os.path.join('dataset', 'test')


face_finder = FaceFinder()
recognizer = FaceRecognizer()
recognizer.load('trainer.yml')

for file in os.listdir(test_dir):
    if file.endswith('png') or file.endswith('jpg'):
        filepath = os.path.join(test_dir, file)
        image_array = cv2.imread(filepath)
        image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        faces = face_finder.find(image_array)
        for coordinates in faces:
            region_of_interest = get_region_of_interest(image_array, coordinates)
            predicted_label, confidence = recognizer.predict(region_of_interest)
            print('{}: {}, {}'.format(file, predicted_label, confidence))
