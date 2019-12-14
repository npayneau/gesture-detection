# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:34:26 2019

@author: Jules
"""

import cv2
import numpy as np


class Video:
    def __init__(self, camera=0, carre=None, resize=False):
        self.cap = cv2.VideoCapture(camera)
        self.resize = False
        self.camera = camera
        if carre is None:
            self.carre = self.crop()
            print(carre)
        else:
            self.carre = carre

    def view(self):
        """
        Generate a continuous video stream
        """
        ancien_geste = ""
        yA, yB, xA, xB = self.carre
        while (True):
            ret, frame = self.cap.read()
            if ret:
                if self.resize:
                    frame = cv2.resize(frame, (1280, 1024))
                img = np.copy(frame)

                cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 1)
                cv2.imshow('image', frame)

                if xA != xB and yA != yB:
                    img = img[yA:yB, xA:xB, :]

                geste = self.model.predict(img)
                print(geste)
                img_affichee = img
                img_affichee = cv2.resize(img_affichee, (800, 700))  # Affichage pixelisé de l'image
                # cv2.putText(img_affichee, geste, (self.size[0], self.size[1]), 0, 2, (255, 0, 255), 2)
                cv2.imshow("Detection", img_affichee)

                ancien_geste = geste
                # api.act(ancien_geste,geste,controller)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()
        #self.cap.release()
        return (None)

    def capture(self, geste, temps=2):
        ancien_geste = ""
        yA, yB, xA, xB = self.carre
        images = []
        while (True):
            ret, frame = self.cap.read()
            print(ret)
            if ret:
                if self.resize:
                    frame = cv2.resize(frame, (1280, 1024))
                img = np.copy(frame)

                cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 1)
                cv2.imshow('image', frame)

                if xA != xB and yA != yB:
                    img = img[yA:yB, xA:xB, :]

                geste = self.model.predict(img)
                images.append(img)
                print(geste)
                img_affichee = img
                img_affichee = cv2.resize(img_affichee, (800, 700))  # Affichage pixelisé de l'image
                # cv2.putText(img_affichee, geste, (self.size[0], self.size[1]), 0, 2, (255, 0, 255), 2)
                cv2.imshow("Capture", img_affichee)

                ancien_geste = geste
                # api.act(ancien_geste,geste,controller)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()
        #self.cap.release()
        return (images)

    def crop(self):
        """
        Crop the video
        """
        ret, frame = self.cap.read()
        img = np.copy(frame)
        if self.resize:
            img = cv2.resize(img, (1280, 1024))
        # Select Region of interest
        r = cv2.selectROI(img)
        # self.cap.release()
        cv2.destroyAllWindows()
        return (int(r[1]), int(r[1] + r[3]), int(r[0]), int(r[0] + r[2]))

    def add_model(self, model):
        self.model = model

    def get_frame(self):
        yA, yB, xA, xB = self.carre
        ret, frame = self.cap.read()
        if self.resize:
            frame = cv2.resize(frame, (1280, 1024))
        img = np.copy(frame)

        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 1)
        # cv2.imshow('image', frame)

        if xA != xB and yA != yB:
            img = img[yA:yB, xA:xB, :]
        geste = self.model.predict(img)
        img_affichee = img
        img_affichee = cv2.resize(img_affichee, (800, 700))
        # cv2.putText(img_affichee, geste, (self.size[0], self.size[1]), 0, 2, (255, 0, 255), 2)
        ancien_geste = geste
        # api.act(ancien_geste,geste,controller)
        ret, jpeg = cv2.imencode('.jpg', img_affichee)
        return (jpeg.tobytes(), geste)


if __name__ == '__main__':
    vid = Video(0)
