# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yang.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1351, 786)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setAcceptDrops(True)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_widget = QtWidgets.QWidget(Form)
        self.main_widget.setAcceptDrops(True)
        self.main_widget.setStyleSheet("QWidget#main_widget{\n"
"    background-color: rgb(252,252,255);\n"
"border-radius:15px;\n"
"border:4px solid #BEBEBE;\n"
"}\n"
"QWidget{\n"
"    background-color: rgb(252,252,255);\n"
"}\n"
"QWidget!hover{\n"
"    background-color: rgb(252,252,255);\n"
"}")
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.titlewidget = QtWidgets.QWidget(self.main_widget)
        self.titlewidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.titlewidget.setStyleSheet("QWidget#titlewidget{\n"
"border-bottom:6px ridge #E0E0E0;\n"
"}\n"
"")
        self.titlewidget.setObjectName("titlewidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titlewidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titlelabel = QtWidgets.QLabel(self.titlewidget)
        self.titlelabel.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.titlelabel.setFont(font)
        self.titlelabel.setObjectName("titlelabel")
        self.horizontalLayout.addWidget(self.titlelabel)
        self.pingtitlelabel = QtWidgets.QLabel(self.titlewidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pingtitlelabel.sizePolicy().hasHeightForWidth())
        self.pingtitlelabel.setSizePolicy(sizePolicy)
        self.pingtitlelabel.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pingtitlelabel.setFont(font)
        self.pingtitlelabel.setObjectName("pingtitlelabel")
        self.horizontalLayout.addWidget(self.pingtitlelabel)
        self.pinginfo_label = QtWidgets.QLabel(self.titlewidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pinginfo_label.setFont(font)
        self.pinginfo_label.setObjectName("pinginfo_label")
        self.horizontalLayout.addWidget(self.pinginfo_label)
        self.tohidepushButton = QtWidgets.QPushButton(self.titlewidget)
        self.tohidepushButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tohidepushButton.setFont(font)
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
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"}")
        self.tohidepushButton.setObjectName("tohidepushButton")
        self.horizontalLayout.addWidget(self.tohidepushButton)
        self.pushMaxButton = QtWidgets.QPushButton(self.titlewidget)
        self.pushMaxButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushMaxButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushMaxButton.setStyleSheet("QPushButton:!hover{\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,  \n"
"                                      stop: 0 rgba(255,85,85,255),\n"
"                                      stop: 0.395 rgba(255,91,91,255),\n"
"                                      stop: 0.505 rgba(255,113,113,255), \n"
"                                      stop: 0.805 rgba(255,146,146,255), \n"
"\n"
"                                      stop: 1 rgba(255,162,162,255));\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 12pt ;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 13pt ;\n"
"border-radius:8px;\n"
"}")
        self.pushMaxButton.setObjectName("pushMaxButton")
        self.horizontalLayout.addWidget(self.pushMaxButton)
        self.exitapppushButton = QtWidgets.QPushButton(self.titlewidget)
        self.exitapppushButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.exitapppushButton.setFont(font)
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
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 15pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"}")
        self.exitapppushButton.setObjectName("exitapppushButton")
        self.horizontalLayout.addWidget(self.exitapppushButton)
        self.verticalLayout_8.addWidget(self.titlewidget)
        self.widget_2 = QtWidgets.QWidget(self.main_widget)
        self.widget_2.setAcceptDrops(True)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_2)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
"padding:5px 15px 5px 5px;\n"
"width:80;\n"
"height:40;\n"
"border-top-color:#369;\n"
"font: 75 10pt \"微软雅黑\";\n"
"\n"
"}\n"
"QTabBar::tab::selected{\n"
"color:rgb(223,86,89);\n"
"padding:5px 15px 5px 5px;\n"
"width:80;\n"
"height:40;\n"
"font: 75 10pt \"微软雅黑\";\n"
"border-bottom:3px solid rgb(223,86,89);\n"
"}\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAcceptDrops(True)
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMaximumSize(QtCore.QSize(450, 16777215))
        self.widget_4.setAcceptDrops(True)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.filetreeWidget = QtWidgets.QTreeWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filetreeWidget.sizePolicy().hasHeightForWidth())
        self.filetreeWidget.setSizePolicy(sizePolicy)
        self.filetreeWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.filetreeWidget.setMaximumSize(QtCore.QSize(450, 16777215))
        self.filetreeWidget.setStyleSheet("/*QScrollBar Style*/\n"
"\n"
"/*纵向滚动条*/\n"
"QScrollBar:vertical {\n"
"    background: transparent; /*背景透明*/\n"
"    width: 10px; /*宽度*/\n"
"    margin: 0px 0px 0px 0px; /**/\n"
"    padding-top: 12px; /*距离上面12px*/\n"
"    padding-bottom: 12px; /*距离底部12px*/\n"
"}\n"
"/*横向滚动条*/\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px; /*高度*/\n"
"    margin: 0px 0px 0px 0px;\n"
"    padding-left: 12px; /*距离左边12px*/\n"
"    padding-right: 12px; /*距离右边12px*/\n"
"}\n"
"\n"
"/*当鼠标放到纵向或者横向滚动条上面时*/\n"
"QScrollBar:vertical:hover,QScrollBar:horizontal:hover {\n"
"    background: rgba(0, 0, 0, 30); /*修改背景透明度 30*/\n"
"    border-radius: 5px; /*圆角*/\n"
"}\n"
"\n"
"/*纵向滚动条上面的滑块*/\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(131,179,249);\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"/*横向滚动条上面的滑块*/\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(0, 0, 0, 50);\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/*当鼠标放到滚动条滑块上面时改变透明度实现颜色的深浅变化*/\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover {\n"
"    background: #6A6AFF;\n"
"}\n"
"\n"
"/*纵向滚动条下部分块*/\n"
"QScrollBar::add-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*横向滚动条后面部分块*/\n"
"QScrollBar::add-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*纵向滚动条上面部分块*/\n"
"QScrollBar::sub-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*横向滚动条左部分块*/\n"
"QScrollBar::sub-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*纵向滚动条顶部三角形位置*/\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: top;\n"
"}\n"
"/*横向滚动条左侧三角形位置*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"/*纵向滚动条下面三角形部分*/\n"
"QScrollBar::add-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: bottom;\n"
"}\n"
"/*横向滚动条右边的三角形部分*/\n"
"QScrollBar::add-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: right;\n"
"}\n"
"")
        self.filetreeWidget.setObjectName("filetreeWidget")
        self.filetreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.filetreeWidget)
        self.widget_12 = QtWidgets.QWidget(self.widget_4)
        self.widget_12.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_12.setMaximumSize(QtCore.QSize(450, 16777215))
        self.widget_12.setStyleSheet(".QWidget {\n"
"border:1px solid #B9B9FF;\n"
"border-radius:4px;\n"
"}")
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_12)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.refresh_vip_pushButton = QtWidgets.QPushButton(self.widget_12)
        self.refresh_vip_pushButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid #B9B9FF;\n"
"    color: #B9B9FF;\n"
"    font: 75 8pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid #B9B9FF;\n"
"    background-color:#B9B9FF;\n"
"    color: blue;\n"
"    font: 75 8pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.refresh_vip_pushButton.setObjectName("refresh_vip_pushButton")
        self.gridLayout_9.addWidget(self.refresh_vip_pushButton, 2, 2, 1, 1)
        self.quate_progressBar = QtWidgets.QProgressBar(self.widget_12)
        self.quate_progressBar.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.quate_progressBar.setFont(font)
        self.quate_progressBar.setStyleSheet("QProgressBar::chunk {   \n"
" background-color:rgb(58, 154, 255);\n"
"border-radius:4px;\n"
"}\n"
"QProgressBar {   \n"
"border:1px solid #B9B9FF;\n"
"      background:white;\n"
"      text-align:center;   /*文本的位置*/\n"
"      color: black;  /*文本颜色*/\n"
"border-radius:10px;\n"
"}")
        self.quate_progressBar.setProperty("value", 0)
        self.quate_progressBar.setObjectName("quate_progressBar")
        self.gridLayout_9.addWidget(self.quate_progressBar, 0, 1, 1, 2)
        self.quota_label = QtWidgets.QLabel(self.widget_12)
        self.quota_label.setMinimumSize(QtCore.QSize(200, 0))
        self.quota_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.quota_label.setFont(font)
        self.quota_label.setObjectName("quota_label")
        self.gridLayout_9.addWidget(self.quota_label, 0, 0, 1, 1)
        self.vip_time_label = QtWidgets.QLabel(self.widget_12)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.vip_time_label.setFont(font)
        self.vip_time_label.setObjectName("vip_time_label")
        self.gridLayout_9.addWidget(self.vip_time_label, 2, 0, 1, 2)
        self.verticalLayout_3.addWidget(self.widget_12)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.widget = QtWidgets.QWidget(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(800, 0))
        self.widget.setAcceptDrops(True)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.root_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.root_label.sizePolicy().hasHeightForWidth())
        self.root_label.setSizePolicy(sizePolicy)
        self.root_label.setMaximumSize(QtCore.QSize(760, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.root_label.setFont(font)
        self.root_label.setObjectName("root_label")
        self.verticalLayout_2.addWidget(self.root_label)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.sharegcidButton = QtWidgets.QPushButton(self.widget_3)
        self.sharegcidButton.setStyleSheet("")
        self.sharegcidButton.setObjectName("sharegcidButton")
        self.gridLayout_8.addWidget(self.sharegcidButton, 0, 3, 1, 1)
        self.refreshButton = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.refreshButton.setFont(font)
        self.refreshButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.refreshButton.setMouseTracking(False)
        self.refreshButton.setStyleSheet("")
        self.refreshButton.setObjectName("refreshButton")
        self.gridLayout_8.addWidget(self.refreshButton, 0, 0, 1, 1)
        self.uploadfileButton = QtWidgets.QPushButton(self.widget_3)
        self.uploadfileButton.setStyleSheet("")
        self.uploadfileButton.setObjectName("uploadfileButton")
        self.gridLayout_8.addWidget(self.uploadfileButton, 0, 4, 1, 1)
        self.addgcidButton = QtWidgets.QPushButton(self.widget_3)
        self.addgcidButton.setStyleSheet("")
        self.addgcidButton.setObjectName("addgcidButton")
        self.gridLayout_8.addWidget(self.addgcidButton, 0, 2, 1, 1)
        self.delete_file_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.delete_file_pushButton.setObjectName("delete_file_pushButton")
        self.gridLayout_8.addWidget(self.delete_file_pushButton, 1, 3, 1, 1)
        self.copy_file_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.copy_file_pushButton.setStyleSheet("")
        self.copy_file_pushButton.setObjectName("copy_file_pushButton")
        self.gridLayout_8.addWidget(self.copy_file_pushButton, 1, 2, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.widget_3)
        self.backButton.setStyleSheet("")
        self.backButton.setObjectName("backButton")
        self.gridLayout_8.addWidget(self.backButton, 0, 1, 1, 1)
        self.move_file_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.move_file_pushButton.setStyleSheet("")
        self.move_file_pushButton.setObjectName("move_file_pushButton")
        self.gridLayout_8.addWidget(self.move_file_pushButton, 1, 1, 1, 1)
        self.creat_folder_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.creat_folder_pushButton.setStyleSheet("")
        self.creat_folder_pushButton.setObjectName("creat_folder_pushButton")
        self.gridLayout_8.addWidget(self.creat_folder_pushButton, 0, 5, 1, 1)
        self.rename_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.rename_pushButton.setObjectName("rename_pushButton")
        self.gridLayout_8.addWidget(self.rename_pushButton, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_3.addWidget(self.widget)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.tab_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.offlinerefreshButton = QtWidgets.QPushButton(self.widget_5)
        self.offlinerefreshButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.offlinerefreshButton.setObjectName("offlinerefreshButton")
        self.horizontalLayout_5.addWidget(self.offlinerefreshButton)
        self.addmagnetButton = QtWidgets.QPushButton(self.widget_5)
        self.addmagnetButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.addmagnetButton.setObjectName("addmagnetButton")
        self.horizontalLayout_5.addWidget(self.addmagnetButton)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.offlineWidget = QtWidgets.QTableWidget(self.tab_2)
        self.offlineWidget.setObjectName("offlineWidget")
        self.offlineWidget.setColumnCount(0)
        self.offlineWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.offlineWidget)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_11 = QtWidgets.QWidget(self.tab_7)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_11.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.refresh_trash_pushButton = QtWidgets.QPushButton(self.widget_11)
        self.refresh_trash_pushButton.setObjectName("refresh_trash_pushButton")
        self.horizontalLayout_6.addWidget(self.refresh_trash_pushButton)
        self.back_trash_pushButton = QtWidgets.QPushButton(self.widget_11)
        self.back_trash_pushButton.setObjectName("back_trash_pushButton")
        self.horizontalLayout_6.addWidget(self.back_trash_pushButton)
        self.delete_trahs_pushButton = QtWidgets.QPushButton(self.widget_11)
        self.delete_trahs_pushButton.setObjectName("delete_trahs_pushButton")
        self.horizontalLayout_6.addWidget(self.delete_trahs_pushButton)
        self.verticalLayout_11.addWidget(self.widget_11)
        self.trash_tableWidget = QtWidgets.QTableWidget(self.tab_7)
        self.trash_tableWidget.setObjectName("trash_tableWidget")
        self.trash_tableWidget.setColumnCount(0)
        self.trash_tableWidget.setRowCount(0)
        self.verticalLayout_11.addWidget(self.trash_tableWidget)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.upload_tabWidget = QtWidgets.QTabWidget(self.tab_3)
        self.upload_tabWidget.setStyleSheet("QTabBar::tab{\n"
"\n"
"width:200;\n"
"height:40;\n"
"border-top-color:#369;\n"
"font: 75 10pt \"微软雅黑\";\n"
"\n"
"}\n"
"QTabBar::tab::selected{\n"
"\n"
"width:200;\n"
"height:40;\n"
"font: 75 10pt \"微软雅黑\";\n"
"border-bottom:3px solid rgb(223,86,89);\n"
"}\n"
"\n"
"            ")
        self.upload_tabWidget.setObjectName("upload_tabWidget")
        self.tab_upload_now = QtWidgets.QWidget()
        self.tab_upload_now.setObjectName("tab_upload_now")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_upload_now)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.upload_now_dtableWidget = QtWidgets.QTableWidget(self.tab_upload_now)
        self.upload_now_dtableWidget.setObjectName("upload_now_dtableWidget")
        self.upload_now_dtableWidget.setColumnCount(0)
        self.upload_now_dtableWidget.setRowCount(0)
        self.verticalLayout_14.addWidget(self.upload_now_dtableWidget)
        self.upload_tabWidget.addTab(self.tab_upload_now, "")
        self.tab_upload_wait = QtWidgets.QWidget()
        self.tab_upload_wait.setObjectName("tab_upload_wait")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_upload_wait)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.upload_wait_dtableWidget = QtWidgets.QTableWidget(self.tab_upload_wait)
        self.upload_wait_dtableWidget.setObjectName("upload_wait_dtableWidget")
        self.upload_wait_dtableWidget.setColumnCount(0)
        self.upload_wait_dtableWidget.setRowCount(0)
        self.verticalLayout_15.addWidget(self.upload_wait_dtableWidget)
        self.upload_tabWidget.addTab(self.tab_upload_wait, "")
        self.tab_upload_finish = QtWidgets.QWidget()
        self.tab_upload_finish.setObjectName("tab_upload_finish")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_upload_finish)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.upload_finish_dtableWidget = QtWidgets.QTableWidget(self.tab_upload_finish)
        self.upload_finish_dtableWidget.setObjectName("upload_finish_dtableWidget")
        self.upload_finish_dtableWidget.setColumnCount(0)
        self.upload_finish_dtableWidget.setRowCount(0)
        self.verticalLayout_16.addWidget(self.upload_finish_dtableWidget)
        self.upload_tabWidget.addTab(self.tab_upload_finish, "")
        self.verticalLayout_5.addWidget(self.upload_tabWidget)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.download_tabWidget = QtWidgets.QTabWidget(self.tab_8)
        self.download_tabWidget.setStyleSheet("QTabBar::tab{\n"
"\n"
"width:200;\n"
"height:40;\n"
"border-top-color:#369;\n"
"font: 75 10pt \"微软雅黑\";\n"
"\n"
"}\n"
"QTabBar::tab::selected{\n"
"\n"
"width:200;\n"
"height:40;\n"
"font: 75 10pt \"微软雅黑\";\n"
"border-bottom:3px solid rgb(223,86,89);\n"
"}\n"
"\n"
"")
        self.download_tabWidget.setObjectName("download_tabWidget")
        self.tab_download_now = QtWidgets.QWidget()
        self.tab_download_now.setObjectName("tab_download_now")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_download_now)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.download_now_dtableWidget = QtWidgets.QTableWidget(self.tab_download_now)
        self.download_now_dtableWidget.setObjectName("download_now_dtableWidget")
        self.download_now_dtableWidget.setColumnCount(0)
        self.download_now_dtableWidget.setRowCount(0)
        self.verticalLayout_13.addWidget(self.download_now_dtableWidget)
        self.download_tabWidget.addTab(self.tab_download_now, "")
        self.tab_download_wait = QtWidgets.QWidget()
        self.tab_download_wait.setObjectName("tab_download_wait")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_download_wait)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.download_wait_dtableWidget = QtWidgets.QTableWidget(self.tab_download_wait)
        self.download_wait_dtableWidget.setObjectName("download_wait_dtableWidget")
        self.download_wait_dtableWidget.setColumnCount(0)
        self.download_wait_dtableWidget.setRowCount(0)
        self.verticalLayout_17.addWidget(self.download_wait_dtableWidget)
        self.download_tabWidget.addTab(self.tab_download_wait, "")
        self.tab_download_finish = QtWidgets.QWidget()
        self.tab_download_finish.setObjectName("tab_download_finish")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.tab_download_finish)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.download_finish_dtableWidget = QtWidgets.QTableWidget(self.tab_download_finish)
        self.download_finish_dtableWidget.setObjectName("download_finish_dtableWidget")
        self.download_finish_dtableWidget.setColumnCount(0)
        self.download_finish_dtableWidget.setRowCount(0)
        self.verticalLayout_18.addWidget(self.download_finish_dtableWidget)
        self.download_tabWidget.addTab(self.tab_download_finish, "")
        self.verticalLayout_12.addWidget(self.download_tabWidget)
        self.widget_13 = QtWidgets.QWidget(self.tab_8)
        self.widget_13.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_13.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.start_alldown_pushButton = QtWidgets.QPushButton(self.widget_13)
        self.start_alldown_pushButton.setObjectName("start_alldown_pushButton")
        self.horizontalLayout_7.addWidget(self.start_alldown_pushButton)
        self.stop_alldown_pushButton = QtWidgets.QPushButton(self.widget_13)
        self.stop_alldown_pushButton.setObjectName("stop_alldown_pushButton")
        self.horizontalLayout_7.addWidget(self.stop_alldown_pushButton)
        self.open_aria2ng_pushButton = QtWidgets.QPushButton(self.widget_13)
        self.open_aria2ng_pushButton.setObjectName("open_aria2ng_pushButton")
        self.horizontalLayout_7.addWidget(self.open_aria2ng_pushButton)
        self.verticalLayout_12.addWidget(self.widget_13)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea.setStyleSheet("/*QScrollBar Style*/\n"
"\n"
"/*纵向滚动条*/\n"
"QScrollBar:vertical {\n"
"    background: transparent; /*背景透明*/\n"
"    width: 10px; /*宽度*/\n"
"    margin: 0px 0px 0px 0px; /**/\n"
"    padding-top: 12px; /*距离上面12px*/\n"
"    padding-bottom: 12px; /*距离底部12px*/\n"
"}\n"
"/*横向滚动条*/\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px; /*高度*/\n"
"    margin: 0px 0px 0px 0px;\n"
"    padding-left: 12px; /*距离左边12px*/\n"
"    padding-right: 12px; /*距离右边12px*/\n"
"}\n"
"\n"
"/*当鼠标放到纵向或者横向滚动条上面时*/\n"
"QScrollBar:vertical:hover,QScrollBar:horizontal:hover {\n"
"    background: rgba(0, 0, 0, 30); /*修改背景透明度 30*/\n"
"    border-radius: 5px; /*圆角*/\n"
"}\n"
"\n"
"/*纵向滚动条上面的滑块*/\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(131,179,249);\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"/*横向滚动条上面的滑块*/\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(0, 0, 0, 50);\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/*当鼠标放到滚动条滑块上面时改变透明度实现颜色的深浅变化*/\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover {\n"
"    background: #6A6AFF;\n"
"}\n"
"\n"
"/*纵向滚动条下部分块*/\n"
"QScrollBar::add-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*横向滚动条后面部分块*/\n"
"QScrollBar::add-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*纵向滚动条上面部分块*/\n"
"QScrollBar::sub-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*横向滚动条左部分块*/\n"
"QScrollBar::sub-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*纵向滚动条顶部三角形位置*/\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: top;\n"
"}\n"
"/*横向滚动条左侧三角形位置*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"/*纵向滚动条下面三角形部分*/\n"
"QScrollBar::add-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: bottom;\n"
"}\n"
"/*横向滚动条右边的三角形部分*/\n"
"QScrollBar::add-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: right;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.configscrollAreaWidgetContents = QtWidgets.QWidget()
        self.configscrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1245, 1068))
        self.configscrollAreaWidgetContents.setObjectName("configscrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.configscrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget1 = QtWidgets.QWidget(self.configscrollAreaWidgetContents)
        self.widget1.setStyleSheet(".QWidget{\n"
"border:3px ridge #E0E0E0;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    padding:5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}\n"
"")
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setMinimumSize(QtCore.QSize(150, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.user_lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.user_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.user_lineEdit.setFont(font)
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.gridLayout.addWidget(self.user_lineEdit, 1, 2, 1, 1)
        self.clear_headers_pushButton = QtWidgets.QPushButton(self.widget1)
        self.clear_headers_pushButton.setStyleSheet("")
        self.clear_headers_pushButton.setObjectName("clear_headers_pushButton")
        self.gridLayout.addWidget(self.clear_headers_pushButton, 2, 3, 1, 1)
        self.checklogin_Button = QtWidgets.QPushButton(self.widget1)
        self.checklogin_Button.setStyleSheet("")
        self.checklogin_Button.setObjectName("checklogin_Button")
        self.gridLayout.addWidget(self.checklogin_Button, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 4)
        self.pushvipcode_Button = QtWidgets.QPushButton(self.widget1)
        self.pushvipcode_Button.setStyleSheet("")
        self.pushvipcode_Button.setObjectName("pushvipcode_Button")
        self.gridLayout.addWidget(self.pushvipcode_Button, 3, 3, 1, 1)
        self.vipcode_lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.vipcode_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.vipcode_lineEdit.setFont(font)
        self.vipcode_lineEdit.setObjectName("vipcode_lineEdit")
        self.gridLayout.addWidget(self.vipcode_lineEdit, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.register_Button = QtWidgets.QPushButton(self.widget1)
        self.register_Button.setStyleSheet("")
        self.register_Button.setObjectName("register_Button")
        self.gridLayout.addWidget(self.register_Button, 1, 4, 1, 1)
        self.password_lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.password_lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout.addWidget(self.password_lineEdit, 2, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setMaximumSize(QtCore.QSize(150, 150))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/pic/src/pikpak.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 4, 1)
        self.label_27 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 3, 1, 1, 1)
        self.phonelogin_Button = QtWidgets.QPushButton(self.widget1)
        self.phonelogin_Button.setObjectName("phonelogin_Button")
        self.gridLayout.addWidget(self.phonelogin_Button, 2, 4, 1, 1)
        self.verticalLayout_9.addWidget(self.widget1)
        self.widget_21 = QtWidgets.QWidget(self.configscrollAreaWidgetContents)
        self.widget_21.setStyleSheet(".QWidget{\n"
"border:3px ridge #E0E0E0;\n"
"border-radius:15px;\n"
"}\n"
"")
        self.widget_21.setObjectName("widget_21")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_21)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.widget_21)
        self.label_9.setMinimumSize(QtCore.QSize(250, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.chooselocalButton = QtWidgets.QPushButton(self.widget_21)
        self.chooselocalButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    padding:5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.chooselocalButton.setObjectName("chooselocalButton")
        self.gridLayout_2.addWidget(self.chooselocalButton, 1, 2, 1, 1)
        self.localdownloadlineEdit = QtWidgets.QLineEdit(self.widget_21)
        self.localdownloadlineEdit.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.localdownloadlineEdit.setFont(font)
        self.localdownloadlineEdit.setObjectName("localdownloadlineEdit")
        self.gridLayout_2.addWidget(self.localdownloadlineEdit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_21)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 3)
        self.verticalLayout_9.addWidget(self.widget_21)
        self.widget_31 = QtWidgets.QWidget(self.configscrollAreaWidgetContents)
        self.widget_31.setStyleSheet(".QWidget{\n"
"border:3px ridge #E0E0E0;\n"
"border-radius:15px;\n"
"}\n"
"")
        self.widget_31.setObjectName("widget_31")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_31)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Aria2_host = QtWidgets.QLabel(self.widget_31)
        self.Aria2_host.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_host.setFont(font)
        self.Aria2_host.setAlignment(QtCore.Qt.AlignCenter)
        self.Aria2_host.setObjectName("Aria2_host")
        self.gridLayout_3.addWidget(self.Aria2_host, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_31)
        self.label_3.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 1, 1, 1)
        self.Aria2_hostlineEdit = QtWidgets.QLineEdit(self.widget_31)
        self.Aria2_hostlineEdit.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_hostlineEdit.setFont(font)
        self.Aria2_hostlineEdit.setInputMask("")
        self.Aria2_hostlineEdit.setPlaceholderText("http://ip")
        self.Aria2_hostlineEdit.setObjectName("Aria2_hostlineEdit")
        self.gridLayout_3.addWidget(self.Aria2_hostlineEdit, 1, 2, 1, 1)
        self.checkaria2_Button = QtWidgets.QPushButton(self.widget_31)
        self.checkaria2_Button.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    padding:5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.checkaria2_Button.setObjectName("checkaria2_Button")
        self.gridLayout_3.addWidget(self.checkaria2_Button, 3, 4, 1, 1)
        self.Aria2_secretlineEdit = QtWidgets.QLineEdit(self.widget_31)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_secretlineEdit.setFont(font)
        self.Aria2_secretlineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.Aria2_secretlineEdit.setObjectName("Aria2_secretlineEdit")
        self.gridLayout_3.addWidget(self.Aria2_secretlineEdit, 2, 2, 1, 1)
        self.Aria2_pathlineEdit = QtWidgets.QLineEdit(self.widget_31)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_pathlineEdit.setFont(font)
        self.Aria2_pathlineEdit.setObjectName("Aria2_pathlineEdit")
        self.gridLayout_3.addWidget(self.Aria2_pathlineEdit, 3, 2, 1, 2)
        self.Aria2_portlineEdit = QtWidgets.QLineEdit(self.widget_31)
        self.Aria2_portlineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Aria2_portlineEdit.setFont(font)
        self.Aria2_portlineEdit.setObjectName("Aria2_portlineEdit")
        self.gridLayout_3.addWidget(self.Aria2_portlineEdit, 1, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget_31)
        self.label_10.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_31)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_31)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/pic/src/aria2.png"))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 3, 1)
        self.verticalLayout_9.addWidget(self.widget_31)
        self.widget_6 = QtWidgets.QWidget(self.configscrollAreaWidgetContents)
        self.widget_6.setStyleSheet(".QWidget{\n"
"border:3px ridge #E0E0E0;\n"
"border-radius:15px;\n"
"}\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_12 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 3)
        self.choosepotButton = QtWidgets.QPushButton(self.widget_6)
        self.choosepotButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    padding:5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.choosepotButton.setObjectName("choosepotButton")
        self.gridLayout_4.addWidget(self.choosepotButton, 1, 2, 1, 1)
        self.IDMlineEdit = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IDMlineEdit.setFont(font)
        self.IDMlineEdit.setObjectName("IDMlineEdit")
        self.gridLayout_4.addWidget(self.IDMlineEdit, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget_6)
        self.label_11.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)
        self.chooseidmpushButton = QtWidgets.QPushButton(self.widget_6)
        self.chooseidmpushButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    padding:5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.chooseidmpushButton.setObjectName("chooseidmpushButton")
        self.gridLayout_4.addWidget(self.chooseidmpushButton, 2, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_6)
        self.label_13.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 2, 0, 1, 1)
        self.Potplayer_pathlineEdit = QtWidgets.QLineEdit(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Potplayer_pathlineEdit.setFont(font)
        self.Potplayer_pathlineEdit.setObjectName("Potplayer_pathlineEdit")
        self.gridLayout_4.addWidget(self.Potplayer_pathlineEdit, 1, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.configscrollAreaWidgetContents)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_7.setStyleSheet(".QWidget{\n"
"border:3px ridge #E0E0E0;\n"
"border-radius:15px;\n"
"}\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Proxy__admin_lineEdit = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Proxy__admin_lineEdit.setFont(font)
        self.Proxy__admin_lineEdit.setObjectName("Proxy__admin_lineEdit")
        self.gridLayout_6.addWidget(self.Proxy__admin_lineEdit, 3, 1, 1, 1)
        self.check_sock_pushButton = QtWidgets.QPushButton(self.widget_7)
        self.check_sock_pushButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    padding:5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.check_sock_pushButton.setObjectName("check_sock_pushButton")
        self.gridLayout_6.addWidget(self.check_sock_pushButton, 1, 4, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 3, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 3, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 6)
        self.Proxy_ip_lineEdit = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Proxy_ip_lineEdit.setFont(font)
        self.Proxy_ip_lineEdit.setObjectName("Proxy_ip_lineEdit")
        self.gridLayout_6.addWidget(self.Proxy_ip_lineEdit, 2, 1, 1, 1)
        self.Proxy_pass_lineEdit = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Proxy_pass_lineEdit.setFont(font)
        self.Proxy_pass_lineEdit.setObjectName("Proxy_pass_lineEdit")
        self.gridLayout_6.addWidget(self.Proxy_pass_lineEdit, 3, 4, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 2, 0, 1, 1)
        self.Proxy_type_comboBox = QtWidgets.QComboBox(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Proxy_type_comboBox.setFont(font)
        self.Proxy_type_comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 2px 1px 2px; \n"
"    min-width: 9em;   \n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/pic/src/三角.png);\n"
"width: 20px;\n"
"}")
        self.Proxy_type_comboBox.setObjectName("Proxy_type_comboBox")
        self.Proxy_type_comboBox.addItem("")
        self.Proxy_type_comboBox.addItem("")
        self.Proxy_type_comboBox.addItem("")
        self.Proxy_type_comboBox.addItem("")
        self.Proxy_type_comboBox.addItem("")
        self.gridLayout_6.addWidget(self.Proxy_type_comboBox, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 1, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 2, 2, 1, 1)
        self.Proxy_port_lineEdit = QtWidgets.QLineEdit(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Proxy_port_lineEdit.setFont(font)
        self.Proxy_port_lineEdit.setObjectName("Proxy_port_lineEdit")
        self.gridLayout_6.addWidget(self.Proxy_port_lineEdit, 2, 4, 1, 1)
        self.verticalLayout_9.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.configscrollAreaWidgetContents)
        self.widget_8.setStyleSheet(".QWidget{\n"
"border:3px ridge #E0E0E0;\n"
"border-radius:15px;\n"
"}\n"
"")
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_15 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 1, 1, 1, 1)
        self.webdav_passlineEdit = QtWidgets.QLineEdit(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.webdav_passlineEdit.setFont(font)
        self.webdav_passlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.webdav_passlineEdit.setObjectName("webdav_passlineEdit")
        self.gridLayout_5.addWidget(self.webdav_passlineEdit, 1, 4, 1, 1)
        self.change_webdav_pushButton = QtWidgets.QPushButton(self.widget_8)
        self.change_webdav_pushButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    padding:5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.change_webdav_pushButton.setObjectName("change_webdav_pushButton")
        self.gridLayout_5.addWidget(self.change_webdav_pushButton, 1, 7, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 0, 1, 1, 7)
        self.label_16 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 1, 3, 1, 1)
        self.webdav_adminlineEdit = QtWidgets.QLineEdit(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.webdav_adminlineEdit.setFont(font)
        self.webdav_adminlineEdit.setPlaceholderText("")
        self.webdav_adminlineEdit.setObjectName("webdav_adminlineEdit")
        self.gridLayout_5.addWidget(self.webdav_adminlineEdit, 1, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 1, 5, 1, 1)
        self.webdav_portlineEdit = QtWidgets.QLineEdit(self.widget_8)
        self.webdav_portlineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.webdav_portlineEdit.setFont(font)
        self.webdav_portlineEdit.setObjectName("webdav_portlineEdit")
        self.gridLayout_5.addWidget(self.webdav_portlineEdit, 1, 6, 1, 1)
        self.verticalLayout_9.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.configscrollAreaWidgetContents)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.nginx_url_lineEdit = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nginx_url_lineEdit.setFont(font)
        self.nginx_url_lineEdit.setObjectName("nginx_url_lineEdit")
        self.gridLayout_7.addWidget(self.nginx_url_lineEdit, 1, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 1, 0, 1, 1)
        self.usernginx_url_lineEdit = QtWidgets.QLineEdit(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.usernginx_url_lineEdit.setFont(font)
        self.usernginx_url_lineEdit.setObjectName("usernginx_url_lineEdit")
        self.gridLayout_7.addWidget(self.usernginx_url_lineEdit, 2, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 2, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.widget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 0, 0, 1, 4)
        self.verticalLayout_9.addWidget(self.widget_9)
        self.scrollArea.setWidget(self.configscrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.widget_10 = QtWidgets.QWidget(self.tab_4)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveconfig_Button = QtWidgets.QPushButton(self.widget_10)
        self.saveconfig_Button.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 14pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    padding:5px 10px 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:10px;\n"
"\n"
"}")
        self.saveconfig_Button.setObjectName("saveconfig_Button")
        self.horizontalLayout_4.addWidget(self.saveconfig_Button)
        self.verticalLayout_6.addWidget(self.widget_10)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.outprint_textBrowser = QtWidgets.QTextBrowser(self.tab_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.outprint_textBrowser.setFont(font)
        self.outprint_textBrowser.setStyleSheet("/*QScrollBar Style*/\n"
"\n"
"/*纵向滚动条*/\n"
"QScrollBar:vertical {\n"
"    background: transparent; /*背景透明*/\n"
"    width: 10px; /*宽度*/\n"
"    margin: 0px 0px 0px 0px; /**/\n"
"    padding-top: 12px; /*距离上面12px*/\n"
"    padding-bottom: 12px; /*距离底部12px*/\n"
"}\n"
"/*横向滚动条*/\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 10px; /*高度*/\n"
"    margin: 0px 0px 0px 0px;\n"
"    padding-left: 12px; /*距离左边12px*/\n"
"    padding-right: 12px; /*距离右边12px*/\n"
"}\n"
"\n"
"/*当鼠标放到纵向或者横向滚动条上面时*/\n"
"QScrollBar:vertical:hover,QScrollBar:horizontal:hover {\n"
"    background: rgba(0, 0, 0, 30); /*修改背景透明度 30*/\n"
"    border-radius: 5px; /*圆角*/\n"
"}\n"
"\n"
"/*纵向滚动条上面的滑块*/\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(131,179,249);\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"/*横向滚动条上面的滑块*/\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(0, 0, 0, 50);\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"    border: none;\n"
"}\n"
"\n"
"/*当鼠标放到滚动条滑块上面时改变透明度实现颜色的深浅变化*/\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover {\n"
"    background: #6A6AFF;\n"
"}\n"
"\n"
"/*纵向滚动条下部分块*/\n"
"QScrollBar::add-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*横向滚动条后面部分块*/\n"
"QScrollBar::add-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*纵向滚动条上面部分块*/\n"
"QScrollBar::sub-page:vertical {\n"
"    width: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*横向滚动条左部分块*/\n"
"QScrollBar::sub-page:horizontal {\n"
"    height: 10px;\n"
"    background: transparent;\n"
"}\n"
"/*纵向滚动条顶部三角形位置*/\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: top;\n"
"}\n"
"/*横向滚动条左侧三角形位置*/\n"
"QScrollBar::sub-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: left;\n"
"}\n"
"\n"
"/*纵向滚动条下面三角形部分*/\n"
"QScrollBar::add-line:vertical {\n"
"    height: 12px;\n"
"    width: 10px;\n"
"    background: transparent;\n"
"    subcontrol-position: bottom;\n"
"}\n"
"/*横向滚动条右边的三角形部分*/\n"
"QScrollBar::add-line:horizontal {\n"
"    height: 10px;\n"
"    width: 12px;\n"
"    background: transparent;\n"
"    subcontrol-position: right;\n"
"}\n"
"")
        self.outprint_textBrowser.setObjectName("outprint_textBrowser")
        self.verticalLayout_10.addWidget(self.outprint_textBrowser)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.author_browser = QtWebEngineWidgets.QWebEngineView(self.tab_6)
        self.author_browser.setObjectName("author_browser")
        self.verticalLayout_7.addWidget(self.author_browser)
        self.about_wight = QtWidgets.QWidget(self.tab_6)
        self.about_wight.setMaximumSize(QtCore.QSize(16777215, 50))
        self.about_wight.setObjectName("about_wight")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.about_wight)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.showhelp_Button = QtWidgets.QPushButton(self.about_wight)
        self.showhelp_Button.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.showhelp_Button.setObjectName("showhelp_Button")
        self.horizontalLayout_8.addWidget(self.showhelp_Button)
        self.visitmeButton = QtWidgets.QPushButton(self.about_wight)
        self.visitmeButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.visitmeButton.setObjectName("visitmeButton")
        self.horizontalLayout_8.addWidget(self.visitmeButton)
        self.visitpikpakButton = QtWidgets.QPushButton(self.about_wight)
        self.visitpikpakButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 12pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 13pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.visitpikpakButton.setObjectName("visitpikpakButton")
        self.horizontalLayout_8.addWidget(self.visitpikpakButton)
        self.verticalLayout_7.addWidget(self.about_wight)
        self.tabWidget.addTab(self.tab_6, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_8.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.main_widget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.upload_tabWidget.setCurrentIndex(0)
        self.download_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.user_lineEdit, self.password_lineEdit)
        Form.setTabOrder(self.password_lineEdit, self.localdownloadlineEdit)
        Form.setTabOrder(self.localdownloadlineEdit, self.Aria2_hostlineEdit)
        Form.setTabOrder(self.Aria2_hostlineEdit, self.Aria2_portlineEdit)
        Form.setTabOrder(self.Aria2_portlineEdit, self.Aria2_secretlineEdit)
        Form.setTabOrder(self.Aria2_secretlineEdit, self.Aria2_pathlineEdit)
        Form.setTabOrder(self.Aria2_pathlineEdit, self.Potplayer_pathlineEdit)
        Form.setTabOrder(self.Potplayer_pathlineEdit, self.IDMlineEdit)
        Form.setTabOrder(self.IDMlineEdit, self.webdav_adminlineEdit)
        Form.setTabOrder(self.webdav_adminlineEdit, self.webdav_passlineEdit)
        Form.setTabOrder(self.webdav_passlineEdit, self.webdav_portlineEdit)
        Form.setTabOrder(self.webdav_portlineEdit, self.Proxy_ip_lineEdit)
        Form.setTabOrder(self.Proxy_ip_lineEdit, self.Proxy_port_lineEdit)
        Form.setTabOrder(self.Proxy_port_lineEdit, self.Proxy__admin_lineEdit)
        Form.setTabOrder(self.Proxy__admin_lineEdit, self.Proxy_pass_lineEdit)
        Form.setTabOrder(self.Proxy_pass_lineEdit, self.pushMaxButton)
        Form.setTabOrder(self.pushMaxButton, self.checklogin_Button)
        Form.setTabOrder(self.checklogin_Button, self.tohidepushButton)
        Form.setTabOrder(self.tohidepushButton, self.clear_headers_pushButton)
        Form.setTabOrder(self.clear_headers_pushButton, self.chooselocalButton)
        Form.setTabOrder(self.chooselocalButton, self.exitapppushButton)
        Form.setTabOrder(self.exitapppushButton, self.tabWidget)
        Form.setTabOrder(self.tabWidget, self.checkaria2_Button)
        Form.setTabOrder(self.checkaria2_Button, self.refreshButton)
        Form.setTabOrder(self.refreshButton, self.backButton)
        Form.setTabOrder(self.backButton, self.filetreeWidget)
        Form.setTabOrder(self.filetreeWidget, self.addgcidButton)
        Form.setTabOrder(self.addgcidButton, self.choosepotButton)
        Form.setTabOrder(self.choosepotButton, self.chooseidmpushButton)
        Form.setTabOrder(self.chooseidmpushButton, self.sharegcidButton)
        Form.setTabOrder(self.sharegcidButton, self.tableWidget)
        Form.setTabOrder(self.tableWidget, self.change_webdav_pushButton)
        Form.setTabOrder(self.change_webdav_pushButton, self.uploadfileButton)
        Form.setTabOrder(self.uploadfileButton, self.offlinerefreshButton)
        Form.setTabOrder(self.offlinerefreshButton, self.offlineWidget)
        Form.setTabOrder(self.offlineWidget, self.check_sock_pushButton)
        Form.setTabOrder(self.check_sock_pushButton, self.addmagnetButton)
        Form.setTabOrder(self.addmagnetButton, self.scrollArea)
        Form.setTabOrder(self.scrollArea, self.Proxy_type_comboBox)
        Form.setTabOrder(self.Proxy_type_comboBox, self.visitmeButton)
        Form.setTabOrder(self.visitmeButton, self.visitpikpakButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PikPakDown"))
        self.titlelabel.setText(_translate("Form", "PikPakDown v2.2.5"))
        self.pingtitlelabel.setText(_translate("Form", "连接情况:"))
        self.pinginfo_label.setText(_translate("Form", "检测中"))
        self.tohidepushButton.setText(_translate("Form", "-"))
        self.pushMaxButton.setText(_translate("Form", "□"))
        self.exitapppushButton.setText(_translate("Form", "X"))
        self.refresh_vip_pushButton.setText(_translate("Form", "刷 新"))
        self.quota_label.setText(_translate("Form", "容量使用:"))
        self.vip_time_label.setText(_translate("Form", "会员到期时间:"))
        self.root_label.setText(_translate("Form", "根目录"))
        self.sharegcidButton.setText(_translate("Form", "导出当前秒链"))
        self.refreshButton.setText(_translate("Form", "刷新列表"))
        self.uploadfileButton.setText(_translate("Form", "上传文件"))
        self.addgcidButton.setText(_translate("Form", "导入秒链"))
        self.delete_file_pushButton.setText(_translate("Form", "删除所选"))
        self.copy_file_pushButton.setText(_translate("Form", "复制所选"))
        self.backButton.setText(_translate("Form", "上级目录"))
        self.move_file_pushButton.setText(_translate("Form", "移动所选"))
        self.creat_folder_pushButton.setText(_translate("Form", "新建文件夹"))
        self.rename_pushButton.setText(_translate("Form", "重命名所选"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "主页"))
        self.offlinerefreshButton.setText(_translate("Form", "刷新列表"))
        self.addmagnetButton.setText(_translate("Form", "添加离线任务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "离线下载"))
        self.refresh_trash_pushButton.setText(_translate("Form", "刷新列表"))
        self.back_trash_pushButton.setText(_translate("Form", "还原选中"))
        self.delete_trahs_pushButton.setText(_translate("Form", "删除选中"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "回收站"))
        self.upload_tabWidget.setTabText(self.upload_tabWidget.indexOf(self.tab_upload_now), _translate("Form", "正在上传（0）"))
        self.upload_tabWidget.setTabText(self.upload_tabWidget.indexOf(self.tab_upload_wait), _translate("Form", "等待中（0）"))
        self.upload_tabWidget.setTabText(self.upload_tabWidget.indexOf(self.tab_upload_finish), _translate("Form", "上传完成（0）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "上传列表"))
        self.download_tabWidget.setTabText(self.download_tabWidget.indexOf(self.tab_download_now), _translate("Form", "正在下载（0）"))
        self.download_tabWidget.setTabText(self.download_tabWidget.indexOf(self.tab_download_wait), _translate("Form", "等待中（0）"))
        self.download_tabWidget.setTabText(self.download_tabWidget.indexOf(self.tab_download_finish), _translate("Form", "已完成（0）"))
        self.start_alldown_pushButton.setText(_translate("Form", "全部开始"))
        self.stop_alldown_pushButton.setText(_translate("Form", "暂停全部"))
        self.open_aria2ng_pushButton.setText(_translate("Form", "打开Aria2NG"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Form", "下载列表"))
        self.label.setText(_translate("Form", " 账号 "))
        self.clear_headers_pushButton.setText(_translate("Form", "清除登录缓存"))
        self.checklogin_Button.setText(_translate("Form", "检查登录"))
        self.label_5.setText(_translate("Form", "账号设置"))
        self.pushvipcode_Button.setText(_translate("Form", "提交兑换码"))
        self.label_2.setText(_translate("Form", " 密码 "))
        self.register_Button.setText(_translate("Form", "注册账号"))
        self.label_27.setText(_translate("Form", "兑换码"))
        self.phonelogin_Button.setText(_translate("Form", "手机号登录"))
        self.label_9.setText(_translate("Form", "本地下载路径"))
        self.chooselocalButton.setText(_translate("Form", "选择路径"))
        self.localdownloadlineEdit.setPlaceholderText(_translate("Form", "不设置则默认在程序目录下载文件夹"))
        self.label_7.setText(_translate("Form", "本地下载配置"))
        self.Aria2_host.setText(_translate("Form", " Aria2地址 "))
        self.label_3.setText(_translate("Form", " Aria2密钥 "))
        self.checkaria2_Button.setText(_translate("Form", "检查Aria2连接性"))
        self.Aria2_pathlineEdit.setPlaceholderText(_translate("Form", "设置为跟Aria2下载路径一致"))
        self.label_10.setText(_translate("Form", " Aria2下载路径"))
        self.label_4.setText(_translate("Form", " 端口 "))
        self.label_12.setText(_translate("Form", "外部扩展设置"))
        self.choosepotButton.setText(_translate("Form", "选择路径"))
        self.label_11.setText(_translate("Form", " Potplayer路径 "))
        self.chooseidmpushButton.setText(_translate("Form", "选择路径"))
        self.label_13.setText(_translate("Form", " IDM路径 "))
        self.Proxy__admin_lineEdit.setPlaceholderText(_translate("Form", "未设置则留空"))
        self.check_sock_pushButton.setText(_translate("Form", "检查代理连接"))
        self.label_22.setText(_translate("Form", "密码"))
        self.label_21.setText(_translate("Form", "用户名"))
        self.label_18.setText(_translate("Form", "代理设置(重启生效)"))
        self.Proxy_pass_lineEdit.setPlaceholderText(_translate("Form", "未设置则留空"))
        self.label_19.setText(_translate("Form", "代理地址"))
        self.Proxy_type_comboBox.setCurrentText(_translate("Form", "None"))
        self.Proxy_type_comboBox.setItemText(0, _translate("Form", "None"))
        self.Proxy_type_comboBox.setItemText(1, _translate("Form", "系统代理"))
        self.Proxy_type_comboBox.setItemText(2, _translate("Form", "http"))
        self.Proxy_type_comboBox.setItemText(3, _translate("Form", "socks4"))
        self.Proxy_type_comboBox.setItemText(4, _translate("Form", "socks5"))
        self.label_20.setText(_translate("Form", "代理类型"))
        self.label_23.setText(_translate("Form", "端口"))
        self.label_15.setText(_translate("Form", "用户名"))
        self.change_webdav_pushButton.setText(_translate("Form", "开启Webdav"))
        self.label_14.setText(_translate("Form", "Webdav"))
        self.label_16.setText(_translate("Form", "密码"))
        self.label_17.setText(_translate("Form", "端口"))
        self.nginx_url_lineEdit.setPlaceholderText(_translate("Form", "不设置请留空，示例：https://go.weinb.top/api"))
        self.label_24.setText(_translate("Form", "API反代地址"))
        self.usernginx_url_lineEdit.setPlaceholderText(_translate("Form", "不设置请留空，示例：https://go.weinb.top/user"))
        self.label_26.setText(_translate("Form", "User反代地址"))
        self.label_25.setText(_translate("Form", "自定义反代(重启生效)"))
        self.saveconfig_Button.setText(_translate("Form", "保存配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "输出台"))
        self.showhelp_Button.setText(_translate("Form", "显示帮助"))
        self.visitmeButton.setText(_translate("Form", "访问作者博客"))
        self.visitpikpakButton.setText(_translate("Form", "加入官方群"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "关于"))
from PyQt5 import QtWebEngineWidgets
import res_rc
