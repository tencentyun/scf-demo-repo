# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader, select_autoescape
from db import get_db
from urllib import parse


env = Environment(
    loader = FileSystemLoader(['templates']),
    autoescape=select_autoescape(['html'])
)

def read_session_UUID(cookie):
    x = cookie.find('sessionUUID=')
    if x != -1:
        b = cookie[x + 12:x + 48]
    else:
        b = None
    return b

def load_logged_in_user(sessionUUID):
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
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

def get_post(id):
    db = get_db()

    with db.cursor() as cursor:
        # Read a single record
        sql = "SELECT p.id, title, body, created, author_id, username"\
              " FROM `post` p JOIN `user` u ON p.author_id = u.id"\
              " WHERE p.id = %s"
        cursor.execute(sql, (id,))
        post = cursor.fetchone()

    return post

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
        sessionUUID = read_session_UUID(cookie)
    else:
        sessionUUID = None

    if sessionUUID:
        user = load_logged_in_user(sessionUUID)
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

    id = event['queryString']['id']

    post = get_post(id)

    if post == None:
        statusCode = 404
    elif post["author_id"] != data['user']["id"]:
        statusCode = 403
    else:
        statusCode = 200



    if event['httpMethod'] == "POST":

        requestForm = parse.parse_qs(event['body'])


        title = requestForm["title"][0]
        body = requestForm["body"][0]


        if error is None:
            # the name is available, store it in the database and go to
            # the login page
            with db.cursor() as cursor:
                # Create a new record
                sql = "UPDATE `post` SET `title` = %s, `body` = %s WHERE (`id` = %s)"
                cursor.execute(sql, (title, body, id))

            db.commit()
            return {
                "isBase64Encoded": False,
                "statusCode": 302,
                "headers": {'Location': '?function=indexes'},
            }
        else:
            flashed_messages.append(error)

    if statusCode == 404:
        return {
            "isBase64Encoded": False,
            "statusCode": 404,
            "headers": {'Content-Type': 'text/html'},
            "body": '404 NOT FOUND'
        }
    elif statusCode == 403:
        return {
            "isBase64Encoded": False,
            "statusCode": 403,
            "headers": {'Content-Type': 'text/html'},
            "body": '403 forbidden'
        }
    elif statusCode == 200:
        template = env.get_template('blog/update.html')
        response_body = template.render(data=data, request={'form': None}, flashed_messages=flashed_messages, post=post)
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {'Content-Type': 'text/html'},
            "body": response_body
        }
    else:
        return {
            "isBase64Encoded": False,
            "statusCode": 403,
            "headers": {'Content-Type': 'text/html'},
            "body": '403 forbidden'
        }
