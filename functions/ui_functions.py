from main import *
import json

with open('config.json') as file:
    data = json.load(file)

GLOBAL_STATE = 0 if data["maximized"] else 1

class UIFunctions(Browser):
    def maximize_restore(self):

        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1

            self.ui.verticalLayout.setContentsMargins(0,0,0,0)

            self.ui.title_frame.setStyleSheet("QFrame#title_frame { background-color: rgb(20, 20, 20); }  QPushButton { background-color: rgba(0,0,0,0); color: rgb(144, 144, 144); font: bold; font-size: 15px; font-family: entypo; }  QPushButton:hover { color: #E8960C; }  QPushButton:pressed { color: #FF8000; padding-left: 5px; padding-top: 5px; }")
            self.ui.bottom_frame.setStyleSheet("background-color: rgb(45, 45, 45)")

            with open('config.json', 'w') as outfile:
                data = {}
                data["maximized"] = True
                json.dump(data, outfile)

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)

            with open('config.json', 'w') as outfile:
                data = {}
                data["maximized"] = False
                json.dump(data, outfile)

            self.ui.verticalLayout.setContentsMargins(10,10,10,10)

            self.ui.title_frame.setStyleSheet("QFrame#title_frame { background-color: rgb(20, 20, 20); border-top-left-radius: 20px; border-top-right-radius: 20px; }  QPushButton { background-color: rgba(0,0,0,0); color: rgb(144, 144, 144); font: bold; font-size: 15px; font-family: entypo; }  QPushButton:hover { color: #E8960C; }  QPushButton:pressed { color: #FF8000; padding-left: 5px; padding-top: 5px; }")
            self.ui.bottom_frame.setStyleSheet("background-color: rgb(45, 45, 45); border-bottom-left-radius: 20px; border-bottom-right-radius: 20px; ")

    def UiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        self.ui.btn_close.clicked.connect(lambda: self.close())

    def returnStatus(self):
        return GLOBAL_STATE
        