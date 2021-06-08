import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                          QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                         QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# ==> SPLASH SCREEN
from components.ui_splash_screen import Ui_SplashScreen

# ==> MAIN WINDOW
from components.ui_browser import Ui_Browser

# ==> FUNCTIONS
from functions.ui_functions import *

# ==> GLOBALS
counter = 0

# YOUR APPLICATION


class Browser(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Browser()
        self.ui.setupUi(self)


        UIFunctions.UiDefinitions(self)
        UIFunctions.maximize_restore(self)

        def moveWindow(event):

            if UIFunctions.returnStatus(self) == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI ==> INTERFACE CODES
        ########################################################################

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_2.setText(
            "<strong>WELCOME</strong> TO NEO BROWSER")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_2.setText(
            "<strong>SEARCHING</strong> FOR UPDATES"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_2.setText(
            "<strong>LOADING</strong> USER INTERFACE"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Browser()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
