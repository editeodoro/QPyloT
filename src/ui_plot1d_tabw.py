# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot1d_tabw.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Plot1D_tabwidget(object):
    def setupUi(self, Plot1D_tabwidget):
        Plot1D_tabwidget.setObjectName("Plot1D_tabwidget")
        Plot1D_tabwidget.resize(565, 485)
        self.gridLayout_3 = QtWidgets.QGridLayout(Plot1D_tabwidget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(Plot1D_tabwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.Data_tab = QtWidgets.QWidget()
        self.Data_tab.setObjectName("Data_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Data_tab)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_15 = QtWidgets.QLabel(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 1, 1, 1, 1)
        self.X_file_comboBox = QtWidgets.QComboBox(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.X_file_comboBox.sizePolicy().hasHeightForWidth())
        self.X_file_comboBox.setSizePolicy(sizePolicy)
        self.X_file_comboBox.setObjectName("X_file_comboBox")
        self.gridLayout_5.addWidget(self.X_file_comboBox, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)
        self.Y_file_comboBox = QtWidgets.QComboBox(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Y_file_comboBox.sizePolicy().hasHeightForWidth())
        self.Y_file_comboBox.setSizePolicy(sizePolicy)
        self.Y_file_comboBox.setObjectName("Y_file_comboBox")
        self.gridLayout_5.addWidget(self.Y_file_comboBox, 3, 1, 1, 1)
        self.X_col_comboBox = QtWidgets.QComboBox(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.X_col_comboBox.sizePolicy().hasHeightForWidth())
        self.X_col_comboBox.setSizePolicy(sizePolicy)
        self.X_col_comboBox.setObjectName("X_col_comboBox")
        self.gridLayout_5.addWidget(self.X_col_comboBox, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.Data_tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 3, 0, 1, 1)
        self.Y_col_comboBox = QtWidgets.QComboBox(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Y_col_comboBox.sizePolicy().hasHeightForWidth())
        self.Y_col_comboBox.setSizePolicy(sizePolicy)
        self.Y_col_comboBox.setObjectName("Y_col_comboBox")
        self.gridLayout_5.addWidget(self.Y_col_comboBox, 3, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 2, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.Data_tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 0, 1, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.Rows_from_spinBox = QtWidgets.QSpinBox(self.Data_tab)
        self.Rows_from_spinBox.setEnabled(False)
        self.Rows_from_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Rows_from_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Rows_from_spinBox.setObjectName("Rows_from_spinBox")
        self.gridLayout.addWidget(self.Rows_from_spinBox, 1, 3, 1, 1)
        self.Rows_all_checkBox = QtWidgets.QCheckBox(self.Data_tab)
        self.Rows_all_checkBox.setChecked(True)
        self.Rows_all_checkBox.setAutoExclusive(True)
        self.Rows_all_checkBox.setObjectName("Rows_all_checkBox")
        self.gridLayout.addWidget(self.Rows_all_checkBox, 1, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.Data_tab)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 1, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.Data_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 6, 1, 1)
        self.Rows_from_checkBox = QtWidgets.QCheckBox(self.Data_tab)
        self.Rows_from_checkBox.setAutoExclusive(True)
        self.Rows_from_checkBox.setObjectName("Rows_from_checkBox")
        self.gridLayout.addWidget(self.Rows_from_checkBox, 1, 2, 1, 1)
        self.Rows_to_spinBox = QtWidgets.QSpinBox(self.Data_tab)
        self.Rows_to_spinBox.setEnabled(False)
        self.Rows_to_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Rows_to_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Rows_to_spinBox.setObjectName("Rows_to_spinBox")
        self.gridLayout.addWidget(self.Rows_to_spinBox, 1, 5, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.Data_tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 1, 1, 6)
        self.label_19 = QtWidgets.QLabel(self.Data_tab)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 0, 1, 1)
        self.Rows_every_spinBox = QtWidgets.QSpinBox(self.Data_tab)
        self.Rows_every_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Rows_every_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Rows_every_spinBox.setMaximum(10000)
        self.Rows_every_spinBox.setProperty("value", 1)
        self.Rows_every_spinBox.setObjectName("Rows_every_spinBox")
        self.gridLayout.addWidget(self.Rows_every_spinBox, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout_2.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.tabWidget.addTab(self.Data_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Xrange_checkBox = QtWidgets.QCheckBox(self.tab)
        self.Xrange_checkBox.setObjectName("Xrange_checkBox")
        self.gridLayout_2.addWidget(self.Xrange_checkBox, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.Yrange_checkBox = QtWidgets.QCheckBox(self.tab)
        self.Yrange_checkBox.setObjectName("Yrange_checkBox")
        self.gridLayout_2.addWidget(self.Yrange_checkBox, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Xrange_to_lineEdit = QtWidgets.QLineEdit(self.tab)
        self.Xrange_to_lineEdit.setEnabled(False)
        self.Xrange_to_lineEdit.setObjectName("Xrange_to_lineEdit")
        self.gridLayout_2.addWidget(self.Xrange_to_lineEdit, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 4, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 1, 1, 1, 4)
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 3, 2, 1, 1)
        self.Yrange_to_lineEdit = QtWidgets.QLineEdit(self.tab)
        self.Yrange_to_lineEdit.setEnabled(False)
        self.Yrange_to_lineEdit.setObjectName("Yrange_to_lineEdit")
        self.gridLayout_2.addWidget(self.Yrange_to_lineEdit, 3, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 2, 2, 1, 1)
        self.Yrange_from_lineEdit = QtWidgets.QLineEdit(self.tab)
        self.Yrange_from_lineEdit.setEnabled(False)
        self.Yrange_from_lineEdit.setObjectName("Yrange_from_lineEdit")
        self.gridLayout_2.addWidget(self.Yrange_from_lineEdit, 3, 1, 1, 1)
        self.Xrange_from_lineEdit = QtWidgets.QLineEdit(self.tab)
        self.Xrange_from_lineEdit.setEnabled(False)
        self.Xrange_from_lineEdit.setObjectName("Xrange_from_lineEdit")
        self.gridLayout_2.addWidget(self.Xrange_from_lineEdit, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.LogX_checkBox = QtWidgets.QCheckBox(self.tab)
        self.LogX_checkBox.setObjectName("LogX_checkBox")
        self.verticalLayout_3.addWidget(self.LogX_checkBox)
        self.LogY_checkBox = QtWidgets.QCheckBox(self.tab)
        self.LogY_checkBox.setObjectName("LogY_checkBox")
        self.verticalLayout_3.addWidget(self.LogY_checkBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
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
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Labelslabel.setFont(font)
        self.Labelslabel.setObjectName("Labelslabel")
        self.gridLayout_7.addWidget(self.Labelslabel, 0, 0, 1, 1)
        self.LabelFonttoolButton = QtWidgets.QToolButton(self.Label_tab)
        self.LabelFonttoolButton.setObjectName("LabelFonttoolButton")
        self.gridLayout_7.addWidget(self.LabelFonttoolButton, 3, 1, 1, 1)
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
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.tabWidget.addTab(self.Label_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Plot1D_tabwidget)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Plot1D_tabwidget)

    def retranslateUi(self, Plot1D_tabwidget):
        _translate = QtCore.QCoreApplication.translate
        Plot1D_tabwidget.setWindowTitle(_translate("Plot1D_tabwidget", "Form"))
        self.label_15.setText(_translate("Plot1D_tabwidget", "File "))
        self.label_13.setText(_translate("Plot1D_tabwidget", " Data X: "))
        self.label_14.setText(_translate("Plot1D_tabwidget", " Data Y: "))
        self.label_16.setText(_translate("Plot1D_tabwidget", "Column"))
        self.label_17.setText(_translate("Plot1D_tabwidget", "DATA SERIES"))
        self.Rows_all_checkBox.setText(_translate("Plot1D_tabwidget", "All"))
        self.label_20.setText(_translate("Plot1D_tabwidget", "to"))
        self.label_18.setText(_translate("Plot1D_tabwidget", "ROWS           "))
        self.Rows_from_checkBox.setText(_translate("Plot1D_tabwidget", "From row"))
        self.label_19.setText(_translate("Plot1D_tabwidget", " Every"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Data_tab), _translate("Plot1D_tabwidget", "Data"))
        self.Xrange_checkBox.setText(_translate("Plot1D_tabwidget", "X Range:"))
        self.Yrange_checkBox.setText(_translate("Plot1D_tabwidget", "Y Range:"))
        self.label_23.setText(_translate("Plot1D_tabwidget", "  :  "))
        self.label_22.setText(_translate("Plot1D_tabwidget", "  :  "))
        self.label_21.setText(_translate("Plot1D_tabwidget", "AXIS RANGE"))
        self.LogX_checkBox.setText(_translate("Plot1D_tabwidget", "Logaritmic X axis"))
        self.LogY_checkBox.setText(_translate("Plot1D_tabwidget", "Logaritmic Y axis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Plot1D_tabwidget", "Axis"))
        self.label.setText(_translate("Plot1D_tabwidget", "Offset"))
        self.YLabellabel.setText(_translate("Plot1D_tabwidget", "  Y label:"))
        self.XLabellabel.setText(_translate("Plot1D_tabwidget", "  X label:"))
        self.Fontlabel.setText(_translate("Plot1D_tabwidget", "  Font:"))
        self.label_2.setText(_translate("Plot1D_tabwidget", "Offset"))
        self.Labelslabel.setText(_translate("Plot1D_tabwidget", "LABELS"))
        self.LabelFonttoolButton.setText(_translate("Plot1D_tabwidget", "Helvetica, 12 pt"))
        self.YticsRightcheckBox.setText(_translate("Plot1D_tabwidget", "Left"))
        self.label_5.setText(_translate("Plot1D_tabwidget", "Label offset"))
        self.label_10.setText(_translate("Plot1D_tabwidget", "Label offset"))
        self.YticsMinorcheckBox.setText(_translate("Plot1D_tabwidget", "Minor tics"))
        self.checkBox_4.setText(_translate("Plot1D_tabwidget", "Right"))
        self.XticsBottomcheckBox.setText(_translate("Plot1D_tabwidget", "Bottom"))
        self.label_11.setText(_translate("Plot1D_tabwidget", "Length"))
        self.label_6.setText(_translate("Plot1D_tabwidget", "Length"))
        self.XticsTopcheckBox.setText(_translate("Plot1D_tabwidget", "Top"))
        self.label_4.setText(_translate("Plot1D_tabwidget", "  X tics:"))
        self.label_8.setText(_translate("Plot1D_tabwidget", "  Y tics:"))
        self.label_3.setText(_translate("Plot1D_tabwidget", "TICS      "))
        self.label_7.setText(_translate("Plot1D_tabwidget", "Length"))
        self.label_9.setText(_translate("Plot1D_tabwidget", "Length"))
        self.XticsMinorcheckBox.setText(_translate("Plot1D_tabwidget", " Minor tics"))
        self.YticsFonttoolButton.setText(_translate("Plot1D_tabwidget", "Helvetica, 12 pt"))
        self.label_12.setText(_translate("Plot1D_tabwidget", "  Font"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Label_tab), _translate("Plot1D_tabwidget", "Labels"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Plot1D_tabwidget", "Markers"))

