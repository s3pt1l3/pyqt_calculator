from PyQt5 import QtWidgets
from ui import Calculator
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
