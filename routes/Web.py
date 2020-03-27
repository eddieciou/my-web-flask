from flask import Blueprint
from controller.Auth import Auth

web = Blueprint('web', __name__)

web.add_url_rule('/login', view_func=Auth().login, methods=('POST',))
web.add_url_rule('/hello', view_func=Auth().hello, methods=('GET',))
