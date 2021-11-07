# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'magnetui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MagnetDialog(object):
    def setupUi(self, MagnetDialog):
        MagnetDialog.setObjectName("MagnetDialog")
        MagnetDialog.resize(555, 399)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MagnetDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(MagnetDialog)
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
        self.magnettextEdit = QtWidgets.QTextEdit(self.widget)
        self.magnettextEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.magnettextEdit.setObjectName("magnettextEdit")
        self.verticalLayout.addWidget(self.magnettextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.magnetpushButton = QtWidgets.QPushButton(self.widget)
        self.magnetpushButton.setStyleSheet("QPushButton:!hover{\n"
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
        self.magnetpushButton.setObjectName("magnetpushButton")
        self.horizontalLayout.addWidget(self.magnetpushButton)
        self.cloeseButton = QtWidgets.QPushButton(self.widget)
        self.cloeseButton.setStyleSheet("QPushButton:!hover{\n"
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
        self.cloeseButton.setObjectName("cloeseButton")
        self.horizontalLayout.addWidget(self.cloeseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(MagnetDialog)
        QtCore.QMetaObject.connectSlotsByName(MagnetDialog)

    def retranslateUi(self, MagnetDialog):
        _translate = QtCore.QCoreApplication.translate
        MagnetDialog.setWindowTitle(_translate("MagnetDialog", "提交磁力链接"))
        self.label.setText(_translate("MagnetDialog", "磁力链接提交"))
        self.magnettextEdit.setHtml(_translate("MagnetDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.magnettextEdit.setPlaceholderText(_translate("MagnetDialog", "在此输入磁力链接，多个磁力用换行间隔"))
        self.magnetpushButton.setText(_translate("MagnetDialog", "提交磁力"))
        self.cloeseButton.setText(_translate("MagnetDialog", "关闭窗口"))
