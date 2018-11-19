# -*- coding: utf-8 -*-

class Error(object):
    """sdk错误码"""

    Param    = -1  # 参数错误
    Network  = -2  # 网络错误
    FilePath = -3  # 文件不存在
    UNKNOWN  = -4  # 未知错误

    @staticmethod
    def json(code, message, httpcode=0):
        return {
                'httpcode': httpcode,
                'code': code,
                'message': message,
                'data':{},
                }

