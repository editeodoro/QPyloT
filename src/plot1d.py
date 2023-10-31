### ----------------------------------------------------------------------------
### plot1d.py: Plot1DWindow class definition derived from Ui_Plot1D_Window class.
###            It controls the actions on the 1D plot window
### ----------------------------------------------------------------------------

import os
import numpy as np
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from moc.ui_plot1d import Ui_Plot1D_Window
from moc.ui_plot1d_tabw import Ui_Plot1D_tabwidget
from moc.ui_axes_tabw import Ui_Axes_tabwidget
from moc.ui_right_selector import Ui_Right_Selector

from PyQt6 import QtWidgets, QtCore, QtGui

class Selector(QtWidgets.QWidget, Ui_Right_Selector):
    
    # Some signals to emit when row is changed 
    # or when a plot is added/deleted/reordered
    rowChanged  = QtCore.pyqtSignal(int)
    plotAdded   = QtCore.pyqtSignal(str,int)
    plotDeleted = QtCore.pyqtSignal(int)
    plotOrder   = QtCore.pyqtSignal(int,str)
    
    def __init__(self, parent=None):
        super(Selector, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
                
        # Adding a contextual menu to the Plus button:
        # The user can choose between a new plot, function or histogram
        self.Plus_Menu = QMenu(self)
        self.add_plot = QAction("Add plot",self)
        self.add_func = QAction("Add function",self)
        self.add_hist = QAction("Add histogram",self)

        self.Plus_Menu.addAction(self.add_plot)
        self.Plus_Menu.addAction(self.add_func)
        self.Plus_Menu.addAction(self.add_hist)
        self.Plus_toolButton.setMenu(self.Plus_Menu)
        
        # Slots
        self.listWidget.currentRowChanged[int].connect(self.RowChanged)
        self.Minus_toolButton.clicked.connect(self.MinusButtonClicked)
        self.Up_toolButton.clicked.connect(self.ReorderEntries)
        self.Down_toolButton.clicked.connect(self.ReorderEntries)
        self.add_plot.triggered.connect(self.PlusButtonClicked)
        self.add_func.triggered.connect(self.PlusButtonClicked)
        self.add_hist.triggered.connect(self.PlusButtonClicked)
        
        # Counters of added plots, functions and histograms
        self.nplot, self.nfunc, self.nhist = 1, 0, 0
        
        # Type of plots: "PLOT", "FUNC" or "HIST"
        self.type = ["PLOT"]
        
        # The first index of the list referring to a plot
        self.firstplot = 4
        
    
        
    @QtCore.pyqtSlot(int)
    def RowChanged(self,idx):
        # Enable the Minus, Up and Down buttons if we are in 'Data' list
        # and emit the rowChaged signal
        if idx>=self.firstplot: isEnabled = True
        else: isEnabled = False
        self.Minus_toolButton.setEnabled(isEnabled)
        self.Down_toolButton.setEnabled(isEnabled)
        self.Up_toolButton.setEnabled(isEnabled)
        self.rowChanged.emit(idx)
    
    
    @QtCore.pyqtSlot()
    def MinusButtonClicked(self):
        # Delete a plot
        curRow = self.listWidget.currentRow()
        ptype = self.type[curRow-self.firstplot]
        self.listWidget.takeItem(curRow)
        self.type.pop(curRow-self.firstplot)


    @QtCore.pyqtSlot()
    def ReorderEntries(self):
        # This function reorder the entries in the listWidget
        if len(self.type)==1: return
        curRow = self.listWidget.currentRow()
        np = curRow-self.firstplot
        if self.sender()==self.Up_toolButton: 
        # Moves the item up
            if np==0: return
            curItem = self.listWidget.takeItem(curRow)
            self.listWidget.insertItem(curRow-1, curItem)
            self.listWidget.setCurrentRow(curRow-1)
            self.type[np-1], self.type[np] = self.type[np], self.type[np-1]
            self.plotOrder.emit(curRow,"up")
        else:    
        # Moves the item down
            if (np==self.listWidget.count()-self.firstplot-1): return
            curItem = self.listWidget.takeItem(curRow);
            self.listWidget.insertItem(curRow+1, curItem)
            self.listWidget.setCurrentRow(curRow+1)
            self.type[np+1], self.type[np] = self.type[np], self.type[np+1]
            self.plotOrder.emit(curRow,"down")
            
            
    @QtCore.pyqtSlot()
    def PlusButtonClicked(self):
        # Function to add a plot
        if self.sender()==self.add_plot:
            self.nplot += 1
            name = ["    Plot"+str(self.nplot), "PLOT"]
        elif self.sender()==self.add_func:
            self.nfunc += 1
            name = ["    Function"+str(self.nfunc), "FUNC"]
        if self.sender()==self.add_hist:
            self.nhist += 1
            name = ["    Histogram"+str(self.nhist), "HIST"]
        
        # Add the item to the qlistwidget
        item = QListWidgetItem(name[0])
        item.setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.listWidget.addItem(item)

        # Send a signal to the parent widget to add a plot tab
        self.plotAdded.emit(name[1],self.firstplot+len(self.type))
        self.type.append(name[1])
        
        
    def getNumberOfPlots(self):
        # This function return the total number of plots and the number of each type
        np,nf,nh = self.type.count("PLOT"),self.type.count("FUNC"),self.type.count("HIST")
        ntot = np+nf+nh
        return ntot, np, nf, nh
        

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
<<<<<<< HEAD
        # The QMenu as two actions: Add and Remove a file
        self.File_Menu.append(QMenu(self))
        self.add_act.append(QAction("Add file",self))
        self.rem_act.append(QAction("Remove file",self))
=======
        # The QMenu has two actions: Add and Remove a file
        self.File_Menu.append(QtWidgets.QMenu(self))
        self.add_act.append(QtWidgets.QAction("Add file",self))
        self.rem_act.append(QtWidgets.QAction("Remove file",self))
>>>>>>> b002e0e61a5c037ff2afbf683205b72da1b0baed
        self.add_act[r].triggered.connect(self.addFile)
        self.rem_act[r].triggered.connect(self.removeFile)
        if r==0: self.rem_act[r].setDisabled(True)
        self.File_Menu[r].addAction(self.add_act[r])
        self.File_Menu[r].addAction(self.rem_act[r])
        self.File_toolButton.append(QtWidgets.QToolButton(self))
        self.File_toolButton[r].setMenu(self.File_Menu[r])
        self.File_toolButton[r].setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.File_toolButton[r].setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
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
    
    @QtCore.pyqtSlot()
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
        
        # The current selected font (initialized here)
        self.font = QtGui.QFont(font)

        # Here the GUI begins
        self.Layout = QtWidgets.QHBoxLayout(self)
        self.Layout.setContentsMargins(0,2,0,2)
        
        # Initilize the widget elements
        self.font_label = QtWidgets.QLabel(" Font:   ")
        self.font_toolButton = QtWidgets.QToolButton()
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.font_toolButton.setSizePolicy(sizePolicy)
        
        # Some properties
        self.font_toolButton.setAutoRaise(True)
        self.updateFont(self.font)
        
        # Add GUI elements to layout
        self.Layout.addWidget(self.font_label)
        self.Layout.addWidget(self.font_toolButton,QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem = QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.Layout.addItem(spacerItem)
        
        # Slots
        self.font_toolButton.clicked.connect(self.openFontDialog)
        
    @QtCore.pyqtSlot()
    def openFontDialog(self):
        # Open the dialog and get the selected color
        self.font = QFontDialog.getFont(self.font)[0]
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
        pol = QSizePolicy.Policy
        sizePolicy = QtWidgets.QSizePolicy(pol.MinimumExpanding, pol.Fixed)
        self.color_toolButton.setSizePolicy(sizePolicy)
        sizePolicy = QtWidgets.QSizePolicy(pol.Maximum, pol.Fixed)
        self.hex_lineEdit.setSizePolicy(sizePolicy)
        sizePolicy = QtWidgets.QSizePolicy(pol.Maximum, pol.Fixed)
        self.alpha_spinBox.setSizePolicy(sizePolicy)

        # Some properties
        self.color_toolButton.setAutoRaise(True)
        self.color_toolButton.setFixedSize(50,20)        
        self.hex_lineEdit.setMaxLength(7)
        self.alpha_spinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.alpha_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)        
        self.alpha_spinBox.setMaximum(1.0)
        self.alpha_spinBox.setSingleStep(0.1)
        self.alpha_spinBox.setValue(1.00)
        self.changeToolButtonColor(self.color)
        self.hex_lineEdit.setText(self.color.name().upper())
        
        # Add GUI elements to layout
        if longcol: self.Layout.addWidget(self.color_label)
        self.Layout.addWidget(self.color_toolButton,QtCore.Qt.AlignmentFlag.AlignLeft)     
        if longcol:
            self.Layout.addWidget(self.hex_label, 0, QtCore.Qt.AlignmentFlag.AlignRight)
            self.Layout.addWidget(self.hex_lineEdit)
            self.Layout.addWidget(self.alpha_label, 0, QtCore.Qt.AlignmentFlag.AlignRight)
            self.Layout.addWidget(self.alpha_spinBox)
        else:
            spacerItem = QtWidgets.QSpacerItem(40, 20, pol.Expanding, pol.Minimum)
            self.Layout.addItem(spacerItem)
        
            
        
        # Slots
        self.color_toolButton.clicked.connect(self.openColorDialog)
        self.hex_lineEdit.editingFinished.connect(self.updateColor)
        self.alpha_spinBox.editingFinished.connect(self.updateColor)

    @QtCore.pyqtSlot()
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
                

class LineStyleSelector (QtWidgets.QWidget):
# This class is just a container for GUI elements useful for linestyle management.
# The GUI has: 

    def __init__(self,parent=None,lstyle='solid',lwidth=1.,lcolor='#000000'):
        # Class constructor
        QtWidgets.QWidget.__init__(self)        
        
        self.Layout = QtWidgets.QGridLayout(self)
        self.Layout.setContentsMargins(0,0,0,0)
        
        self.lstyle = lstyle
        
        # Initilize the widget elements
        self.lstyle_label = QtWidgets.QLabel(" Line style:  ")
        self.lwidth_label = QtWidgets.QLabel(" Line width:  ")
        self.lcolor_label = QtWidgets.QLabel(" Color:  ")
        self.lstyle_comboBox = QtWidgets.QComboBox(self)
        self.lstyle_lineEdit = QtWidgets.QLineEdit(self)
        self.lwidth_spinBox = QtWidgets.QDoubleSpinBox(self)
        self.lcolor = ColorPicker(self,color=lcolor,longcol=False)
        
        # Elements Properties
        alig = QtCore.Qt.AlignmentFlag
        self.lstyle_label.setAlignment(alig.AlignRight|alig.AlignTrailing|alig.AlignVCenter)
        self.lwidth_label.setAlignment(alig.AlignRight|alig.AlignTrailing|alig.AlignVCenter)
        self.lcolor_label.setAlignment(alig.AlignRight|alig.AlignTrailing|alig.AlignVCenter)
        self.lwidth_spinBox.setAlignment(alig.AlignRight|alig.AlignTrailing|alig.AlignVCenter)
        self.lwidth_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.lstyle_comboBox.addItem("solid")
        self.lstyle_comboBox.addItem("dashed")
        self.lstyle_comboBox.addItem("dotted")
        self.lstyle_comboBox.addItem("dashdotted")
        self.lstyle_comboBox.addItem("custom")
        self.lstyle_lineEdit.setHidden(True)

        # Adding to layout
        self.Layout.addWidget(self.lstyle_label,0,0,1,1)
        self.Layout.addWidget(self.lstyle_comboBox,0,1,1,1)
        self.Layout.addWidget(self.lstyle_lineEdit,0,2,1,2)
        self.Layout.addWidget(self.lwidth_label,1,0,1,1)
        self.Layout.addWidget(self.lwidth_spinBox,1,1,1,1)
        self.Layout.addWidget(self.lcolor_label,1,2,1,1)
        self.Layout.addWidget(self.lcolor,1,3,1,1)

        #Slots
        #self.lstyle_comboBox.activated[str].connect(self.LineStyleActivated)
        
    @pyqtSlot(str)
    def LineStyleActivated(self, val):
        if val=='custom':
            self.lstyle_lineEdit.setHidden(False)
        else:
            self.lstyle_lineEdit.setHidden(True)
            self.lstyle = val
            
            

class Axes_Tab (QWidget,Ui_Axes_tabwidget):
    def __init__(self, parent=None):
        super(Axes_Tab, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        
        
        #Initializing the Font Pickers and Color Picker for Labels and Tics
        self.AxesLabelsFont = FontPicker(self)
        self.AxesLabels_gridLayout.addWidget(self.AxesLabelsFont, 3, 0, 1, 2)
        
        self.LabelColor = ColorPicker(self,color='#000000',longcol=False)
        self.AxesLabels_gridLayout.addWidget(self.LabelColor, 3, 3)
        
        self.TicsLabelsFont = FontPicker(self)
        self.Tics_gridLayout.addWidget(self.TicsLabelsFont, 8, 0, 1, 3)

        self.TicsLabelColor = ColorPicker(self,color='#000000',longcol=False)
        self.Tics_gridLayout.addWidget(self.TicsLabelColor, 8, 4,1,3)

        self.AxesColor = ColorPicker(self,color='#000000',longcol=False)
        self.AxesProperties_gridLayout.addWidget(self.AxesColor, 3, 2, 1, 1)
        
        self.AxesCanvasColor = ColorPicker(self,color='#FFFFFF',longcol=False)
        self.AxesProperties_gridLayout.addWidget(self.AxesCanvasColor, 3, 4, 1, 1)
        
        self.GridLineStyle = LineStyleSelector(self,lstyle="dotted",lwidth=0.5)
        self.AxesProperties_gridLayout.addWidget(self.GridLineStyle, 5, 1, 2, 4)
        self.GridLineStyle.setEnabled(False)

        
        
        
        self.tabWidget.setCurrentIndex(0)
        
        #Slots
        self.Grid_checkBox.clicked[bool].connect(self.GridClicked)
        self.Xrange_checkBox.clicked[bool].connect(self.XrangeClicked)
        self.Yrange_checkBox.clicked[bool].connect(self.YrangeClicked)
        self.XticsMinor_checkBox.clicked[bool].connect(self.TicsMinorClicked)
        self.YticsMinor_checkBox.clicked[bool].connect(self.TicsMinorClicked)
        self.showLeft_checkBox.clicked[bool].connect(self.showAxisClicked)
        self.showBottom_checkBox.clicked[bool].connect(self.showAxisClicked)
        self.showRight_checkBox.clicked[bool].connect(self.showAxisClicked)
        self.showTop_checkBox.clicked[bool].connect(self.showAxisClicked)
    
    
    @QtCore.pyqtSlot(bool)
    def GridClicked(self, checked):
        self.GridLineStyle.setEnabled(checked)
    
    @QtCore.pyqtSlot(bool)
    def XrangeClicked(self, checked):
        self.Xrange_from_lineEdit.setEnabled(checked)
        self.Xrange_to_lineEdit.setEnabled(checked)
    
    @QtCore.pyqtSlot(bool)
    def YrangeClicked(self, checked):
        self.Yrange_from_lineEdit.setEnabled(checked)
        self.Yrange_to_lineEdit.setEnabled(checked)
    
    @QtCore.pyqtSlot(bool)
    def TicsMinorClicked(self, checked):
        # Enable the fields for minor tics
        if (self.sender()==self.XticsMinor_checkBox):
            self.XticsMinor_spinBox.setEnabled(checked)
            self.XticsMinorLength_doubleSpinBox.setEnabled(checked)
            self.XticsMinorLength_label.setEnabled(checked)
            self.XticsMinorWidth_doubleSpinBox.setEnabled(checked)
            self.XticsMinorWidth_label.setEnabled(checked)
        elif (self.sender()==self.YticsMinor_checkBox):
            self.YticsMinor_spinBox.setEnabled(checked)
            self.YticsMinorLength_doubleSpinBox.setEnabled(checked)
            self.YticsMinorLength_label.setEnabled(checked)
            self.YticsMinorWidth_doubleSpinBox.setEnabled(checked)
            self.YticsMinorWidth_label.setEnabled(checked)
            
    @QtCore.pyqtSlot(bool)
    def showAxisClicked(self, checked):
        # If an axis is disabled, disabling the corresponding tics
        snd = self.sender()
        if   (snd==self.showLeft_checkBox):   cBox = self.TicsLeft_checkBox
        elif (snd==self.showBottom_checkBox): cBox = self.TicsBottom_checkBox
        elif (snd==self.showRight_checkBox):  cBox = self.TicsRight_checkBox
        elif (snd==self.showTop_checkBox):    cBox = self.TicsTop_checkBox
        cBox.setChecked(checked)
        cBox.setEnabled(checked)
        
class Plot_Tab (QWidget,Ui_Plot1D_tabwidget):
    def __init__(self, parent=None, plottype="PLOT"):
        super(Plot_Tab, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        
        self.MarkColor = ColorPicker(self)
        self.Marker_gridLayout.addWidget(self.MarkColor, 2, 0, 1, 5)
        
        self.MarkEdgeColor = ColorPicker(self)
        self.MarkEdgeColor.color_label.setText(" Edges:     ")
        #self.Marker_gridLayout.addWidget(self.MarkEdgeColor, 3, 0, 1, 5)

        self.tabWidget.setCurrentIndex(0)
        
        #Slots
        self.Xerr_checkBox.clicked[bool].connect(self.XerrClicked)
        self.Yerr_checkBox.clicked[bool].connect(self.YerrClicked)
        self.Rows_from_checkBox.clicked[bool].connect(self.RowsfromClicked)
        self.Rows_all_checkBox.clicked[bool].connect(self.RowsAllClicked)
        
    @QtCore.pyqtSlot(bool)
    def XerrClicked(self, checked):
        self.Xerr_file_comboBox.setEnabled(checked)
        self.Xerr_col_comboBox.setEnabled(checked)

    @QtCore.pyqtSlot(bool)
    def YerrClicked(self, checked):
        self.Yerr_file_comboBox.setEnabled(checked)
        self.Yerr_col_comboBox.setEnabled(checked)
    
    @QtCore.pyqtSlot(bool)
    def RowsfromClicked(self, checked):
        self.Rows_from_spinBox.setEnabled(checked)
        self.Rows_to_spinBox.setEnabled(checked)
    
    @QtCore.pyqtSlot(bool)
    def RowsAllClicked(self, checked):
        self.Rows_from_spinBox.setEnabled(not checked)
        self.Rows_to_spinBox.setEnabled(not checked)


class Plot1DWindow(QWidget, Ui_Plot1D_Window):
    def __init__(self, parent=None):
        super(Plot1DWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.file_inp = Filein_Widget(self)
        self.Main_gridLayout.addWidget(self.file_inp,0,0,1,4)
        
        self.selector = Selector(self)       
        self.Main_gridLayout.addWidget(self.selector,1,0,1,1)
        
        self.GeneralFont = FontPicker(self)
        self.GeneralSettings_gridLayout.addWidget(self.GeneralFont, 1, 0, 1, 2)

        self.axes_tab = Axes_Tab()
        self.stackedWidget.insertWidget(1,self.axes_tab)
        
        
        
        self.plot_tab = []
        self.addPlot_tab("PLOT",self.selector.firstplot)
                
        self.selector.rowChanged[int].connect(self.Diocare)
        self.selector.plotAdded[str,int].connect(self.addPlot_tab)
        self.selector.plotOrder[int,str].connect(self.reorderPlot_tab)
        
        
        self.stackedWidget.setCurrentIndex(0)
        
    def addPlot_tab (self, plottype, idx):
        self.plot_tab.append(Plot_Tab(self,plottype=plottype))
        self.stackedWidget.insertWidget(idx,self.plot_tab[-1])
    
    def reorderPlot_tab (self, idx, direc):
        np = idx-self.selector.firstplot
        curWid = self.stackedWidget.widget(idx)
        if direc.lower()=="up": insrow, insn = idx-1, np-1
        else: insrow, insn = idx+1, np+1
        self.stackedWidget.insertWidget(insrow, curWid)
        self.stackedWidget.setCurrentIndex(insrow)
        self.plot_tab[insn], self.plot_tab[np] = self.plot_tab[np], self.plot_tab[insn]
        
        
        print (self.stackedWidget.count())
    
    def Diocare (self,idx):
        self.stackedWidget.setCurrentIndex(idx)
        


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
