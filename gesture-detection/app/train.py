from keras.preprocessing.image import ImageDataGenerator

from modules.CnnModel import CnnModel
from modules.Dataset import Dataset
from modules.Video import Video

# %% Parameters
camera = 0
resize = False
model_name = "model"
dataset_name = "Dataset"
size = (100, 100, 3)
maxpardossier = 100
charge = 1
batchsize = 32
epochs = 10

# %% Loading data
dataset = Dataset(size=size, batchsize=batchsize)
dataset.load(dataset_name=dataset_name, charge=charge, maxpardossier=maxpardossier)
# Now that the folders are loaded, you can apply images preprocessing shifts and transformations with the ImageDataGenerator:
imagen = ImageDataGenerator(vertical_flip=True)
# You can also save a tree copy of the dataset in an excel file
dataset.save_excel()

# %% Training on model
# Creating a model
model = CnnModel(model_name=model_name, size=size)
# Compiling the dataset into an iterator to train
batchiterator = dataset.compile()
# Training
model.train(batchiterator, epochs=epochs)
# Saving the new model into a copy (if you have written on another model, you can still get it from the backups directory)
model.save(model_name="final_model")

# %% Showing results
video = Video(cnnmodel=model, camera=camera, resize=resize)
video.view()
