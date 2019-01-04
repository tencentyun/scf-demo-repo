# -*- coding: utf-8 -*-

import platform
from . import __version__

class Conf(object):

    __SERVICE_ADDR = 'service.image.myqcloud.com'
    __HEADER_HOST = 'service.image.myqcloud.com'

    def __init__(self):
        self.__REQ_TIMEOUT = 60
        self.__SCHEME = 'http'

    def use_http(self):
        self.__SCHEME = 'http'
    def use_https(self):
        self.__SCHEME = 'https'
    def set_timeout(self, timeout):
        if timeout > 0:
            self.__REQ_TIMEOUT = timeout

    def timeout(self):
        return self.__REQ_TIMEOUT
    def host(self):
        return Conf.__HEADER_HOST

    def build_url(self, uri):
        return self.__SCHEME + '://' + Conf.__SERVICE_ADDR + '/' + uri.lstrip('/')

    @staticmethod
    def get_ua(appid=None):
        ua = 'CIPythonSDK/'+__version__+' ('+platform.platform()+')';
        if appid:
            ua = ua + ' User('+appid+')'
        return ua

