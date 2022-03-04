import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Ui_untitled
import Ui_untitled2
import Ui_untitled3
import tweepy
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_untitled.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
