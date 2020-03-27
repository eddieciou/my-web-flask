from flask import Flask
from routes.Web import web

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eff2b5ea073d43e331ae0e77e44d2bb46b688d0489f701db'

app.register_blueprint(web, url_prefix='/web_api')

# migrate = Migrate(app, db)


@app.route('/')
def index():
    return 'Croxera Reservation API Server with mongo'


if __name__ == '__main__':
    app.run()
