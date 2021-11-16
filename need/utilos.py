# -*- coding: utf-8 -*-
from io import RawIOBase
import requests
import json


# file io wrapper for requests module
class RequestsIO(RawIOBase):
    def __init__(self, req):
        super(RequestsIO, self).__init__()
        self.req = req
        #self.rptr = self.req.iter_content(CONTENT_CHUNK_SIZE)

    def readable(self):
        return True

    def read(self, n=-1):
        if n == -1:
            return self.req.content
        return self.req.raw.read(n)

    def seekable(self):
        return False

    def writable(self):
        return False

class UrlIO(RawIOBase):
    def __init__(self, url, size=-1, params={}, headers={}, cookies={}, session=None):
        super(UrlIO, self).__init__()
        self.url = url
        self.size = size
        self.offset = 0
        self.last_pos = size - 1
        self.range_mode = False
        self.params = params
        self.headers = headers
        self.cookies = cookies
        self.session = session if session else requests
        self.req = None

    def readable(self):
        return True

    def read(self, n=-1):
        if self.req is None:
            hdrs = self.headers.copy()
            if self.range_mode:
                self.last_pos = (self.size-1) if n == -1 else (self.offset+n-1)
                if self.last_pos >= self.size:
                    self.last_pos = (self.size-1)
                hdrs.update({"Range":"bytes=%d-%d" % (self.offset, self.last_pos)})

            self.req = self.session.get(self.url, params=self.params, headers=hdrs, cookies=self.cookies, stream=True, timeout=50)
        if n == -1:
            _b = self.req.content
        else:
            _b = self.req.raw.read(n)
        m = len(_b)
        self.offset += m
        if self.offset > self.last_pos:
            self.req = None     # fetch next block
        return _b

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2 and self.size >= offset:
            self.offset = self.size - offset
        self.range_mode = True
        self.req = None
        return self.offset

    def tell(self):
        return self.offset

    def writable(self):
        return False

#------------------------------------------------
from lru import LRUCacheDict

_dircache = LRUCacheDict(max_size=100, expiration=100*60)
