# import logging
from config import setting
from flask import Blueprint, request
from controller.web.Auth import Auth
from controller.web.Schedules import Schedules
from commons.AuthToken import AuthToken
from commons.Response import response

logger = logging.getLogger(__name__)
web = Blueprint('web', __name__)


# Auth
web.add_url_rule('/login', view_func=Auth().login, methods=('POST',))

# Schedules
web.add_url_rule('/get_schedules', view_func=Schedules().get_schedules, methods=('GET',))


def register_blueprint(app):
    app.register_blueprint(web, url_prefix='/web_api')


@web.before_request
def before_request():
    # 網頁API Before Request
    logger.info('before_request')

    environ = request.headers.environ
    logger.info('Header')
    logger.debug(environ)
    request_path = environ['PATH_INFO']
    logger.debug(request_path)

    if request_path in setting.VerifyExceptionPaths:
        return

    # 驗證Token
    user_id = request.headers.get('user_id', None)
    jwt_token = request.headers.get('Authorization', None)

    logger.info(f'jwt_token: {jwt_token}')
    logger.info(f'user_id: {user_id}')

    auth_token = AuthToken.verify_token(jwt_token)
    if auth_token:
        pass
    else:
        # token 驗證失敗,回傳http code 401
        return response(900, http_code=401)
