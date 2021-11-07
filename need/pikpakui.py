# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pikpakui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(990, 721)
        Dialog.setStyleSheet("")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 10, 981, 701))
        self.widget.setStyleSheet("#widget {\n"
"    background-color: rgb(255,250,240);\n"
"\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 961, 681))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setEnabled(True)
        self.label_8.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("QLabel{\n"
"    color: rgb(131,179,249);\n"
"font: \'新宋体\';\n"
"font-weight:bold;\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.tohidepushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.tohidepushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.tohidepushButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(255,85,85,255),\n"
"                                      stop: 0.395 rgba(255,91,91,255),\n"
"                                      stop: 0.505 rgba(255,113,113,255), \n"
"                                      stop: 0.805 rgba(255,146,146,255), \n"
"\n"
"                                      stop: 1 rgba(255,162,162,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}")
        self.tohidepushButton.setObjectName("tohidepushButton")
        self.horizontalLayout_13.addWidget(self.tohidepushButton)
        self.exitapppushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.exitapppushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.exitapppushButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(255,85,85,255),\n"
"                                      stop: 0.395 rgba(255,91,91,255),\n"
"                                      stop: 0.505 rgba(255,113,113,255), \n"
"                                      stop: 0.805 rgba(255,146,146,255), \n"
"\n"
"                                      stop: 1 rgba(255,162,162,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}")
        self.exitapppushButton.setObjectName("exitapppushButton")
        self.horizontalLayout_13.addWidget(self.exitapppushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(650, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab{width:191;\n"
"border-top-color:#369;\n"
" background-color: rgb(255,250,240);\n"
"padding-bottom:5px;\n"
"padding-top:8px;\n"
"padding-bottom:10px;\n"
"font:14pt \'新宋体\'}\n"
"\n"
"QTabBar::tab::selected{\n"
"color:rgb(131,179,249);\n"
" background-color: rgb(255,250,240);\n"
"font:14pt \'新宋体\';\n"
"font-weight:bold;\n"
"border-bottom:5px solid #5AA4FA;\n"
"padding-top:8px;\n"
"padding-bottom:10px;\n"
"}\n"
"QTabWidget{\n"
"border-top-color:white;\n"
"background: white;\n"
"}\n"
"QWidget{\n"
" background-color: rgb(255,250,240);\n"
"}\n"
"\n"
"")
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setMinimumSize(QtCore.QSize(944, 0))
        self.tab.setMaximumSize(QtCore.QSize(944, 614))
        self.tab.setObjectName("tab")
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 951, 571))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 931, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.refreshButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.refreshButton.setFont(font)
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.refreshButton.setMouseTracking(False)
        self.refreshButton.setStyleSheet("QPushButton:!hover{\n"
"\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"\n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"\n"
"}")
        self.refreshButton.setObjectName("refreshButton")
        self.horizontalLayout_6.addWidget(self.refreshButton)
        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"}")
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_6.addWidget(self.backButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.uploadfileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.uploadfileButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"}")
        self.uploadfileButton.setObjectName("uploadfileButton")
        self.horizontalLayout_11.addWidget(self.uploadfileButton)
        self.addgcidButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addgcidButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"}")
        self.addgcidButton.setObjectName("addgcidButton")
        self.horizontalLayout_11.addWidget(self.addgcidButton)
        self.sharegcidButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sharegcidButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"}")
        self.sharegcidButton.setObjectName("sharegcidButton")
        self.horizontalLayout_11.addWidget(self.sharegcidButton)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"    background-color:rgb(255,250,240);\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 941, 601))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.offlinerefreshButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.offlinerefreshButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"}")
        self.offlinerefreshButton.setObjectName("offlinerefreshButton")
        self.horizontalLayout_10.addWidget(self.offlinerefreshButton)
        self.addmagnetButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addmagnetButton.sizePolicy().hasHeightForWidth())
        self.addmagnetButton.setSizePolicy(sizePolicy)
        self.addmagnetButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"}")
        self.addmagnetButton.setObjectName("addmagnetButton")
        self.horizontalLayout_10.addWidget(self.addmagnetButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.offlineWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.offlineWidget.setObjectName("offlineWidget")
        self.offlineWidget.setColumnCount(0)
        self.offlineWidget.setRowCount(0)
        self.verticalLayout_3.addWidget(self.offlineWidget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.downloadtableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.downloadtableWidget.setGeometry(QtCore.QRect(0, 10, 941, 601))
        self.downloadtableWidget.setObjectName("downloadtableWidget")
        self.downloadtableWidget.setColumnCount(0)
        self.downloadtableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 12, 931, 455))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout1Main = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layout1Main.setContentsMargins(0, 0, 0, 0)
        self.layout1Main.setSpacing(5)
        self.layout1Main.setObjectName("layout1Main")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.user_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.horizontalLayout.addWidget(self.user_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout.addWidget(self.password_lineEdit)
        self.checklogin_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.checklogin_Button.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 16pt \"微软雅黑\";\n"
"}")
        self.checklogin_Button.setObjectName("checklogin_Button")
        self.horizontalLayout.addWidget(self.checklogin_Button)
        self.layout1Main.addLayout(self.horizontalLayout)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.localdownloadlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.localdownloadlineEdit.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.localdownloadlineEdit.setFont(font)
        self.localdownloadlineEdit.setObjectName("localdownloadlineEdit")
        self.horizontalLayout_14.addWidget(self.localdownloadlineEdit)
        self.chooselocalButton = QtWidgets.QPushButton(self.layoutWidget)
        self.chooselocalButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 16pt \"微软雅黑\";\n"
"}")
        self.chooselocalButton.setObjectName("chooselocalButton")
        self.horizontalLayout_14.addWidget(self.chooselocalButton)
        self.layout1Main.addLayout(self.horizontalLayout_14)
        self.layout1T1 = QtWidgets.QHBoxLayout()
        self.layout1T1.setSpacing(5)
        self.layout1T1.setObjectName("layout1T1")
        self.Aria2_host = QtWidgets.QLabel(self.layoutWidget)
        self.Aria2_host.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Aria2_host.setFont(font)
        self.Aria2_host.setObjectName("Aria2_host")
        self.layout1T1.addWidget(self.Aria2_host)
        self.Aria2_hostlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.Aria2_hostlineEdit.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_hostlineEdit.setFont(font)
        self.Aria2_hostlineEdit.setInputMask("")
        self.Aria2_hostlineEdit.setPlaceholderText("http://ip")
        self.Aria2_hostlineEdit.setObjectName("Aria2_hostlineEdit")
        self.layout1T1.addWidget(self.Aria2_hostlineEdit)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.layout1T1.addWidget(self.label_4)
        self.Aria2_portlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_portlineEdit.setFont(font)
        self.Aria2_portlineEdit.setObjectName("Aria2_portlineEdit")
        self.layout1T1.addWidget(self.Aria2_portlineEdit)
        self.layout1Main.addLayout(self.layout1T1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.Aria2_secretlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_secretlineEdit.setFont(font)
        self.Aria2_secretlineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.Aria2_secretlineEdit.setObjectName("Aria2_secretlineEdit")
        self.horizontalLayout_3.addWidget(self.Aria2_secretlineEdit)
        self.layout1Main.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.Aria2_pathlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_pathlineEdit.setFont(font)
        self.Aria2_pathlineEdit.setObjectName("Aria2_pathlineEdit")
        self.horizontalLayout_2.addWidget(self.Aria2_pathlineEdit)
        self.checkaria2_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.checkaria2_Button.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}")
        self.checkaria2_Button.setObjectName("checkaria2_Button")
        self.horizontalLayout_2.addWidget(self.checkaria2_Button)
        self.layout1Main.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.Potplayer_pathlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Potplayer_pathlineEdit.setFont(font)
        self.Potplayer_pathlineEdit.setObjectName("Potplayer_pathlineEdit")
        self.horizontalLayout_8.addWidget(self.Potplayer_pathlineEdit)
        self.choosepotButton = QtWidgets.QPushButton(self.layoutWidget)
        self.choosepotButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}")
        self.choosepotButton.setObjectName("choosepotButton")
        self.horizontalLayout_8.addWidget(self.choosepotButton)
        self.layout1Main.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.IDMlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IDMlineEdit.setFont(font)
        self.IDMlineEdit.setObjectName("IDMlineEdit")
        self.horizontalLayout_7.addWidget(self.IDMlineEdit)
        self.chooseidmpushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.chooseidmpushButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}")
        self.chooseidmpushButton.setObjectName("chooseidmpushButton")
        self.horizontalLayout_7.addWidget(self.chooseidmpushButton)
        self.layout1Main.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.webdav_adminlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.webdav_adminlineEdit.setFont(font)
        self.webdav_adminlineEdit.setPlaceholderText("")
        self.webdav_adminlineEdit.setObjectName("webdav_adminlineEdit")
        self.horizontalLayout_12.addWidget(self.webdav_adminlineEdit)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.webdav_passlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.webdav_passlineEdit.setFont(font)
        self.webdav_passlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.webdav_passlineEdit.setObjectName("webdav_passlineEdit")
        self.horizontalLayout_12.addWidget(self.webdav_passlineEdit)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.webdav_portlineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.webdav_portlineEdit.setFont(font)
        self.webdav_portlineEdit.setObjectName("webdav_portlineEdit")
        self.horizontalLayout_12.addWidget(self.webdav_portlineEdit)
        self.change_webdav_pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.change_webdav_pushButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}")
        self.change_webdav_pushButton.setObjectName("change_webdav_pushButton")
        self.horizontalLayout_12.addWidget(self.change_webdav_pushButton)
        self.layout1Main.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveconfig_Button = QtWidgets.QPushButton(self.layoutWidget)
        self.saveconfig_Button.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 16pt \"微软雅黑\";\n"
"}")
        self.saveconfig_Button.setObjectName("saveconfig_Button")
        self.horizontalLayout_4.addWidget(self.saveconfig_Button)
        self.layout1Main.addLayout(self.horizontalLayout_4)
        self.layout1Main.setStretch(2, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 931, 551))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setEnabled(True)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.visitmeButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.visitmeButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"}")
        self.visitmeButton.setObjectName("visitmeButton")
        self.horizontalLayout_5.addWidget(self.visitmeButton)
        self.visitpikpakButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.visitpikpakButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(131,179,249,255),\n"
"                                      stop: 0.495 rgba(131,179,249,255),\n"
"                                      stop: 0.505 rgba(131,179,249,255), \n"
"                                      stop: 0.805 rgba(92,208,245,255), \n"
"\n"
"                                      stop: 1 rgba(77,218,244,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    \n"
"    background-color: rgb(131,179,249);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"}")
        self.visitpikpakButton.setObjectName("visitpikpakButton")
        self.horizontalLayout_5.addWidget(self.visitpikpakButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_5.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PikPakDown"))
        self.label_8.setText(_translate("Dialog", " PikPakDown V1.1"))
        self.tohidepushButton.setText(_translate("Dialog", "-"))
        self.exitapppushButton.setText(_translate("Dialog", "X"))
        self.refreshButton.setText(_translate("Dialog", "刷新列表"))
        self.backButton.setText(_translate("Dialog", "上级目录"))
        self.uploadfileButton.setText(_translate("Dialog", "上传文件"))
        self.addgcidButton.setText(_translate("Dialog", "导入秒链"))
        self.sharegcidButton.setText(_translate("Dialog", "导出当前秒链"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "主页"))
        self.offlinerefreshButton.setText(_translate("Dialog", "刷新列表"))
        self.addmagnetButton.setText(_translate("Dialog", "添加离线任务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "离线下载"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "任务列表"))
        self.label.setText(_translate("Dialog", " 账号 "))
        self.label_2.setText(_translate("Dialog", " 密码 "))
        self.checklogin_Button.setText(_translate("Dialog", "检查登录"))
        self.label_9.setText(_translate("Dialog", "本地下载路径"))
        self.localdownloadlineEdit.setPlaceholderText(_translate("Dialog", "不设置则默认在程序目录下载文件夹"))
        self.chooselocalButton.setText(_translate("Dialog", "选择路径"))
        self.Aria2_host.setText(_translate("Dialog", " Aria2地址 "))
        self.label_4.setText(_translate("Dialog", " 端口 "))
        self.label_3.setText(_translate("Dialog", " Aria2密钥 "))
        self.label_5.setText(_translate("Dialog", " Aria2下载路径"))
        self.Aria2_pathlineEdit.setPlaceholderText(_translate("Dialog", "设置为跟Aria2下载路径一致"))
        self.checkaria2_Button.setText(_translate("Dialog", "检查Aria2连接性"))
        self.label_6.setText(_translate("Dialog", " Potplayer路径 "))
        self.choosepotButton.setText(_translate("Dialog", "选择路径"))
        self.label_7.setText(_translate("Dialog", " IDM路径 "))
        self.chooseidmpushButton.setText(_translate("Dialog", "选择路径"))
        self.label_10.setText(_translate("Dialog", "Webdav:"))
        self.label_13.setText(_translate("Dialog", "用户名"))
        self.label_12.setText(_translate("Dialog", "密码"))
        self.label_11.setText(_translate("Dialog", "端口"))
        self.change_webdav_pushButton.setText(_translate("Dialog", "开启Webdav"))
        self.saveconfig_Button.setText(_translate("Dialog", "保存配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "设置"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">本工具为Pikapk的第三方工具。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">官方群组：https://t.me/pikpak_userservice</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">目前实现:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">- 推送迅雷</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">- 推送IDM</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">- 推送Potplayer</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">- 推送Aria2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">- 多选文件推送(不支持文件夹)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">- 单个文件夹整体推送</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:14pt;\">Bug反馈:https://t.me/Ben_chao</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:14pt;\"><br /></p></body></html>"))
        self.visitmeButton.setText(_translate("Dialog", "访问作者博客"))
        self.visitpikpakButton.setText(_translate("Dialog", "加入官方群"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "关于"))
import res_rc
