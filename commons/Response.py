from flask import make_response
from flask import jsonify


def response(code=0, msg=None, data=None, http_code: int = 200, **kwargs):
    """
    統一 api response 格式
    :param code:
    :param msg:
    :param data:
    :param http_code:
    :param kwargs:
    :return:
    """
    r_data = {
        "header": {
            "status": code,
            "msg": msg
        }
    }
    if data:
        r_data['body'] = data

    r = make_response(jsonify(r_data), http_code)

    #  kwargs 用來傳入額外header
    if kwargs.get("headers"):
        for k, v in kwargs.get("headers").items():
            r.headers[k] = v

    r.headers['Content-Type'] = 'application/json; charset=utf-8'
    return r