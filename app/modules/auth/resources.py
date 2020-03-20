from flask_restful import Resource
from flask import render_template, make_response, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from .models import User
from .form import LoginForm


class Login(Resource):
    def get(self):
        form = LoginForm()
        return make_response(render_template('login.html', form=form))

    def post(self):
        form = LoginForm()
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            # login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('index')
            return redirect(next)
        flash('登入失敗，請檢查帳號與密碼')
        return make_response(render_template('login.html', form=form))


class Logout(Resource):
    def get(self):
        logout_user()
        flash('使用者已登出')
        form = LoginForm()
        return make_response(render_template('login.html', form=form))
