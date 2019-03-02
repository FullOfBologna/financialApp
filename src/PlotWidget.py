from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from matplotlib import *

matplotlib.use('QT5Agg')

class MplCanvas(FigureCanvasQtAgg):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add.subplot(111)
        FigureCanvasQtAgg.__init__(self,self.fig)
        FigureCanvasQtAgg.setSizePolicy(self,
                                        QtWidgets.QSizePolicy.Expanding,
                                        QtWidgets.QSizePolicy.Expanding)

        FigureCanvasQtAgg.updateGeometry(self)

#MatPlotLib Widget
class MplWidget(QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)    #inherit from QWidget
        self.canvas = MplCanvas()                   #create canvas object
        self.vBoxLayout = QtWidgets.QVBoxLayout()   #set box for plotting
        self.vBoxLayout.addWidget(self.canvas)
        self.setLayout(self.vboxLayout)

        

