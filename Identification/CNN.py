import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
import pickle
import numpy as np
from datetime import datetime

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

history=model.fit(x_train, y_train, epochs=5, batch_size=16, verbose=1, validation_data=(x_validate, y_validate))

#%% Affichage accuracy

now = datetime.now()
now = now.strftime("%D"+"  %Hh%Mm%Ss").replace('/','-')
model.save(os.getcwd()+'\\models\\'+str(now)+'.h5')
plothistory(history)


