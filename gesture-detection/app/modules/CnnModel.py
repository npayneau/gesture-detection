# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:37:23 2019

@author: Jules
"""
import os
from datetime import datetime

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tensorflow import get_default_graph
from tensorflow import global_variables_initializer
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.backend import get_session
from tensorflow.keras.backend import set_session
from tensorflow.keras.models import load_model
from tensorflow.keras.models import save_model


class CnnModel:
    def __init__(self, model_name="", size=(100, 100, 3), models_directory=os.path.join("data", "models")):
        """
        Charge/ Créée un modèle Keras muni d'une taille et d'un dictionnaire de gestes
        :param model_name: nom du modèle à charger, s'il n'y en a pas, un nouveau modèle est créé
        :param size: taille des images (entrée du réseau de neurones)
        :param models_directory: chemin vers le dossier des modèles
        :type model_name: str
        :type size: tuple
        :type models_directory: str
        """
        self.name = model_name
        self.size = size
        # Chaque modèle a un fichier -lookup.pickle associé
        self.lookup = pd.read_pickle(os.path.join(models_directory, model_name + "-lookup.pickle"))
        # On sauvegarde la session, le graphe et les paramètres globaux de tensorflow afin de supprimer les conflits entre flask et tensorflow sous windows
        self.session = get_session()
        init = global_variables_initializer()
        self.session.run(init)
        # Chargement/ Création du modèle s'il est vide
        if model_name == "":
            self.construct_model()
        else:
            self.model = load_model(os.path.join(models_directory, model_name + ".h5"))
        self.graph = get_default_graph()

    def construct_model(self):
        """
        Permet de construire un CNN en repartant de zéro (modèle utilisé au départ)
        """
        model = models.Sequential()
        model.add(layers.Conv2D(32, (5, 5), strides=(2, 2), activation='relu', input_shape=self.size))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(len(self.lookup), activation='softmax'))
        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        configuration = model.summary()
        self.model = model
        return (None)

    def train(self, batchiterator, epochs, **kwargs):
        def plothistory(history):
            """
            Permet d'afficher les graphes de l'accuracy et de loss
            :param history: variable renvoyée par un model.fit de Keras
            """
            # Plot training & validation accuracy values
            plt.plot(history.history['acc'])
            plt.plot(history.history['val_acc'])
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
            return (None)

        history = self.model.fit_generator(batchiterator, epochs=epochs)
        # affichage de l'accuracy
        # plothistory(history)
        return (None)

    def predict(self, image):
        """
        Permet de prédire une image donnée
        :param image: image à prédire, redimensionnement automatique selon la taille d'entrée du réseau
        :return: geste prédit par le réseau
        """
        img = cv2.resize(np.array(image), (self.size[0], self.size[1]))
        img = np.array(img)
        img = img * 1.0 / 255
        with self.graph.as_default():
            set_session(self.session)
            predictions = self.model.predict(img.reshape((1, self.size[0], self.size[1], self.size[2])))
        geste = self.lookup[np.argmax(predictions[0])]
        return (geste)

    def save(self, model_name, directory=os.path.join("data", "models")):
        """
        Permet de sauvegarder le modèle Keras ainsi que son fichier -lookup.pickle associé dans le répertoire directory, sous le nom model_name
        """
        save_model(self.model, os.path.join(directory, model_name + ".h5"))
        pd.to_pickle(self.lookup, os.path.join(directory, model_name + "-lookup.pickle"))
        now = datetime.now()
        now = now.strftime("%D" + "  %Hh%Mm%Ss").replace('/', '-')
        save_model(self.model, os.path.join(directory, "backups", now + ".h5"))
        pd.to_pickle(self.lookup, os.path.join(directory, "backups", now + "-lookup.pickle"))
        return (0)
