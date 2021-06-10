from main import *

class TabFunctions(Ui_Browser):
    def addTab(self, qurl=None, label="Untitled"):
        if qurl is None:
            qurl = QUrl('file:///html/home.html')

        browser = QWebEngineView()
        page = WebEnginePage(browser)
        browser.setPage(page)
        browser.setUrl(qurl)
        page.printRequested.connect(self.printRequested)
        QtWebEngineWidgets.QWebEngineProfile.defaultProfile(
        ).downloadRequested.connect(self.on_downloadRequested)

        i = self.ui.tabWidget.addTab(browser, label)

        self.ui.tabWidget.setCurrentIndex(i)

        self.ui.tabWidget.setTabIcon(i, browser.page().icon())

        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.ui.tabWidget.setTabText(i, browser.page().title()))

        browser.iconChanged.connect(lambda _, i=i, browser=browser:
                                     self.ui.tabWidget.setTabIcon(i, browser.icon()))
