from datetime import datetime

from flask import Flask, render_template, session, redirect, url_for, flash
from app import modules, extenstions

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'efgrsfewgewSSl'


class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


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


if __name__ == '__main__':
    app.run()
