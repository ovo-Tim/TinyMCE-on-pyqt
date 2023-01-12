#!/usr/bin/python3
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

import TinyMCE_on_Pyqt as editor

app=QApplication(sys.argv)
win=editor.TinyMCE_on_PyQt_window()
win.show()
app.exit(app.exec_())