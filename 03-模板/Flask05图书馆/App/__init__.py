from flask import Flask
from .views import *
from .exts import *

def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)

    # db_uri = 'sqlite:///sqlite3.db'
    db_uri = 'mysql+pymysql://root:123456@localhost:3306/bookdb'
    app.config['SQLALCHEMY_DATABASE_URI']=db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #禁止对象追踪修改

    init_exts(app=app)

    return app
