# -*- coding: utf-8 -*-
from db import get_db



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
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
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
        statusCode = 302



    if event['httpMethod'] == "POST":


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
        elif statusCode == 302:
            with db.cursor() as cursor:
                # Create a new record
                sql = "DELETE FROM `post` WHERE (`id` = %s)"
                cursor.execute(sql, (id,))

            db.commit()
            return {
                "isBase64Encoded": False,
                "statusCode": 302,
                "headers": {'Location': '?function=indexes'},
            }
        else:
            return {
                "isBase64Encoded": False,
                "statusCode": 403,
                "headers": {'Content-Type': 'text/html'},
                "body": '403 forbidden'
            }


