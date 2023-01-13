#!/usr/bin/python3
import sys,os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *

class TinyMCE_on_PyQt_window(QWidget):
    def __init__(self):
        super(TinyMCE_on_PyQt_window, self).__init__()

        # 创建浏览器控件
        self.browser = QWebEngineView()
        self.url = QFileInfo("./main.html").absoluteFilePath()
        print(self.url)
        self.browser.load(QUrl("file://"+self.url))
        
        # 设置QWidget的layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

        
    def get_file(self):
        pass
        return

    def save_file(self):
        pass
