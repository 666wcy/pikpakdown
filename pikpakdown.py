# -*- coding: utf-8 -*-

import json
import os

app_config = {}
icon_content = {}



def set_config():
    with open("config.json", "w") as jsonFile:
        json.dump(app_config, jsonFile, indent=4, ensure_ascii=False)
        jsonFile.close()


def read_config():
    global app_config
    if os.path.isfile("config.json") == True:
        with open('config.json', 'r') as f:
            # 读取数据并分割。 最后一个为空，所以去除
            app_config = json.loads(f.read())
        f.close()

    else:
        app_config = {
            "user": "",
            "password": "",
            "Aria2_host": "",
            "Aria2_port": "",
            "Aria2_secret": "",
            "Aria2_path": "",
            "Potplayer_path": "",
            "IDMplayer_path": "",
            "Download_path": "",
            "Webdav_admin": "",
            "Webdav_password": "",
            "Webdav_port": 9090,
            "Proxy_type": "None",
            "Proxy_ip": "",
            "Proxy_port": "",
            "Proxy_admin": "",
            "Proxy_pass": "",
            "Nginx_url":"",
            "User_url": ""

        }

        with open("config.json", "w") as jsonFile:
            json.dump(app_config, jsonFile, indent=4, ensure_ascii=False)
            jsonFile.close()


read_config()



if app_config['Proxy_type'] == "None":

    os.environ['no_proxy'] = '*'

elif app_config['Proxy_type'] == "系统代理":

    import urllib.request

    try:
        proxy=urllib.request.getproxies()
        os.environ['HTTP_PROXY'] = str(proxy['http'])

        os.environ['HTTPS_PROXY'] = str(proxy['http'])
    except:
        print("获取系统代理失败")
        os.environ['no_proxy'] = '*'
else:
    if app_config['Proxy_admin'] != "":
        os.environ[
            'HTTP_PROXY'] = f"{app_config['Proxy_type']}://{app_config['Proxy_admin']}:{app_config['Proxy_pass']}@{app_config['Proxy_ip']}:{app_config['Proxy_port']}"
        os.environ[
            'HTTPS_PROXY'] = f"{app_config['Proxy_type']}://{app_config['Proxy_admin']}:{app_config['Proxy_pass']}@{app_config['Proxy_ip']}:{app_config['Proxy_port']}"

    else:
        os.environ[
            'HTTP_PROXY'] = f"{app_config['Proxy_type']}://{app_config['Proxy_ip']}:{app_config['Proxy_port']}"
        os.environ[
            'HTTPS_PROXY'] = f"{app_config['Proxy_type']}://{app_config['Proxy_ip']}:{app_config['Proxy_port']}"


from need.hashui import Ui_Addhash
from need.yang import Ui_Form
from need.magnetui import Ui_MagnetDialog
from need.rename_fileui import Ui_Rename_file_Dialog
from need.web import Open_webdav_Worker
from need.creat_new_folderui import Ui_New_folder_Dialog
import time
import re
from PyQt5.QtWidgets import QMessageBox
from need.pikabout import check_login, get_list, get_download_url,back_tash, \
    get_offline_list, magnet_upload, gcid_hash_file,get_quate_info,\
    delete_task,get_trash_list,delete_tash,get_my_vip, \
    get_headers, login, pikpak_add_hash, get_folder_all_file,creat_folder,copy_files,move_files,delete_files,rename_file

from need.plugins import thread_Thunder, thread_IDM, thread_pot, check_aria2, thread_aria2, Copy_downloadurl_Worker

import sys
from PyQt5.QtWidgets import QMenu, QTableWidget, QTableWidgetItem, QHeaderView, QTreeWidgetItem, QVBoxLayout
from PyQt5.QtCore import QThread, QWaitCondition, QMutex, QPoint, QPropertyAnimation, QUrl
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QMouseEvent, QIcon, QDesktopServices, QMovie,QIntValidator
from PyQt5.QtWidgets import QDialog, QWidget, QLabel, QHBoxLayout, \
    QGridLayout, QSpacerItem, QSizePolicy, QGraphicsDropShadowEffect, \
    QListWidget, QListWidgetItem, QApplication, QRubberBand
import need.res_rc
from PyQt5.QtCore import  QEvent, QObject
from oss2 import StsAuth, Bucket
import oss2
import aria2p
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap, QImage,  QPainterPath,QTextCursor
from functools import reduce  # 导入排序模块
from PyQt5.QtCore import pyqtProperty, QSize, Qt, QRectF, QTimer
from PyQt5.QtGui import QColor, QPainter, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSlider
from PyQt5.QtWebEngineWidgets import QWebEngineView

import threading
from ping3 import ping
import os,base64
import requests
from urllib.parse import urlparse
from io import BytesIO
from subprocess import Popen
import subprocess

import cgitb



normal_button_style = '''
QPushButton:!hover{
		border:1px solid rgb(234,144,146);
	color: rgb(234,144,146);
	font: 75 14pt "微软雅黑";
border-radius:8px;
	padding:5px 10px 5px 10px;
}

QPushButton:hover{

	border:1px solid rgb(234,144,146);
	background-color:#faefef;
	color: rgb(234,144,146);
	font: 75 14pt "微软雅黑";
border-radius:8px;

}
'''

running_button_style = '''
QPushButton:!hover{
		border:1px solid rgb(234,144,146);
	color: rgb(234,144,146);
	font: 75 14pt "微软雅黑";
border-radius:8px;
	padding:5px 10px 5px 10px;
}

QPushButton:hover{

	border:1px solid rgb(234,144,146);
	background-color:#faefef;
	color: rgb(234,144,146);
	font: 75 14pt "微软雅黑";
border-radius:8px;

}

'''

# 列表样式
HeaderView_style = '''
QTableWidget{
border:1px solid #ADADAD;

};
QHeaderView{
background-color: #F0F0F0;
border:1px solid #d0d0d0;
border-top-style:groove
text-align:center;
font:9pt '宋体';
color: #5B5B5B;
vertical-align:top;
};
'''

# 右键菜单样式
Menu_Style = """
QMenu {
    /* 半透明效果 */
    background-color: rgba(255, 255, 255, 230);
    border: none;
    border-radius: 4px;
}

QMenu::item {
    border-radius: 4px;
    /* 这个距离很麻烦需要根据菜单的长度和图标等因素微调 */
    padding: 8px 48px 8px 36px; /* 36px是文字距离左侧距离*/
    background-color: transparent;
}

/* 鼠标悬停和按下效果 */
QMenu::item:selected {
    border-radius: 0px;
    /* 半透明效果 */
    background-color: rgba(232, 232, 232, 232);
}

/* 禁用效果 */
QMenu::item:disabled {
    background-color: transparent;
}

/* 图标距离左侧距离 */
QMenu::icon {
    left: 15px;
}

/* 分割线效果 */
QMenu::separator {
    height: 1px;
    background-color: rgb(232, 236, 243);
}
"""

# 滚动条样式
QScrollBar_style = '''
/*QScrollBar Style*/

/*纵向滚动条*/
QScrollBar:vertical {
    background: transparent; /*背景透明*/
    width: 10px; /*宽度*/
    margin: 0px 0px 0px 0px; /**/
    padding-top: 12px; /*距离上面12px*/
    padding-bottom: 12px; /*距离底部12px*/
}
/*横向滚动条*/
QScrollBar:horizontal {
    background: transparent;
    height: 10px; /*高度*/
    margin: 0px 0px 0px 0px;
    padding-left: 12px; /*距离左边12px*/
    padding-right: 12px; /*距离右边12px*/
}

/*当鼠标放到纵向或者横向滚动条上面时*/
QScrollBar:vertical:hover,QScrollBar:horizontal:hover {
    background: rgba(0, 0, 0, 30); /*修改背景透明度 30*/
    border-radius: 5px; /*圆角*/
}

/*纵向滚动条上面的滑块*/
QScrollBar::handle:vertical {
    background: rgb(131,179,249);
    width: 10px;
    border-radius: 5px;
    border: none;
}
/*横向滚动条上面的滑块*/
QScrollBar::handle:horizontal {
    background: rgba(0, 0, 0, 50);
    height: 10px;
    border-radius: 5px;
    border: none;
}

/*当鼠标放到滚动条滑块上面时改变透明度实现颜色的深浅变化*/
QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover {
    background: #6A6AFF;
}

/*纵向滚动条下部分块*/
QScrollBar::add-page:vertical {
    width: 10px;
    background: transparent;
}
/*横向滚动条后面部分块*/
QScrollBar::add-page:horizontal {
    height: 10px;
    background: transparent;
}
/*纵向滚动条上面部分块*/
QScrollBar::sub-page:vertical {
    width: 10px;
    background: transparent;
}
/*横向滚动条左部分块*/
QScrollBar::sub-page:horizontal {
    height: 10px;
    background: transparent;
}
/*纵向滚动条顶部三角形位置*/
QScrollBar::sub-line:vertical {
    height: 12px;
    width: 10px;
    background: transparent;
    subcontrol-position: top;
}
/*横向滚动条左侧三角形位置*/
QScrollBar::sub-line:horizontal {
    height: 10px;
    width: 12px;
    background: transparent;
    subcontrol-position: left;
}

/*纵向滚动条下面三角形部分*/
QScrollBar::add-line:vertical {
    height: 12px;
    width: 10px;
    background: transparent;
    subcontrol-position: bottom;
}
/*横向滚动条右边的三角形部分*/
QScrollBar::add-line:horizontal {
    height: 10px;
    width: 12px;
    background: transparent;
    subcontrol-position: right;
}
}'''

# 进度条样式
QProgressBar_StyleSheet = '''
QProgressBar::chunk {   
 background-color:rgb(58, 154, 255);
      border-radius:4px;
}
QProgressBar {   
border:none;   /*无边框*/
      background:white;
     
      text-align:center;   /*文本的位置*/
      color: black;  /*文本颜色*/

}
'''



def hum_convert(value):
    value = float(value)
    if value == 0:
        return "0"
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = 1024.0
    for i in range(len(units)):
        if (value / size) < 1:
            return "%.2f%s" % (value, units[i])
        value = value / size


# 提示框相关
class NotificationIcon:
    Info, Success, Warning, Error, Close = range(5)
    Types = {
        Info: None,
        Success: None,
        Warning: None,
        Error: None,
        Close: None
    }

    @classmethod
    def init(cls):
        cls.Types[cls.Info] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAC5ElEQVRYR8VX0VHbQBB9e/bkN3QQU0FMBSEVYFcQ8xPBJLJ1FWAqOMcaxogfTAWQCiAVRKkgTgfmM4zRZu6QhGzL0p0nDPr17e7bt7tv14RX/uiV48MJgAon+8TiAMRtMFogaqUJxADPwRRzg67kl8+xbWJWANR40iPQSSFgtX/mGQkaDr56V3VAKgGos4s2JXwJoF3naMPvMS+SrpTHs032GwGkdF+DsFMVnJm/oyGGeHico0EjIjpYes+YMyVd6R/flfkpBWCCQ9zaZM2LZDfLMGXsZ5kdI/lYBmINgHHyyLd1mWdBbAFAM/GY7K2WYx1AeB4T6L1N9umbGxZ0qktATaEAdCps48D39oq/LwEw3U5CN92LfczJoewfT7MAywDCaEbAuxeLrh0zz4L+0e4aAJfGy+sP3IMxlH1vpMJoSMCJDXgWtJeJVc6ACs9HBBrYODCJAFdYvAmkPJxnNqMwYht7Bn+T/lGg3z4DGEd3RPhQ54DBvwAOVkeqagRXfTLjh+x7+8sALOtfHLuiYzWOAiLoKbD58mnIGbCmLxUepS6NQmYlUGE0JeCTTXT9JvA9E9sZgO5iIpoyc6/YzcqSwQzgGgBXB7oXpH9klpRSkxY1xW/b7Iu2zk34PILPnazCqEPAtTWA8iZ0HsOu9L0bw4DzCJeNocMGNDpQ3IKO+6NUiJ4ysZNiBv5I3zPnmJmG5oM+wbS+9+qkvGi7NAXGmeUy0ioofa+XA0jH0UaMKpdRWs/adcwMqfV/tenqpqHY/Znt+j2gJi00RUzA201dXaxh9iZdZloJS+9H1otrkbRrD5InFqpPskxEshJQ468CkSmJC+i1HigaaxCAuCljgoDhwPdOjf7rFVxxuJrMkXScjtKc1rOLNpJk6nii5XmYzbngzlZn+RIb40kPJPTBYXUt6VEDJ8Pi6bWpNFb/jFYY6YGpDeKdjBmTKdMcxDGEmP73v2a2Gr/NOycGtglQZ/MPzEqCMLGckJEAAAAASUVORK5CYII=')))
        cls.Types[cls.Success] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACZUlEQVRYR8VXS3LTQBDtVsDbcAPMCbB3limkcAKSG4QFdnaYE2BOQLKzxSLJCeAGSUQheSnfwLmB2VJhXmpExpFHI2sk2RWv5FJPv9evP9NieuIfPzE+VSJw8qt3IMDvmahDoDYxt2UAACXMWIIowR5ffn8TJbaBWRE4CXvHAH9RgKXOgQUI48CfXZbZbiTw8Xe/w3d0zkydMkem91IZpyWOJu5sUXS+kEAqt3B+MNOLOuDqDEBLxxFHk7eza5MfIwEJDjhXTYD1s8zinYlEjsCD7FdNI9cJpEq0RFdPR47AMOzLCn69zegz6UgCP+pmfa8RSKudnPNdgCufTOLDxJtdPP7PoA1Cd8HEL5sSUCCD0B0x8bc1f8Bi6sevcgS2VXh6hMOwDz0gsUddNaxWKRjeuKfE/KlJ9Dq4UYH/o/Ns6scj+bgiMAjdayb26xLQwTfVEwg3gRcf6ARq578KuLo7VDc8psCQqwfjr4EfjYvkrAquFJ56UYpdSkAZSmNd1rrg0leOQFELgvA58OJTxVyRaAJORPOpF6UXnFUR5sDiXjs7UqsOMGMRlrWhTkJXpFL3mNrQZhA1lH3F0TiI5FurUQyMpn58VjhkSqQA4Tbw4nSVW6sBU5VXktXSeONlJH3s8jrOVr9RgVSFuNcWfzlh5n3LoKzMAPxxWuiULiQpiR2sZNnCyzIuWUr5Z1Ml0sgdHFZaShVDuR86/0huL3VXtDk/F4e11vKsTHLSCeKx7bYkW80hjLOrV1GhWH0ZrSlyh2MwdZhYfi8oZeYgLBmUiGd8sfVPM6syr2lUSYGaGBuP3QN6rVUwYV/egwAAAABJRU5ErkJggg==')))
        cls.Types[cls.Warning] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACmElEQVRYR8VXTW7TUBD+xjYSXZFukOIsSE9AskNJJMoJmq4r7OYEwAkabhBOkB/Emt4gVIojdpgbpIumEitX6gKB7UHPkauXxLHfc4F6Z3l+vvnmm/fGhAd+6IHzQwvA9cfOITMfAdQAcx1EdVEAM/tEFADsWyaPn57MfdXClABcT1qnzHSWJiwMzrwgoF91vXGRbS6AH59ajd8hDYmoURQo67tgxoij42rv62KX/04Agu44xmciVMokT32YERgGjquvZ1+y4mQCWPUa0/sk3vQlwqssEFsAVrQbU4XKL/ai2+5PPK6waQ4AOsoDnDARh83NdmwBuJq0fQI9L6p+L7rd3+/5gbAToMPI+FbkIzRRc72mbLcGIFE7jGFRIPHddmZrvstJh1X8CHGv6sxHqe1GkPYCoGcqgcoCAPPCdr2DLQC6wqMoPEj7qdqCNKllxs30sLpjYDluDUDGG5XqhY2sal3w4PiD7c7fJnHShMtJR8zpy/8CALiwndnhBgD1/t+XAXkaZAaUVHwnHulg0W6BNEWlAQD8zna8gQB0Ne70iXCm2j55jCUAei1gxvuaO+uXAcDg7zXHSy640iKUAehOEDJFqDmGQkiPLO5Fv+KADXOqvCuIsrPGsIyQdHou22YeRMJgOdHTQTkAfGk7XrLKrWlAvOhcRgBfWiZ3RQti0zxXuUFXCXMuo0TRitfxugjbIxC5RYzI6s9kIGFh+KLOpiW22id5AUuI8IaisFG4kCQg/sFKJgtPLix3KWXGeRETRbQDuCFCV2spTYMm+2FEI1WBbYIRPTeiqFtqLZeDraaD+qrbkpgQAvfl1WsXU0p/RjIjYYhTkNFgcCVlRlRKoAAc+5aF0V//NVPoc2kTLQZKZ8lx/AMXBmMwuXUwOAAAAABJRU5ErkJggg==')))
        cls.Types[cls.Error] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACrklEQVRYR82XW27aQBSG/4PtiNhIpStouoImKwjZAV1B07coWCpZQcgK6kh2lLeSFZSsIOwgdAdkBaUSEBQDpxpjU9vM+EJR03nDzJz/mzm3GcIrD3plfZQCeD47O1ho2jERNRmoE9AQG2BgBGBAwIiZe5Zh3JPjiG+5oxCAEF5q2iWITnMtRhOYu5XF4mr/9naYtSYXYGLbHQCXhYVTEwlom657rVqvBOB2uz71/a+ldq1SYe6ahnEhc4sSYGzbfQKOt915eh0D/ZrrnqS/SwEmrVYXRJ92Jb4OC+C65rrtuN0NgIltNwF837V4zN5Hy3V70e9NgFZrCKJ3CQDmJ9MwDsW36XzeB/AhA/CHqeuN2WxWX2paX2JraHneeynA+Pz8lCqVbxLjV5brimxAEJxqiEA8CjZVBvFy+bl2c9MV9hInoAw85qFpGEeRYQVEQjzMokcQHWxsiPne8jzh6j8AodGfyqNlHpiGcaKAkIk/gChwm2yYuv5W2FqfwLNtN5bAQ2bwySB83zENo50A8/1McaFRAU72XVek+mpk+D/JlIKI/xkee654uCbIhjVAqZIrgSgpLhiCwN4OAEj4vEB2yDybBCjsAol4ZD0nRdMQSRcUCsKUeNSw4o2mKMRGEOamoVx8FXDZKVosDYNMUHXAsBRnppo8RQcbpTgIGEkhykpFjnWxzGhPQYxt2yHgS/oIlKVYTJxImpG482nz+VG1Wh1N84pMCCGa0ULXHwmoJwCYnyzPW5fn/68dh7EgPbrMMl3gz7gro+n/7EoWD7w4a96l1NnJ1Yz5Lt6wCgFEk0r1CIkbiPnC9DxH5aHcd4FYGD5MOqVOg/muslh0/vphkm63k5eXZvA0I6qD+ZCI3jDzLxANiHn1NNvb6+30aVYgwLeeUsgFW1svsPA3Ncq4MHzVeO8AAAAASUVORK5CYII=')))
        cls.Types[cls.Close] = QPixmap(QImage.fromData(base64.b64decode(
            'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAeElEQVQ4T2NkoBAwUqifgboGzJy76AIjE3NCWmL0BWwumzV/qcH/f38XpCfHGcDkUVwAUsDw9+8GBmbmAHRDcMlheAGbQnwGYw0DZA1gp+JwFUgKZyDCDQGpwuIlrGGAHHAUGUCRFygKRIqjkeKERE6+oG5eIMcFAOqSchGwiKKAAAAAAElFTkSuQmCC')))

    @classmethod
    def icon(cls, ntype):
        return cls.Types.get(ntype)


class NotificationItem(QWidget):
    closed = pyqtSignal(QListWidgetItem)

    def __init__(self, title, message, item, *args, ntype=0, callback=None, **kwargs):
        super(NotificationItem, self).__init__(*args, **kwargs)
        self.item = item
        self.callback = callback
        layout = QHBoxLayout(self, spacing=0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.bgWidget = QWidget(self)  # 背景控件, 用于支持动画效果
        layout.addWidget(self.bgWidget)

        layout = QGridLayout(self.bgWidget)
        layout.setHorizontalSpacing(15)
        layout.setVerticalSpacing(10)

        # 标题左边图标
        layout.addWidget(
            QLabel(self, pixmap=NotificationIcon.icon(ntype)), 0, 0)

        # 标题
        self.labelTitle = QLabel(title, self)
        font = self.labelTitle.font()
        font.setBold(True)
        font.setPixelSize(22)
        self.labelTitle.setFont(font)

        # 关闭按钮
        self.labelClose = QLabel(
            self, cursor=Qt.PointingHandCursor, pixmap=NotificationIcon.icon(NotificationIcon.Close))

        # 消息内容
        self.labelMessage = QLabel(
            message, self, cursor=Qt.PointingHandCursor, wordWrap=True, alignment=Qt.AlignLeft | Qt.AlignTop)
        font = self.labelMessage.font()
        font.setPixelSize(20)
        self.labelMessage.setFont(font)
        self.labelMessage.adjustSize()

        # 添加到布局
        layout.addWidget(self.labelTitle, 0, 1)
        layout.addItem(QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 0, 2)
        layout.addWidget(self.labelClose, 0, 3)
        layout.addWidget(self.labelMessage, 1, 1, 1, 2)

        # 边框阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setColor(QColor(0, 0, 0, 25))
        effect.setOffset(0, 2)
        self.setGraphicsEffect(effect)

        self.adjustSize()

        # 5秒自动关闭
        self._timer = QTimer(self, timeout=self.doClose)
        self._timer.setSingleShot(True)  # 只触发一次
        self._timer.start(5000)

    def doClose(self):
        try:
            # 可能由于手动点击导致item已经被删除了
            self.closed.emit(self.item)
        except:
            pass

    def showAnimation(self, width):
        # 显示动画
        pass

    def closeAnimation(self):
        # 关闭动画
        pass

    def mousePressEvent(self, event):
        super(NotificationItem, self).mousePressEvent(event)
        w = self.childAt(event.pos())
        if not w:
            return
        if w == self.labelClose:  # 点击关闭图标
            # 先尝试停止计时器
            self._timer.stop()
            self.closed.emit(self.item)
        elif w == self.labelMessage and self.callback and callable(self.callback):
            # 点击消息内容
            self._timer.stop()
            self.closed.emit(self.item)
            self.callback()  # 回调

    def paintEvent(self, event):
        # 圆角以及背景色
        super(NotificationItem, self).paintEvent(event)
        painter = QPainter(self)
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 6, 6)
        painter.fillPath(path, Qt.white)


class NotificationWindow(QListWidget):
    _instance = None

    def __init__(self, *args, **kwargs):
        super(NotificationWindow, self).__init__(*args, **kwargs)
        self.setSpacing(20)
        self.setMinimumWidth(412)
        self.setMaximumWidth(412)
        QApplication.instance().setQuitOnLastWindowClosed(True)
        # 隐藏任务栏,无边框,置顶等
        self.setWindowFlags(self.windowFlags() | Qt.Tool |
                            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 去掉窗口边框
        self.setFrameShape(self.NoFrame)
        # 背景透明
        self.viewport().setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 不显示滚动条
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 获取屏幕高宽
        rect = QApplication.instance().desktop().availableGeometry(self)
        self.setMinimumHeight(rect.height())
        self.setMaximumHeight(rect.height())
        self.move(rect.width() - self.minimumWidth() - 18, 0)

    def removeItem(self, item):
        # 删除item
        w = self.itemWidget(item)
        self.removeItemWidget(item)
        item = self.takeItem(self.indexFromItem(item).row())
        w.close()
        w.deleteLater()
        del item

    @classmethod
    def _createInstance(cls):
        # 创建实例
        if not cls._instance:
            cls._instance = NotificationWindow()
            cls._instance.show()
            NotificationIcon.init()

    @classmethod
    def info(cls, title, message, callback=None):
        cls._createInstance()
        item = QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance,
                             ntype=NotificationIcon.Info, callback=callback)
        w.closed.connect(cls._instance.removeItem)
        item.setSizeHint(QSize(cls._instance.width() -
                               cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def success(cls, title, message, callback=None):
        cls._createInstance()
        item = QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance,
                             ntype=NotificationIcon.Success, callback=callback)
        w.closed.connect(cls._instance.removeItem)
        item.setSizeHint(QSize(cls._instance.width() -
                               cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def warning(cls, title, message, callback=None):
        cls._createInstance()
        item = QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item, cls._instance,
                             ntype=NotificationIcon.Warning, callback=callback)
        w.closed.connect(cls._instance.removeItem)
        item.setSizeHint(QSize(cls._instance.width() -
                               cls._instance.spacing(), w.height()))
        cls._instance.setItemWidget(item, w)

    @classmethod
    def error(cls, title, message, callback=None):
        cls._createInstance()
        item = QListWidgetItem(cls._instance)
        w = NotificationItem(title, message, item,
                             ntype=NotificationIcon.Error, callback=callback)
        w.closed.connect(cls._instance.removeItem)
        width = cls._instance.width() - cls._instance.spacing()
        item.setSizeHint(QSize(width, w.height()))
        cls._instance.setItemWidget(item, w)


# 主页刷新调用
class refreshThread(QThread):
    refresh_proess_signal = pyqtSignal(list)  # 创建信号

    def __init__(self, folder_id):
        super(refreshThread, self).__init__()

        self.folder_id = folder_id

    def start_choose_icon(self, icon_url):
        global icon_content
        if icon_url in icon_content:

            return icon_content[icon_url]
        else:
            try:
                result = requests.get(icon_url,  timeout=5).content
                icon_content[icon_url] = result
                return result
            except:
                return ""

    def run(self):
        try:
            file_list = get_list(self.folder_id)

            for a in range(len(file_list)):


                file_list[a]['icon_content']=self.start_choose_icon(icon_url=file_list[a]['icon_link'])


            self.refresh_proess_signal.emit(file_list)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


# 下载调用
class downloadThread(QThread):
    download_proess_signal = pyqtSignal(list)  # 创建信号

    def __init__(self, url, filesize, file_name, buffer,  down_path):
        super(downloadThread, self).__init__()
        if app_config['Download_path'] != "":
            self.file_path = f"{app_config['Download_path']}/{down_path}"

            if not os.path.exists(self.file_path):
                os.makedirs(self.file_path)
        else:
            self.file_path = f"下载/{down_path}"
            parent_path = os.path.dirname(self.file_path)
            if not os.path.exists(self.file_path):
                os.makedirs(self.file_path)
        self.file_name = file_name
        self.url = url
        self.filesize = filesize

        self.buffer = buffer

        self.download_list = []


        self.currdownload = None

        self.aria2 = aria2p.API(
            aria2p.Client(
                host="http://127.0.0.1",
                port=29385,
                secret="pikpakdown"
            )
        )

        try:
            sta = self.aria2.get_stats()

        except Exception as e:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):本地aria2未启动,即将启动")

            pid = os.getpid()
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE |subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            subprocess.Popen(
                ["Aria2/aria2c.exe", '--enable-rpc=true', f'--stop-with-process={pid}', '--conf-path=Aria2/aria2.conf',
                 "--rpc-listen-port=29385", '--rpc-secret=pikpakdown'], startupinfo=startupinfo)
            try:
                sta = self.aria2.get_stats()
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f"INFO ({new_time}):本地Aria2启动成功")

            except Exception as e:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f"Error ({new_time}):连接本地Aria2失败:{e}")


                return





    def run(self):

        try:
            currdownload = self.aria2.add_uris([self.url], options={"dir": self.file_path, "out": self.file_name})
            self.currdownload = currdownload
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):内部下载添加任务：{self.file_name} 路径:{self.file_path}")
        except Exception as e:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):添加下载任务失败:{self.file_name}:{e}")

            return None



# 上传调用
class uploadThread(QThread):
    upload_proess_signal = pyqtSignal(list)  # 创建信号

    def __init__(self, path, folder_id, row):
        super(uploadThread, self).__init__()
        try:
            self.folder_id = folder_id
            self.file_path = path
            self.old_time = 0
            self.old_part = 0
            self.row = row


            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):开始上传:{path}")

            self._isPause = False
            self._isRemove = False
            self._value = 0
            self.cond = QWaitCondition()
            self.mutex = QMutex()
        except Exception as e:


            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):上传错误:{e}")

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

    def remove(self):
        self._isRemove = True
        self.cond.wakeAll()

    def percentage(self, consumed_bytes, total_bytes):
        """进度条回调函数，计算当前完成的百分比

        :param consumed_bytes: 已经上传/下载的数据量
        :param total_bytes: 总数据量
        """
        self.mutex.lock()
        if self._isPause:
            self.upload_proess_signal.emit([0, self.row, '0M/S', "上传暂停"])  # 发送信号
            self.cond.wait(self.mutex)
        if self._isRemove:
            self.upload_proess_signal.emit([0, self.row, '0M/S', "上传删除"])  # 发送信号
            # self.exit(0)  # 关闭线程
            QThread.exit(0)

        if total_bytes:
            if self.old_time == 0:
                self.old_time = time.time()
                self.old_part = float(consumed_bytes)
            else:
                if time.time() - self.old_time > 1:
                    if float(consumed_bytes) != self.old_part:
                        speed = (float(consumed_bytes) - self.old_part) / 1024 / 1024
                    else:
                        speed = 0

                    self.old_time = time.time()
                    self.old_part = float(consumed_bytes)
                    rate = int(100 * (float(consumed_bytes) / float(total_bytes)))

                    self.upload_proess_signal.emit([rate, self.row, '%.2fM/S' % speed, "上传中"])  # 发送信号
        else:
            self.upload_proess_signal.emit([100, self.row, '0M/S', "上传完成"])  # 发送信号

        self.mutex.unlock()

    def run(self):
        try:

            file_hash, file_size, filename = gcid_hash_file(self.file_path)

            if app_config['Nginx_url'] == "":
                pikpak_api_url = "https://api-drive.mypikpak.com"

            else:
                pikpak_api_url = app_config['Nginx_url']

            upload_url = f"{pikpak_api_url}/drive/v1/files"
            login_headers = get_headers()
            upload_url_data = {
                "kind": "drive#file",
                "name": str(filename),
                "size": int(file_size),
                "hash": str(file_hash),
                "upload_type": "UPLOAD_TYPE_RESUMABLE",
                "objProvider": {"provider": "UPLOAD_TYPE_UNKNOWN"}}
            if self.folder_id != "":
                upload_url_data["parent_id"] = self.folder_id
            upload_result = requests.post(url=upload_url, headers=login_headers, json=upload_url_data,  timeout=5).json()

            if "error" in upload_result:


                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"Info ({new_time}):登录过期，正在重新登录")
                login()
                login_headers = get_headers()
                upload_result = requests.post(url=upload_url, headers=login_headers, json=upload_url_data,  timeout=5)

            if 'resumable' in upload_result:
                auth = StsAuth(access_key_id=upload_result['resumable']['params']['access_key_id'],
                               access_key_secret=upload_result['resumable']['params']['access_key_secret'],
                               security_token=upload_result['resumable']['params']['security_token']
                               )

                # Endpoint以杭州为例，其它Region请按实际情况填写。
                bucket = Bucket(auth=auth,
                                endpoint=f"https://{upload_result['resumable']['params']['endpoint']}",
                                bucket_name=upload_result['resumable']['params']['bucket'], is_cname=True,
                                )

                key = upload_result['resumable']['params']['key']

                oss2.resumable_upload(bucket, key, self.file_path,
                                      multipart_threshold=265 * 1024,
                                      part_size=265 * 1024,
                                      num_threads=2,
                                      progress_callback=self.percentage)
                # self.upload_proess_signal.emit([100, self.row, '0M/S', "上传完成"])  # 发送信号

            else:



                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"Info ({new_time}):已存在，直接秒传:{filename}")
                self.upload_proess_signal.emit([100, self.row, '%.2fM/S' % 0, "秒传完成"])  # 发送信号




        except Exception as e:


            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):上传失败:{e}")


# 添加磁力子弹窗
class MyMagnet_Form(QDialog, Ui_MagnetDialog):
    _signal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):

        super(MyMagnet_Form, self).__init__(parent)
        self.setupUi(self)

        # 将子窗口置顶
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # dialog相关
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.widget.setStyleSheet(Widget_Stylesheet)

        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

        self.magnetpushButton.clicked.connect(self.push_new_magnnet)
        self.cloeseButton.clicked.connect(self.close)

        # 窗口淡化动画
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(500)  # 持续时间1秒
        self.doShow()
        ###

    # 窗口淡化动画
    def doShow(self):
        try:
            # 尝试先取消动画完成后关闭窗口的信号
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # 透明度范围从0逐渐增加到1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)  # 动画完成则关闭窗口
        # 透明度范围从1逐渐减少到0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    ###

    # 鼠标移动事件
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    ###

    def push_new_magnnet(self):

        magnet_url = self.magnettextEdit.toPlainText()

        if magnet_url == "":
            QMessageBox.information(self, "提示", "输入框为空")
            return
        self._signal.emit(magnet_url)


        self.close()


# 添加秒传子弹窗
class MyHash_Form(QDialog, Ui_Addhash):
    # 定义信号
    _signal = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):

        super(MyHash_Form, self).__init__(parent)
        self.setupUi(self)

        # 将子窗口置顶
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # dialog相关
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.widget.setStyleSheet(Widget_Stylesheet)

        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

        self.closeButton.clicked.connect(self.close)

        # 窗口淡化动画
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(500)  # 持续时间1秒
        self.doShow()
        ###
        self.addhashButton.clicked.connect(self.get_hash_text)

    def get_hash_text(self):
        hash_list = []
        hash_text = self.hashtextEdit.toPlainText()
        if "\n" not in hash_text:
            hash_list.append(hash_text)
        else:
            temp = str(hash_text).split("\n")
            hash_list = hash_list + temp

        self._signal.emit(hash_list)
        self.close()

    # 窗口淡化动画
    def doShow(self):
        try:
            # 尝试先取消动画完成后关闭窗口的信号
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # 透明度范围从0逐渐增加到1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)  # 动画完成则关闭窗口
        # 透明度范围从1逐渐减少到0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    ###

    # 鼠标移动事件
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    ###


# 新建文件夹子弹窗
class My_new_folder_Form(QDialog, Ui_New_folder_Dialog):
    # 定义信号
    _signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):

        super(My_new_folder_Form, self).__init__(parent)
        self.setupUi(self)

        # 将子窗口置顶
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # dialog相关
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.widget.setStyleSheet(Widget_Stylesheet)

        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

        self.closeButton.clicked.connect(self.close)

        # 窗口淡化动画
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(500)  # 持续时间1秒
        self.doShow()

        self.creat_folderButton.clicked.connect(self.get_folder_name)

    def get_folder_name(self):
        folder_name = self.foder_name_lineEdit.text()

        self._signal.emit(str(folder_name))
        self.close()





    # 窗口淡化动画
    def doShow(self):
        try:
            # 尝试先取消动画完成后关闭窗口的信号
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # 透明度范围从0逐渐增加到1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)  # 动画完成则关闭窗口
        # 透明度范围从1逐渐减少到0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    ###

    # 鼠标移动事件
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    ###


# 新建文件夹子弹窗
class Rename_file_Form(QDialog, Ui_Rename_file_Dialog):
    # 定义信号
    _signal = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None,file_id=None):

        super(Rename_file_Form, self).__init__(parent)
        self.setupUi(self)
        self.file_id = file_id
        # 将子窗口置顶
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        # dialog相关
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.widget.setStyleSheet(Widget_Stylesheet)

        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

        self.closeButton.clicked.connect(self.close)

        # 窗口淡化动画
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setDuration(500)  # 持续时间1秒
        self.doShow()

        self.creat_folderButton.clicked.connect(self.get_folder_name)

    def get_folder_name(self):
        folder_name = self.foder_name_lineEdit.text()
        result = {'name':folder_name,"file_id":self.file_id}
        self._signal.emit(result)
        self.close()





    # 窗口淡化动画
    def doShow(self):
        try:
            # 尝试先取消动画完成后关闭窗口的信号
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # 透明度范围从0逐渐增加到1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)  # 动画完成则关闭窗口
        # 透明度范围从1逐渐减少到0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()

    ###

    # 鼠标移动事件
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    ###

# 线程添加秒传
class Hash_Worker(QThread):
    valueChanged = pyqtSignal(list)  # 值变化信号

    def __init__(self, name_list, size_list, file_hash_list, folder_id):
        super(Hash_Worker, self).__init__()

        self.name_list = name_list
        self.size_list = size_list
        self.file_hash_list = file_hash_list
        self.folder_id = folder_id

    def run(self):
        try:
            for name, size, file_hash in zip(self.name_list, self.size_list, self.file_hash_list):
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"Info ({new_time}):添加秒传:{name}-{file_hash}")
                result = pikpak_add_hash(filename=name, file_size=size, file_hash=file_hash, folder_id=self.folder_id)

                self.valueChanged.emit([result, name])
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


# 添加下载任务url线程
class Add_download_Worker(QThread):
    valueChanged = pyqtSignal(list)  # 值变化信号

    def __init__(self, fileid):
        super(Add_download_Worker, self).__init__()

        self.fileid = fileid


    def run(self):
        try:
            down_name, down_url, file_size = get_download_url(file_id=self.fileid)


            if down_url == "":


                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"Info ({new_time}):内部下载,识别为文件夹:{down_name}")

                name_list, url_list, size_list, path_list = get_folder_all_file(folder_id=self.fileid, path=f"{down_name}/")
                for name, url, size, path in zip(name_list, url_list, size_list, path_list):



                    down_name = f"{name}"
                    the_filesize = size
                    file_size = size
                    down_url = url
                    down_path = path
                    self.valueChanged.emit([down_name, down_url, file_size, the_filesize, down_path])


            else:
                the_url = down_url
                the_filesize = requests.get(the_url, stream=True,  timeout=5).headers['Content-Length']
                self.valueChanged.emit([down_name, down_url, file_size, the_filesize, ""])
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


# 添加检查网络线程
class Ping_networl_Worker(QThread):
    valueChanged = pyqtSignal(int)  # 值变化信号

    def __init__(self):
        super(Ping_networl_Worker, self).__init__()


    def run(self):
        try:
            if app_config['Nginx_url'] == "":
                host = 'api-drive.mypikpak.com'
            else:
                host = urlparse(str(app_config['Nginx_url']))[1]
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):延迟检测地址:{host}")
            while True:
            # 简单用法 ping地址即可，超时会返回None 否则返回耗时，单位默认是秒
                if app_config['Proxy_type']=="None":

                    second = ping(host)

                    if second != None:

                        self.valueChanged.emit(int(second * 1000))

                    else:

                        self.valueChanged.emit(0)
                else:
                    self.valueChanged.emit(-1)
                    return
                time.sleep(2)
        except:
            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


# 窗口缩放类
class FramelessObject(QObject):
    Margins = 1  # 边缘边距
    TitleHeight = 10  # 标题栏高度
    Widgets = set()  # 无边框窗口集合

    @classmethod
    def set_margins(cls, margins):
        cls.Margins = margins

    @classmethod
    def set_title_height(cls, height):
        cls.TitleHeight = height

    @classmethod
    def add_widget(cls, widget):
        cls.Widgets.add(widget)

    @classmethod
    def del_widget(cls, widget):
        if widget in cls.Widgets:
            cls.Widgets.remove(widget)

    def _get_edges(self, pos, width, height):
        """根据坐标获取方向
        :param pos: QPoint
        :param width: int
        :param height: int
        :return: Qt.Edges
        """
        edge = 0
        x, y = pos.x(), pos.y()

        if y <= self.Margins:
            edge |= Qt.TopEdge
        if x <= self.Margins:
            edge |= Qt.LeftEdge
        if x >= width - self.Margins:
            edge |= Qt.RightEdge
        if y >= height - self.Margins:
            edge |= Qt.BottomEdge

        return edge

    def _get_cursor(self, edges):
        """调整鼠标样式
        :param edges: int or None
        :return: Qt.CursorShape
        """
        if edges == Qt.LeftEdge | Qt.TopEdge or edges == Qt.RightEdge | Qt.BottomEdge:
            return Qt.SizeFDiagCursor
        elif edges == Qt.RightEdge | Qt.TopEdge or edges == Qt.LeftEdge | Qt.BottomEdge:
            return Qt.SizeBDiagCursor
        elif edges == Qt.LeftEdge or edges == Qt.RightEdge:
            return Qt.SizeHorCursor
        elif edges == Qt.TopEdge or edges == Qt.BottomEdge:
            return Qt.SizeVerCursor

        return Qt.ArrowCursor

    def is_titlebar(self, pos):
        """判断是否是标题栏
        :param pos: QPoint
        :return: bool
        """
        return pos.y() <= self.TitleHeight

    def moveOrResize(self, window, pos, width, height):
        edges = self._get_edges(pos, width, height)
        if edges:
            if window.windowState() == Qt.WindowNoState:
                window.startSystemResize(edges)
        else:
            if self.is_titlebar(pos):
                window.startSystemMove()

    def eventFilter(self, obj, event):
        if obj.isWindowType():
            # top window 处理光标样式
            if event.type() == QEvent.MouseMove and obj.windowState() == Qt.WindowNoState:
                obj.setCursor(self._get_cursor(self._get_edges(event.pos(), obj.width(), obj.height())))
            elif event.type() == QEvent.TouchUpdate:
                self.moveOrResize(obj, event.pos(), obj.width(), obj.height())
        elif obj in self.Widgets and isinstance(event, QMouseEvent) and event.button() == Qt.LeftButton:
            if event.type() == QEvent.MouseButtonDblClick:
                # 双击最大化还原
                if self.is_titlebar(event.pos()):
                    if obj.windowState() == Qt.WindowFullScreen:
                        pass
                    elif obj.windowState() == Qt.WindowMaximized:
                        obj.showNormal()
                    else:
                        obj.showMaximized()
            elif event.type() == QEvent.MouseButtonPress:
                self.moveOrResize(obj.windowHandle(), event.pos(), obj.width(), obj.height())

        return False


# 等待加载动画
class Wait_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        label = QLabel()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(
            self.windowFlags() | Qt.FramelessWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.Tool)

        # 将子窗口置顶
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.setAlignment(Qt.AlignCenter)
        text_label = QLabel()
        text_label.setText("双击动画取消加载")
        text_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        text_label.setStyleSheet("QLabel{border:1px solid gray;border-radius:8px;}")

        vbox.addWidget(text_label)
        self.setLayout(vbox)

        gif = QMovie(':/pic/src/loading.gif')
        #设置gif大小
        gif.setScaledSize(QSize().scaled(300, 300, Qt.KeepAspectRatio))
        label.setMovie(gif)
        gif.start()

    def mouseDoubleClickEvent(self, QMouseEvent):

        self.close()


# 添加鼠标悬浮显示图片
class Mouse_maintable_Worker(QThread):
    valueChanged = pyqtSignal(list)  # 值变化信号

    def __init__(self,parent, row, column,img_url):
        super(Mouse_maintable_Worker, self).__init__()

        self.row = row
        self.column = column
        self.img_url = img_url


    def run(self):
        try:
            response = requests.get(self.img_url)  # 将这个图片保存在内存

            # 得到这个图片的base64编码
            ls_f = base64.b64encode(BytesIO(response.content).read())
            # 打印出这个base64编码

            img_base64 = str(ls_f, encoding='utf-8')

            img_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'

            self.valueChanged.emit([self.row, self.column, img_html])
        except:

            None


# Mpv播放器
class Mpv_video_Worker(QThread):
    valueChanged = pyqtSignal(list)  # 值变化信号

    def __init__(self,file_id):
        super(Mpv_video_Worker, self).__init__()

        self.file_id = file_id



    def run(self):
        try:
            down_name, down_url, file_size = get_download_url(self.file_id)
            Popen(["MPV/mpv",  down_url,f"--title={down_name}"])
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)

#检查代理线程
class Check_proxy_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self, Proxy_type,Proxy_ip,Proxy_port,Proxy_admin,Proxy_pass ):
        super(Check_proxy_Worker, self).__init__()
        self.Proxy_type =Proxy_type

        self.Proxy_ip = Proxy_ip
        self.Proxy_port = Proxy_port
        self.Proxy_admin = Proxy_admin
        self.Proxy_pass = Proxy_pass


    def run(self):
        try:
            s = requests.session()
            if self.Proxy_type == "None":


                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


                print(f"Info ({new_time}):未启用代理")
            elif self.Proxy_admin != "":
                proxy_proxies = {'https': f"{self.Proxy_type}://{self.Proxy_admin}:{self.Proxy_pass}@{self.Proxy_ip}:{self.Proxy_port}"}
            else:
                proxy_proxies = {'https': f"{self.Proxy_type}://{self.Proxy_ip}:{self.Proxy_port}"}
            try:
                print(s.proxies)
                requests.get(url="https://www.baidu.com",proxies=proxy_proxies,timeout=5)

                self.valueChanged.emit(True)  # 发送信号
            except Exception as e:

                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"Error ({new_time}):代理测试失败:{e}")
                self.valueChanged.emit(False)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


#检查登录线程
class Check_login_Worker(QThread):
    valueChanged = pyqtSignal(dict)  # 值变化信号

    def __init__(self, login_admin,login_password ):
        super(Check_login_Worker, self).__init__()


        self.login_admin = login_admin
        self.login_password = login_password


    def run(self):
        try:
            check_result = check_login(login_admin=self.login_admin, login_password=self.login_password)

            if check_result != False:
                self.valueChanged.emit(check_result)  # 发送信号
            else:
                self.valueChanged.emit({})  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)

#检查aria2线程
class Check_aria2_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self, Aria2_host,Aria2_port,Aria2_secret ):
        super(Check_aria2_Worker, self).__init__()


        self.Aria2_host = Aria2_host
        self.Aria2_port = Aria2_port
        self.Aria2_secret = Aria2_secret

    def run(self):
        try:
            check_result = check_aria2(Aria2_host=self.Aria2_host, Aria2_port=self.Aria2_port, Aria2_secret=self.Aria2_secret)

            self.valueChanged.emit(check_result)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


# 离线列表刷新调用
class offline_Thread(QThread):
    refresh_proess_signal = pyqtSignal(list)  # 创建信号

    def __init__(self):
        super(offline_Thread, self).__init__()

    def start_choose_icon(self, icon_url):
        global icon_content
        if icon_url in icon_content:

            return icon_content[icon_url]
        else:
            try:
                result = requests.get(icon_url,  timeout=5).content
                icon_content[icon_url] = result
                return result
            except:
                return ""

    def run(self):
        try:
            file_list = get_offline_list()

            for a in range(len(file_list)):


                file_list[a]['icon_content']=self.start_choose_icon(icon_url=file_list[a]['icon_link'])

            self.refresh_proess_signal.emit(file_list)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


# 回收站列表刷新调用
class trash_Thread(QThread):
    refresh_proess_signal = pyqtSignal(list)  # 创建信号

    def __init__(self):
        super(trash_Thread, self).__init__()

    def start_choose_icon(self, icon_url):
        global icon_content
        if icon_url in icon_content:

            return icon_content[icon_url]
        else:
            try:
                result = requests.get(icon_url,  timeout=5).content
                icon_content[icon_url] = result
                return result
            except:
                return ""

    def run(self):
        try:
            file_list = get_trash_list()

            for a in range(len(file_list)):


                file_list[a]['icon_content']=self.start_choose_icon(icon_url=file_list[a]['icon_link'])

            self.refresh_proess_signal.emit(file_list)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)

#重定向打印
class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))

#创建文件夹进程
class Creat_folder_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self, name,folder_id ):
        super(Creat_folder_Worker, self).__init__()


        self.name = name
        self.folder_id = folder_id


    def run(self):
        try:


            creat_folder(parent_id=self.folder_id,name=self.name)
            self.valueChanged.emit(True)  # 发送信号

        except:
            self.valueChanged.emit(False)  # 发送信号
            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


#粘贴文件夹进程
class Paste_file_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self, paste_type,folder_id,to_id):
        super(Paste_file_Worker, self).__init__()

        self.paste_type = paste_type
        self.folder_id = folder_id
        self.to_id = to_id


    def run(self):
        try:
            if self.paste_type:
                copy_files(parent_id=self.to_id,file_id=self.folder_id)
            else:
                move_files(parent_id=self.to_id,file_id=self.folder_id)
            self.valueChanged.emit(True)  # 发送信号

        except:
            self.valueChanged.emit(False)  # 发送信号
            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


#删除文件进程
class Delete_file_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self,file_id):
        super(Delete_file_Worker, self).__init__()

        self.file_id = file_id


    def run(self):
        try:
            delete_files(file_id=self.file_id)
            self.valueChanged.emit(True)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


#删除回收站文件进程
class Delete_trash_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self,file_id):
        super(Delete_trash_Worker, self).__init__()

        self.file_id = file_id


    def run(self):
        try:
            delete_tash(file_id=self.file_id)
            self.valueChanged.emit(True)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


#还原回收站文件进程
class Back_trash_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self,file_id):
        super(Back_trash_Worker, self).__init__()

        self.file_id = file_id


    def run(self):
        try:
            back_tash(file_id=self.file_id)
            self.valueChanged.emit(True)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


#删除文件进程
class Rename_file_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self,file_id,name):
        super(Rename_file_Worker, self).__init__()

        self.file_id = file_id
        self.name = name


    def run(self):
        try:
            rename_file(file_id=self.file_id,name=self.name)
            self.valueChanged.emit(True)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


#删除任务进程
class Delete_task_Worker(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self,file_id):
        super(Delete_task_Worker, self).__init__()

        self.file_id = file_id


    def run(self):
        try:
            delete_task(task_id=self.file_id)
            self.valueChanged.emit(True)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)


#添加离线任务进程
class Add_magnet_Worker(QThread):


    def __init__(self,magnet_text):
        super(Add_magnet_Worker, self).__init__()

        self.magnet_text = magnet_text


    def run(self):
        try:
            magnet_upload(file_url=self.magnet_text)

        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)

#刷新容量进程
class Get_quate_task_Worker(QThread):
    valueChanged = pyqtSignal(dict)  # 值变化信号

    def __init__(self):
        super(Get_quate_task_Worker, self).__init__()


    def run(self):
        try:
            result = get_quate_info()
            vip_info = get_my_vip()
            trans_dict = {"quate":result,"user":vip_info}
            self.valueChanged.emit(trans_dict)  # 发送信号
        except:

            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)

#圆形进度条
class PercentProgressBar(QWidget):
    MinValue = 0
    MaxValue = 100
    Value = 0
    BorderWidth = 4
    Clockwise = True  # 顺时针还是逆时针
    ShowPercent = True  # 是否显示百分比
    ShowFreeArea = False  # 显示背后剩余
    ShowSmallCircle = False  # 显示带头的小圆圈
    TextColor = QColor(255, 255, 255)  # 文字颜色
    BorderColor = QColor(24, 189, 155)  # 边框圆圈颜色
    BackgroundColor = QColor(70, 70, 70)  # 背景颜色

    def __init__(self, *args, value=0, minValue=0, maxValue=100,
                 borderWidth=4, clockwise=True, showPercent=True,
                 showFreeArea=False, showSmallCircle=False,
                 textColor=QColor(255, 255, 255),
                 borderColor=QColor(24, 189, 155),
                 backgroundColor=QColor(70, 70, 70), **kwargs):
        super(PercentProgressBar, self).__init__(*args, **kwargs)
        self.Value = value
        self.MinValue = minValue
        self.MaxValue = maxValue
        self.BorderWidth = borderWidth
        self.Clockwise = clockwise
        self.ShowPercent = showPercent
        self.ShowFreeArea = showFreeArea
        self.ShowSmallCircle = showSmallCircle
        self.TextColor = textColor
        self.BorderColor = borderColor
        self.BackgroundColor = backgroundColor

    def setRange(self, minValue: int, maxValue: int):
        if minValue >= maxValue:  # 最小值>=最大值
            return
        self.MinValue = minValue
        self.MaxValue = maxValue
        self.update()

    def paintEvent(self, event):
        super(PercentProgressBar, self).paintEvent(event)
        width = self.width()
        height = self.height()
        side = min(width, height)

        painter = QPainter(self)
        # 反锯齿
        painter.setRenderHints(QPainter.Antialiasing |
                               QPainter.TextAntialiasing)
        # 坐标中心为中间点
        painter.translate(width / 2, height / 2)
        # 按照100x100缩放
        painter.scale(side / 100.0, side / 100.0)

        # 绘制中心园
        self._drawCircle(painter, 50)
        # 绘制圆弧
        self._drawArc(painter, 50 - self.BorderWidth / 2)
        # 绘制文字
        self._drawText(painter, 50)

    def _drawCircle(self, painter: QPainter, radius: int):
        # 绘制中心园
        radius = radius - self.BorderWidth
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.BackgroundColor)
        painter.drawEllipse(QRectF(-radius, -radius, radius * 2, radius * 2))
        painter.restore()

    def _drawArc(self, painter: QPainter, radius: int):
        # 绘制圆弧
        painter.save()
        painter.setBrush(Qt.NoBrush)
        # 修改画笔
        pen = painter.pen()
        pen.setWidthF(self.BorderWidth)
        pen.setCapStyle(Qt.RoundCap)

        arcLength = 360.0 / (self.MaxValue - self.MinValue) * self.Value
        rect = QRectF(-radius, -radius, radius * 2, radius * 2)

        if not self.Clockwise:
            # 逆时针
            arcLength = -arcLength

        # 绘制剩余进度圆弧
        if self.ShowFreeArea:
            acolor = self.BorderColor.toRgb()
            acolor.setAlphaF(0.2)
            pen.setColor(acolor)
            painter.setPen(pen)
            painter.drawArc(rect, (0 - arcLength) *
                            16, -(360 - arcLength) * 16)

        # 绘制当前进度圆弧
        pen.setColor(self.BorderColor)
        painter.setPen(pen)
        painter.drawArc(rect, 0, int(-arcLength * 16))

        # 绘制进度圆弧前面的小圆
        if self.ShowSmallCircle:
            offset = radius - self.BorderWidth + 1
            radius = self.BorderWidth / 2 - 1
            painter.rotate(-90)
            circleRect = QRectF(-radius, radius + offset,
                                radius * 2, radius * 2)
            painter.rotate(arcLength)
            painter.drawEllipse(circleRect)

        painter.restore()

    def _drawText(self, painter: QPainter, radius: int):
        # 绘制文字
        painter.save()
        painter.setPen(self.TextColor)
        painter.setFont(QFont('Arial', 15))
        strValue = '{}%'.format(int(self.Value / (self.MaxValue - self.MinValue)
                                    * 100)) if self.ShowPercent else str(self.Value)
        painter.drawText(QRectF(-radius, -radius, radius * 2,
                                radius * 2), Qt.AlignCenter, strValue)
        painter.restore()

    @pyqtProperty(int)
    def minValue(self) -> int:
        return self.MinValue

    @minValue.setter
    def minValue(self, minValue: int):
        if self.MinValue != minValue:
            self.MinValue = minValue
            self.update()

    @pyqtProperty(int)
    def maxValue(self) -> int:
        return self.MaxValue

    @maxValue.setter
    def maxValue(self, maxValue: int):
        if self.MaxValue != maxValue:
            self.MaxValue = maxValue
            self.update()

    @pyqtProperty(int)
    def value(self) -> int:
        return self.Value

    @value.setter
    def value(self, value: int):
        if self.Value != value:
            self.Value = value
            self.update()

    @pyqtProperty(float)
    def borderWidth(self) -> float:
        return self.BorderWidth

    @borderWidth.setter
    def borderWidth(self, borderWidth: float):
        if self.BorderWidth != borderWidth:
            self.BorderWidth = borderWidth
            self.update()

    @pyqtProperty(bool)
    def clockwise(self) -> bool:
        return self.Clockwise

    @clockwise.setter
    def clockwise(self, clockwise: bool):
        if self.Clockwise != clockwise:
            self.Clockwise = clockwise
            self.update()

    @pyqtProperty(bool)
    def showPercent(self) -> bool:
        return self.ShowPercent

    @showPercent.setter
    def showPercent(self, showPercent: bool):
        if self.ShowPercent != showPercent:
            self.ShowPercent = showPercent
            self.update()

    @pyqtProperty(bool)
    def showFreeArea(self) -> bool:
        return self.ShowFreeArea

    @showFreeArea.setter
    def showFreeArea(self, showFreeArea: bool):
        if self.ShowFreeArea != showFreeArea:
            self.ShowFreeArea = showFreeArea
            self.update()

    @pyqtProperty(bool)
    def showSmallCircle(self) -> bool:
        return self.ShowSmallCircle

    @showSmallCircle.setter
    def showSmallCircle(self, showSmallCircle: bool):
        if self.ShowSmallCircle != showSmallCircle:
            self.ShowSmallCircle = showSmallCircle
            self.update()

    @pyqtProperty(QColor)
    def textColor(self) -> QColor:
        return self.TextColor

    @textColor.setter
    def textColor(self, textColor: QColor):
        if self.TextColor != textColor:
            self.TextColor = textColor
            self.update()

    @pyqtProperty(QColor)
    def borderColor(self) -> QColor:
        return self.BorderColor

    @borderColor.setter
    def borderColor(self, borderColor: QColor):
        if self.BorderColor != borderColor:
            self.BorderColor = borderColor
            self.update()

    @pyqtProperty(QColor)
    def backgroundColor(self) -> QColor:
        return self.BackgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: QColor):
        if self.BackgroundColor != backgroundColor:
            self.BackgroundColor = backgroundColor
            self.update()

    def setValue(self, value):
        self.value = value

    def sizeHint(self) -> QSize:
        return QSize(50, 50)




# 主窗口
class MyPyQT_Form(QDialog, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()

        self.setupUi(self)

        sys.stdout = EmittingStr(textWritten=self.outputWritten)
        sys.stderr = EmittingStr(textWritten=self.outputWritten)

        # dialog相关
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        # 窗体隐藏
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 取消空隙
        self.verticalLayout.setSpacing(0)

        # self.widget.setStyleSheet(Widget_Stylesheet)

        '''# 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)'''

        # 文件树相关
        self.all_folder_tree_list = []

        self.page_config()

        self.main_page()
        self.download_page()
        self.offline_page()
        self.about_page()
        self.check_networl_call()
        self.the_trash_page()

        markdown_text = self.textBrowser.toPlainText()
        self.textBrowser.setMarkdown(markdown_text)

        #粘贴列表
        self.paste_type = True
        self.paste_id_list = []

        self.download_list = []

        self.my_info = True

        #悬浮图片
        self.Mouse_maintable_Worker = None

        self.thread_task_list = []

        # 排序依据
        self.orderType = Qt.DescendingOrder



        # 窗口最大化
        self.is_min = True

        #判断鼠标table悬停
        self.check_mouse_table_list = []
        self.check_mouse_offtable_list = []
        self.check_trash_table_list = []

        self.exitapppushButton.clicked.connect(self.start_exit_app)
        self.tohidepushButton.clicked.connect(self.showMinimized)
        self.pushMaxButton.clicked.connect(self.start_max_min)
        # 窗口淡化动画


        self.my_print()
        self.show_download_html()

       ###

    #输出到控制台

    #输出到输出台
    def outputWritten(self, text):
        with open('log.txt', 'a+') as f:  # 设置文件对象
            f.write(text)  # 将字符串写入文件中
            f.close()
        cursor = self.outprint_textBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)


        text = str(text).replace(
            "INFO", f"<br><font color=\"#01B468\">INFO</font>"
        ).replace(
            "Info",f"<br><font color=\"#01B468\">INFO</font>").replace(
            "Error",f"<br><font color=\"#FF2D2D\">Error</font>"
        )
        #cursor.insertText(text)
        cursor.insertHtml(text)
        self.outprint_textBrowser.setTextCursor(cursor)


        self.outprint_textBrowser.ensureCursorVisible()


    def my_print(self):


        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"Info ({new_time}):软件启动")
        if app_config['Proxy_type'] == "socks5":


            print(f"Info ({new_time}):使用sockes5代理")
        elif app_config['Proxy_type'] == "socks4":

            print(f"Info ({new_time}):使用sockes4代理")

        elif app_config['Proxy_type'] == "http":

            print(f"Info ({new_time}):使用sockes4代理")
        else:
            print(f"Info ({new_time}):不使用代理")

        if app_config['Nginx_url'] == "":
            pikpak_api_url = "https://api-drive.mypikpak.com"
            print(f"Info ({new_time}):使用官方api:{pikpak_api_url}")
        else:
            pikpak_api_url = app_config['Nginx_url']
            print(f"Info ({new_time}):使用自定义反代api:{pikpak_api_url}")

        if app_config['User_url'] == "":
            pikpak_user_url = "https://user.mypikpak.com"
            print(f"Info ({new_time}):使用官方api:{pikpak_user_url}")
        else:
            pikpak_user_url = app_config['User_url']
            print(f"Info ({new_time}):使用自定义反代api:{pikpak_user_url}")

    # 最大化
    def start_max_min(self):
        if self.is_min:
            self.showMaximized()
            self.is_min = False
        else:
            self.showNormal()
            self.is_min = True

    def paintEvent(self, event):
        # 透明背景但是需要留下一个透明度用于鼠标捕获
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(255, 255, 255, 1))

    # 鼠标移动事件
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    ###

    # 窗口淡化动画
    def doShow(self):
        try:
            # 尝试先取消动画完成后关闭窗口的信号
            self.animation.finished.disconnect(self.close)
        except:
            pass
        self.animation.stop()
        # 透明度范围从0逐渐增加到1
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def doClose(self):
        self.animation.stop()
        self.animation.finished.connect(self.close)  # 动画完成则关闭窗口
        # 透明度范围从1逐渐减少到0
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.start()


    def show_download_html(self):


        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.page().profile().setHttpAcceptLanguage("zh-CN,zh;q=0.9,en;q=0.8")
        self.browser.load(QUrl('file:///index.html#!/settings/rpc/set/http/127.0.0.1/29385/jsonrpc/cGlrcGFrZG93bg=='))
        self.verticalLayout_13.addWidget(self.browser)






    #回收站鼠标悬停,信号
    def choose_trash_tableWidget_back(self, result):
        row, column, img_html = result
        try:
            if column == 0:
                self.trash_tableWidget.item(row, column).setToolTip(img_html)
        except Exception as e:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):修改item线程错误:{e}")

    #回收站鼠标悬停,调用线程
    def choose_trash_tableWidget_call(self, row, column):

        img_url = self.trash_tableWidget.item(row,4).text()

        if img_url not in self.check_trash_table_list:
            if img_url!="" and column==0:
                try:
                    the_Mouse_maintable_Worker = Mouse_maintable_Worker(parent=self,row=row,column=column,img_url=img_url)
                    the_Mouse_maintable_Worker.valueChanged.connect(self.choose_trash_tableWidget_back)
                    the_Mouse_maintable_Worker.start()
                    self.thread_task_list.append(the_Mouse_maintable_Worker)
                    self.check_trash_table_list.append(img_url)
                except Exception as e:
                    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    print(f"Error ({new_time}):调用鼠标线程错误:{e}")


    # 清空回收站界面table
    def clear_trash_table(self):
        self.trash_tableWidget.clear()
        self.trash_tableWidget.setColumnCount(0)  # 设置列数
        self.trash_tableWidget.setRowCount(0)  # 设置列数

        titles = ['文件名称', '大小', "删除时间", "ID", "thumbnail_link"]

        self.trash_tableWidget.setColumnCount(5)  # 设置列数
        self.trash_tableWidget.hideColumn(3)  # 隐藏指定列
        self.trash_tableWidget.hideColumn(4)  # 隐藏指定列
        self.trash_tableWidget.setHorizontalHeaderLabels(titles)  # 标题列---水平标题

        #
        self.trash_tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选中行

        # 鼠标悬停
        self.trash_tableWidget.setMouseTracking(True)  # 设置跟踪鼠标
        self.trash_tableWidget.cellEntered.connect(self.choose_trash_tableWidget_call)  # 绑定自定义函数

        # QTableWidget.resizeColumnsToContents(self.trash_tableWidget)
        self.trash_tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.trash_tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # 设置列宽的适应方式
        self.trash_tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.trash_tableWidget.setColumnWidth(1, 120)  # 设置某列的宽度
        self.trash_tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.trash_tableWidget.setColumnWidth(2, 150)  # 设置某列的宽度


        self.trash_tableWidget.setStyleSheet(QScrollBar_style)

    #刷新回收站，信号
    def start_get_trash_back(self,result):
        for a in result:

            row_cnt = self.trash_tableWidget.rowCount()
            it_name = QtWidgets.QTableWidgetItem(a["name"])
            it_name.setToolTip(str(a["name"]))

            it_name.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 给指定单元格设置对齐方式

            pixmap = QPixmap()
            pixmap.loadFromData(a['icon_content'])
            icon = QIcon(pixmap)

            it_name.setIcon(icon)

            it_size = QtWidgets.QTableWidgetItem(hum_convert(a["size"]))
            it_size.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式


            it_time = QtWidgets.QTableWidgetItem(self.start_get_thetime(a["delete_time"]))
            it_time.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式

            it_id = QtWidgets.QTableWidgetItem(a["id"])
            it_id.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式

            img_url = QTableWidgetItem(a["thumbnail_link"])  # 创建表格项---文本项目
            img_url.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式

            self.trash_tableWidget.insertRow(row_cnt)

            for c, item in enumerate((it_name, it_size,  it_time, it_id, img_url)):
                self.trash_tableWidget.setItem(row_cnt, c, item)
            self.trash_tableWidget.setRowHeight(row_cnt, 50)
        if wait_screen.isVisible():
            wait_screen.close()

    #刷新回收站线程
    def start_get_trash_call(self):

        self.show_loading()
        self.clear_trash_table()
        # 滚动条样式

        self.trash_Thread = trash_Thread()
        self.trash_Thread.refresh_proess_signal.connect(self.start_get_trash_back)
        self.trash_Thread.start()


    #删除回收站文件线程调用
    def start_delete_trash_call(self):

        row_list = []


        for i in self.trash_tableWidget.selectionModel().selection().indexes():
            row_list.append(i.row())
        row_list = list(dict.fromkeys(row_list))
        if len(row_list)==0:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):未选中删除文件")
            return
        file_id_list= []
        for a in row_list:

            file_id = self.trash_tableWidget.item(a, 3).text()

            file_id_list.append(file_id)


        self.Delete_trash_Worker = Delete_trash_Worker(file_id=file_id_list)
        self.Delete_trash_Worker.valueChanged.connect(self.start_delete_trash_back)
        self.Delete_trash_Worker.start()

    # 删除回收站文件线程信号
    def start_delete_trash_back(self,result):
        self.start_get_trash_call()

    #还原文件信号
    def start_back_trash_back(self):
        self.start_get_trash_call()

    #还原文件调用
    def start_back_trash_call(self):

        row_list = []
        for i in self.trash_tableWidget.selectionModel().selection().indexes():
            row_list.append(i.row())
        row_list = list(dict.fromkeys(row_list))
        if len(row_list)==0:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):未选中删除文件")
            return
        file_id_list= []
        for a in row_list:

            file_id = self.trash_tableWidget.item(a, 3).text()

            file_id_list.append(file_id)


        self.Back_trash_Worker = Back_trash_Worker(file_id=file_id_list)
        self.Back_trash_Worker.valueChanged.connect(self.start_back_trash_back)
        self.Back_trash_Worker.start()

    # 回收站列表右键
    def trash_Menu(self, pos):


        main_menu = QMenu()
        main_menu.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框、去掉自带阴影
        main_menu.setWindowFlags(
            main_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        main_menu.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框、去掉自带阴影

        item0 = main_menu.addAction(QIcon(":/pic/src/还原.png"), u"还原文件")
        item1 = main_menu.addAction(QIcon(":/pic/src/删除.png"), u"删除文件")


        action = main_menu.exec_(self.trash_tableWidget.mapToGlobal(pos))

        if action == item1:
            self.start_delete_trash_call()

        elif action == item0:
            self.start_back_trash_call()


    #回收站页面
    def the_trash_page(self):
        self.clear_trash_table()
        self.refresh_trash_pushButton.clicked.connect(self.start_get_trash_call)
        self.delete_trahs_pushButton.clicked.connect(self.start_delete_trash_call)
        self.back_trash_pushButton.clicked.connect(self.start_back_trash_call)

        conLayout = QHBoxLayout()
        self.trash_tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.trash_tableWidget.customContextMenuRequested.connect(self.trash_Menu)  ####右键菜单
        self.trash_tableWidget.setLayout(conLayout)

    # 时间处理
    def start_get_thetime(self, timeamp):
        timeamp = str(timeamp)
        time1 = timeamp.split("T")[0]
        if "." in timeamp:
            time2 = str(timeamp.split("T")[1]).split(".")[0]
        else:
            time2 = str(timeamp.split("T")[1]).split("+")[0]
        return f"{time1} {time2}"

    #添加检查网络延迟进程
    def check_networl_call(self):
        self.Ping_networl_Worker = Ping_networl_Worker()
        self.Ping_networl_Worker.valueChanged.connect(self.check_network_back)
        self.Ping_networl_Worker.start()

    #接受ping值信号
    def check_network_back(self,num):
        if num==-1:
            self.pinginfo_label.setText(f"使用代理中")
            self.pinginfo_label.setStyleSheet("color:green")
        elif num==0:
            self.pinginfo_label.setText("超时")
            self.pinginfo_label.setStyleSheet("color:red")
        elif 0 < num and num <=100:
            self.pinginfo_label.setText(f"{num}ms")
            self.pinginfo_label.setStyleSheet("color:green")

        elif 100 < num and num <=200:
            self.pinginfo_label.setText(f"{num}ms")
            self.pinginfo_label.setStyleSheet("color:blue")

        else:
            self.pinginfo_label.setText(f"{num}ms")
            self.pinginfo_label.setStyleSheet("color:red")

    # 退出APP
    def start_exit_app(self):
        exit()

    # 离线下载界面
    def offline_page(self):

        self.clear_offline_table()
        self.offlinerefreshButton.clicked.connect(self.start_get_offline_status_call)
        self.addmagnetButton.clicked.connect(self.add_new_magnnet)
        conLayout = QHBoxLayout()
        self.offlineWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.offlineWidget.customContextMenuRequested.connect(self.off_Menu)  ####右键菜单
        self.offlineWidget.setLayout(conLayout)

    # 清空离线下载界面table
    def clear_offline_table(self):
        self.offlineWidget.clear()
        self.offlineWidget.setColumnCount(0)  # 设置列数
        self.offlineWidget.setRowCount(0)  # 设置列数

        titles = ['文件名称', '大小', '离线进度', "任务状态","更新时间", "ID","thumbnail_link"]

        self.offlineWidget.setColumnCount(7)  # 设置列数
        self.offlineWidget.hideColumn(5)  # 隐藏指定列
        self.offlineWidget.hideColumn(6)  # 隐藏指定列
        self.offlineWidget.setHorizontalHeaderLabels(titles)  # 标题列---水平标题

        #
        self.offlineWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选中行



        #鼠标悬停
        self.offlineWidget.setMouseTracking(True)  # 设置跟踪鼠标
        self.offlineWidget.cellEntered.connect(self.choose_offlineWidget_call)  # 绑定自定义函数

        # QTableWidget.resizeColumnsToContents(self.offlineWidget)
        self.offlineWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.offlineWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # 设置列宽的适应方式
        self.offlineWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.offlineWidget.setColumnWidth(1, 120)  # 设置某列的宽度
        self.offlineWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.offlineWidget.setColumnWidth(2, 100)  # 设置某列的宽度
        self.offlineWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.offlineWidget.setColumnWidth(3, 150)  # 设置某列的宽度

        self.offlineWidget.setStyleSheet(QScrollBar_style)

    def start_delete_task_back(self,result):
        self.start_get_offline_status_call()

    # 离线下载列表右键
    def off_Menu(self, pos):
        # rint( pos)
        row_num = -1
        row_list = []
        for i in self.offlineWidget.selectionModel().selection().indexes():
            row_list.append(i.row())

        row_list = list(dict.fromkeys(row_list))

        if len(row_list) == 1:

            row_num = row_list[0]
            Multiple_choice = False
        else:

            Multiple_choice = True

        main_menu = QMenu()
        main_menu.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框、去掉自带阴影
        main_menu.setWindowFlags(
            main_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        main_menu.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框、去掉自带阴影


        item1 = main_menu.addAction(QIcon(":/pic/src/删除.png"), u"删除任务")


        action = main_menu.exec_(self.offlineWidget.mapToGlobal(pos))

        if action == item1:
            if Multiple_choice:

                file_id_list = []
                for a in row_list:

                    file_id = self.offlineWidget.item(a, 5).text()
                    file_id_list.append(file_id)

                self.Delete_task_Worker = Delete_task_Worker(file_id=file_id_list)
                self.Delete_task_Worker.valueChanged.connect(self.start_delete_task_back)
                self.Delete_task_Worker.start()

            else:

                file_id = self.offlineWidget.item(row_num, 5).text()
                self.Delete_task_Worker = Delete_task_Worker(file_id=[file_id])
                self.Delete_task_Worker.valueChanged.connect(self.start_delete_task_back)
                self.Delete_task_Worker.start()


    # 刷新离线下载,回调信号
    def start_get_offline_status_back(self,result):
        for a in result:

            row_cnt = self.offlineWidget.rowCount()
            it_name = QtWidgets.QTableWidgetItem(a["name"])
            it_name.setToolTip(str(a["name"]))

            it_name.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 给指定单元格设置对齐方式


            pixmap = QPixmap()
            pixmap.loadFromData(a['icon_content'])
            icon = QIcon(pixmap)

            it_name.setIcon(icon)

            it_size = QtWidgets.QTableWidgetItem(hum_convert(a["file_size"]))
            it_size.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式

            it_status = QtWidgets.QTableWidgetItem(a["message"])
            it_status.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式

            it_progress = PercentProgressBar(self.downloadtableWidget, styleSheet="""
            qproperty-textColor: rgb(223,86,89);
            qproperty-borderColor: #FF9797;
            qproperty-backgroundColor: white;
            
            """)

            it_progress.setValue(int(a["progress"]))
            # self.progressBar.setObjectName("progressBar")

            it_time = QtWidgets.QTableWidgetItem(self.start_get_thetime(a["updated_time"]))
            it_time.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式

            it_id = QtWidgets.QTableWidgetItem(a["id"])
            it_id.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式


            if a["reference_resource"]["thumbnail_link"]!="":
                img_url = QTableWidgetItem(a["reference_resource"]["thumbnail_link"])  # 创建表格项---文本项目
                img_url .setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
            else:
                img_url = QTableWidgetItem("")  # 创建表格项---文本项目
                img_url .setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式

            self.offlineWidget.insertRow(row_cnt)

            for c, item in enumerate((it_name, it_size, it_progress, it_status,it_time, it_id,img_url)):
                if c == 2:
                    self.offlineWidget.setCellWidget(row_cnt, c, item)
                else:

                    self.offlineWidget.setItem(row_cnt, c, item)
            self.offlineWidget.setRowHeight(row_cnt, 50)
        if wait_screen.isVisible():
                wait_screen.close()

    # 刷新离线下载,调用线程
    def start_get_offline_status_call(self):
        self.show_loading()
        self.clear_offline_table()
        # 滚动条样式


        self.offline_Thread = offline_Thread()
        self.offline_Thread.refresh_proess_signal.connect(self.start_get_offline_status_back)
        self.offline_Thread.start()

    # table鼠标悬停,接受信号
    def choose_offlineWidget_back(self,result):
        row ,column ,img_html =result
        try:
            if column==0:
                self.offlineWidget.item(row,column).setToolTip(img_html)
        except Exception as e:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):修改item线程错误:{e}")


    #离线页面table鼠标悬停,调用线程
    def choose_offlineWidget_call(self, row, column):
        try:
            img_url = self.offlineWidget.item(row,6).text()
        except:
            return

        if img_url not in self.check_mouse_offtable_list:
            if img_url!=""  and column==0 :
                try:
                    the_Mouse_offlineWidget_Worker = Mouse_maintable_Worker(parent=self,row=row,column=column,img_url=img_url)
                    the_Mouse_offlineWidget_Worker.valueChanged.connect(self.choose_offlineWidget_back)
                    the_Mouse_offlineWidget_Worker.start()
                    self.thread_task_list.append(the_Mouse_offlineWidget_Worker)
                    self.check_mouse_offtable_list.append(img_url)

                except Exception as e:


                    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    print(f"Error ({new_time}):调用鼠标线程错误:{e}")



    # 关于界面
    def about_page(self):
        # self.textEdit.setStyleSheet("QTextEdit{background-color: rgb(85, 0, 0);}")
        self.visitmeButton.clicked.connect(self.visit_author_site)
        self.visitpikpakButton.clicked.connect(self.visit_pikpak_site)

    # 访问作者博客
    def visit_author_site(self):
        QDesktopServices.openUrl(QUrl("https://weinb.top"))

    # 访问官方群
    def visit_pikpak_site(self):
        QDesktopServices.openUrl(QUrl("https://t.me/pikpak_userservice"))


    def add_magnet_back(self,result):
        #self.start_get_offline_status_call()
        self.Add_magnet_Worker = Add_magnet_Worker(result)

        self.Add_magnet_Worker.start()



    # 添加新磁力弹框
    def add_new_magnnet(self):
        self.newDialog = MyMagnet_Form()
        self.newDialog.show()
        self.newDialog._signal.connect(self.add_magnet_back)

    # 下载管理界面
    def download_page(self):
        self.downloadtableWidget.clear()

        conLayout = QHBoxLayout()
        self.downloadtableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.downloadtableWidget.customContextMenuRequested.connect(self.download_Menu)  ####右键菜单
        self.downloadtableWidget.setLayout(conLayout)

        titles = ['任务名称', '大小', "状态", "速度", '进度',"文件地址"]
        # self.table = QTableWidget(4,3,self)  #创建4行3列的表格
        # self.tableWidget.setRowCount(9)  # 设置行数--不包括标题列
        self.downloadtableWidget.setColumnCount(6)  # 设置列数
        self.downloadtableWidget.setHorizontalHeaderLabels(titles)  # 标题列---水平标题
        self.downloadtableWidget.hideColumn(5)  # 隐藏指定列
        #
        self.downloadtableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选中行

        # QTableWidget.resizeColumnsToContents(self.tableWidget)
        self.downloadtableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.downloadtableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # 设置列宽的适应方式
        self.downloadtableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.downloadtableWidget.setColumnWidth(1, 200)  # 设置某列的宽度
        self.downloadtableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.downloadtableWidget.setColumnWidth(2, 90)  # 设置某列的宽度
        self.downloadtableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.downloadtableWidget.setColumnWidth(3, 130)  # 设置某列的宽度
        self.downloadtableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.downloadtableWidget.setColumnWidth(4, 100)  # 设置某列的宽度

    # 获取信号向进度条添加下载任务
    def add_download_to_pro(self, info_list):
        down_name, down_url, file_size, the_filesize, down_path = info_list



        #### 创建下载线程
        self.downloadThread = downloadThread(url=down_url, filesize=the_filesize, file_name=down_name, buffer=10240,down_path=down_path)
        self.downloadThread.start()
        self.download_list.append(self.downloadThread)


    # 下载列表右键
    def download_Menu(self, pos):
        # rint( pos)
        row_num = -1
        row_list = []
        for i in self.downloadtableWidget.selectionModel().selection().indexes():
            row_list.append(i.row())

        row_list = list(dict.fromkeys(row_list))



        down_menu = QMenu()
        # 背景透明
        down_menu.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框、去掉自带阴影
        down_menu.setWindowFlags(
            down_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        item1 = down_menu.addAction(QIcon(":/pic/src/开始.png"), u"开始")
        item2 = down_menu.addAction(QIcon(":/pic/src/暂停.png"), u"暂停")
        item3 = down_menu.addAction(QIcon(":/pic/src/删除.png"), u"删除")
        item4 = down_menu.addAction(QIcon(":/pic/src/文件夹.png"), u"打开文件夹")
        action = down_menu.exec_(self.downloadtableWidget.mapToGlobal(pos))

        if action == item1:
            for a in row_list:

                self.download_list[int(a)].resume()

        elif action == item2:
            for a in row_list:

                self.download_list[int(a)].pause()

        elif action == item3:
            for a in row_list:

                self.download_list[int(a)].remove()

        elif action == item4:

            row_num = int(row_list[0])

            download_path = self.downloadtableWidget.item(row_num, 5).text()
            if download_path != "":

                os.startfile(download_path)

    # 更新下载进度
    def set_progressbar_value(self, result):

        # self.progressBar.setValue(value)
        value = result[0]
        row = result[1]
        speed = result[2]
        status = result[3]
        if len(result)==5:
            download_part = result[4]
            if value == -1:

                self.downloadtableWidget.item(int(row), 1).setText("任务已删除")
            else:

                self.downloadtableWidget.cellWidget(int(row), 4).setValue(int(value))

                self.downloadtableWidget.item(int(row), 3).setText(str(speed))
                self.downloadtableWidget.item(int(row), 2).setText(status)
                self.downloadtableWidget.item(int(row), 1).setText(download_part)
            if value == 100:
                name = self.downloadtableWidget.item(int(row), 0).text()
                NotificationWindow.success('提示', f'{name} 任务完成')
        else:
            if value == -1:

                self.downloadtableWidget.item(int(row), 1).setText("任务已删除")
            else:

                self.downloadtableWidget.cellWidget(int(row), 4).setValue(int(value))

                self.downloadtableWidget.item(int(row), 3).setText(str(speed))
                self.downloadtableWidget.item(int(row), 2).setText(status)

            if value == 100:
                name = self.downloadtableWidget.item(int(row), 0).text()
                NotificationWindow.success('提示', f'{name} 任务完成')

    # 主页右键菜单项
    def generateMenu(self, pos):
        # rint( pos)
        row_num = -1
        row_list = []
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_list.append(i.row())

        row_list = list(dict.fromkeys(row_list))

        if len(row_list) == 1:

            row_num = row_list[0]
            Multiple_choice = False
        else:

            Multiple_choice = True

        main_menu = QMenu()

                # 背景透明
        main_menu.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框、去掉自带阴影
        main_menu.setWindowFlags(
            main_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)

        #二级菜单
        small_menu = QMenu('文件操作', main_menu)
        small_menu.setIcon(QIcon(":/pic/src/pikpak.png"))
        # 背景透明
        small_menu.setAttribute(Qt.WA_TranslucentBackground)
        # 无边框、去掉自带阴影
        small_menu.setWindowFlags(small_menu.windowFlags() | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        move_item =small_menu.addAction( QIcon(":/pic/src/剪切.png"),'剪切')
        copy_item =small_menu.addAction(QIcon(":/pic/src/复制.png"), '复制')
        delete_item = small_menu.addAction(QIcon(":/pic/src/删除.png"),'删除')
        rename_item = small_menu.addAction(QIcon(":/pic/src/重命名.png"),'重命名')



        main_menu.addMenu( small_menu)

        item1 = main_menu.addAction(QIcon(":/pic/src/下载.png"), u"本地下载")
        #:/pic/src/Thunder11.ico
        item2 = main_menu.addAction(QIcon(":/pic/src/Thunder11-0.png"), u"发送到迅雷")
        item3 = main_menu.addAction(QIcon(":/pic/src/potplayer.png"), u"推送Potplayer")
        item4 = main_menu.addAction(QIcon(":/pic/src/IDM.jpg"), u"推送IDM")
        item5 = main_menu.addAction(QIcon(":/pic/src/aria2.png"), u"推送Aria2")
        #:/pic/src/复制.png
        item6 = main_menu.addAction(QIcon(":/pic/src/复制.png"), u"复制秒传链接")
        item7 = main_menu.addAction(QIcon(":/pic/src/复制.png"), u"复制下载链接")
        action = main_menu.exec_(self.tableWidget.mapToGlobal(pos))

        if action == item1:
            if Multiple_choice:

                file_id_list = []
                for a in row_list:

                    file_id = self.tableWidget.item(a, 3).text()
                    file_type = self.tableWidget.item(a, 4).text()
                    if file_type == "文件夹":
                        QMessageBox.information(self, "提示", "多选不支持文件夹")
                        return
                    file_id_list.append(file_id)

                for a in file_id_list:

                    self.Add_download_Worker = Add_download_Worker(a)
                    self.Add_download_Worker.valueChanged.connect(self.add_download_to_pro)
                    self.Add_download_Worker.start()
                    time.sleep(0.5)

            else:

                file_id = self.tableWidget.item(row_num, 3).text()


                self.Add_download_Worker = Add_download_Worker(file_id)
                self.Add_download_Worker.valueChanged.connect(self.add_download_to_pro)
                self.Add_download_Worker.start()

        elif action == item2:

            if Multiple_choice:

                file_id_list = []
                for a in row_list:

                    file_id = self.tableWidget.item(a, 3).text()
                    file_type = self.tableWidget.item(a, 4).text()
                    if file_type == "文件夹":
                        QMessageBox.information(self, "提示", "多选不支持文件夹")
                        return
                    file_id_list.append(file_id)
                t1 = threading.Thread(target=thread_Thunder, args=(file_id_list,))
                t1.start()
            else:

                file_id = self.tableWidget.item(row_num, 3).text()
                t1 = threading.Thread(target=thread_Thunder, args=(file_id,))
                t1.start()


        elif action == item3:
            if app_config['Potplayer_path'] == "":
                NotificationWindow.error('PikPakDown', "未设置路径")
                return
            if Multiple_choice:

                file_id_list = []
                for a in row_list:

                    file_id = self.tableWidget.item(a, 3).text()
                    file_type = self.tableWidget.item(a, 4).text()
                    if file_type == "文件夹":
                        QMessageBox.information(self, "提示", "多选不支持文件夹")
                        return
                    file_id_list.append(file_id)
                Pot = app_config['Potplayer_path']
                t1 = threading.Thread(target=thread_pot, args=(file_id_list, Pot))
                t1.start()
            else:

                file_id = self.tableWidget.item(row_num, 3).text()
                Pot = app_config['Potplayer_path']
                t1 = threading.Thread(target=thread_pot, args=(file_id, Pot,))
                t1.start()

        elif action == item4:
            if app_config['IDMplayer_path'] == "":
                NotificationWindow.error('PikPakDown', "未设置路径")
                return
            if Multiple_choice:

                file_id_list = []
                for a in row_list:

                    file_id = self.tableWidget.item(a, 3).text()
                    file_type = self.tableWidget.item(a, 4).text()
                    if file_type == "文件夹":
                        QMessageBox.information(self, "提示", "多选不支持文件夹")
                        return
                    file_id_list.append(file_id)
                IDM = app_config['IDMplayer_path']
                t1 = threading.Thread(target=thread_IDM, args=(file_id_list, IDM))
                t1.start()
            else:

                file_id = self.tableWidget.item(row_num, 3).text()
                IDM = app_config['IDMplayer_path']

                t1 = threading.Thread(target=thread_IDM, args=(file_id, IDM,))
                t1.start()

        elif action == item5:
            if Multiple_choice:

                file_id_list = []
                for a in row_list:

                    file_id = self.tableWidget.item(a, 3).text()
                    file_type = self.tableWidget.item(a, 4).text()
                    if file_type == "文件夹":
                        QMessageBox.information(self, "提示", "多选不支持文件夹")
                        return
                    file_id_list.append(file_id)

                t1 = threading.Thread(target=thread_aria2, args=(file_id_list,))
                t1.start()
            else:

                file_id = self.tableWidget.item(row_num, 3).text()

                t1 = threading.Thread(target=thread_aria2, args=(file_id,))
                t1.start()

        elif action == item6:
            if Multiple_choice:

                file_id_list = []
                text = ""
                for a in row_list:

                    file_type = self.tableWidget.item(a, 4).text()
                    if file_type == "文件夹":
                        QMessageBox.information(self, "提示", "多选不支持文件夹")
                        return

                    name = self.tableWidget.item(a, 0).text()
                    hash = self.tableWidget.item(a, 5).text()
                    size = self.tableWidget.item(a, 6).text()

                    share_hash = f"PikPak://{name}|{size}|{hash}"
                    text = text + share_hash + "\n"

                clipboard = QApplication.clipboard()

                clipboard.setText(text)
                NotificationWindow.success('PikPakDown', f'{len(row_list)}个文件 复制秒链成功')


            else:

                type = self.tableWidget.item(row_num, 4).text()
                folder_name = self.tableWidget.item(row_num, 0).text()

                text = ""
                num = 0
                if type == "文件夹":
                    folder_id = self.tableWidget.item(row_num, 3).text()
                    file_list = get_list(foder_id=folder_id)

                    for a in file_list:

                        if a['kind'] == "drive#file":
                            name = a['name']
                            hash = a['hash']
                            size = a['size']

                            share_hash = f"PikPak://{name}|{size}|{hash}"
                            text = text + share_hash + "\n"
                            num = num + 1

                    clipboard = QApplication.clipboard()

                    clipboard.setText(text)
                    NotificationWindow.success('PikPakDown', f'{folder_name} 文件夹\n'
                                                             f'{num}子文件复制秒链成功')

                else:
                    name = self.tableWidget.item(row_num, 0).text()
                    hash = self.tableWidget.item(row_num, 5).text()
                    size = self.tableWidget.item(row_num, 6).text()

                    share_hash = f"PikPak://{name}|{size}|{hash}"

                    clipboard = QApplication.clipboard()

                    clipboard.setText(share_hash)
                    NotificationWindow.success('PikPakDown', f'{name} 复制秒链成功')

        elif action == item7:
            if Multiple_choice:

                file_id_list = []
                for a in row_list:

                    file_id = self.tableWidget.item(a, 3).text()
                    file_type = self.tableWidget.item(a, 4).text()
                    if file_type == "文件夹":
                        QMessageBox.information(self, "提示", "多选不支持文件夹")
                        return
                    file_id_list.append(file_id)


                self.Copy_downloadurl_Worker = Copy_downloadurl_Worker(file_id_list)
                self.Copy_downloadurl_Worker.valueChanged.connect(self.start_show_info)
                self.Copy_downloadurl_Worker.start()

            else:

                file_id = self.tableWidget.item(row_num, 3).text()


                self.Copy_downloadurl_Worker = Copy_downloadurl_Worker(file_id)
                self.Copy_downloadurl_Worker.valueChanged.connect(self.start_show_info)
                self.Copy_downloadurl_Worker.start()

        elif action == move_item:

            self.start_move_file()

        elif action == copy_item:

            self.start_copy_file()

        elif action == delete_item:

            self.start_delete_file_call()

        elif action == rename_item:

            if Multiple_choice:

                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"Error ({new_time}):多选不支持重命名")


            else:

                self.start_rename_call()


        else:
            return

    # 综合信号接收器
    def start_show_info(self, info_list):
        info_type = info_list[0]
        text = info_list[1]
        copy_text = info_list[2]

        if info_type == "success":
            clipboard = QApplication.clipboard()

            clipboard.setText(copy_text)
            NotificationWindow.success('PikPakDown', text)

    # 主页相关
    def main_page(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)  # 设置列数
        self.tableWidget.setRowCount(0)  # 设置列数

        self.filetreeWidget.clicked.connect(self.onTreeClicked)

        self.file_tree_wait()

        conLayout = QHBoxLayout()
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单
        self.tableWidget.setLayout(conLayout)

        titles = ['文件名称', '大小', '修改时间', "ID", "类型", "hash", "size"]

        self.tableWidget.setColumnCount(7)  # 设置列数
        self.tableWidget.setHorizontalHeaderLabels(titles)  # 标题列---水平标题
        self.tableWidget.hideColumn(3)  # 隐藏指定列
        self.tableWidget.hideColumn(4)  # 隐藏指定列
        self.tableWidget.hideColumn(5)  # 隐藏指定列
        self.tableWidget.hideColumn(6)  # 隐藏指定列


        # 设置表头颜色
        #self.tableWidget.setStyleSheet(HeaderView_style)

        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sort_by_item)

        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选中行

        # QTableWidget.resizeColumnsToContents(self.tableWidget)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # 设置列宽的适应方式
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.tableWidget.setColumnWidth(1, 120)  # 设置某列的宽度
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.tableWidget.setColumnWidth(2, 200)  # 设置某列的宽度

        self.tableWidget.doubleClicked.connect(self.start_double_click)

        self.refreshButton.clicked.connect(self.new_main_folder_call)

        self.backButton.clicked.connect(self.start_back_parfolder)
        self.uploadfileButton.clicked.connect(self.start_upload_file)
        self.sharegcidButton.clicked.connect(self.get_all_hash)
        self.addgcidButton.clicked.connect(self.start_add_hash)
        self.creat_folder_pushButton.clicked.connect(self.start_creat_new_folder)

        self.copy_file_pushButton.clicked.connect(self.start_copy_file)
        self.move_file_pushButton.clicked.connect(self.start_move_file)
        self.delete_file_pushButton.clicked.connect(self.start_delete_file_call)
        self.rename_pushButton.clicked.connect(self.start_rename_call)

    #重命名信号接收
    def start_rename_back_back(self, result):
        if result:
            self.new_main_folder_call()

        else:
            NotificationWindow.error('PikPakDown', f'重命名失败')
            self.delete_paste_button()
    #重命名
    def start_rename_back_call(self,result):

        file_id = result['file_id']
        name = result['name']

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):开始调用重命名请求，{name}")

        self.Rename_file_Worker =Rename_file_Worker(file_id=file_id,name=name)
        self.Rename_file_Worker.valueChanged.connect(self.start_rename_back_back)
        self.Rename_file_Worker.start()
    #重命名
    def start_rename_call(self):
        row_list = []

        for i in self.tableWidget.selectionModel().selection().indexes():
            row_list.append(i.row())
        row_list = list(dict.fromkeys(row_list))
        if len(row_list) == 0:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):重命名未选中文件")
            return
        elif len(row_list) == 1:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):重命名未选中文件")
            file_id = self.tableWidget.item(row_list[0], 3).text()

            self.rename_file_Dialog = Rename_file_Form(file_id=file_id)
            self.rename_file_Dialog.show()
            self.rename_file_Dialog._signal.connect(self.start_rename_back_call)
        else:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):重命名不支持多选")



    #删除文件线程调用
    def start_delete_file_call(self):

        row_list = []


        for i in self.tableWidget.selectionModel().selection().indexes():
            row_list.append(i.row())
        row_list = list(dict.fromkeys(row_list))
        if len(row_list)==0:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):未选中删除文件")
            return
        file_id_list= []
        for a in row_list:

            file_id = self.tableWidget.item(a, 3).text()


            file_id_list.append(file_id)

            for b in range(len(self.all_folder_tree_list)):

                if str(self.all_folder_tree_list[b]['id']) == str(file_id):
                    del self.all_folder_tree_list[b]
                    break


        self.Delete_file_Worker = Delete_file_Worker(file_id=file_id_list)
        self.Delete_file_Worker.valueChanged.connect(self.start_delete_file_back)
        self.Delete_file_Worker.start()

    def start_delete_file_back(self,result):
        self.new_main_folder_call()


    #开始剪切文件
    def start_move_file(self):
        row_list = []
        self.paste_type=False

        for i in self.tableWidget.selectionModel().selection().indexes():
            row_list.append(i.row())
        row_list = list(dict.fromkeys(row_list))
        if len(row_list)==0:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):未选中剪切文件")
            return
        file_id_list= []
        for a in row_list:

            file_id = self.tableWidget.item(a, 3).text()


            file_id_list.append(file_id)


        self.paste_id_list = file_id_list

        _translate = QtCore.QCoreApplication.translate
        self.paste_file_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.paste_file_pushButton.setStyleSheet("")
        self.paste_file_pushButton.setObjectName("paste_file_pushButton")
        self.gridLayout_8.addWidget(self.paste_file_pushButton, 1, 4, 1, 1)
        self.paste_file_pushButton.setText(_translate("Form", f"粘贴文件({len(file_id_list)})"))

        self.del_paste_file_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.del_paste_file_pushButton.setStyleSheet("")
        self.del_paste_file_pushButton.setObjectName("del_paste_file_pushButton")
        self.gridLayout_8.addWidget(self.del_paste_file_pushButton, 1, 5, 1, 1)
        self.del_paste_file_pushButton.setText(_translate("Form", "取消粘贴"))

        self.del_paste_file_pushButton.clicked.connect(self.delete_paste_button)
        self.paste_file_pushButton.clicked.connect(self.paste_file_call)


    #开始复制文件
    def start_copy_file(self):
        row_list = []
        self.paste_type=True

        for i in self.tableWidget.selectionModel().selection().indexes():
            row_list.append(i.row())
        row_list = list(dict.fromkeys(row_list))
        if len(row_list)==0:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):未选中复制文件")
            return
        file_id_list= []
        for a in row_list:

            file_id = self.tableWidget.item(a, 3).text()


            file_id_list.append(file_id)


        self.paste_id_list = file_id_list

        _translate = QtCore.QCoreApplication.translate
        self.paste_file_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.paste_file_pushButton.setStyleSheet("")
        self.paste_file_pushButton.setObjectName("paste_file_pushButton")
        self.gridLayout_8.addWidget(self.paste_file_pushButton, 1, 4, 1, 1)
        self.paste_file_pushButton.setText(_translate("Form", f"粘贴文件({len(file_id_list)})"))

        self.del_paste_file_pushButton = QtWidgets.QPushButton(self.widget_3)
        self.del_paste_file_pushButton.setStyleSheet("")
        self.del_paste_file_pushButton.setObjectName("del_paste_file_pushButton")
        self.gridLayout_8.addWidget(self.del_paste_file_pushButton, 1, 5, 1, 1)
        self.del_paste_file_pushButton.setText(_translate("Form", "取消粘贴"))

        self.del_paste_file_pushButton.clicked.connect(self.delete_paste_button)
        self.paste_file_pushButton.clicked.connect(self.paste_file_call)

    #粘贴文件，回调
    def paste_file_back(self,result):
        if result:
            self.new_main_folder_call()
            self.delete_paste_button()

        else:
            NotificationWindow.error('PikPakDown', f'粘贴失败')
            self.delete_paste_button()

    #粘贴文件线程
    def paste_file_call(self):


        now_path = self.root_label.text()
        for a in self.all_folder_tree_list:
            if now_path == f"{a['path']}/{a['name']}":
                to_id = a['id']

                break
        else:
            to_id = ""

        paste_type=self.paste_type
        folder_id = self.paste_id_list
        for a in self.paste_id_list:
            for b in range(len(self.all_folder_tree_list)):

                if str(self.all_folder_tree_list[b]['id']) == str(a):
                    del self.all_folder_tree_list[b]
                    break

        self.Paste_file_Worker = Paste_file_Worker(folder_id=folder_id,to_id=to_id,paste_type=paste_type)
        self.Paste_file_Worker.valueChanged.connect(self.paste_file_back)
        self.Paste_file_Worker.start()


    #取消复制、粘贴
    def delete_paste_button(self):
        self.paste_file_pushButton.deleteLater()
        self.del_paste_file_pushButton.deleteLater()

    #新建文件夹信号
    def creat_new_folder_back(self,result):
        if result:
            self.new_main_folder_call()

        else:
            NotificationWindow.error('PikPakDown', f'新建文件夹失败')

    #接收文件夹昵称,调用进程
    def creat_new_folder_call(self,name):

        now_path = self.root_label.text()
        for a in self.all_folder_tree_list:
            if now_path == f"{a['path']}/{a['name']}":
                folder_id = a['id']
                break
        else:
            folder_id = ""


        self.Creat_folder_Worker = Creat_folder_Worker(folder_id=folder_id,name=name)
        self.Creat_folder_Worker.valueChanged.connect(self.creat_new_folder_back)
        self.Creat_folder_Worker.start()


    #弹出新建文件夹子窗口
    def start_creat_new_folder(self):

        self.newfolderDialog = My_new_folder_Form()
        self.newfolderDialog.show()
        self.newfolderDialog._signal.connect(self.creat_new_folder_call)

    # 文件树点击事件
    def onTreeClicked(self, qmodelindex):
        self.show_loading()
        item = self.filetreeWidget.currentItem()

        if item.text(0) =="根目录":
            self.clear_table()

            # 滚动条样式
            self.tableWidget.setStyleSheet(QScrollBar_style)

            #### 创建刷新线程
            self.refreshThread = refreshThread(folder_id="")
            self.refreshThread.refresh_proess_signal.connect(self.new_main_folder_back)
            self.refreshThread.start()
            return

        if item.text(1) == "":
            return



        folder_id = item.text(1)


        # 更新路径
        self.root_label.setText(f"{item.text(2)}/{item.text(0)}")

        self.clear_table()

        # 滚动条样式
        self.tableWidget.setStyleSheet(QScrollBar_style)

        #### 创建刷新线程
        self.refreshThread = refreshThread(folder_id=folder_id)
        self.refreshThread.refresh_proess_signal.connect(self.new_main_folder_back)
        self.refreshThread.start()

    # 初始化文件树
    def file_tree_wait(self):
        # 设置列数
        self.filetreeWidget.clear()
        #self.filetreeWidget.setStyleSheet(QScrollBar_style)
        self.filetreeWidget.setColumnCount(2)

        # 设置头的标题
        self.filetreeWidget.setHeaderLabels(['文件名称', "ID", "path"])
        item_dict = {}
        self.filetreeWidget.hideColumn(1)
        self.filetreeWidget.hideColumn(2)
        # 设置根节点
        root = QTreeWidgetItem(self.filetreeWidget)
        root.setText(0, '根目录')
        item_dict['根目录'] = root
        # 设置列宽
        self.filetreeWidget.setColumnWidth(0, 150)


        # 列表去重
        run_function = lambda x, y: x if y in x else x + [y]
        self.all_folder_tree_list = reduce(run_function, [[], ] + self.all_folder_tree_list)

        for a in self.all_folder_tree_list:

            if a['path'] == "根目录":
                child1 = QTreeWidgetItem(item_dict['根目录'])
                child1.setText(0, a['name'])
                child1.setIcon(0, QIcon(":/pic/src/文件夹.png"))
                child1.setText(1, a['id'])
                child1.setText(2, a['path'])
                item_dict[f"{a['path']}/{a['name']}"] = child1
            elif a['path'] in item_dict:
                child1 = QTreeWidgetItem(item_dict[a['path']])
                child1.setText(0, a['name'])
                child1.setIcon(0, QIcon(":/pic/src/文件夹.png"))
                child1.setText(1, a['id'])
                child1.setText(2, a['path'])
                item_dict[f"{a['path']}/{a['name']}"] = child1

        temp_path = self.root_label.text()
        if temp_path != "根目录":
            self.filetreeWidget.expandItem(item_dict[temp_path])
        while temp_path != "根目录":
            del_path = temp_path[temp_path.rindex('/') + 1: len(temp_path)]
            temp_path = temp_path.replace(f"/{del_path}", "")

            self.filetreeWidget.expandItem(item_dict[temp_path])
        self.filetreeWidget.expandItem(root)

    # 文件目录排序
    def sort_by_item(self, index):

        if index == 1:


            index = 6
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.tableWidget.sortItems(index, self.orderType)

    # 打开秒链对话框
    def start_add_hash(self):
        self.newhashDialog = MyHash_Form()
        self.newhashDialog.show()
        self.newhashDialog._signal.connect(self.get_add_hash)

    # 获取返回的hash值,添加进程
    def get_add_hash(self, result):
        name_list = []
        size_list = []
        file_hash_list = []
        for a in result:
            info = re.findall("PikPak://(.*)", str(a), re.S)[0]
            info_list = str(info).split("|")
            name = info_list[0]
            size = info_list[1]
            file_hash = info_list[2]

            name_list.append(name)
            size_list.append(size)
            file_hash_list.append(file_hash)

        now_path = self.root_label.text()
        for a in self.all_folder_tree_list:
            if now_path == f"{a['path']}/{a['name']}":
                folder_id = a['id']
                break
        else:
            folder_id = ""

        self.Hash_Worker = Hash_Worker(name_list, size_list, file_hash_list, folder_id)
        self.Hash_Worker.valueChanged.connect(self.theat_add_hash)
        self.Hash_Worker.start()

    # 接受hash结束信号，提示信息
    def theat_add_hash(self, result):

        name = result[1]

        if result[0] == True:
            NotificationWindow.success('PikPakDown', f'{name} 秒传成功')
        else:
            NotificationWindow.error('PikPakDown', f'{name} 秒传失败')

    # 获取当前文件夹秒链
    def get_all_hash(self):
        row_cnt = self.tableWidget.rowCount()
        text = ""
        num = 0
        for a in range(1, row_cnt):

            file_type = self.tableWidget.item(a, 4).text()


            if file_type == "文件":
                name = self.tableWidget.item(a, 0).text()
                hash = self.tableWidget.item(a, 5).text()
                size = self.tableWidget.item(a, 6).text()

                share_hash = f"PikPak://{name}|{size}|{hash}"
                text = text + share_hash + "\n"
                num = num + 1

        clipboard = QApplication.clipboard()

        clipboard.setText(text)
        NotificationWindow.success('PikPakDown', f'{num}个文件 复制秒链成功')

    # 上传文件
    def start_upload_file(self):
        now_path = self.root_label.text()
        for a in self.all_folder_tree_list:
            if now_path == f"{a['path']}/{a['name']}":
                folder_id = a['id']
                break
        else:
            folder_id = ""

        openfile_name, file_type = QFileDialog.getOpenFileNames()
        if openfile_name == []:

            return
        file_path = openfile_name[0]
        file_name = os.path.basename(file_path)


        file_size = os.path.getsize(file_path)


        row_cnt = self.downloadtableWidget.rowCount()
        self.downloadtableWidget.insertRow(row_cnt)
        # 添加下载名称
        it_name = QtWidgets.QTableWidgetItem(file_name)
        it_name.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 给指定单元格设置对齐方式
        self.downloadtableWidget.setItem(row_cnt, 0, it_name)  # 给指定单元格设置数据

        # 添加下载文件大小
        it_size = QtWidgets.QTableWidgetItem(hum_convert(file_size))
        it_size.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
        self.downloadtableWidget.setItem(row_cnt, 1, it_size)  # 给指定单元格设置数据

        # 添加下载状态
        it_stasus = QtWidgets.QTableWidgetItem("即将上传")
        it_stasus.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
        self.downloadtableWidget.setItem(row_cnt, 2, it_stasus)  # 给指定单元格设置数据
        # 添加速度
        it_speed = QtWidgets.QTableWidgetItem("0kb")
        it_speed.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
        self.downloadtableWidget.setItem(row_cnt, 3, it_speed)  # 给指定单元格设置数据
        # 添加下载进度条
        progressBar = QtWidgets.QProgressBar(self.downloadtableWidget)
        progressBar.setStyleSheet(QProgressBar_StyleSheet)
        progressBar.setProperty("value", 0)
        # self.progressBar.setObjectName("progressBar")
        self.downloadtableWidget.setCellWidget(row_cnt, 4, progressBar)

        #### 创建上传线程
        self.uploadThread = uploadThread(file_path, folder_id, row_cnt)

        self.uploadThread.upload_proess_signal.connect(self.set_progressbar_value)
        self.uploadThread.start()
        self.download_list.append(self.uploadThread)


    # 刷新主页当前目录,信号
    def new_main_folder_back(self, file_list):


        for a in file_list:

            row_cnt = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_cnt)  # 尾部插入一行新行表格

            newItem = QTableWidgetItem(str(a["name"]))  # 创建表格项---文本项目

            newItem.setToolTip(str(a["name"]))
            newItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 给指定单元格设置对齐方式

            self.tableWidget.setRowHeight(row_cnt, 50)
            pixmap = QPixmap()

            #pixmap.loadFromData(self.start_choose_icon(icon_link))
            pixmap.loadFromData(a['icon_content'])
            icon = QIcon(pixmap)

            newItem.setIcon(icon)


            self.tableWidget.setItem(row_cnt, 0, newItem)  # 给指定单元格设置数据
            newItem = QTableWidgetItem(hum_convert(a["size"]))  # 创建表格项---文本项目
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式

            self.tableWidget.setItem(row_cnt, 1, newItem)  # 给指定单元格设置数据

            file_time = self.start_get_thetime(a["modified_time"])

            newItem = QTableWidgetItem(file_time)  # 创建表格项---文本项目

            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
            self.tableWidget.setItem(row_cnt, 2, newItem)  # 给指定单元格设置数据

            newItem = QTableWidgetItem(a["id"])  # 创建表格项---文本项目
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
            self.tableWidget.setItem(row_cnt, 3, newItem)  # 给指定单元格设置数据

            if a['kind'] == "drive#folder":
                newItem = QTableWidgetItem("文件夹")  # 创建表格项---文本项目
            else:
                newItem = QTableWidgetItem("文件")  # 创建表格项---文本项目
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
            self.tableWidget.setItem(row_cnt, 4, newItem)  # 给指定单元格设置数据

            newItem = QTableWidgetItem(a["hash"])  # 创建表格项---文本项目
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
            self.tableWidget.setItem(row_cnt, 5, newItem)  # 给指定单元格设置数据

            newItem = QTableWidgetItem()  # 创建表格项---文本项目
            # newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
            newItem.setData(QtCore.Qt.DisplayRole, int(a["size"]))
            self.tableWidget.setItem(row_cnt, 6, newItem)  # 给指定单元格设置数据

            newItem = QTableWidgetItem(a["thumbnail_link"])  # 创建表格项---文本项目
            newItem.setTextAlignment(Qt.AlignCenter | Qt.AlignTop)  # 给指定单元格设置对齐方式
            self.tableWidget.setItem(row_cnt, 7, newItem)  # 给指定单元格设置数据

            if a['kind'] == "drive#folder":
                now_path = self.root_label.text()
                self.all_folder_tree_list.append(
                    {
                        'name': str(a['name']),
                        "icon_link": a["icon_link"],
                        "id": a["id"],
                        "path": now_path
                    }
                )

        self.file_tree_wait()
        if wait_screen.isVisible():
            wait_screen.close()

    def get_my_quate_back(self,result):


        quate_text = f"容量使用:{hum_convert(int(result['quate']['quota']['usage']))}/{hum_convert(int(result['quate']['quota']['limit']))}"
        self.quota_label.setText(quate_text)


        self.quate_progressBar.setValue(int(int(result['quate']['quota']['usage'])/int(result['quate']['quota']['limit'])*100))
        vip_text = f"会员到期时间:{self.start_get_thetime(str(result['user']['data']['expire']))}"

        self.vip_time_label.setText(vip_text)


    # 刷新主页当前目录，进程
    def new_main_folder_call(self):
        self.show_loading()
        if self.my_info:
            self.Get_quate_task_Worker = Get_quate_task_Worker()
            self.Get_quate_task_Worker.valueChanged.connect(self.get_my_quate_back)
            self.Get_quate_task_Worker.start()
            self.my_info=False
        now_path = self.root_label.text()
        for a in self.all_folder_tree_list:
            if now_path == f"{a['path']}/{a['name']}":
                folder_id = a['id']
                break
        else:
            folder_id = ""

        self.clear_table()
        #### 创建主页刷新线程
        self.refreshThread = refreshThread(folder_id=folder_id)
        self.refreshThread.refresh_proess_signal.connect(self.new_main_folder_back)
        self.refreshThread.start()

        # file_list = get_list(folder_id)

    #主页table鼠标悬停,调用线程
    def choose_tableWidget_call(self, row, column):

        img_url = self.tableWidget.item(row,7).text()

        if img_url not in self.check_mouse_table_list:


            if img_url!="" and column==0:
                try:
                    the_Mouse_maintable_Worker = Mouse_maintable_Worker(parent=self,row=row,column=column,img_url=img_url)
                    the_Mouse_maintable_Worker.valueChanged.connect(self.choose_tableWidget_back)
                    the_Mouse_maintable_Worker.start()
                    self.thread_task_list.append(the_Mouse_maintable_Worker)
                    self.check_mouse_table_list.append(img_url)
                except Exception as e:
                    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    print(f"Error ({new_time}):调用鼠标线程错误:{e}")


    # table鼠标悬停,接受信号
    def choose_tableWidget_back(self,result):
        row ,column ,img_html =result
        try:
            if column == 0:
                self.tableWidget.item(row,column).setToolTip(img_html)
        except Exception as e:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):修改item线程错误:{e}")





    # 清空主页列表
    def clear_table(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)  # 设置列数
        self.tableWidget.setRowCount(0)  # 设置列数

        titles = ['文件名称', '大小', '修改时间', "ID", "类型", "hash", "size","thumbnail_link"]

        self.tableWidget.setColumnCount(8)  # 设置列数
        self.tableWidget.setHorizontalHeaderLabels(titles)  # 标题列---水平标题
        self.tableWidget.hideColumn(3)  # 隐藏指定列
        self.tableWidget.hideColumn(4)  # 隐藏指定列
        self.tableWidget.hideColumn(5)  # 隐藏指定列
        self.tableWidget.hideColumn(6)  # 隐藏指定列
        self.tableWidget.hideColumn(7)  # 隐藏指定列
        # 滚动条样式
        self.tableWidget.setStyleSheet(QScrollBar_style)

        #鼠标悬停
        self.tableWidget.setMouseTracking(True)  # 设置跟踪鼠标
        self.tableWidget.cellEntered.connect(self.choose_tableWidget_call)  # 绑定自定义函数




        #
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选中行

        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # 设置列宽的适应方式
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.tableWidget.setColumnWidth(1, 120)  # 设置某列的宽度
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)  # 设置列宽的适应方式
        self.tableWidget.setColumnWidth(2, 200)  # 设置某列的宽度


        # QTableWidget.resizeColumnsToContents(self.tableWidget)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    # 双击进入子文件夹
    def start_double_click(self, index):


        # table_column = index.column()
        table_row = index.row()

        folder_type = str(self.tableWidget.item(int(table_row), 4).text())

        if folder_type == "文件":

            file_id = self.tableWidget.item(int(table_row), 3).text()

            self.Mpv_video_Worker = Mpv_video_Worker(file_id=file_id)
            #self.Mpv_video_Worker.valueChanged.connect(self.choose_tableWidget_back)
            self.Mpv_video_Worker.start()

            return


        self.show_loading()
        folder_id = self.tableWidget.item(int(table_row), 3).text()


        # 更新路径
        folder_name = self.tableWidget.item(int(table_row), 0).text()
        now_path = self.root_label.text()

        self.root_label.setText(f"{now_path}/{folder_name}")

        self.clear_table()

        # 滚动条样式
        self.tableWidget.setStyleSheet(QScrollBar_style)

        now_path = self.root_label.text()
        for a in self.all_folder_tree_list:
            if now_path == f"{a['path']}/{a['name']}":
                folder_id = a['id']
                break
        else:
            folder_id = ""

        #### 创建下载线程
        self.refreshThread = refreshThread(folder_id=folder_id)
        self.refreshThread.refresh_proess_signal.connect(self.new_main_folder_back)
        self.refreshThread.start()

    # 显示加载动画
    def show_loading(self):


        rect = self.geometry()


        x_location = int(int(rect.left()) + int(rect.width()) * (1 / 3))
        y_location = int(int(rect.top()) + int(rect.height()) * (1 / 4))

        if not wait_screen.isVisible():
            wait_screen.show()
            wait_screen.move(x_location, y_location)


    # 返回上一级
    def start_back_parfolder(self):
        # 显示加载动画
        self.show_loading()



        # 获取上级路径
        temp_path = self.root_label.text()


        if temp_path!="根目录":
            del_path = temp_path[temp_path.rindex('/') + 1: len(temp_path)]
            num = temp_path.count(f"/{del_path}")-1
            if num==0:
                num=-1
            temp_path = temp_path.replace(f"/{del_path}", "",num)
            self.root_label.setText(temp_path)


        for a in self.all_folder_tree_list:
            if temp_path == f"{a['path']}/{a['name']}":
                folder_id = a['id']
                break
        else:
            folder_id = ""

        self.clear_table()

        #### 创建下载线程
        self.refreshThread = refreshThread(folder_id=folder_id)
        self.refreshThread.refresh_proess_signal.connect(self.new_main_folder_back)
        self.refreshThread.start()

    # 此部分为设置页相关
    def page_config(self):



        # 启动时插入配置
        self.user_lineEdit.setText(str(app_config['user']))
        self.password_lineEdit.setText(str(app_config['password']))
        self.Aria2_hostlineEdit.setText(str(app_config['Aria2_host']))
        self.Aria2_portlineEdit.setText(str(app_config['Aria2_port']))
        self.Aria2_secretlineEdit.setText(str(app_config['Aria2_secret']))
        self.Aria2_pathlineEdit.setText(str(app_config['Aria2_path']))
        self.Potplayer_pathlineEdit.setText(str(app_config['Potplayer_path']))
        self.IDMlineEdit.setText(str(app_config['IDMplayer_path']))
        self.localdownloadlineEdit.setText(str(app_config['Download_path']))
        self.webdav_adminlineEdit.setText(str(app_config['Webdav_admin']))
        self.webdav_passlineEdit.setText(str(app_config['Webdav_password']))
        self.webdav_portlineEdit.setText(str(app_config['Webdav_port']))
        try:
            for i in range(self.Proxy_type_comboBox.count()):
                if str(app_config['Proxy_type']) ==self.Proxy_type_comboBox.itemText(i):
                    comboBox = i
            self.Proxy_type_comboBox.setCurrentIndex(comboBox)
        except:
            self.Proxy_type_comboBox.setCurrentIndex(0)
        self.Proxy_ip_lineEdit.setText(str(app_config['Proxy_ip']))
        self.Proxy_port_lineEdit.setText(str(app_config['Proxy_port']))
        self.Proxy__admin_lineEdit.setText(str(app_config['Proxy_admin']))
        self.Proxy_pass_lineEdit.setText(str(app_config['Proxy_pass']))
        self.nginx_url_lineEdit.setText(str(app_config['Nginx_url']))
        self.usernginx_url_lineEdit.setText(str(app_config['User_url']))

        self.saveconfig_Button.clicked.connect(self.save_config)
        self.checklogin_Button.clicked.connect(self.start_check_login_call)
        self.checkaria2_Button.clicked.connect(self.start_check_aria2_call)
        self.choosepotButton.clicked.connect(self.start_choose_pot)
        self.chooseidmpushButton.clicked.connect(self.start_choose_idm)
        self.chooselocalButton.clicked.connect(self.start_choose_local_downloadpath)
        self.change_webdav_pushButton.clicked.connect(self.start_the_webdav)
        self.check_sock_pushButton.clicked.connect(self.start_check_proxy_call)
        self.clear_headers_pushButton.clicked.connect(self.clear_login_headers)

        self.user_lineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.password_lineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.localdownloadlineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Aria2_hostlineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Aria2_portlineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Aria2_secretlineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Aria2_pathlineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Potplayer_pathlineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.IDMlineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Proxy_ip_lineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Proxy_pass_lineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Proxy_port_lineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Proxy__admin_lineEdit.textChanged.connect(self.save_config_now)  # 改变时发射的信号，传出文本框当前内容
        self.Proxy_type_comboBox.currentIndexChanged.connect(self.save_config_now)
        self.nginx_url_lineEdit.textChanged.connect(self.save_config_now)
        self.usernginx_url_lineEdit.textChanged.connect(self.save_config_now)
        self.webdav_portlineEdit.textChanged.connect(self.save_config_now)
        self.webdav_adminlineEdit.textChanged.connect(self.save_config_now)
        self.webdav_passlineEdit.textChanged.connect(self.save_config_now)


        self.Aria2_portlineEdit.setValidator(QIntValidator())#设置只能输入int类型的数据
        self.Proxy_port_lineEdit.setValidator(QIntValidator())#设置只能输入int类型的数据
        self.webdav_portlineEdit.setValidator(QIntValidator())#设置只能输入int类型的数据


    # 检查代理，信号
    def start_check_proxy_back(self,check_result):
        if wait_screen.isVisible():
            wait_screen.close()
        if check_result:
            info = f"连接成功"
            self.save_config()
            NotificationWindow.success('PikPakDown', info)
        else:
            info =f"连接失败"
            NotificationWindow.error('PikPakDown', info)

    #检查代理，线程
    def start_check_proxy_call(self):
        self.show_loading()

        Proxy_type = self.Proxy_type_comboBox.currentText()

        Proxy_ip = self.Proxy_ip_lineEdit.text()
        Proxy_port = self.Proxy_port_lineEdit.text()
        Proxy_admin = self.Proxy__admin_lineEdit.text()
        Proxy_pass = self.Proxy_pass_lineEdit.text()


        self.Check_proxy_Worker = Check_proxy_Worker(Proxy_type,Proxy_ip,Proxy_port,Proxy_admin,Proxy_pass)
        self.Check_proxy_Worker.valueChanged.connect(self.start_check_proxy_back)
        self.Check_proxy_Worker.start()


    # 开启关闭webdav
    def start_the_webdav(self):

        button_text = self.change_webdav_pushButton.text()
        if button_text == "开启Webdav":

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):开启webdav")
            self._thread = Open_webdav_Worker(admin=app_config['Webdav_admin'],
                                              password=app_config['Webdav_password'],
                                              port=int(app_config['Webdav_port']))
            self._thread.finished.connect(self._thread.deleteLater)
            self.change_webdav_pushButton.setText("关闭Webdav")
            self.change_webdav_pushButton.setStyleSheet(running_button_style)

            self._thread.start()  # 启动线程
        else:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Info ({new_time}):关闭webdav")
            self.change_webdav_pushButton.setText("开启Webdav")
            self.change_webdav_pushButton.setStyleSheet(normal_button_style)
            if self._thread.isRunning():
                self._thread.exit()

    # 选择下载路径
    def start_choose_local_downloadpath(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "")  # 起始路径


        self.localdownloadlineEdit.setText(directory)
        self.save_config()


    def clear_login_headers(self):

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"Info ({new_time}):清除登录缓存")
        app_config['headers'] = {}
        self.save_config()

    # 实时保存配置
    def save_config_now(self):
        global app_config
        app_config['user'] = self.user_lineEdit.text()
        app_config['password'] = self.password_lineEdit.text()
        app_config['Aria2_host'] = self.Aria2_hostlineEdit.text()
        app_config['Aria2_port'] = self.Aria2_portlineEdit.text()
        app_config['Aria2_secret'] = self.Aria2_secretlineEdit.text()
        app_config['Aria2_path'] = self.Aria2_pathlineEdit.text()
        app_config['Potplayer_path'] = self.Potplayer_pathlineEdit.text()
        app_config['IDMplayer_path'] = self.IDMlineEdit.text()
        app_config['Download_path'] = self.localdownloadlineEdit.text()
        app_config['Webdav_admin'] = self.webdav_adminlineEdit.text()
        app_config['Webdav_password'] = self.webdav_passlineEdit.text()
        app_config['Webdav_port'] = self.webdav_portlineEdit.text()
        app_config['Proxy_type'] = self.Proxy_type_comboBox.currentText()

        app_config['Proxy_ip'] =self.Proxy_ip_lineEdit.text()
        app_config['Proxy_port'] = self.Proxy_port_lineEdit.text()
        app_config['Proxy_admin'] = self.Proxy__admin_lineEdit.text()
        app_config['Proxy_pass'] = self.Proxy_pass_lineEdit.text()
        app_config['Nginx_url']=self.nginx_url_lineEdit.text()
        app_config['User_url'] = self.usernginx_url_lineEdit.text()

        set_config()


    # 保存配置
    def save_config(self):
        global app_config
        app_config['user'] = self.user_lineEdit.text()
        app_config['password'] = self.password_lineEdit.text()
        app_config['Aria2_host'] = self.Aria2_hostlineEdit.text()
        app_config['Aria2_port'] = self.Aria2_portlineEdit.text()
        app_config['Aria2_secret'] = self.Aria2_secretlineEdit.text()
        app_config['Aria2_path'] = self.Aria2_pathlineEdit.text()
        app_config['Potplayer_path'] = self.Potplayer_pathlineEdit.text()
        app_config['IDMplayer_path'] = self.IDMlineEdit.text()
        app_config['Download_path'] = self.localdownloadlineEdit.text()
        app_config['Webdav_admin'] = self.webdav_adminlineEdit.text()
        app_config['Webdav_password'] = self.webdav_passlineEdit.text()
        app_config['Webdav_port'] = self.webdav_portlineEdit.text()
        app_config['Proxy_type'] = self.Proxy_type_comboBox.currentText()

        app_config['Proxy_ip'] =self.Proxy_ip_lineEdit.text()
        app_config['Proxy_port'] = self.Proxy_port_lineEdit.text()
        app_config['Proxy_admin'] = self.Proxy__admin_lineEdit.text()
        app_config['Proxy_pass'] = self.Proxy_pass_lineEdit.text()
        app_config['Nginx_url'] = self.nginx_url_lineEdit.text()
        app_config['User_url'] = self.usernginx_url_lineEdit.text()

        set_config()

        NotificationWindow.success('PikPakDown', "配置保存完成")

    # 检查登录连接性,接受信号
    def start_check_login_back(self,check_result):
        if wait_screen.isVisible():
            wait_screen.close()
        if check_result != {}:
            info = f"登录成功:{check_result['name']}"
            self.save_config()
            NotificationWindow.success('PikPakDown', info)
        else:
            info = f"登录失败"
            NotificationWindow.error('PikPakDown', info)


    # 检查登录连接性,调用线程
    def start_check_login_call(self):
        self.show_loading()
        login_admin = self.user_lineEdit.text()
        login_password = self.password_lineEdit.text()

        self.Check_login_Worker = Check_login_Worker(login_admin,login_password)
        self.Check_login_Worker.valueChanged.connect(self.start_check_login_back)
        self.Check_login_Worker.start()

    # 检查aria2
    def start_check_aria2_call(self):
        self.show_loading()
        Aria2_host = self.Aria2_hostlineEdit.text()
        Aria2_port = self.Aria2_portlineEdit.text()
        Aria2_secret = self.Aria2_secretlineEdit.text()


        self.Check_aria2_Worker = Check_aria2_Worker(Aria2_host,Aria2_port,Aria2_secret)
        self.Check_aria2_Worker.valueChanged.connect(self.start_check_aria2_back)
        self.Check_aria2_Worker.start()


    def start_check_aria2_back(self,check_result):
        if wait_screen.isVisible():
            wait_screen.close()
        if check_result:
            info = f"连接成功"
            self.save_config()
            NotificationWindow.success('PikPakDown', info)
        else:
            info = f"连接失败"
            NotificationWindow.error('PikPakDown', info)

    # 获取Potplayer路径
    def start_choose_pot(self):

        openfile_name, file_type = QFileDialog.getOpenFileNames()
        try:
            pot_path = openfile_name[0]
        except:
            return
        self.Potplayer_pathlineEdit.setText(str(pot_path))
        self.save_config()

    # 获取IDM路径
    def start_choose_idm(self):
        # IDMplayer_path
        openfile_name, file_type = QFileDialog.getOpenFileNames()
        try:
            idm_path = (openfile_name[0])
        except:
            return
        self.IDMlineEdit.setText(str(idm_path))
        self.save_config()



if __name__ == '__main__':

    #崩溃错误捕获
    log_dir = os.path.join(os.getcwd(), 'log')
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    cgitb.enable(format='text', logdir=log_dir)


    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(Menu_Style)
    my_pyqt_form = MyPyQT_Form()

    wait_screen = Wait_Window()





    # 安装全局事件过滤器,缩放
    fo = FramelessObject()
    app.installEventFilter(fo)
    fo.add_widget(my_pyqt_form)


    my_pyqt_form.show()

    sys.exit(app.exec_())



