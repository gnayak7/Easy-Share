 python#!/usr/bin/python
import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
win=QtGui.QWidget()
grid = QtGui.QGridLayout()
label=QtGui.QLabel(sys.argv[1])
grid.addWidget(label, 3, 2)
win.setLayout(grid) 
win.show()
sys.exit(app.exec_())   
