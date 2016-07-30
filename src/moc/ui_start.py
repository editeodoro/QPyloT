# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIs/start_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Start_Window(object):
    def setupUi(self, Start_Window):
        Start_Window.setObjectName("Start_Window")
        Start_Window.resize(558, 400)
        self.centralWidget = QtWidgets.QWidget(Start_Window)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Plot1Dpage = QtWidgets.QWidget()
        self.Plot1Dpage.setObjectName("Plot1Dpage")
        self.gridLayout = QtWidgets.QGridLayout(self.Plot1Dpage)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Plot1Dpage)
        self.Plot2Dpage = QtWidgets.QWidget()
        self.Plot2Dpage.setObjectName("Plot2Dpage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Plot2Dpage)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.Plot2Dpage)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Plot2Dpage)
        self.verticalLayout.addWidget(self.stackedWidget)
        Start_Window.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Start_Window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 558, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        Start_Window.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Start_Window)
        self.mainToolBar.setMovable(True)
        self.mainToolBar.setIconSize(QtCore.QSize(28, 28))
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.mainToolBar.setObjectName("mainToolBar")
        Start_Window.addToolBar(QtCore.Qt.LeftToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Start_Window)
        self.statusBar.setObjectName("statusBar")
        Start_Window.setStatusBar(self.statusBar)
        self.actionQuit = QtWidgets.QAction(Start_Window)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Start_Window)
        self.stackedWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(Start_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Start_Window)

    def retranslateUi(self, Start_Window):
        _translate = QtCore.QCoreApplication.translate
        Start_Window.setWindowTitle(_translate("Start_Window", "QPyLOT"))
        self.toolButton.setText(_translate("Start_Window", "..."))
        self.menuFile.setTitle(_translate("Start_Window", "File"))
        self.actionQuit.setText(_translate("Start_Window", "Quit"))

