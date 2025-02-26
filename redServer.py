from flask import Flask, Response
import cv2
import numpy as np

app = Flask(__name__)

def generate_red_frame():
    red_image = np.zeros((480, 640, 3), dtype=np.uint8)
    red_image[:] = (0, 0, 255) 
    ret, jpeg = cv2.imencode('.jpg', red_image)
    if not ret:
        raise ValueError("Could not encode image")

    return jpeg.tobytes()

def generate_mjpeg_stream():
    while True:
        frame = generate_red_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/redscreen.mjpg')
def red_screen():
    return Response(generate_mjpeg_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)