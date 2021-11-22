<!--
 * @Date: 2021-10-26 17:02:43
 * @LastEditors: Ben
 * @LastEditTime: 2021-11-22 16:02:58
-->
# 软件介绍

Pikpakdown是基于Python编写的Pikapk的第三方工具(Win)，所有信息来源均来自对官方app接口的调用，不对用户信息、文件进行保存，目前已开源。欢迎加入Pikpak官方群组。

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=666wcy&repo=pikpakdown)](https://github.com/666wcy/pikpakdown)

# 软件介绍

主要功能:
- [X] 账号注册，支持自定义用户名
- [X] 会员兑换码提交
- [X] 软件自带内部下载
- [X] 推送迅雷
- [X] 推送IDM
- [X] 推送Potplayer
- [X] 推送Aria2
- [X] 多选文件推送(多选文件中不支持文件夹)
- [X] 单个文件夹整体推送，保持文件夹的目录结构进行推送下载
- [X] 双击视频文件自动调用内部MPV播放
- [X] 只读型webdav生成
- [X] Pikpak秒传链接生成、导入
- [X] 代理支持：支持不走系统代理、系统代理、http、sock4、sock5代理
- [X] 鼠标悬停显示文件预览图

# 使用说明

一般情况下，在设置页填入账号和密码即可正常使用，返回主页刷新列表即可显示文件

# 常见问题

## 文件列表无法加载

一般情况下为你的网络与api连接性不好，需要设置代理或反代

代理相关：

方法一：手动设置http、socks4或socks5代理

方法二：开启代理软件的代理功能，在本软件的代理设置中设置为系统代理

如果不想设置代理，可以直接在反代中填入反代地址

博主提供的反代接口，api接口：https://go.weinb.top/api，user接口：https://go.weinb.top/user。

反代的搭建在博客有教程。


**代理和反代设置需要重启才能生效**


**大部分软件问题与上面的原因相关**


## 下载列表显示Aria2未连接

不需要手动启动，在主页进行内部下载时软件会自动启动并添加任务



# 软件下载

下载版本说明，带test的一般不用下载，调试用的。带all是全部依赖打包编译的，兼容性最好。带onefile的是单exe文件，其它都是非exe的绿色免安装版，解压即可使用。

[button color="success" icon="glyphicon glyphicon-download" url="https://github.com/666wcy/pikpakdown/releases"]下载[/button]  [button color="danger" icon="glyphicon glyphicon-user" url="https://t.me/Ben_chao"]Bug反馈[/button]

# 效果展示



![下载效果-全自动Aria2](https://cdn.jsdelivr.net/gh/666wcy/img_share@main/img/下载演示.3cou71t4xdg0.gif)


![系统代理及悬停显示](https://cdn.jsdelivr.net/gh/666wcy/img_share@main/img/系统代理和悬浮显示.2j2klel267m0.gif)

![双击视频播放](https://cdn.jsdelivr.net/gh/666wcy/img_share@main/img/双击视频播放-MPV.1ib0oj2s3xfk.gif)

![外部调用(IDM、迅雷、aria2、potplayer)](https://cdn.jsdelivr.net/gh/666wcy/img_share@main/img/外部调用.izr07w5itls.gif)

# 自定义反代

博主提供的反代接口，api接口：https://go.weinb.top/api，user接口：https://go.weinb.top/user。

## Cloudflare

放入worker即可使用，无需更改。api接口:worker链接/api,user接口：worker链接/user

```
addEventListener('fetch', event => {


    const request = event.request;
    const url = new URL(request.url);
    console.log("test",request.url);

    var api_to_url = "https://api-drive.mypikpak.com";
    var user_to_url = "https://user.mypikpak.com";



    console.log("标头",url.protocol);
    //console.log("路径",url.pathname);
    console.log("host",url.host);

    //req_url = to_url + url.pathname

    //console.log("处理后链接",req_url);
    if ( request.url.search("/api/") != -1 )
    {   
        temp_path = url.protocol + "//" + url.host + "/api"
        console.log("替换链接",temp_path);
        req_url = request.url.replace(temp_path,api_to_url);
        console.log("处理后链接",req_url);
        let request_headers = request.headers;
        let new_request_headers = new Headers(request_headers);
        new_request_headers.set('Host', "api-drive.mypikpak.com");

        const response = fetch(req_url, {
                method: request.method,
                headers: new_request_headers,
                body: request.body,
            });

            event.respondWith(response);
    }
    else if ( request.url.search("/user/") != -1 )
    {   
        temp_path = url.protocol + "//" + url.host + "/user"
        console.log("替换链接",temp_path);
        req_url = request.url.replace(temp_path,user_to_url);
        console.log("处理后链接",req_url);
        let request_headers = request.headers;
        let new_request_headers = new Headers(request_headers);
        new_request_headers.set('Host', "user.mypikpak.com");

        const response = fetch(req_url, {
                method: request.method,
                headers: new_request_headers,
                body: request.body,
            });

            event.respondWith(response);
    }



});


```

## 腾讯云函数

新建flask模板，app.py替换为以下代码，无需更改。
部署成功地址:
api:云函数地址/api
user:云函数地址/user

```
import os
from flask import Flask, jsonify, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from flask import Response
import flask,requests
from flask import Flask,redirect


IS_SERVERLESS = bool(os.environ.get('SERVERLESS'))
print(IS_SERVERLESS)

app = Flask(__name__)

api_site = "https://api-drive.mypikpak.com/"

@app.route("/")
def index():
        if request.method == 'GET':
            url = f'https://weinb.top'
            headers = dict(flask.request.headers)
            print(headers)
            headers['Host'] = "weinb.top"
            resp = requests.get(url=url, headers=headers)
            print(resp.text)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response

@app.route('/user/<path:path>',methods=['GET',"POST",'DELETE','PATCH'])
def proxy_user(path):
    headers = dict(flask.request.headers)
    print(headers)
    headers['Host'] = "user.mypikpak.com"
    par = flask.request.query_string.decode()
    print(path)

    if par != "":
        url = f'{api_site}{path}?{par}'
    else:
        url = f'{api_site}{path}'


    if request.method == 'GET':


        resp = requests.get(url=url, headers=headers)
        print(resp.text)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method == 'POST':

        print(url)

        data = flask.request.data
        print(data)
        resp = requests.post(url=url, headers=headers, data=data)
        print(resp.text)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

    elif request.method == 'DELETE':


        data = flask.request.data

        resp = requests.delete(url=url, headers=headers, data=data)
        print(resp.text)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response

    elif request.method == 'PATCH':


            data = flask.request.data

            resp = requests.patch(url=url, headers=headers, data=data)
            print(resp.text)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response

@app.route('/api/<path:path>',methods=['GET',"POST",'DELETE','PATCH'])
def proxy_api(path):
    print(request.method)
    headers = dict(flask.request.headers)
    print(headers)
    headers['Host'] = "api-drive.mypikpak.com"
    par = flask.request.query_string.decode()
    print(path)
    if par != "":
        url = f'{api_site}{path}?{par}'
    else:
        url = f'{api_site}{path}'
    print(url)


    if request.method == 'GET':


        resp = requests.get(url=url, headers=headers)
        print(resp.text)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    elif request.method == 'POST':


            data = flask.request.data

            resp = requests.post(url=url, headers=headers, data=data)
            print(resp.text)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response

    elif request.method == 'DELETE':


            data = flask.request.data

            resp = requests.delete(url=url, headers=headers, data=data)
            print(resp.text)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response

    elif request.method == 'PATCH':


            data = flask.request.data

            resp = requests.patch(url=url, headers=headers, data=data)
            print(resp.text)
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
            response = Response(resp.content, resp.status_code, headers)
            return response







# 启动服务，监听 9000 端口，监听地址为 0.0.0.0
app.run(debug=IS_SERVERLESS != True, port=9000, host='0.0.0.0')

```



