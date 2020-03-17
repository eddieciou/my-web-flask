import os
from flask import Flask
from app import modules

app = Flask(__name__)
modules.init_app(app)


# import os
#
# from flask import Flask, render_template, request, Response
# from flask_sqlalchemy import SQLAlchemy
#
#
# db_user = os.environ.get("DB_USER")
# db_pass = os.environ.get("DB_PASS")
# db_name = os.environ.get("DB_NAME")
# cloud_sql_connection_name = os.environ.get("CLOUD_SQL_CONNECTION_NAME")
#
# db = SQLAlchemy()
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pass}@/{db_name}' \
#     f'?unix_socket=/cloudsql/{cloud_sql_connection_name}'
#
# db.init_app(app)
#
#
# # db = sqlalchemy.create_engine(
# #     sqlalchemy.engine.url.URL(
# #         drivername="mysql+pymysql",
# #         username=db_user,
# #         password=db_pass,
# #         database=db_name,
# #         query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
# #     ),
# #     pool_size=5,
# #     max_overflow=2,
# #     pool_timeout=30,
# #     pool_recycle=1800,
# # )
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     try:
#         aa = 'init'
#         sql_cmd = """
#             select *
#             from users
#             """
#         try:
#             aa = db.engine.execute(sql_cmd)
#         except Exception as e:
#             return Response(
#                 status=500,
#                 response=f'RRR {e} , {aa}'
#             )
#         if request.method == 'GET':
#             try:
#                 return render_template('login.html', data=aa)
#             except Exception as e:
#                 return Response(
#                     status=500,
#                     response=f'RRR {e} , {aa}'
#                 )
#
#         return render_template('login.html')
#     except Exception as e:
#         return Response(
#             status=500,
#             response=f'RRR {e} , {aa}'
#         )


if __name__ == '__main__':
    app.run(host=os.getenv("HOST"))
