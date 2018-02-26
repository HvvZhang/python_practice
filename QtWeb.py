'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    # 自定义信号
    my_signal = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 信号槽机制，与处理函数绑定
        #self.windowTitleChanged.connect(lambda x : self._my_func('app',666))
        self.windowTitleChanged.connect(self._my_func)
        # 设置窗口标题
        self.setWindowTitle('My First App')
        # 设置标签
        label = QLabel('Welcome to Shiyanlou!')
        # 设置标签显示在中央
        label.setAlignment(Qt.AlignCenter)
        # 添加标签到主窗口
        self.setCentralWidget(label)

        # 创建工具栏
        tb = QToolBar('Tool Bar')
        # 添加工具栏到主窗口
        self.addToolBar(tb)

        button = QPushButton('Click me')
        button.pressed.connect(self._click_button)
        self.my_signal.connect(self._my_func)
        # 添加到主窗口
        self.setCentralWidget(button)


        
        # 添加布局
        layout = QHBoxLayout()

        # 创建按钮
        for i in range(5):
            button = QPushButton(str(i))
            # 将按钮按压信号与自定义函数关联
            button.pressed.connect(lambda x=i: self._my_func(x))
            # 将按钮添加到布局中
            layout.addWidget(button)

        # 创建部件
        widget = QWidget()
        # 将布局添加到部件
        widget.setLayout(layout)
        # 将部件添加到主窗口上
        self.setCentralWidget(widget)

        # 自定义的信号处理函数
    def _click_button(self):
        self.my_signal.emit('shiyan')

    def _my_func(self, s):
        print(s)

    def _my_func1(self, n):
        print('click button %s' % n)

    def _my_func2(self, s='my_func', a=100):
        dic = {'s':s, 'a':a}
        print(dic) 



# 创建应用实例，通过 sys.argv 传入命令行参数
app = QApplication(sys.argv)
# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()
'''
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('My Browser')
        # 设置窗口图标
        self.setWindowIcon(QIcon('icons/penguin.png'))
        self.show()

        # 设置浏览器
        self.browser = QWebEngineView() # 加载渲染网页
        url = 'https://www.baidu.com/'
        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(url))
         # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)
        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        # 设定图标的大小
        navigation_bar.setIconSize(QSize(16, 16))
        self.addToolBar(navigation_bar)

        # 添加前进、后退、停止加载和刷新的按钮
        back_button = QAction(QIcon('icons/back.png'), 'Back', self)
        next_button = QAction(QIcon('icons/next.png'), 'Forward', self)
        stop_button = QAction(QIcon('icons/cross.png'), 'stop', self)
        reload_button = QAction(QIcon('icons/renew.png'), 'reload', self)

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        # 将按钮添加到导航栏上
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

# 创建应用
app = QApplication(sys.argv)
# 创建主窗口
window = MainWindow()
# 显示窗口
window.show()
# 运行应用，并监听事件
app.exec_()

