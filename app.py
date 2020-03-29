import logging

import extenstions

from flask import Flask

from routes import Mobile, Web
from config.logging import RequestFormatter


# Customize Logging Setting 只在main 加載,避免 不同Service 的 logging 互相影響
formatter = RequestFormatter(
    '[%(uuid)s] - %(asctime)s - (%(process)d-%(thread)d) - %(name)s[%(levelname)s] - %(message)s'
)
sh = logging.StreamHandler()
sh.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(sh)


app = Flask(__name__)

extenstions.init_app(app)
Web.register_blueprint(app)
Mobile.register_blueprint(app)


@app.route('/')
def index():
    return 'Croxera Reservation API Server'


if __name__ == '__main__':
    app.run()
