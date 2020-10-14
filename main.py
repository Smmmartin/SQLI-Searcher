from window_ui import *
from googlesearch import search
from sys import platform

class MainWindow(QtWidgets.QMainWindow, QtWidgets.QListWidget, QtWidgets.QFileDialog, Ui_MainWindow):
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

        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.clearButton.clicked.connect(self.clearTable)
        self.saveButton.clicked.connect(self.saveTXT)

    def searchButtonClicked(self):
        query = self.DorksList.currentText()
        results = self.results.value()

        self.search(query, results)

    def search(self, query, results):
        for i in search(query, num=results, stop=results, pause=2):
            self.urlTable.addItem(i)

    def clearTable(self):
        self.urlTable.clear()

    def saveTXT(self):
        items = self.urlTable.count()
        if (platform == "win32"):
            urls = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '%HOMEPATH%/urls', filter='*.txt')
        elif (platform == "linux" or "linux2"):
            urls =QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '/home/alex/urls', filter='*.txt')
        print(items)

        for i in str(items):
            print("hola")

if __name__=="__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
