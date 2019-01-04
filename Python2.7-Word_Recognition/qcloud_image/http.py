# -*- coding: utf-8 -*-

import json
import requests
from .error import Error

class Http(object):
    ''' 发送Http请求，返回Json数据 '''

    @staticmethod
    def post(*args, **kwargs):
        try:
            response = requests.post(*args, **kwargs)
            result = response.json()
            result['httpcode'] = response.status_code

        except Exception as e:
            if 'response' in locals().keys():
                result = Error.json(Error.Network, 'response is not json', response.status_code)
            else:
                result = Error.json(Error.Network, str(e))

        return result

