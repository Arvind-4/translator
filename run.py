import os
import sys

from PyQt5 import QtWidgets

from app.main import UIForm

os.environ["XDG_SESSION_TYPE"] = "xcb"


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = UIForm()
    ui.setup_ui(form)
    form.show()
    sys.exit(app.exec_())
