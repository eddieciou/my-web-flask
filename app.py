import logging
from flask import Flask, request, g
from routes.Web import web
from config import setting
from config.logging import RequestFormatter
from commons.AuthToken import AuthToken
from model.Users import Users
from controller.Response import response

# Customize Logging Setting 只在main 加載,避免 不同Service 的 logging 互相影響
formatter = RequestFormatter(
    '[%(uuid)s] - %(asctime)s - (%(process)d-%(thread)d) - %(name)s[%(levelname)s] - %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(sh)


app = Flask(__name__)
app.register_blueprint(web, url_prefix='/web_api')


@app.before_request
def before_request():
    logger.info('before_request')

    environ = request.headers.environ
    logger.info('Header')
    logger.debug(environ)
    request_path = environ['PATH_INFO']
    logging.debug(request_path)

    if request_path in setting.VerifyExceptionPaths:
        return

    user_id = request.headers.get('user_id', None)
    jwt_token = request.headers.get('Authorization', None)

    logger.info(f'jwt_token: {jwt_token}')
    logger.info(f'user_id: {user_id}')

    auth = AuthToken.verify_token(jwt_token)
    if auth:
        user_info = Users().get_user_info(user_id)

        g.user = user_info
        g.user_id = user_id
        g.jwt_token = jwt_token

        return
    else:
        return response(999, 'token 失效')


# migrate = Migrate(app, db)


@app.route('/')
def index():
    return 'Croxera Reservation API Server with mongo'


if __name__ == '__main__':
    app.run(debug=True)
