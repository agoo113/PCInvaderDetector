import os
import numpy as np
import cv2
from face_finder import FaceFinder, get_region_of_interest
from face_recognizer import FaceRecognizer

face_finder = FaceFinder()
recognizer = FaceRecognizer()
dataset_dir = os.path.join('dataset', 'train')


x_train = []
y_labels = []
label = 1


def recursive_append(path, x_train, y_labels, current_label):
    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        if os.path.isdir(filepath):
            recursive_append(filepath, x_train, y_labels, current_label)
        elif file.endswith('png') or file.endswith('jpg'):
            image_array = cv2.imread(filepath)
            image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
            # image_array = cv2.equalizeHist(image_array)
            # normalized_image_array = np.zeros(image_array.shape)
            # normalized_image_array = cv2.normalize(image_array, normalized_image_array)
            # while True:
            #     cv2.imshow('image', image_array)
            #     if cv2.waitKey(20) & 0xFF == ord('q'):
            #         break
            faces = face_finder.find(image_array)
            for coordinates in faces:
                region_of_interest = get_region_of_interest(image_array, coordinates)
                x_train.append(region_of_interest)
                y_labels.append(current_label)
                print('filepath: {}, label: {}'.format(filepath, label))


for person_dir in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person_dir)
    recursive_append(person_path, x_train, y_labels, label)
    label += 1

recognizer.train(x_train, np.array(y_labels), 'trainer.yml')
