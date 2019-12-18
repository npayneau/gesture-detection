import time

import requests
from flask import Flask, render_template, Response, request

from modules.CnnModel import CnnModel
from modules.Video import Video

# %% Parameters
camera = 0
resize = False
model_name = "model"
size = (100, 100, 3)

app = Flask(__name__)

# %% Création du modèle
model = CnnModel(model_name=model_name, size=size)

vid = Video(cnnmodel=model, camera=camera, resize=resize)

# %% Définition de la fonction qui permet de poster un geste
geste = ""
data = ""
ancien_geste = ""
last_acted = time.time()


def post_geste(nouveau_geste, ancien_geste, last_acted):
    if time.time() - last_acted > 1 or ancien_geste == "Rien" or nouveau_geste == "Rien":
        r = requests.post('http://localhost:8090/getAPI', data={'geste': nouveau_geste, 'position': '0123'})
        last_acted = time.time()
        print(nouveau_geste)
        return (nouveau_geste, last_acted)
    else:
        return (ancien_geste, last_acted)


# %% Fonction qui génère la vidéo

def gen():
    global geste, ancien_geste, last_acted
    while True:
        frame, geste = vid.get_frame()
        # print(geste)
        ancien_geste, last_acted = post_geste(geste, ancien_geste, last_acted)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# %% Définition des différentes pages html

@app.route('/')
def video():
    return render_template('index.html', geste=geste)


@app.route('/pptDisplay')
def ppt():
    return render_template('pptDisplay.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/geste')
def geste():
    r = requests.post('http://localhost:8090/getAPI', data={'geste': "Main Ouverte", 'position': '0123'})
    return ("geste")


@app.route('/data', methods=['GET', 'POST'])
def data():
    global data
    if request.method == 'POST':
        data = request
        return (request)
    if request.method == 'GET':
        return (data)


if __name__ == '__main__':
    app.run(debug=False)
