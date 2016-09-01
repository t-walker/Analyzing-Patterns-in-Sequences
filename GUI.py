# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VM.ui'
#
# Created: Sun Jun 14 21:20:07 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
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

class analyzeSamplesThread(QThread):
    def __init__(self, sample_files, donor_file, input_path, output_directory,
                 min_len, min_gap, max_gap, st_anchor, en_anchor):
        QThread.__init__(self)
        self.samples = sample_files
        self.donor_file = donor_file
        self.input_path = input_path
        self.output_directory = output_directory
        self.min_len = min_len
        self.min_gap = min_gap
        self.max_gap = max_gap
        self.st_anchor = st_anchor
        self.en_anchor = en_anchor

    def __del__(self):
        self.wait()

    def _run_sample(self, sample):
        call_main(self.donor_file, self.input_path, sample, self.output_directory,
                  min_len=self.min_len, min_gap=self.min_gap, max_gap=self.max_gap,
                  st_anchor=self.st_anchor, en_anchor=self.en_anchor)

    def run(self):
        for sample in self.samples:
            self.emit(SIGNAL('processing(QString)'), sample)
            self._run_sample(sample)
            self.emit(SIGNAL('processed(QString)'), sample)
            self.sleep(1)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 300)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))

        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.image = QtGui.QLabel()
        self.horizontalLayout_11.addWidget(self.image, alignment=QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.don_all_line = QtGui.QLineEdit(self.centralwidget)
        self.don_all_line.setObjectName(_fromUtf8("don_all_line"))
        self.horizontalLayout.addWidget(self.don_all_line)
        self.don_all_button = QtGui.QPushButton(self.centralwidget)
        self.don_all_button.setObjectName(_fromUtf8("don_all_button"))
        self.don_all_button.setMaximumWidth(30)
        self.horizontalLayout.addWidget(self.don_all_button)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)

        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.inp_all_line = QtGui.QLineEdit(self.centralwidget)
        self.inp_all_line.setObjectName(_fromUtf8("inp_all_line"))
        self.horizontalLayout_2.addWidget(self.inp_all_line)
        self.inp_all_button = QtGui.QPushButton(self.centralwidget)
        self.inp_all_button.setObjectName(_fromUtf8("inp_all_button"))
        self.inp_all_button.setMaximumWidth(30)
        self.horizontalLayout_2.addWidget(self.inp_all_button)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)

        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.out_dir_line = QtGui.QLineEdit(self.centralwidget)
        self.out_dir_line.setObjectName(_fromUtf8("out_dir_line"))
        self.horizontalLayout_3.addWidget(self.out_dir_line)
        self.out_dir_button = QtGui.QPushButton(self.centralwidget)
        self.out_dir_button.setObjectName(_fromUtf8("out_dir_button"))
        self.out_dir_button.setMaximumWidth(30)
        self.horizontalLayout_3.addWidget(self.out_dir_button)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)

        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem1)

        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.min_pat_len = QtGui.QSpinBox(self.centralwidget)
        self.min_pat_len.setObjectName(_fromUtf8("min_pat_len"))
        self.min_pat_len.setValue(4)
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.min_pat_len)

        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_8)
        self.min_gap_len = QtGui.QSpinBox(self.centralwidget)
        self.min_gap_len.setObjectName(_fromUtf8("min_gap_len"))
        self.min_gap_len.setValue(2)
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.min_gap_len)

        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_6)
        self.max_gap_len = QtGui.QSpinBox(self.centralwidget)
        self.max_gap_len.setObjectName(_fromUtf8("max_gap_len"))
        self.max_gap_len.setValue(4)
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.max_gap_len)

        self.label_st_anchor = QtGui.QLabel(self.centralwidget)
        self.label_st_anchor.setObjectName(_fromUtf8("label_st_anchor"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_st_anchor)
        self.start_anchor = QtGui.QLineEdit(self.centralwidget)
        self.start_anchor.setObjectName(_fromUtf8("start_anchor"))
        self.start_anchor.setText(_fromUtf8("KWG"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.start_anchor)

        self.label_en_anchor = QtGui.QLabel(self.centralwidget)
        self.label_en_anchor.setObjectName(_fromUtf8("label_en_anchor"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_en_anchor)
        self.end_anchor = QtGui.QLineEdit(self.centralwidget)
        self.end_anchor.setObjectName(_fromUtf8("end_anchor"))
        self.end_anchor.setText(_fromUtf8("GMA"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.end_anchor)

        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(13, QtGui.QFormLayout.LabelRole, spacerItem2)

        self.run = QtGui.QPushButton("Run")
        self.run.setObjectName(_fromUtf8("run"))
        self.stop = QtGui.QPushButton("Stop")
        self.stop.setObjectName(_fromUtf8("stop"))

        self.hbox_progress_bar = QtGui.QHBoxLayout()
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.hbox_progress_bar.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.hbox_progress_bar, 2, 0, 1, 1)

        self.hbox_process_buttons = QtGui.QHBoxLayout()
        self.hbox_process_buttons.addWidget(self.run)
        self.hbox_process_buttons.addWidget(self.stop)
        self.gridLayout.addLayout(self.hbox_process_buttons, 3, 0, 1, 1)

        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Sequence Pattern Analyzer", None))
        self.label.setText(_translate("MainWindow", "Donor Alleles File", None))
        self.don_all_button.setText(_translate("MainWindow", "...", None))
        self.label_2.setText(_translate("MainWindow", "Input Alleles Directory", None))
        self.inp_all_button.setText(_translate("MainWindow", "...", None))
        self.label_3.setText(_translate("MainWindow", "Output Directory", None))
        self.out_dir_button.setText(_translate("MainWindow", "...", None))
        self.label_7.setText(_translate("MainWindow", "Minimum Pattern Length", None))
        self.label_8.setText(_translate("MainWindow", "Minimum Gap Length", None))
        self.label_6.setText(_translate("MainWindow", "Maximum Gap Length", None))
        self.label_st_anchor.setText(_translate("MainWindow", "Start Anchor", None))
        self.label_en_anchor.setText(_translate("MainWindow", "End Anchor", None))
        self.run.setText(_translate("MainWindow", "Run", None))
        self.pixmap = QtGui.QPixmap("./SequencePatternAnalyzerTop.png")
        self.pixmap.scaled(75,74, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_all_button.clicked.connect(self.input_buttonClicked)
        self.out_dir_button.clicked.connect(self.output_buttonClicked)
        self.don_all_button.clicked.connect(self.donor_buttonClicked)
        self.stop.setEnabled(False)
        self.run.clicked.connect(self.analyze)


    def donor_buttonClicked(self):
        self.don_all_line.setText(QtGui.QFileDialog.getOpenFileName())

    def input_buttonClicked(self):
        self.inp_all_line.setText(QtGui.QFileDialog.getExistingDirectory())

    def output_buttonClicked(self):
        self.out_dir_line.setText(QtGui.QFileDialog.getExistingDirectory())

    def analyze(self):
        input_files = []
        usable_files = []

        input_files = listdir(str(self.inp_all_line.text()))
        for sample in input_files:
            if sample[-2:] == "fa" or sample[-5:] == "fasta":
                usable_files.append(sample)

        self.progressBar.setMaximum(len(usable_files))
        self.progressBar.setValue(0)

        donor_file = str(self.don_all_line.text())
        input_path = str(self.inp_all_line.text())
        output_directory = str(self.out_dir_line.text())

        min_len = self.min_pat_len.value()
        min_gap = self.min_gap_len.value()
        max_gap = self.max_gap_len.value()

        st_anchor = str(self.start_anchor.text())
        en_anchor = str(self.end_anchor.text())

        self.get_thread = analyzeSamplesThread(usable_files, donor_file,
                                               input_path, output_directory,
                                               min_len, min_gap, max_gap,
                                               st_anchor, en_anchor)
        self.connect(self.get_thread, SIGNAL("processing(QString)"), self.sampleProcessing)
        self.connect(self.get_thread, SIGNAL("processed(QString)"), self.sampleProcessed)
        self.connect(self.get_thread, SIGNAL("finished()"), self.done)

        self.get_thread.start()
        self.stop.setEnabled(True)
        self.stop.clicked.connect(self.get_thread.terminate)
        self.run.setEnabled(False)

    def sampleProcessing(self, sample):
        self.statusbar.showMessage("Analyzing " + sample + "...")

    def sampleProcessed(self, sample):
        self.progressBar.setValue(self.progressBar.value() + 1)

    def done(self):
        print("Done!")
        self.run.setEnabled(True)
        self.stop.setEnabled(False)
        self.progressBar.setValue(0)
        self.statusbar.showMessage("")
        QtGui.QMessageBox.information(self, "Sequence Pattern Analyzer", "Analysis of all sequence patterns completed!")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
