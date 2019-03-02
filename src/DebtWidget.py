from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from matplotlib import * 

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
        self.MinimumPaymentInit()
        self.RemainingLengthInit()
        
        self.CalculateButton = QPushButton("Calculate")
        self.CalculateButton.clicked.connect(lambda: self.CalculateDebtPayoff())

        self.layout.addWidget(self.CalculateButton,6,0,1,2)

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

    #-------Initialize GUI Elements for inputting minimum Payment-------#
    def MinimumPaymentInit(self):
        self.minimumPaymentLabel = QLabel("Minimum Payment")
        self.layout.addWidget(self.minimumPaymentLabel,3,0,1,1)

        self.minimumPaymentEdit = QLineEdit()
        self.layout.addWidget(self.minimumPaymentEdit, 3,1,1,1)

    #-------Initialize GUI Elements for inputting minimum Payment-------#
    def ExtraPaymentInit(self):
        self.extraPaymentLabel = QLabel("Extra Payment")
        self.layout.addWidget(self.extraPaymentLabel,3,0,1,1)

        self.extraPaymentEdit = QLineEdit()
        self.layout.addWidget(self.extraPaymentEdit, 3,1,1,1)

    #-------Initialize GUI Elements for Inputing Remaining Lenght of Loan-------#
    def RemainingLengthInit(self):
        self.remainingLengthLabel = QLabel("Remianing Lenght of Loan (months)")
        self.layout.addWidget(self.remainingLengthLabel,4,0,1,1)

        self.remainingLengthLineEdit = QLineEdit()
        self.layout.addWidget(self.remainingLengthLineEdit,4,1,1,1)

    

    def CalculateDebtPayoff(self):
        balance = 0.0
        interestRate = 0.0
        minimumPayment = 0.0
        extraPayment = 0.0

        balanceRemainingList = []
        totalMonthlyInterestList = []
        totalInterestPaid = 0
        

        balanceSet = False
        interestRateSet = False
        minimumPaymentSet = False
        

        if self.balanceLineEdit.text() != "": 
            balance = self.balanceLineEdit.getText().toFloat()
            #print balance
            balanceSet = True;
        
        if self.interestLineEdit.text() != "":
            if ((interestRate > 0) and (interestRate < 100)):
                interestRate = self.interestRate.getText().toFloat()/100
                interestRateSet = True;

        if self.minimumPaymentEdit.text() != "":
            minimumPayment = self.minimumPaymentEdit.getText().toFloat()
            minimumPaymentSet = True
        
        dateOfPayment = 01

        if balanceSet and interestRateSet and minimumPaymentSet:
            currentBalance = balance
            currentDate = QDate.currentDate()
            while(currentBalance > 0):
                currentBalance = currentBalance*(1+interestRate)
                totalInterest = totalInterest + (currentBalance*interestRate)
                totalMonthlyInterest = totalMonthlyInterest + (currentBalance*interestRate)

                currentDate.addDays(1)

                if(currentDate.day() == dateOfPayment):
                    qDebug('current Day = ', dateOfPayment)
                    currentBalance = currentBalance - minimumPayment

                    totalMonthlyInterestList.append(totalMonthlyInterest)
                    
                    print "Total Monthly Interest Paid: ", totalMonthlyInterest
                    
                    totalMonthlyInterest = 0

           #Debt Widget makes a call to pop up a matbplotlib plot with incremental payment options. 

        


