#!/usr/bin/python3
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class TinyMCE_on_PyQt_window(QWidget):
    def __init__(self,port=1145):
        super(TinyMCE_on_PyQt_window, self).__init__()

        self.service_port=port
        self.html_path="./html"
        self.html_file="/main.html"

        self.browser=QWebEngineView()
        self.url=self.html_path+self.html_file
        self.browser.load(QUrl(self.url))
        self.setCentralWidget(self.browser) 
        
