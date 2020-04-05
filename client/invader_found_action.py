import os
import ctypes
import win32com.client as win32
import win32ui

from playsound import playsound


def play_audio(filepath):
    playsound(filepath)


def email_culprit(image_path):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    # Add your email group here
    mail.To = 'example@server.com'
    mail.Subject = 'PC pirate culprit is found!'
    mail.Body = 'Over the past few weeks, PC pirates have been invading countless innocent programming monkeys\' ' + \
                'desktop, which ruins our serenity. Today, we finally catch the culprit! Please see attachment for ' + \
                'his lovely face.'

    attachment = image_path
    mail.Attachments.Add(attachment)

    mail.Send()


def on_invader_found():

    ctypes.windll.user32.LockWorkStation() #lock screen


try:
    import cv2
    def on_invader_found_with_image(image):
        print('Invader found. Lock screen')
        culprit_image_path = 'culprit.png'
        cv2.imwrite(culprit_image_path, image)
        # email_culprit(os.path.join(os.getcwd(), culprit_image_path))
        ctypes.windll.user32.LockWorkStation()
        play_audio(os.path.join('audio', 'invader_found_alarm.wav'))
except:
    pass