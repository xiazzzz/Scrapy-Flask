from .exts import db

class User(db.Model):

    __tablename__ = 'user'  #表名
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  #C 字段 In 整数
    name =db.Column(db.String(30),unique=True,index=True)   #唯一约束  普通索引
    age =db.Column(db.Integer,default=1)
    sex = db.Column(db.Boolean,default=True)
    salary = db.Column(db.Float, default=100000,nullable=False)


    def __repr__(self):
        return self.name