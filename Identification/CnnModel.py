# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:37:23 2019

@author: Jules
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.models import load_model


class CnnModel():

    def __init__(self, model=None, lookup=None, size=(100, 100, 3)):
        self.size = size
        self.lookup = lookup
        if model is None:
            self.construct_model()
        else:
            self.model = load_model(model)

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
        #plothistory(history)
        return (None)

    def predict(self, image):
        img = cv2.resize(image, (self.size[0], self.size[1]))
        img = np.array(img)
        img = img * 1.0 / 255
        predictions = self.model.predict(img.reshape((1, self.size[0], self.size[1], self.size[2])))
        geste = self.lookup[np.argmax(predictions[0])]
        return (geste)
