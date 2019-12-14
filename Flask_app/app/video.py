import pickle

import cv2
import numpy as np
from tensorflow.keras.models import load_model


class Video:
    def __init__(self,camera):
        self.cap=cv2.VideoCapture(camera)

        #%% Parameters
        self.size=(100,100,3)

        self.model = load_model('model1.h5')
        self.lookup = pickle.load(open("lookup.pickle", "rb"))

        self.resize = False

        self.camera = camera
        self.carre = self.crop_current_image()
        #%% Cropping the image

    def crop_current_image(self):
        # Read image
        cap = cv2.VideoCapture(self.camera)
        ret, frame = cap.read()
        img = np.copy(frame)
        if self.resize :
            img = cv2.resize(img, (1280, 1024))
        # Select Region of interest
        r = cv2.selectROI(img)
        cv2.destroyAllWindows()
        cap.release()
        return(int(r[1]), int(r[1] + r[3]), int(r[0]), int(r[0] + r[2]))

    def get_frame(self):
        yA,yB,xA,xB=self.carre
        ret,frame=self.cap.read()

        #return jpeg.tobytes()

        if self.resize:
            frame = cv2.resize(frame,(1280,1024))
        img = np.copy(frame)

        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 1)
        #cv2.imshow('image', frame)


        if xA!=xB and yA!=yB:
            img=img[yA:yB,xA:xB,:]

        img = cv2.resize(img,(self.size[0],self.size[1]))
        img = np.array(img)
        img2 = img*1.0
        predictions = self.model.predict(img2.reshape((1,self.size[0],self.size[1],self.size[2])))
        geste=self.lookup[np.argmax(predictions[0])]

        img_affichee = img
        img_affichee = cv2.resize(img_affichee,(800,700))    #Affichage pixelisé de l'image
        cv2.putText(img_affichee,geste,(self.size[0],self.size[1]),0, 2, (255,0,255),2)
        #cv2.imshow("Detection",img_affichee)

        ancien_geste=geste
        ret, jpeg = cv2.imencode('.jpg', img_affichee)
        return(jpeg.tobytes(),geste)
        #api.act(ancien_geste,geste,controller)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

if __name__ == '__main__':
    vid = Video(0)
