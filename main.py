import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                          QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                         QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# ==> SPLASH SCREEN
from components.ui_splash_screen import Ui_SplashScreen

# ==> MAIN WINDOW
from components.ui_browser import Ui_Browser

# ==> AUXILIAR WINDOWS
from components.ui_options import Ui_Options
from components.ui_shortcuts import Ui_Shortcuts

# ==> FUNCTIONS
from functions.ui_functions import *
from functions.browser_functions import *

# ==> GLOBALS
counter = 0

# OPTIONS MENU


class Options(QMainWindow):

    def shortcuts(self):
        self.app = Shortcuts()
        self.app.show()
        self.close()

    def add_tab(self):
        Browser.add_tab(self)

    def print(self):
        Browser.print(self)

    def open_file(self):
        Browser.open_file(self)

    def save_page(self):
        Browser.save_page(self)

    def view_source_code(self):
        Browser.view_source_code(self)

    def about(self):
        AboutFunctions.about(self)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Options()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        def moveWindow(event):

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.dropShadowFrame.mouseMoveEvent = moveWindow

        self.ui.btn_shortcuts.clicked.connect(self.shortcuts)
        self.ui.btn_addTab.clicked.connect(self.add_tab)
        self.ui.btn_print.clicked.connect(self.print)
        self.ui.btn_open.clicked.connect(self.open_file)
        self.ui.btn_save.clicked.connect(self.save_page)
        self.ui.btn_code.clicked.connect(self.view_source_code)
        self.ui.btn_about.clicked.connect(self.about)

        self.shortcut_close = QShortcut(QKeySequence('Esc'), self)
        self.shortcut_close.activated.connect(lambda: self.close())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

# SHORTCUTS MENU


class Shortcuts(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Shortcuts()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        def moveWindow(event):

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.dropShadowFrame.mouseMoveEvent = moveWindow

        self.shortcut_close = QShortcut(QKeySequence('Esc'), self)
        self.shortcut_close.activated.connect(lambda: self.close())

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

# BROWSER


class Browser(QMainWindow):

    def open_options(self):
        self.options = Options()
        self.options.show()

    def tab_open_click(self):
        pass

    def current_tab_changed(self):
        TabFunctions.currentTabChanged(self)

    def close_tab(self):
        TabFunctions.closeTab(self)

    def add_tab(self):
        TabFunctions.addTab(self)

    def back_page(self):
        TabFunctions.previousPage(self)

    def next_page(self):
        TabFunctions.nextPage(self)

    def reload(self):
        TabFunctions.reloadPage(self)

    def print(self):
        TabFunctions.printPage(self)

    def open_file(self):
        FilesFunctions.openFile(self)

    def save_page(self):
        FilesFunctions.savePage(self)

    def view_source_code(self):
        TabFunctions.viewSourceCode(self)

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

        '''self.ui.btn_options.clicked.connect(self.open_options)
        self.ui.btn_previous.clicked.connect(self.back_page)

        self.ui.tabWidget.tabBarDoubleClicked.connect(self.tab_open_click)
        self.ui.tabWidget.currentChanged.connect(self.current_tab_changed)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)'''

        # ==> SHORTCUTS

        self.shortcut_new_tab = QShortcut(QKeySequence('Ctrl+t'), self)
        self.shortcut_new_tab.activated.connect(self.add_tab)

        self.shortcut_close_tab = QShortcut(QKeySequence('Ctrl+w'), self)
        self.shortcut_close_tab.activated.connect(self.close_tab)

        self.shortcut_back = QShortcut(QKeySequence('Alt+left'), self)
        self.shortcut_back.activated.connect(self.back_page)

        self.shortcut_next = QShortcut(QKeySequence('Alt+right'), self)
        self.shortcut_next.activated.connect(self.next_page)

        self.shortcut_reload = QShortcut(QKeySequence('Ctrl+r'), self)
        self.shortcut_reload.activated.connect(self.reload)

        self.shortcut_print = QShortcut(QKeySequence('Ctrl+p'), self)
        self.shortcut_print.activated.connect(self.print)

        self.shortcut_open_file = QShortcut(QKeySequence('Ctrl+o'), self)
        self.shortcut_open_file.activated.connect(self.open_file)

        self.shortcut_save_page = QShortcut(QKeySequence('Ctrl+s'), self)
        self.shortcut_save_page.activated.connect(self.save_page)

        self.shortcut_view_source_code = QShortcut(
            QKeySequence('Ctrl+u'), self)
        self.shortcut_view_source_code.activated.connect(
            self.view_source_code)

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
