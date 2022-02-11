from win32com import client
from need.pikabout import get_download_url,get_list,get_folder_all_file,get_download_info
from subprocess import Popen
import json
from PyQt5.QtCore import QThread,pyqtSignal
import time
import aria2p
import pythoncom
import re
#推送aria2单任务
def add_down(url, path, file_name):

    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    try:
        Aria2_host = data['Aria2_host']
        Aria2_port = data['Aria2_port']
        Aria2_secret = data['Aria2_secret']
        Aria2_path = data['Aria2_path']
    except Exception as e:
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"Error ({new_time}):推送Aria2错误:{e}")


        return
    try:
        aria2 = aria2p.API(
            aria2p.Client(
                host=Aria2_host,
                port=int(Aria2_port),
                secret=Aria2_secret
            )
        )
        currdownload = aria2.add_uris([url], options={"dir": f"{Aria2_path}{path}", "out": file_name})
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):推送Aria2:{file_name}，下载路径:{Aria2_path}{path}")



    except Exception as e:
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"Error ({new_time}):Aria2添加任务出错:{e}")



#检查Aria2连接性
def check_aria2(Aria2_host,Aria2_port,Aria2_secret):
    try:

        aria2 = aria2p.API(
            aria2p.Client(
                host=Aria2_host,
                port=int(Aria2_port),
                secret=Aria2_secret
            )
        )
        sta=aria2.get_stats()
        return True

    except Exception as e:
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"Error ({new_time}):连接Aria2出错:{e}")
        return False

#迅雷推送线程
def thread_Thunder(file_id):
    pythoncom.CoInitialize()
    thunder = client.Dispatch('ThunderAgent.Agent64.1')
    with open('config.json', 'r') as f:
        # 读取数据并分割。 最后一个为空，所以去除
        app_config = json.loads(f.read())
    f.close()

    if type(file_id)==list:
        down_name_list=[]
        down_url_list=[]
        for a in file_id:
            down_name, down_url, temp = get_download_url(a)
            down_name_list.append(down_name)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            down_url_list.append(down_url)

        for down_url, down_name in zip(down_url_list,down_name_list):
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送迅雷:{down_name}")
            thunder.AddTask(down_url, down_name)
        thunder.CommitTasks()

    else:
        down_name, down_url, temp = get_download_url(file_id)


        if down_url == "":
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送迅雷,文件夹:{down_name}，即将获取目录信息")
            for name,url,size,path in get_folder_all_file(folder_id=file_id,path=f"{down_name}/"):

                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):推送迅雷:{name}")
                down_name = f"{name}"
                the_filesize = size
                file_size = size
                down_url = url

                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                    down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                down_path = path
                thunder.AddTask(down_url, down_name)
            thunder.CommitTasks()

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送迅雷:{down_name}")
            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            thunder.AddTask(down_url, down_name)
            thunder.CommitTasks()

#IDM线程
def thread_IDM(file_id,IDM):
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()

    app_config = data

    Popen([IDM])

    if type(file_id) == list:
        down_name_list = []
        down_url_list = []
        for a in file_id:
            down_name, down_url, temp = get_download_url(a)
            down_name_list.append(down_name)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            down_url_list.append(down_url)

        for down_url, down_name in zip(down_url_list, down_name_list):

            new_time= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送IDM:{down_name}")

            Popen([IDM, '/d', down_url, "/p", data['Download_path'], '/f', down_name, '/n', '/a'])


        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):IDM开始下载")
        Popen([IDM, '/s'])

    else:

        down_name, down_url, temp = get_download_url(file_id)


        if down_url == "":

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送IDM:识别为文件夹:{down_name}，开始获取目录信息")


            for name, url, size, path in get_folder_all_file(folder_id=file_id, path=f"{data['Download_path']}/{down_name}/"):


                down_name = f"{name}"
                the_filesize = size
                file_size = size
                down_url = url
                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                    down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                down_path = path
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):推送IDM:{down_name}")

                Popen([IDM, '/d', down_url,"/p",down_path, '/f', down_name, '/n', '/a'])

            print(f"INFO ({new_time}):IDM开始下载")
            Popen([IDM, '/s'])


        else:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送IDM:{down_name}")

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            Popen([IDM, '/d', down_url,"/p",data['Download_path'], '/f', down_name, '/n', '/s'])


def thread_pot(file_id,Pot):
    with open('config.json', 'r') as f:
        # 读取数据并分割。 最后一个为空，所以去除
        app_config = json.loads(f.read())
    f.close()

    if type(file_id) == list:
        Popen([Pot, '/current'])
        down_name_list = []
        down_url_list = []
        for a in file_id:
            down_name, down_url, temp = get_download_url(a)
            down_name_list.append(down_name)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            down_url_list.append(down_url)

        for down_url, down_name in zip(down_url_list, down_name_list):
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Potplayer:{down_name}")

            Popen([Pot, down_url, '/insert','/current'])

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):Potplayer开始播放")
        Popen([Pot, '/autoplay','/current'])

    else:

        down_name, down_url, temp = get_download_url(file_id)


        if down_url == "":
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Potplayer，识别为文件夹:{down_name}")
            file_list = get_list(file_id)

            for a in file_list:

                if a['kind'] != 'drive#folder':
                    down_name, down_url, file_size = get_download_url(a['id'])

                    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    print(f"INFO ({new_time}):推送Potplayer:{down_name}")

                    if app_config['download_url_key'] == "True":
                        down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                        down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                    Popen([Pot, down_url, '/insert', '/current'])

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):Potplayer开始播放")
            Popen([Pot, '/autoplay', '/current'])
        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Potplayer:{down_name}")

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            Popen([Pot, down_url, '/new'])


def thread_aria2(file_id):
    with open('config.json', 'r') as f:
        # 读取数据并分割。 最后一个为空，所以去除
        app_config = json.loads(f.read())
    f.close()
    if type(file_id) == list:

        for a in file_id:
            down_name, down_url, temp = get_download_url(a)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            add_down(url=down_url ,path="/" ,file_name=down_name)



    else:
        down_name, down_url, temp = get_download_url(file_id)


        if down_url == "":

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Aria2,识别为文件夹:{down_name}")

            for name,url,size,path in get_folder_all_file(folder_id=file_id,path=f"/{down_name}/"):


                down_name = f"{name}"
                the_filesize = size
                file_size = size
                down_url = url
                down_path = path
                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                    down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                add_down(url=down_url, path=path, file_name=down_name)


        else:

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            add_down(url=down_url ,path="/" ,file_name=down_name)


#复制下载任务url线程
class Copy_downloadurl_Worker(QThread):
    valueChanged = pyqtSignal(list)  # 值变化信号

    def __init__(self, fileid):
        super(Copy_downloadurl_Worker, self).__init__()

        self.fileid = fileid


    def run(self):
        with open('config.json', 'r') as f:
            # 读取数据并分割。 最后一个为空，所以去除
            app_config = json.loads(f.read())
        f.close()
        text = ""
        if type(self.fileid) == list:

            for a in self.fileid:
                down_name, down_url, temp = get_download_url(a)

                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                    down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                text = text + down_url + "\n"



            info_text = f"{len(self.fileid)}个文件 复制下载链接成功"
            self.valueChanged.emit(["success", info_text,text])


        else:
            down_name, down_url, temp = get_download_url(self.fileid)


            if down_url == "":

                file_list = get_list(self.fileid)

                num = 0
                for a in file_list:

                    if a['kind'] != 'drive#folder':
                        down_name, down_url, file_size = get_download_url(a['id'])

                        if app_config['download_url_key'] == "True":
                            down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                            down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                        text = text + down_url + "\n"
                        num = num+1

                info_text = f"{num}个文件 复制下载链接成功"

                self.valueChanged.emit(["success", info_text,text])
            else:

                info_text= f"{down_name} 复制下载链接成功"
                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?mypikpak.com).*", down_url, re.S)[0]
                    down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                text = down_url

                self.valueChanged.emit(["success", info_text,text])

#复制磁力url线程
class Copy_magnet_Worker(QThread):
    valueChanged = pyqtSignal(list)  # 值变化信号

    def __init__(self, fileid):
        super(Copy_magnet_Worker, self).__init__()

        self.fileid = fileid


    def run(self):

        text = ""
        if type(self.fileid) == list:
            num = 0
            for a in self.fileid:
                result = get_download_info(a)
                try:
                    magnet_url = result['params']['url']
                except KeyError :
                    continue
                if magnet_url !="":
                    text = text + magnet_url + "\n"
                    num = num + 1



            if text!="":
                info_text = f"{num}个文件 复制磁力链接成功"
                self.valueChanged.emit(["success", info_text,text])
            else:
                info_text = f"{len(num)}个文件 复制磁力链接失败"
                self.valueChanged.emit(["error", info_text, text])


        else:
            result = get_download_info(self.fileid)
            down_name = result["name"]
            try:
                magnet_url = result['params']['url']
            except KeyError:
                info_text = f"{down_name} 复制磁力链接失败"
                self.valueChanged.emit(["error", info_text, ""])
                return




            if magnet_url != "":
                info_text = f"{down_name} 复制磁力链接成功"
                self.valueChanged.emit(["success", info_text,magnet_url])
            else:
                info_text = f"{down_name} 复制磁力链接失败"
                self.valueChanged.emit(["error", info_text, ""])

