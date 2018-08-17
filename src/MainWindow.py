import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from DebtWidget import *

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUi()

    def initUi(self):
        self.resize(300,500)
        self.setWindowTitle('Financial Application')

        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        self.debtInfo = DebtWidget()

        self.layout.addWidget(self.debtInfo)

