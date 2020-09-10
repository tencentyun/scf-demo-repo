# -*- coding: utf-8 -*-

#####----------------------------------------------------------------#####
#####                                                                #####
#####   使用教程/readme:                                              #####
#####   https://cloud.taifucloud.com/document/product/583/47075         #####
#####                                                                #####
#####----------------------------------------------------------------#####

import os
from qcloud_cos_v5 import CosConfig
from qcloud_cos_v5 import CosS3Client
import logging
import PIL
from PIL import ImageFont, ImageDraw, Image,ImageOps
import sys
import pygame

reload(sys)
sys.setdefaultencoding('utf8')

region = os.environ.get('region')
target_bucket = os.environ.get('target_bucket')
target_path = os.environ.get('target_path')

#控制log輸出級别
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

#  原圖到tmp目錄，并且賦予權限,tmp是雲函數的本地磁盤空間，可讀可寫
with open("./source.jpg", "rb") as rf:
    with open("/tmp/source.jpg", "wb") as wf:
        wf.write(rf.read())

#删除本地文件
def delete_local_file(src):
    logger.info("delete files and folders")
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            delete_local_file(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass

def main_handler(event, context):
    logger.info("start main handler")
    #使用臨時秘鑰初始化COS Client
    secret_id = os.environ.get('TENCENTCLOUD_SECRETID')      
    secret_key = os.environ.get('TENCENTCLOUD_SECRETKEY')    
    token = os.environ.get('TENCENTCLOUD_SESSIONTOKEN') 
    cosClient = CosS3Client(CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key,Token=token))

    #判斷請求是否從API閘道傳遞
    if "body" in event.keys():
        name = event['body']
        logger.info (str(len(name.decode('utf-8'))))
        logger.info ('name: '+ name)
        #判斷加入文字的長度
        if len(name.decode('utf-8')) > 15:
            return {
                "isBase64Encoded": False,"statusCode": 420,"headers": {"Content-Type": "text", "Access-Control-Allow-Origin": "*"},"body": "Error: Name is too long!"
            }
    else:
        return {
                "isBase64Encoded": False,"statusCode": 410,"headers": {"Content-Type": "text", "Access-Control-Allow-Origin": "*"},"body": "Error: Name is null"
            }

    #  原圖到tmp目錄，并且賦予權限,tmp是雲函數的本地磁盤空間，可讀可寫
    upload_path = '/tmp/邀請函-%s-ServerlessDays.jpg'% name
    logger.info('upload_path: '+ upload_path)

    #打開圖片
    img = Image.open("/tmp/source.jpg")
    logger.info('img.width: ' + str(img.width))
    logger.info('img.height: ' + str(img.height))

    # 添加常規字體
    logger.info('add_txt')
    #如果字元長度小於等于5，采用PIL庫添加字體
    if len(name.decode('utf-8')) <= 5:
        font_pil = ImageFont.truetype("./STXINWEI.TTF", 90)
        draw = ImageDraw.Draw(img)
        width = (img.width - len(name.decode('utf-8'))*90)/2
        height = (img.height)/2 - 90
        logger.info('width: ' + str(width))
        logger.info('height: ' + str(height))
        draw.text( (width,height), name.decode('utf-8'), font = font_pil, fill=(255,255,255))
        img.save(upload_path)
    #如果字元長度大于5，采用pygame給字體加格式，生成圖片後加浮水印的方式合成新的邀請函
    else:
        # pygame初始化，生成加粗+斜體的浮水印圖片
        pygame.init()
        # 設置字體和字号，自定義
        font = pygame.font.Font('./STXINWEI.TTF', 90)
        font.set_bold(True)
        font.set_italic(True) 
        ftext = font.render(name.decode('utf-8'), True,  (255,255,255))
        pygame.image.save(ftext, "/tmp/image.png")  # 圖片保存網址
        # 添加圖片浮水印
        mark = Image.open("/tmp/image.png")
        layer = Image.new('RGBA', img.size, (0,0,0,0))
        print('mark.width: ', mark.width)
        print('mark.height: ', mark.height)
        width = (img.width - mark.width)/2
        height = (img.height)/2-mark.height-10
        layer.paste(mark.rotate(5, expand=1), (width,height))
        out = Image.composite(layer,img,layer)
        out.save(upload_path)
    
    # 上傳圖片到COS
    logger.info('upload to cos')
    cosClient.put_object_from_local_file(
        Bucket=target_bucket,
        LocalFilePath=upload_path,
        Key= target_path+'/'+ upload_path.split('/')[-1]
    )
    delete_local_file("/tmp/image.png") 
    delete_local_file(upload_path)   
    Key = target_path+'/'+ upload_path.split('/')[-1]
    #返回COS下載網址
    download_path = 'https://'+ target_bucket +'.cos.'+ region + '.myqcloud.com'+ Key
    logger.info('cos download_path: '+ download_path)
    
    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "text", "Access-Control-Allow-Origin": "*"},
        "body": download_path
    }

    return response