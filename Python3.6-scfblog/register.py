# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader, select_autoescape

from Crypto.Hash import SHA256
from urllib import parse
from db import get_db

env = Environment(
    loader = FileSystemLoader(['templates']),
    autoescape=select_autoescape(['html'])
)

def main_handler(event, context):
    print('event:\n', event, '\n###')
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
            sql = "SELECT `id` FROM `user` WHERE `username`=%s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            print(result)

        if result is not None:
            error = "User {0} is already registered.".format(username)

        if error is None:
            # the name is available, store it in the database and go to
            # the login page

            hash_SHA256 = SHA256.new()
            hash_SHA256.update(password.encode(encoding='utf-8'))
            password_hash = hash_SHA256.hexdigest()
            with db.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `user` (`username`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, (username, password_hash))

            db.commit()
            return {
                "isBase64Encoded": False,
                "statusCode": 302,
                "headers": {'Location': '?function=login'}
            }
        else:
            flashed_messages.append(error)

    template = env.get_template('auth/register.html')
    response_body = template.render(data={},flashed_messages=flashed_messages)

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {'Content-Type': 'text/html'},
        "body": response_body
    }
