from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import Translator, LANGUAGES


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 478)
        Form.setMinimumSize(QtCore.QSize(400, 478))
        Form.setMaximumSize(QtCore.QSize(400, 478))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color:rgb(254, 255, 161)")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(15, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("background-color:rgb(255, 196, 16);\n"
                                 "font: 75 bold 14pt \"SansSerif\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.plainTextEditInput = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEditInput.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                              "font: 75 bold 14pt \"MS Shell Dlg 2\";")
        self.plainTextEditInput.setObjectName("plainTextEditInput")
        self.gridLayout.addWidget(self.plainTextEditInput, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 2)
        self.comboBoxInput = QtWidgets.QComboBox(Form)
        self.comboBoxInput.setStyleSheet("background-color: rgb(255, 187, 202)")
        self.comboBoxInput.setObjectName("comboBoxInput")
        self.gridLayout.addWidget(self.comboBoxInput, 3, 0, 1, 1)
        self.comboBoxOutput = QtWidgets.QComboBox(Form)
        self.comboBoxOutput.setStyleSheet("background-color: rgb(255, 187, 202)")
        self.comboBoxOutput.setObjectName("comboBoxOutput")
        self.gridLayout.addWidget(self.comboBoxOutput, 3, 1, 1, 1)
        self.plainTextEditOutput = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEditOutput.setStyleSheet("background-color: rgb(85, 255, 255);\n"
                                               "font: 75 bold 14pt \"MS Shell Dlg 2\";")
        self.plainTextEditOutput.setObjectName("plainTextEditOutput")
        self.gridLayout.addWidget(self.plainTextEditOutput, 5, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonTranslate = QtWidgets.QPushButton(Form)
        self.pushButtonTranslate.setStyleSheet("background-color: rgb(136, 255, 0);\n"
                                               "font: 75 bold 14pt \"MS Sans Serif\";")
        self.pushButtonTranslate.setObjectName("pushButtonTranslate")
        self.horizontalLayout.addWidget(self.pushButtonTranslate)
        self.pushButtonClear = QtWidgets.QPushButton(Form)
        self.pushButtonClear.setMinimumSize(QtCore.QSize(51, 31))
        self.pushButtonClear.setMaximumSize(QtCore.QSize(51, 31))
        self.pushButtonClear.setStyleSheet("background-color: rgb(255, 58, 68)")
        self.pushButtonClear.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/Thrash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonClear.setIcon(icon1)
        self.pushButtonClear.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout.addWidget(self.pushButtonClear)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 8, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 6, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.plainTextEditInput.setPlaceholderText('Type Your Text here!')
        self.plainTextEditOutput.setPlaceholderText('Your Translated Text will appear here!')
        self.AddLanguages()
        self.pushButtonTranslate.clicked.connect(self.Function)
        self.pushButtonClear.clicked.connect(self.Clear)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Translator --Arvind"))
        self.label.setText(_translate("Form", "Translator"))
        self.pushButtonTranslate.setText(_translate("Form", "Translate →"))

    def AddLanguages(self):
        for i in LANGUAGES.values():
            self.comboBoxInput.addItem(i.capitalize())
            self.comboBoxOutput.addItem(i.capitalize())

    def Function(self):
        self.plainTextEditInput.setPlaceholderText('Type Your Text here!')
        self.plainTextEditOutput.setPlaceholderText('Your Translated Text will appear here!')
        inputlang = self.comboBoxInput.currentText()
        outputlang = self.comboBoxOutput.currentText()
        text = self.plainTextEditInput.toPlainText()

        translator = Translator()

        translated = translator.translate(text,
                                          src=inputlang,
                                          dest=outputlang)

        self.plainTextEditOutput.setPlainText(translated.text)

    def Clear(self):
        self.plainTextEditOutput.setPlainText('')
        self.plainTextEditInput.setPlainText('')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
