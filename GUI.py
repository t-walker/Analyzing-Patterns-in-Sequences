# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VM.ui'
#
# Created: Sun Jun 14 21:20:07 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from os import listdir
from os.path import isfile, join
from seq_identifier import call_main
from os.path import expanduser
home = expanduser("~")

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
        MainWindow.resize(422, 281)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.don_all_line = QtGui.QLineEdit(self.centralwidget)
        self.don_all_line.setObjectName(_fromUtf8("don_all_line"))
        self.horizontalLayout.addWidget(self.don_all_line)
        self.don_all_button = QtGui.QPushButton(self.centralwidget)
        self.don_all_button.setObjectName(_fromUtf8("don_all_button"))
        self.horizontalLayout.addWidget(self.don_all_button)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.inp_all_line = QtGui.QLineEdit(self.centralwidget)
        self.inp_all_line.setObjectName(_fromUtf8("inp_all_line"))
        self.horizontalLayout_2.addWidget(self.inp_all_line)
        self.inp_all_button = QtGui.QPushButton(self.centralwidget)
        self.inp_all_button.setObjectName(_fromUtf8("inp_all_button"))
        self.horizontalLayout_2.addWidget(self.inp_all_button)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.out_dir_line = QtGui.QLineEdit(self.centralwidget)
        self.out_dir_line.setObjectName(_fromUtf8("out_dir_line"))
        self.horizontalLayout_3.addWidget(self.out_dir_line)
        self.out_dir_button = QtGui.QPushButton(self.centralwidget)
        self.out_dir_button.setObjectName(_fromUtf8("out_dir_button"))
        self.horizontalLayout_3.addWidget(self.out_dir_button)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.min_pat_len = QtGui.QSpinBox(self.centralwidget)
        self.min_pat_len.setObjectName(_fromUtf8("min_pat_len"))
        self.horizontalLayout_4.addWidget(self.min_pat_len)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.min_gap_len = QtGui.QSpinBox(self.centralwidget)
        self.min_gap_len.setObjectName(_fromUtf8("min_gap_len"))
        self.horizontalLayout_5.addWidget(self.min_gap_len)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.max_gap_len = QtGui.QSpinBox(self.centralwidget)
        self.max_gap_len.setObjectName(_fromUtf8("max_gap_len"))
        self.horizontalLayout_6.addWidget(self.max_gap_len)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.formLayout.setLayout(7, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.run = QtGui.QPushButton(self.centralwidget)
        self.run.setObjectName(_fromUtf8("run"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.run)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.progressBar)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtGui.QFormLayout.LabelRole, spacerItem5)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.inp_all_button.clicked.connect(self.input_buttonClicked)
        self.out_dir_button.clicked.connect(self.output_buttonClicked)
        self.don_all_button.clicked.connect(self.donor_buttonClicked)
        self.run.clicked.connect(self.analyze)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sequence Pattern Analyzer", None))
        self.label.setText(_translate("MainWindow", "Donor Alleles File", None))
        self.don_all_button.setText(_translate("MainWindow", "Open...", None))
        self.label_3.setText(_translate("MainWindow", "Output Directory", None))
        self.label_2.setText(_translate("MainWindow", "Input Alleles File", None))
        self.inp_all_button.setText(_translate("MainWindow", "Open...", None))
        self.out_dir_button.setText(_translate("MainWindow", "Open..", None))
        self.label_4.setText(_translate("MainWindow", "Minimum Pattern Length", None))
        self.label_5.setText(_translate("MainWindow", "Minimum Gap Length", None))
        self.label_6.setText(_translate("MainWindow", "Maximum Gap Length", None))
        self.run.setText(_translate("MainWindow", "Run...", None))

    def donor_buttonClicked(self):
        self.don_all_line.setText(QtGui.QFileDialog.getOpenFileName())

    def input_buttonClicked(self):
        self.inp_all_line.setText(QtGui.QFileDialog.getExistingDirectory())

    def output_buttonClicked(self):
        self.out_dir_line.setText(QtGui.QFileDialog.getExistingDirectory())

    def analyze(self):
        self.progressBar.setProperty("value", 0)
        donor_file = ""
        input_files = []
        output_directory = ""

        minimum_pattern_length = 0
        minimum_gap_length = 0
        maximum_gap_length = 0

        donor_file = str(self.don_all_line.text())
        input_path = str(self.inp_all_line.text())
        input_files = listdir(str(self.inp_all_line.text()))
        output_directory = str(self.out_dir_line.text())

        minimum_pattern_length = self.min_pat_len.value()
        minimum_gap_length = self.min_gap_len.value()
        maximum_gap_lengh = self.max_gap_len.value()

        count = 0
        for sample in input_files:
            call_main(donor_file, input_path, sample, minimum_pattern_length, minimum_pattern_length, maximum_gap_length, output_directory)
            count += 1
            self.progressBar.setProperty("value", (count / len(input_files)*100))

        return


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
