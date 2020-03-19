from datetime import datetime

from flask import Flask, render_template, session, redirect, url_for, flash
from app import modules, extenstions

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app.modules.auth.models import User
from app.extenstions.sql_conn import db
# from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'efgrsfewgewSSl'

# migrate = Migrate(app, db)


class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data, role_id=1)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/hello')
def hello_world():
    return render_template('user.html', name='eddie')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


extenstions.init_app(app)
modules.init_app(app)