# -*- coding: utf-8 -*-

import time
import random
import hmac
import hashlib
import binascii
import base64

class Auth(object):

    def __init__(self, appid, sid, skey):
        self._appid, self._secretid, self._secretkey = str(appid), str(sid), str(skey)

    def get_sign(self, bucket, howlong=30):
        """ GET REUSABLE SIGN

        :param bucket: 图片处理所使用的 bucket
        :param howlong: 签名的有效时长，单位 秒

        :return: 签名字符串
        """
        
        if howlong <= 0:
            raise Exception('Param howlong must be great than 0')

        now = int(time.time())
        rdm = random.randint(0, 999999999)

        text = 'a='+self._appid + '&b='+bucket + '&k='+self._secretid + '&e='+str(now+howlong) + '&t='+str(now) + '&r='+str(rdm) + '&f='
        hexstring = hmac.new(self._secretkey.encode('utf-8'), text.encode('utf-8'), hashlib.sha1).hexdigest()
        binstring = binascii.unhexlify(hexstring)

        return base64.b64encode(binstring+text.encode('utf-8')).rstrip()

