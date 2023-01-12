#!/usr/bin/python3
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *

class TinyMCE_on_PyQt_window(QWidget):
    def __init__(self):
        super(TinyMCE_on_PyQt_window, self).__init__()

        # 创建浏览器控件
        self.html_path="."
        self.html_file="/main.html"
        self.browser=QWebEngineView()
        self.url=self.html_path+self.html_file
        # print(self.url)
        self.browser.load(QUrl("http://baidu.com"))
        
        # 设置QWidget的layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

        
    def get_file(self):
        pass
        return

    def save_file(self):
        pass
