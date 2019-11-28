from flask import Flask, render_template, url_for, Response
from video import Video

app = Flask(__name__)
vid=Video()

def gen():
    while True:
        frame = vid.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video():
    return render_template('index.html')

@app.route('/pptDisplay')
def ppt():
    return render_template('pptDisplay.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
        mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
