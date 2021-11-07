

from cheroot import wsgi
from wsgidav.wsgidav_app import WsgiDAVApp

from need.utilos import UrlIO, _dircache


import time
import os
from wsgidav.dav_provider import DAVProvider, DAVNonCollection, DAVCollection

from need.pikabout import get_list,get_download_info
from PyQt5.QtCore import QThread,pyqtSignal
#输出日志
'''import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("wsgidav")
logger.propagate = True
logger.setLevel(logging.DEBUG)
'''




FILE_FOLDER = r"c:\temp\virtfiles"
_resourceData = [
    {
        "key": "1",
        "title": "My doc 1",
        "orga": "development",
        "tags": ["cool", "hot"],
        "status": "draft",
        "description": "This resource contains two specification files.",
        "resPathList": [
            os.path.join(FILE_FOLDER, "MySpec.doc"),
            os.path.join(FILE_FOLDER, "MySpec.pdf"),
        ],
    },
    {
        "key": "2",
        "title": "My doc 2",
        "orga": "development",
        "tags": ["cool", "nice"],
        "status": "published",
        "description": "This resource contains one file.",
        "resPathList": [os.path.join(FILE_FOLDER, "My URS.doc")],
    },
    {
        "key": "3",
        "title": u"My doc (euro:\u20AC, uuml:��)".encode("utf8"),
        "orga": "marketing",
        "tags": ["nice"],
        "status": "published",
        "description": "Long text describing it",
        "resPathList": [os.path.join(FILE_FOLDER, "My URS.doc")],
    },
]

fileid_dict = {}
user_mapping = {}
def get_path_list(path):
    #按目录结构获取路径信息排列列表
    global fileid_dict
    path_list = []


    temp_path = path
    while temp_path != "":
        path_list.insert(0, temp_path)

        del_path = temp_path [ temp_path.rindex( '/' ) + 1 : len( temp_path  ) ]
        temp_path = temp_path.replace(f"/{del_path}","")

    #path_list.insert(0,"/")

    result_list = get_list("")
    for a in result_list:
        fileid_dict[f"/{a['name']}"] = a['id']

    for a in path_list:
        result_list = get_list(fileid_dict[a])
        for b in result_list:
            fileid_dict[f"{a}/{b['name']}"] = b['id']




def start_get_thetime(timeamp):
    timeamp = str(timeamp)
    time1 = timeamp.split("T")[0]
    time2 = str(timeamp.split("T")[1]).split(".")[0]

    return f"{time1} {time2}"


class MydriveFile(DAVNonCollection):
    """Represents a file."""
    def __init__(self, path, environ, data):
        #        assert name in _artifactNames
        DAVNonCollection.__init__(self, path, environ)
        self.data = data
        self.path = path
        self.info = data


    def get_content_length(self):

        return int(self.info['size'])

    def get_content_type(self):


        return str(self.info['mime_type'])





    def supportRanges(self):
        return False


    def get_ref_url(self):

        return self.path

    def get_display_info(self):

        return {"type": "Content file"}



    def get_etag(self):
        return None

    def get_creation_date(self):

        time_str = str(self.info["modified_time"])


        temp = start_get_thetime(time_str)


        timeArray = time.strptime(str(temp), "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)

        return int(timestamp)

    def get_last_modified(self):


        time_str = str(self.info["modified_time"])


        temp = start_get_thetime(time_str)

        timeArray = time.strptime(str(temp), "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)

        return int(timestamp)



    def get_content(self):
        file_id = self.info['id']
        url = get_download_info(file_id=file_id)["web_content_link"]

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):获取下载链接:{url}")
        default_headers = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',

        }
        #return requests.get(url, headers=default_headers,stream=True).content
        return UrlIO(url,size=int(self.info['size']),headers=default_headers)




'''class CategoryTypeCollection(DAVCollection):
    """Resolve '/catType' URLs, for example '/by_tag'."""

    def __init__(self, path, environ):
        DAVCollection.__init__(self, path, environ)

    def get_display_info(self):
        return {"type": "Category type"}

    def get_member_names(self):
        names = []
        for data in _resourceData:
            if self.name == "by_status":
                if not data["status"] in names:
                    names.append(data["status"])
            elif self.name == "by_orga":
                if not data["orga"] in names:
                    names.append(data["orga"])
            elif self.name == "by_tag":
                for tag in data["tags"]:
                    if tag not in names:
                        names.append(tag)

        names.sort()
        print(f"1 {names}")
        return names'''

class RootCollection(DAVCollection):
    """Resolve top-level requests '/'."""

    '''_visibleMemberNames = ("by_orga", "by_tag", "by_status")
    _validMemberNames = _visibleMemberNames + ("by_key",)'''

    def __init__(self,path, environ):
        DAVCollection.__init__(self, path, environ)
        self.path = path

        self.abspath = path
        try:
            self.result_list = _dircache[self.abspath]
        except KeyError:
            self.result_list = None



    def get_creation_date(self):

        return None

    def get_last_modified(self):

        return None

    def get_member_names(self):


        global fileid_dict
        if self.result_list is None:
            if self.path == "/":
                self.result_list =get_list("")
                for a in self.result_list:
                    fileid_dict[f"{self.path}{a['name']}"] = a['id']
            else:

                if self.path in fileid_dict:
                    self.result_list = get_list(fileid_dict[str(self.path)])
                else:
                    get_path_list(self.path)
                    self.result_list = get_list(fileid_dict[str(self.path)])

            _dircache[self.abspath] = self.result_list



        self.file_list = [item['name'] for item in self.result_list]

        return self.file_list

    def getDisplayInfo(self):
        return {"type": "Collection"}

    def get_member(self, name):
        # Handle visible categories and also /by_key/...
        global fileid_dict

        if self.result_list is None:
            if self.path=="/":
                self.result_list = get_list("")
            elif self.path in fileid_dict:
                self.result_list = get_list(fileid_dict[str(self.path)])
            else:
                get_path_list(self.path)
                self.result_list = get_list(fileid_dict[str(self.path)])
            _dircache[self.abspath] = self.result_list


        for item in self.result_list:
            bname = item['name']
            # path = joinUrl(self.path, name)
            path = item['name']

            if bname == name:
                if item['kind'] == "drive#folder":



                    new_path = str(os.path.join(self.path, name)).replace("\\","/")
                    return RootCollection(new_path, self.environ)
                else:



                    new_path = str(os.path.join(self.path, name)).replace("\\","/")
                    return MydriveFile(new_path, self.environ, item)
                    #return _VirtualNonCollection(join_uri(self.path, name), self.environ)
                    #return CategoryTypeCollection(join_uri(self.path, name), self.environ)


        #return None


#调用入口
class VirtualResourceProvider(DAVProvider):
    """
    DAV provider that serves a VirtualResource derived structure.
    """

    def __init__(self):
        super(VirtualResourceProvider, self).__init__()
        self.resourceData = _resourceData

    def get_resource_inst(self, path, environ):
        """Return _VirtualResource object for path.

        path is expected to be
            categoryType/category/name/artifact
        for example:
            'by_tag/cool/My doc 2/info.html'

        See DAVProvider.get_resource_inst()
        """


        self._count_get_resource_inst += 1
        #初始化，开始信息
        root = RootCollection("/",environ)
        return root.resolve("", path)





#开启webdav线程
class Open_webdav_Worker(QThread):
    valueChanged = pyqtSignal(list)  # 值变化信号

    def __init__(self, admin,password,port):
        super(Open_webdav_Worker, self).__init__()

        self.admin = admin
        self.password = password
        self.port = port

        new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        print(f"INFO ({new_time}):开启webdav：账号{self.admin} 密码：{self.password}")


    def run(self):

        config = {
            "host": "0.0.0.0",
            "port": int(self.port),
            "provider_mapping": {
                "/": VirtualResourceProvider(),
            },

            "verbose": 0,
            # "simple_dc": {"user_mapping": {"*": True}},  # anonymous access
            "simple_dc": {"user_mapping": {'/':
                                               {str(self.admin): {'password': str(self.password), 'description': '', 'roles': []
                                                             }
                                                }
                                           }},
            "hotfixes": {
                "emulate_win32_lastmod": True,  # True: support Win32LastModifiedTime
                "re_encode_path_info": None,  # (See issue #73) None: activate on Python 3
                "unquote_path_info": False,  # See issue #8
                "win_accept_anonymous_options": False,
                "winxp_accept_root_share_login": True,  # Was True in v2.4
            },
        }

        app = WsgiDAVApp(config)

        server_args = {
            "bind_addr": (config["host"], config["port"]),
            "wsgi_app": app,
        }
        server = wsgi.Server(**server_args)
        server.start()

