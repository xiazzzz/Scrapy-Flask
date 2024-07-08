
from flask import Blueprint,render_template


blue = Blueprint('user',__name__)

@blue.route('/')
def index():

    data = {
        'name':'ikun ikun',
        'age':8,
        'likes':['ball','sing','dance','code']
    }
    # return render_template('home.html',**data)
    return render_template('child2.html',**data)