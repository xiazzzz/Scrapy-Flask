import uuid

from flask import Blueprint, request,render_template
from .models import *
from sqlalchemy import and_,not_,or_

blue = Blueprint('user',__name__)

@blue.route('/')
def home():
    return 'wwwww'


#单表操作 增加
@blue.route('/useradd/')
def user_add():
    #添加一条数据
    # u = User()
    # u.name = 'ikun'
    # u.age=24
    # db.session.add(u) #将u对象添加session
    # db.session.commit() #同步到数据库中
    # 添加多条数据
    user = []
    for i in range(10, 30):
        u = User()
        u.name='夏夏' + str(i)
        u.age= i
        user.append(u)
    try:
        db.session.add_all(user)
        db.session.commit()  #事务提交
    except Exception as e:
        db.session.rollback() #回滚  如果事务未完成，全部返回
        db.session.flush()  #清空缓存
        return 'fail' +str(e)

    return 'success!'


#删除
@blue.route('/userdel/')
def user_delete():
    u = User.query.first() #查询第一条数据

    db.session.delete(u)
    db.session.commit()
    return 'success!'

#修改
@blue.route('/userupdate/')
def user_updata():
    u = User.query.first()
    u.age = 100
    db.session.commit()
    return 'success'


@blue.route('/userget/')
def user_get():
    users = User.query.all()
    # print(users)      #list  <class 'flask_sqlalchemy.query.Query'>
    # print(User.query) #

    users = User.query.filter()  #过滤   sql中的where
    # print(users, type(users))   #  查询集 <class 'flask_sqlalchemy.query.Query'>
    # print(list(users))

    #get()
    # user = User.query.get(8)
    # print(user,type(user))
    # print(user.name,user.age,user.sex,user.salary)


    #filter() #sql中的where
    #filter_by() 用于等值操作的过滤
    # users = User.query.filter(User.sex==1)
    # users = User.query.filter_by(sex=1)  #等价上面 只能等值操作
    # users = User.query.filter(User.age>=20)
    # print(list(users))

    #first() 第一条数据
    #first_or_404()  如果不存在第一条就404
    user = User.query.first()
    # user = User.query.filter_by(age=120).first_or_404()  #返回404
    # print(user)

    #count()  查询条数
    # users = User.query.filter()
    # print(users.count())

    #limit() 前几条
    #offset() 跳过前几条
    # users = User.query.offset(3).limit(4)
    # print(list(users))

    # order_by() 排序
    # users = User.query.order_by('age')   #升序   降序使用desc
    # print(list(users))

    # and_ or_ not_
    # users = User.query.filter(User.age>20,User.age<25)  #且
    # users = User.query.filter(and_(User.age > 20, User.age < 25))
    # print(list(users))

    # 查询属性
    users = User.query.filter(User.name.contains('3'))  #模糊查找

    users = User.query.filter(User.age.in_([10,13,15]))   # 包含
    users = User.query.filter(User.name.startswith('夏夏1'))  #开头
    users = User.query.filter(User.name.endswith('1'))  #结尾
    users = User.query.filter(User.age.__gt__(25))  # 结尾
    print(list(users))
    return 'success'

@blue.route('/paginate/',methods=['GET','POST'])
def get_paginate():
    page = int(request.args.get('page',1))
    per_page = int(request.args.get('per_page',5))    #设置每页为5
    # print(page,type(page))
    # print(per_page,type(per_page))

    p = User.query.paginate(
        page=page,per_page=per_page,error_out=False
    )           #分页操作
    print(p.items)    #当前数据

    # has_next:是否还有下一页
    # print(p.has_next)
    # has_prev 是否还有上一页
    # print(p.has_prev)
    #next(error_out=False)  返回下一页的pagination
    # print(p.next(error_out=False).page)  #下一页的对象

    print(p.page)  #当前页码
    print(p.pages) #总页数
    print(p.per_page) #每页数量
    print(p.prev_num) #上一页页码数      next_num
    print(p.total)   #查询返回的记录总数


    return render_template('paginate.html',p=p)


