# -*- coding: utf-8 -*-
# Quick Change
# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created: Mon Aug 18 18:54:30 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

#CUSTOM 
from PyQt4.QtGui import QFileDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    
    #CUSTOM
    def selectFile_a(self):
        self.Source_A.setText(QFileDialog.getOpenFileName())
    
    def selectFile_b(self): 
        self.Source_B.setText(QFileDialog.getOpenFileName())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(325, 222)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 281, 27))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.gridLayout = QtGui.QGridLayout(self.horizontalLayoutWidget_3)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.Destination = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.Destination.setObjectName(_fromUtf8("Destination"))
        self.gridLayout.addWidget(self.Destination, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.dest_push = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.dest_push.setObjectName(_fromUtf8("dest_push"))
        self.horizontalLayout_5.addWidget(self.dest_push)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.Analyze = QtGui.QPushButton(self.centralwidget)
        self.Analyze.setGeometry(QtCore.QRect(220, 150, 75, 23))
        self.Analyze.setObjectName(_fromUtf8("Analyze"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 43, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 41, 42, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(69, 10, 221, 25))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Source_A = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.Source_A.setObjectName(_fromUtf8("Source_A"))
        self.horizontalLayout_2.addWidget(self.Source_A)
        self.a_push = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.a_push.setObjectName(_fromUtf8("a_push"))
        self.horizontalLayout_2.addWidget(self.a_push)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(69, 41, 221, 25))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Source_B = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.Source_B.setObjectName(_fromUtf8("Source_B"))
        self.horizontalLayout_3.addWidget(self.Source_B)
        self.b_push = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.b_push.setObjectName(_fromUtf8("b_push"))
        self.horizontalLayout_3.addWidget(self.b_push)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFiles = QtGui.QMenu(self.menubar)
        self.menuFiles.setObjectName(_fromUtf8("menuFiles"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFiles.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #CUSTOM
        self.a_push.clicked.connect(self.selectFile_a)
        self.b_push.clicked.connect(self.selectFile_b)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Destination", None))
        self.dest_push.setText(_translate("MainWindow", "Browse...", None))
        self.Analyze.setText(_translate("MainWindow", "Analyze", None))
        self.label.setText(_translate("MainWindow", "Source A   f", None))
        self.label_2.setText(_translate("MainWindow", "Source B", None))
        self.a_push.setText(_translate("MainWindow", "Browse...", None))
        self.b_push.setText(_translate("MainWindow", "Browse...", None))
        self.menuFiles.setTitle(_translate("MainWindow", "Files", None))
        self.actionAbout.setText(_translate("MainWindow", "About... ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
