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
from tensorflow.keras.backend import get_session
from tensorflow.keras.backend import set_session
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.models import load_model
from tensorflow.keras.models import save_model
from tensorflow import global_variables_initializer


class CnnModel:
    def __init__(self, model_name="", size=(100, 100, 3), models_directory=os.path.join("data", "models")):
        self.size = size
        self.lookup = pd.read_pickle(os.path.join(models_directory, model_name + "-lookup.pickle"))
        self.session = get_session()
        init = global_variables_initializer()
        self.session.run(init)
        if model_name == "":
            self.construct_model()
        else:
            self.model = load_model(os.path.join(models_directory, model_name + ".h5"))
        self.graph = get_default_graph()
        print(self.graph)

    def construct_model(self):
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
            return ()

        history = self.model.fit_generator(batchiterator, epochs=epochs)
        # plothistory(history)
        return (None)

    def predict(self, image):
        img = cv2.resize(image, (self.size[0], self.size[1]))
        img = np.array(img)
        img = img * 1.0/255
        with self.graph.as_default():
            set_session(self.session)
            predictions = self.model.predict(img.reshape((1, self.size[0], self.size[1], self.size[2])))
        geste = self.lookup[np.argmax(predictions[0])]
        return (geste)

    def save(self, model_name, directory=os.path.join("data", "models")):
        save_model(self.model, os.path.join(directory, model_name + ".h5"))
        pd.to_pickle(self.lookup, os.path.join(directory, model_name + "-lookup.pickle"))
        now = datetime.now()
        now = now.strftime("%D" + "  %Hh%Mm%Ss").replace('/', '-')
        save_model(self.model, os.path.join(directory, "backups", now + ".h5"))
        pd.to_pickle(self.lookup, os.path.join(directory, "backups", now + "-lookup.pickle"))
        return (0)
