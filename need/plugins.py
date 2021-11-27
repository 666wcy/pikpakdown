from win32com import client
from need.pikabout import get_download_url,get_list,get_folder_all_file
from subprocess import Popen
import json
from PyQt5.QtCore import QThread,pyqtSignal
import time
import aria2p
import pythoncom
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

    if type(file_id)==list:
        down_name_list=[]
        down_url_list=[]
        for a in file_id:
            down_name, down_url, temp = get_download_url(a)
            down_name_list.append(down_name)
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
            name_list, url_list, size_list, path_list = get_folder_all_file(folder_id=file_id,path=f"{down_name}/")
            for name,url,size,path in zip(name_list, url_list, size_list, path_list):
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):推送迅雷:{name}")
                down_name = f"{name}"
                the_filesize = size
                file_size = size
                down_url = url
                down_path = path
                thunder.AddTask(down_url, down_name)
            thunder.CommitTasks()

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送迅雷:{down_name}")
            thunder.AddTask(down_url, down_name)
            thunder.CommitTasks()

#IDM线程
def thread_IDM(file_id,IDM):
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()

    Popen([IDM])

    if type(file_id) == list:
        down_name_list = []
        down_url_list = []
        for a in file_id:
            down_name, down_url, temp = get_download_url(a)
            down_name_list.append(down_name)
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


            name_list, url_list, size_list, path_list = get_folder_all_file(folder_id=file_id, path=f"{data['Download_path']}/{down_name}/")
            for name, url, size, path in zip(name_list, url_list, size_list, path_list):

                down_name = f"{name}"
                the_filesize = size
                file_size = size
                down_url = url
                down_path = path
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):推送IDM:{down_name}")

                Popen([IDM, '/d', down_url,"/p",down_path, '/f', down_name, '/n', '/a'])

            print(f"INFO ({new_time}):IDM开始下载")
            Popen([IDM, '/s'])


        else:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送IDM:{down_name}")
            Popen([IDM, '/d', down_url,"/p",data['Download_path'], '/f', down_name, '/n', '/s'])


def thread_pot(file_id,Pot):


    if type(file_id) == list:
        Popen([Pot, '/current'])
        down_name_list = []
        down_url_list = []
        for a in file_id:
            down_name, down_url, temp = get_download_url(a)
            down_name_list.append(down_name)
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

                    Popen([Pot, down_url, '/insert', '/current'])

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):Potplayer开始播放")
            Popen([Pot, '/autoplay', '/current'])
        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Potplayer:{down_name}")

            Popen([Pot, down_url, '/new'])


def thread_aria2(file_id):

    if type(file_id) == list:

        for a in file_id:
            down_name, down_url, temp = get_download_url(a)
            add_down(url=down_url ,path="/" ,file_name=down_name)



    else:
        down_name, down_url, temp = get_download_url(file_id)


        if down_url == "":

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Aria2,识别为文件夹:{down_name}")

            name_list, url_list, size_list, path_list = get_folder_all_file(folder_id=file_id,path=f"/{down_name}/")
            for name,url,size,path in zip(name_list, url_list, size_list, path_list):

                down_name = f"{name}"
                the_filesize = size
                file_size = size
                down_url = url
                down_path = path


                add_down(url=down_url, path=path, file_name=down_name)


        else:
            add_down(url=down_url ,path="/" ,file_name=down_name)


#复制下载任务url线程
class Copy_downloadurl_Worker(QThread):
    valueChanged = pyqtSignal(list)  # 值变化信号

    def __init__(self, fileid):
        super(Copy_downloadurl_Worker, self).__init__()

        self.fileid = fileid


    def run(self):

        text = ""
        if type(self.fileid) == list:

            for a in self.fileid:
                down_name, down_url, temp = get_download_url(a)
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
                        text = text + down_url + "\n"
                        num = num+1

                info_text = f"{num}个文件 复制下载链接成功"

                self.valueChanged.emit(["success", info_text,text])
            else:

                info_text= f"{down_name} 复制下载链接成功"
                text = down_url

                self.valueChanged.emit(["success", info_text,text])



