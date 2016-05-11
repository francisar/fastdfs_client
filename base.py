#!/usr/bin/env python
# coding=utf-8

import struct
from fdfs_protocol.constant import *

class FdfsHeader(object):

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

    def pkg_len(self):
        return self.pkg_len

    def status(self):
        return self.status

'''
typedef struct
{
	char group_name[FDFS_GROUP_NAME_MAX_LEN+1];
	char storage_port[FDFS_PROTO_PKG_LEN_SIZE];
	char storage_http_port[FDFS_PROTO_PKG_LEN_SIZE];
	char store_path_count[FDFS_PROTO_PKG_LEN_SIZE];
	char subdir_count_per_path[FDFS_PROTO_PKG_LEN_SIZE];
	char upload_priority[FDFS_PROTO_PKG_LEN_SIZE];
	char join_time[FDFS_PROTO_PKG_LEN_SIZE]; //storage join timestamp
	char up_time[FDFS_PROTO_PKG_LEN_SIZE];   //storage service started timestamp
	char version[FDFS_VERSION_SIZE];   //storage version
	char domain_name[FDFS_DOMAIN_NAME_MAX_SIZE];
	char init_flag;
	signed char status;
	char tracker_count[FDFS_PROTO_PKG_LEN_SIZE];  //all tracker server count
} TrackerStorageJoinBody;
'''

class TrackerStorageJoinBody(object):

    def __init__(self):
        self._fmt = '!%ds 11Q' % (FDFS_GROUP_NAME_MAX_LEN + 1)
        self._st = struct.Struct(self._fmt)