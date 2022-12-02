import sys
import sqlite3
from konto import Ui_konto
from Kassensystem_mit_SQL_Datenbank import Ui_Kasse
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def openkonto(self):
        # SQL Datenbank erstellen und befüllen
        con = sqlite3.connect("Konto.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Konto(Benutzername TEXT, Passwort TEXT, Passwort2 TEXT)")
        con.commit()
        con.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_konto()
        self.ui.setupUi(self.window)
        self.window.show()

    def openKasse(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kasse()
        self.ui.setupUi(self.window)
        self.window.show()

    def login(self):
        Benutzername = self.lineEdit.text()
        Passwort = self.lineEdit_2.text()
        con = sqlite3.connect("Konto.db")
        cur = con.cursor()
        query = "SELECT Passwort FROM Konto"
        cur.execute(query)
        result = cur.fetchone()[0]
        query2 = "SELECT Benutzername FROM Konto"
        cur.execute(query2)
        result2 = cur.fetchone()[0]
        if result == Passwort and result2 == Benutzername:
            self.openKasse()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
        else:
            self.label.setText("Benutzername oder Passwort falsch")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 651)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 270, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 420, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
# ---------------------------------------------------Anmelde Button funktion--------------------------------------------
        # Login für Kasse
        self.pushButton.clicked.connect(self.login)
        # Login Fenster schliessen
        # self.pushButton.clicked.connect(Dialog.close)
# ----------------------------------------------------------------------------------------------------------------------
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 200, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 310, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 540, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
# -----------------------------------------Konto anlegen Button funktion------------------------------------------------
        # Neues Konto erstellen funktion
        self.pushButton_2.clicked.connect(self.openkonto)
# ----------------------------------------------------------------------------------------------------------------------

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 380, 281, 21))
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setPointSize(12)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 50, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Passwort"))
        self.label_3.setText(_translate("Dialog", "Benutzername"))
        self.pushButton.setText(_translate("Dialog", "Anmelden"))
        self.pushButton_2.setText(_translate("Dialog", "Konto erstellen"))
        self.label.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", "Login"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
