import sys
from MainWindow import *

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
