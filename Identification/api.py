# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:14:45 2019

@author: Jules
"""
from pywinauto.application import Application
import pywinauto.keyboard as kb
import time
import pyautogui as pag

first_call=True
app=None

last_acted=time.time()

def controlPlayer(order):
    global first_call
    if first_call:
        app=None
        first_call=False
    print(order)
    if order=='open':
        pag.press("playpause")
    elif order=="close":
        pag.press("volumemute")
#    elif order=="rien":
#        print("Rien")
    elif order=="next":
        pag.press("nexttrack")
    elif order=="previous":
        pag.press("prevtrack")
    elif order=='blur':
        pag.press("volumedown")
    return(None)

def controlPPT(order):
    global first_call,app
    if first_call:
        app = Application()
        app.connect(path=r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE")
        # print(app.windows())
        # describe the window inside NoteUntitledNotepad.exe process
        window = app.top_window()
        first_call=False
    else:
        window = app.top_window()
    print(order)
    if order=='open':
        window.type_keys("{F5}")
    elif order=="close":
        window.type_keys("{ESC}")
    elif order=="next":
        window.type_keys("{DOWN}")
    elif order=="previous":
        window.type_keys("{UP}")
    elif order=='blur':
        window.type_keys("b")
    return(None)

def act(geste,ancien_geste,controller=controlPPT):
    global last_acted
    if time.time()-last_acted>1 or ancien_geste=="Rien" or geste=="Rien":
        last_acted=time.time()
        if geste=='Main Ouverte':
            controller('open')
        elif geste=='Poing':
            controller('close')
        elif geste=="Rien":
            controller('rien')
        elif geste=="Doigt 1":
            controller("next")
        elif geste=="Pouce Haut":
            controller("previous")
        elif geste=="2 Doigts":
            controller('blur')
    return(None)