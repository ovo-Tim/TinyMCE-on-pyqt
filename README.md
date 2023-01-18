# TinyMCE on PyQt
主要作用是在pyqt中方便的开发富文本编辑器
## 目标
### 已实现
- ✅ 使用面向对象的思想，方便调用
- ✅ 加载大量插件
- ✅ 支持图片
- ✅ 由Python控制配置
- ✅ 由Python控制保存位置
- ✅ Python端控制TinyMCE配置
- ✅ 打开html文件
### 待实现
- ❎ 打包成Python库，并发布到PyPi

## 快速上手
可以查看 [例子](example.py) ,比较简单方便上手
### 开始
#### 导入pyside和本库
``` python
#!/usr/bin/python3

# 导入PySide
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

import TinyMCE_on_Pyqt as editor # 导入本库

from qt_material import apply_stylesheet #美化包(可选)
```
#### 直接使用
``` python
app=QApplication(sys.argv)
apply_stylesheet(app, theme='dark_teal.xml') #设置主题(可选)
win=editor.TinyMCE_on_PyQt_window()
win.init() #初始化
win.show()
app.exit(app.exec())
```
#### 继承(推荐)
``` python
class my_TinyMCE(editor.TinyMCE_on_PyQt_window):
    def __init__(self):
        super(my_TinyMCE, self).__init__()

app=QApplication(sys.argv)
apply_stylesheet(app, theme='dark_teal.xml')
win=my_TinyMCE()
win.init()
win.show()
app.exit(app.exec())
```
#### 选择文件并保存
``` python 
def choose_file(self):
    file_url = QFileDialog.getSaveFileName(self, 
            "设置保存位置","./",
            "All Files (*);;Text Files (*.html)")[0]

    self.save_file(file_url)
```

## 个性化说明
### 重写html
默认的html文件位于 `./main.html`

默认定义代码为 `self.url = QFileInfo("./main.html").absoluteFilePath()` (注意此处必须修改为**绝对路径**)

您可以自定义您的html为 `self.url = QFileInfo(你的html位置).absoluteFilePath()`

### 修改TinyMCE配置
默认的配置
``` python
json.dumps({ #转为json方便与JS交互
    'selector': '#TinyMCE',
    'language': 'zh_CN',
    'height': 'calc(100vh)',
    'plugins':'code,table,autosave,lists,advlist,anchor,autolink,charmap,emoticons,insertdatetime,media,preview,quickbars,searchreplace,template,wordcount',
    'toolbar': ['aligncenter | alignjustify | alignleft | alignnone | alignright | blockquote | backcolor | blocks | bold | copy | cut | fontfamily | fontsize | forecolor | h1 | h2 | h3 | h4 | h5 | h6 | newdocument | outdent | paste | pastetext | print | redo | remove | removeformat | selectall | strikethrough | styles | subscript | superscript | underline | undo | visualaid | code | restoredraft | bullist | anchor | link | charmap | emoticons | insertdatetime | media | preview | searchreplace | table tabledelete | tableprops tablerowprops tablecellprops | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol | template | wordcount']
}
```

您可以自定义 `self.TinyMCE_config="你的配置(json格式)"` (此处为了方便交互，配置必须为**json格式**，JS那边会自动转换)

### 获取TinyMCE的html内容
内容会保存在 `self.content` 当中，但是并**不是实施刷新**的
#### 刷新内容
您可以使用 `refresh_content()` 来刷新 `self.content` (`refresh_content()`**不会堵塞**，由 `self.refresh_state` 来表示TinyMCE文本刷新状态，True代表刷新完成内容可用，False代表正在等待JS回调)
#### 获取内容(有堵塞)
你可以使用 `get_file()` 来确保获取到的内容是最新的，等待回调时会使用一下代码来堵塞
``` python
while not self.refresh_state: # 当内容没有刷新完成时进行堵塞
    QApplication.processEvents()
```
#### 保存文件
`save_file(路径,是否刷新文件确保最新)`

### 设置内容
#### 设置html
`set_html(html代码)`
#### 打开文件
``` python
def open_file(self):
    file_url = QFileDialog.getOpenFileName(self, 
            "选择打开位置","./",
            "All Files (*);;Text Files (*.html)")[0]
    print(file_url)
    with open(file_url, mode='r', encoding='utf-8') as file_obj:
        self.set_html(file_obj.read())
```

## 帮助我们改进
显然这是一个刚刚入门pyqt的小菜鸟写的程序，所以如果您有任何好的建议都可以提交issues或PR😊
### 代码规范程度
很多的程序员都不愿意提高自己的代码规范程度 ~~进而形成屎山代码~~

在本程序当中我已经尽量使用了**面向对象**的思想，尽量将一个功能**封装**函数，并添加了较多**注释**，但是我必定存在**大量缺陷**🤔，希望交流时可以友好交流😊