# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:32:43 2019

@author: Jules
"""
import os
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import cv2
import progressbar

class Dataset():
    extensions=['.png','.jpg']
    def __init__(self, size=(100,100,3)):
        self.size=size
        self.data_source=""
        self.data=[]
        self.lookup={}
        self.reverselookup={}
        self.X_data=[]
        self.Y_data=[]
        return(None)
    def load(self,data_path="Dataset",charge=1,maxpardossier=1000)
        self.data_source=data_path
        self.charge=charge
        self.maxpardossier=maxpardossier
        count=0;
        di=int(1/charge)
        for i in os.walk(self.data_source):
            if '.' not in i[0] and i[1]==[]:
                name=i[0].split("\\")[-1]
                fichiers=i[2][0:self.maxpardossier:int(1/self.charge)]
                count=0
                for j in fichiers:
                    if ends(j,extensions):
                        self.data.append((name,i[0]+'\\'+j))
                        count+=1
                if count>0:
                    if name not in reverselookup:
                        indice=len(reverselookup)
                        self.lookup[indice]=name
                        self.reverselookup[name]=indice
        X_data=[]
        Y_data=[]
        bar = progressbar.ProgressBar(maxval=len(self.data))
        bar.start()
        i=0
        for y_data,x_data in self.data:
            self.Y_data.append(reverselookup[y_data])
            self.X_data.append(cv2.resize(cv2.imread(x_data),(size[0],size[1])))
            i+=1
            bar.update(i)

        datacount = len(data)

        X_data = np.array(X_data, dtype = 'float32')
        X_data = X_data/255
        X_data = X_data.reshape((datacount, size[0],size[1], size[2]))

        Y_data = np.array(Y_data)
        Y_data = Y_data.reshape(datacount, 1)
        Y_data= to_categorical(Y_data)
        return(None)
    def ends(file_path,extensions=extensions):
        for e in extensions:
            if file_path.endswith(e):
                return(True)
        return(False)
    def split(self):
        x_train,x_further,y_train,y_further = train_test_split(self.X_data,self.Y_data,test_size = 0.1)
        x_dev,x_test,y_dev,y_test = train_test_split(x_further,y_further,test_size = 0.5)
        return(x_train,x_test,x_dev,y_train,y_test,y_dev)


