import tkinter as tk
from tkinter import ttk
from multiprocessing import Process
from random import randrange

LARGE_FONT= ("Verdana", 24)
NORM_FONT = ("Helvetica", 20)
SMALL_FONT = ("Helvetica", 16)


def popupmsg(msg): 
    
    for i in range(40):
        x = str(randrange(100, 1000))
        y = str(randrange(100, 1000))
        geo = "300x300" + "+"+ x + "+" +y
        popup = tk.Tk()
        popup.geometry(geo)
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg, font=NORM_FONT, anchor="center")
        label.pack(side="top", fill="x", pady=10)
    popup.mainloop()

