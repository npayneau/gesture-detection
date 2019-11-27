# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:54:15 2019

@author: thieb
"""

#%% Imports
from tensorflow.keras.models import load_model
import cv2
import numpy as np
import crop_image as cim
import powerpoint_api as pw
import pickle

#%% Parameters
size=(100,100,3)

model = load_model('model.h5')

lookup = pickle.load(open("lookup.pickle", "rb"))

camera=0
#%% Cropping the image

yA,yB,xA,xB = cim.crop_current_image(camera, True)

#%% Video Capture
def video_predict(camera=0,resize = False):
    cap = cv2.VideoCapture(camera)
    ancien_geste=""
    while(True):
        ret, frame = cap.read()
        cap.set(cv2.CAP_PROP_FPS, 30)
        if ret:
            if resize:
                frame = cv2.resize(frame,(1280,1024))
            img = np.copy(frame)

            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 1)
            cv2.imshow('image', frame)


            if xA!=xB and yA!=yB:
                img=img[yA:yB,xA:xB,:]

            img = cv2.resize(img,(size[0],size[1]))
            img = np.array(img)

            img2 = img*1.0
            predictions = model.predict(img2.reshape((1,size[0],size[1],size[2])))
            geste=lookup[np.argmax(predictions[0])]

            img_affichee = img
            img_affichee = cv2.resize(img_affichee,(800,700))    #Affichage pixelisé de l'image
            cv2.putText(img_affichee,geste,(size[0],size[1]),0, 2, (255,0,255),2)
            cv2.imshow("Detection",img_affichee)

            ancien_geste=geste
            pw.act(ancien_geste,geste,controller=pw.controlPlayer)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

#%%

video_predict(camera, True)