# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:56:07 2019

@author: thieb
"""

#%% Imports

import cv2
import crop_image as cim
import pickle
import os
import numpy as np
import time
from datetime import datetime

#%% Parameters
camera = 0
yA, yB, xA, xB = cim.crop_current_image(camera, True)
size = (100, 100, 3)
lookup = pickle.load(open("lookup.pickle", "rb"))
CATEGORIES = list(lookup.values())
reverselookup = pickle.load(open("reverselookup.pickle", "rb"))
current_path = os.getcwd()
data_source = os.path.join(current_path, "Dataset")
now = datetime.now()
now = now.strftime("%D"+"  %Hh%Mm%Ss").replace('/','-')
data_source=os.path.join(data_source,now)

def capture(camera=0, resize = False):
    global xA, xB, yA, yB
    cap = cv2.VideoCapture(camera)
    cap.set(cv2.CAP_PROP_FPS, 5)
    # On Créé un dataset pour chaque geste
    for i in CATEGORIES :
        directory = os.path.join(data_source, i)
        if not os.path.exists(directory):
            os.makedirs(directory)
        print("Prepare yourself to do the gesture " + i + "...")
        print("Start is in 5 seconds")
        time.sleep(5)
        start_time = time.time()
        current_time = time.time()
        while (current_time - start_time)<20:
            ret, frame = cap.read()
            if not ret:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if resize:
                frame = cv2.resize(frame, (1280, 1024))
            img = np.copy(frame)
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 1)
            cv2.imshow('Capturing...', frame)
            if xA != xB and yA != yB:
                img = img[min(yA, yB):max(yA, yB), min(xA, xB):max(xA, xB), :]
#            img = cv2.resize(img,(size[0],size[1]))
            img = cv2.resize(img, (700,600))
            cv2.imshow("Capturing....", img)
            cv2.imwrite(os.path.join(directory, str(current_time)+'.jpg'), img=img)
            current_time = time.time()
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


#%% Calling the function

capture(camera, True)

