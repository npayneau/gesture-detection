from __future__ import absolute_import, division, print_function, unicode_literals

# Install TensorFlow

import tensorflow as tf
import os
import string
import cv2


mnist = tf.keras.datasets.mnist
# Creation du dataset d'images
DATADIR_TEST = "./asl-alphabet/asl_alphabet_test/asl_alphabet_test"
DATADIR_TRAIN = "./asl-alphabet/asl_alphabet_train/asl_alphabet_train"

CATEGORIES = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","nothing"]
'''
for i in range(0, 26):
 CATEGORIES.append(i)
'''
training_data = []
testing_data = []

IMG_SIZE = 50  #50

def create_test_data():
    path = os.path.join(DATADIR_TEST, "")
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

import pickle

pickle_out = open("X_test.pickle", "wb")
pickle.dump(X_test, pickle_out)
pickle_out.close()

pickle_out = open("X_train.pickle", "wb")
pickle.dump(X_train, pickle_out)
pickle_out.close()

pickle_out = open("y_train.pickle", "wb")
pickle.dump(y_train, pickle_out)
pickle_out.close()

pickle_out = open("y_test.pickle", "wb")
pickle.dump(y_test, pickle_out)
pickle_out.close()


# Reseau de neurone & Convolution
#(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(len(training_data))
