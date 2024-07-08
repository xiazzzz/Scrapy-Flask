from .exts import db

class Author(db.Model):

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  #C 字段 In 整数
    name =db.Column(db.String(30))   #唯一约束  普通索引
    age =db.Column(db.Integer,default=1)
    sex = db.Column(db.Boolean,default=True)
    email = db.Column(db.String(200))

    books = db.relationship('Book',backref='auther',lazy='dynamic')

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  #C 字段 In 整数
    title =db.Column(db.String(100),unique=True)   #唯一约束  普通索引
    date =db.Column(db.DateTime)
    #多的一端写外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))


book_publisher = db.Table(
    'book_publisher',
    db.Column('book_id',db.Integer,db.ForeignKey('book.id'),primary_key=True),
    db.Column('publisher_id',db.Integer,db.ForeignKey('publisher.id'),primary_key=True),
)

class Publisher(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  #C 字段 In 整数
    name =db.Column(db.String(20),unique=True)   #唯一约束
    address =db.Column(db.String(200))
    city = db.Column(db.String(100))
    province = db.Column(db.String(100))
    country = db.Column(db.String(100))
    website = db.Column(db.String(100))
    #多的一端写外键
    books = db.relationship('Book',backref='publishers',
                            secondary=book_publisher,
                            lazy='dynamic')