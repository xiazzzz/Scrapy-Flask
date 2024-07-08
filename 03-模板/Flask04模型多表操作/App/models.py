from .exts import db

class Grade(db.Model):

    __tablename__ = 'grade'  #表名
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  #C 字段 In 整数
    name =db.Column(db.String(30),unique=True)

    #建立关联 第一个参数：class id
    #第二个参数 反向引用的参数,grade对象,  Student.grade
    #懒加载，调用才建立关系
    students = db.relationship('Student',backref='grade',lazy=True)


class Student(db.Model):

    __tablename__ = 'student'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30),unique=True,)
    age = db.Column(db.Integer)
    #外键 与Grade表ID字段关联
    gradeid = db.Column(db.Integer,db.ForeignKey(Grade.id))



#多对多
# 用户:电影= N:M

#中间表
collect = db.Table(
    'collects',
    db.Column('user_id',db.Integer,db.ForeignKey('usermodel.id'),primary_key=True),
    db.Column('movie_id',db.Integer,db.ForeignKey('movie.id'),primary_key=True),
)

class UserModel(db.Model):
    __tablename__ = 'usermodel'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30),unique=True)
    age = db.Column(db.Integer)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))
    users = db.relationship('UserModel',backref='movies',lazy='dynamic',secondary=collect)   #Movie.users得到 UserModel参数   UerModel.movies 等于调用movie