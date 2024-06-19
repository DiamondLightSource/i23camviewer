#!/dls/science/groups/i23/pyenvs/i23camsconda/bin/python
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from cothread.catools import *
import sys

class LiveCheckThread(QtCore.QThread):
    update_status = QtCore.pyqtSignal(str, bool)

    def __init__(self, camlib):
        super().__init__()
        self.camlib = camlib

    def run(self):
        while True:
            for cam_name, cam_address in self.camlib.items():
                live = caget(cam_address)
                if live == 0.0:
                    self.update_status.emit(cam_name, False)
                else:
                    self.update_status.emit(cam_name, True)
            self.msleep(1000)  

class Ui_I23Cams(object):
    def setupUi(self, I23Cams):
        I23Cams.setObjectName("I23Cams")
        I23Cams.resize(716, 1219)
        I23Cams.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(I23Cams)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setSizeIncrement(QtCore.QSize(1, 1))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.mainCams = QtWidgets.QWidget()
        self.mainCams.setObjectName("mainCams")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.mainCams)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gonioView = QtWebEngineWidgets.QWebEngineView(self.mainCams)
        self.gonioView.setUrl(QtCore.QUrl("http://bl23i-di-serv-01.diamond.ac.uk:8080/ECAM10.mjpg.mjpg"))
        self.gonioView.setObjectName("gonioView")
        self.verticalLayout.addWidget(self.gonioView)
        self.gripperView = QtWebEngineWidgets.QWebEngineView(self.mainCams)
        self.gripperView.setAutoFillBackground(False)
        self.gripperView.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM6.mjpg.mjpg"))
        self.gripperView.setObjectName("gripperView")
        self.verticalLayout.addWidget(self.gripperView)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.frontView = QtWebEngineWidgets.QWebEngineView(self.mainCams)
        self.frontView.setEnabled(True)
        self.frontView.setMinimumSize(QtCore.QSize(0, 500))
        self.frontView.setMaximumSize(QtCore.QSize(16777215, 800))
        self.frontView.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM7.mjpg.mjpg"))
        self.frontView.setObjectName("frontView")
        self.gridLayout_4.addWidget(self.frontView, 1, 0, 1, 1)
        self.tabWidget.addTab(self.mainCams, "")
        self.extraCams = QtWidgets.QWidget()
        self.extraCams.setObjectName("extraCams")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.extraCams)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.hotelView = QtWebEngineWidgets.QWebEngineView(self.extraCams)
        self.hotelView.setUrl(QtCore.QUrl("http://bl23i-di-serv-01.diamond.ac.uk:8080/ECAM9.mjpg.mjpg"))
        self.hotelView.setObjectName("hotelView")
        self.gridLayout.addWidget(self.hotelView, 1, 1, 1, 1)
        self.OAV = QtWebEngineWidgets.QWebEngineView(self.extraCams)
        self.OAV.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/OAV.mjpg.mjpg"))
        self.OAV.setObjectName("OAV")
        self.gridLayout.addWidget(self.OAV, 1, 0, 1, 1)
        self.outboardView = QtWebEngineWidgets.QWebEngineView(self.extraCams)
        self.outboardView.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM3.mjpg.mjpg"))
        self.outboardView.setObjectName("outboardView")
        self.gridLayout.addWidget(self.outboardView, 0, 0, 1, 1)
        self.inboardView = QtWebEngineWidgets.QWebEngineView(self.extraCams)
        self.inboardView.setAutoFillBackground(False)
        self.inboardView.setUrl(QtCore.QUrl("http://bl23i-di-serv-02.diamond.ac.uk:8080/ECAM5.mjpg.mjpg"))
        self.inboardView.setObjectName("inboardView")
        self.gridLayout.addWidget(self.inboardView, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.extraCams, "")
        self.diagnosticCams = QtWidgets.QWidget()
        self.diagnosticCams.setEnabled(True)
        self.diagnosticCams.setObjectName("diagnosticCams")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.diagnosticCams)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.d1 = QtWebEngineWidgets.QWebEngineView(self.diagnosticCams)
        self.d1.setToolTipDuration(-1)
        self.d1.setUrl(QtCore.QUrl("http://bl23i-di-serv-03.diamond.ac.uk:8082/D1.CAM.mjpg.mjpg"))
        self.d1.setObjectName("d1")
        self.verticalLayout_2.addWidget(self.d1)
        self.d2 = QtWebEngineWidgets.QWebEngineView(self.diagnosticCams)
        self.d2.setUrl(QtCore.QUrl("http://bl23i-di-serv-03.diamond.ac.uk:8082/D2.CAM.mjpg.mjpg"))
        self.d2.setObjectName("d2")
        self.verticalLayout_2.addWidget(self.d2)
        self.d3 = QtWebEngineWidgets.QWebEngineView(self.diagnosticCams)
        self.d3.setUrl(QtCore.QUrl("http://bl23i-di-serv-03.diamond.ac.uk:8082/D3.CAM.mjpg.mjpg"))
        self.d3.setObjectName("d3")
        self.verticalLayout_2.addWidget(self.d3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.diagnosticCams, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        I23Cams.setCentralWidget(self.centralwidget)

        self.retranslateUi(I23Cams)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(I23Cams)

        self.camlib = {
            "frontView": self.frontView,
            "gonioView": self.gonioView,
            "gripperView": self.gripperView,
            "OAV": self.OAV,
            "hotelView": self.hotelView,
            "inboardView": self.inboardView,
            "outboardView": self.outboardView,
            "d1": self.d1,
            "d2": self.d2,
            "d3": self.d3,
        }
        self.cam_addresses = {
            "frontView": "BL23I-DI-CAM-07:CAM:ArrayRate_RBV",
            "gonioView": "BL23I-DI-CAM-06:CAM:ArrayRate_RBV",
            "gripperView": "BL23I-DI-CAM-10:CAM:ArrayRate_RBV",
            "OAV": "BL23I-DI-OAV-01:CAM:ArrayRate_RBV",
            "hotelView": "BL23I-DI-CAM-09:CAM:ArrayRate_RBV",
            "inboardView": "BL23I-DI-CAM-05:CAM:ArrayRate_RBV",
            "outboardView": "BL23I-DI-CAM-03:CAM:ArrayRate_RBV",
            "d1": "BL23I-DI-PHDGN-01:CAM:ArrayRate_RBV",
            "d2": "BL23I-DI-PHDGN-02:CAM:ArrayRate_RBV",
            "d3": "BL23I-DI-PHDGN-03:CAM:ArrayRate_RBV",
        }

        self.live_check_thread = LiveCheckThread(self.cam_addresses)
        self.live_check_thread.update_status.connect(self.update_camera_status)
        self.live_check_thread.start()

    def update_camera_status(self, cam_name, is_live):
        if is_live:
            self.camlib[cam_name].setUrl(self.camlib[cam_name].url())  
        else:
            self.camlib[cam_name].setUrl(QtCore.QUrl("about:blank")) 

    def retranslateUi(self, I23Cams):
        _translate = QtCore.QCoreApplication.translate
        I23Cams.setWindowTitle(_translate("I23Cams", "I23 Cam Viewer"))
        self.tabWidget.setToolTip(_translate("I23Cams", "<html><head/><body><p>Switch views between the main cameras for daily operation, extra cameras for troubleshooting and diagnostic cameras for... diagnostics.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainCams), _translate("I23Cams", "Main Cams"))
        self.hotelView.setToolTip(_translate("I23Cams", "<html><head/><body><p>Hotel camera</p></body></html>"))
        self.OAV.setToolTip(_translate("I23Cams", "<html><head/><body><p>OAV camera</p></body></html>"))
        self.outboardView.setToolTip(_translate("I23Cams", "<html><head/><body><p>Outboard camera</p></body></html>"))
        self.inboardView.setToolTip(_translate("I23Cams", "<html><head/><body><p>Inboard camera</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extraCams), _translate("I23Cams", "Extra Cams"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diagnosticCams), _translate("I23Cams", "Diagnostic Cams"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_I23Cams()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())