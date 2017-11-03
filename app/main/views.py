from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Role,Post

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home'

    posts = Post.get_posts()

    return render_template('index.html', title = title, posts=posts )





   

