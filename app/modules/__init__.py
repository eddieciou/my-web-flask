import os
import json
import logging

from . import auth
from flask_restful import Api
from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

db = SQLAlchemy()


def init_app(app):
    blueprint = Blueprint('web', __name__)
    # api = Api(
    #     blueprint,
    #     version='0.0.1',
    #     title='Croxera Console',
    #     description='Restful API used for Croxera Console web',
    # )
    # app.register_blueprint(blueprint, url_prefix='/v1')
    app.register_blueprint(blueprint, url_prefix='/v1')
    api = Api(app)
    auth.register_resources(api)

    @app.before_request
    def do_before_request():
        logging.info("Headers: %s", request.headers)
        if request.method == "POST":
            logging.info("Body: %s", request.get_data())

    @app.after_request
    def do_after_request(response):
        logging.info(json.dumps(response.json))
        return response

