# -*- coding: utf-8 -*-


def main_handler(event, context):
    """Clear the current session, including the stored user id."""

    response_headers = {
        "Set-Cookie": "sessionUUID=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/",
        'Location': '?function=indexes'
    }

    return {
        "isBase64Encoded": False,
        "statusCode": 302,
        "headers": response_headers,
    }

