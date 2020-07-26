
from PyQt5 import QtCore
import bot, time


class QThread1(QtCore.QThread):

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        bot.analys()
        time.sleep(2)
