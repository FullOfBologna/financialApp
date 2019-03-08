import sys

from DebtWidget import *

import PlotWidget

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUi()

    def initUi(self):
        self.resize(1500,1300)
        self.setWindowTitle('Financial Application')
        
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.file_menu = QtWidgets.QMenu('&File',self)
        self.file_menu.addAction('&Quit',self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)

        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QtWidget.QMenu('&Help',self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About',self.about)

        self.mainWidget = QWidgets
        
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        
        #Have main window be a largge screen view with blank widgets to start. Will have 
        #several sections for various different data point

    
        #self.debtInfo = DebtWidget()

        #self.layout.addWidget(self.debtInfo)

