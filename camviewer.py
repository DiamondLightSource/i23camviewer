"""
I23 Camera Viewer
Lightweight PyQt5 GUI for viewing I23 beamline cameras during data collection.
"""

import logging
import os
import subprocess
import sys
import threading

import cothread
from cothread.catools import caget
from PyQt5 import QtCore, QtWidgets

from design import Ui_I23Cams

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger(__name__)

# Single source of truth for all camera PVs and stream URLs.
# Keys must match the widget attribute names in Ui_I23Cams.
CAMERA_CONFIG = {
    "frontView":    ("BL23I-DI-CAM-07:CAM:ArrayRate_RBV",   "http://bl23i-di-serv-04.diamond.ac.uk:8080/ECAM7.mjpg.mjpg"),
    "gonioView":    ("BL23I-DI-CAM-06:CAM:ArrayRate_RBV",   "http://bl23i-di-serv-04.diamond.ac.uk:8080/ECAM6.mjpg.mjpg"),
    "gripperView":  ("BL23I-DI-CAM-10:CAM:ArrayRate_RBV",   "http://bl23i-di-serv-01.diamond.ac.uk:8080/ECAM10.mjpg.mjpg"),
    "OAV":          ("BL23I-DI-OAV-01:CAM:ArrayRate_RBV",   "http://bl23i-di-serv-04.diamond.ac.uk:8080/OAV.mjpg.mjpg"),
    "hotelView":    ("BL23I-DI-CAM-09:CAM:ArrayRate_RBV",   "http://bl23i-di-serv-01.diamond.ac.uk:8080/ECAM9.mjpg.mjpg"),
    "inboardView":  ("BL23I-DI-CAM-05:CAM:ArrayRate_RBV",   "http://bl23i-di-serv-04.diamond.ac.uk:8080/ECAM5.mjpg.mjpg"),
    "outboardView": ("BL23I-DI-CAM-03:CAM:ArrayRate_RBV",   "http://bl23i-di-serv-04.diamond.ac.uk:8080/ECAM3.mjpg.mjpg"),
    "d1":           ("BL23I-DI-PHDGN-01:CAM:ArrayRate_RBV", "http://bl23i-di-serv-05.diamond.ac.uk:8082/D1.CAM.mjpg.mjpg"),
    "d2":           ("BL23I-DI-PHDGN-02:CAM:ArrayRate_RBV", "http://bl23i-di-serv-05.diamond.ac.uk:8082/D2.CAM.mjpg.mjpg"),
    "d3":           ("BL23I-DI-PHDGN-03:CAM:ArrayRate_RBV", "http://bl23i-di-serv-05.diamond.ac.uk:8082/D3.CAM.mjpg.mjpg"),
}

RED_SCREEN_URL = "http://127.0.0.1:8080/redscreen.mjpg"


def start_red_server() -> subprocess.Popen:
    """Start the local red-screen placeholder MJPEG server.

    Uses the current Python interpreter so no hardcoded paths are needed.
    Returns the Popen handle so the caller can terminate it on exit.
    """
    script = os.path.join(os.path.dirname(__file__), "redServer.py")
    proc = subprocess.Popen(
        [sys.executable, script],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    log.info("Red screen server started (pid %d)", proc.pid)
    return proc


class LiveCheckThread(QtCore.QThread):
    """Polls EPICS PVs for each camera's frame rate and emits status updates."""

    updateStatus = QtCore.pyqtSignal(str, bool, str)

    def __init__(self) -> None:
        super().__init__()
        self._stop = threading.Event()

    def run(self) -> None:
        while not self._stop.is_set():
            for cam_name, (pv, url) in CAMERA_CONFIG.items():
                try:
                    framerate = float(caget(pv, timeout=1.0))
                    running = framerate > 0.0
                except Exception as exc:
                    log.warning("PV read failed for %s (%s): %s", cam_name, pv, exc)
                    running = False
                self.updateStatus.emit(cam_name, running, url)
            self.msleep(2000)

    def stop(self) -> None:
        self._stop.set()


class CamViewerWindow(QtWidgets.QMainWindow):
    """Main window: sets up the UI, owns the camera widget map, handles status updates."""

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_I23Cams()
        self.ui.setupUi(self)

        # Build an explicit name→widget map from CAMERA_CONFIG keys.
        # This avoids fragile getattr(self, string) lookups at update time
        # and gives a clear error at startup if a key doesn't match a widget.
        self._cam_widgets = {}
        for name in CAMERA_CONFIG:
            widget = getattr(self.ui, name, None)
            if widget is None:
                log.error("CAMERA_CONFIG key '%s' has no matching UI widget — check design.ui", name)
            else:
                self._cam_widgets[name] = widget

        # Override initial URLs from the single source of truth (CAMERA_CONFIG).
        # design.py may have stale/wrong addresses from a previous generation.
        for name, (_, url) in CAMERA_CONFIG.items():
            if name in self._cam_widgets:
                self._cam_widgets[name].setUrl(QtCore.QUrl(url))

    def set_camera_status(self, cam_name: str, running: bool, url: str) -> None:
        widget = self._cam_widgets.get(cam_name)
        if widget is None:
            return
        target = url if running else RED_SCREEN_URL
        if widget.url().toString() != target:
            widget.setUrl(QtCore.QUrl(target))


if __name__ == "__main__":
    # QApplication must exist before cothread.iqt() integrates the event loops.
    app = QtWidgets.QApplication(sys.argv)
    cothread.iqt()

    red_proc = start_red_server()

    window = CamViewerWindow()

    live_check = LiveCheckThread()
    live_check.updateStatus.connect(window.set_camera_status)
    live_check.start()

    window.show()

    try:
        cothread.WaitForQuit()
    finally:
        log.info("Shutting down...")
        live_check.stop()
        live_check.wait(3000)
        red_proc.terminate()
        log.info("Shutdown complete")
