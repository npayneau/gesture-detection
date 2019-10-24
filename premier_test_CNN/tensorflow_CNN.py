from __future__ import absolute_import, division, print_function, unicode_literals

# Install TensorFlow

import tensorflow as tf
import os
import string

mnist = tf.keras.datasets.mnist
# Creation du dataset d'images
DATADIR_TEST = "./asl-alphabet/asl_alphabet_test/asl_alphabet_test/"
DATADIR_TRAIN = "./asl-alphabet/asl_alphabet_train/asl_alphabet_train/"

CATEGORIES = []
for i in range(A, Z):
 CATEGORIES.append(i)

training_data = []
testing_data = []

IMG_SIZE = 50  #50

def create_test_data():
    path = os.path.join(DATADIR_TEST, category)
    for img in os.listdir(path):
        try :
            img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))
            testing_data.append([new_array, 1])
        except Exception as e:
            pass

def create_traning_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR_TRAIN, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try :
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass

create_traning_data()
create_test_data()

#print(len(training_data))

import random

random.shuffle(training_data)
#for sample in training_data[:10]:
#    print(sample[1])
X_train = []
y_train = []
X_test = []
y_test = []


for features, label in training_data:
    X_train.append(features)
    y_train.append(label)
for features, label in testing_data:
    X_test.append(features)
    y_test.append(label)

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


# Reseau de neurone & Convolution
#(x_train, y_train), (x_test, y_test) = mnist.load_data()


X_train, X_test = X_train / 255.0, X_test / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5)

model.evaluate(X_test,  y_test, verbose=2)
