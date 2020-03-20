from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('帳號 :&nbsp', validators=[DataRequired()])
    password = PasswordField('密碼 :&nbsp', validators=[DataRequired()])
