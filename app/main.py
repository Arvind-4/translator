from googletrans import LANGUAGES, Translator
from PyQt5 import QtCore, QtGui, QtWidgets

from app.config import ICON_FILE, TRASH_FILE


class UIForm(object):
    def setup_ui(self, form: QtWidgets.QWidget):
        form.setObjectName("form")
        form.setMinimumHeight(750)
        form.setMinimumWidth(1000)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(str(ICON_FILE)), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        form.setWindowIcon(icon)
        form.setStyleSheet("background-color:rgb(254, 255, 161)")
        self.gridLayout_2 = QtWidgets.QGridLayout(form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            15, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(form)
        self.label.setStyleSheet(
            "background-color:rgb(255, 196, 16);\n" 'font: 75 bold 14pt "SansSerif";'
        )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.plainTextEditInput = QtWidgets.QPlainTextEdit(form)
        self.plainTextEditInput.setStyleSheet(
            "background-color: rgb(85, 255, 255);\n"
            'font: 75 bold 14pt "MS Shell Dlg 2";'
        )
        self.plainTextEditInput.setObjectName("plainTextEditInput")
        self.gridLayout.addWidget(self.plainTextEditInput, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 2)
        self.comboBoxInput = QtWidgets.QComboBox(form)
        self.comboBoxInput.setObjectName("comboBoxInput")
        self.gridLayout.addWidget(self.comboBoxInput, 3, 0, 1, 1)
        self.comboBoxOutput = QtWidgets.QComboBox(form)
        self.comboBoxOutput.setObjectName("comboBoxOutput")
        self.gridLayout.addWidget(self.comboBoxOutput, 3, 1, 1, 1)
        self.plainTextEditOutput = QtWidgets.QPlainTextEdit(form)
        self.plainTextEditOutput.setStyleSheet(
            "background-color: rgb(85, 255, 255);\n"
            'font: 75 bold 14pt "MS Shell Dlg 2";'
        )
        self.plainTextEditOutput.setObjectName("plainTextEditOutput")
        self.gridLayout.addWidget(self.plainTextEditOutput, 5, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonTranslate = QtWidgets.QPushButton(form)
        self.pushButtonTranslate.setStyleSheet(
            "background-color: rgb(136, 255, 0);\n"
            'font: 75 bold 14pt "MS Sans Serif";'
        )
        self.pushButtonTranslate.setObjectName("pushButtonTranslate")
        self.horizontalLayout.addWidget(self.pushButtonTranslate)
        self.pushButtonClear = QtWidgets.QPushButton(form)
        self.pushButtonClear.setMinimumSize(QtCore.QSize(51, 31))
        self.pushButtonClear.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonClear.setStyleSheet("background-color: rgb(255, 58, 68)")
        self.pushButtonClear.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(str(TRASH_FILE)), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.pushButtonClear.setIcon(icon1)
        self.pushButtonClear.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout.addWidget(self.pushButtonClear)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem3, 8, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem4, 6, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.re_translator_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

        self.plainTextEditInput.setPlaceholderText("Type Your Text here!")
        self.plainTextEditOutput.setPlaceholderText(
            "Your Translated Text will appear here!"
        )
        self.add_languages()
        self.pushButtonTranslate.clicked.connect(self.translator_function)
        self.pushButtonClear.clicked.connect(self.clear_function)

    def re_translator_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Translator --Arvind"))
        self.label.setText(_translate("form", "Translator"))
        self.pushButtonTranslate.setText(_translate("form", "Translate →"))

    def add_languages(self):
        for i in LANGUAGES.values():
            self.comboBoxInput.addItem(i.capitalize())
            self.comboBoxOutput.addItem(i.capitalize())
        self.comboBoxInput.setStyleSheet(
            "QComboBox {background-color: rgb(255, 187, 202);combobox-popup: 0; }"
        )
        self.comboBoxOutput.setStyleSheet(
            "QComboBox {background-color: rgb(255, 187, 202);combobox-popup: 0; }"
        )

    def translator_function(self):
        self.plainTextEditInput.setPlaceholderText("Type Your Text here!")
        self.plainTextEditOutput.setPlaceholderText(
            "Your Translated Text will appear here!"
        )
        inputlang = self.comboBoxInput.currentText()
        outputlang = self.comboBoxOutput.currentText()
        text = self.plainTextEditInput.toPlainText()

        translator = Translator()

        translated = translator.translate(text, src=inputlang, dest=outputlang)

        self.plainTextEditOutput.setPlainText(translated.text)

    def clear_function(self):
        self.plainTextEditOutput.setPlainText("")
        self.plainTextEditInput.setPlainText("")
