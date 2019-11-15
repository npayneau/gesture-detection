# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:03:53 2019

@author: Jules
"""

from tensorflow.keras import layers
from tensorflow.keras import models
import cv2
import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.utils import to_categorical
from time import sleep
from datetime import datetime
import os


#%% Parameters
size=(100,100,3)    #Taille de l'image en entrée
#gestes = {0:"Point fermé",1:"Main ouverte",2:"gauche",3:"droite",4:"haut",5:"bas"}

data_source = r"C:\Users\thieb\Desktop\Data\2 signs"
charge=1  #Pourcentage d'utilisation des données pour éviter les pbs de mémoire
nbmaximagespardossier=300
#%% Functions

def plothistory(history):
    # Plot training & validation accuracy values
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

    # Plot training & validation loss values
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()
    return()


def liste_dossiers(liste):
    liste_dossiers=[]
    for elt in liste:
        if '.' not in elt:
            liste_dossiers.append(elt)
    return(liste_dossiers)

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

def crop(event,x,y,flags,param):
    global xA,yA,xB,yB,drawing,img,img2
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        xA,yA = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            xB,yB = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing=False
    return()
    #%% Camera learning opencv fonction
drawing=True
def capture(geste):
    global xA,xB,yA,yB,drawing
    if geste not in reverselookup:
        lookup[len(lookup)]=geste
        reverselookup[geste]=len(reverselookup)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    taille=np.shape(frame)
    xA,yA,xB,yB = 0,0,taille[1],taille[0]
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',crop)
    imgs=[]
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        img = np.copy(frame)
        cv2.rectangle(img,(xA,yA),(xB,yB),(255,0,0),1)
        cv2.imshow('image',img)
        #print(xA,yA,xB,yB)
        if xA!=xB and yA!=yB:
            img=frame[min(yA,yB):max(yA,yB),min(xA,xB):max(xA,xB),:]
        #frame=cv2.resize(frame,size, interpolation = cv2.INTER_AREA)
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #edges = cv2.Canny(frame,100,200)
        # Display the resulting frame
        #img=rgb2gray(frame)
        #laplacian = cv2.Laplacian(img,cv2.CV_64F)
        img = cv2.resize(img,(size[0],size[1]))
        img=np.array(img)
        #img2=img
        #img=(img>0.6)*np.ones(size)
        cv2.imshow('Capturing...',cv2.resize(img,(500,500)))    #Affichage pixelisé de l'image
        #plt.imshow(x_test2[0],cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
        #plt.show()
        #plt.imshow(img,cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
        #plt.show()
        imgs.append(img)
        #predictions = model.predict(img)
        #print(np.argmax(predictions,axis=1))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    #imgs2=imgs
    x_data=imgs
    y_data=[reverselookup[geste]]*len(imgs)
    return(x_data,y_data)


#plt.imshow(x_test2[0])
#plt.show()

def rgb2gray(rgb):
    G=np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    return(G)



#%% Construction of the dataset
datasets=os.listdir(data_source)

lookup={}
reverselookup={}

X_data = []
Y_data = []
count=0;
di=int(1/charge)

current_dir=data_source
#Création de la liste des gestes
for dataset in datasets:
    print('Exploring '+dataset)
    current_dir = data_source+'\\'+dataset
    dossiers = liste_dossiers(os.listdir(current_dir))
    for d in dossiers:
        print('    Exploring '+d)
        current_dir = data_source+'\\'+dataset+'\\'+d
        noms_gestes=liste_dossiers(os.listdir(current_dir))
        for nom_geste in noms_gestes:
            print('        Exploring '+nom_geste)
            current_dir = data_source+'\\'+dataset+'\\'+d+'\\'+nom_geste
            if nom_geste not in reverselookup:
                lookup[count]=nom_geste
                reverselookup[nom_geste]=count
                count+=1
            fichiers=os.listdir(current_dir)
            n=min(len(fichiers),nbmaximagespardossier)
            for i in range(0,n,di):
                img=cv2.imread(current_dir+'\\'+fichiers[i])
                img=cv2.resize(img,(size[0],size[1]))
                X_data.append(img)
                Y_data.append(reverselookup[nom_geste])

#%% Data from camera
x_data,y_data=capture('Rien')
for i in range(6):
    X_data.extend(x_data)
    Y_data.extend(y_data)


#%%
datacount = len(Y_data)

#Reshaping
X_data = np.array(X_data, dtype = 'float32')
X_data = X_data/255
X_data = X_data.reshape((datacount, size[0],size[1], size[2]))

Y_data = np.array(Y_data)
Y_data = Y_data.reshape(datacount, 1)
Y_data= to_categorical(Y_data)


#Ancien script pour randomizer les images
#r=np.random.permutation(range(nbimages))
#x_train3=[]
#y_train3=[]
#for i in r:
#    x_train3.append(x_train[i])
#    y_train3.append(y_train[i])
#x_train3=np.array(x_train3)
#y_train3=np.array(y_train3)
#x_train3=x_train3.reshape((np.shape(x_train3)[0],np.shape(x_train3)[1],np.shape(x_train3)[2],1))

from sklearn.model_selection import train_test_split
x_train,x_further,y_train,y_further = train_test_split(X_data,Y_data,test_size = 0.1)
x_validate,x_test,y_validate,y_test = train_test_split(x_further,y_further,test_size = 0.5)

#%% Construction of the CNN (convolutional neural network)

model=models.Sequential()
model.add(layers.Conv2D(32, (5, 5), strides=(2,2),activation='relu',input_shape=size))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(len(lookup), activation='softmax'))
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


configuration = model.summary()

#model.load_weights('model.h5')

#%% CNN training
history=model.fit(x_train, y_train, epochs=1, batch_size=30, verbose=1, validation_data=(x_validate, y_validate))
#☺model.fit(X_data,Y_data,epochs=8)

#%% Saving and plotting training results
#now = datetime.now()
#now = now.strftime("%D"+"  %Hh%Mm%Ss").replace('/','-')
model.save('model1.h5')
plothistory(history)
#print('ok')

#%% Test on real time






#from pywinauto.application import Application
#app = Application()
#app.connect(path=r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE")
## describe the window inside NoteUntitledNotepad.exe process
#window = app.top_window()







cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 30)
fps = int(cap.get(5))
print("fps:", fps)

#ret, frame = cap.read()
#taille=np.shape(frame)
#xA,yA,xB,yB = 0,0,taille[1],taille[0]
#cv2.namedWindow('image')
#cv2.setMouseCallback('image',crop)
ancien_geste=""
while(1):
    ret, frame = cap.read()
    img = np.copy(frame)
    cv2.rectangle((frame),(xA,yA),(xB,yB),(255,0,0),1)
    cv2.imshow('image',img)
#    print(xA,yA,xB,yB)
    if xA!=xB and yA!=yB:
        img=frame[min(yA,yB):max(yA,yB),min(xA,xB):max(xA,xB),:]
    img = cv2.resize(img,(size[0],size[1]))
    img = np.array(img)
    #img2=img
    #img=(img>0.6)*np.ones(size)
    #plt.imshow(x_test2[0],cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    #plt.show()
    #plt.imshow(img,cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    #plt.show()
    #predictions = model.predict(img)
    #print(np.argmax(predictions,axis=1))
    img = img*1.0
    predictions = model.predict(img.reshape((1,size[0],size[1],size[2])))
    geste=lookup[np.argmax(predictions[0])]
    proba=max(predictions[0])
    #print(geste+':'+str(proba)[:4],end=' ')
    img_affichee = img
    img_affichee = cv2.resize(img_affichee,(500,500))    #Affichage pixelisé de l'image
    #print(predictions)
    cv2.putText(img_affichee,geste,(size[0],size[1]),0, 2, (255,0,255),2)
    #geste+':'+str(proba)[:4]
    cv2.imshow("Detection",img_affichee)
#    act(geste,ancien_geste)
#    ancien_geste=geste
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()