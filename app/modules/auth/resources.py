from flask_restful import Resource
from flask import render_template, make_response
# from .models import User


class Login(Resource):
    def get(self):
        # try:
        #     # data = User.query.filter_by(username='eddieciou').first()
        #     return make_response(render_template('login.html', data=data))
        # except Exception as e:
        #     return {
        #         "error": f'{e}'
        #     }
        return make_response(render_template('login.html', data="dddd"))