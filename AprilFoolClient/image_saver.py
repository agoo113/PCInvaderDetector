import cv2
import os


class ImageSaver:
    def __init__(self, prefix, save_dir, multiple=1):
        self.index = 0
        self.prefix = prefix
        self.save_dir = save_dir
        self.multiple = multiple

    def save(self, image):
        if self.index % self.multiple == 0:
            name = '{}_{}.png'.format(self.prefix, self.index)
            path = os.path.join(self.save_dir, name)
            cv2.imwrite(path, image)
        self.index += 1
