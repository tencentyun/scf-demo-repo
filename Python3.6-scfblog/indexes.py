# -*- coding: utf-8 -*-
from jinja2 import Environment, FileSystemLoader, select_autoescape
from db import get_db

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
    """Show all the posts, most recent first."""
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

    with db.cursor() as cursor:
        # Read a single record
        sql = "SELECT p.id, title, body, created, author_id, username"\
              " FROM `post` p JOIN `user` u ON p.author_id = u.id"\
              " ORDER BY created DESC"

        cursor.execute(sql)
        posts = cursor.fetchall()

    template = env.get_template('blog/indexes.html')
    response_body = template.render(data=data, posts=posts, flashed_messages=flashed_messages)
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": response_body
    }
