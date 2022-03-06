from win32com import client
from need.pikabout import get_download_url,get_list,get_folder_all_file,get_download_info
from subprocess import Popen
import json
from PyQt5.QtCore import QThread,pyqtSignal
import time
import aria2p
import pythoncom
import re
import requests
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

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)


            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

                if app_config['domain_ip_key'] == "True":
                    down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                    get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                    down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                    down_url = down_url.replace(down_domain, down_key)

                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                    down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                down_path = path
                thunder.AddTask(down_url, down_name)
            thunder.CommitTasks()

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送迅雷:{down_name}")
            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

                if app_config['domain_ip_key'] == "True":
                    down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                    get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                    down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                    down_url = down_url.replace(down_domain, down_key)

                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

                    if app_config['domain_ip_key'] == "True":
                        down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                        get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                        down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                        down_url = down_url.replace(down_domain, down_key)

                    if app_config['download_url_key'] == "True":
                        down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                        down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                    Popen([Pot, down_url, '/insert', '/current'])

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):Potplayer开始播放")
            Popen([Pot, '/autoplay', '/current'])
        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Potplayer:{down_name}")

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

                if app_config['domain_ip_key'] == "True":
                    down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                    get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                    down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                    down_url = down_url.replace(down_domain, down_key)

                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                    down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                add_down(url=down_url, path=path, file_name=down_name)


        else:

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            add_down(url=down_url ,path="/" ,file_name=down_name)

def thread_Bitcomet(file_id,thread_url):
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()

    app_config = data



    if type(file_id) == list:
        down_name_list = []
        down_url_list = []
        for a in file_id:
            down_name, down_url, temp = get_download_url(a)
            down_name_list.append(down_name)

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))

            down_url_list.append(down_url)

        for down_url, down_name in zip(down_url_list, down_name_list):
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Bitcomet:{down_name}")

            #Popen([IDM, '/d', down_url, "/p", data['Download_path'], '/f', down_name, '/n', '/a'])
            down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
            domain_key_list = ["https://vod0051-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0037-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0039-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0038-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0049-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0050-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0041-hwyun02-vip-lixian.mypikpak.com",
                               "https://vod0042-hwyun02-vip-lixian.mypikpak.com",
                               "https://vod0043-hwyun02-vip-lixian.mypikpak.com"]
            mirror_url = f""
            for a in domain_key_list:

                if app_config['domain_ip_key'] == "True":
                    down_domain = re.findall("https://(.*?)/", a, re.S)[0]
                    get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                    down_key_list = requests.get(url=get_ip_url).json()["Answer"]
                    for b in down_key_list:
                        mirror_url  = mirror_url + down_url.replace(down_domain, b["data"]) + "\n"
                        mirror_url = mirror_url + down_url.replace(down_domain, b["data"]) + "&\n"

                else:

                    mirror_url = mirror_url + down_url.replace(down_key, a) + "\n"
                    mirror_url = mirror_url + down_url.replace(down_key, a) + "&\n"
            data = {
                "url": f"{down_url}",
                "save_path": data['Download_path'],
                "connection": "200",
                "file_name": down_name,
                "referrer": "",
                "user_agent": "",
                "cookie": "",
                "mirror_url_list": mirror_url
            }
            html = requests.post(url=f"{thread_url}/panel/task_add_httpftp_result", data=data)
            if "faild" in html.text:
                print(f"ERROR ({new_time}):推送Bitcomet:{html.text}")

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):Bitcomet开始下载")


    else:

        down_name, down_url, temp = get_download_url(file_id)

        if down_url == "":

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Bitcomet:识别为文件夹:{down_name}，开始获取目录信息")

            for name, url, size, path in get_folder_all_file(folder_id=file_id,
                                                             path=f"{data['Download_path']}/{down_name}/"):

                down_name = f"{name}"
                the_filesize = size
                file_size = size
                down_url = url

                if app_config['domain_ip_key'] == "True":
                    down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                    get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                    down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                    down_url = down_url.replace(down_domain, down_key)

                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                    down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                down_path = path
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):推送Bitcomet:{down_name}")

                #Popen([IDM, '/d', down_url, "/p", down_path, '/f', down_name, '/n', '/a'])

                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                domain_key_list = ["https://vod0051-aliyun18-vip-lixian.mypikpak.com",
                                   "https://vod0037-aliyun17-vip-lixian.mypikpak.com",
                                   "https://vod0039-aliyun17-vip-lixian.mypikpak.com",
                                   "https://vod0038-aliyun17-vip-lixian.mypikpak.com",
                                   "https://vod0049-aliyun18-vip-lixian.mypikpak.com",
                                   "https://vod0050-aliyun18-vip-lixian.mypikpak.com",
                                   "https://vod0041-hwyun02-vip-lixian.mypikpak.com",
                                   "https://vod0042-hwyun02-vip-lixian.mypikpak.com",
                                   "https://vod0043-hwyun02-vip-lixian.mypikpak.com"]
                mirror_url = f""
                for a in domain_key_list:

                    if app_config['domain_ip_key'] == "True":
                        down_key = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                        down_domain = a.replace("https://", "")
                        get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                        info_json = requests.get(url=get_ip_url).json()
                        print(info_json)
                        if not "Answer" in info_json:
                            continue
                        down_key_list = info_json["Answer"]
                        for b in down_key_list:
                            mirror_url = mirror_url + down_url.replace(down_key, b["data"]) + "\n"
                            mirror_url = mirror_url + down_url.replace(down_key, b["data"]) + "&\n"

                    else:
                        down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                        mirror_url = mirror_url + down_url.replace(down_key, a) + "\n"
                        mirror_url = mirror_url + down_url.replace(down_key, a) + "&\n"

                data = {
                    "url": f"{down_url}",
                    "save_path": down_path,
                    "connection": "200",
                    "file_name": down_name,
                    "referrer": "",
                    "user_agent": "",
                    "cookie": "",
                    "mirror_url_list": mirror_url
                }
                html = requests.post(url=f"{thread_url}/panel/task_add_httpftp_result", data=data)
                if "faild" in html.text:
                    print(f"ERROR ({new_time}):推送Bitcomet:{html.text}")





        else:

            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):推送Bitcomet:{down_name}")

            if app_config['domain_ip_key'] == "True":
                down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                down_url = down_url.replace(down_domain, down_key)

            if app_config['download_url_key'] == "True":
                down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                down_url = down_url.replace(down_key, str(app_config['download_url_word']))


            domain_key_list = ["https://vod0051-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0037-aliyun17-vip-lixian.mypikpak.com",
                               "https://vod0039-aliyun17-vip-lixian.mypikpak.com",
                               "https://vod0038-aliyun17-vip-lixian.mypikpak.com",
                               "https://vod0049-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0050-aliyun18-vip-lixian.mypikpak.com",
                               "https://vod0041-hwyun02-vip-lixian.mypikpak.com",
                               "https://vod0042-hwyun02-vip-lixian.mypikpak.com",
                               "https://vod0043-hwyun02-vip-lixian.mypikpak.com"]
            mirror_url=f""

            for a in domain_key_list:

                if app_config['domain_ip_key'] == "True":
                    down_key = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                    down_domain = a.replace("https://","")
                    get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                    info_json = requests.get(url=get_ip_url).json()
                    print(info_json)
                    if not "Answer" in info_json:
                        continue
                    down_key_list = info_json["Answer"]
                    for b in down_key_list:

                        mirror_url = mirror_url + down_url.replace(down_key, b["data"]) + "\n"
                        mirror_url = mirror_url + down_url.replace(down_key, b["data"]) + "&\n"

                else:
                    down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                    mirror_url = mirror_url + down_url.replace(down_key, a) + "\n"
                    mirror_url = mirror_url + down_url.replace(down_key, a) + "&\n"
            data = {
                "url": f"{down_url}",
                "save_path": data['Download_path'],
                "connection": "200",
                "file_name": down_name,
                "referrer": "",
                "user_agent": "",
                "cookie": "",
                "mirror_url_list": mirror_url
            }
            html = requests.post(url=f"{thread_url}/panel/task_add_httpftp_result",data=data)
            if "faild" in html.text:

                print(f"ERROR ({new_time}):推送Bitcomet:{html.text}")




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

                if app_config['domain_ip_key'] == "True":
                    down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                    get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                    down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                    down_url = down_url.replace(down_domain, down_key)

                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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

                        if app_config['domain_ip_key'] == "True":
                            down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                            get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                            down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                            down_url = down_url.replace(down_domain, down_key)

                        if app_config['download_url_key'] == "True":
                            down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
                            down_url = down_url.replace(down_key, str(app_config['download_url_word']))

                        text = text + down_url + "\n"
                        num = num+1

                info_text = f"{num}个文件 复制下载链接成功"

                self.valueChanged.emit(["success", info_text,text])
            else:

                info_text= f"{down_name} 复制下载链接成功"

                if app_config['domain_ip_key'] == "True":
                    down_domain = re.findall("https://(.*?)/download.*", down_url, re.S)[0]
                    get_ip_url = f"https://223.5.5.5/resolve?ct=application/dns-json&name={down_domain}.&type=A&edns_client_subnet=0.0.0.0"
                    down_key = requests.get(url=get_ip_url).json()["Answer"][0]["data"]

                    down_url = down_url.replace(down_domain, down_key)

                if app_config['download_url_key'] == "True":
                    down_key = re.findall("(.*?)/download.*", down_url, re.S)[0]
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


'''{
	"url": "https://vod0050-aliyun18-vip-lixian.mypikpak.com/download/?fid=8EjS5VME9cYbtDuEjGR1jTR*tQ63D*k2AAAAAA4OkA0TjTLRQTm**q7CT4pd6men&mid=666&threshold=251&tid=EA093CE26197A2C675AF5F3187FBC387&srcid=0&verno=2&pk=xdrive&e=1646573332&g=0E0E900D138D32D14139BEFAAEC24F8A5DEA67A7&i=F048D2E55304F5C61BB43B848C64758D347EB50E&ui=YRdkHHI8ZU8Ap0ER&t=0&hy=1&ms=6300000&th=0&pt=1&f=921243575&spr=flow&fileid=VMnBPVQjMRShWd-IisrphFm0o1&fext=rar&userid=YRdkHHI8ZU8Ap0ER&clientid=YNxT9w7GMdWvEOKa&projectid=2wks56c31dc80sxm5p9&vip=PVIP&clientver=&at=D9235013033155DEC13D1848EC498E8C",
	"save_path": "C:\\Users\\weicy\\Downloads\\Telegram+Desktop",
	"connection": "200",
	"file_name": "1.mp4",
	"referrer": "",
	"user_agent": "",
	"cookie": "",
	"mirror_url_list": "https://vod0051-aliyun18-vip-lixian.mypikpak.com/download/?fid=8EjS5VME9cYbtDuEjGR1jTR*tQ63D*k2AAAAAA4OkA0TjTLRQTm**q7CT4pd6men&mid=666&threshold=251&tid=EA093CE26197A2C675AF5F3187FBC387&srcid=0&verno=2&pk=xdrive&e=1646573332&g=0E0E900D138D32D14139BEFAAEC24F8A5DEA67A7&i=F048D2E55304F5C61BB43B848C64758D347EB50E&ui=YRdkHHI8ZU8Ap0ER&t=0&hy=1&ms=6300000&th=0&pt=1&f=921243575&spr=flow&fileid=VMnBPVQjMRShWd-IisrphFm0o1&fext=rar&userid=YRdkHHI8ZU8Ap0ER&clientid=YNxT9w7GMdWvEOKa&projectid=2wks56c31dc80sxm5p9&vip=PVIP&clientver=&at=D9235013033155DEC13D1848EC498E8C\r\nhttps://vod0049-aliyun18-vip-lixian.mypikpak.com/download/?fid=8EjS5VME9cYbtDuEjGR1jTR*tQ63D*k2AAAAAA4OkA0TjTLRQTm**q7CT4pd6men&mid=666&threshold=251&tid=EA093CE26197A2C675AF5F3187FBC387&srcid=0&verno=2&pk=xdrive&e=1646573332&g=0E0E900D138D32D14139BEFAAEC24F8A5DEA67A7&i=F048D2E55304F5C61BB43B848C64758D347EB50E&ui=YRdkHHI8ZU8Ap0ER&t=0&hy=1&ms=6300000&th=0&pt=1&f=921243575&spr=flow&fileid=VMnBPVQjMRShWd-IisrphFm0o1&fext=rar&userid=YRdkHHI8ZU8Ap0ER&clientid=YNxT9w7GMdWvEOKa&projectid=2wks56c31dc80sxm5p9&vip=PVIP&clientver=&at=D9235013033155DEC13D1848EC498E8C"
}'''