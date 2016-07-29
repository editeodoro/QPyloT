### ----------------------------------------------------------------------------
### plot1d.py: Plot1DWindow class definition derived from Ui_Plot1D_Window class.
###            It controls the actions on the 1D plot window
### ----------------------------------------------------------------------------

import os
import numpy as np
from PyQt5.QtWidgets import *
from moc.ui_plot1d import Ui_Plot1D_Window
from moc.ui_plot1d_tabw import Ui_Plot1D_tabwidget

from PyQt5 import QtWidgets, QtCore, QtGui

class Filein_Widget(QtWidgets.QWidget):
# This class is just a container for an array (lineedit + button Open + button Add)
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self)        
        # GUI elements and settings
        self.parent = parent
        self.Layout = QtWidgets.QGridLayout(self)
        
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


class Plot_Tab (QWidget,Ui_Plot1D_tabwidget):
    def __init__(self, parent=None):
        super(Plot_Tab, self).__init__(parent)
        self.setupUi(self)


class Plot1DWindow(QMainWindow, Ui_Plot1D_Window):
    def __init__(self, parent=None):
        super(Plot1DWindow, self).__init__(parent)
        self.setupUi(self)
    
        self.file_inp = Filein_Widget(self)
        self.Main_gridLayout.addWidget(self.file_inp,0,0,1,0)
        self.plot_tab = Plot_Tab(self)
        #self.Main_gridLayout.addWidget(self.plot_tab,1,2)
        
        self.stackedWidget.insertWidget(6,self.plot_tab)
        
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
