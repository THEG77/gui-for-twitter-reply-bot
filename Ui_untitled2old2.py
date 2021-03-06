# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Cool\Cool\Python stuff\QTmaybe\twitterreplygui\untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import main
import json, time

class Ui_Form(object):
    def editusername(self):
        updatedtext = self.lineEdit.text()
        currentlistindex = self.listWidget.currentRow()
        try:
            f = open("config.json")
            data = json.load(f)
            f.close()
            data["usernameList"][currentlistindex] = updatedtext
            with open("config.json","w") as outfile:
                json.dump(data,outfile)
            self.refreshlist()
        except Exception as e:
            print(e)

    def updateedittextbox(self):
        try:
            currentselectedrow = self.listWidget.currentRow()
            currentselectedtext = self.listWidget.item(currentselectedrow).text()
            self.lineEdit.setText(currentselectedtext)
        except Exception as e:
            print(e)
    def refreshlist(self):
        try:
            self.listWidget.clear()
            f = open("config.json")
            jsondata = json.load(f)
            f.close()
            for username in jsondata['usernameList']:
                item = QtWidgets.QListWidgetItem(username)
                self.listWidget.addItem(item)
            f.close()
            
        except Exception as e:
            print(e)
    def openaddusername(self):
        self.window =  QtWidgets.QMainWindow()
        self.ui = main.Ui_untitled3.Ui_Form2()
        self.ui.setupUi3(self.window)
        self.window.show()
        
    def deleteselectd(self):
        currentrow = self.listWidget.currentRow()
        self.listWidget.takeItem(currentrow)
        try:
            f = open("config.json")
            data = json.load(f)
            f.close()
            del data["usernameList"][currentrow]
            with open("config.json","w") as outfile:
                json.dump(data,outfile)
            self.refreshlist()
        except Exception as e:
            print(e)

    def setupUi2(self, Form):
        Form.setObjectName("Form")
        Form.resize(923, 522)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 921, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 321, 411))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.clicked.connect(self.openaddusername)
        
        self.refreshlist()
        self.pushButton.setGeometry(QtCore.QRect(470, 280, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        
        self.pushButton_2.setGeometry(QtCore.QRect(470, 360, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.deleteselectd)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(420, 10, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        try:
            self.listWidget.currentRowChanged.connect(self.updateedittextbox)
            print("TEAST")
        except Exception as e:
            print(e)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 60, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.editusername)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 10, 191, 401))
        self.listWidget_2.setObjectName("listWidget_2")
        try:
            self.refreshlist()
        except Exception as e:
            print(e)
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_3.setGeometry(QtCore.QRect(230, 10, 271, 401))
        self.listWidget_3.setObjectName("listWidget_3")

        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(550, 220, 311, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 291, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 90, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 150, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(560, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "Add New"))
        self.pushButton_2.setText(_translate("Form", "Delete Selected"))
        self.groupBox.setTitle(_translate("Form", "Edit Selected"))
        self.pushButton_3.setText(_translate("Form", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Username List"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("Form", "Add"))

        self.groupBox_2.setTitle(_translate("Form", "Media"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Image Name"))
        self.radioButton.setText(_translate("Form", "Add/Change Image"))
        self.label.setText(_translate("Form", "Image name with extension"))
        self.pushButton_4.setText(_translate("Form", "Add"))
        self.label_2.setText(_translate("Form", "No Image Attached"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Reply Text"))
