from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import os

# Parameters
current_path=os.getcwd()
data_source = os.path.join(current_path,"Dataset")
charge = 1
di=int(1/charge)
nbmaximagespardossier=1000

for i in os.walk(data_source):
    if '.' not in i[0] and i[1]==[]:
        fichiers=i[2][0:nbmaximagespardossier:di]
        for j in fichiers:
            # change the path to the current one
            current_path = os.path.join(data_source)
            current_path = os.path.join(current_path,)
            # load the image
            img = load_img('bird.jpg')
            # convert to numpy array
            data = img_to_array(img)
            # expand dimension to one sample
            samples = expand_dims(data, 0)
            # create image data augmentation generator
            datagen = ImageDataGenerator(horizontal_flip=True)
            # prepare iterator
            it = datagen.flow(samples, batch_size=1)
            # generate samples and plot
            for k in range(9):
                # define subplot
                pyplot.subplot(330 + 1 + i)
                # generate batch of images
                batch = it.next()
                # save the image in the same folder