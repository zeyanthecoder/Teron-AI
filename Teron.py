from TeronGui import Ui_JarvusUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime, QDate
from PyQt5.uic import loadUiType
import TeronUi
import os
import datetime
import webbrowser as web
import sys

class MainThread(QThread):
    def  __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        TeronUi.taskexe(self)

StartExe = MainThread()

class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_JarvusUi()
        self.gui.setupUi(self)

        self.gui.start.clicked.connect(self.startTask)
        self.gui.exit.clicked.connect(self.close)
        self.gui.chrome.clicked.connect(self.chrome_app)
        self.gui.whatsapp.clicked.connect(self.whatsapp_app)
        self.gui.VsCode.clicked.connect(self.Vscode_app)
        self.gui.yt.clicked.connect(self.yt_app)
        self.gui.Word.clicked.connect(self.word_app)
        self.gui.postman.clicked.connect(self.postman_app)
        self.gui.MsPowerpoint.clicked.connect(self.powerpoint_app)
        self.gui.steam.clicked.connect(self.steam_app)
    
    def chrome_app(self):
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def yt_app(self):
        web.open("https://www.youtube.com")

    def whatsapp_app(self):
        web.open("https://web.whatsapp.com")

    def Vscode_app(self):
        os.startfile("C:\\Users\\Zeyan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    def word_app(self):
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")

    def powerpoint_app(self):
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")

    def postman_app(self):
        os.startfile("C:\\Users\\zeyan\\AppData\\Local\\Postman\\Postman.exe")

    def steam_app():
        os.startfile("C:\\Program Files (x86)\\Steam\\steam.exe")

    def startTask(self):
        self.gui.label1 = QtGui.QMovie("Voice.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("Gif_1.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()
    
        self.gui.label3 = QtGui.QMovie("Gif_2.gif")
        self.gui.gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("gif_3.gif")
        self.gui.gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        StartExe.start()

    def showTimeLive(self):
        t_ime = QTime.currentTime()
        time = t_ime.toString()
        d_ate = QDate.currentDate()
        date = d_ate.toString()
        label_time = "Time :" + time
        label_date = "Date :" + date

        self.gui.text_time.setText(label_time)
        self.gui.text_date.setText(label_date);


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_start()
jarvis_gui.show()
exit(GuiApp.exec_())