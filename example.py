#!/usr/bin/python3
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

from qt_material import apply_stylesheet

import TinyMCE_on_Pyqt as editor

class my_TinyMCE(editor.TinyMCE_on_PyQt_window):
    def __init__(self):
        super(my_TinyMCE, self).__init__()
        # 添加保存按钮
        self.save_button = QPushButton("保存文件",self)
        self.save_button.clicked.connect(self.choose_file)
        self.layout.addWidget(self.save_button)

    # 监听键盘
    def keyPressEvent(self, event):
        if QApplication.keyboardModifiers() == Qt.ControlModifier and event.key() == Qt.Key_S: #检测CtrlS保存按键
            self.choose_file()

    def choose_file(self):
        file_url = QFileDialog.getSaveFileName(self, 
              "设置保存位置","./",
              "All Files (*);;Text Files (*.html)")[0]

        self.save_file(file_url)
            



app=QApplication(sys.argv)
apply_stylesheet(app, theme='dark_teal.xml')
win=my_TinyMCE()
win.init()
win.show()
app.exit(app.exec())