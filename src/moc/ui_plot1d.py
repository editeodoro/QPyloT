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
        Plot1D_Window.resize(750, 629)
        self.centralWidget = QtWidgets.QWidget(Plot1D_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Main_gridLayout = QtWidgets.QGridLayout()
        self.Main_gridLayout.setContentsMargins(11, 11, 11, 11)
        self.Main_gridLayout.setSpacing(6)
        self.Main_gridLayout.setObjectName("Main_gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Main_gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Main_gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralWidget)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.treeWidget.setIndentation(10)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item_0.setFont(0, font)
        self.treeWidget.header().setVisible(False)
        self.Main_gridLayout.addWidget(self.treeWidget, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.Main_gridLayout)
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
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 750, 27))
        self.menuBar.setObjectName("menuBar")
        Plot1D_Window.setMenuBar(self.menuBar)

        self.retranslateUi(Plot1D_Window)
        QtCore.QMetaObject.connectSlotsByName(Plot1D_Window)

    def retranslateUi(self, Plot1D_Window):
        _translate = QtCore.QCoreApplication.translate
        Plot1D_Window.setWindowTitle(_translate("Plot1D_Window", "QPyLOT - Plot 1D"))
        self.treeWidget.headerItem().setText(0, _translate("Plot1D_Window", "1"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Plot1D_Window", "Data"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Plot1D_Window", "Plot1"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Plot1D_Window", "Axis"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

