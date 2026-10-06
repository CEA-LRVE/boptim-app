from PySide6 import QtWidgets
from boptim_app.ui.widgets import MyWidget
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())