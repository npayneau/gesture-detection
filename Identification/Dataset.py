# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:32:43 2019

@author: Jules
"""
import os
from datetime import datetime

import cv2
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator


class Dataset:
    extensions = ['.png', '.jpg']

    def __init__(self, size=(100, 100, 3), batchsize=32):
        self.size = size
        self.dataframe = []
        self.lookup = {}
        self.reverselookup = {}
        self.batchiterator = None
        self.batchsize = batchsize

    def compile(self, **kwargs):
        """Returns an iterator over all the images of the dataset"""

        datagen = ImageDataGenerator(rescale=1. / 255, **kwargs)
        iterator = datagen.flow_from_dataframe(self.dataframe, x_col="chemin", y_col="nom_geste",
                                               batch_size=self.batchsize,
                                               target_size=(self.size[0], self.size[1]))
        return (iterator)

    def reload(self):
        self.load(self.path, self.charge, self.maxpardossier)

    def load(self, data_path="Dataset2", charge=1, maxpardossier=1000):
        self.path = data_path
        self.maxpardossier = maxpardossier
        self.charge = charge

        def ends(file_path, extensions=self.extensions):
            for e in extensions:
                if file_path.endswith(e):
                    return (True)
            return (False)

        data = []
        for i in os.walk(data_path):
            if '.' not in i[0] and i[1] == []:
                name = i[0].split("\\")[-1]
                fichiers = i[2][0:maxpardossier:int(1 / charge)]
                count = 0
                for j in fichiers:
                    if ends(j, self.extensions):
                        data.append((name, i[0] + '\\' + j))
                        count += 1
                if count > 0:
                    if name not in self.reverselookup:
                        indice = len(self.reverselookup)
                        self.lookup[indice] = name
                        self.reverselookup[name] = indice
        self.dataframe = pd.DataFrame(data, columns=['nom_geste', 'chemin'])
        return (None)

    def add(self, images, geste):
        now = datetime.now()
        now = now.strftime("%D" + "  %Hh%Mm").replace('/', '-')
        destination = os.path.join(self.path, now, geste)
        os.makedirs(destination)
        for i in range(len(images)):
            cv2.imwrite(os.path.join(destination, str(i) + '.jpg'), img=images[i])
        self.reload()
        return (None)
