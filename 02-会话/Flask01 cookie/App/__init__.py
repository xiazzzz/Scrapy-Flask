from flask import Flask
from .views import *
import datetime
def create_app():
    app  = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    # print(app.config)
    app.config['SECRET_KEY'] = 'abc123'
    app.config["PERMANENT_SESSION_LIFETIME"] = datetime.timedelta(days=2)
    return app

