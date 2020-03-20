from . import sql_conn
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'login'


def init_app(app):
    login_manager.init_app(app)
    sql_conn.init_app(app)

