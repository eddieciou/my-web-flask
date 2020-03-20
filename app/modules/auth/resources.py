from flask_restful import Resource
from flask import render_template, make_response, redirect, url_for, flash
from flask_login import login_user
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
            return redirect(url_for('index'))
        flash('登入失敗，請檢查帳號與密碼')
        return make_response(render_template('login.html', form=form))