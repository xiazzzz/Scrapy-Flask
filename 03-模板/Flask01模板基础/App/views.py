
from flask import Blueprint
from .models import *
blue = Blueprint('user',__name__)

@blue.route('/')
def home():
    return 'wwwww'