# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VM.ui'
#
# Created: Sun Jun 14 21:20:07 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from os import listdir, getcwd
from os.path import isfile, join
from seq_identifier import call_main
from os.path import expanduser
from reportlab import rl_settings
import threading

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

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 300)
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
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.inp_all_line = QtGui.QLineEdit(self.centralwidget)
        self.inp_all_line.setObjectName(_fromUtf8("inp_all_line"))
        self.horizontalLayout_2.addWidget(self.inp_all_line)
        self.inp_all_button = QtGui.QPushButton(self.centralwidget)
        self.inp_all_button.setObjectName(_fromUtf8("inp_all_button"))
        self.horizontalLayout_2.addWidget(self.inp_all_button)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
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
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_9.addWidget(self.label_7)
        self.min_pat_len = QtGui.QSpinBox(self.centralwidget)
        self.min_pat_len.setObjectName(_fromUtf8("min_pat_len"))
        self.verticalLayout_9.addWidget(self.min_pat_len)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_9.addWidget(self.label_8)
        self.min_gap_len = QtGui.QSpinBox(self.centralwidget)
        self.min_gap_len.setObjectName(_fromUtf8("min_gap_len"))
        self.verticalLayout_9.addWidget(self.min_gap_len)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_9.addWidget(self.label_6)
        self.max_gap_len = QtGui.QSpinBox(self.centralwidget)
        self.max_gap_len.setObjectName(_fromUtf8("max_gap_len"))
        self.verticalLayout_9.addWidget(self.max_gap_len)
        self.horizontalLayout_11.addLayout(self.verticalLayout_9)
        self.image = QtGui.QLabel()
        self.horizontalLayout_11.addWidget(self.image)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_11)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.run = QtGui.QPushButton(self.centralwidget)
        self.run.setObjectName(_fromUtf8("run"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.run)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.progressBar)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Donor Alleles File", None))
        self.don_all_button.setText(_translate("MainWindow", "Open...", None))
        self.label_2.setText(_translate("MainWindow", "Input Alleles Directory", None))
        self.inp_all_button.setText(_translate("MainWindow", "Open...", None))
        self.label_3.setText(_translate("MainWindow", "Output Directory", None))
        self.out_dir_button.setText(_translate("MainWindow", "Open..", None))
        self.label_4.setText(_translate("MainWindow", "", None))
        self.label_7.setText(_translate("MainWindow", "Minimum Pattern Length", None))
        self.label_8.setText(_translate("MainWindow", "Minimum Gap Length", None))
        self.label_6.setText(_translate("MainWindow", "Maximum Gap Length", None))
        self.run.setText(_translate("MainWindow", "Run...", None))
        self.pixmap = QtGui.QPixmap(getcwd() + "/SequencePatternAnalyzer.png")
        self.pixmap.scaled(75,74, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_all_button.clicked.connect(self.input_buttonClicked)
        self.out_dir_button.clicked.connect(self.output_buttonClicked)
        self.don_all_button.clicked.connect(self.donor_buttonClicked)
        self.run.clicked.connect(self.analyze)


    def donor_buttonClicked(self):
        self.don_all_line.setText(QtGui.QFileDialog.getOpenFileName())

    def input_buttonClicked(self):
        self.inp_all_line.setText(QtGui.QFileDialog.getExistingDirectory())

    def output_buttonClicked(self):
        self.out_dir_line.setText(QtGui.QFileDialog.getExistingDirectory())

    def run_sample(self, sample):
        minimum_pattern_length = self.min_pat_len.value()
        minimum_gap_length = self.min_gap_len.value()
        maximum_gap_length = self.max_gap_len.value()

        donor_file = str(self.don_all_line.text())
        input_path = str(self.inp_all_line.text())
        output_directory = str(self.out_dir_line.text())

        call_main(donor_file, input_path, sample, minimum_pattern_length, minimum_gap_length, maximum_gap_length, output_directory)
        self.count += 1
        self.val = (float(self.count)/float(len(self.usable_files)))*100
        self.progressBar.setValue(self.val)
        return

    def analyze(self):
        self.progressBar.setProperty("value", 0)
        self.count = 0
        donor_file = ""
        input_files = []
        self.usable_files = []
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
        print("\n\n\n\n")
        print(minimum_gap_length)
        print(minimum_pattern_length)
        print(maximum_gap_lengh)
        threads = []
        for sample in input_files:
            if sample[-2:] == "fa" or sample[-5:] == "fasta":
                self.usable_files.append(sample)

        for sample in self.usable_files:
                t = threading.Thread(target=self.run_sample, args=(sample,))
                threads.append(t)
                t.daemon = True
                t.start()
        return


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
