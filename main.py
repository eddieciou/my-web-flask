# import os
# from flask import Flask
# from app import modules
#
# app = Flask(__name__)
# modules.init_app(app)


import os

from flask import Flask, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy


db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pass}@/{db_name}' \
    f'?unix_socket=/cloudsql/{cloud_sql_connection_name}'

db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        aa = 'init'
        # sql_cmd = """
        #     select *
        #     from users
        #     """
        try:
            aa = User.query.filter_by(username='eddieciou').first()
        except Exception as e:
            return Response(
                status=500,
                response=f'RRR {e} , {aa}'
            )
        if request.method == 'GET':
            try:
                return render_template('login.html', data=aa)
            except Exception as e:
                return Response(
                    status=500,
                    response=f'RRR {e} , {aa}'
                )

        return render_template('login.html')
    except Exception as e:
        return Response(
            status=500,
            response=f'RRR {e} , {aa}'
        )


if __name__ == '__main__':
    app.run()
