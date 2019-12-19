# Gesture-detection
## Introduction
Ce projet à pour but de permettre de réaliser de la reconnaissance gestuelle à travers du Machine Learning dans le but de déclencher des événements (ici permet d'animer un diaporama PowerPoint).

Le projet se compose de 3 parties distinctes : Une identification des gestes sous python, une affichage de serveur Web HTML sous Flask et un serveur Java sous Spring Boot.
## Installation
### Modules à installer:
#### Java:
- Spring Tool Suite
#### Python 3.7: 
- Flask: `pip install keras`
- Keras: `pip install tf`
- Pandas: `pip install pandas`
- OpenCV: `pip install opencv-python`; penser à télécharger le zip d'openCV sur leur site web
- Requests: `pip install requests`
- Numpy: `pip install numpy`
## Démarrage
### Serveur Flask:
Lancer le fichier python
\gesture-detection\app\app.py
### SpringBoot:
####Lancer le serveur spring Boot :

Le projet spring boot est composé de plusieurs modules.

Ouvrir le module "com.gesturedetection.application.application" et lancer la classe en tant que serveur Spring Boot.

####Comment configurer le code :
Changer le fichier à lancer : ouvrir la classe "com.gesturedetection.application.controllers" et changer le chemin du ficher dans la la fonction HomePage().

Attention : certains raccourcis peuvent ne pas fonctionner en fonction du système d'exploitation. Pour changer les raccourcis clavier dans appliqués à la machine, ouvrir la classe GesteService dans "com.gesturedetection.application.services" et modifier les KeyEvent en fonction de votre machine.
Liste des KeyEvent possible : https://docs.oracle.com/javase/6/docs/api/java/awt/event/KeyEvent.html

## Configuration
