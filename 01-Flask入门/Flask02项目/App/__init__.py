#初始化

# 不能其他文件绑定init文件， app只能出现一次
from flask import Flask
from .views import *


def create_app():
    app = Flask(__name__)

    #注册蓝图
    app.register_blueprint(blueprint=blue)
    return app
