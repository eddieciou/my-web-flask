from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from .models import User


class LoginForm(FlaskForm):
    username = StringField('帳號 :&nbsp', validators=[DataRequired()])
    password = PasswordField('密碼 :&nbsp', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('輸入帳號:', validators=[
        DataRequired(),
        Length(1, 2),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('輸入密碼:', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('確認密碼:', validators=[DataRequired()])

    # 自訂驗證函式
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
