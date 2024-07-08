import random

from flask import Blueprint
from .models import *
blue = Blueprint('user',__name__)

@blue.route('/')
def home():
    return 'index'

@blue.route('/addgrade/')
def add_grade():
    #添加班级
    grades = []
    for i in range(10):
        grade = Grade()
        grade.name = f'Jay{i}-{str(random.randint(10,99))}'
        grades.append(grade)
    try:
        db.session.add_all(grades)
        db.session.commit()
    except Exception as e :
        print('e:',e)
        db.session.rollback()
        db.session.flush()
    return 'OK'


@blue.route('/addstu/')
def add_stu():
    #添加班级
    students = []
    for i in range(10,20):
        stu = Student()
        stu.name = f'Lucy{i}'
        stu.age = i
        stu.gradeid = random.randint(2,3)
        students.append(stu)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e :
        print('e:',e)
        db.session.rollback()
        db.session.flush()
    return 'OK'

#修改
@blue.route('/updatestu/')
def update_stu():
    stu = Student.query.first()
    stu.age = 100
    db.session.commit()
    return 'ok'
#删除
@blue.route('/delstu/')
def del_stu():
    stu = Student.query.first()
    db.session.delete(stu)
    db.session.commit()
    return 'ok'

#查询
@blue.route('/getstu/')
def get_stu():
    stu = Student.query.get(4)
    print(stu.name,stu.age)
    print(stu.gradeid,stu.grade,stu.grade.name,stu.grade.id)

    grade = Grade.query.get(3)
    print(grade.name)
    print(grade)
    print(grade.students)

    return 'ok'


#------------多对多
@blue.route('/adduser/')
def add_user():
    #添加班级
    users = []
    for i in range(10,14):
        user = UserModel()
        user.name = f'Jay{i}'
        user.age = i
        users.append(user)
    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e :
        print('e:',e)
        db.session.rollback()
        db.session.flush()
    return 'OK'

@blue.route('/addmovie/')
def add_movie():
    #添加班级
    movies = []
    for i in range(10,14):
        movie = Movie()
        movie.name = f'阿凡达-{i}'
        movies.append(movie)
    try:
        db.session.add_all(movies)
        db.session.commit()
    except Exception as e :
        print('e:',e)
        db.session.rollback()
        db.session.flush()
    return 'OK'

@blue.route('/addcollect/')
def add_collect():

    user = UserModel.query.get(1)
    movie = Movie.query.get(1)
    user.movies.append(movie)
    db.session.commit()

    return 'OK'

@blue.route('/getcollect/')
def get_collect():
    user = UserModel.query.get(2)
    print(user.movies)

    movie = Movie.query.get(3)
    print(list(movie.users))

    return 'OK'

@blue.route('/deluser/')
def del_user():
    user= UserModel.query.get(1)
    db.session.delete(user)
    db.session.commit()
    return 'OK'
