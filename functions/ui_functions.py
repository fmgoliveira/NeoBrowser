from main import *
import json

with open('config.json') as file:
    data = json.load(file)

GLOBAL_STATE = 0 if data["maximized"] else 1

class UIFunctions(Browser):
    def maximize_restore(self):

        global GLOBAL_STATE
        global data
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1

            self.ui.verticalLayout.setContentsMargins(0,0,0,0)

            self.ui.bottom_frame.setStyleSheet("background-color: rgb(45,45,45); border-bottom-left-radius: 0px; border-bottom-right-radius: 0px")
            self.ui.title_frame.setStyleSheet("QFrame#title_frame {\n"
"    background-color: rgb(20, 20, 20); border-top-right-radius: 0px; border-top-left-radius: 0px\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(144, 144, 144);\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    font-family: entypo;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #E8960C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #FF8000;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}")

            with open('config.json', 'w+') as outfile:
                data["maximized"] = True
                json.dump(data, outfile)

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)

            with open('config.json', 'w+') as outfile:
                data["maximized"] = False
                json.dump(data, outfile)

            self.ui.verticalLayout.setContentsMargins(10,10,10,10)

            self.ui.bottom_frame.setStyleSheet("background-color: rgb(45,45,45); border-bottom-left-radius: 20px; border-bottom-right-radius: 20px")
            self.ui.title_frame.setStyleSheet("QFrame#title_frame {\n"
"    background-color: rgb(20, 20, 20); border-top-right-radius: 20px; border-top-left-radius: 20px\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(0,0,0,0);\n"
"    color: rgb(144, 144, 144);\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    font-family: entypo;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #E8960C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #FF8000;\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"}")

    def UiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        self.ui.btn_close.clicked.connect(lambda: self.close())

    def returnStatus(self):
        return GLOBAL_STATE
        