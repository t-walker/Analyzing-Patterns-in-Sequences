# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VM.ui'
#
# Created: Sun May 31 22:48:51 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui
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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 262)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.donor_line = QtGui.QLineEdit(self.centralwidget)
        self.donor_line.setObjectName(_fromUtf8("donor_line"))
        self.horizontalLayout_2.addWidget(self.donor_line)
        self.open_donorfile = QtGui.QPushButton(self.centralwidget)
        self.open_donorfile.setObjectName(_fromUtf8("open_donorfile"))
        self.horizontalLayout_2.addWidget(self.open_donorfile)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.output_line = QtGui.QLineEdit(self.centralwidget)
        self.output_line.setObjectName(_fromUtf8("output_line"))
        self.horizontalLayout_4.addWidget(self.output_line)
        self.open_outputdirectory = QtGui.QPushButton(self.centralwidget)
        self.open_outputdirectory.setObjectName(_fromUtf8("open_outputdirectory"))
        self.horizontalLayout_4.addWidget(self.open_outputdirectory)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.run = QtGui.QPushButton(self.centralwidget)
        self.run.setObjectName(_fromUtf8("run"))
        self.horizontalLayout_5.addWidget(self.run)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        spacerItem3 = QtGui.QSpacerItem(40, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.LabelRole, spacerItem3)
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setObjectName(_fromUtf8("status"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.status)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.input_line = QtGui.QLineEdit(self.centralwidget)
        self.input_line.setObjectName(_fromUtf8("input_line"))
        self.horizontalLayout_3.addWidget(self.input_line)
        self.open_inputdirectory = QtGui.QPushButton(self.centralwidget)
        self.open_inputdirectory.setObjectName(_fromUtf8("open_inputdirectory"))
        self.horizontalLayout_3.addWidget(self.open_inputdirectory)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        #CUSTOM
        self.open_inputdirectory.clicked.connect(self.input_buttonClicked)
        self.open_outputdirectory.clicked.connect(self.output_buttonClicked)
        self.open_donorfile.clicked.connect(self.donor_buttonClicked)
        #END CUSTOM

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FASTA Pattern Analyzer", None))
        self.open_donorfile.setText(_translate("MainWindow", "Open...", None))
        self.label.setText(_translate("MainWindow", "Donor Alleles File", None))
        self.label_2.setText(_translate("MainWindow", "Input Alleles Directory", None))
        self.label_3.setText(_translate("MainWindow", "Output Directory", None))
        self.open_outputdirectory.setText(_translate("MainWindow", "Open...", None))
        self.run.setText(_translate("MainWindow", "Run...", None))
        self.status.setText(_translate("MainWindow", "Waiting for data...", None))
        self.open_inputdirectory.setText(_translate("MainWindow", "Open...", None))

    def donor_buttonClicked(self):
        self.donor_line.setText(QtGui.QFileDialog.getOpenFileName())

    def input_buttonClicked(self):
        self.input_line.setText(QtGui.QFileDialog.getExistingDirectory())

    def output_buttonClicked(self):
        self.output_line.setText(QtGui.QFileDialog.getExistingDirectory())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
