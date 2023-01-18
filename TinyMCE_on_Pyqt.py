#!/usr/bin/python3
import sys,os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import *
from PySide6.QtWebChannel import *
import logging

import json
import threading

logging.basicConfig(level=logging.DEBUG) #设置日志等级

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

        self.refresh_state=True #TinyMCE文本刷新状态，True代表刷新完成内容可用，False代表正在等待JS回调

    def init(self):
        # 创建浏览器控件
        self.browser = QWebEngineView()
        self.browser.load(QUrl("file://"+self.url))

        # 新建QWebChannel
        self.channel = QWebChannel()
        self.browser.page().setWebChannel(self.channel)

        self.browser.page().loadFinished.connect(self.init_TinyMCE)
        
        # 设置QWidget的layout
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

    def init_TinyMCE(self):
        #初始化TinyMCE(调用JS)
        self.browser.page().runJavaScript("init_editor('%s');" % self.TinyMCE_config)

    # 刷新TinyMCE编辑器的内容
    def __call_back(self,result):
        logging.info("已收到call back")
        self.content=result
        self.refresh_state=True #回调完成，self.content内容已刷新，内容 可用(最新)
    def refresh_content(self):
        logging.info("开始刷新TinyMCE内容")
        self.refresh_state=False #开始等待回调，内容 不可用(不一定最新)
        self.browser.page().runJavaScript("tinymce.activeEditor.getContent();",0,self.__call_back)
    
    # 当newest为True时，进程将堵塞等待刷新完成
    def get_file(self):
        self.refresh_content() #开始刷新内容
        logging.info("开始堵塞，等待刷新完成")
        while not self.refresh_state: # 当内容没有刷新完成时进行堵塞
            QApplication.processEvents()
            pass
        return self.content

    def save_file(self,url,refresh=True):
        with open(url, mode='w', encoding='utf-8') as file_obj:
            if refresh:
                file_obj.write(self.get_file())
            else:
                file_obj.write(self.content)

    def set_html(self,html_code):
        self.browser.page().runJavaScript("tinymce.activeEditor.setContent('%s');" % html_code)
