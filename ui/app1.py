from PyQt5 import QtWidgets, uic
import sys


class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('ui/app1.ui',self)

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
app.exec_()