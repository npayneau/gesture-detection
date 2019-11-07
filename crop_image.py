# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:33:18 2019

@author: Jules
"""

import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in  i]
#print(events)

import numpy as np

size=(500,500)
drawing = False # true if mouse is pressed


# mouse callback function
def crop(event,x,y,flags,param):
    global xA,yA,xB,yB,drawing,img,img2   
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        img2=np.copy(img)
        xA,yA = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            xB,yB = x,y
            img2=np.copy(img)
            print("y")         
    elif event == cv2.EVENT_LBUTTONUP:
        drawing=False
        
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 30)
fps = int(cap.get(5))
print("fps:", fps)
ret, frame = cap.read()
taille=np.shape(frame)
xA,yA,xB,yB = 0,0,taille[1],taille[0]
cv2.namedWindow('image')
cv2.setMouseCallback('image',crop)

while(1):
    ret, frame = cap.read()
    img = np.copy(frame)
    img2=np.copy(img)
    cv2.rectangle(img2,(xA,yA),(xB,yB),(255,0,0),1)
    cv2.imshow('image',img2)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    print(xA,yA,xB,yB)
cv2.destroyAllWindows()