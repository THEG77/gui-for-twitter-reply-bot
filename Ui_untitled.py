# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Cool\Cool\Python stuff\QTmaybe\twitterreplygui\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import main
import tweepy,time,json
class Ui_MainWindow(object):
    
    def startreplying(self):
        try:
            def user_tweet(username):
                statuses = api.user_timeline(screen_name=username)
                tweetid = statuses[0].id
                return tweetid

            self.textEdit.append("Starting...")
            f = open("config.json")
            data = json.load(f)
            f.close()
            latesttweetids = []
            consumerkey = data["accountdetails"]["CONSUMER_KEY"]
            consumersecret = data["accountdetails"]["CONSUMER_SECRET"]
            accesstoken = data["accountdetails"]["ACCESS_TOKEN"]
            accesstokensecret = data["accountdetails"]["ACCESS_TOKEN_SECRET"]
            
            self.label.setText("         Started!")
            #spaces because i fucked up the text alignment
            auth = tweepy.OAuthHandler(consumerkey,consumersecret)
            auth.set_access_token(accesstoken,accesstokensecret)
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
            try:
                api.verify_credentials()
                print("Authentication OK")
                self.textEdit.append("Authentication OK")

            except:
                print("Error during authentication")
                self.textEdit.append("Error during authentication")


            for usernames in data["usernameList"]:
                temp = user_tweet(usernames)
                latesttweetids.append(temp)
                tempstr = "Latest Tweet ID from "+ str(usernames) + " | " + str(temp)
                self.textEdit.append(tempstr)
                time.sleep(3)
        except Exception as e:
            print(e)        

    def stopreplying(self):
        self.label.setText("         Stopped!")
        self.textEdit.append("Stopped!")
    def opensettings(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = main.Ui_untitled2.Ui_Form()
        self.ui.setupUi2(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 431, 211))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.startreplying)



        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.stopreplying)
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 300, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings.triggered.connect(self.opensettings)
        self.actionAccount = QtWidgets.QAction(MainWindow)
        self.actionAccount.setObjectName("actionAccount")
        self.menuFile.addAction(self.actionAccount)
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TwitterReplyGUI"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Logs..."))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Working ! / Stopped !"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionAccount.setText(_translate("MainWindow", "Account"))
