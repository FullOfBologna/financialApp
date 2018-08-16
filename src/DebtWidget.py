from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DebtWidget(QWidget):
    def __init__(self):
        super(DebtWidget,self).__init__()

        self.initUi()


    def initUi(self):
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        self.BalanceInit()
        self.InterestInit()
        self.FrequencyInit()
        self.RemainingLengthInit()

    #-------Initialize GUI Elements for inputing Remaining Balance-------#
    def BalanceInit(self):
        self.balanceLabel = QLabel("Balance Remaining")
        self.layout.addWidget(self.balanceLabel,0,0,1,1)

        self.balanceLineEdit = QLineEdit()
        self.layout.addWidget(self.balanceLineEdit,0,1,1,1)

    #-------Initialize GUI Elements for Inputing Interest Rate-------#
    def InterestInit(self):
        self.interestLabel = QLabel("Interest Rate")
        self.layout.addWidget(self.interestLabel,1,0,1,1)

        self.interestLineEdit = QLineEdit()
        self.layout.addWidget(self.interestLineEdit,1,1,1,1)

    #-------Initialize GUI Elements for inputing Payment Frequency-------#
    def FrequencyInit(self):
        self.frequencyLabel = QLabel("Payment Frequency")
        self.layout.addWidget(self.frequencyLabel,2,0,1,1)

        self.frequencyComboBox = QComboBox()
        self.layout.addWidget(self.frequencyComboBox,2,1,1,1)

    #-------Initialize GUI Elements for Inputing Remaining Lenght of Loan-------#
    def RemainingLengthInit(self):
        self.remainingLengthLabel = QLabel("Remianing Lenght of Loan (months)")
        self.layout.addWidget(self.remainingLengthLabel,3,0,1,1)

        self.remainingLengthLineEdit = QLineEdit()
        self.layout.addWidget(self.remainingLengthLineEdit,3,1,1,1)

