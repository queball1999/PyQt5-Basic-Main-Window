#
#   Program: PyQt5 Basic Main Window
#
#   Software: Microsoft Visual Studios 16.8.3
#
#   GUI: PyQt5
#
#   Date: 10th of July 2021
#
#   Author: Quynn Bell
#

# importing operating system libraries
import os
#importing Sysytem-specefic parameters and functions
import sys
# importing regular expressions library
import re
# importing PyQt5 GUI
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

# define Main class and insert QMainWindow into the class
# this class can be named whatever you like, but you must insert QMainWindow to get the Main Window functionality of this window
# for all other sub-window, you will use something like QWidget insead of QMainWindow; there can only be one Main Window
class Main(QMainWindow):

    def __init__(self):
         # setting up window parameters
        super().__init__()

        self.title = '[Enter Title Here]'
        screen = app.primaryScreen()
        size = screen.size()
        self.width = size.width()
        self.height = size.height()
        self.left = (self.width / 2) - (self.width / 4)
        self.top = (self.height / 2) - (self.height / 4)


        self.css_dark = """
        QMainWindow { background-color : #202020; color : white; }
        QWidget { background-color : #202020; border : None; }
        QMenuBar { background-color : #383838; color : white; font-family : Arial, sans-serif; font-size : 12; }
        QMenuBar::item { background-color : #383838; color : white; font-family : Arial, sans-serif; font-size : 12; }
        QMenuBar::item:selected { background-color : #202020; color : white; }
        QMenuBar::item:pressed { background-color : #202020; color : white; }
        QMenu {  background-color : #383838; color : white; font-family : Arial, sans-serif; font-size : 12; }
        QMenu::item { background-color : #383838; color : white; }
        QMenu::item:selected { background-color : #2d2d30; color : white; }
        QMenu::item:pressed { background-color : #2d2d30; color : white; }
        QToolBar { background-color : #383838; color : white; }
        QToolButton { background-color : #383838; color : white; font-family : Arial, sans-serif; font-size : 12; }
        QToolButton::pressed { background-color : #202020; color : white; }
        QLabel { background-color : #202020; color : white; font-family : Arial, sans-serif; font-weight : bold; font-size : 18; }
        QLineEdit { background-color : #2d2d30; color : white; border-color : white; border-width : 1px; border-style : solid; padding : 4px 4px 4px 4px; font-family : Arial, sans-serif; font-weight : bold; font-size : 18; }
        QListWidget { background-color : #2d2d30; color : white; border-color : white; border-width : 1px; border-style : solid; padding : 10px 10px; font-family : Arial, sans-serif; font-weight : bold; font-size : 18; }
        QPushButton { background-color : #2d2d30; color : white; border-color : white; border-width : 1px; border-style : solid; padding : 4px 10px 4px 10px; font-family : Arial, sans-serif; font-weight : bold; font-size : 18; }
        QPushButton:hover {background-color : #202020; color : white; border-color : white; border-width : 1px; border-style : solid; padding : 4px 10px 4px 10px; }
        QPushButton:pressed {background-color : #2d2d30; color : white; border-color : white; border-width : 1px; border-style : solid; padding : 4px 10px 4px 10px; }
        QProgressBar { color : white; background-color : #202020; border : 1px}
        QScrollArea { background-color : #202020; border-color : white; border-width : 1px; border-style : solid; padding-top : 10px; padding-bottom : 10px; }
        QScrollBar::vertical { background-color : #202020; width : 15px; margin: 15px 3px 15px 3px; border : 1px transparent #202020; border-radius : 4px;  }
        QScrollBar::handle:vertical { background-color : #005dac; border-radius: 4px; }
        QScrollBar::sub-line:vertical { height : 0px }
        QScrollBar::add-line:vertical { height : 0px }
        QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background : none; }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background : none; height : 0px }
        QStatusBar { background-color : #383838; color : white; font-family : Arial, sans-serif; font-weight : bold; font-size : 18;}
        QTabWidget::pane { background-color : #383838; color : white; }
        QTabBar::tab { background-color : #383838; color : white; min-width : 35ex; padding : 4px 10px 4px 10px; font-family : Arial, sans-serif; font-weight : bold; font-size : 18; }
        QTabBar::tab:hover { background-color : #2d2d30; color : white; }
        QTabBar::tab:selected { border-color : #005dac; border-width : 1px; border-style : solid; }
        QTabBar::close-button { image : url(photos/close_button.png); }
        QTextEdit { background-color : #2d2d30; color : white; border-color : white; border-width : 1px; border-style : solid; padding : 4px 4px 4px 4px; font-family : Arial, sans-serif; font-weight : bold; font-size : 18; }
        """
        self.setStyleSheet(self.css_dark)
        self.setFont(QFont('Arial', 10))
        self.labels()

    def labels(self):
        # declaring grid layout for widget organization
        widget = QWidget()
        gridLayout = QGridLayout()

        # labels, buttons, and entry fields
        self.testLabel = QLabel('test')

        #gridLayout.addWidget(self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
        gridLayout.addWidget(self.testLabel, 0, 0, 1, 1)
        
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage('StatusBar')
        widget.setLayout(gridLayout)

        self.initUI()

    def closeEvent(self, event):
        pass

    def initUI(self):
        #self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title) 
        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except:
            self.setGeometry(self.left, self.top, self.width / 2, self.height / 2)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
