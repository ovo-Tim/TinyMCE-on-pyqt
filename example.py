#!/usr/bin/python3
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

import TinyMCE_on_Pyqt as editor

app=QApplication(sys.argv)
win=editor.TinyMCE_on_PyQt_window()
win.show()
app.exit(app.exec())