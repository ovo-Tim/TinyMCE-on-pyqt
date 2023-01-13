#!/usr/bin/python3
import sys,os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *

import json

class TinyMCE_on_PyQt_window(QWidget):
    def __init__(self):
        super(TinyMCE_on_PyQt_window, self).__init__()

        self.url = QFileInfo("./main.html").absoluteFilePath()
        self.layout = QVBoxLayout() 
        self.TinyMCE_config=json.dumps({ #转为json方便与JS交互
            'selector': '#TinyMCE',
            'language': 'zh_CN',
            'height': 'calc(100vh)',
            'plugins':'code,table,autosave,lists,advlist,anchor,autolink,charmap,emoticons,insertdatetime,media,preview,quickbars,searchreplace,template,wordcount',
            'toolbar': ['aligncenter | alignjustify | alignleft | alignnone | alignright | blockquote | backcolor | blocks | bold | copy | cut | fontfamily | fontsize | forecolor | h1 | h2 | h3 | h4 | h5 | h6 | newdocument | outdent | paste | pastetext | print | redo | remove | removeformat | selectall | strikethrough | styles | subscript | superscript | underline | undo | visualaid | code | restoredraft | bullist | anchor | link | charmap | emoticons | insertdatetime | media | preview | searchreplace | table tabledelete | tableprops tablerowprops tablecellprops | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol | template | wordcount']
        })

    def init(self):
        # 创建浏览器控件
        self.browser = QWebEngineView()
        self.browser.load(QUrl("file://"+self.url))

        #初始化TinyMCE(调用JS)
        self.browser.page().runJavaScript("window.init('%s')" % self.TinyMCE_config)
        
        # 设置QWidget的layout
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)
        
    def get_file(self):
        pass
        return

    def save_file(self):
        pass
