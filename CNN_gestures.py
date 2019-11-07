# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:03:53 2019

@author: Jules
"""

from keras import layers
from keras import models
import cv2
import numpy as np
from matplotlib import pyplot as plt
from keras.utils import to_categorical
from time import sleep
from datetime import datetime


#%% Parameters
size=(100,100,3)	#Taille de l'image en entrée
#gestes = {0:"Point fermé",1:"Main ouverte",2:"gauche",3:"droite",4:"haut",5:"bas"}
gestes = {0:"1D",1:"2D",2:"3D",3:"rien"}



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


#%% Camera learning opencv fonction

def capture(indice):
    cap = cv2.VideoCapture(0)
    imgs=[]
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #frame=cv2.resize(frame,size, interpolation = cv2.INTER_AREA)
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #edges = cv2.Canny(frame,100,200)
        # Display the resulting frame
        #img=rgb2gray(frame)
        #laplacian = cv2.Laplacian(img,cv2.CV_64F)
        img = cv2.resize(frame,(size[0],size[1]))
        img=np.array(img)
        #img2=img
        #img=(img>0.6)*np.ones(size)
        cv2.imshow('Capturing...',cv2.resize(img,(500,500)))	#Affichage pixelisé de l'image
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
    y_data=[indice]*len(imgs)
    return(x_data,y_data)


#plt.imshow(x_test2[0])
#plt.show()

def rgb2gray(rgb):
    G=np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    return(G)

#%% Construction of the dataset
nbGestes = len(gestes)

X_data = []
Y_data = []

for i in range(2):
	for g in gestes:
		print("Capturing "+gestes[g])
		sleep(2.)
		x_data,y_data=capture(g)
		X_data+=x_data
		Y_data+=y_data
	
	
	
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
x_train,x_further,y_train,y_further = train_test_split(X_data,Y_data,test_size = 0.2)
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
model.add(layers.Dense(nbGestes, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


configuration = model.summary()

#model.load_weights('model.h5')

#%% CNN training
history=model.fit(x_train, y_train, epochs=5, batch_size=30, verbose=1, validation_data=(x_validate, y_validate))
#☺model.fit(X_data,Y_data,epochs=8)

#%% Saving and plotting training results
now = datetime.now()
now = now.strftime("%D"+"  %Hh%Mm%Ss").replace('/','-')
model.save_weights('models/'+str(now)+'.h5')
plothistory(history)
#print('ok')

#%% Test on real time

imgs=[]

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 10)
fps = int(cap.get(5))
print("fps:", fps)

while(True):
	ret, frame = cap.read()
	#frame=cv2.resize(frame,size, interpolation = cv2.INTER_AREA)
	# Our operations on the frame come here
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#edges = cv2.Canny(frame,100,200)
	# Display the resulting frame
	#img=rgb2gray(frame)
	#laplacian = cv2.Laplacian(img,cv2.CV_64F)
	img = cv2.resize(frame,(size[0],size[1]))
	img=np.array(img)
	#img2=img
	#img=(img>0.6)*np.ones(size)
	#plt.imshow(x_test2[0],cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
	#plt.show()
	#plt.imshow(img,cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
	#plt.show()
	imgs.append(img)
	#predictions = model.predict(img)
	#print(np.argmax(predictions,axis=1))	
	predictions = model.predict(img.reshape((1,size[0],size[1],size[2])))
	geste=gestes[np.argmax(predictions[0])]
	proba=max(predictions[0])
	#print(geste+':'+str(proba)[:4],end=' ')
	img_affichee = img
	img_affichee = cv2.resize(img_affichee,(500,500))	#Affichage pixelisé de l'image
	cv2.putText(img_affichee,geste+':'+str(proba)[:4],(size[0],size[1]),0, 2, (255,0,255),2)
	cv2.imshow("Detection",img_affichee)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()