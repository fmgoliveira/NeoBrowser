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

    def UiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        self.ui.btn_close.clicked.connect(lambda: self.close())

    def returnStatus(self):
        return GLOBAL_STATE
        