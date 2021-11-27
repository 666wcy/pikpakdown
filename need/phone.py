# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phone.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Phone_Form(object):
    def setupUi(self, Phone_Form):
        Phone_Form.setObjectName("Phone_Form")
        Phone_Form.resize(590, 309)
        self.gridLayout = QtWidgets.QGridLayout(Phone_Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(Phone_Form)
        self.widget.setStyleSheet("#widget {\n"
"    background-color:  rgb(252,252,255);\n"
"border:1px solid rgb(131,179,249);\n"
"    border-radius: 10px;\n"
"}")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.phone_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.phone_lineEdit.setText("")
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.gridLayout_2.addWidget(self.phone_lineEdit, 2, 1, 1, 3)
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 9pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 8pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 8, 1, 1, 2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout_2.addWidget(self.password_lineEdit, 4, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
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
"\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)
        self.sendcode_Button = QtWidgets.QPushButton(self.widget)
        self.sendcode_Button.setMinimumSize(QtCore.QSize(80, 0))
        self.sendcode_Button.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 8pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 8pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.sendcode_Button.setObjectName("sendcode_Button")
        self.gridLayout_2.addWidget(self.sendcode_Button, 3, 2, 1, 1)
        self.code_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.code_lineEdit.setText("")
        self.code_lineEdit.setObjectName("code_lineEdit")
        self.gridLayout_2.addWidget(self.code_lineEdit, 3, 1, 1, 1)
        self.name_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.gridLayout_2.addWidget(self.name_lineEdit, 6, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("QLabel{\n"
"    color:rgb(234,144,146);\n"
"font: \'新宋体\';\n"
"font-weight:bold;\n"
"padding-top:8px;\n"
"padding-bottom:8px;\n"
"}\n"
"")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 2)
        self.agian_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.agian_lineEdit.setObjectName("agian_lineEdit")
        self.gridLayout_2.addWidget(self.agian_lineEdit, 5, 1, 1, 2)
        self.register_Button = QtWidgets.QPushButton(self.widget)
        self.register_Button.setStyleSheet("QPushButton:!hover{\n"
"        border:1px solid rgb(234,144,146);\n"
"    color: rgb(234,144,146);\n"
"    font: 75 9pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    border:1px solid rgb(234,144,146);\n"
"    background-color:#faefef;\n"
"    color: rgb(234,144,146);\n"
"    font: 75 8pt \"微软雅黑\";\n"
"border-radius:8px;\n"
"\n"
"}")
        self.register_Button.setObjectName("register_Button")
        self.gridLayout_2.addWidget(self.register_Button, 7, 1, 1, 2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Phone_Form)
        QtCore.QMetaObject.connectSlotsByName(Phone_Form)
        Phone_Form.setTabOrder(self.phone_lineEdit, self.code_lineEdit)
        Phone_Form.setTabOrder(self.code_lineEdit, self.register_Button)
        Phone_Form.setTabOrder(self.register_Button, self.closeButton)
        Phone_Form.setTabOrder(self.closeButton, self.sendcode_Button)

    def retranslateUi(self, Phone_Form):
        _translate = QtCore.QCoreApplication.translate
        Phone_Form.setWindowTitle(_translate("Phone_Form", "手机号登录"))
        self.phone_lineEdit.setPlaceholderText(_translate("Phone_Form", "电话，例：+8618877776666"))
        self.closeButton.setText(_translate("Phone_Form", "关闭窗口"))
        self.password_lineEdit.setPlaceholderText(_translate("Phone_Form", "6-16位密码，使用字母、数字和符号混合，账号登录无需填写"))
        self.label.setText(_translate("Phone_Form", "手机号登录"))
        self.sendcode_Button.setText(_translate("Phone_Form", "发送验证码"))
        self.code_lineEdit.setPlaceholderText(_translate("Phone_Form", "验证码"))
        self.name_lineEdit.setPlaceholderText(_translate("Phone_Form", "用户名，留空则使用官方规则，账号登录无需填写"))
        self.label_2.setText(_translate("Phone_Form", "注意：未注册会自动注册，通过此软件注册，你将获得官方活动给予的一定会员时间，开发者也因为你的注册获得一定会员时间(邀请机制)，如若介意，请自行安装官方安卓APP下载注册"))
        self.agian_lineEdit.setPlaceholderText(_translate("Phone_Form", "确认密码，账号登录无需填写"))
        self.register_Button.setText(_translate("Phone_Form", "登录"))
