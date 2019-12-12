# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:39:58 2019

@author: Jules
"""

from CnnModel import CnnModel
from Dataset import Dataset
from Video import Video

camera=1

dataset = Dataset()
dataset.load("Dataset")
batchiterator = dataset.compile()
model = CnnModel(model="model1.h5",lookup=dataset.lookup)
#model.train(batchiterator, epochs=2)
video = Video(camera)
video.add_model(model)
#video.view()
geste = "Hi"
images = video.capture(geste=geste)
dataset.add(images, geste)
