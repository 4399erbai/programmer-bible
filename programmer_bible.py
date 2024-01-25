# -*- coding: utf-8 -*-import random

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QSize, Qt
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu

from base.bible_util import number_generator, tips
from base import consts_util


class Bible(QMainWindow):  # 继承了QMainWindow类的方法和属性
    def __init__(self, parent=None):
        super(Bible, self).__init__(parent)
        self.setWindowIcon(QIcon(consts_util.IMAGES["logo"]))  # 加载log图片
        self.setupUi(self)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1034, 769)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # #滑动条
        # self.verticalScrollBar = QtWidgets.QScrollBar(self.frame)
        # self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        # self.verticalScrollBar.setObjectName("verticalScrollBar")
        # self.gridLayout.addWidget(self.verticalScrollBar, 0, 2, 2, 1)

        # 弹簧右边
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding)
        """width（宽度）：空白间隔的水平尺寸，以像素为单位。 height（高度）：空白间隔的垂直尺寸，以像素为单位。"""
        self.gridLayout.addItem(spacerItem, 0, 20)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 310, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.horizontalLayout.addWidget(self.frame)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(mainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(mainWindow)
        self.setButton()
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "程序员基础宝典"))
        self.label.setText(_translate("mainWindow", "题库"))
        # self.pushButton.setText(_translate("mainWindow", "添加"))
        self.menu.setTitle(_translate("mainWindow", "用户"))
        self.menu_2.setTitle(_translate("mainWindow", "关于"))
        self.action.setText(_translate("mainWindow", "登录"))
        self.action_2.setText(_translate("mainWindow", "注册"))
        self.action_3.setText(_translate("mainWindow", "注销"))



    def setButton(self):
        """用于设置添加按钮参数的"""
        _translate = QtCore.QCoreApplication.translate
        # 初始化默认值
        self.books = []  # 存储图书的列表
        self.buttons = []
        self.row_index = 0  # 当前行索引
        self.books_len = 9

        # 初增加按钮
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setFixedSize(100, 120)
        self.addButton.setIcon(QIcon(consts_util.IMAGES["add"])) #添加图片为add
        self.addButton.setIconSize(QSize(40, 40)) #设置图片的尺寸
        # self.addButton.setText('添加')
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.create_book)
        self.gridLayout.addWidget(self.addButton, self.row_index, 0)

        # 创建一个生成器对象
        self.generator = number_generator()

    def create_book(self, button=None):
        """创建并添加一个新的按钮到网格布局中"""
        # 初始化变量
        book_title = '书本' + str(next(self.generator) + 1)
        # 初始化添加按钮参数
        new_button = QPushButton(book_title)
        new_button.clicked.connect(lambda: tips(book_title))
        # 设置按钮的上下文菜单策略为CustomContextMenu,配合以下函数实现右键删除
        new_button.setContextMenuPolicy(Qt.CustomContextMenu)
        new_button.customContextMenuRequested.connect(lambda pos: self.show_custom_menu(new_button, pos))
        # 设置按钮的大小
        new_button.setFixedSize(100, 120)

        if not button:
            x = (len(self.buttons)) % self.books_len
            y = (len(self.buttons)) // self.books_len
            self.buttons.append(new_button)
            self.gridLayout.addWidget(new_button, y, x)
        else:
            x = self.buttons.index(button) % self.books_len
            y = self.buttons.index(button) // self.books_len
            self.gridLayout.addWidget(button, y, x)

        tips(f'数量：{len(self.buttons)},x：{y},y:{x}')
        # 当新增书本到9个，加号就添加到第二行了
        if x == self.books_len - 1:
            self.gridLayout.addWidget(self.addButton, y + 1, x - (self.books_len - 1))
        else:
            self.gridLayout.addWidget(self.addButton, y, x + 1)


    # 设置右键删除函数
    def show_custom_menu(self, button, pos):
        menu = QMenu()
        delete_action = menu.addAction("删除")
        action = menu.exec_(button.mapToGlobal(pos))
        if action == delete_action:
            # book_title = button.text()
            self.buttons.remove(button)
            button.setParent(None)  # 从父控件中移除
            button.deleteLater()   # 销毁按钮
            self.reset_view() # 重塑界面

    def reset_view(self):
        """
        当点击右键删除时，删除全部按钮，并重新添加
        """
        for but in self.buttons:
            but.setParent(None)
            self.create_book(but)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Bible()
    mainWindow.show()
    app.exec_()