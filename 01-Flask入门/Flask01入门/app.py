from flask import Flask,request,render_template
from datetime import datetime

app = Flask(__name__)

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email
def datatime_format(value,format="%Y-%m-%d %H:%M:%S"):
    return value.strftime(format)
app.add_template_filter(datatime_format,'dformat')



#创建一个路由和视图函数的映射
@app.route('/')
def hello_world():  # put application's code here
    user = User('张飞','876197093@qq.com')
    person = {
        "username":'张飞',
        "email":'222151@qq.com'
    }

    return render_template('index.html',user = user,person=person)

#过滤器的使用
@app.route('/filter')
def filter_demo():
    user = User('张飞xxx','876197093@qq.com')
    mytime = datetime.now()
    return render_template('filter.html',user=user,mytime=mytime)

#控制语句
@app.route('/control')
def control1():
    age = 19
    books = [{
        'name':'三国演义',
        'author':'罗贯中'
},{
        'name':'水浒传',
        'author':'施耐庵'
    }
    ]
    return  render_template('control.html',age=age,books=books)


@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template('blog_detail.html',blog_id=blog_id,usrname="知了")


@app.route('/child1')
def child1():
    return render_template('child1.html')

@app.route('/child2')
def child2():
    return render_template('child2.html')


# @app.route('/blog/<blog_id>')
# def blog(blog_id):
#     return '我是谁:{}'.format(blog_id)

#查询字符串的方式传
#/book/list？page=2：获取第二页数据
@app.route('/book/list')
def book_list():
    page = request.args.get('page',default=1,type=int)
    return f'你获取的是第{page}的图书列表！'





if __name__ == '__main__':
    app.run(debug=True)
