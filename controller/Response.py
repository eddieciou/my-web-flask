from flask import make_response


def response(code=0, msg=None, data=None, **kwargs):
    data = {
        "header": {
            "status": code,
            "msg": msg
        },
        "body": data
    }
    r = make_response(data)

    # Token由header傳送
    if kwargs:
        for k, v in kwargs.items():
            r.headers[k] = v

    r.headers['Content-Type'] = 'application/json; charset=utf-8'
    return r
