import requests
import os
import json
import re
from urllib.parse import urlparse
import time
from PyQt5.QtCore import QThread,pyqtSignal
import hashlib
with open("config.json", "r") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()
import random



the_config = data
if the_config['Nginx_url'] == "":
        pikpak_api_url = "https://api-drive.mypikpak.com"

else:
    pikpak_api_url = the_config['Nginx_url']

if the_config['User_url'] == "":
        pikpak_user_url = "https://user.mypikpak.com"

else:
    pikpak_user_url = the_config['User_url']


def check_login(login_admin, login_password):
    try:

        login_url = f"{pikpak_user_url}/v1/auth/signin?client_id=YNxT9w7GMdWvEOKa"

        login_data = {"captcha_token": "",
                      "client_id": "YNxT9w7GMdWvEOKa",
                      "client_secret": "dbw2OtmVEeuUvIptb1Coyg",
                      "password": login_password, "username": login_admin}

        headers = {
            'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'user.mypikpak.com',
            }
        if the_config['User_url'] != "":
            headers['Host'] = urlparse(str(the_config['User_url']))[1]

        # {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImMwOTk1ZjljLTJlODctNDIyNi1hOTJhLTU0ZDliZTNmYWYxYyJ9.eyJpc3MiOiJodHRwczovL3VzZXIubXlwaWtwYWsuY29tIiwic3ViIjoiWVJka0hISThaVThBcDBFUiIsImF1ZCI6IllOeFQ5dzdHTWRXdkVPS2EiLCJleHAiOjE2MzA2NzY2MjUsImlhdCI6MTYzMDY2OTQyNSwiYXRfaGFzaCI6InIuTWNad2NReXNFZXlRdEphb1ZqSG95QSIsInNjb3BlIjoidXNlciBwYW4gc3luYyBvZmZsaW5lIiwicHJvamVjdF9pZCI6IjJ3a3M1NmMzMWRjODBzeG01cDkifQ.CtFrbSybtJL26yZriZ0IhNcyQlaqXNW09ciSagemQP9Cx1JrplMDDbcogTBzAZOOuxdX18n5ZSnuajMrnh7esmqOxl5k3o9CtlhFsy7hoKxyYe3xdh5SayiYUYCbvbsouTXyusmV-_lsTU9EDZ3ufiPn242mD8wX9folgOrxBOEVmKvIh1nCbxqv8Hx-jXgZePWLlFly0up2jwAY8KJzkIyogJfbj1dw822mYV0oagugu7E8X83JYnQFKojibSESxhANDVYFgrnF2Gbg23ENgzoBx7czFvGMzaAC1-vavGHt9cCw-o_DZsgUYNnlxdZ5w4bKAFoCuU9EodDb48PQtA', 'X-Device-Id': '073163586e9858ede866bcc9171ae3dc', 'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/', 'Host': 'user.mypikpak.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}
        print("检查登录")
        login_result = requests.post(url=login_url, json=login_data, headers=headers,  timeout=5)

        if login_result.status_code == 404:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):登录失败,网络连接错误或反代设置失败")
            return False

        info = login_result.json()


        if "error_code" in info:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):登录失败:{info['error']}")
            return False
        login_headers = headers


        headers['Authorization'] = f"Bearer {info['access_token']}"

        me_url = f"{pikpak_user_url}/v1/user/me"
        me_result = requests.get(url=me_url, headers=login_headers,  timeout=5)

        headers['Host'] = 'api-drive.mypikpak.com'

        return me_result.json()



    except Exception as e:


        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"Error ({new_time}):检查登录失败:{e}")
        print(f"已知错误类型:1.网络无法连接api--'Connection aborted.', OSError(0, 'Error')")
        return False


def login():
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
        jsonFile.close()
    #
    if data['refresh_token'] == "":

        login_admin = data['user']
        login_password = data['password']
        login_url = f"{pikpak_user_url}/v1/auth/signin?client_id=YNxT9w7GMdWvEOKa"

        login_data = {"captcha_token": "",
                      "client_id": "YNxT9w7GMdWvEOKa",
                      "client_secret": "dbw2OtmVEeuUvIptb1Coyg",
                      "password": login_password, "username": login_admin}

        headers = {
            'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'user.mypikpak.com',

            }
        if the_config['User_url'] != "":
            host = urlparse(str(the_config['User_url']))[1]
            headers['Host'] = host
        # {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImMwOTk1ZjljLTJlODctNDIyNi1hOTJhLTU0ZDliZTNmYWYxYyJ9.eyJpc3MiOiJodHRwczovL3VzZXIubXlwaWtwYWsuY29tIiwic3ViIjoiWVJka0hISThaVThBcDBFUiIsImF1ZCI6IllOeFQ5dzdHTWRXdkVPS2EiLCJleHAiOjE2MzA2NzY2MjUsImlhdCI6MTYzMDY2OTQyNSwiYXRfaGFzaCI6InIuTWNad2NReXNFZXlRdEphb1ZqSG95QSIsInNjb3BlIjoidXNlciBwYW4gc3luYyBvZmZsaW5lIiwicHJvamVjdF9pZCI6IjJ3a3M1NmMzMWRjODBzeG01cDkifQ.CtFrbSybtJL26yZriZ0IhNcyQlaqXNW09ciSagemQP9Cx1JrplMDDbcogTBzAZOOuxdX18n5ZSnuajMrnh7esmqOxl5k3o9CtlhFsy7hoKxyYe3xdh5SayiYUYCbvbsouTXyusmV-_lsTU9EDZ3ufiPn242mD8wX9folgOrxBOEVmKvIh1nCbxqv8Hx-jXgZePWLlFly0up2jwAY8KJzkIyogJfbj1dw822mYV0oagugu7E8X83JYnQFKojibSESxhANDVYFgrnF2Gbg23ENgzoBx7czFvGMzaAC1-vavGHt9cCw-o_DZsgUYNnlxdZ5w4bKAFoCuU9EodDb48PQtA', 'X-Device-Id': '073163586e9858ede866bcc9171ae3dc', 'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/', 'Host': 'user.mypikpak.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}

        login_result = requests.post(url=login_url, json=login_data, headers=headers,  timeout=5)


        login_headers = headers

        info = login_result.json()
        print(info)
        headers['Authorization'] = f"Bearer {info['access_token']}"

        headers['Host'] = 'api-drive.mypikpak.com'

        data['headers'] = login_headers
        data['refresh_token'] = info['refresh_token']
        with open("config.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4, ensure_ascii=False)
            jsonFile.close()

    else:
        refresh_url = f"{pikpak_user_url}/v1/auth/token?client_id=YNxT9w7GMdWvEOKa"
        refresh_json = {
            "client_id": "YNxT9w7GMdWvEOKa",
            "client_secret": "dbw2OtmVEeuUvIptb1Coyg",
            "grant_type": "refresh_token",
            "refresh_token": data['refresh_token']
        }
        headers = {
            'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'user.mypikpak.com',

            }
        if the_config['User_url'] != "":
            host = urlparse(str(the_config['User_url']))[1]
            headers['Host'] = host
        refresh_result = requests.post(url=refresh_url, json=refresh_json, headers=headers, timeout=5)
        info = refresh_result.json()
        print(info)
        if "error" in info:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


            if info['error_code'] == 4126:
                print(f"INFO ({new_time}):其它设备登录，发生挤号，正在尝试账号密码重新登录")
                login_admin = data['user']

                if login_admin == "":
                    print(f"INFO ({new_time}):未检测到账号密码，手机登录请重新在设置页获取验证码")
                    return

                login_password = data['password']
                login_url = f"{pikpak_user_url}/v1/auth/signin?client_id=YNxT9w7GMdWvEOKa"

                login_data = {"captcha_token": "",
                              "client_id": "YNxT9w7GMdWvEOKa",
                              "client_secret": "dbw2OtmVEeuUvIptb1Coyg",
                              "password": login_password, "username": login_admin}
                headers = {
                    'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Host': 'user.mypikpak.com',

                }
                if the_config['User_url'] != "":
                    host = urlparse(str(the_config['User_url']))[1]
                    headers['Host'] = host
                # {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImMwOTk1ZjljLTJlODctNDIyNi1hOTJhLTU0ZDliZTNmYWYxYyJ9.eyJpc3MiOiJodHRwczovL3VzZXIubXlwaWtwYWsuY29tIiwic3ViIjoiWVJka0hISThaVThBcDBFUiIsImF1ZCI6IllOeFQ5dzdHTWRXdkVPS2EiLCJleHAiOjE2MzA2NzY2MjUsImlhdCI6MTYzMDY2OTQyNSwiYXRfaGFzaCI6InIuTWNad2NReXNFZXlRdEphb1ZqSG95QSIsInNjb3BlIjoidXNlciBwYW4gc3luYyBvZmZsaW5lIiwicHJvamVjdF9pZCI6IjJ3a3M1NmMzMWRjODBzeG01cDkifQ.CtFrbSybtJL26yZriZ0IhNcyQlaqXNW09ciSagemQP9Cx1JrplMDDbcogTBzAZOOuxdX18n5ZSnuajMrnh7esmqOxl5k3o9CtlhFsy7hoKxyYe3xdh5SayiYUYCbvbsouTXyusmV-_lsTU9EDZ3ufiPn242mD8wX9folgOrxBOEVmKvIh1nCbxqv8Hx-jXgZePWLlFly0up2jwAY8KJzkIyogJfbj1dw822mYV0oagugu7E8X83JYnQFKojibSESxhANDVYFgrnF2Gbg23ENgzoBx7czFvGMzaAC1-vavGHt9cCw-o_DZsgUYNnlxdZ5w4bKAFoCuU9EodDb48PQtA', 'X-Device-Id': '073163586e9858ede866bcc9171ae3dc', 'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/', 'Host': 'user.mypikpak.com', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'}

                login_result = requests.post(url=login_url, json=login_data, headers=headers, timeout=5)

                info = login_result.json()


        headers['Authorization'] = f"Bearer {info['access_token']}"

        headers['Host'] = 'api-drive.mypikpak.com'

        data['headers'] = headers
        data['refresh_token'] = info['refresh_token']

        with open("config.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4, ensure_ascii=False)
            jsonFile.close()



def get_headers():
    if os.path.isfile("config.json") == True:
        try:

            with open("config.json", "r") as jsonFile:
                data = json.load(jsonFile)
                jsonFile.close()

            if 'headers' in data:
                login_headers = data['headers']
                if the_config['Nginx_url'] != "":
                    host = urlparse(str(the_config['Nginx_url']))[1]
                    login_headers['Host'] = host

                return login_headers

            else:

                login()
                login_headers = data['headers']
                if the_config['Nginx_url'] != "":

                    host = urlparse(str(the_config['Nginx_url']))[1]
                    login_headers['Host'] = host

                return login_headers

        except Exception as e:


            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):读取配置失败:{e}")
            return False

    else:

        with open("config.json", "a") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内容
            file.close()
        return False


def get_list(foder_id):
    try:

        login_headers = get_headers()
        file_list = []
        #/drive/v1/files?parent_id=&thumbnail_size=SIZE_LARGE&filters={"trashed":{%22eq%22:false}}
        list_url = f"{pikpak_api_url}/drive/v1/files?parent_id=" + foder_id +"&thumbnail_size=SIZE_LARGE" + "&filters={\"trashed\":{%22eq%22:false}}"
        list_result = requests.get(url=list_url, headers=login_headers,  timeout=5)

        if "error" in list_result.json():
            if list_result.json()['error_code'] == 16:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):登录过期，正在重新登录")
                login()
                login_headers = get_headers()
                list_result = requests.get(url=list_url, headers=login_headers,  timeout=5)
            else:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f"Error ({new_time}):f{list_result.json()['error_description']}")
                return



        file_list = file_list + list_result.json()['files']

        while list_result.json()['next_page_token'] != "":
            list_url = f"{pikpak_api_url}/drive/v1/files?parent_id=" + foder_id + "&page_token=" + \
                       list_result.json()[
                           'next_page_token'] + "&thumbnail_size=SIZE_LARGE" + "&filters={\"trashed\":{%22eq%22:false}}"
            list_result = requests.get(url=list_url, headers=login_headers,  timeout=5)

            file_list = file_list + list_result.json()['files']





        return file_list
    except Exception as e:

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"Error ({new_time}):获取列表失败:{e}")

        return []


def get_download_url(file_id):
    try:
        login_headers = get_headers()
        download_url = f"{pikpak_api_url}/drive/v1/files/{file_id}?magic=2021&thumbnail_size=SIZE_LARGE"
        download_info = requests.get(url=download_url, headers=login_headers,  timeout=5)

        if "error" in download_info.json():
            if download_info.json()['error_code'] == 16:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):登录过期，正在重新登录")
                login()
                login_headers = get_headers()
                download_info = requests.get(url=download_url, headers=login_headers,  timeout=5)
            else:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f"Error ({new_time}):f{download_info.json()['error_description']}")
                return



        return download_info.json()['name'], download_info.json()['web_content_link'], download_info.json()['size']
    except:
        return "","",""


# print(get_list(foder_id=""))

def get_offline_list():
    login_headers = get_headers()
    offline_list_url = f"{pikpak_api_url}/drive/v1/tasks?type=offline&page_token=&thumbnail_size=SIZE_LARGE&filters=%7B%7D&with=reference_resource"
    offline_list_info = requests.get(url=offline_list_url, headers=login_headers,  timeout=5)

    if "error" in offline_list_info.json():
        if offline_list_info.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            offline_list_info = requests.get(url=offline_list_url, headers=login_headers,  timeout=5)
        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{offline_list_info.json()['error_description']}")
            return



    return offline_list_info.json()['tasks']


def magnet_upload(file_url):
    if "\n" in file_url:
        file_list = str(file_url).split("\n")
        file_num = len(file_list)
        num = 0
        for a in file_list:
            login_headers = get_headers()
            torrent_url = f"{pikpak_api_url}/drive/v1/files"

            torrent_data = {
                "kind": "drive#file",
                "name": "",
                "upload_type": "UPLOAD_TYPE_URL",
                "url": {
                    "url": a
                },
                "folder_type": "DOWNLOAD"
            }

            torrent_result = requests.post(url=torrent_url, headers=login_headers, json=torrent_data,  timeout=5)

            if "error" in torrent_result.json():
                if torrent_result.json()['error_code'] == 16:
                    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    print(f"INFO ({new_time}):登录过期，正在重新登录")
                    login()
                    login_headers = get_headers()
                    torrent_result = requests.post(url=torrent_url, headers=login_headers, json=torrent_data,  timeout=5)
                else:
                    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    print(f"Error ({new_time}):f{torrent_result.json()['error_description']}")
                    return


            num = num+1
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):添加离线任务:{num}/{file_num}-<a href=\"{a}\" onclick=\"return false\">磁力链接</a>")

    else:

        login_headers = get_headers()
        torrent_url = f"{pikpak_api_url}/drive/v1/files"

        torrent_data = {
            "kind": "drive#file",
            "name": "",
            "upload_type": "UPLOAD_TYPE_URL",
            "url": {
                "url": file_url
            },
            "folder_type": "DOWNLOAD"
        }

        torrent_result = requests.post(url=torrent_url, headers=login_headers, json=torrent_data,  timeout=5)

        if "error" in torrent_result.json():
            if torrent_result.json()['error_code'] == 16:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):登录过期，正在重新登录")
                login()
                login_headers = get_headers()
                torrent_result = requests.post(url=torrent_url, headers=login_headers, json=torrent_data,  timeout=5)

            else:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f"Error ({new_time}):f{torrent_result.json()['error_description']}")
                return


        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):添加离线任务:<a href=\"{file_url}\" onclick=\"return false\">磁力链接</a>")


def gcid_hash_file(filepath):
    h = hashlib.sha1()
    size = os.path.getsize(filepath)
    psize = 0x40000
    while size / psize > 0x200 and psize < 0x200000:
        psize = psize << 1
    with open(filepath, 'rb') as stream:
        data = stream.read(psize)
        while data:
            h.update(hashlib.sha1(data).digest())
            data = stream.read(psize)

    file_hash = h.hexdigest().upper()
    file_size = os.path.getsize(filepath)
    filename = os.path.split(filepath)[1]

    return file_hash, file_size, filename


def pikpak_add_hash(filename, file_size, file_hash, folder_id):


    upload_url = f"{pikpak_api_url}/drive/v1/files"
    login_headers = get_headers()
    upload_url_data = {
        "kind": "drive#file",
        "name": str(filename),
        "size": int(file_size),
        "hash": str(file_hash),
        "upload_type": "UPLOAD_TYPE_RESUMABLE",
        "objProvider": {"provider": "UPLOAD_TYPE_UNKNOWN"}}
    if folder_id != "":
        upload_url_data["parent_id"] = folder_id
    upload_result = requests.post(url=upload_url, headers=login_headers, json=upload_url_data,  timeout=5)

    if "error" in upload_result.json():
        if upload_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            upload_result = requests.post(url=upload_url, headers=login_headers, json=upload_url_data,  timeout=5)

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{upload_result.json()['error_description']}")
            return


    if 'resumable' in upload_result.json():
        return False
    else:
        return True


def pikpak_copy_file(file_id, to_folder_id):
    login_headers = get_headers()
    copy_url = f"{pikpak_api_url}/drive/v1/files:batchCopy"
    copy_data = {

        "to": {"parent_id": to_folder_id},
        "ids": [file_id]
    }
    copy_info = requests.post(url=copy_url, headers=login_headers, json=copy_data,  timeout=5)

    if "error" in copy_info.json():
        if copy_info.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            copy_info = requests.post(url=copy_url, headers=login_headers, json=copy_data,  timeout=5)

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{copy_info.json()['error_description']}")
            return





def get_download_info(file_id):
    login_headers = get_headers()
    download_url = f"{pikpak_api_url}/drive/v1/files/{file_id}"
    download_info = requests.get(url=download_url, headers=login_headers,  timeout=5)

    if "error" in download_info.json():
        if download_info.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            download_info = requests.get(url=download_url, headers=login_headers,  timeout=5)

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{download_info.json()['error_description']}")
            return



    return download_info.json()


def get_folder_all_file(folder_id,path):


    foler_list = get_list(foder_id=folder_id)

    for a in foler_list:
        if a["kind"] == "drive#file":
            down_name, down_url, file_size = get_download_url(file_id=a["id"])
            if down_name=="":
                continue
            yield down_name,down_url, file_size,path
        else:
            new_path = path + a['name'] + "/"

            for temp_name,temp_url,temp_size,temp_path in get_folder_all_file(folder_id=a["id"],path=new_path):

                yield temp_name,temp_url,temp_size,temp_path


#新建文件夹
def creat_folder(parent_id,name):

    login_headers = get_headers()

    creat_folder_url = f"{pikpak_api_url}/drive/v1/files"
    creat_folder_data ={"kind":"drive#folder","parent_id":parent_id,"name":name}
    creat_folder_result = requests.post(url=creat_folder_url, headers=login_headers,json=creat_folder_data,  timeout=5)

    if "error" in creat_folder_result.json():
        if creat_folder_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            creat_folder_result = requests.post(url=creat_folder_url, headers=login_headers,json=creat_folder_data,  timeout=5)

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):{creat_folder_result.json()['error_description']}")
            return

    return creat_folder_result.json()




#删除文件夹、文件
def delete_files(file_id):

    login_headers = get_headers()

    delete_files_url = f"{pikpak_api_url}/drive/v1/files:batchTrash"
    if type(file_id) == list:
        delete_files_data = {"ids": file_id}
    else:
        delete_files_data = {"ids": [file_id]}
    delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data,  timeout=5)

    if "error" in delete_files_result.json():
        if delete_files_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data,  timeout=5)

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{delete_files_result.json()['error_description']}")
            return

    return delete_files_result.json()

#获取任务信息
def get_task_info(task_id):

    login_headers = get_headers()

    get_task_info_url = f"{pikpak_api_url}/drive/v1/tasks/" + task_id

    get_task_info_result = requests.get(url=get_task_info_url, headers=login_headers,  timeout=5)

    if "error" in get_task_info_result.json():
        if get_task_info_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            get_task_info_result = requests.post(url=get_task_info_url, headers=login_headers,  timeout=5)



        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{get_task_info_result.json()['error_description']}")
            return


    return get_task_info_result.json()

#移动文件夹、文件
def move_files(parent_id,file_id):

    login_headers = get_headers()

    move_files_url = f"{pikpak_api_url}/drive/v1/files:batchMove"
    if type(file_id) == list:
        move_files_data = {"to": {"parent_id": parent_id}, "ids": file_id}
    else:
        move_files_data = {"to": {"parent_id": parent_id}, "ids": [file_id]}
    move_files_result = requests.post(url=move_files_url, headers=login_headers, json=move_files_data,  timeout=5)

    if "error" in move_files_result.json():
        if move_files_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            move_files_result = requests.post(url=move_files_url, headers=login_headers, json=move_files_data,  timeout=5)

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{move_files_result.json()['error_description']}")
            return

    return move_files_result.json()


#复制文件夹、文件
def copy_files(parent_id,file_id):

    login_headers = get_headers()

    copy_files_url = f"{pikpak_api_url}/drive/v1/files:batchCopy"
    if type(file_id) == list:
        copy_files_data = {"to":{"parent_id":parent_id},"ids":file_id}
    else:
        copy_files_data = {"to": {"parent_id": parent_id}, "ids": [file_id]}
    copy_files_result = requests.post(url=copy_files_url, headers=login_headers, json=copy_files_data,  timeout=5)

    if "error" in copy_files_result.json():
        if copy_files_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            copy_files_result = requests.post(url=copy_files_url, headers=login_headers, json=copy_files_data,
                                              timeout=5)

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{copy_files_result.json()['error_description']}")
            return

    return copy_files_result.json()

#重命名
def rename_file(file_id,name):


    login_headers = get_headers()

    rename_files_url = f"{pikpak_api_url}/drive/v1/files/" + file_id
    rename_files_data = {"name":name}
    rename_files_result = requests.patch(url=rename_files_url, headers=login_headers, json=rename_files_data,  timeout=5)

    if "error" in rename_files_result.json():
        if rename_files_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            rename_files_result = requests.patch(url=rename_files_url, headers=login_headers, json=rename_files_data,  timeout=5)


        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{rename_files_result.json()['error_description']}")
            return

    return rename_files_result.json()


#删除任务信息
def delete_task(task_id):

    login_headers = get_headers()
    task_text = ""
    for a in task_id:
        task_text =task_text + f"task_ids={a}&"
    millis = int(round(time.time() * 1000))

    task_text = task_text + str(millis)
    get_task_info_url = f"{pikpak_api_url}/drive/v1/tasks?" + task_text

    get_task_info_result = requests.delete(url=get_task_info_url, headers=login_headers,  timeout=5)

    if "error" in get_task_info_result.json():
        if get_task_info_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            get_task_info_result = requests.delete(url=get_task_info_url, headers=login_headers, timeout=5)


        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{get_task_info_result.json()['error_description']}")
            return

    return get_task_info_result.json()

#获取回收站信息
def get_trash_list():
    #https://api-drive.mypikpak.com/drive/v1/files?parent_id=*&page_token=&with_audit=true&thumbnail_size=SIZE_LARGE&filters={%22phase%22:%20{%22eq%22:%20%22PHASE_TYPE_COMPLETE%22},%20%22trashed%22:{%22eq%22:true}}
    try:

        login_headers = get_headers()
        file_list = []
        #/drive/v1/files?parent_id=&thumbnail_size=SIZE_LARGE&filters={"trashed":{%22eq%22:false}}
        list_url = f"{pikpak_api_url}/drive/v1/files?parent_id=*" +"&thumbnail_size=SIZE_LARGE" + "&filters={\"phase\": {\"eq\": \"PHASE_TYPE_COMPLETE\"}, \"trashed\":{\"eq\":true}}"
        list_result = requests.get(url=list_url, headers=login_headers,  timeout=5)

        if "error" in list_result.json():
            if list_result.json()['error_code'] == 16:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"INFO ({new_time}):登录过期，正在重新登录")
                login()
                login_headers = get_headers()
                list_result = requests.get(url=list_url, headers=login_headers,  timeout=5)

            else:
                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f"Error ({new_time}):f{list_result.json()['error_description']}")
                return



        file_list = file_list + list_result.json()['files']

        while list_result.json()['next_page_token'] != "":
            list_url = f"{pikpak_api_url}/drive/v1/files?parent_id=*" + "&page_token=" + \
                       list_result.json()[
                           'next_page_token'] + "&thumbnail_size=SIZE_LARGE" + "&filters={\"phase\": {\"eq\": \"PHASE_TYPE_COMPLETE\"}, \"trashed\":{\"eq\":true}}"
            list_result = requests.get(url=list_url, headers=login_headers,  timeout=5)

            file_list = file_list + list_result.json()['files']





        return file_list
    except Exception as e:

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"Error ({new_time}):获取列表失败:{e}")

        return []


#删除回收站文件
def delete_tash(file_id):

    login_headers = get_headers()

    delete_files_url = f"{pikpak_api_url}/drive/v1/files:batchDelete"
    if type(file_id) == list:
        delete_files_data = {"ids": file_id}
    else:
        delete_files_data = {"ids": [file_id]}
    delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data,  timeout=5)

    if "error" in delete_files_result.json():

        if delete_files_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data,
                                                timeout=5)

        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{delete_files_result.json()['error_description']}")
            return

    return delete_files_result.json()

#删除回收站文件
def back_tash(file_id):

    login_headers = get_headers()

    delete_files_url = f"{pikpak_api_url}/drive/v1/files:batchUntrash"
    if type(file_id) == list:
        delete_files_data = {"ids": file_id}
    else:
        delete_files_data = {"ids": [file_id]}
    delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data,  timeout=5)

    if "error" in delete_files_result.json():
        if delete_files_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data, timeout=5)
        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{delete_files_result.json()['error_description']}")
            return


    return delete_files_result.json()


def get_quate_info():
    login_headers = get_headers()

    get_quate_info_url = f"{pikpak_api_url}/drive/v1/about"

    get_quate_info_result = requests.get(url=get_quate_info_url, headers=login_headers,  timeout=5)

    if "error" in get_quate_info_result.json():
        if get_quate_info_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            get_quate_info_result = requests.get(url=get_quate_info_url, headers=login_headers, timeout=5)
        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{get_quate_info_result.json()['error_description']}")
            return


    return get_quate_info_result.json()

def get_my_vip():
    login_headers = get_headers()



    me_url =  f"{pikpak_api_url}/drive/v1/privilege/vip"
    me_result = requests.get(url=me_url, headers=login_headers,  timeout=5)
    if "error" in me_result.json():
        if me_result.json()['error_code'] == 16:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            me_result = requests.get(url=me_url, headers=login_headers, timeout=5)
        else:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"Error ({new_time}):f{me_result.json()['error_description']}")
            return






    return me_result.json()



#发送验证码线程
class Register_account_get(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self, verification_id,verification_code,captcha_token,account_name,email,password):
        super(Register_account_get, self).__init__()

        self.email = email
        self.verification_id=verification_id
        self.verification_code = verification_code
        self.captcha_token=captcha_token
        self.account_name = account_name
        self.password = password



    def run(self):
        try:
            CLIENT_ID = 'YNxT9w7GMdWvEOKa'
            VersionName = '1.7.0'
            PackageName = 'com.pikcloud.pikpak'

            DeviceID_list = random.sample('1234567890zyxwvutsrqponmlkjihgfedcba', 32)
            DeviceID = ""
            for a in DeviceID_list:
                DeviceID = DeviceID + a
            print(DeviceID)
            timestamp = str(int(round(time.time() * 1000)))


            email = self.email
            verification_id=self.verification_id
            verification_code = self.verification_code
            captcha_token=self.captcha_token
            account_name = self.account_name
            password = self.password
            headers = {
                'User-Agent': f'ANDROID-com.pikcloud.pikpak/null protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.f78911b4fdd89ca52b5e351273e17ca10f0594675e0cdc49c75a25f4853b1c02 sdkversion/1.0.1.101700 datetime/1637652663646 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/null deviceid/{DeviceID} providername/NONE refresh_token/ usrno/ appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
                'Content-Type': 'application/json; charset=utf-8',
                'Host': 'user.mypikpak.com',
            }
            if the_config['User_url'] != "":
                host = urlparse(str(the_config['User_url']))[1]
                headers['Host'] = host

            verify_url = f"{pikpak_user_url}/v1/auth/verification/verify?client_id=YNxT9w7GMdWvEOKa"
            verify_json = {"client_id": "YNxT9w7GMdWvEOKa",
                           "verification_id": verification_id,
                           "verification_code": verification_code}

            verify_result = requests.post(url=verify_url, headers=headers, json=verify_json)
            print(verify_result.json())
            verification_token = verify_result.json()['verification_token']

            signup_url = f"{pikpak_user_url}/v1/auth/signup?client_id=YNxT9w7GMdWvEOKa"
            signup_json = {
                "captcha_token": captcha_token,
                "client_id": "YNxT9w7GMdWvEOKa", "client_secret": "dbw2OtmVEeuUvIptb1Coyg", "email": email,
                "name": account_name, "password": password,
                "verification_token": verification_token}
            signup_result = requests.post(url=signup_url, headers=headers, json=signup_json)




            captcha_json = {"action": "POST:/v1/auth/signup", "captcha_token": captcha_token,
                            "client_id": "YNxT9w7GMdWvEOKa",
                            "device_id": DeviceID,
                            "meta": {"email": email,

                                     'user_id':"","package_name":PackageName,"timestamp":timestamp
                                     ,"client_version":VersionName},
                            "redirect_uri": "xlaccsdk01://xunlei.com/callback?state=harbor",

                            }

            captcha_url = f"{pikpak_user_url}/v1/shield/captcha/init?client_id=YNxT9w7GMdWvEOKa"
            captcha_result = requests.post(url=captcha_url, headers=headers, json=captcha_json)

            captcha_token = captcha_result.json()['captcha_token']

            verify_json = {"client_id": "YNxT9w7GMdWvEOKa",
                           "verification_id": verification_id,
                           "verification_code": verification_code}

            verify_result = requests.post(url=verify_url, headers=headers, json=verify_json)

            verification_token = verify_result.json()['verification_token']
            signup_url = f"{pikpak_user_url}/v1/auth/signup?client_id=YNxT9w7GMdWvEOKa"
            signup_json = {
                "captcha_token": captcha_token,
                "client_id": "YNxT9w7GMdWvEOKa", "client_secret": "dbw2OtmVEeuUvIptb1Coyg", "email": email,
                "name": account_name, "password": password,
                "verification_token": verification_token}
            signup_result = requests.post(url=signup_url, headers=headers, json=signup_json)

            if 'error' in signup_result.json():

                new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                print(f"Error ({new_time}):注册失败:{signup_result.json()}")

                self.valueChanged.emit(False)
                return

            else:
                info = signup_result.json()



                userid = info['sub']

                invite_url = f"https://invite.wei666.workers.dev/{userid}"

                new_headers = {}
                new_headers['authorization'] = f"Bearer {info['access_token']}"


                invite_result = requests.get(url=invite_url, headers=new_headers )
                print(invite_result.text)

                self.valueChanged.emit(True)

                '''info=signup_result.json()
                add_free_vip = f"{pikpak_api_url}/vip/v1/order/free"
                userid = info['sub']
                add_free_json = {"product_id":"premium_free_auto",
                                 "data":{"sdk_int":"28","uuid":"f78911b4fdd89ca52b5e351273e17ca1",
                                         "userType":"1","userid":userid,
                                         "product_flavor_name":"gp","language_system":"zh-CN",
                                         "language_app":"zh-CN","build_version_release":"9",
                                         "phoneModel":"LG V30","build_manufacturer":"LGE","build_sdk_int":"28",
                                         "channel":"google","versionCode":"10040","versionName":"1.6.1","country":"CN"}}


                headers['Authorization'] = f"Bearer {info['access_token']}"

                headers['Host'] = 'api-drive.mypikpak.com'
                add_free_result = requests.post(url=add_free_vip, headers=headers, json=add_free_json)
                print(add_free_result.text)
                print(add_free_result.json())

                self.valueChanged.emit(True)'''

        except Exception as e:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):注册失败:{e}")

            self.valueChanged.emit(False)


#发送验证码线程
class Register_account_send(QThread):
    valueChanged = pyqtSignal(dict)  # 值变化信号

    def __init__(self, email):
        super(Register_account_send, self).__init__()

        self.email = email


    def run(self):
        email = self.email
        captcha_url = f"{pikpak_user_url}/v1/shield/captcha/init?client_id=YNxT9w7GMdWvEOKa"
        captcha_json = {"action": "POST:/v1/auth/verification", "captcha_token": "", "client_id": "YNxT9w7GMdWvEOKa",
                        "device_id": "073163586e9858ede866bcc9171ae3dc", "meta": {"email": email},
                        "redirect_uri": "xlaccsdk01://xunlei.com/callback?state=harbor"}

        headers = {
            'User-Agent': 'ANDROID-com.pikcloud.pikpak/null protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.f78911b4fdd89ca52b5e351273e17ca10f0594675e0cdc49c75a25f4853b1c02 sdkversion/1.0.1.101700 datetime/1637652663646 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/null deviceid/f78911b4fdd89ca52b5e351273e17ca1 providername/NONE refresh_token/ usrno/ appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'user.mypikpak.com',
        }
        if the_config['User_url'] != "":
            host = urlparse(str(the_config['User_url']))[1]
            headers['Host'] = host

        captcha_result = requests.post(url=captcha_url, headers=headers, json=captcha_json)

        captcha_token = captcha_result.json()['captcha_token']

        verification_url = f"{pikpak_user_url}/v1/auth/verification?client_id=YNxT9w7GMdWvEOKa"

        verification_json = {
            "captcha_token": captcha_token,
            "client_id": "YNxT9w7GMdWvEOKa", "email": email, "locale": "zh-cn", "target": "ANY"}
        verification_result = requests.post(url=verification_url, headers=headers, json=verification_json)
        print(verification_result.json())
        try:
            verification_id = verification_result.json()['verification_id']
            result = {'status':True,'verification_id':verification_id,'captcha_token':captcha_token,'text':''}
            self.valueChanged.emit(result)
        except Exception as e :
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):请求注册码失败:{e}")
            result = {'status': False, 'verification_id': "", 'captcha_token':"", 'text': ''}
            self.valueChanged.emit(result)
        return


#register_account()


def push_vip_code(vip_code):

    login_headers = get_headers()

    push_vip_url = f"{pikpak_api_url}/vip/v1/order/activation-code"

    push_vip_data = {"activation_code":vip_code}
    push_vip_result = requests.post(url=push_vip_url, headers=login_headers, json=push_vip_data,  timeout=5)
    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    print(f"INFO ({new_time}):提交兑换码:{vip_code}")
    if "error" in push_vip_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        push_vip_result = requests.post(url=push_vip_url, headers=login_headers, json=push_vip_data, timeout=5)

    return push_vip_result.json()


class Phone_login_get(QThread):
    valueChanged = pyqtSignal(bool)  # 值变化信号

    def __init__(self, verification_id,verification_code,captcha_token,account_name,phone_number,password,sighup):
        super(Phone_login_get, self).__init__()

        self.phone_number = phone_number
        self.verification_id=verification_id
        self.verification_code = verification_code
        self.captcha_token=captcha_token
        self.account_name = account_name
        self.password = password
        self.sighup = sighup
        print(self.sighup)


    def run(self):
        try:
            if self.sighup:
                CLIENT_ID = 'YNxT9w7GMdWvEOKa'
                VersionName = '1.7.0'
                PackageName = 'com.pikcloud.pikpak'

                DeviceID_list = random.sample('1234567890zyxwvutsrqponmlkjihgfedcba', 32)
                DeviceID = ""
                for a in DeviceID_list:
                    DeviceID = DeviceID + a
                print(DeviceID)
                timestamp = str(int(round(time.time() * 1000)))


                phone_number = self.phone_number
                verification_id=self.verification_id
                verification_code = self.verification_code
                captcha_token=self.captcha_token
                account_name = self.account_name
                password = self.password
                headers = {
                    'User-Agent': f'ANDROID-com.pikcloud.pikpak/null protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.f78911b4fdd89ca52b5e351273e17ca10f0594675e0cdc49c75a25f4853b1c02 sdkversion/1.0.1.101700 datetime/1637652663646 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/null deviceid/{DeviceID} providername/NONE refresh_token/ usrno/ appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Host': 'user.mypikpak.com',
                }
                if the_config['User_url'] != "":
                    host = urlparse(str(the_config['User_url']))[1]
                    headers['Host'] = host


                captcha_json = {"action": "POST:/v1/auth/signup", "captcha_token": captcha_token,
                                "client_id": "YNxT9w7GMdWvEOKa",
                                "device_id": DeviceID,
                                "meta": {"phone_number": phone_number,

                                         'user_id':"","package_name":PackageName,"timestamp":timestamp
                                         ,"client_version":VersionName},
                                "redirect_uri": "xlaccsdk01://xunlei.com/callback?state=harbor",

                                }

                captcha_url = f"{pikpak_user_url}/v1/shield/captcha/init?client_id=YNxT9w7GMdWvEOKa"
                captcha_result = requests.post(url=captcha_url, headers=headers, json=captcha_json)

                captcha_token = captcha_result.json()['captcha_token']

                verify_json = {"client_id": "YNxT9w7GMdWvEOKa",
                               "verification_id": verification_id,
                               "verification_code": verification_code}

                verify_url = f"{pikpak_user_url}/v1/auth/verification/verify?client_id=YNxT9w7GMdWvEOKa"

                verify_result = requests.post(url=verify_url, headers=headers, json=verify_json)

                verification_token = verify_result.json()['verification_token']
                signup_url = f"{pikpak_user_url}/v1/auth/signup?client_id=YNxT9w7GMdWvEOKa"
                signup_json = {
                    "captcha_token": captcha_token,
                    "client_id": "YNxT9w7GMdWvEOKa", "client_secret": "dbw2OtmVEeuUvIptb1Coyg",
                    "phone_number": phone_number,
                    "name": account_name, "password": password,
                    "verification_token": verification_token}
                signup_result = requests.post(url=signup_url, headers=headers, json=signup_json)

                if 'error' in signup_result.json():

                    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    print(f"Error ({new_time}):注册失败:{signup_result.json()}")

                    self.valueChanged.emit(False)
                    return

                else:
                    info = signup_result.json()

                    userid = info['sub']

                    invite_url = f"https://invite.wei666.workers.dev/{userid}"

                    new_headers = {}
                    new_headers['authorization'] = f"Bearer {info['access_token']}"


                    invite_result = requests.get(url=invite_url, headers=new_headers )
                    print(invite_result.text)
                    with open("config.json", "r") as jsonFile:
                        data = json.load(jsonFile)
                        jsonFile.close()
                    headers = {
                        'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
                        'Content-Type': 'application/json; charset=utf-8', 'Host': 'api-drive.mypikpak.com',
                        'Authorization': f"Bearer {info['access_token']}"}

                    data['headers'] = headers
                    data['refresh_token'] = info['refresh_token']
                    with open("config.json", "w") as jsonFile:
                        json.dump(data, jsonFile, indent=4, ensure_ascii=False)
                        jsonFile.close()

                    self.valueChanged.emit(True)
            else:
                CLIENT_ID = 'YNxT9w7GMdWvEOKa'
                VersionName = '1.7.0'
                PackageName = 'com.pikcloud.pikpak'

                DeviceID_list = random.sample('1234567890zyxwvutsrqponmlkjihgfedcba', 32)
                DeviceID = ""
                for a in DeviceID_list:
                    DeviceID = DeviceID + a
                print(DeviceID)
                timestamp = str(int(round(time.time() * 1000)))

                phone_number = self.phone_number
                verification_id = self.verification_id
                verification_code = self.verification_code
                captcha_token = self.captcha_token
                account_name = self.account_name
                password = self.password
                headers = {
                    'User-Agent': f'ANDROID-com.pikcloud.pikpak/null protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.f78911b4fdd89ca52b5e351273e17ca10f0594675e0cdc49c75a25f4853b1c02 sdkversion/1.0.1.101700 datetime/1637652663646 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/null deviceid/{DeviceID} providername/NONE refresh_token/ usrno/ appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
                    'Content-Type': 'application/json; charset=utf-8',
                    'Host': 'user.mypikpak.com',
                }
                if the_config['User_url'] != "":
                    host = urlparse(str(the_config['User_url']))[1]
                    headers['Host'] = host

                captcha_json = {"action": "POST:/v1/auth/signin", "captcha_token": captcha_token,
                                "client_id": "YNxT9w7GMdWvEOKa",
                                "device_id": DeviceID,
                                "meta": {"phone_number": phone_number,

                                         'user_id': "", "package_name": PackageName, "timestamp": timestamp
                                    , "client_version": VersionName},
                                "redirect_uri": "xlaccsdk01://xunlei.com/callback?state=harbor",

                                }

                captcha_url = f"{pikpak_user_url}/v1/shield/captcha/init?client_id=YNxT9w7GMdWvEOKa"
                captcha_result = requests.post(url=captcha_url, headers=headers, json=captcha_json)

                captcha_token = captcha_result.json()['captcha_token']

                verify_json = {"client_id": "YNxT9w7GMdWvEOKa",
                               "verification_id": verification_id,
                               "verification_code": verification_code}

                verify_url = f"{pikpak_user_url}/v1/auth/verification/verify?client_id=YNxT9w7GMdWvEOKa"

                verify_result = requests.post(url=verify_url, headers=headers, json=verify_json)

                verification_token = verify_result.json()['verification_token']
                signup_url = f"{pikpak_user_url}/v1/auth/signin?client_id=YNxT9w7GMdWvEOKa"
                signup_json = {
                    "captcha_token": captcha_token,
                    "client_id": "YNxT9w7GMdWvEOKa", "client_secret": "dbw2OtmVEeuUvIptb1Coyg",
                    "username": phone_number,
                    "verification_token": verification_token}
                signup_result = requests.post(url=signup_url, headers=headers, json=signup_json)

                if 'error' in signup_result.json():
                    new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                    print(f"Error ({new_time}):注册失败:{signup_result.json()}")

                    self.valueChanged.emit(False)
                    return
                else:
                    info = signup_result.json()


                    with open("config.json", "r") as jsonFile:
                        data = json.load(jsonFile)
                        jsonFile.close()
                    headers = {
                        'User-Agent': 'protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.073163586e9858ede866bcc9171ae3dcd067a68cbbee55455ab0b6096ea846a0 sdkversion/1.0.1.101300 datetime/1630669401815 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/ deviceid/073163586e9858ede866bcc9171ae3dc providername/NONE refresh_token/ usrno/null appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
                        'Content-Type': 'application/json; charset=utf-8', 'Host': 'api-drive.mypikpak.com',
                        'Authorization': f"Bearer {info['access_token']}"}

                    data['headers'] = headers
                    data['refresh_token'] = info['refresh_token']
                    with open("config.json", "w") as jsonFile:
                        json.dump(data, jsonFile, indent=4, ensure_ascii=False)
                        jsonFile.close()

                    self.valueChanged.emit(True)




        except Exception as e:
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):登录失败:{e}")

            self.valueChanged.emit(False)

#发送验证码线程
class Phone_login_send(QThread):
    valueChanged = pyqtSignal(dict)  # 值变化信号

    def __init__(self, phone_number):
        super(Phone_login_send, self).__init__()

        self.phone_number = phone_number


    def run(self):
        phone_number = self.phone_number
        headers = {
            'User-Agent': 'ANDROID-com.pikcloud.pikpak/null protocolversion/200 clientid/YNxT9w7GMdWvEOKa action_type/ networktype/WIFI sessionid/ devicesign/div101.f78911b4fdd89ca52b5e351273e17ca10f0594675e0cdc49c75a25f4853b1c02 sdkversion/1.0.1.101700 datetime/1637652663646 appname/android-com.pikcloud.pikpak session_origin/ grant_type/ clientip/ devicemodel/LG V30 accesstype/ clientversion/null deviceid/f78911b4fdd89ca52b5e351273e17ca1 providername/NONE refresh_token/ usrno/ appid/ devicename/Lge_Lg V30 cmd/login osversion/9 platformversion/10 accessmode/',
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'user.mypikpak.com',
        }
        if the_config['User_url'] != "":
            host = urlparse(str(the_config['User_url']))[1]
            headers['Host'] = host

        verification_url = f"{pikpak_user_url}/v1/auth/verification?client_id=YNxT9w7GMdWvEOKa"

        verification_json = {
            "captcha_token": "",
            "client_id": "YNxT9w7GMdWvEOKa", "phone_number": phone_number, "locale": "zh-cn", "target": "ANY"}
        verification_result = requests.post(url=verification_url, headers=headers, json=verification_json)




        captcha_url = f"{pikpak_user_url}/v1/shield/captcha/init?client_id=YNxT9w7GMdWvEOKa"
        captcha_json = {"action": "POST:/v1/auth/verification", "captcha_token": "", "client_id": "YNxT9w7GMdWvEOKa",
                        "device_id": "073163586e9858ede866bcc9171ae3dc", "meta": {"phone_number": phone_number},
                        "redirect_uri": "xlaccsdk01://xunlei.com/callback?state=harbor"}




        captcha_result = requests.post(url=captcha_url, headers=headers, json=captcha_json)

        captcha_token = captcha_result.json()['captcha_token']



        verification_url = f"{pikpak_user_url}/v1/auth/verification?client_id=YNxT9w7GMdWvEOKa"

        verification_json = {
            "captcha_token": captcha_token,
            "client_id": "YNxT9w7GMdWvEOKa", "phone_number": phone_number, "locale": "zh-cn", "target": "ANY"}
        verification_result = requests.post(url=verification_url, headers=headers, json=verification_json)
        print(verification_result.json())
        if 'is_user' in verification_result.json():
            sighup = False
        else:
            sighup = True
        try:
            verification_id = verification_result.json()['verification_id']
            result = {'status':True,'verification_id':verification_id,'captcha_token':captcha_token,'text':'','sighup':sighup}
            self.valueChanged.emit(result)
        except Exception as e :
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"Error ({new_time}):请求验证码失败:{e}")
            result = {'status': False, 'verification_id': "", 'captcha_token':"", 'text': '','sighup':sighup}
            self.valueChanged.emit(result)
        return