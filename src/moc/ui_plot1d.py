# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/plot1d.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Plot1D_Window(object):
    def setupUi(self, Plot1D_Window):
        Plot1D_Window.setObjectName("Plot1D_Window")
        Plot1D_Window.resize(689, 559)
        self.centralWidget = QtWidgets.QWidget(Plot1D_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.Main_gridLayout = QtWidgets.QGridLayout()
        self.Main_gridLayout.setContentsMargins(11, 11, 11, 11)
        self.Main_gridLayout.setSpacing(6)
        self.Main_gridLayout.setObjectName("Main_gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        self.Main_gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageGeneral = QtWidgets.QWidget()
        self.pageGeneral.setObjectName("pageGeneral")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.pageGeneral)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.line_4 = QtWidgets.QFrame(self.pageGeneral)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_10.addWidget(self.line_4, 0, 1, 1, 2)
        self.Generallabel = QtWidgets.QLabel(self.pageGeneral)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Generallabel.setFont(font)
        self.Generallabel.setObjectName("Generallabel")
        self.gridLayout_10.addWidget(self.Generallabel, 0, 0, 1, 1)
        self.GeneralFonttoolButton = QtWidgets.QToolButton(self.pageGeneral)
        self.GeneralFonttoolButton.setObjectName("GeneralFonttoolButton")
        self.gridLayout_10.addWidget(self.GeneralFonttoolButton, 1, 1, 1, 1)
        self.GeneralFontlabel = QtWidgets.QLabel(self.pageGeneral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GeneralFontlabel.sizePolicy().hasHeightForWidth())
        self.GeneralFontlabel.setSizePolicy(sizePolicy)
        self.GeneralFontlabel.setObjectName("GeneralFontlabel")
        self.gridLayout_10.addWidget(self.GeneralFontlabel, 1, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageGeneral)
        self.pageAxesEMPTY = QtWidgets.QWidget()
        self.pageAxesEMPTY.setObjectName("pageAxesEMPTY")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.pageAxesEMPTY)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_15 = QtWidgets.QLabel(self.pageAxesEMPTY)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.pageAxesEMPTY)
        self.pageLabels = QtWidgets.QWidget()
        self.pageLabels.setObjectName("pageLabels")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageLabels)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.pageLabels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 1, 2, 1, 1)
        self.XLabeloffsetdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.pageLabels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XLabeloffsetdoubleSpinBox.sizePolicy().hasHeightForWidth())
        self.XLabeloffsetdoubleSpinBox.setSizePolicy(sizePolicy)
        self.XLabeloffsetdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XLabeloffsetdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XLabeloffsetdoubleSpinBox.setObjectName("XLabeloffsetdoubleSpinBox")
        self.gridLayout_7.addWidget(self.XLabeloffsetdoubleSpinBox, 1, 3, 1, 1)
        self.YLabellabel = QtWidgets.QLabel(self.pageLabels)
        self.YLabellabel.setObjectName("YLabellabel")
        self.gridLayout_7.addWidget(self.YLabellabel, 2, 0, 1, 1)
        self.XLabellabel = QtWidgets.QLabel(self.pageLabels)
        self.XLabellabel.setObjectName("XLabellabel")
        self.gridLayout_7.addWidget(self.XLabellabel, 1, 0, 1, 1)
        self.YLabellineEdit = QtWidgets.QLineEdit(self.pageLabels)
        self.YLabellineEdit.setObjectName("YLabellineEdit")
        self.gridLayout_7.addWidget(self.YLabellineEdit, 2, 1, 1, 1)
        self.XLabellineEdit = QtWidgets.QLineEdit(self.pageLabels)
        self.XLabellineEdit.setObjectName("XLabellineEdit")
        self.gridLayout_7.addWidget(self.XLabellineEdit, 1, 1, 1, 1)
        self.Fontlabel = QtWidgets.QLabel(self.pageLabels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fontlabel.sizePolicy().hasHeightForWidth())
        self.Fontlabel.setSizePolicy(sizePolicy)
        self.Fontlabel.setObjectName("Fontlabel")
        self.gridLayout_7.addWidget(self.Fontlabel, 3, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.pageLabels)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_7.addWidget(self.line_2, 0, 1, 1, 3)
        self.YLabeloffsetdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.pageLabels)
        self.YLabeloffsetdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YLabeloffsetdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YLabeloffsetdoubleSpinBox.setObjectName("YLabeloffsetdoubleSpinBox")
        self.gridLayout_7.addWidget(self.YLabeloffsetdoubleSpinBox, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.pageLabels)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 2, 2, 1, 1)
        self.Labelslabel = QtWidgets.QLabel(self.pageLabels)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Labelslabel.setFont(font)
        self.Labelslabel.setObjectName("Labelslabel")
        self.gridLayout_7.addWidget(self.Labelslabel, 0, 0, 1, 1)
        self.LabelFonttoolButton = QtWidgets.QToolButton(self.pageLabels)
        self.LabelFonttoolButton.setObjectName("LabelFonttoolButton")
        self.gridLayout_7.addWidget(self.LabelFonttoolButton, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_7)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.XticsOffsetdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.pageLabels)
        self.XticsOffsetdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XticsOffsetdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XticsOffsetdoubleSpinBox.setObjectName("XticsOffsetdoubleSpinBox")
        self.gridLayout_8.addWidget(self.XticsOffsetdoubleSpinBox, 3, 2, 1, 1)
        self.XticsTopcheckBox = QtWidgets.QCheckBox(self.pageLabels)
        self.XticsTopcheckBox.setChecked(True)
        self.XticsTopcheckBox.setObjectName("XticsTopcheckBox")
        self.gridLayout_8.addWidget(self.XticsTopcheckBox, 1, 5, 1, 1)
        self.YticsMinorLengthdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.pageLabels)
        self.YticsMinorLengthdoubleSpinBox.setEnabled(False)
        self.YticsMinorLengthdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YticsMinorLengthdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YticsMinorLengthdoubleSpinBox.setObjectName("YticsMinorLengthdoubleSpinBox")
        self.gridLayout_8.addWidget(self.YticsMinorLengthdoubleSpinBox, 5, 4, 1, 1)
        self.YticsFonttoolButton = QtWidgets.QToolButton(self.pageLabels)
        self.YticsFonttoolButton.setObjectName("YticsFonttoolButton")
        self.gridLayout_8.addWidget(self.YticsFonttoolButton, 7, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.pageLabels)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_8.addWidget(self.checkBox_4, 4, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.pageLabels)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 4, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.pageLabels)
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 4, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.pageLabels)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_8.addWidget(self.line_3, 0, 1, 1, 6)
        self.YticslineEdit = QtWidgets.QLineEdit(self.pageLabels)
        self.YticslineEdit.setObjectName("YticslineEdit")
        self.gridLayout_8.addWidget(self.YticslineEdit, 4, 1, 1, 2)
        self.XticsMinorLengthdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.pageLabels)
        self.XticsMinorLengthdoubleSpinBox.setEnabled(False)
        self.XticsMinorLengthdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XticsMinorLengthdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XticsMinorLengthdoubleSpinBox.setObjectName("XticsMinorLengthdoubleSpinBox")
        self.gridLayout_8.addWidget(self.XticsMinorLengthdoubleSpinBox, 2, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.pageLabels)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.pageLabels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 3, 1, 1, 1)
        self.YticsMinorcheckBox = QtWidgets.QCheckBox(self.pageLabels)
        self.YticsMinorcheckBox.setObjectName("YticsMinorcheckBox")
        self.gridLayout_8.addWidget(self.YticsMinorcheckBox, 5, 1, 1, 1)
        self.XticsBottomcheckBox = QtWidgets.QCheckBox(self.pageLabels)
        self.XticsBottomcheckBox.setChecked(True)
        self.XticsBottomcheckBox.setObjectName("XticsBottomcheckBox")
        self.gridLayout_8.addWidget(self.XticsBottomcheckBox, 1, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.pageLabels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)
        self.XticsMinorcheckBox = QtWidgets.QCheckBox(self.pageLabels)
        self.XticsMinorcheckBox.setObjectName("XticsMinorcheckBox")
        self.gridLayout_8.addWidget(self.XticsMinorcheckBox, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.pageLabels)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.pageLabels)
        self.label_7.setEnabled(False)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 2, 3, 1, 1)
        self.XticslineEdit = QtWidgets.QLineEdit(self.pageLabels)
        self.XticslineEdit.setObjectName("XticslineEdit")
        self.gridLayout_8.addWidget(self.XticslineEdit, 1, 1, 1, 2)
        self.XticsMinorspinBox = QtWidgets.QSpinBox(self.pageLabels)
        self.XticsMinorspinBox.setEnabled(False)
        self.XticsMinorspinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XticsMinorspinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XticsMinorspinBox.setObjectName("XticsMinorspinBox")
        self.gridLayout_8.addWidget(self.XticsMinorspinBox, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.pageLabels)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_8.addWidget(self.label_6, 1, 3, 1, 1)
        self.XticsLengthdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.pageLabels)
        self.XticsLengthdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.XticsLengthdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.XticsLengthdoubleSpinBox.setProperty("value", 5.0)
        self.XticsLengthdoubleSpinBox.setObjectName("XticsLengthdoubleSpinBox")
        self.gridLayout_8.addWidget(self.XticsLengthdoubleSpinBox, 1, 4, 1, 1)
        self.YticsRightcheckBox = QtWidgets.QCheckBox(self.pageLabels)
        self.YticsRightcheckBox.setChecked(True)
        self.YticsRightcheckBox.setObjectName("YticsRightcheckBox")
        self.gridLayout_8.addWidget(self.YticsRightcheckBox, 4, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.pageLabels)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 7, 0, 1, 1)
        self.YticsLengthdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.pageLabels)
        self.YticsLengthdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YticsLengthdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YticsLengthdoubleSpinBox.setProperty("value", 5.0)
        self.YticsLengthdoubleSpinBox.setObjectName("YticsLengthdoubleSpinBox")
        self.gridLayout_8.addWidget(self.YticsLengthdoubleSpinBox, 4, 4, 1, 1)
        self.YticsOffsetdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.pageLabels)
        self.YticsOffsetdoubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YticsOffsetdoubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YticsOffsetdoubleSpinBox.setObjectName("YticsOffsetdoubleSpinBox")
        self.gridLayout_8.addWidget(self.YticsOffsetdoubleSpinBox, 6, 2, 1, 1)
        self.YticsMinorspinBox = QtWidgets.QSpinBox(self.pageLabels)
        self.YticsMinorspinBox.setEnabled(False)
        self.YticsMinorspinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.YticsMinorspinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.YticsMinorspinBox.setObjectName("YticsMinorspinBox")
        self.gridLayout_8.addWidget(self.YticsMinorspinBox, 5, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.pageLabels)
        self.label_11.setEnabled(False)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 5, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.pageLabels)
        self.pageRange = QtWidgets.QWidget()
        self.pageRange.setObjectName("pageRange")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pageRange)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Yrange_checkBox = QtWidgets.QCheckBox(self.pageRange)
        self.Yrange_checkBox.setObjectName("Yrange_checkBox")
        self.gridLayout_2.addWidget(self.Yrange_checkBox, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Xrange_to_lineEdit = QtWidgets.QLineEdit(self.pageRange)
        self.Xrange_to_lineEdit.setEnabled(False)
        self.Xrange_to_lineEdit.setObjectName("Xrange_to_lineEdit")
        self.gridLayout_2.addWidget(self.Xrange_to_lineEdit, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 4, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.pageRange)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 1, 1, 1, 4)
        self.label_23 = QtWidgets.QLabel(self.pageRange)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 3, 2, 1, 1)
        self.Yrange_to_lineEdit = QtWidgets.QLineEdit(self.pageRange)
        self.Yrange_to_lineEdit.setEnabled(False)
        self.Yrange_to_lineEdit.setObjectName("Yrange_to_lineEdit")
        self.gridLayout_2.addWidget(self.Yrange_to_lineEdit, 3, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.pageRange)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 2, 2, 1, 1)
        self.Yrange_from_lineEdit = QtWidgets.QLineEdit(self.pageRange)
        self.Yrange_from_lineEdit.setEnabled(False)
        self.Yrange_from_lineEdit.setObjectName("Yrange_from_lineEdit")
        self.gridLayout_2.addWidget(self.Yrange_from_lineEdit, 3, 1, 1, 1)
        self.Xrange_from_lineEdit = QtWidgets.QLineEdit(self.pageRange)
        self.Xrange_from_lineEdit.setEnabled(False)
        self.Xrange_from_lineEdit.setObjectName("Xrange_from_lineEdit")
        self.gridLayout_2.addWidget(self.Xrange_from_lineEdit, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.pageRange)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)
        self.Xrange_checkBox = QtWidgets.QCheckBox(self.pageRange)
        self.Xrange_checkBox.setObjectName("Xrange_checkBox")
        self.gridLayout_2.addWidget(self.Xrange_checkBox, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.LogX_checkBox = QtWidgets.QCheckBox(self.pageRange)
        self.LogX_checkBox.setObjectName("LogX_checkBox")
        self.verticalLayout.addWidget(self.LogX_checkBox)
        self.LogY_checkBox = QtWidgets.QCheckBox(self.pageRange)
        self.LogY_checkBox.setObjectName("LogY_checkBox")
        self.verticalLayout.addWidget(self.LogY_checkBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.pageRange)
        self.pageLegend = QtWidgets.QWidget()
        self.pageLegend.setObjectName("pageLegend")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.pageLegend)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_26 = QtWidgets.QLabel(self.pageLegend)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_9.addWidget(self.label_26, 1, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.pageLegend)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_9.addWidget(self.line_6, 1, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageLegend)
        self.pageDataEMPTY = QtWidgets.QWidget()
        self.pageDataEMPTY.setObjectName("pageDataEMPTY")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pageDataEMPTY)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_13 = QtWidgets.QLabel(self.pageDataEMPTY)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.pageDataEMPTY)
        self.pageData1 = QtWidgets.QWidget()
        self.pageData1.setObjectName("pageData1")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.pageData1)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(492, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.pageData1)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.pageData1)
        self.Main_gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.Main_gridLayout, 0, 0, 1, 1)
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
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 689, 22))
        self.menuBar.setObjectName("menuBar")
        Plot1D_Window.setMenuBar(self.menuBar)

        self.retranslateUi(Plot1D_Window)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(Plot1D_Window)

    def retranslateUi(self, Plot1D_Window):
        _translate = QtCore.QCoreApplication.translate
        Plot1D_Window.setWindowTitle(_translate("Plot1D_Window", "QPyLOT - Plot 1D"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Plot1D_Window", "General"))
        item = self.listWidget.item(1)
        item.setText(_translate("Plot1D_Window", "Axes"))
        item = self.listWidget.item(2)
        item.setText(_translate("Plot1D_Window", "    Range"))
        item = self.listWidget.item(3)
        item.setText(_translate("Plot1D_Window", "    Labels"))
        item = self.listWidget.item(4)
        item.setText(_translate("Plot1D_Window", "Legend"))
        item = self.listWidget.item(5)
        item.setText(_translate("Plot1D_Window", "Data"))
        item = self.listWidget.item(6)
        item.setText(_translate("Plot1D_Window", "    Plot1"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.Generallabel.setText(_translate("Plot1D_Window", "GENERAL SETTINGS"))
        self.GeneralFonttoolButton.setText(_translate("Plot1D_Window", "Helvetica, 12 pt"))
        self.GeneralFontlabel.setText(_translate("Plot1D_Window", "  Font:"))
        self.label_15.setText(_translate("Plot1D_Window", "EMPTY AXES PAGE"))
        self.label.setText(_translate("Plot1D_Window", "Offset"))
        self.YLabellabel.setText(_translate("Plot1D_Window", "  Y label:"))
        self.XLabellabel.setText(_translate("Plot1D_Window", "  X label:"))
        self.Fontlabel.setText(_translate("Plot1D_Window", "  Font:"))
        self.label_2.setText(_translate("Plot1D_Window", "Offset"))
        self.Labelslabel.setText(_translate("Plot1D_Window", "LABELS"))
        self.LabelFonttoolButton.setText(_translate("Plot1D_Window", "Helvetica, 12 pt"))
        self.XticsTopcheckBox.setText(_translate("Plot1D_Window", "Top"))
        self.YticsFonttoolButton.setText(_translate("Plot1D_Window", "Helvetica, 12 pt"))
        self.checkBox_4.setText(_translate("Plot1D_Window", "Right"))
        self.label_9.setText(_translate("Plot1D_Window", "Length"))
        self.label_8.setText(_translate("Plot1D_Window", "  Y tics:"))
        self.label_10.setText(_translate("Plot1D_Window", "Label offset"))
        self.label_5.setText(_translate("Plot1D_Window", "Label offset"))
        self.YticsMinorcheckBox.setText(_translate("Plot1D_Window", "Minor tics"))
        self.XticsBottomcheckBox.setText(_translate("Plot1D_Window", "Bottom"))
        self.label_4.setText(_translate("Plot1D_Window", "  X tics:"))
        self.XticsMinorcheckBox.setText(_translate("Plot1D_Window", " Minor tics"))
        self.label_3.setText(_translate("Plot1D_Window", "TICS      "))
        self.label_7.setText(_translate("Plot1D_Window", "Length"))
        self.label_6.setText(_translate("Plot1D_Window", "Length"))
        self.YticsRightcheckBox.setText(_translate("Plot1D_Window", "Left"))
        self.label_12.setText(_translate("Plot1D_Window", "  Font"))
        self.label_11.setText(_translate("Plot1D_Window", "Length"))
        self.Yrange_checkBox.setText(_translate("Plot1D_Window", "Y Range:"))
        self.label_23.setText(_translate("Plot1D_Window", "  :  "))
        self.label_22.setText(_translate("Plot1D_Window", "  :  "))
        self.label_21.setText(_translate("Plot1D_Window", "AXIS RANGE"))
        self.Xrange_checkBox.setText(_translate("Plot1D_Window", "X Range:"))
        self.LogX_checkBox.setText(_translate("Plot1D_Window", "Logaritmic X axis"))
        self.LogY_checkBox.setText(_translate("Plot1D_Window", "Logaritmic Y axis"))
        self.label_26.setText(_translate("Plot1D_Window", "LEGEND"))
        self.label_13.setText(_translate("Plot1D_Window", "EMPTY DATA PAGE"))
        self.label_14.setText(_translate("Plot1D_Window", "Plot #1"))

