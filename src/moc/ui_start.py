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
        self.Main_stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.Main_stackedWidget.setObjectName("Main_stackedWidget")
        self.verticalLayout.addWidget(self.Main_stackedWidget)
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
        self.Main_stackedWidget.setCurrentIndex(-1)
        self.actionQuit.triggered.connect(Start_Window.close)
        QtCore.QMetaObject.connectSlotsByName(Start_Window)

    def retranslateUi(self, Start_Window):
        _translate = QtCore.QCoreApplication.translate
        Start_Window.setWindowTitle(_translate("Start_Window", "QPyLOT"))
        self.menuFile.setTitle(_translate("Start_Window", "File"))
        self.actionQuit.setText(_translate("Start_Window", "Quit"))

