import sys
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_konto(object):
    def newaccount(self):
        name = self.lineEdit.text()
        passwort = self.lineEdit_2.text()
        # SQL Datenbank
        con = sqlite3.connect("Konto.db")
        cur = con.cursor()
        cur.execute("INSERT INTO Konto (Benutzername, Passwort) VALUES (?, ?)",
                    (name, passwort))
        con.commit()
        con.close()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(623, 649)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 470, 221, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.newaccount)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 180, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 240, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 280, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 340, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 70, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Konto erstellen"))
        self.label_2.setText(_translate("Dialog", "Passwort"))
        self.label_4.setText(_translate("Dialog", "Benutzname"))
        self.label.setText(_translate("Dialog", "Konto erstellen"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_konto()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())