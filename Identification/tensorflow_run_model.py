# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:36:46 2019

@author: thieb
"""


from tensorflow.keras.models import load_model
import pickle
import numpy as np
import cv2
from matplotlib import pyplot as plt


X_dev = pickle.load(open("x_dev.pickle", "rb"))
y_dev = pickle.load(open("y_dev.pickle", "rb"))
X_test = pickle.load(open("x_test.pickle", "rb"))
y_test = pickle.load(open("y_test.pickle", "rb"))

# returns a compiled model
# identical to the previous one
model = load_model('modelCNN.h5')

dev_loss, dev_acc = model.evaluate(X_dev, y_dev, verbose = 0)

test_loss, test_acc = model.evaluate(X_test, y_test, verbose = 0)

print('Dev accuracy: {:2.2f}%'.format(dev_acc*100))

print('Test accuracy: {:2.2f}%'.format(test_acc*100))