from flask import make_response


def response(code=0, msg=None, data=None):
    data = {
        "header": {
            "status": code,
            "msg": msg
        },
        "body": data
    }
    r = make_response(data)

    r.headers['Content-Type'] = 'application/json; charset=utf-8'
    return r
