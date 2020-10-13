from window_ui import *
from googlesearch import search

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("SQLI Searcher")

        app_icon = QtGui.QIcon()
        app_icon.addFile('icon.jpg', QtCore.QSize(16,16))
        app_icon.addFile('icon.jpg', QtCore.QSize(24,24))
        app_icon.addFile('icon.jpg', QtCore.QSize(32,32))
        app_icon.addFile('icon.jpg', QtCore.QSize(48,48))
        app_icon.addFile('icon.jpg', QtCore.QSize(256,256))
        self.setWindowIcon(app_icon)

        self.searchButton.clicked.connect(self.buttonClicked)

        self.clearButton.clicked.connect(self.clearTable)
    def buttonClicked(self):
        query = self.DorksList.currentText()
        results = self.results.value()

        self.search(query, results)

    def search(self, query, results):
        for i in search(query, num=results, stop=results, pause=2):
            self.urlTable.addItem(i)

    def clearTable(self):
        self.urlTable.clear()

if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()