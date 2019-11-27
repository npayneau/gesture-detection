# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:13:27 2019

@author: thieb
"""

#%% Imports
import cv2
import numpy as np
from tensorflow.keras.utils import to_categorical
import os
from sklearn.model_selection import train_test_split

#%%Parameters
size=(100,100,3)    #Taille de l'image en entrée

data_source = r".\data"

#data_source = r"C:\Users\thieb\Desktop\Data\2 signs"

CATEGORIES = ["Poing","Doigt 1","Main Ouverte","2 Doigts","Rien"]


datasets=os.listdir()

# Hashmap lookup : keys are the training example"s number and the values are the gestures
lookup={}

#Hashmap reverselookup : keys are the gestures, the values are the training example's number
reverselookup={}

X_data = []
Y_data = []
count=0

#%%Used Functions

def liste_dossiers(liste):
    liste_dossiers=[]
    for elt in liste:
        if '.' not in elt:
            liste_dossiers.append(elt)
    return(liste_dossiers)

#%% Dataset Creation

datasets=os.listdir(data_source)

lookup={}
reverselookup={}

X_data = []
Y_data = []
count=0;
di=1

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
        for nom_geste in CATEGORIES:
#            if nom_geste in CATEGORIES :
            print('        Exploring '+nom_geste)
            current_dir = data_source+'\\'+dataset+'\\'+d+'\\'+nom_geste
            if nom_geste not in reverselookup:
                lookup[count]=nom_geste
                reverselookup[nom_geste]=count
                count+=1
#            n=min(len(fichiers),nbmaximagespardossier)
            fichiers=os.listdir(current_dir)
            for img in fichiers:
                try:
                    img2=cv2.imread(current_dir+"\\"+img)
                    img2=cv2.resize(img2,(size[0],size[1]))
                    X_data.append(img2)
                    Y_data.append(reverselookup[nom_geste])
                except:
                    pass


#%% Reshaping the dataset


datacount = len(Y_data)
print(datacount)

X_data = np.array(X_data, dtype = 'float32')
X_data = X_data/255
X_data = X_data.reshape((datacount, size[0],size[1], size[2]))

Y_data = np.array(Y_data)
Y_data = Y_data.reshape(datacount, 1)
Y_data= to_categorical(Y_data)

x_train,x_further,y_train,y_further = train_test_split(X_data,Y_data,test_size = 0.2)
x_dev,x_test,y_dev,y_test = train_test_split(x_further,y_further,test_size = 0.5)



#%% Saving the dataset

import pickle

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
