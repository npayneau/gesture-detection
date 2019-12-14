import os

from modules.CnnModel import CnnModel
from modules.Dataset import Dataset
from modules.Video import Video

# %% Parameters
camera = 1
resize = False
model_name = "model"
dataset_name = "Dataset"
size = (100, 100, 3)
maxpardossier = 100
charge = 1
batchsize = 32

# %% Loading data
dataset = Dataset(size=size, batchsize=batchsize)
dataset.load(dataset_name=dataset_name, charge=charge, maxpardossier=maxpardossier)

# %% Training on model
model = CnnModel(model_name=model_name, size=size)
model.save(model_name="model222")

# %% Showing results
video = Video(cnnmodel=model, camera=camera, resize=resize)
video.view()
