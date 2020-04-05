import ctypes
import os

def changeVirus(index):
    image = ['1', '2', '3', '4', '5']
    SPI_SETDESKWALLPAPER = 20     #which command (20)

    SPIF_UPDATEINIFILE   = 0x2 #forces instant update
    dirpath = os.getcwd()
  
    src = os.path.join(dirpath, image[index] + ".jpg")
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINIFILE)
