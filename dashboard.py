
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox



import os
from shlex import shlex
import sys
import subprocess
import json



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(0, 0, 201, 561))
        self.sidebar.setAutoFillBackground(True)
        self.sidebar.setFrameShape(QtWidgets.QFrame.Panel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.crime_but = QtWidgets.QPushButton(self.sidebar)
        self.crime_but.setGeometry(QtCore.QRect(20, 130, 161, 31))
        self.crime_but.setObjectName("crime_but")
        self.cctv_but = QtWidgets.QPushButton(self.sidebar)
        self.cctv_but.setGeometry(QtCore.QRect(20, 90, 161, 31))
        self.cctv_but.setObjectName("cctv_but")
        self.tracker_but = QtWidgets.QPushButton(self.sidebar)
        self.tracker_but.setGeometry(QtCore.QRect(20, 170, 161, 31))
        self.tracker_but.setObjectName("tracker_but")
        self.label = QtWidgets.QLabel(self.sidebar)
        self.label.setGeometry(QtCore.QRect(20, 520, 141, 31))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.sidebar)
        self.line.setGeometry(QtCore.QRect(10, 500, 161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.home = QtWidgets.QPushButton(self.sidebar)
        self.home.setGeometry(QtCore.QRect(20, 50, 161, 31))
        self.home.setObjectName("home")
        self.hate_but = QtWidgets.QPushButton(self.sidebar)
        self.hate_but.setGeometry(QtCore.QRect(20, 210, 161, 31))
        self.hate_but.setObjectName("hate_but")
        self.senti_but = QtWidgets.QPushButton(self.sidebar)
        self.senti_but.setGeometry(QtCore.QRect(20, 250, 161, 31))
        self.senti_but.setObjectName("senti_but")
        self.entity_but = QtWidgets.QPushButton(self.sidebar)
        self.entity_but.setGeometry(QtCore.QRect(20, 290, 161, 31))
        self.entity_but.setObjectName("entity_but")
        self.audio_but = QtWidgets.QPushButton(self.sidebar)
        self.audio_but.setGeometry(QtCore.QRect(20, 330, 161, 31))
        self.audio_but.setObjectName("audio_but")
        self.video_but = QtWidgets.QPushButton(self.sidebar)
        self.video_but.setGeometry(QtCore.QRect(20, 370, 161, 31))
        self.video_but.setObjectName("video_but")
        self.crime_panel = QtWidgets.QFrame(self.centralwidget)
        self.crime_panel.setGeometry(QtCore.QRect(210, 10, 161, 81))
        self.crime_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.crime_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.crime_panel.setObjectName("crime_panel")
        self.upload_crime = QtWidgets.QPushButton(self.crime_panel)
        self.upload_crime.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.upload_crime.setObjectName("upload_crime")
        self.label_3 = QtWidgets.QLabel(self.crime_panel)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 64, 19))
        self.label_3.setObjectName("label_3")
        self.cctv_panel = QtWidgets.QFrame(self.centralwidget)
        self.cctv_panel.setGeometry(QtCore.QRect(210, 100, 161, 71))
        self.cctv_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cctv_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cctv_panel.setObjectName("cctv_panel")
        self.upload_cctv = QtWidgets.QPushButton(self.cctv_panel)
        self.upload_cctv.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.upload_cctv.setObjectName("upload_cctv")
        self.label_2 = QtWidgets.QLabel(self.cctv_panel)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 64, 19))
        self.label_2.setObjectName("label_2")
        self.panel_tracker = QtWidgets.QFrame(self.centralwidget)
        self.panel_tracker.setGeometry(QtCore.QRect(210, 180, 161, 71))
        self.panel_tracker.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.panel_tracker.setFrameShadow(QtWidgets.QFrame.Raised)
        self.panel_tracker.setObjectName("panel_tracker")
        self.label_4 = QtWidgets.QLabel(self.panel_tracker)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 64, 19))
        self.label_4.setObjectName("label_4")
        self.upload_tracker = QtWidgets.QPushButton(self.panel_tracker)
        self.upload_tracker.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.upload_tracker.setObjectName("upload_tracker")
        self.audio_panel = QtWidgets.QFrame(self.centralwidget)
        self.audio_panel.setGeometry(QtCore.QRect(210, 260, 161, 71))
        self.audio_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.audio_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.audio_panel.setObjectName("audio_panel")
        self.upload_audio = QtWidgets.QPushButton(self.audio_panel)
        self.upload_audio.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.upload_audio.setObjectName("upload_audio")
        self.label_5 = QtWidgets.QLabel(self.audio_panel)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 64, 19))
        self.label_5.setObjectName("label_5")
        self.video_panel = QtWidgets.QFrame(self.centralwidget)
        self.video_panel.setGeometry(QtCore.QRect(210, 340, 161, 91))
        self.video_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_panel.setObjectName("video_panel")
        self.labelkl = QtWidgets.QLabel(self.video_panel)
        self.labelkl.setGeometry(QtCore.QRect(10, 70, 64, 19))
        self.labelkl.setObjectName("labelkl")
        self.upload_video = QtWidgets.QPushButton(self.video_panel)
        self.upload_video.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.upload_video.setObjectName("upload_video")
        self.entity_panel = QtWidgets.QFrame(self.centralwidget)
        self.entity_panel.setGeometry(QtCore.QRect(210, 440, 161, 101))
        self.entity_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.entity_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entity_panel.setObjectName("entity_panel")
        self.upload_enitiy = QtWidgets.QPushButton(self.entity_panel)
        self.upload_enitiy.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.upload_enitiy.setObjectName("upload_enitiy")
        self.label_6 = QtWidgets.QLabel(self.entity_panel)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 64, 19))
        self.label_6.setObjectName("label_6")
        self.hate_panel = QtWidgets.QFrame(self.centralwidget)
        self.hate_panel.setGeometry(QtCore.QRect(390, 10, 181, 81))
        self.hate_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hate_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hate_panel.setObjectName("hate_panel")
        self.upload_hate = QtWidgets.QPushButton(self.hate_panel)
        self.upload_hate.setGeometry(QtCore.QRect(30, 20, 121, 31))
        self.upload_hate.setObjectName("upload_hate")
        self.label_7 = QtWidgets.QLabel(self.hate_panel)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 64, 19))
        self.label_7.setObjectName("label_7")
        self.senti_panel = QtWidgets.QFrame(self.centralwidget)
        self.senti_panel.setGeometry(QtCore.QRect(390, 100, 181, 71))
        self.senti_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.senti_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.senti_panel.setObjectName("senti_panel")
        self.upload_senti = QtWidgets.QPushButton(self.senti_panel)
        self.upload_senti.setGeometry(QtCore.QRect(30, 10, 111, 31))
        self.upload_senti.setObjectName("upload_senti")
        self.label_8 = QtWidgets.QLabel(self.senti_panel)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 64, 19))
        self.label_8.setObjectName("label_8")
        self.home_panel = QtWidgets.QFrame(self.centralwidget)
        self.home_panel.setGeometry(QtCore.QRect(390, 180, 181, 71))
        self.home_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_panel.setObjectName("home_panel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #me

        self.crime_panel.hide()
        self.cctv_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.hide()
        self.entity_panel.hide()
        self.audio_panel.hide()
        self.hate_panel.hide()
        self.senti_panel.hide()
        self.home_panel.show()




        self.cctv_but.clicked.connect(self.showCctv)
        self.crime_but.clicked.connect(self.showCrime)
        self.tracker_but.clicked.connect(self.showTracker)
        self.hate_but.clicked.connect(self.showHate)
        self.senti_but.clicked.connect(self.showSenti)
        self.entity_but.clicked.connect(self.showEntity)
        self.audio_but.clicked.connect(self.showAudio)
        self.video_but.clicked.connect(self.showVideo)
        self.home.clicked.connect(self.showHome)


        self.upload_cctv.clicked.connect(self.uploadCctv)
        self.upload_tracker.clicked.connect(self.uploadTracker)
        self.upload_audio.clicked.connect(self.uploadAudio)
        self.upload_hate.clicked.connect(self.uploadHate)
        self.upload_tracker.clicked.connect(self.uploadTracker)


    
    def showCrime(self):

        self.crime_panel.show()
        self.cctv_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.hide()
        self.entity_panel.hide()
        self.audio_panel.hide()
        self.hate_panel.hide()
        self.senti_panel.hide()
        self.home_panel.hide()



    def showCctv(self):
    
        self.cctv_panel.show()
        self.crime_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.hide()
        self.entity_panel.hide()
        self.audio_panel.hide()
        self.hate_panel.hide()
        self.senti_panel.hide()
        self.home_panel.hide()

    def showVideo(self):

        self.cctv_panel.hide()
        self.crime_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.show()
        self.entity_panel.hide()
        self.audio_panel.hide()
        self.hate_panel.hide()
        self.senti_panel.hide()
        self.home_panel.hide()

    def showEntity(self):

        self.cctv_panel.hide()
        self.crime_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.hide()
        self.entity_panel.show()
        self.audio_panel.hide()
        self.hate_panel.hide()
        self.senti_panel.hide()
        self.home_panel.hide()

    def showAudio(self):

        self.cctv_panel.hide()
        self.crime_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.hide()
        self.entity_panel.hide()
        self.audio_panel.show()
        self.hate_panel.hide()
        self.senti_panel.hide()
        self.home_panel.hide()

    def showTracker(self):

        self.cctv_panel.hide()
        self.crime_panel.hide()
        self.panel_tracker.show()
        self.video_panel.hide()
        self.entity_panel.hide()
        self.audio_panel.hide()
        self.hate_panel.hide()
        self.senti_panel.hide()
        self.home_panel.hide()

    def showHate(self):

        self.cctv_panel.hide()
        self.crime_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.hide()
        self.entity_panel.hide()
        self.audio_panel.hide()
        self.hate_panel.show()
        self.senti_panel.hide()
        self.home_panel.hide()

    def showSenti(self):

        self.cctv_panel.hide()
        self.crime_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.hide()
        self.entity_panel.hide()
        self.audio_panel.hide()
        self.hate_panel.hide()
        self.senti_panel.show()
        self.home_panel.hide()


    def showHome(self):

        self.cctv_panel.hide()
        self.crime_panel.hide()
        self.panel_tracker.hide()
        self.video_panel.hide()
        self.entity_panel.hide()
        self.audio_panel.hide()
        self.hate_panel.hide()
        self.senti_panel.hide()
        self.home_panel.show()


    def uploadCctv(self):
        fileName = QFileDialog.getSaveFileName(None, 'Dialog Title', "", "")

        if fileName[0]:
            QMessageBox.about(None, "SKynet", "Video Uploaded Successfully")
            
            txt = "python3 ./key_frame.py '" + fileName[0] + "' 'keys.mp4'"
            process = subprocess.Popen(
                txt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()
            
            QMessageBox.about(None, "SKynet", "Video Filtered Successfully")
            command = "vlc keys.mp4"
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()


        else:
            QMessageBox.about(None, "SKynet", "Error! Video Uploading Failed")

    def uploadTracker(self):
        fileName = QFileDialog.getSaveFileName(None, 'Dialog Title', "", "")

        if fileName[0]:
            QMessageBox.about(None, "SKynet", "Video Uploaded Successfully")
            
            txt = "python3 ./tracking/key_frame.py"
            process = subprocess.Popen(
                txt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()
            
            QMessageBox.about(None, "SKynet", "Video Filtered Successfully")
            command = "vlc keys.mp4"
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()


        else:
            QMessageBox.about(None, "SKynet", "Error! Video Uploading Failed")

    def uploadAudio(self):
        fileName = QFileDialog.getSaveFileName(None, 'Dialog Title', "", "")

        if fileName[0]:
            QMessageBox.about(None, "SKynet", "Audio Uploaded Successfully")
            
            txt = "python3 ./audio/audio_transcribe.py '"+fileName[0]+"'"
            process = subprocess.Popen(
                txt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()
            
            QMessageBox.about(None, "SKynet", "Audio Extracted")
            command = "gedit data.txt"
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()


        else:
            QMessageBox.about(None, "SKynet", "Error! Audio Uploading Failed")

    
    def uploadHate(self):
        fileName = QFileDialog.getSaveFileName(None, 'Dialog Title', "", "")

        if fileName[0]:
            QMessageBox.about(None, "SKynet", "Audio Uploaded Successfully! Start to Evaluating")
            
            txt = "python3 ./hate/audio_transcribe.py '"+fileName[0]+"'"
            process = subprocess.Popen(
                txt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()
            
            QMessageBox.about(None, "SKynet", "Audio Evaluated")
            data=json.loads(open('./hate/data.json').read())
              
            QMessageBox.about(None, "SKynet","'%' of Hate Speach: "+str(data['classes'][0]['confidence'])+" \n '%' of Offensive Language:"+str(data['classes'][1]['confidence'])+" \n '%' of Neutral:"+str(data['classes'][2]['confidence']))
        else:
            QMessageBox.about(None, "SKynet", "Error! Audio Uploading Failed")

    def uploadTracker(self):
        fileName = QFileDialog.getSaveFileName(None, 'Dialog Title', "", "")

        if fileName[0]:
            QMessageBox.about(None, "SKynet", "Audio Uploaded Successfully! Draw aroud the vehicle")
            
            txt = "python3 ./tracking/main.py '"+fileName[0]+"'"
            process = subprocess.Popen(
                txt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            out, err = process.communicate()

              
        else:
            QMessageBox.about(None, "SKynet", "Error! Audio Uploading Failed")




    #me

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MulSource Data Analytic Frame Work"))
        self.crime_but.setText(_translate("MainWindow", "Crime Detection"))
        self.cctv_but.setText(_translate("MainWindow", "CCTV Filter"))
        self.tracker_but.setText(_translate("MainWindow", "Tracker"))
        self.label.setText(_translate("MainWindow", "Developed by SkyNet"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.hate_but.setText(_translate("MainWindow", "Hate Speech Analyzer"))
        self.senti_but.setText(_translate("MainWindow", "Sentimental Analysis"))
        self.entity_but.setText(_translate("MainWindow", "Entity Miner"))
        self.audio_but.setText(_translate("MainWindow", "Audio Extractor"))
        self.video_but.setText(_translate("MainWindow", "Video/Image Analytics"))
        self.upload_crime.setText(_translate("MainWindow", "Upload Video"))
        self.label_3.setText(_translate("MainWindow", "crime"))
        self.upload_cctv.setText(_translate("MainWindow", "Upload Footage"))
        self.label_2.setText(_translate("MainWindow", "cctv"))
        self.label_4.setText(_translate("MainWindow", "tracker"))
        self.upload_tracker.setText(_translate("MainWindow", "Upload here"))
        self.upload_audio.setText(_translate("MainWindow", "Upload Audio"))
        self.label_5.setText(_translate("MainWindow", "Audio"))
        self.labelkl.setText(_translate("MainWindow", "video panel"))
        self.upload_video.setText(_translate("MainWindow", "Upload Video"))
        self.upload_enitiy.setText(_translate("MainWindow", "Upload File"))
        self.label_6.setText(_translate("MainWindow", "entity"))
        self.upload_hate.setText(_translate("MainWindow", "Upload File"))
        self.label_7.setText(_translate("MainWindow", "hate"))
        self.upload_senti.setText(_translate("MainWindow", "Upload File"))
        self.label_8.setText(_translate("MainWindow", "senti"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
