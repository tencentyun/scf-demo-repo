# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader, select_autoescape

from db import get_db
from urllib import parse
from Crypto.Hash import SHA256
import uuid


env = Environment(
    loader = FileSystemLoader(['templates']),
    autoescape=select_autoescape(['html'])
)

def main_handler(event, context):
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    flashed_messages = []
    error = None

    if event['httpMethod'] == "POST":

        requestForm = parse.parse_qs(event['body'])

        username = requestForm["username"][0]
        password = requestForm["password"][0]

        db = get_db()

        with db.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `user` WHERE `username`=%s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()


        if user is None:
            error = "Incorrect username."

        hash_SHA256 = SHA256.new()
        hash_SHA256.update(password.encode(encoding='utf-8'))
        password_hash = hash_SHA256.hexdigest()

        if user["password"] != password_hash:
            error = "Incorrect password."


        if error is None:
            # the name is available, store it in the database and go to
            # the login page
            sessionUUID4 = str(uuid.uuid4())
            with db.cursor() as cursor:
                # Create a new record
                sql = "UPDATE `user` SET `sessionUUID4`=%s WHERE `username`=%s"
                cursor.execute(sql, (sessionUUID4, username))

            db.commit()
            response_headers = {
                "Set-Cookie": "sessionUUID=" + sessionUUID4 + "; Path=/",
                'Location': '?function=indexes'
            }

            return {
                "isBase64Encoded": False,
                "statusCode": 302,
                "headers": response_headers,
            }
        else:
            flashed_messages.append(error)


    template = env.get_template('auth/login.html')
    response_body = template.render(data={},flashed_messages=flashed_messages)

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": response_body
    }


