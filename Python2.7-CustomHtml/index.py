#!/usr/bin/env python
# -*- coding:utf-8 -*-

def render_template(html, keys={}):
    for k, v in keys.iteritems():
        html = html.replace("${" + k + "}", v)
    return html

def main_handler(event, context):
    f = open("./demo.html")
    html = f.read()
    keys = {
        "master": "腾讯云云函数团队", # 您的名称
        "centralCouplet": "年年有余", # 横批
        "upCouplet": "千年迎新春", # 上联
        "downCouplet": "瑞雪兆丰年" # 下联
    }
    html = render_template(html, keys)
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": html
    }