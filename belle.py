
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()

label = QLabel(window)
label.setText("Hello Sz")
label.move(200, 200)

window.show()

sys.exit(app.exec_())