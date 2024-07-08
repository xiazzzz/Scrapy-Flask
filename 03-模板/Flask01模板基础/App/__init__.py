from flask import Flask
from .views import *
from .exts import *

def create_app():
    app = Flask(__name__)
    #注册蓝图
    app.register_blueprint(blueprint=blue)

    #配置数据库
    db_uri = 'sqlite:///sqlite3.db'
    app.config['SQLALCHEMY_DATABASE_URI']=db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #禁止对象追踪修改


    init_exts(app=app)

    return app
