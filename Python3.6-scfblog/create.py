# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader, select_autoescape
from db import get_db
from urllib import parse


env = Environment(
    loader = FileSystemLoader(['templates']),
    autoescape=select_autoescape(['html'])
)

def load_logged_in_user(cookie):
    """If a user id is stored in the session, load the user object from
    the database into ``data.user``."""

    x = cookie.find('sessionUUID=')
    if x != -1:
        sessionUUID = cookie[x + 12:x + 48]
    else:
        sessionUUID = None

    db = get_db()

    if sessionUUID is None:
        user = None
    else:
        with db.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `user` WHERE `sessionUUID4`=%s"
            cursor.execute(sql, (sessionUUID,))
            user = cursor.fetchone()

    return user




def main_handler(event, context):
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    flashed_messages = []
    error = None
    db = get_db()

    try:
        cookie = event['headers']['cookie']
    except:
        cookie = None

    if cookie:
        user = load_logged_in_user(cookie)
    else:
        user = None

    if user:
        logged = True
    else:
        logged = False

    data = {
        'logged': logged,
        'user': user
    }

    if event['httpMethod'] == "POST":

        requestForm = parse.parse_qs(event['body'])


        title = requestForm["title"][0]
        body = requestForm["body"][0]


        if error is None:
            # the name is available, store it in the database and go to
            # the login page
            with db.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `post` (`title`, `body`, `author_id`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (title, body, user['id']))

            db.commit()
            return {
                "isBase64Encoded": False,
                "statusCode": 302,
                "headers": {'Location': '?function=indexes'},
            }
        else:
            flashed_messages.append(error)

    template = env.get_template('blog/create.html')
    response_body = template.render(data=data, request={'form': None}, flashed_messages=flashed_messages)
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": response_body
    }
