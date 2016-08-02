# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/dummy.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Axes_tabwidget(object):
    def setupUi(self, Axes_tabwidget):
        Axes_tabwidget.setObjectName("Axes_tabwidget")
        Axes_tabwidget.resize(524, 320)
        self.gridLayout = QtWidgets.QGridLayout(Axes_tabwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.AxesProperties_gridLayout = QtWidgets.QGridLayout()
        self.AxesProperties_gridLayout.setObjectName("AxesProperties_gridLayout")
        self.label_24 = QtWidgets.QLabel(Axes_tabwidget)
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.AxesProperties_gridLayout.addWidget(self.label_24, 2, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Axes_tabwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.AxesProperties_gridLayout.addWidget(self.lineEdit, 1, 3, 1, 2)
        self.label_25 = QtWidgets.QLabel(Axes_tabwidget)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.AxesProperties_gridLayout.addWidget(self.label_25, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Axes_tabwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.AxesProperties_gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(Axes_tabwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.AxesProperties_gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(Axes_tabwidget)
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.AxesProperties_gridLayout.addWidget(self.label_26, 2, 1, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Axes_tabwidget)
        self.doubleSpinBox_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.AxesProperties_gridLayout.addWidget(self.doubleSpinBox_2, 2, 2, 1, 1)
        self.gridLayout.addLayout(self.AxesProperties_gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Axes_tabwidget)
        QtCore.QMetaObject.connectSlotsByName(Axes_tabwidget)

    def retranslateUi(self, Axes_tabwidget):
        _translate = QtCore.QCoreApplication.translate
        self.label_24.setText(_translate("Axes_tabwidget", "Color:  "))
        self.label_25.setText(_translate("Axes_tabwidget", "Linestyle:  "))
        self.comboBox.setItemText(0, _translate("Axes_tabwidget", "Solid"))
        self.comboBox.setItemText(1, _translate("Axes_tabwidget", "Dashed"))
        self.comboBox.setItemText(2, _translate("Axes_tabwidget", "Dotted"))
        self.comboBox.setItemText(3, _translate("Axes_tabwidget", "Dashdotted"))
        self.comboBox.setItemText(4, _translate("Axes_tabwidget", "Custom"))
        self.checkBox_2.setText(_translate("Axes_tabwidget", "Grid:"))
        self.label_26.setText(_translate("Axes_tabwidget", "Linewidth:  "))

