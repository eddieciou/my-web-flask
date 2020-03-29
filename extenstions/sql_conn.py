import os

from flask_sqlalchemy import SQLAlchemy

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

db = SQLAlchemy()


def init_app(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:52duckli1314@127.0.0.1/my_web'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pass}@/{db_name}' \
        f'?unix_socket=/cloudsql/{cloud_sql_connection_name}'

    db.init_app(app)
