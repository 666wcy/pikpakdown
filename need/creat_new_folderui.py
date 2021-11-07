# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creat_new_folderui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_New_folder_Dialog(object):
    def setupUi(self, New_folder_Dialog):
        New_folder_Dialog.setObjectName("New_folder_Dialog")
        New_folder_Dialog.resize(621, 154)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(New_folder_Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(New_folder_Dialog)
        self.widget.setStyleSheet("#widget {\n"
"    background-color: white;\n"
"border:1px solid red;\n"
"    border-radius: 10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: rgb(131,179,249);\n"
"font: \'新宋体\';\n"
"font-weight:bold;\n"
"padding-top:8px;\n"
"padding-bottom:8px;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.foder_name_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.foder_name_lineEdit.setObjectName("foder_name_lineEdit")
        self.verticalLayout.addWidget(self.foder_name_lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.creat_folderButton = QtWidgets.QPushButton(self.widget)
        self.creat_folderButton.setStyleSheet("QPushButton:!hover{\n"
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
        self.creat_folderButton.setObjectName("creat_folderButton")
        self.horizontalLayout.addWidget(self.creat_folderButton)
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setStyleSheet("QPushButton:!hover{\n"
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
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(New_folder_Dialog)
        QtCore.QMetaObject.connectSlotsByName(New_folder_Dialog)

    def retranslateUi(self, New_folder_Dialog):
        _translate = QtCore.QCoreApplication.translate
        New_folder_Dialog.setWindowTitle(_translate("New_folder_Dialog", "Dialog"))
        self.label.setText(_translate("New_folder_Dialog", "新建文件夹"))
        self.foder_name_lineEdit.setPlaceholderText(_translate("New_folder_Dialog", "输入文件夹昵称"))
        self.creat_folderButton.setText(_translate("New_folder_Dialog", "提交请求"))
        self.closeButton.setText(_translate("New_folder_Dialog", "关闭窗口"))
