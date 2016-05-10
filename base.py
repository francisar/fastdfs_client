#!/usr/bin/env python
# coding=utf-8

import struct

class Fdfs_Header(object):

    def __init__(self):
        self._fmt = '!QBB'
        self._st = struct.Struct(self._fmt)

    def pack(self, pkg_len=0, cmd=0, status=0):
        return self.st.pack(pkg_len, cmd, status)

    def unpack(self, bytes_stream):
        self.pkg_len, self.cmd, self.status = self.st.unpack(bytes_stream)
        return True

    def header_len(self):
        return self.st.size



