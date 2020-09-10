# -*- coding: utf8 -*-
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import logging
import json
import requests
from email.mime.text import MIMEText
from email.header import Header
import smtplib

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Third-party SMTP service for sending alert emails. 第三方 SMTP 服務，用于發送告警郵件
mail_host = "smtp.qq.com"       # SMTP server, such as QQ mailbox, need to open SMTP service in the account. SMTP服務器,如QQ電子信箱，需要在帳戶裏開啓SMTP服務
mail_user = "XXXXXXXXX@qq.com"  # Username 用戶名
mail_pass = "****************"  # Password, SMTP service password. 密碼，SMTP服務密碼
mail_port = 465  # SMTP service port. SMTP服務端口

# The URL address need to dial test. 需要撥測的URL網址
test_url_list = [
    "http://www.baidu.com",
    "http://www.qq.com",
    "http://wrong.tencent.com",
    "http://unkownurl.com"
]

# The notification list of alert emails. 告警郵件通知清單
email_notify_list = {
    "XXXXXXXXX@qq.com",
    "XXXXXXXXX@qq.com"
}


def sendEmail(fromAddr, toAddr, subject, content):
    sender = fromAddr
    receivers = [toAddr]
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(fromAddr, 'utf-8')
    message['To'] = Header(toAddr, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("send email success")
        return True
    except smtplib.SMTPException as e:
        print(e)
        print("Error: send email fail")
        return False


def test_url(url_list):
    errorinfo = []
    for url in url_list:
        resp = None
        try:
            resp = requests.get(url, timeout=3)
            print (resp)
        except (
        requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout) as e:
            logger.warn("request exceptions:" + str(e))
            errorinfo.append("Access " + url + " timeout")
        else:
            if resp.status_code >= 400:
                logger.warn("response status code fail:" + str(resp.status_code))
                errorinfo.append("Access " + url + " fail, status code:" + str(resp.status_code))
    if len(errorinfo) != 0:
        body = "\r\n".join(errorinfo)
        subject = "Please note: PlayCheck Error"
        for toAddr in email_notify_list:
            print ("send message [%s] to [%s]" % (body, toAddr))
            sendEmail(mail_user, toAddr, subject, body)


def main_handler(event, context):
    test_url(test_url_list)


if __name__ == '__main__':
    main_handler("", "")