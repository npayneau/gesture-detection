from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import os
import time
import cv2

# Parameters
current_path=os.getcwd()
data_source = os.path.join(current_path, "Dataset")
charge = 1
di=int(1/charge)
nbmaximagespardossier=10

def data_augmentation():
    for i in os.walk(data_source):
        if '.' not in i[0] and i[1]==[]:
            fichiers=i[2][0:nbmaximagespardossier:di]
            for j in fichiers:
                # change the path to the current one
                current_path = os.path.join(data_source, i[0])
                current_path = os.path.join(current_path, j)
                # load the image
                img = load_img(current_path)
                # convert to numpy array
                data = img_to_array(img)
                # expand dimension to one sample
                samples = expand_dims(data, 0)
                # create image data augmentation generator
                datagen = ImageDataGenerator(horizontal_flip=True)
                # prepare iterator
                it = datagen.flow(samples, batch_size=1)
                # generate samples and plot
                batch = it.next()
                # convert the array into an image
                image = batch[0].astype('uint8')
                # save the image
                cv2.imwrite(os.path.join(current_path, str(time.time())+'.jpg'),img=image)

data_augmentation()