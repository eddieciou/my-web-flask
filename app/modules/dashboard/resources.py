from flask_restful import Resource
from flask import render_template, make_response
from flask_login import login_required


class Dashboard(Resource):
    @login_required
    def get(self):
        return make_response(render_template('hello_world.html'))
