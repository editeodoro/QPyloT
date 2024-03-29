# Form implementation generated from reading ui file 'UIs/right_selector.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Right_Selector(object):
    def setupUi(self, Right_Selector):
        Right_Selector.setObjectName("Right_Selector")
        Right_Selector.resize(169, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Right_Selector.sizePolicy().hasHeightForWidth())
        Right_Selector.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Right_Selector)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Down_toolButton = QtWidgets.QToolButton(parent=Right_Selector)
        self.Down_toolButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Down_toolButton.sizePolicy().hasHeightForWidth())
        self.Down_toolButton.setSizePolicy(sizePolicy)
        self.Down_toolButton.setText("")
        self.Down_toolButton.setArrowType(QtCore.Qt.ArrowType.DownArrow)
        self.Down_toolButton.setObjectName("Down_toolButton")
        self.gridLayout.addWidget(self.Down_toolButton, 1, 1, 1, 1)
        self.Up_toolButton = QtWidgets.QToolButton(parent=Right_Selector)
        self.Up_toolButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Up_toolButton.sizePolicy().hasHeightForWidth())
        self.Up_toolButton.setSizePolicy(sizePolicy)
        self.Up_toolButton.setText("")
        self.Up_toolButton.setArrowType(QtCore.Qt.ArrowType.UpArrow)
        self.Up_toolButton.setObjectName("Up_toolButton")
        self.gridLayout.addWidget(self.Up_toolButton, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(parent=Right_Selector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
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
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsUserCheckable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsEditable|QtCore.Qt.ItemFlag.ItemIsDragEnabled|QtCore.Qt.ItemFlag.ItemIsDropEnabled|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 4)
        self.Minus_toolButton = QtWidgets.QToolButton(parent=Right_Selector)
        self.Minus_toolButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Minus_toolButton.sizePolicy().hasHeightForWidth())
        self.Minus_toolButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Minus_toolButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UIs/icons/minus-xxl.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Minus_toolButton.setIcon(icon)
        self.Minus_toolButton.setIconSize(QtCore.QSize(10, 10))
        self.Minus_toolButton.setObjectName("Minus_toolButton")
        self.gridLayout.addWidget(self.Minus_toolButton, 1, 2, 1, 1)
        self.Plus_toolButton = QtWidgets.QToolButton(parent=Right_Selector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Plus_toolButton.sizePolicy().hasHeightForWidth())
        self.Plus_toolButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(13)
        self.Plus_toolButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UIs/icons/plus-xxl.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Plus_toolButton.setIcon(icon1)
        self.Plus_toolButton.setIconSize(QtCore.QSize(10, 10))
        self.Plus_toolButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)
        self.Plus_toolButton.setArrowType(QtCore.Qt.ArrowType.NoArrow)
        self.Plus_toolButton.setObjectName("Plus_toolButton")
        self.gridLayout.addWidget(self.Plus_toolButton, 1, 3, 1, 1)

        self.retranslateUi(Right_Selector)
        QtCore.QMetaObject.connectSlotsByName(Right_Selector)

    def retranslateUi(self, Right_Selector):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Right_Selector", "General "))
        item = self.listWidget.item(1)
        item.setText(_translate("Right_Selector", "Axes"))
        item = self.listWidget.item(2)
        item.setText(_translate("Right_Selector", "Legend"))
        item = self.listWidget.item(3)
        item.setText(_translate("Right_Selector", "Data"))
        item = self.listWidget.item(4)
        item.setText(_translate("Right_Selector", "    Plot1"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.Minus_toolButton.setText(_translate("Right_Selector", "-"))
        self.Plus_toolButton.setText(_translate("Right_Selector", "+"))
