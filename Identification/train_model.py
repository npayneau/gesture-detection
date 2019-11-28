import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.models import load_model
import pickle
import os
import numpy as np
from datetime import datetime
import  matplotlib.pyplot as plt


size = (100, 100, 3)

def plothistory(history):
    # Plot training & validation acc values
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('acc')
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


X_train = pickle.load(open("X_train.pickle", "rb"))
y_train = pickle.load(open("y_train.pickle", "rb"))
X_test = pickle.load(open("X_test.pickle", "rb"))
y_test = pickle.load(open("y_test.pickle", "rb"))
X_dev = pickle.load(open("X_dev.pickle", "rb"))
y_dev = pickle.load(open("y_dev.pickle", "rb"))
lookup = pickle.load(open("lookup.pickle", "rb"))
reverselookup = pickle.load(open("reverselookup.pickle", "rb"))

if not os.path.exists('model.h5'):
    model=models.Sequential()
    model.add(layers.Conv2D(32, (5, 5), strides=(2,2),activation='relu',input_shape=size))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(len(lookup), activation='softmax'))
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    configuration = model.summary()

else:
    model = load_model('model1.h5')

configuration = model.summary()

history=model.fit(X_train, y_train, epochs=10, batch_size=1024, verbose=1, validation_data=(X_dev, y_dev))

#%% Affichage accuracy

now = datetime.now()
now = now.strftime("%D"+"  %Hh%Mm%Ss").replace('/','-')
model.save(os.getcwd()+'\\models\\'+str(now)+'.h5')
model.save(os.getcwd()+'\\model1.h5')
plothistory(history)


