# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:14:45 2019

@author: Jules
"""
from pywinauto.application import Application
import time

app = Application()
app.connect(path=r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE")
# describe the window inside NoteUntitledNotepad.exe process
window = app.top_window()
last_acted=time.time()

def controle(order):
    global app
    window = app.top_window()
    print(order)
    if order=='open':
        window.type_keys("{F5}")
    elif order=="close":
        window.type_keys("{ESC}")
#    elif order=="rien":
#        print("Rien")
    elif order=="next":
        window.type_keys("{UP}")
    elif order=="previous":
        window.type_keys("{DOWN}")
    elif order=='blur':
        window.type_keys("B")
    return(None)

def act(geste,ancien_geste):
    global last_acted
    if time.time()-last_acted>2 or ancien_geste=="Rien" or geste=="Rien":
        last_acted=time.time()
        if geste=='Main Ouverte':
            controle('open')
        elif geste=='Poing':
            #controle('close')
            print("stop")
        elif geste=="Rien":
            controle('rien')
        elif geste=="Doigt 1":
            controle("next")
        elif geste=="Pouce Haut":
            controle("previous")
        elif geste=="2 Doigts":
            controle('blur')
    return(None)