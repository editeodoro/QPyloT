try:
    from PySide.QtWidgets import *
except:
    from PyQt5.QtWidgets import *
    
    
    
import sys,subprocess

from moc.ui_start import Ui_Start_Window
from plot1d import Plot1DWindow

from moc.ui_qpylot import Ui_QPyLOTWindow

from PyQt5 import QtGui

def open_file(filename):
    if sys.platform.startswith('darwin'):
        subprocess.call(('open', filename))
    elif os.name == 'nt':
        os.startfile(filepath)
    elif os.name == 'posix':
        subprocess.call(('xdg-open', filename))


class StartWindow(QMainWindow, Ui_Start_Window):
    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setupUi(self)
        self.plot1d_w = None
        self.plot2d_w = None

        # Set the QToolBar with different QAction. The QActionGroup is used for
        # keep button-down the selected QAction. You can do the same with 
        # QToolButton and QButtonGroup 
        self.actionGroup = QActionGroup(parent)
        self.actionPlot1D = QAction("Plot1D", self.actionGroup)
        self.actionPlot1D.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot1D.setIcon(icon)
        self.actionPlot2D = QAction("Plot2D", self.actionGroup)
        self.actionPlot2D.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/plus_128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot2D.setIcon(icon)
        self.mainToolBar.addAction(self.actionPlot1D)
        self.mainToolBar.addAction(self.actionPlot2D)
        
        
        
        
        
        self.actionPlot1D.triggered.connect(self.openPlot1D_Window)
        self.pushButton_plot1d.clicked.connect(self.openPlot1D_Window)
        self.pushButton_plot2d.clicked.connect(self.openPlot2D_Window)

        
    def openPlot1D_Window(self):
        if self.plot1d_w is None:
            self.plot1d_w = Plot1DWindow(self)
        self.plot1d_w.show()

    def openPlot2D_Window(self):
        if self.plot2d_w is None:
            self.plot2d_w = Plot2DWindow(self)
        self.plot2d_w.show()


    def chk_fun(self):
	    print("Good.")
        
    






class Plot2DWindow(QMainWindow, Ui_QPyLOTWindow):
    def __init__(self, parent=None):
        super(Plot2DWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = StartWindow()
 #   frame = Plot1DWindow()
    frame.show()
    app.exec_()
	
	
	

	    
