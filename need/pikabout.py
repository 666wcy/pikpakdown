import requests
import os
import json
import hashlib
from urllib.parse import urlparse
import time

with open("config.json", "r") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()

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

        login_result = requests.post(url=login_url, json=login_data, headers=headers)

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
        me_result = requests.get(url=me_url, headers=login_headers)

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

    login_result = requests.post(url=login_url, json=login_data, headers=headers)


    login_headers = headers

    info = login_result.json()
    headers['Authorization'] = f"Bearer {info['access_token']}"

    headers['Host'] = 'api-drive.mypikpak.com'

    data['headers'] = login_headers
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

            print(f"INFO ({new_time}):读取配置失败:{e}")
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
        list_result = requests.get(url=list_url, headers=login_headers)

        if "error" in list_result.json():
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            list_result = requests.get(url=list_url, headers=login_headers)


        file_list = file_list + list_result.json()['files']

        while list_result.json()['next_page_token'] != "":
            list_url = f"{pikpak_api_url}/drive/v1/files?parent_id=" + foder_id + "&page_token=" + \
                       list_result.json()[
                           'next_page_token'] + "&thumbnail_size=SIZE_LARGE" + "&filters={\"trashed\":{%22eq%22:false}}"
            list_result = requests.get(url=list_url, headers=login_headers)

            file_list = file_list + list_result.json()['files']





        return file_list
    except Exception as e:

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"Error ({new_time}):获取列表失败:{e}")

        return []


def get_download_url(file_id):
    login_headers = get_headers()
    download_url = f"{pikpak_api_url}/drive/v1/files/{file_id}"
    download_info = requests.get(url=download_url, headers=login_headers)

    if "error" in download_info.json():

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        download_url = f"{pikpak_api_url}/drive/v1/files/{file_id}"
        download_info = requests.get(url=download_url, headers=login_headers)


    return download_info.json()['name'], download_info.json()['web_content_link'], download_info.json()['size']


# print(get_list(foder_id=""))

def get_offline_list():
    login_headers = get_headers()
    offline_list_url = f"{pikpak_api_url}/drive/v1/tasks?type=offline&page_token=&thumbnail_size=SIZE_LARGE&filters=%7B%7D&with=reference_resource"
    offline_list_info = requests.get(url=offline_list_url, headers=login_headers)

    if "error" in offline_list_info.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        offline_list_url = f"{pikpak_api_url}/drive/v1/tasks?type=offline&page_token=&thumbnail_size=SIZE_LARGE&filters=%7B%7D&with=reference_resource"
        offline_list_info = requests.get(url=offline_list_url, headers=login_headers)


    return offline_list_info.json()['tasks']


def magnet_upload(file_url):
    if "\n" in file_url:
        file_list = str(file_url).split("\n")
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

            torrent_result = requests.post(url=torrent_url, headers=login_headers, json=torrent_data)

            if "error" in torrent_result.json():
                login()
                login_headers = get_headers()
                torrent_result = requests.post(url=torrent_url, headers=login_headers, json=torrent_data)


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

        torrent_result = requests.post(url=torrent_url, headers=login_headers, json=torrent_data)

        if "error" in torrent_result.json():
            login()
            login_headers = get_headers()
            torrent_result = requests.post(url=torrent_url, headers=login_headers, json=torrent_data)




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
    upload_result = requests.post(url=upload_url, headers=login_headers, json=upload_url_data)

    if "error" in upload_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        upload_result = requests.post(url=upload_url, headers=login_headers, json=upload_url_data)

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
    copy_info = requests.post(url=copy_url, headers=login_headers, json=copy_data)

    if "error" in copy_info.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        copy_info = requests.post(url=copy_url, headers=login_headers, json=copy_data)




def get_download_info(file_id):
    login_headers = get_headers()
    download_url = f"{pikpak_api_url}/drive/v1/files/{file_id}"
    download_info = requests.get(url=download_url, headers=login_headers)

    if "error" in download_info.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        download_url = f"{pikpak_api_url}/drive/v1/files/{file_id}"
        download_info = requests.get(url=download_url, headers=login_headers)


    return download_info.json()


def get_folder_all_file(folder_id,path):
    name_list = []
    url_list = []
    size_list = []
    path_list = []
    foler_list = get_list(foder_id=folder_id)

    for a in foler_list:
        if a["kind"] == "drive#file":
            down_name, down_url, file_size = get_download_url(file_id=a["id"])
            name_list.append(down_name)
            url_list.append(down_url)
            size_list.append(file_size)
            path_list.append(path)
        else:
            new_path = path + a['name'] + "/"
            temp_name,temp_url,temp_size,temp_path = get_folder_all_file(folder_id=a["id"],path=new_path)
            name_list = name_list + temp_name
            url_list = url_list + temp_url
            size_list = size_list + temp_size
            path_list = path_list + temp_path


    return name_list,url_list,size_list,path_list

#新建文件夹
def creat_folder(parent_id,name):

    login_headers = get_headers()

    creat_folder_url = f"{pikpak_api_url}/drive/v1/files"
    creat_folder_data ={"kind":"drive#folder","parent_id":parent_id,"name":name}
    creat_folder_result = requests.post(url=creat_folder_url, headers=login_headers,json=creat_folder_data)

    if "error" in creat_folder_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        creat_folder_result = requests.post(url=creat_folder_url, headers=login_headers,json=creat_folder_data)

    return creat_folder_result.json()




#删除文件夹、文件
def delete_files(file_id):

    login_headers = get_headers()

    delete_files_url = f"{pikpak_api_url}/drive/v1/files:batchTrash"
    if type(file_id) == list:
        delete_files_data = {"ids": file_id}
    else:
        delete_files_data = {"ids": [file_id]}
    delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data)

    if "error" in delete_files_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data)

    return delete_files_result.json()

#获取任务信息
def get_task_info(task_id):

    login_headers = get_headers()

    get_task_info_url = f"{pikpak_api_url}/drive/v1/tasks/" + task_id

    get_task_info_result = requests.get(url=get_task_info_url, headers=login_headers)

    if "error" in get_task_info_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        get_task_info_result = requests.post(url=get_task_info_url, headers=login_headers)

    return get_task_info_result.json()

#移动文件夹、文件
def move_files(parent_id,file_id):

    login_headers = get_headers()

    move_files_url = f"{pikpak_api_url}/drive/v1/files:batchMove"
    if type(file_id) == list:
        move_files_data = {"to": {"parent_id": parent_id}, "ids": file_id}
    else:
        move_files_data = {"to": {"parent_id": parent_id}, "ids": [file_id]}
    move_files_result = requests.post(url=move_files_url, headers=login_headers, json=move_files_data)

    if "error" in move_files_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        move_files_result = requests.post(url=move_files_url, headers=login_headers, json=move_files_data)

    return move_files_result.json()


#复制文件夹、文件
def copy_files(parent_id,file_id):

    login_headers = get_headers()

    copy_files_url = f"{pikpak_api_url}/drive/v1/files:batchCopy"
    if type(file_id) == list:
        copy_files_data = {"to":{"parent_id":parent_id},"ids":file_id}
    else:
        copy_files_data = {"to": {"parent_id": parent_id}, "ids": [file_id]}
    copy_files_result = requests.post(url=copy_files_url, headers=login_headers, json=copy_files_data)

    if "error" in copy_files_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        copy_files_result = requests.post(url=copy_files_url, headers=login_headers, json=copy_files_data)

    return copy_files_result.json()

#重命名
def rename_file(file_id,name):


    login_headers = get_headers()

    rename_files_url = f"{pikpak_api_url}/drive/v1/files/" + file_id
    rename_files_data = {"name":name}
    rename_files_result = requests.patch(url=rename_files_url, headers=login_headers, json=rename_files_data)

    if "error" in rename_files_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        rename_files_result = requests.patch(url=rename_files_url, headers=login_headers, json=rename_files_data)

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

    get_task_info_result = requests.delete(url=get_task_info_url, headers=login_headers)

    if "error" in get_task_info_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        get_task_info_result = requests.delete(url=get_task_info_url, headers=login_headers)

    return get_task_info_result.json()

#获取回收站信息
def get_trash_list():
    #https://api-drive.mypikpak.com/drive/v1/files?parent_id=*&page_token=&with_audit=true&thumbnail_size=SIZE_LARGE&filters={%22phase%22:%20{%22eq%22:%20%22PHASE_TYPE_COMPLETE%22},%20%22trashed%22:{%22eq%22:true}}
    try:

        login_headers = get_headers()
        file_list = []
        #/drive/v1/files?parent_id=&thumbnail_size=SIZE_LARGE&filters={"trashed":{%22eq%22:false}}
        list_url = f"{pikpak_api_url}/drive/v1/files?parent_id=*" +"&thumbnail_size=SIZE_LARGE" + "&filters={\"phase\": {\"eq\": \"PHASE_TYPE_COMPLETE\"}, \"trashed\":{\"eq\":true}}"
        list_result = requests.get(url=list_url, headers=login_headers)

        if "error" in list_result.json():
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            print(f"INFO ({new_time}):登录过期，正在重新登录")
            login()
            login_headers = get_headers()
            list_result = requests.get(url=list_url, headers=login_headers)


        file_list = file_list + list_result.json()['files']

        while list_result.json()['next_page_token'] != "":
            list_url = f"{pikpak_api_url}/drive/v1/files?parent_id=*" + "&page_token=" + \
                       list_result.json()[
                           'next_page_token'] + "&thumbnail_size=SIZE_LARGE" + "&filters={\"phase\": {\"eq\": \"PHASE_TYPE_COMPLETE\"}, \"trashed\":{\"eq\":true}}"
            list_result = requests.get(url=list_url, headers=login_headers)

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
    delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data)

    if "error" in delete_files_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data)

    return delete_files_result.json()

#删除回收站文件
def back_tash(file_id):

    login_headers = get_headers()

    delete_files_url = f"{pikpak_api_url}/drive/v1/files:batchUntrash"
    if type(file_id) == list:
        delete_files_data = {"ids": file_id}
    else:
        delete_files_data = {"ids": [file_id]}
    delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data)

    if "error" in delete_files_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        delete_files_result = requests.post(url=delete_files_url, headers=login_headers, json=delete_files_data)

    return delete_files_result.json()


def get_quate_info():
    login_headers = get_headers()

    get_quate_info_url = f"{pikpak_api_url}/drive/v1/about"

    get_quate_info_result = requests.get(url=get_quate_info_url, headers=login_headers)

    if "error" in get_quate_info_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()
        get_quate_info_result = requests.get(url=get_quate_info_url, headers=login_headers)

    return get_quate_info_result.json()

def get_my_vip():
    login_headers = get_headers()



    me_url =  f"{pikpak_api_url}/drive/v1/privilege/vip"
    me_result = requests.get(url=me_url, headers=login_headers)
    if "error" in me_result.json():
        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):登录过期，正在重新登录")
        login()
        login_headers = get_headers()



        me_result = requests.get(url=me_url, headers=login_headers)


    return me_result.json()



