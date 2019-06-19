import win32api
import win32con
import time
import pywintypes

from client import get_system_status
from invader_found_action import on_invader_found


class InvaderDetectorWithActivity():
    def __init__(self):
        self.key_list = list(range(ord('A'), ord('Z') + 1)) + \
                        [win32con.VK_SPACE, win32con.VK_UP, win32con.VK_DOWN, win32con.VK_LEFT,
                         win32con.VK_RIGHT]
        self.last_mouse_position = win32api.GetCursorPos()
        self.activity_count = 0

    def is_any_key_pressed(self):
        for key in self.key_list:
            if win32api.GetAsyncKeyState(key):
                return True

        return False

    def flush_keyboard(self):
        try:
            for _ in range(5):
                self.is_any_key_pressed()
                time.sleep(0.2)
        except pywintypes.error:
            pass

    def on_enabled_start(self):
        self.flush_keyboard()

    def on_disabled_update(self):
        self.flush_keyboard()

    def detect(self):
        try:
            mouse_position = win32api.GetCursorPos()
            mouse_change = mouse_position != self.last_mouse_position
            self.last_mouse_position = mouse_position
            key_pressed = self.is_any_key_pressed()

            if mouse_change or key_pressed:
                self.activity_count += 1
            else:
                self.activity_count = 0

            if self.activity_count >= 5:
                print('Suspicious activities detected.')

                return True

            return False

        except pywintypes.error:
            return False
