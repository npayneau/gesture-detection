# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 10:15:53 2019

@author: Jules

Can explore a specified folder (data_source) to create a tensorflow dataset.
This dataset is saved by pickle
"""
import os
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import cv2
import progressbar

#%% Parameters
current_path=os.getcwd()
data_source = os.path.join(current_path,"Dataset")

charge=1  #Pourcentage d'utilisation des données pour éviter les pbs de mémoire
nbmaximagespardossier=1000
extensions=['.png','.jpg']

size=(100,100,3)
#%% Exploring the dataset files

def ends(file,extensions):
    for e in extensions:
        if file.endswith(e):
            return(True)
    return(False)

data=[]#No data

lookup={}
reverselookup={}

count=0;
di=int(1/charge)

current_dir=data_source
#Création de la liste des gestes
data=[]
for i in os.walk(data_source):
    if '.' not in i[0] and i[1]==[]:
        name=i[0].split("\\")[-1]
        fichiers=i[2][0:nbmaximagespardossier:int(1/charge)]
        count=0
        for j in fichiers:
            if ends(j,extensions):
                data.append((name,i[0]+'\\'+j))
                count+=1
        if count>0:
            if name not in reverselookup:
                indice=len(reverselookup)
                lookup[indice]=name
                reverselookup[name]=indice
X_data=[]
Y_data=[]

bar = progressbar.ProgressBar(maxval=len(data))
bar.start()
i=0
for y_data,x_data in data:
    Y_data.append(reverselookup[y_data])
    X_data.append(cv2.resize(cv2.imread(x_data),(size[0],size[1])))
    i+=1
    bar.update(i)

#%% Reshaping the dataset

datacount = len(data)

X_data = np.array(X_data, dtype = 'float32')
X_data = X_data/255
X_data = X_data.reshape((datacount, size[0],size[1], size[2]))

Y_data = np.array(Y_data)
Y_data = Y_data.reshape(datacount, 1)
Y_data= to_categorical(Y_data)

x_train,x_further,y_train,y_further = train_test_split(X_data,Y_data,test_size = 0.1)
x_dev,x_test,y_dev,y_test = train_test_split(x_further,y_further,test_size = 0.5)

#%% Saving the dataset

pickle_out = open("X_test.pickle", "wb")
pickle.dump(x_test, pickle_out)
pickle_out.close()

pickle_out = open("X_train.pickle", "wb")
pickle.dump(x_train, pickle_out)
pickle_out.close()

pickle_out = open("X_dev.pickle", "wb")
pickle.dump(x_dev, pickle_out)
pickle_out.close()

pickle_out = open("y_train.pickle", "wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()

pickle_out = open("y_test.pickle", "wb")
pickle.dump(y_test, pickle_out)
pickle_out.close()

pickle_out = open("y_dev.pickle", "wb")
pickle.dump(y_dev, pickle_out)
pickle_out.close()

pickle_out = open("lookup.pickle","wb")
pickle.dump(lookup, pickle_out)
pickle_out.close()

pickle_out = open("reverselookup.pickle","wb")
pickle.dump(reverselookup, pickle_out)
pickle_out.close()