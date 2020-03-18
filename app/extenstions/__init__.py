from . import sql_conn


def init_app(app):
    sql_conn.init_app(app)
