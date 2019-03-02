import sys

from DebtWidget import *

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUi()

    def initUi(self):
        self.resize(1500,1300)
        self.setWindowTitle('Financial Application')

        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        
        #Have main window be a largge screen view with blank widgets to start. Will have 
        #several sections for various different data point

    
        #self.debtInfo = DebtWidget()

        #self.layout.addWidget(self.debtInfo)

