# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'te.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 153)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.P1 = QtWidgets.QLabel(self.centralwidget)
        self.P1.setGeometry(QtCore.QRect(20, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.P1.setFont(font)
        self.P1.setObjectName("P1")
        self.X1 = QtWidgets.QLabel(self.centralwidget)
        self.X1.setGeometry(QtCore.QRect(200, 90, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.X1.setFont(font)
        self.X1.setObjectName("X1")
        self.Y1 = QtWidgets.QLabel(self.centralwidget)
        self.Y1.setGeometry(QtCore.QRect(290, 90, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Y1.setFont(font)
        self.Y1.setObjectName("Y1")
        self.E1 = QtWidgets.QLabel(self.centralwidget)
        self.E1.setGeometry(QtCore.QRect(110, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.E1.setFont(font)
        self.E1.setObjectName("E1")
        self.Z1 = QtWidgets.QLabel(self.centralwidget)
        self.Z1.setGeometry(QtCore.QRect(370, 90, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Z1.setFont(font)
        self.Z1.setObjectName("Z1")
        self.P = QtWidgets.QLabel(self.centralwidget)
        self.P.setGeometry(QtCore.QRect(20, 30, 50, 50))
        self.P.setText("")
        self.P.setObjectName("P")
        self.E = QtWidgets.QLabel(self.centralwidget)
        self.E.setGeometry(QtCore.QRect(110, 30, 50, 50))
        self.E.setText("")
        self.E.setObjectName("E")
        self.X = QtWidgets.QLabel(self.centralwidget)
        self.X.setGeometry(QtCore.QRect(200, 30, 50, 50))
        self.X.setText("")
        self.X.setObjectName("X")
        self.Y = QtWidgets.QLabel(self.centralwidget)
        self.Y.setGeometry(QtCore.QRect(290, 30, 50, 50))
        self.Y.setText("")
        self.Y.setObjectName("Y")
        self.Z = QtWidgets.QLabel(self.centralwidget)
        self.Z.setGeometry(QtCore.QRect(370, 30, 50, 50))
        self.Z.setText("")
        self.Z.setObjectName("Z")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.P1.setText(_translate("MainWindow", "POWER"))
        self.X1.setText(_translate("MainWindow", "X-axis"))
        self.Y1.setText(_translate("MainWindow", "Y-axis"))
        self.E1.setText(_translate("MainWindow", "ERROR"))
        self.Z1.setText(_translate("MainWindow", "Z-axis"))
