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
        """
        Initialisation du dataset
        :param size: taille des images en entree du CNN
        :param batchsize: taille (nombre d'images dans chaque batch)
        """
        self.size = size
        self.dataframe = []
        self.lookup = {}
        self.batchiterator = None
        self.batchsize = batchsize

    def compile(self, **kwargs):
        """
        Créée un itérateur sur l'ensemble des images du dataset.
        :param kwargs: spécification des options de ImageDataGenerator
        """
        datagen = ImageDataGenerator(**kwargs)
        iterator = datagen.flow_from_dataframe(self.dataframe, x_col="chemin", y_col="nom_geste",
                                               batch_size=self.batchsize,
                                               target_size=(self.size[0], self.size[1]))
        return (iterator)

    def reload(self):
        self.load(self.path, self.charge, self.maxpardossier)

    def load(self, dataset_name, charge=1., maxpardossier=1000,
             dataset_path=os.path.join("data", "datasets")
             ):
        """
        Charge les images du dossier spécifié selon les paramètres charge et maxpardossier, excepté les images dont le dossier parent contient '.'.
        :param dataset_name: nom du dataset
        :param charge: pourcentage d'images chargées par dossier
        :param maxpardossier: nombre maximal d'images utlisées par dossier
        :param dataset_path: chemin vers le dossier contenant l'ensemble des datasets
        """
        self.path = os.path.join(dataset_path, dataset_name)
        self.maxpardossier = maxpardossier
        self.charge = charge

        def ends(file_path, extensions=self.extensions):
            for e in extensions:
                if file_path.endswith(e):
                    return (True)
            return (False)

        data = []
        for i in os.walk(self.path):
            if '.' not in i[0] and i[1] == []:
                name = i[0].split("\\")[-1]
                fichiers = i[2][0:maxpardossier:int(1 / charge)]
                count = 0
                for j in fichiers:
                    if ends(j, self.extensions):
                        data.append((name, i[0] + '\\' + j))
                        count += 1
                if count > 0:
                    if name not in self.lookup.items():
                        indice = len(self.lookup)
                        self.lookup[indice] = name
        self.dataframe = pd.DataFrame(data, columns=['nom_geste', 'chemin'])
        return (None)

    def add(self, images, geste):
        """
        Enregistre la liste d'images dans un sous-dossier du dataset (dont le nom est composé du geste)
        """
        now = datetime.now()
        now = now.strftime("%D" + "  %Hh%Mm").replace('/', '-')
        destination = os.path.join(self.path, now, geste)
        os.makedirs(destination)
        for i in range(len(images)):
            cv2.imwrite(os.path.join(destination, str(i) + '.jpg'), img=images[i])
        self.reload()
        return (None)
