# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:34:26 2019

@author: Jules
"""

import time

import cv2
import numpy as np
import requests


class Video:
    def __init__(self, cnnmodel, camera=0, carre=None, resize=False):
        """
        Activation de la caméra à partir d'un modèle donné
        :param cnnmodel: CnnModel qui permet la prédiction des gestes capturés
        :param camera: caméra à utiliser en capture (0: interne, 1: externe)
        :param carre: zone de capture (sinon la fonction crop est appelée)
        :param resize: permet de redimensionner la fenêtre de capture pour les écrans à haute résolution
        :type camera: int
        :type carre: list of len 4
        :type resize: boolean
        :type cnnmodel: CnnModel
        """
        self.cap = cv2.VideoCapture(camera)
        self.resize = resize
        self.camera = camera
        self.model = cnnmodel
        if carre is None:
            self.carre = self.crop()
            # print(carre)
        else:
            self.carre = carre

    def view(self, post=False):
        """
        Affiche le flux de la vidéo capturée
        """
        last_acted = time.time()
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
                # recadrage
                if xA != xB and yA != yB:
                    img = img[yA:yB, xA:xB, :]
                # prédiction du geste à partir du modèle
                geste = self.model.predict(img)
                if post:
                    ancien_geste, last_acted = self.post_geste(geste, ancien_geste, last_acted)
                # print(geste)
                img_affichee = img
                img_affichee = cv2.resize(img_affichee, (800, 700))  # Affichage pixelisé de l'image
                # cv2.putText(img_affichee, geste, (self.size[0], self.size[1]), 0, 2, (255, 0, 255), 2)
                cv2.imshow("Detection", img_affichee)

                ancien_geste = geste
                # api.act(ancien_geste,geste,controller)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()
        self.cap.release()
        return (None)

    def capture(self, geste, duree=2):
        """
        Générer une liste d'images d'un geste à partir d'une vidéo pendant une durée définie
        :param geste: nom du geste à capturer
        :param duree: durée de capture du geste
        :return: Liste d'images capturees à sauvegarder dans le dataset
        """
        t0=time.time()
        print("Capture de", geste, "pendant", str(duree))
        ancien_geste = ""
        yA, yB, xA, xB = self.carre
        images = []
        while (time.time()-t0<duree):
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

                images.append(img)
                # print(geste)
                img_affichee = img
                img_affichee = cv2.resize(img_affichee, (800, 700))  # Affichage pixelisé de l'image
                # cv2.putText(img_affichee, geste, (self.size[0], self.size[1]), 0, 2, (255, 0, 255), 2)
                cv2.imshow("Capture", img_affichee)

                ancien_geste = geste
                # api.act(ancien_geste,geste,controller)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()
        # self.cap.release()
        return (images)

    def post_geste(self, nouveau_geste, ancien_geste, last_acted):
        """
        Permet de poster un geste sur le port de l'API Java
        :param nouveau_geste: nouveau geste
        :param ancien_geste: ancien geste
        :param last_acted: date du dernier post
        :return: nouveau geste ,ancien geste
        """
        if ancien_geste != nouveau_geste and (
                time.time() - last_acted > 1 or ancien_geste == "Rien" or nouveau_geste == "Rien"):
            r = requests.post('http://localhost:8090/getAPI', data={'geste': nouveau_geste, 'position': '0123'})
            last_acted = time.time()
            print(nouveau_geste)
            return (nouveau_geste, last_acted)
        else:
            return (ancien_geste, last_acted)

    def crop(self):
        """
        Sélection d'une zone d'intérêt sur la vidéo
        """
        ret = False
        while not ret:
            ret, frame = self.cap.read()
            ret = True
        img = np.copy(frame)
        if self.resize:
            img = cv2.resize(img, (1280, 1024))
        # Select Region of interest
        r = cv2.selectROI(img)
        # self.cap.release()
        cv2.destroyAllWindows()
        return (int(r[1]), int(r[1] + r[3]), int(r[0]), int(r[0] + r[2]))

    def get_frame(self):
        """
        Renvoie la vidéo frame par frame
        :return: frame, geste
        """
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
        # geste="Main Ouverte"
        img_affichee = img
        img_affichee = cv2.resize(img_affichee, (800, 700))
        cv2.putText(img_affichee, geste, (100,100), 0, 2, (255, 0, 255), 2)
        ancien_geste = geste
        # api.act(ancien_geste,geste,controller)
        ret, jpeg = cv2.imencode('.jpg', img_affichee)
        return (jpeg.tobytes(), geste)


if __name__ == '__main__':
    vid = Video(0)
    vid.view()
