from flask import Flask
from .views import *

def crate_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    return app