import datetime

from flask import Blueprint, render_template, request, redirect, session

blue = Blueprint('user',__name__)

@blue.route('/')
@blue.route('/home/')
def home():
    #获取cookie
    # username = request.cookies.get('user')
    username = session.get('user')
    print(username)

    return render_template('home.html', username=username)

@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    elif request.method == 'POST':
        #1 、 获取前端数据
        username = request.form.get('username')
        password = request.form.get('password')

        # 2、模拟登录
        if username =='xiatian' and password=='123456':
            response = redirect('/home/')
            #3、设置cookie no中文
            #过期方式:max_age 秒   expires 日期
            # response.set_cookie('user',username,expires=datetime.datetime(2024,8,1))
            session['user'] = username
            session.permanent = True
            return response

        else:
            return "用户名错误"
 #注销
@blue.route('/logout/')
def logout():
    #5.注销cookie
    response = redirect('/')
    # response.delete_cookie('user')
    session.pop('user')
    return response

