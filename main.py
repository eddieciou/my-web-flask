import os
import datetime

from flask import Flask, render_template, request, Response
import sqlalchemy


db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_name = os.environ.get("DB_NAME")
cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")

app = Flask(__name__)

db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=db_user,
        password=db_pass,
        database=db_name,
        query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800,
)


@app.route('/login', methods=['GET', 'POST'])
def login():
    stmt = sqlalchemy.text(
        "SELECT * FROM users"
    )
    try:
        with db.connect() as coon:
            aa = coon.execute(stmt)
    except Exception as e:
        return Response(
            status=500,
            response=f'RRR {e} , {aa}'
        )
    if request.method == 'GET':
        return render_template('login.html', data=aa[0])

    return render_template('login.html')


if __name__ == '__main__':
    app.run(host=os.getenv("HOST"))
