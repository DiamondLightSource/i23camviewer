"""
Local MJPEG server that streams a solid red frame as a camera-offline placeholder.
Binds to 127.0.0.1 only — this service is not intended to be network-accessible.
"""

import numpy as np
import cv2
from flask import Flask, Response

app = Flask(__name__)

# Generate the red frame once at startup — it never changes, so there's no
# reason to re-encode it on every iteration of the stream loop.
def _build_red_frame() -> bytes:
    image = np.zeros((480, 640, 3), dtype=np.uint8)
    image[:] = (0, 0, 255)  # BGR: solid red
    ret, jpeg = cv2.imencode(".jpg", image)
    if not ret:
        raise RuntimeError("Failed to encode red placeholder frame")
    return jpeg.tobytes()

_RED_FRAME: bytes = _build_red_frame()


def _generate_mjpeg_stream():
    while True:
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + _RED_FRAME + b"\r\n"
        )


@app.route("/redscreen.mjpg")
def red_screen():
    return Response(
        _generate_mjpeg_stream(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


if __name__ == "__main__":
    # Bind to localhost only — this server is a local placeholder, not a
    # network service. Binding to 0.0.0.0 would expose it on the facility network.
    app.run(host="127.0.0.1", port=8080, threaded=True)