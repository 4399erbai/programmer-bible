# -*- coding: utf-8 -*-
# @Author  : 陈新林
# @Time    : 2023/9/10 12:00
# @version    : 1.1
# @Update log ：第一版
import ctypes
import sys

import programmer_bible
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    MainWindow = QMainWindow()
    ui = programmer_bible.Bible()  # 更改这里类名
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# class  WkpMain(programmer_bible.Bible):
#     def __init__(self, parent=None):
#         super(WkpMain, self).__init__(parent)
#
#         print(4)
# if __name__ == "__main__":
#     # 设置默认编码格式为 UTF-8
#     # 设置默认编码格式为 UTF-8
#     QtCore.QTextCodec.setCodecForLocale(QtCore.QTextCodec.codecForName("UTF-8"))
#     cgitb.enable(format='text', logdir=consts.LOGDIR)
#
#
#     app = QApplication(sys.argv)
#     mainWindow = WkpMain()
#     mainWindow.showNormal()
#     mainWindow.show()
#
#     app.exec_()