from PyQt5.QtCore import QThread, QUrl
import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import sys
import worker


class Form():

    def __init__(self, url):
        self.url=url

        self.app = QApplication(sys.argv)
        self.web = QWebEngineView()
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web.setWindowFlags(PyQt5.QtCore.Qt.WindowStaysOnTopHint)
        self.web.load(QUrl(self.url))
        self.web.setWindowTitle('habbo')
        self.web.setFixedSize(1000, 800)
        self.web.show()

        self.thread1 = worker.QThread1()
        self.thread1.start()

        self.app.exec_()


Form(url='https://habbo.com/hotel')