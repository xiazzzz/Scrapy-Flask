
#路由+视图文件
from flask import Blueprint, request, render_template, jsonify, make_response, Response, redirect, url_for
from .models import *

#相当于一个机器分多个线
blue = Blueprint('user',__name__)

@blue.route('/',methods=['GET','POST'])
def index():
    return 'index'

@blue.route('/string/<string:name>')
def get_string(name):
    return name

#752158b5-a44e-4742-9f4e-3a83670e4710
@blue.route('/uuid/<uuid:id>')
def get_uuid(id):
    return str(id)

@blue.route('/get_uuid')
def get_uuid2():
    import uuid
    return str(uuid.uuid4())

#request 请求
@blue.route('/request/',methods=['GET','POST'])
def get_request():
    # print(request) #<Request 'http://127.0.0.1:5000/request' [GET]>
    print(request.method) #请求方法
    print(request.args)  #get请求参数  类字典对象 可以出现重复的KEY
    # print(request.args['name'],request.args['age'])
    # print(request.args.get('name'))
    # print(request.args.getlist('name'))

    print(request.form) # post 参数
    print(request.form.get('name'))
    # print(request.cookies)
    print(request.path)
    print(request.url)#http://127.0.0.1:5000/request/?name=xia&name=xu&age=16
    print(request.base_url)  #host+path  http://127.0.0.1:5000/request/
    print(request.host_url)  #http://127.0.0.1:5000/
    print(request.remote_addr)  #  127.0.0.1

    print(request.files)

    print(request.headers)  #请求头
    print(request.user_agent)  #用户代理，包含浏览器和操作信息

    return "request ok"

#response
@blue.route('/response/')
def get_response():
    pass
    # return 'response OK!'

    #模板渲染  前后端不分离
    # return render_template('index.html',name='张三',age=33)

    #分离，只返回字典数据, 序列化，字典=》字符串
    # data = {'name':'李四','age':44}
    # return jsonify(data)

    html = render_template('index.html',name='张三',age=33)
    # print(html,type(html))

    res= make_response(html,200)
    # res = Response(html)
    return res

# redirect:重定向
@blue.route('/redirect/')
def make_redirect():
    pass
    # return redirect('/uuid/<uuid:id>')

    # url_for ('蓝图名称.视图函数名') 反向解析 通过函数名找到路由
    ret = url_for('user.get_request',name='王五',age=21)
    print('ret:',ret)
    return redirect(ret)