# -*- coding: utf-8 -*-
import os

host = os.environ.get('MYSQL_HOST')
port = int(os.environ.get('MYSQL_PORT'))
user = os.environ.get('MYSQL_USER')
pas = os.environ.get('MYSQL_PASS')
db = os.environ.get('MYSQL_DB')


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





