# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot1d_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Plot1D_Window(object):
    def setupUi(self, Plot1D_Window):
        Plot1D_Window.setObjectName("Plot1D_Window")
        Plot1D_Window.resize(732, 557)
        self.centralWidget = QtWidgets.QWidget(Plot1D_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_4.addWidget(self.listWidget, 1, 0, 1, 1)
        self.File_lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.File_lineEdit.setObjectName("File_lineEdit")
        self.gridLayout_4.addWidget(self.File_lineEdit, 0, 1, 1, 1)
        self.File_label = QtWidgets.QLabel(self.centralWidget)
        self.File_label.setObjectName("File_label")
        self.gridLayout_4.addWidget(self.File_label, 0, 0, 1, 1)
        self.File_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.File_pushButton.setObjectName("File_pushButton")
        self.gridLayout_4.addWidget(self.File_pushButton, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_5.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 1, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_5.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.Label_tab = QtWidgets.QWidget()
        self.Label_tab.setObjectName("Label_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Label_tab)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.Label_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 1, 2, 1, 1)
        self.XLabeloffsetdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.Label_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XLabeloffsetdoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.XLabeloffsetdoubleSpinBox.setSizePolicy(sizePolicy)
        self.XLabeloffsetdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XLabeloffsetdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XLabeloffsetdoubleSpinBox.setObjectName("XLabeloffsetdoubleSpinBox")
        self.gridLayout_7.addWidget(self.XLabeloffsetdoubleSpinBox, 1, 3, 1, 1)
        self.YLabellabel = QtWidgets.QLabel(self.Label_tab)
        self.YLabellabel.setObjectName("YLabellabel")
        self.gridLayout_7.addWidget(self.YLabellabel, 2, 0, 1, 1)
        self.XLabellabel = QtWidgets.QLabel(self.Label_tab)
        self.XLabellabel.setObjectName("XLabellabel")
        self.gridLayout_7.addWidget(self.XLabellabel, 1, 0, 1, 1)
        self.YLabellineEdit = QtWidgets.QLineEdit(self.Label_tab)
        self.YLabellineEdit.setObjectName("YLabellineEdit")
        self.gridLayout_7.addWidget(self.YLabellineEdit, 2, 1, 1, 1)
        self.XLabellineEdit = QtWidgets.QLineEdit(self.Label_tab)
        self.XLabellineEdit.setObjectName("XLabellineEdit")
        self.gridLayout_7.addWidget(self.XLabellineEdit, 1, 1, 1, 1)
        self.Fontlabel = QtWidgets.QLabel(self.Label_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fontlabel.sizePolicy().hasHeightForWidth())
        self.Fontlabel.setSizePolicy(sizePolicy)
        self.Fontlabel.setObjectName("Fontlabel")
        self.gridLayout_7.addWidget(self.Fontlabel, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.Label_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 0, 1, 1, 3)
        self.YLabeloffsetdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.Label_tab)
        self.YLabeloffsetdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YLabeloffsetdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YLabeloffsetdoubleSpinBox.setObjectName("YLabeloffsetdoubleSpinBox")
        self.gridLayout_7.addWidget(self.YLabeloffsetdoubleSpinBox, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.Label_tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 2, 2, 1, 1)
        self.Labelslabel = QtWidgets.QLabel(self.Label_tab)
        self.Labelslabel.setObjectName("Labelslabel")
        self.gridLayout_7.addWidget(self.Labelslabel, 0, 0, 1, 1)
        self.LabelFonttoolButton = QtWidgets.QToolButton(self.Label_tab)
        self.LabelFonttoolButton.setObjectName("LabelFonttoolButton")
        self.gridLayout_7.addWidget(self.LabelFonttoolButton, 3, 2, 1, 1)
        self.fontComboBox = QtWidgets.QFontComboBox(self.Label_tab)
        self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.NonScalableFonts|QtWidgets.QFontComboBox.ProportionalFonts)
        self.fontComboBox.setObjectName("fontComboBox")
        self.gridLayout_7.addWidget(self.fontComboBox, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.YticsMinorspinBox = QtWidgets.QSpinBox(self.Label_tab)
        self.YticsMinorspinBox.setEnabled(False)
        self.YticsMinorspinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YticsMinorspinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YticsMinorspinBox.setObjectName("YticsMinorspinBox")
        self.gridLayout_8.addWidget(self.YticsMinorspinBox, 5, 2, 1, 1)
        self.YticsLengthdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.Label_tab)
        self.YticsLengthdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YticsLengthdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YticsLengthdoubleSpinBox.setProperty("value", 5.0)
        self.YticsLengthdoubleSpinBox.setObjectName("YticsLengthdoubleSpinBox")
        self.gridLayout_8.addWidget(self.YticsLengthdoubleSpinBox, 4, 4, 1, 1)
        self.YticsRightcheckBox = QtWidgets.QCheckBox(self.Label_tab)
        self.YticsRightcheckBox.setChecked(True)
        self.YticsRightcheckBox.setObjectName("YticsRightcheckBox")
        self.gridLayout_8.addWidget(self.YticsRightcheckBox, 4, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.Label_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 3, 1, 1, 1)
        self.XticsMinorspinBox = QtWidgets.QSpinBox(self.Label_tab)
        self.XticsMinorspinBox.setEnabled(False)
        self.XticsMinorspinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XticsMinorspinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XticsMinorspinBox.setObjectName("XticsMinorspinBox")
        self.gridLayout_8.addWidget(self.XticsMinorspinBox, 2, 2, 1, 1)
        self.YticslineEdit = QtWidgets.QLineEdit(self.Label_tab)
        self.YticslineEdit.setObjectName("YticslineEdit")
        self.gridLayout_8.addWidget(self.YticslineEdit, 4, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.Label_tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 6, 1, 1, 1)
        self.XticslineEdit = QtWidgets.QLineEdit(self.Label_tab)
        self.XticslineEdit.setObjectName("XticslineEdit")
        self.gridLayout_8.addWidget(self.XticslineEdit, 1, 1, 1, 2)
        self.YticsMinorLengthdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.Label_tab)
        self.YticsMinorLengthdoubleSpinBox.setEnabled(False)
        self.YticsMinorLengthdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YticsMinorLengthdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YticsMinorLengthdoubleSpinBox.setObjectName("YticsMinorLengthdoubleSpinBox")
        self.gridLayout_8.addWidget(self.YticsMinorLengthdoubleSpinBox, 5, 4, 1, 1)
        self.XticsLengthdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.Label_tab)
        self.XticsLengthdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XticsLengthdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XticsLengthdoubleSpinBox.setProperty("value", 5.0)
        self.XticsLengthdoubleSpinBox.setObjectName("XticsLengthdoubleSpinBox")
        self.gridLayout_8.addWidget(self.XticsLengthdoubleSpinBox, 1, 4, 1, 1)
        self.YticsMinorcheckBox = QtWidgets.QCheckBox(self.Label_tab)
        self.YticsMinorcheckBox.setObjectName("YticsMinorcheckBox")
        self.gridLayout_8.addWidget(self.YticsMinorcheckBox, 5, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.Label_tab)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_8.addWidget(self.checkBox_4, 4, 6, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.Label_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_8.addWidget(self.line_3, 0, 1, 1, 6)
        self.XticsBottomcheckBox = QtWidgets.QCheckBox(self.Label_tab)
        self.XticsBottomcheckBox.setChecked(True)
        self.XticsBottomcheckBox.setObjectName("XticsBottomcheckBox")
        self.gridLayout_8.addWidget(self.XticsBottomcheckBox, 1, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.Label_tab)
        self.label_11.setEnabled(False)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 5, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.Label_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 1, 3, 1, 1)
        self.XticsTopcheckBox = QtWidgets.QCheckBox(self.Label_tab)
        self.XticsTopcheckBox.setChecked(True)
        self.XticsTopcheckBox.setObjectName("XticsTopcheckBox")
        self.gridLayout_8.addWidget(self.XticsTopcheckBox, 1, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.Label_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.Label_tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.Label_tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Label_tab)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 2, 3, 1, 1)
        self.XticsMinorLengthdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.Label_tab)
        self.XticsMinorLengthdoubleSpinBox.setEnabled(False)
        self.XticsMinorLengthdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XticsMinorLengthdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XticsMinorLengthdoubleSpinBox.setObjectName("XticsMinorLengthdoubleSpinBox")
        self.gridLayout_8.addWidget(self.XticsMinorLengthdoubleSpinBox, 2, 4, 1, 1)
        self.YticsOffsetdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.Label_tab)
        self.YticsOffsetdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YticsOffsetdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YticsOffsetdoubleSpinBox.setObjectName("YticsOffsetdoubleSpinBox")
        self.gridLayout_8.addWidget(self.YticsOffsetdoubleSpinBox, 6, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.Label_tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 4, 3, 1, 1)
        self.XticsMinorcheckBox = QtWidgets.QCheckBox(self.Label_tab)
        self.XticsMinorcheckBox.setObjectName("XticsMinorcheckBox")
        self.gridLayout_8.addWidget(self.XticsMinorcheckBox, 2, 1, 1, 1)
        self.XticsOffsetdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.Label_tab)
        self.XticsOffsetdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XticsOffsetdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XticsOffsetdoubleSpinBox.setObjectName("XticsOffsetdoubleSpinBox")
        self.gridLayout_8.addWidget(self.XticsOffsetdoubleSpinBox, 3, 2, 1, 1)
        self.YticsFonttoolButton = QtWidgets.QToolButton(self.Label_tab)
        self.YticsFonttoolButton.setObjectName("YticsFonttoolButton")
        self.gridLayout_8.addWidget(self.YticsFonttoolButton, 7, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.Label_tab)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 7, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_8)
        self.tabWidget.addTab(self.Label_tab, "")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 1, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        Plot1D_Window.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(Plot1D_Window)
        self.mainToolBar.setOrientation(QtCore.Qt.Horizontal)
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.mainToolBar.setObjectName("mainToolBar")
        Plot1D_Window.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Plot1D_Window)
        self.statusBar.setObjectName("statusBar")
        Plot1D_Window.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(Plot1D_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 732, 27))
        self.menuBar.setObjectName("menuBar")
        Plot1D_Window.setMenuBar(self.menuBar)

        self.retranslateUi(Plot1D_Window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Plot1D_Window)

    def retranslateUi(self, Plot1D_Window):
        _translate = QtCore.QCoreApplication.translate
        Plot1D_Window.setWindowTitle(_translate("Plot1D_Window", "QPyLOT - Plot 1D"))
        self.File_label.setText(_translate("Plot1D_Window", "File (ASCII or FITS table)"))
        self.File_pushButton.setText(_translate("Plot1D_Window", "Open"))
        self.label_13.setText(_translate("Plot1D_Window", "   X   "))
        self.label_14.setText(_translate("Plot1D_Window", "   Y   "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Plot1D_Window", "Tab 1"))
        self.label.setText(_translate("Plot1D_Window", "Offset"))
        self.YLabellabel.setText(_translate("Plot1D_Window", "  Y label:"))
        self.XLabellabel.setText(_translate("Plot1D_Window", "  X label:"))
        self.Fontlabel.setText(_translate("Plot1D_Window", "  Font:"))
        self.label_2.setText(_translate("Plot1D_Window", "Offset"))
        self.Labelslabel.setText(_translate("Plot1D_Window", "LABELS"))
        self.LabelFonttoolButton.setText(_translate("Plot1D_Window", "Helvetica, 12 pt"))
        self.fontComboBox.setCurrentText(_translate("Plot1D_Window", "ClearlyU"))
        self.YticsRightcheckBox.setText(_translate("Plot1D_Window", "Left"))
        self.label_5.setText(_translate("Plot1D_Window", "Label offset"))
        self.label_10.setText(_translate("Plot1D_Window", "Label offset"))
        self.YticsMinorcheckBox.setText(_translate("Plot1D_Window", "Minor tics"))
        self.checkBox_4.setText(_translate("Plot1D_Window", "Right"))
        self.XticsBottomcheckBox.setText(_translate("Plot1D_Window", "Bottom"))
        self.label_11.setText(_translate("Plot1D_Window", "Length"))
        self.label_6.setText(_translate("Plot1D_Window", "Length"))
        self.XticsTopcheckBox.setText(_translate("Plot1D_Window", "Top"))
        self.label_4.setText(_translate("Plot1D_Window", "  X tics:"))
        self.label_8.setText(_translate("Plot1D_Window", "  Y tics:"))
        self.label_3.setText(_translate("Plot1D_Window", "TICS      "))
        self.label_7.setText(_translate("Plot1D_Window", "Length"))
        self.label_9.setText(_translate("Plot1D_Window", "Length"))
        self.XticsMinorcheckBox.setText(_translate("Plot1D_Window", " Minor tics"))
        self.YticsFonttoolButton.setText(_translate("Plot1D_Window", "Helvetica, 12 pt"))
        self.label_12.setText(_translate("Plot1D_Window", "  Font"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Label_tab), _translate("Plot1D_Window", "Tab 2"))

