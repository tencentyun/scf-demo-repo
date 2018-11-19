# -*- coding: utf-8 -*-

import os
import time
import json
import sys
import base64
import urllib

from .error import Error
from .http import Http
from .auth import Auth
from .conf import Conf
from .type import *

class Client(object):

    def __init__(self, appid, sid, skey, bucket):
        self._auth = Auth(appid, sid, skey)
        self._bucket = bucket
        self._conf = Conf()


    def use_http(self):
        return self._conf.use_http()
    def use_https(self):
        return self._conf.use_https()
    def set_timeout(self, timeout):
        return self._conf.set_timeout(timeout)
    
    def porn_detect(self, pictures):
        ''' 黄图识别

        :param pictures: 图片
        :type  picture: CIFiles  or CIUrls
        
        '''

        if not isinstance(pictures, CIUrls) and not isinstance(pictures, CIFiles):
            return Error.json(Error.Param, 'param pictures must be instance of CIUrls or CIFiles')
        if not pictures:
            return Error.json(Error.Param, 'param pictures is empty')

        requrl = self._conf.build_url('/detection/pornDetect')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
        }
        
        if isinstance(pictures, CIUrls):
            headers['Content-Type'] = 'application/json'
            
            files['url_list'] = pictures
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            i=0
            for image in pictures:
                if sys.version_info < (3, 0) :
                    filename = urllib.quote(image)    
                    image = image.decode('utf-8')                             
                else:
                    filename = urllib.parse.quote(image)
                    
                local_path = os.path.abspath(image)
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')
                
                files['images['+str(i)+']'] = (filename, open(image,'rb'))
                i = i+1

            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())
    
    def tag_detect(self, picture):
        ''' 标签识别

        :param picture: 识别的图片
        :type  picture: CIFile or CIBuffer or CIUrl

        '''

        if not isinstance(picture, CIUrl) and not isinstance(picture, CIFile) and not isinstance(picture, CIBuffer):
            return Error.json(Error.Param, 'param picture must be instance of CIUrl or CIFile or CIBuffer')
        if not picture:
            return Error.json(Error.Param, 'param picture is empty')

        requrl = self._conf.build_url('/v1/detection/imagetag_detect')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
        }

        if isinstance(picture, CIUrl):
            headers['Content-Type'] = 'application/json'
            files['url'] = picture
            #return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(picture, CIFile):
                if sys.version_info < (3, 0) and isinstance(picture, str):
                    image = picture.decode('utf-8')
                else: 
                    image = picture           
                    
                local_path = os.path.abspath(image)
                
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')
                
                files['image'] = base64.b64encode(open(local_path,'rb').read()).decode()
                #return Error.json(Error.Param, files['image'])
            else:
                files['image'] = base64.b64encode(picture).decode()
               
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())
        
    def idcard_detect(self, pictures,  cardType=0):
        ''' 身份证识别
        
        :param pictures: 需要添加的图片
        :type  pictures: CIFiles or CIBuffers or CIUrls

        :param cardType:  0为身份证有照片的一面，1为身份证有国徽的一面                
        '''
        if not isinstance(pictures, CIUrls) and not isinstance(pictures, CIFiles) and not isinstance(pictures, CIBuffers):
            return Error.json(Error.Param, 'param pictures must be instance of CIUrls or CIFiles or CIBuffers')
        if len(pictures) == 0:
            return Error.json(Error.Param, 'param pictures is empty')

        requrl = self._conf.build_url('/ocr/idcard')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'card_type':str(cardType)
        }
        
        if isinstance(pictures, CIUrls):
            headers['Content-Type'] = 'application/json'
            files['card_type'] = cardType
            files['url_list'] = pictures
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(pictures, CIFiles):
                i=0
                for image in pictures:
                    if sys.version_info < (3, 0) :
                        filename = urllib.quote(image)    
                        image = image.decode('utf-8')                             
                    else:
                        filename = urllib.parse.quote(image)

                    local_path = os.path.abspath(image)
                    if not os.path.exists(local_path):
                        return Error.json(Error.FilePath, 'file '+image+' not exists')
                    
                    if not os.path.isfile(local_path):
                        return Error.json(Error.FilePath, local_path+' is not file')
                
                    files['images['+str(i)+']'] = (filename, open(image,'rb'))
                    i = i+1
            else:
                i=0
                for buffer in pictures:
                    files['images['+str(i)+']'] = buffer
                    i = i+1
                                      
            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())
     
    def namecard_detect(self, pictures, retImage=0):
        '''名片识别
        
        :param pictures: 需要识别的图片
        :type  pictures: CIFiles or CIBuffers or CIUrls

        '''
        if not isinstance(pictures, CIUrls) and not isinstance(pictures, CIFiles) and not isinstance(pictures, CIBuffers):
            return Error.json(Error.Param, 'param pictures must be instance of CIUrls or CIFiles or CIBuffers')
        if len(pictures) == 0:
            return Error.json(Error.Param, 'param pictures is empty')

        requrl = self._conf.build_url('/ocr/namecard')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'ret_image':str(retImage)
        }
        
        if isinstance(pictures, CIUrls):
            headers['Content-Type'] = 'application/json'

            files['url_list'] = pictures
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(pictures, CIFiles):
                i=0
                for image in pictures:
                    if sys.version_info < (3, 0) :
                        filename = urllib.quote(image)    
                        image = image.decode('utf-8')                             
                    else:
                        filename = urllib.parse.quote(image)
                    
                    local_path = os.path.abspath(image)
                    if not os.path.exists(local_path):
                        return Error.json(Error.FilePath, 'file '+image+' not exists')
                    
                    if not os.path.isfile(local_path):
                        return Error.json(Error.FilePath, local_path+' is not file')
                    files['images['+str(i)+']'] = (filename, open(image,'rb'))
                    i = i+1

            else:
                i=0
                for buffer in pictures:
                    files['images['+str(i)+']'] = buffer
                    i = i+1

            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())
           
    def face_newperson(self, person_id, group_ids, picture, person_name=None, tag=None):
        ''' 创建 Person

        :param group_ids: person需要加入的group_id的数组
        :type  group_ids: list<string>

        :param person_id: 创建的person的id
        :type  person_id: string

        :param picture: person的人脸图片
        :type  picture: CIFile or CIBuffer or CIUrl

        :param person_name: person的名字
        :param tag: 为person打标签
        '''

        if not isinstance(group_ids, list):
            return Error.json(Error.Param, 'param group_ids error')
        if len(group_ids) == 0:
            return Error.json(Error.Param, 'param group_ids cannot be empty')
        if not isinstance(picture, CIUrl) and not isinstance(picture, CIFile) and not isinstance(picture, CIBuffer):
            return Error.json(Error.Param, 'param picture must be instance of CIUrl or CIFile or CIBuffer')
        if not picture:
            return Error.json(Error.Param, 'param picture is empty')

        requrl = self._conf.build_url('/face/newperson')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'person_id': str(person_id),
        }
        if person_name:
            files['person_name'] = str(person_name)
        if tag:
            files['tag'] = str(tag)

        if isinstance(picture, CIUrl):
            headers['Content-Type'] = 'application/json'

            files['group_ids'] = group_ids
            files['url'] = picture
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            i = 0
            for group_id in group_ids:
                files['group_ids['+str(i)+']'] = str(group_id)
                i = i+1

            if isinstance(picture, CIFile):
                if sys.version_info < (3, 0) :
                    filename = urllib.quote(picture)    
                    image = picture.decode('utf-8')                             
                else:
                    filename = urllib.parse.quote(picture)
                    image = picture                 
                    
                local_path = os.path.abspath(image)
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')                
                files['image'] = (filename, open(local_path,'rb'))

            else:
                files['image'] = picture

            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_delperson(self, person_id):
        ''' 创建 Person

        :param person_id: 删除的person的id
        :type  person_id: string
        '''

        requrl = self._conf.build_url('/face/delperson')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'person_id': str(person_id),
        }
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_addface(self, person_id, pictures, tag=None):
        ''' 为Person 添加人脸

        :param person_id: 需要添加人脸的person的id
        :type  person_id: string

        :param pictures: 需要添加的人脸
        :type  pictures: CIFiles or CIBuffers or CIUrls

        :param tag: 为face打标签
        '''

        if not isinstance(pictures, CIUrls) and not isinstance(pictures, CIFiles) and not isinstance(pictures, CIBuffers):
            return Error.json(Error.Param, 'param pictures must be instance of CIUrls or CIFiles or CIBuffers')
        if len(pictures) == 0:
            return Error.json(Error.Param, 'param pictures is empty')

        requrl = self._conf.build_url('/face/addface')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'person_id': str(person_id),
        }
        if tag:
            files['tag'] = str(tag)

        if isinstance(pictures, CIUrls):
            headers['Content-Type'] = 'application/json'

            files['urls'] = pictures
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(pictures, CIFiles):
                i=0
                for image in pictures:
                    if sys.version_info < (3, 0) :
                        filename = urllib.quote(image)    
                        image = image.decode('utf-8')                             
                    else:
                        filename = urllib.parse.quote(image)     

                    local_path = os.path.abspath(image)
                    if not os.path.exists(local_path):
                        return Error.json(Error.FilePath, 'file '+image+' not exists')
                    
                    if not os.path.isfile(local_path):
                        return Error.json(Error.FilePath, local_path+' is not file') 
                     
                    files['images['+str(i)+']'] = (filename, open(image,'rb'))
                    i = i+1

            else:
                i=0
                for buffer in pictures:
                    files['images['+str(i)+']'] = buffer
                    i = i+1

            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_delface(self, person_id, face_ids):
        ''' 删除 Person的face

        :param person_id: 需要删除face的person的id
        :type  person_id: string

        :param face_ids: 需要删除的face的id
        :type  face_ids: list<string>
        '''

        requrl = self._conf.build_url('/face/delface')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'person_id': str(person_id),
            'face_ids': face_ids
        }
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_setinfo(self, person_id, person_name=None, tag=None):
        ''' 为 Person设置信息

        :param person_id: 操作的person的id
        :type  person_id: string

        :param person_name: person的名字
        :param tag: 为person打标签
        '''

        requrl = self._conf.build_url('/face/setinfo')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'person_id': str(person_id),
        }
        if person_name:
            files['person_name']=person_name
        if tag:
            files['tag'] = tag
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_getinfo(self, person_id):
        ''' 获取 Person信息

        :param person_id: 操作的person的id
        :type  person_id: string
        '''

        requrl = self._conf.build_url('/face/getinfo')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'person_id': str(person_id),
        }
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_getgroupids(self):
        ''' 获取appid下的组列表 
        '''

        requrl = self._conf.build_url('/face/getgroupids')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
        }
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_getpersonids(self, group_id):
        ''' 获取 Person信息

        :param group_id: 需要获取列表的groupid
        :type  group_id: string
        '''

        requrl = self._conf.build_url('/face/getpersonids')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'group_id': str(group_id),
        }
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_getfaceids(self, person_id):
        ''' 获取 Person的人脸列表

        :param person_id: 操作的person的id
        :type  person_id: string
        '''

        requrl = self._conf.build_url('/face/getfaceids')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'person_id': str(person_id),
        }
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_getfaceinfo(self, face_id):
        ''' 获取 face的信息

        :param face_id: 操作的face的id
        :type  face_id: string
        '''

        requrl = self._conf.build_url('/face/getfaceinfo')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'face_id': str(face_id),
        }
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_identify(self, group_id, picture):
        ''' 识别指定的图片是指定group_id中的哪个Person

        :param group_id: 需要对比的group_id
        :type  group_id: string

        :param picture: 人脸图片
        :type  picture: CIFile or CIBuffer or CIUrl
        '''

        if not isinstance(picture, CIUrl) and not isinstance(picture, CIFile) and not isinstance(picture, CIBuffer):
            return Error.json(Error.Param, 'param picture must be instance of CIUrl or CIFile or CIBuffer')
        if not picture:
            return Error.json(Error.Param, 'param picture is empty')

        requrl = self._conf.build_url('/face/identify')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'group_id': str(group_id),
        }

        if isinstance(picture, CIUrl):
            headers['Content-Type'] = 'application/json'

            files['url'] = picture
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(picture, CIFile):
                if sys.version_info < (3, 0) :
                    filename = urllib.quote(picture)    
                    image = picture.decode('utf-8')                             
                else:
                    filename = urllib.parse.quote(picture)   
                    image = picture

                local_path = os.path.abspath(image)
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')  
                
                files['image'] = (filename, open(local_path,'rb'))

            else:
                files['image'] = picture

            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_verify(self, person_id, picture):
        ''' 识别指定的图片是指定group_id中的哪个Person

        :param person_id: 需要对比的person
        :type  person_id: string

        :param picture: 人脸图片
        :type  picture: CIFile or CIBuffer or CIUrl
        '''

        if not isinstance(picture, CIUrl) and not isinstance(picture, CIFile) and not isinstance(picture, CIBuffer):
            return Error.json(Error.Param, 'param picture must be instance of CIUrl or CIFile or CIBuffer')
        if not picture:
            return Error.json(Error.Param, 'param picture is empty')

        requrl = self._conf.build_url('/face/verify')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'person_id': str(person_id),
        }

        if isinstance(picture, CIUrl):
            headers['Content-Type'] = 'application/json'

            files['url'] = picture
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(picture, CIFile):
                if sys.version_info < (3, 0) :
                    filename = urllib.quote(picture)    
                    image = picture.decode('utf-8')                             
                else:
                    filename = urllib.parse.quote(picture)   
                    image = picture
                    
                local_path = os.path.abspath(image)
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')  
                
                files['image'] = (filename, open(local_path,'rb'))

            else:
                files['image'] = picture

            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_compare(self, pictureA, pictureB):
        ''' 对比两张图片是否是同一个人

        :param pictureA: 人脸图片
        :type  pictureA: CIFile or CIBuffer or CIUrl

        :param pictureB: 人脸图片
        :type  pictureB: CIFile or CIBuffer or CIUrl
        '''

        if not isinstance(pictureA, CIUrl) and not isinstance(pictureA, CIFile) and not isinstance(pictureA, CIBuffer):
            return Error.json(Error.Param, 'param pictureA must be instance of CIUrl or CIFile or CIBuffer')
        if not pictureA:
            return Error.json(Error.Param, 'param pictureA is empty')

        if not isinstance(pictureB, CIUrl) and not isinstance(pictureB, CIFile) and not isinstance(pictureB, CIBuffer):
            return Error.json(Error.Param, 'param pictureB must be instance of CIUrl or CIFile or CIBuffer')
        if not pictureB:
            return Error.json(Error.Param, 'param pictureB is empty')

        requrl = self._conf.build_url('/face/compare')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
        }

        if isinstance(pictureA, CIUrl):
            files['urlA'] = pictureA
        elif isinstance(pictureA, CIFile):
            if sys.version_info < (3, 0) :
                filename = urllib.quote(pictureA)    
                image = pictureA.decode('utf-8')                             
            else:
                filename = urllib.parse.quote(pictureA)   
                image = pictureA              
                    
            local_path = os.path.abspath(image)
            if not os.path.exists(local_path):
                return Error.json(Error.FilePath, 'file '+image+' not exists')
            
            if not os.path.isfile(local_path):
                return Error.json(Error.FilePath, local_path+' is not file')  
            files['imageA'] = (filename, open(local_path,'rb'))
        else:
            files['imageA'] = pictureA

        if isinstance(pictureB, CIUrl):
            files['urlB'] = pictureB
        elif isinstance(pictureB, CIFile):
            if sys.version_info < (3, 0) :
                filename = urllib.quote(pictureB)    
                image = pictureB.decode('utf-8')                             
            else:
                filename = urllib.parse.quote(pictureB)
                image = pictureB  
                
            local_path = os.path.abspath(image)
            if not os.path.exists(local_path):
                return Error.json(Error.FilePath, 'file '+image+' not exists')
            
            if not os.path.isfile(local_path):
                return Error.json(Error.FilePath, local_path+' is not file')  
            files['imageB'] = (filename, open(local_path,'rb'))
        else:
            files['imageB'] = pictureB

        if isinstance(pictureA, CIUrl) and isinstance(pictureB, CIUrl):
            headers['Content-Type'] = 'application/json'
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_detect(self, picture, mode=0):
        ''' 检测图中的人脸

        :param picture: 人脸图片
        :type  picture: CIFile or CIBuffer or CIUrl

        :param mode: 检测的模式，0为所有人的脸，1为最大的人脸
        :type  mode: int
        '''

        if not isinstance(picture, CIUrl) and not isinstance(picture, CIFile) and not isinstance(picture, CIBuffer):
            return Error.json(Error.Param, 'param picture must be instance of CIUrl or CIFile or CIBuffer')
        if not picture:
            return Error.json(Error.Param, 'param picture is empty')
        if mode != 0 and mode != 1:
            return Error.json(Error.Param, 'param mode must be 0 or 1')

        requrl = self._conf.build_url('/face/detect')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
        }

        if isinstance(picture, CIUrl):
            headers['Content-Type'] = 'application/json'
            files['mode'] = mode
            files['url'] = picture
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(picture, CIFile):
                if sys.version_info < (3, 0) :
                    filename = urllib.quote(picture)    
                    image = picture.decode('utf-8')                             
                else:
                    filename = urllib.parse.quote(picture) 
                    image = picture 
                
                local_path = os.path.abspath(image)
                
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')  
                
                files['image'] = (filename, open(local_path,'rb'))

            else:
                files['image'] = picture

            files['mode'] = str(mode)
            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_shape(self, picture, mode=0):
        ''' 定位图中的人脸的五官信息

        :param picture: 人脸图片
        :type  picture: CIFile or CIBuffer or CIUrl

        :param mode: 检测的模式，0为所有人的脸，1为最大的人脸
        :type  mode: int
        '''

        if not isinstance(picture, CIUrl) and not isinstance(picture, CIFile) and not isinstance(picture, CIBuffer):
            return Error.json(Error.Param, 'param picture must be instance of CIUrl or CIFile or CIBuffer')
        if not picture:
            return Error.json(Error.Param, 'param picture is empty')
        if mode != 0 and mode != 1:
            return Error.json(Error.Param, 'param mode must be 0 or 1')

        requrl = self._conf.build_url('/face/shape')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
        }

        if isinstance(picture, CIUrl):
            headers['Content-Type'] = 'application/json'
            files['mode'] = mode
            files['url'] = picture
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(picture, CIFile):
                if sys.version_info < (3, 0) :
                    filename = urllib.quote(picture)    
                    image = picture.decode('utf-8')                             
                else:
                    filename = urllib.parse.quote(picture)  
                    image = picture                    
                    
                local_path = os.path.abspath(image)
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')  
                
                files['image'] = (filename, open(local_path,'rb'))

            else:
                files['image'] = picture

            files['mode'] = str(mode)
            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_idcardcompare(self, idcard_number, idcard_name, picture):
        ''' 检测picture中的人和给定的信息是否相同

        :param idcard_number: 身份证号
        :type  idcard_number: string

        :param idcard_name: 姓名
        :type  idcard_name: string

        :param picture: 人脸图片
        :type  picture: CIFile or CIBuffer or CIUrl
        '''

        if not isinstance(picture, CIUrl) and not isinstance(picture, CIFile) and not isinstance(picture, CIBuffer):
            return Error.json(Error.Param, 'param picture must be instance of CIUrl or CIFile or CIBuffer')
        if not picture:
            return Error.json(Error.Param, 'param picture is empty')

        requrl = self._conf.build_url('/face/idcardcompare')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'idcard_number': str(idcard_number),
            'idcard_name': str(idcard_name),
        }

        if isinstance(picture, CIUrl):
            headers['Content-Type'] = 'application/json'

            files['url'] = picture
            return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())

        else:
            if isinstance(picture, CIFile):
                if sys.version_info < (3, 0) :
                    filename = urllib.quote(picture)    
                    image = picture.decode('utf-8')                             
                else:
                    filename = urllib.parse.quote(picture)
                    image = picture
                    
                local_path = os.path.abspath(image)
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')  
                
                files['image'] = (filename, open(local_path,'rb'))

            else:
                files['image'] = picture

            return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_livegetfour(self, seq=None):
        ''' 活体检测第一步：获取 唇语(验证码)

        :param seq: 指定一个session_id，若指定，请确保每次请求的session_id唯一
        :type  seq: string
        '''

        requrl = self._conf.build_url('/face/livegetfour')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type':'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
        }
        if seq:
            files['seq'] = seq
        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


    def face_livedetectfour(self, validate_data, video, compare_flag, card=None, seq=None):
        ''' 活体检测第二步：检测

        :param validate_data: 由face_livegetfour返回的验证码
        :type  validate_data: string

        :param video: 拍摄的视频
        :type  video: CIFile or CIBuffer

        :param compare_flag: 是否将视频中的人与card做对比
        :type  compare_flag: Bool

        :param card: 需要对比的人脸图片
        :type  card: CIFile or CIBuffer 

        :param seq: 指定一个session_id，若指定，请确保每次请求的session_id唯一
        :type  seq: string
        '''

        if not isinstance(video, CIFile) and not isinstance(video, CIBuffer):
            return Error.json(Error.Param, 'param video must be instance of CIFile or CIBuffer')
        if not video:
            return Error.json(Error.Param, 'param video is empty')


        requrl = self._conf.build_url('/face/livedetectfour')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'validate_data': str(validate_data),
        }

        if isinstance(video, CIFile):
            if sys.version_info < (3, 0) :
                filename = urllib.quote(video)    
                image = video.decode('utf-8')                             
            else:
                filename = urllib.parse.quote(video)
                image = video               
                    
            local_path = os.path.abspath(image)
            if not os.path.exists(local_path):
                return Error.json(Error.FilePath, 'file '+image+' not exists')
            
            if not os.path.isfile(local_path):
                return Error.json(Error.FilePath, local_path+' is not file')  
            
            files['video'] = (filename, open(local_path,'rb'))

        else:
            files['video'] = video

        if compare_flag:
            if not isinstance(card, CIFile) and not isinstance(card, CIBuffer):
                return Error.json(Error.Param, 'param card must be instance of CIFile or CIBuffer')
            if not card:
                return Error.json(Error.Param, 'param card is empty')

            if isinstance(card, CIFile):
                if sys.version_info < (3, 0) :
                    filename = urllib.quote(card)    
                    image = card.decode('utf-8')                             
                else:
                    filename = urllib.parse.quote(card)
                    image = card   

                local_path = os.path.abspath(image)
                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file '+image+' not exists')
                
                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path+' is not file')  
                
                files['card'] = (filename, open(local_path,'rb'))

            else:
                files['card'] = card

            files['compare_flag'] = 'true'
        else:
            files['compare_flag'] = 'false'

        if seq:
            files['seq'] = str(seq)

        return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())


    def face_idcardlivedetectfour(self, validate_data, video, idcard_number, idcard_name, seq=None):
        ''' 活体检测第二步：检测--指定身份信息

        :param validate_data: 由face_livegetfour返回的验证码
        :type  validate_data: string

        :param video: 拍摄的视频
        :type  video: CIFile or CIBuffer

        :param idcard_number: 身份证号
        :type  idcard_number: string

        :param idcard_name: 姓名
        :type  idcard_name: string

        :param seq: 指定一个session_id，若指定，请确保每次请求的session_id唯一
        :type  seq: string
        '''

        if not isinstance(video, CIFile) and not isinstance(video, CIBuffer):
            return Error.json(Error.Param, 'param video must be instance of CIFile or CIBuffer')
        if not video:
            return Error.json(Error.Param, 'param video is empty')


        requrl = self._conf.build_url('/face/idcardlivedetectfour')
        headers = {
            'Host': self._conf.host(),
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket,
            'validate_data': str(validate_data),
            'idcard_number': str(idcard_number),
            'idcard_name': str(idcard_name),
        }

        if isinstance(video, CIFile):
            if sys.version_info < (3, 0) :
                filename = urllib.quote(video)    
                image = video.decode('utf-8')                             
            else:
                filename = urllib.parse.quote(video)
                image = video                     

            local_path = os.path.abspath(image)
            if not os.path.exists(local_path):
                return Error.json(Error.FilePath, 'file '+image+' not exists')
            
            if not os.path.isfile(local_path):
                return Error.json(Error.FilePath, local_path+' is not file')  
            files['video'] = (filename, open(local_path,'rb'))

        else:
            files['video'] = video

        if seq:
            files['seq'] = str(seq)

        return Http.post(requrl, headers=headers, files=files, timeout=self._conf.timeout())

    def word_detect(self, picture):
        ''' 文字识别
        :param pictures: 需要添加的图片
        :type  pictures: CIFiles or CIBuffers or CIUrls
        '''

        if not isinstance(picture, CIUrl) and not isinstance(picture, CIFile) and not isinstance(picture, CIBuffer):
            return Error.json(Error.Param, 'param picture must be instance of CIUrl or CIFile or CIBuffer')
        if not picture:
            return Error.json(Error.Param, 'param picture is empty')

        requrl = "http://recognition.image.myqcloud.com/ocr/general"
        headers = {
            'Host': 'recognition.image.myqcloud.com',
            'Authorization': self._auth.get_sign(self._bucket),
            'User-Agent': Conf.get_ua(self._auth._appid),
            'Content-Type' : 'application/json',
        }
        files = {
            'appid': self._auth._appid,
            'bucket': self._bucket
        }

        if isinstance(picture, CIUrl):
            headers['Content-Type'] = 'application/json'
            # headers['Content-Type'] = 'multipart/form-data'
            files['url'] = picture

        else:
            if isinstance(picture, CIFile):
                if sys.version_info < (3, 0) and isinstance(picture, str):
                    image = picture.decode('utf-8')
                else:
                    image = picture

                local_path = os.path.abspath(image)

                if not os.path.exists(local_path):
                    return Error.json(Error.FilePath, 'file ' + image + ' not exists')

                if not os.path.isfile(local_path):
                    return Error.json(Error.FilePath, local_path + ' is not file')

                files['image'] = base64.b64encode(open(local_path, 'rb').read()).decode()
                # files['image'] = open(local_path, 'rb').read()
                # print("files[image] is %s" % files['image'] )

            else:
                files['image'] = base64.b64encode(picture).decode()
                # files['image'] = picture

        return Http.post(requrl, headers=headers, data=json.dumps(files), timeout=self._conf.timeout())


