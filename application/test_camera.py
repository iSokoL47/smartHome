from flask import Flask, render_template, Response, redirect, url_for
import io
import cv2
import numpy as np
from datetime import datetime
from picamera2 import Picamera2
import os

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

def gen_frames():
    while True:
        frame = picam2.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
    frame = picam2.capture_array()
    directory = "images"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = f"{directory}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
    cv2.imwrite(filename, frame)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
