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
#%% Parameters

yA,yB,xA,xB = cim.crop_current_image()
size = (100,100,3)
CATEGORIES = ["Poing","Doigt 1","Main Ouverte","2 Doigts","Rien"]
lookup = pickle.load(open("lookup.pickle", "rb"))
reverselookup = pickle.load(open("reverselookup.pickle", "rb"))
current_path = os.getcwd()
data_source = os.path.join(current_path,"Dataset")
data_source = os.path.join(data_source,"Nous")
data_source = os.path.join(data_source,"Kevin")

def capture():
    global xA, xB, yA, yB
    cap = cv2.VideoCapture(0)
    cnt = 0
    # On Créé un dataset pour chaque geste
    for i in CATEGORIES :
        directory = data_source + '\\' + i
        os.chdir(directory)
        print("Prepare yourself to do the gesture " + i + "...")
        print("Start is in 5 seconds")
        time.sleep(5)
        start_time = time.time()
        current_time = time.time()
        while (current_time - start_time)<20:
            ret, frame = cap.read()
            if ret == False:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            img0 = np.copy(frame)
            cv2.rectangle(img0,(xA,yA),(xB,yB),(0,255,0),1)
            cv2.imshow('Capturing...',img0)
            img = np.copy(frame)
            if xA!=xB and yA!=yB:
                img=img[min(yA,yB):max(yA,yB),min(xA,xB):max(xA,xB),:]
#            img = cv2.resize(img,(size[0],size[1]))
            img = cv2.resize(img,(1000,1000))
            cv2.imshow("Capturing....",img)
            cv2.imwrite(filename='super'+str(cnt)+'.jpg',img = img)
            cnt+=1
            current_time = time.time()
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


#%% Calling the function

capture()

