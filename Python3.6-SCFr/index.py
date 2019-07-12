# -*- coding: utf-8 -*-

host = '数据库地址'
port = 数据库端口
user = '数据库用户名'
pas = '数据库用户密码'
db = '数据库名'



def main_handler(event, context):

    try:
        function = event['queryString']['function']
    except:
        function = None

    if function == 'style':
        from style import main_handler
        return main_handler(event, None)

    if function == 'register':
        from register import main_handler
        return main_handler(event, None)

    if function == 'login':
        from login import main_handler
        return main_handler(event, None)

    if function == 'logout':
        from logout import main_handler
        return main_handler(event, None)

    if function == 'indexes':
        from indexes import main_handler
        return main_handler(event, None)

    if function == 'create':
        from create import main_handler
        return main_handler(event, None)

    if function == 'update':
        from update import main_handler
        return main_handler(event, None)

    if function == 'delete':
        from delete import main_handler
        return main_handler(event, None)

    if function == None:
        from indexes import main_handler
        return main_handler(event, None)





