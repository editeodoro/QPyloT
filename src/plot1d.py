### ----------------------------------------------------------------------------
### plot1d.py: Plot1DWindow class definition derived from Ui_Plot1D_Window class.
###            It controls the actions on the 1D plot window
### ----------------------------------------------------------------------------

import os
import numpy as np
from PyQt5.QtWidgets import *
from moc.ui_plot1d import Ui_Plot1D_Window
from moc.ui_plot1d_tabw import Ui_Plot1D_tabwidget
from moc.ui_axes_tabw import Ui_Axes_tabwidget

from PyQt5 import QtWidgets, QtCore, QtGui

class Filein_Widget(QtWidgets.QWidget):
# This class is just a container for an array (lineedit + button Open + button Add)
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)        
        # GUI elements and settings
        self.parent = parent
        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(2,0,2,0)
        
        self.File_label = QtWidgets.QLabel("  File (ASCII or FITS table)  ")
        self.Layout.addWidget(self.File_label,0,0)
        
        self.File_lineEdit, self.File_pushButton, self.File_toolButton = [],[],[]
        self.File_Menu, self.add_act, self.rem_act = [], [], []
        
        self.file_name, self.col_name = [], [[]]

        self.addFile()
     
        
    def addFile(self):
        r = len(self.File_lineEdit)
        
        # Set the lineEdit and the "Open" pushButton
        self.File_lineEdit.append(QtWidgets.QLineEdit(self))
        self.Layout.addWidget(self.File_lineEdit[r],r,1)
        self.File_pushButton.append(QtWidgets.QPushButton(self))
        self.File_pushButton[r].setText("Open")
        self.Layout.addWidget(self.File_pushButton[r],r,2)
        self.File_pushButton[r].clicked.connect(self.openDialog)
        
        # Now creating the "Add" toolButton with a popup menu.
        # The QMenu as two actions: Add and Remove a file
        self.File_Menu.append(QtWidgets.QMenu(self))
        self.add_act.append(QtWidgets.QAction("Add file",self))
        self.rem_act.append(QtWidgets.QAction("Remove file",self))
        self.add_act[r].triggered.connect(self.addFile)
        self.rem_act[r].triggered.connect(self.removeFile)
        if r==0: self.rem_act[r].setDisabled(True)
        self.File_Menu[r].addAction(self.add_act[r])
        self.File_Menu[r].addAction(self.rem_act[r])
        self.File_toolButton.append(QtWidgets.QToolButton(self))
        self.File_toolButton[r].setMenu(self.File_Menu[r])
        self.File_toolButton[r].setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.File_toolButton[r].setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.File_toolButton[r].setIcon(QtGui.QIcon("icons/plus_128.png"))        
        self.Layout.addWidget(self.File_toolButton[r],r,3)
        
        self.file_name.append(None)
        self.col_name.append(None)
            
    def removeFile(self):
        for idx, ad in enumerate(self.rem_act):
            if ad==self.sender():
                self.File_lineEdit[idx].setVisible(False)
                self.File_pushButton[idx].setVisible(False)
                self.File_toolButton[idx].setVisible(False)
                self.file_name[idx] = self.col_name[idx] = None
    
    def openDialog(self):
        # Select file and read column names        
        filen = QFileDialog.getOpenFileName(self, 'Open file')[0]
        if filen:
            for idx, ad in enumerate(self.File_pushButton):
                if ad==self.sender():
                    self.file_name[idx]=os.path.expanduser(filen)
                    self.File_lineEdit[idx].setText(self.file_name[idx])
                    try:
                        data = np.genfromtxt(self.file_name[idx], names=True, autostrip=True)
                        self.col_name[idx]=data.dtype.names
                    except:
                        print ("NUN CE CAPISCO")
    
                    
                    
                    if self.parent is not None: 
                        self.parent.grancazzo() # Send a signal to parent object self.FileChanged()

class FontPicker (QtWidgets.QWidget):
# This class is just a container for GUI elements useful for font management.
# The GUI has a font label + a toolButton to select the font

    def __init__(self,parent=None,font='Helvetica'):
        QtWidgets.QWidget.__init__(self)        
        
        # The current selected color (initialized here)
        self.font = QtGui.QFont(font)

        # Here the GUI begins
        self.Layout = QtWidgets.QHBoxLayout(self)
        self.Layout.setContentsMargins(0,2,0,2)
        
        # Initilize the widget elements
        self.font_label = QtWidgets.QLabel(" Font:   ")
        self.font_toolButton = QtWidgets.QToolButton()
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.font_toolButton.setSizePolicy(sizePolicy)
        
        # Some properties
        self.font_toolButton.setAutoRaise(True)
        self.updateFont(self.font)
        
        # Add GUI elements to layout
        self.Layout.addWidget(self.font_label)
        self.Layout.addWidget(self.font_toolButton,QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout.addItem(spacerItem)
        
        # Slots
        self.font_toolButton.clicked.connect(self.openFontDialog)
        
    def openFontDialog(self):
        # Open the dialog and get the selected color
        self.font = QtWidgets.QFontDialog.getFont(self.font)[0]
        self.updateFont(self.font)
            
    def updateFont(self,newfont):
        fontsize = newfont.pointSize()
        fontstr = newfont.family()+", "+str(fontsize)
        newfont.setPointSize(12)
        self.font_toolButton.setFont(newfont)
        newfont.setPointSize(fontsize)
        self.font_toolButton.setText(fontstr)
            
            
class ColorPicker (QtWidgets.QWidget):
# This class is just a container for GUI elements useful for color management.
# The GUI has: 1) a toolButton that opens a QColorDialog for picking colors,
#              2) a lineEdit for storing the hexadecimal value of the color
#              3) a spinBox with the value of transparency (alpha)
# The selected color is stored in the variable 'color'

    def __init__(self,parent=None,color='#FFFFFF',longcol=True):
        # Class constructor:
        #   color = the inital color
        #   longcol = if True, the widget comprises the hex lineedit
        #             and alpha spinBox 
        QtWidgets.QWidget.__init__(self)        
        
        # The current selected color (initialized here)
        self.color = QtGui.QColor(color)
        if not self.color.isValid(): self.color =  QtGui.QColor('#FFFFFF')
        
        # Here the GUI begins
        self.Layout = QtWidgets.QHBoxLayout(self)
        self.Layout.setContentsMargins(0,0,0,0)
        
        # Initilize the widget elements
        self.color_label = QtWidgets.QLabel(" Color:      ")
        self.color_toolButton = QtWidgets.QToolButton() 
        self.hex_label = QtWidgets.QLabel(" Hex: ")
        self.hex_lineEdit = QtWidgets.QLineEdit()
        self.alpha_label = QtWidgets.QLabel(" Alpha: ")
        self.alpha_spinBox = QtWidgets.QDoubleSpinBox()
        
        # Some non standard size policies
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.color_toolButton.sizePolicy().hasHeightForWidth())
        self.color_toolButton.setSizePolicy(sizePolicy)
        
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.hex_lineEdit.setSizePolicy(sizePolicy)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        self.alpha_spinBox.setSizePolicy(sizePolicy)

        # Some properties
        self.color_toolButton.setAutoRaise(True)
        self.color_toolButton.setFixedSize(50,20)        
        self.hex_lineEdit.setMaxLength(7)
        self.alpha_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.alpha_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)        
        self.alpha_spinBox.setMaximum(1.0)
        self.alpha_spinBox.setSingleStep(0.1)
        self.alpha_spinBox.setValue(1.00)
        self.changeToolButtonColor(self.color)
        self.hex_lineEdit.setText(self.color.name().upper())
        
        # Add GUI elements to layout
        if longcol: self.Layout.addWidget(self.color_label)
        self.Layout.addWidget(self.color_toolButton,QtCore.Qt.AlignLeft)     
        if longcol:
            self.Layout.addWidget(self.hex_label, 0, QtCore.Qt.AlignRight)
            self.Layout.addWidget(self.hex_lineEdit)
            self.Layout.addWidget(self.alpha_label, 0, QtCore.Qt.AlignRight)
            self.Layout.addWidget(self.alpha_spinBox)
        else:
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.Layout.addItem(spacerItem)
        
            
        
        # Slots
        self.color_toolButton.clicked.connect(self.openColorDialog)
        self.hex_lineEdit.editingFinished.connect(self.updateColor)
        self.alpha_spinBox.editingFinished.connect(self.updateColor)
        
    def openColorDialog(self):
        # Open the dialog and get the selected color
        col = QtWidgets.QColorDialog.getColor(self.color,options=QtWidgets.QColorDialog.ShowAlphaChannel)
        if col.isValid():
            self.color = col
            # Change the color icon and set the hexadecimal lineedit and the alpha spinbox
            self.changeToolButtonColor(col)
            self.hex_lineEdit.setText(col.name().upper())
            self.alpha_spinBox.setValue(col.alphaF())
        
    def updateColor(self):
        # Update the color from the hexadecimal lineEdit and alpha spinBox
        colstr = self.hex_lineEdit.text()
        if QtGui.QColor.isValidColor(colstr):
            self.color = QtGui.QColor(colstr)
            self.color.setAlphaF(self.alpha_spinBox.value())
            self.changeToolButtonColor(self.color)
        else:
            self.hex_lineEdit.setText(self.color.name().upper())
        
    def changeToolButtonColor (self, col):
        # Change the color of the toolButton
        if col.isValid():
            #px = QtGui.QPixmap(20, 20)
            #px.fill(col)
            #icon = QtGui.QIcon()
            #icon.addPixmap(px)
            #self.color_toolButton.setIcon(icon)
            self.color_toolButton.setStyleSheet("background-color: "+self.color.name())
                

class Axes_Tab (QWidget,Ui_Axes_tabwidget):
    def __init__(self, parent=None):
        super(Axes_Tab, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        
        #Initializing the Font Pickers for Labels and Tics
        self.AxesLabelsFont = FontPicker(self)
        self.AxesLabels_gridLayout.addWidget(self.AxesLabelsFont, 3, 0, 1, 2)
        
        self.TicsLabelsFont = FontPicker(self)
        self.Tics_gridLayout.addWidget(self.TicsLabelsFont, 8, 0, 1, 2)

        self.AxesColor = ColorPicker(self,color='#000000',longcol=False)
        self.AxesProperties_gridLayout.addWidget(self.AxesColor, 3, 2, 1, 1)
        
        self.AxesCanvasColor = ColorPicker(self,color='#FFFFFF',longcol=False)
        self.AxesProperties_gridLayout.addWidget(self.AxesCanvasColor, 3, 4, 1, 1)
        
        self.LabelColor = ColorPicker(self,color='#000000',longcol=False)
        self.AxesLabels_gridLayout.addWidget(self.LabelColor, 3, 3)
        
        #Slots
        self.Xrange_checkBox.clicked[bool].connect(self.XrangeClicked)
        self.Yrange_checkBox.clicked[bool].connect(self.YrangeClicked)
        self.XticsMinor_checkBox.clicked[bool].connect(self.XticsMinorClicked)
        self.YticsMinor_checkBox.clicked[bool].connect(self.YticsMinorClicked)
        
    def XrangeClicked(self, checked):
        self.Xrange_from_lineEdit.setEnabled(checked)
        self.Xrange_to_lineEdit.setEnabled(checked)
        
    def YrangeClicked(self, checked):
        self.Yrange_from_lineEdit.setEnabled(checked)
        self.Yrange_to_lineEdit.setEnabled(checked)
        
    def XticsMinorClicked(self, checked):
        self.XticsMinor_spinBox.setEnabled(checked)
        self.XticsMinorLength_doubleSpinBox.setEnabled(checked)
        self.XticsMinorLength_label.setEnabled(checked)
        
    def YticsMinorClicked(self, checked):
        self.YticsMinor_spinBox.setEnabled(checked)
        self.YticsMinorLength_doubleSpinBox.setEnabled(checked)
        self.YticsMinorLength_label.setEnabled(checked)
        
class Plot_Tab (QWidget,Ui_Plot1D_tabwidget):
    def __init__(self, parent=None):
        super(Plot_Tab, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        
        self.MarkColor = ColorPicker(self)
        self.Marker_gridLayout.addWidget(self.MarkColor, 2, 0, 1, 5)
        
        self.MarkEdgeColor = ColorPicker(self)
        self.MarkEdgeColor.color_label.setText(" Edges:     ")
        #self.Marker_gridLayout.addWidget(self.MarkEdgeColor, 3, 0, 1, 5)

        
        #Slots
        self.Xerr_checkBox.clicked[bool].connect(self.XerrClicked)
        self.Yerr_checkBox.clicked[bool].connect(self.YerrClicked)
        self.Rows_from_checkBox.clicked[bool].connect(self.RowsfromClicked)
        self.Rows_all_checkBox.clicked[bool].connect(self.RowsAllClicked)
        
    def XerrClicked(self, checked):
        self.Xerr_file_comboBox.setEnabled(checked)
        self.Xerr_col_comboBox.setEnabled(checked)

    def YerrClicked(self, checked):
        self.Yerr_file_comboBox.setEnabled(checked)
        self.Yerr_col_comboBox.setEnabled(checked)
        
    def RowsfromClicked(self, checked):
        self.Rows_from_spinBox.setEnabled(checked)
        self.Rows_to_spinBox.setEnabled(checked)
    
    def RowsAllClicked(self, checked):
        self.Rows_from_spinBox.setEnabled(not checked)
        self.Rows_to_spinBox.setEnabled(not checked)


class Plot1DWindow(QWidget, Ui_Plot1D_Window):
    def __init__(self, parent=None):
        super(Plot1DWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.file_inp = Filein_Widget(self)
        self.Main_gridLayout.addWidget(self.file_inp,0,0,1,0)
        
        self.GeneralFont = FontPicker(self)
        self.GeneralSettings_gridLayout.addWidget(self.GeneralFont, 1, 0, 1, 2)
        

        
        self.axes_tab = Axes_Tab()
        self.stackedWidget.insertWidget(1,self.axes_tab)
        
        self.plot_tab = Plot_Tab(self)
        self.stackedWidget.insertWidget(4,self.plot_tab)
        

        
        
        
        self.listWidget.currentRowChanged[int].connect(self.Diocare)
        
    def Diocare (self,idx):
        self.stackedWidget.setCurrentIndex(idx)
        
        # Connect all the slots to the correspondent functions
        #self.File_lineEdit.editingFinished.connect(self.FileChanged)
        #self.X_file_comboBox.currentIndexChanged[int].connect(self.X_fileChanged)
        #self.Y_file_comboBox.currentIndexChanged[int].connect(self.Y_fileChanged)

    def grancazzo(self):
        fn = self.file_inp.file_name
        for i, t in enumerate(fn):
            if t is not None:
                cols = self.file_inp.col_name[i]
                print (cols)
            
        print ("sta grande minchia")
            
#    def FileChanged(self):
 #       filename = self.File_lineEdit.text()
  #      filename = os.path.expanduser(filename)

        #if filename: 
        #    print (filename)
        #    self.X_file_comboBox.addItem(filename.split("/")[-1])
        #    self.Y_file_comboBox.addItem(filename.split("/")[-1])
            
            
   # def X_fileChanged(self, item): self.updateColumnComboBox(self.X_col_comboBox,item)     
   # def Y_fileChanged(self, item): self.updateColumnComboBox(self.Y_col_comboBox,item)
        
        
    
    def updateColumnComboBox(self, combobox, item):
        try:
            data = np.genfromtxt(self.files[item], names=True, autostrip=True)
            colnames = data.dtype.names
            combobox.clear()
            for cn in colnames:
                combobox.addItem(cn)
        except:
            print ("NUN CE CAPISCO")
       
        
        
        
        
        
        
        
        r
