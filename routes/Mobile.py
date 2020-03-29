import logging
from flask import Blueprint
from controller.mobile.MobileRequest import MobileRequest

logger = logging.getLogger(__name__)
mobile = Blueprint('mobile', __name__)

mobile.add_url_rule('/mobile_request', view_func=MobileRequest().mobile_request, methods=('GET',))


def register_blueprint(app):
    app.register_blueprint(mobile, url_prefix='/mobile_api')


@mobile.before_request
def before_request():
    # 網頁API Before Request
    logger.info('before_request')
