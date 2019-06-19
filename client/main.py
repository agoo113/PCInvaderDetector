import time
import cv2

from facial_recognition import InvaderDetectorWithFace
from invader_found_action import on_invader_found_with_image
from mouse_keyboard_detector import InvaderDetectorWithActivity
from client import get_system_status

capture = cv2.VideoCapture(0)
invader_detector_with_face = InvaderDetectorWithFace()
invader_detector_with_activity = InvaderDetectorWithActivity()

invader_found = False

try:
    while not invader_found:
        system_enabled = get_system_status()

        if system_enabled:
            print('Enabled')

            invader_detector_with_face.on_enabled_start()
            invader_detector_with_activity.on_enabled_start()
            while not invader_found:
                system_enabled = get_system_status()
                if not system_enabled:
                    break

                ret, frame = capture.read()
                if invader_detector_with_activity.detect() or \
                        invader_detector_with_face.detect(frame):
                    invader_found = True
                    on_invader_found_with_image(frame)
                    break

                time.sleep(0.1)

                # cv2.imshow('frame', frame)
                # if cv2.waitKey(20) & 0xFF == ord('q'):
                #     break

        else:
            print('Not enabled')

            invader_detector_with_activity.on_disabled_update()
            invader_detector_with_face.on_disabled_update()
            time.sleep(1)


finally:
    print('Finish up.')
    capture.release()
    cv2.destroyAllWindows()
