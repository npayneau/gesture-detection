from __future__ import absolute_import, division, print_function, unicode_literals

# Install TensorFlow

import tensorflow as tf
import os

mnist = tf.keras.datasets.mnist
# Création du dataset d'images
DATADIR = "./asl-alphabet"
CATEGORIES = [1:28]
training_data = []
IMG_SIZE = 50  #50

def create_traning_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try :
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass

create_traning_data()

#print(len(training_data))

import random

random.shuffle(training_data)
for sample in training_data[:10]:
    print(sample[1])
X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

#X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
'''
import pickle

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)
'''


# Réseau de neurone & Convolution
#(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = X
y_train = y

x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
              model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)
