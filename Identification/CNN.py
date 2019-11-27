import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
import pickle
import numpy as np

IMG_SIZE = 100  #50

X_train = pickle.load(open("X_train.pickle", "rb"))
y_train = pickle.load(open("y_train.pickle", "rb"))
X_test = pickle.load(open("X_test.pickle", "rb"))
y_test = pickle.load(open("y_test.pickle", "rb"))
X_dev = pickle.load(open("X_dev.pickle", "rb"))
y_dev = pickle.load(open("y_dev.pickle", "rb"))
lookup = pickle.load(open("lookup.pickle", "rb"))
reverselookup = pickle.load(open("reverselookup.pickle", "rb"))


model=models.Sequential()
model.add(layers.Conv2D(32, (5, 5), strides=(2,2),activation='relu',input_shape=size))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(len(lookup), activation='softmax'))
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

configuration = model.summary()

model.fit(X_train, y_train, epochs = 5)

model.evaluate(X_test, y_test, validation_data = (X_dev, y_dev))

model.save('model.h5')


