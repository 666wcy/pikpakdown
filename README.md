随缘更新

[TOC]



# 简介

软件支持实现自定义菜单，通过自定义菜单可实现推送Potplayer、IDM等更多工具。



在自定义菜单模块，你将拥有以下信息

文件的原始下载文件信息变量**html**，可理解为json格式，示例格式如下

```
{
     "kind": "drive#file",
     "id": "VN4hEEv3WbpMlmRxG2fvns6oo1",
     "parent_id": "VMh2MlJCcsBC70VSqSFYESGko1",
     "name": "[Lilith-Raws] Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu - 11 [Baha][WEB-DL][1080p][AVC AAC][CHT][MP4].mp4",
     "user_id": "YRdkHHI8ZU8Ap0ER",
     "size": "534068171",
     "revision": "0",
     "file_extension": ".mp4",
     "mime_type": "video/mp4",
     "starred": false,
     "web_content_link": "https://dl-a10b-0051.mypikpak.com/download/?fid=YBjRmppitN37FiQEY8otIEiasenLO9UfAAAAAHC-iIEcZb4PeXBMbmx-HVYwJF-w&mid=666&threshold=251&tid=26BD051F5C083BB6595864D25CADFDB4&srcid=0&verno=2&pk=1101&e=1655899407&g=70BF88811C65BE0F79704C6E6C7F1D5630245FF0&i=6018D19A9A62B4DDFB16240463CA2D20489AB1E9&ui=YRdkHHI8ZU8Ap0ER&t=0&hy=1&ms=6300000&th=0&pt=1&f=534068171&alt=0&pks=1101&rts=&spr=flow&fileid=VN4hEEv3WbpMlmRxG2fvns6oo1&fext=mp4&userid=YRdkHHI8ZU8Ap0ER&clientid=YNxT9w7GMdWvEOKa&projectid=2wks56c31dc80sxm5p9&vip=PVIP&clientver=&at=0B0D1694AADBBEB8F221503169B0BCF2",
     "created_time": "2022-06-16T23:58:44.584+08:00",
     "modified_time": "2022-06-16T23:58:44.584+08:00",
     "icon_link": "https://static.mypikpak.com/39998a187e280e2ee9ceb5f58315a1bcc744fa64",
     "thumbnail_link": "",
     "md5_checksum": "",
     "hash": "70BF88811C65BE0F79704C6E6C7F1D5630245FF0",
     "links": {
          "application/octet-stream": {
               "url": "https://dl-a10b-0051.mypikpak.com/download/?fid=YBjRmppitN37FiQEY8otIEiasenLO9UfAAAAAHC-iIEcZb4PeXBMbmx-HVYwJF-w&mid=666&threshold=251&tid=26BD051F5C083BB6595864D25CADFDB4&srcid=0&verno=2&pk=1101&e=1655899407&g=70BF88811C65BE0F79704C6E6C7F1D5630245FF0&i=6018D19A9A62B4DDFB16240463CA2D20489AB1E9&ui=YRdkHHI8ZU8Ap0ER&t=0&hy=1&ms=6300000&th=0&pt=1&f=534068171&alt=0&pks=1101&rts=&spr=flow&fileid=VN4hEEv3WbpMlmRxG2fvns6oo1&fext=mp4&userid=YRdkHHI8ZU8Ap0ER&clientid=YNxT9w7GMdWvEOKa&projectid=2wks56c31dc80sxm5p9&vip=PVIP&clientver=&at=0B0D1694AADBBEB8F221503169B0BCF2",
               "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkY2RuaHViX2xldmVsIjo5LCJleHAiOjE2NTU4NTYyMDcsImp0aSI6IlhEUklWRSIsInBlZXJfaWQiOiIiLCJwaHViX2xldmVsIjo5LCJwcm9kdWN0X3R5cGUiOiIxMTAxIiwicHJvZHVjdF92ZXJzaW9uIjoiMCIsInJlc190eXBlIjoiZ2NpZCIsInJlc192YWx1ZSI6IjcwQkY4ODgxMUM2NUJFMEY3OTcwNEM2RTZDN0YxRDU2MzAyNDVGRjAiLCJ1c2VyX2RhdGEiOiJ7XCJQdFwiOjF9IiwidXNlcl9pZCI6IllSZGtISEk4WlU4QXAwRVIiLCJ2ZXJzaW9uIjoiMi4wLjAifQ.zstpRe_P_Q8YVLe9orHvewlYSwJeB51mlpp0yDXBufUvEAtnIS7GuFJrx9YX9o0HMY5s5euwKtkMyndt_v_v5aTsp9umpMuTTqCR9TFj3xOaaXqAG1_uWp1AavF_giqaHj7ARI1ee4OGz9Q-Z7A9KnMtw-jjtSprx8WGiXvcYOI",
               "expire": "2022-06-22T08:03:27.081+08:00"
          }
     },
     "phase": "PHASE_TYPE_COMPLETE",
     "audit": {
          "status": "STATUS_OK",
          "message": "Normal resource",
          "title": ""
     },
     "medias": [
          {
               "media_id": "70BF88811C65BE0F79704C6E6C7F1D5630245FF0",
               "media_name": "Original",
               "video": null,
               "link": {
                    "url": "https://dl-a10b-0051.mypikpak.com/download/?fid=YBjRmppitN37FiQEY8otIEiasenLO9UfAAAAAHC-iIEcZb4PeXBMbmx-HVYwJF-w&mid=666&threshold=251&tid=26BD051F5C083BB6595864D25CADFDB4&srcid=0&verno=2&pk=1101&e=1655899407&g=70BF88811C65BE0F79704C6E6C7F1D5630245FF0&i=6018D19A9A62B4DDFB16240463CA2D20489AB1E9&ui=YRdkHHI8ZU8Ap0ER&t=0&hy=1&ms=6300000&th=6300000&pt=0&f=534068171&alt=0&pks=1101&rts=&vip=PVIP&clientver=&spr=vip&fileid=VN4hEEv3WbpMlmRxG2fvns6oo1&fext=mp4&userid=YRdkHHI8ZU8Ap0ER&clientid=YNxT9w7GMdWvEOKa&projectid=2wks56c31dc80sxm5p9&at=9485D157A2E59FD712B4F65E738A5525",
                    "token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkY2RuaHViX2xldmVsIjo5LCJleHAiOjE2NTU4NTYyMDcsImp0aSI6IlhEUklWRSIsInBlZXJfaWQiOiIiLCJwaHViX2xldmVsIjo5LCJwcm9kdWN0X3R5cGUiOiIxMTAxIiwicHJvZHVjdF92ZXJzaW9uIjoiMCIsInJlc190eXBlIjoiZ2NpZCIsInJlc192YWx1ZSI6IjcwQkY4ODgxMUM2NUJFMEY3OTcwNEM2RTZDN0YxRDU2MzAyNDVGRjAiLCJ1c2VyX2RhdGEiOiJ7XCJQYXJlbnRHY2lkXCI6XCI3MEJGODg4MTFDNjVCRTBGNzk3MDRDNkU2QzdGMUQ1NjMwMjQ1RkYwXCJ9IiwidXNlcl9pZCI6IllSZGtISEk4WlU4QXAwRVIiLCJ2ZXJzaW9uIjoiMi4wLjAifQ.OVMeNIpIyhTWGZYKllPxD62Xnqc-F5XU76ZHZNOdz6e_sxzoaFhgMlgdERAaGKjP_01vJk7nk3egIhA3uJieWVOrztdVDdM2o-JuaEGm3L5pJvzSw7OtLcdM7OTKlThRBXINvckSJVq9SAaZyO0cOmEVoilAdlafikUEqZ99cMk",
                    "expire": "2022-06-22T08:03:27.090+08:00"
               },
               "need_more_quota": false,
               "vip_types": [],
               "redirect_link": "",
               "icon_link": "",
               "is_default": true,
               "priority": 0,
               "is_origin": true,
               "resolution_name": "",
               "is_visible": true,
               "category": ""
          }
     ],
     "trashed": false,
     "delete_time": "",
     "original_url": "",
     "params": {
          "platform_icon": "https://static.mypikpak.com/21ecdc2c6b2372cdee91b193df9a6248b885a1b0",
          "url": "magnet:?xt=urn:btih:2766e108f6f90653008704a988dc0db42f140e6b"
     },
     "original_file_index": 0,
     "space": "",
     "apps": [],
     "writable": true,
     "folder_type": "NORMAL",
     "collection": null
}
```

**down_path** 为设置中设定的下载路径，文件夹内的文件会自动添加父文件夹到路径



# 调用示例

代码使用语言为aardio，也可在aardio中调用Python，以下为示例

## 推送Potplayer

```
//获取文件信息和下载路径
var html,down_path = ...;
import process
import web.json

//将文件信息解析为json
var fileinfo = web.json.parse(html)
//从json中提取出文件直链
var file_url = fileinfo["web_content_link"]


//调用Potplayer，此处换为自己的Potplayer路径
process( "D:\软件\绿色好软\PotPlayer_20180625\PotPlayerMini.exe", file_url, '/insert','/current'  ) 
```

## 推送BitTorrent

```
//获取文件信息和下载路径
var html,down_path = ...;
//调用Python3
import py3;

import preg;

//从Python中引用requests模块
var requests = py3.import("requests");
import web.json

//设置bitcomet的调用地址，更改
var bitcomet_url = "http://账号:密码@192.168.0.92:1235"  + "/panel/task_add_httpftp_result"

//将文件信息解析为json
var fileinfo = web.json.parse(html)
//从json中提取出文件直链
var file_url = fileinfo["web_content_link"]
//从json中提取出文件名称
var file_name = fileinfo["name"]
//下部分为处理下载链接，添加镜像
var regex = preg("(.*?)com");
mirror_url_list=""
domain_key_list = {"https://vod0051-aliyun18-vip-lixian.mypikpak.com",
                   			"https://vod0037-aliyun17-vip-lixian.mypikpak.com",
                   			"https://vod0039-aliyun17-vip-lixian.mypikpak.com",
                   			"https://vod0038-aliyun17-vip-lixian.mypikpak.com",
                   			"https://vod0049-aliyun18-vip-lixian.mypikpak.com",
                   			"https://vod0050-aliyun18-vip-lixian.mypikpak.com",
                   			"https://vod0041-hwyun02-vip-lixian.mypikpak.com",
                   			"https://vod0042-hwyun02-vip-lixian.mypikpak.com",
                   			"https://vod0043-hwyun02-vip-lixian.mypikpak.com"}

for k,v in domain_key_list{
mirror_url_list = mirror_url_list + tostring(regex.replace( file_url,v )) + '\n'
}
//构建请求
var postdata = {
	"url": file_url,
	"save_path": down_path,
	"connection": "200",
	"file_name": file_name,
	"referrer": "",
	"user_agent": "",
	"cookie": "",
	"mirror_url_list": mirror_url_list
}
//向Bittorrnet推送请求
var html = requests.post.invoke(url=bitcomet_url,data=postdata)
```

## 推送MPV

```
//获取文件信息和下载路径
var html,down_path = ...;
import process
import web.json

//将文件信息解析为json
var fileinfo = web.json.parse(html)
//从json中提取出文件直链
var file_url = fileinfo["web_content_link"]
//从json中提取出文件名称
var file_name = fileinfo["name"]

//调用mpv，此处换为自己的mpv路径
process( "\res\MPV\mpv.exe",file_url, "--title="+file_name  )
```



## 推送Aria2(文件直链)

```
var html,down_path = ...;
import inet;
import inet.http;	
import web.json;

//将文件信息解析为json
var fileinfo = web.json.parse(html)
//从json中提取出文件直链
var url = fileinfo['web_content_link']
//从json中提取出文件名称
var file_name = fileinfo['name']



var http = inet.http();
//构建请求,此处pikpakdown修改为自己的token
var  login_data = {'jsonrpc': '2.0', 
			'id': 'qwer',
            'method': 'aria2.addUri',
            'params': {"token:pikpakdown", {url},{"dir": down_path,"out": file_name}}
            };       

//向Aria2推送请求，http://127.0.0.1:29385修改为自己aria2地址，支持https
var html,err,errCode = http.post(  "http://127.0.0.1:29385/jsonrpc" 
	,web.json.stringify(login_data));
http.close();
```



## 推送Aria2(多镜像链接)

```
var html,down_path = ...;
import inet;
import inet.http;	
import web.json;

//将文件信息解析为json
var fileinfo = web.json.parse(html)
//从json中提取出文件直链
var url = fileinfo['web_content_link']
//从json中提取出文件名称
var file_name = fileinfo['name']

//下部分为处理下载链接，添加镜像
var url_list = {}
import preg;
var regex = preg("(.*?)com");
		mirror_url_list=""
		domain_key_list = {"https://vod0051-aliyun18-vip-lixian.mypikpak.com",
                           			"https://vod0037-aliyun17-vip-lixian.mypikpak.com",
                           			"https://vod0039-aliyun17-vip-lixian.mypikpak.com",
                           			"https://vod0038-aliyun17-vip-lixian.mypikpak.com",
                           			"https://vod0049-aliyun18-vip-lixian.mypikpak.com",
                           			"https://vod0050-aliyun18-vip-lixian.mypikpak.com",
                           			"https://vod0041-hwyun02-vip-lixian.mypikpak.com",
                           			"https://vod0042-hwyun02-vip-lixian.mypikpak.com",
                           			"https://vod0043-hwyun02-vip-lixian.mypikpak.com"}
		
for k,v in domain_key_list{
url_list[#url_list+1] =  tostring(regex.replace( url,v )) + ' '
}

var http = inet.http();
//构建请求,此处pikpakdown修改为自己的token
var  login_data = {'jsonrpc': '2.0', 
			'id': 'qwer',
            'method': 'aria2.addUri',
            'params': {"token:pikpakdown", url_list,{"dir": down_path,"out": file_name}}
            };       

//向Aria2推送请求，http://127.0.0.1:29385修改为自己aria2地址，支持https
var html,err,errCode = http.post(  "http://127.0.0.1:29385/jsonrpc" 
	,web.json.stringify(login_data));
http.close();


```

