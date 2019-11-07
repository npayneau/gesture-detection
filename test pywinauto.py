# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:52:38 2019

@author: Jules
"""

from pywinauto.application import Application
app = Application()
app.connect(path=r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE")
# describe the window inside NoteUntitledNotepad.exe process
window = app.top_window()
# wait till the window is really open
dialogs = app.windows() 
controls=window.print_control_identifiers()
window.type_keys("{F5}")
window = app.top_window()
window.type_keys("{DOWN 1}")