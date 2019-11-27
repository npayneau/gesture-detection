# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:14:45 2019

@author: Jules
"""


from pywinauto.application import Application

app = Application()
app.connect(path=r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE")
# describe the window inside NoteUntitledNotepad.exe process
window = app.top_window()


def controle(order):
    global window
    if order=='open':
        window.type_keys("{F5}")
    elif order=="close":
        window.type_keys("{ESC}")
    return()

def act(geste,ancien_geste):
    if geste!=ancien_geste:
        if geste=='Main':
            controle('open')
        elif geste=='Poing':
            controle('close')
        elif geste=="Rien":
            controle('nothing')
    return()
